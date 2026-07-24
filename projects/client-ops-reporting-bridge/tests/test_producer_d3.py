"""Phase 1B-D3 gated live transport and confirmation gate tests (offline)."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

from support import PROJECT_ROOT, ExporterTestCase  # noqa: F401

from client_ops_reporting_bridge.cli import main
from client_ops_reporting_bridge.producer_config import parse_producer_profile
from client_ops_reporting_bridge.producer_constants import (
    D3_ENABLE_PHRASE,
    D3_PRODUCER_MARKER,
    D3_SEND_FIRST_PHRASE,
    D3_SEND_REPLAY_PHRASE,
    EXIT_NETWORK_NOT_AUTHORIZED,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
)
from client_ops_reporting_bridge.producer_d3 import (
    apply_d3_synthetic_markers,
    build_d3_synthetic_envelope,
)
from client_ops_reporting_bridge.producer_d3_gates import (
    D3GateError,
    assert_request_budget,
    build_authorization,
    load_charter_state,
    save_charter_state,
)
from client_ops_reporting_bridge.producer_http import (
    EndpointAllowlistError,
    LiveHttpTransport,
    create_d3_live_transport,
    validate_and_allow_endpoint,
)
from client_ops_reporting_bridge.producer_request import OutboundRequest
from client_ops_reporting_bridge.producer_transport import (
    NetworkDispatchNotAuthorized,
    create_transport,
)


def _run_cli(argv: list[str]) -> tuple[int, str, str]:
    buf_out = io.StringIO()
    buf_err = io.StringIO()
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        code = main(argv)
    return code, buf_out.getvalue(), buf_err.getvalue()


def _approved_profile(**overrides):
    raw = {
        "webhook_base": "https://n8n.ai-metacode.com",
        "webhook_route": "/webhook/client-ops-test-route",
        "request_timeout_ms": 30000,
        "connect_timeout_ms": 5000,
        "environment": "sandbox",
        "site_id": "SITE-002",
        "max_retries": 0,
        "concurrency": 1,
        "host_class": "n8n-client-ops",
    }
    raw.update(overrides)
    return parse_producer_profile(raw)


class TestD3EndpointAllowlist(unittest.TestCase):
    def test_approved_https(self) -> None:
        ep = validate_and_allow_endpoint(_approved_profile())
        self.assertEqual(ep.scheme, "https")
        self.assertTrue(ep.sanitized_dict()["host_approved"])
        self.assertNotIn("webhook_base", ep.sanitized_dict())

    def test_wrong_host_rejected(self) -> None:
        with self.assertRaises(EndpointAllowlistError):
            validate_and_allow_endpoint(
                _approved_profile(webhook_base="https://evil.example.com")
            )

    def test_http_scheme_rejected(self) -> None:
        with self.assertRaises(EndpointAllowlistError):
            validate_and_allow_endpoint(
                _approved_profile(webhook_base="http://n8n.ai-metacode.com")
            )

    def test_query_rejected(self) -> None:
        with self.assertRaises((EndpointAllowlistError, Exception)):
            # Profile parser rejects query; allowlist also rejects if reached
            try:
                validate_and_allow_endpoint(
                    _approved_profile(webhook_base="https://n8n.ai-metacode.com?x=1")
                )
            except Exception as exc:
                self.assertTrue(
                    "query" in str(exc).lower() or "fragment" in str(exc).lower()
                    or type(exc).__name__ in {"EndpointAllowlistError", "ProducerConfigError"}
                )
                raise

    def test_fragment_rejected(self) -> None:
        with self.assertRaises(Exception):
            validate_and_allow_endpoint(
                _approved_profile(webhook_base="https://n8n.ai-metacode.com#frag")
            )

    def test_localhost_rejected(self) -> None:
        with self.assertRaises(EndpointAllowlistError):
            validate_and_allow_endpoint(
                _approved_profile(webhook_base="https://localhost")
            )


class TestD3Gates(unittest.TestCase):
    def test_wrong_phrase_rejected(self) -> None:
        auth = build_authorization(
            enable_phrase="WRONG",
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_concurrency_rejected(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=2,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_max_retries_rejected(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=1,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_wrong_environment_rejected(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="production",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_dry_run_blocked_from_live(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=True,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_missing_marker_rejected(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=False,
            profile_present=True,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_third_request_budget(self) -> None:
        state = {
            "real_http_requests": 2,
            "first_seen_consumed": True,
            "exact_replay_consumed": True,
            "charter_consumed": True,
        }
        with self.assertRaises(D3GateError):
            assert_request_budget(state, mode="first_seen")


class TestD3TransportMocked(unittest.TestCase):
    def _auth(self):
        return build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )

    def test_mocked_https_accepted(self) -> None:
        profile = _approved_profile()
        endpoint = validate_and_allow_endpoint(profile)
        transport = LiveHttpTransport(
            endpoint=endpoint,
            auth_secret="test-secret-value-not-real",
            connect_timeout_s=5,
            read_timeout_s=10,
            authorization=self._auth(),
        )
        req = OutboundRequest(
            method="POST",
            host_class="n8n-client-ops",
            route_configured=True,
            content_type="application/json",
            auth_header_name="X-MARS-Client-Ops-Token",
            auth_header_present=True,
            body={"event_id": "e1", "schema_name": "mars.client_ops.report"},
            connect_timeout_ms=5000,
            request_timeout_ms=30000,
            headers_redacted={"X-MARS-Client-Ops-Token": "<redacted>"},
        )

        class FakeResp:
            status = 202

            def read(self, _n):
                return b'{"result":"ACCEPTED","dedupe_result":"FIRST_SEEN","event_id":"e1"}'

            def getcode(self):
                return 202

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        class FakeOpener:
            def open(self, request, timeout=None):
                # Ensure auth header present and secret not logged via transport
                self.last_headers = request.headers
                return FakeResp()

        with mock.patch(
            "client_ops_reporting_bridge.producer_http.urllib.request.build_opener",
            return_value=FakeOpener(),
        ):
            resp = transport.dispatch(req)
        self.assertEqual(resp.http_status, 202)
        self.assertEqual(resp.network_calls, 1)
        self.assertFalse(resp.simulated)
        self.assertEqual(transport.network_calls, 1)
        sanitized = json.dumps(resp.sanitized_dict())
        self.assertNotIn("test-secret-value-not-real", sanitized)

    def test_tls_verify_cannot_disable(self) -> None:
        profile = _approved_profile()
        endpoint = validate_and_allow_endpoint(profile)
        transport = LiveHttpTransport(
            endpoint=endpoint,
            auth_secret="x",
            connect_timeout_s=1,
            read_timeout_s=1,
            authorization=self._auth(),
            tls_verify=False,
        )
        req = OutboundRequest(
            method="POST",
            host_class="n8n-client-ops",
            route_configured=True,
            content_type="application/json",
            auth_header_name="X-MARS-Client-Ops-Token",
            auth_header_present=True,
            body={"event_id": "e1"},
            connect_timeout_ms=1000,
            request_timeout_ms=1000,
            headers_redacted={},
        )
        with self.assertRaises(D3GateError):
            transport.dispatch(req)

    def test_redirect_rejected(self) -> None:
        profile = _approved_profile()
        endpoint = validate_and_allow_endpoint(profile)
        transport = LiveHttpTransport(
            endpoint=endpoint,
            auth_secret="x",
            connect_timeout_s=1,
            read_timeout_s=1,
            authorization=self._auth(),
        )
        req = OutboundRequest(
            method="POST",
            host_class="n8n-client-ops",
            route_configured=True,
            content_type="application/json",
            auth_header_name="X-MARS-Client-Ops-Token",
            auth_header_present=True,
            body={"event_id": "e1"},
            connect_timeout_ms=1000,
            request_timeout_ms=1000,
            headers_redacted={},
        )

        class FakeOpener:
            def open(self, request, timeout=None):
                raise EndpointAllowlistError("redirects are not followed")

        with mock.patch(
            "client_ops_reporting_bridge.producer_http.urllib.request.build_opener",
            return_value=FakeOpener(),
        ):
            resp = transport.dispatch(req)
        self.assertFalse(resp.ok)
        self.assertEqual(resp.error_class, "UNEXPECTED_RESPONSE")


class TestD3CliAndGenericBlock(ExporterTestCase):
    def test_push_webhook_still_blocked(self) -> None:
        code, out, _ = _run_cli(["push-webhook", "--live", "--apply"])
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D2, out)

    def test_create_transport_http_still_blocked(self) -> None:
        with self.assertRaises(NetworkDispatchNotAuthorized):
            create_transport("http")

    def test_dry_run_never_network(self) -> None:
        code, out, _ = _run_cli(
            [
                "producer-d3-controlled-live",
                "--dry-run",
                "--mode",
                "first_seen",
            ]
        )
        payload = json.loads(out)
        self.assertEqual(payload["network_calls"], 0)
        self.assertFalse(payload.get("real_network", False))
        self.assertIn(payload["final_state"], {"D3_DRY_RUN_READY", "NOT_READY"})

    def test_live_without_phrase_blocked(self) -> None:
        code, out, _ = _run_cli(
            [
                "producer-d3-controlled-live",
                "--apply",
                "--mode",
                "first_seen",
                "--fixture",
                str(self.fixture("fixture-d3-synthetic-producer")),
                "--confirm-enable",
                "WRONG",
                "--confirm-send",
                D3_SEND_FIRST_PHRASE,
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D3, out)
        payload = json.loads(out)
        self.assertEqual(payload["network_calls"], 0)

    def test_producer_dry_run_still_offline(self) -> None:
        code, out, _ = _run_cli(
            [
                "producer-dry-run",
                "--fixture",
                str(self.fixture("fixture-ok")),
                "--transport",
                "mock",
                "--live",
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D2, out)


class TestD3SyntheticEvent(ExporterTestCase):
    def test_marker_and_event_id(self) -> None:
        env = build_d3_synthetic_envelope(
            self.fixture("fixture-d3-synthetic-producer")
        )
        self.assertEqual(env["producer"]["name"], D3_PRODUCER_MARKER)
        self.assertEqual(env["site"]["site_id"], "SITE-002")
        self.assertEqual(env["site"]["domain"], "bzpm.ru")
        self.assertEqual(env["event_type"], "site.post_1c_monitor")
        self.assertEqual(env["run"]["normalized_status"], "OK")
        self.assertTrue(env["event_id"])
        # event_id stable for same source
        env2 = build_d3_synthetic_envelope(
            self.fixture("fixture-d3-synthetic-producer")
        )
        self.assertEqual(env["event_id"], env2["event_id"])

    def test_marker_override_preserves_id(self) -> None:
        from client_ops_reporting_bridge.pipeline import process_fixture_dir

        proc = process_fixture_dir(
            self.fixture("fixture-d3-synthetic-producer"), build_envelope=True
        )
        marked = apply_d3_synthetic_markers(dict(proc.envelope))
        self.assertEqual(proc.envelope["event_id"], marked["event_id"])


class TestD3CharterState(unittest.TestCase):
    def test_budget_sequence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runs = Path(tmp)
            state = load_charter_state(runs)
            assert_request_budget(state, mode="first_seen")
            state["real_http_requests"] = 1
            state["first_seen_consumed"] = True
            save_charter_state(runs, state)
            state2 = load_charter_state(runs)
            assert_request_budget(state2, mode="exact_replay")
            state2["real_http_requests"] = 2
            state2["exact_replay_consumed"] = True
            state2["charter_consumed"] = True
            with self.assertRaises(D3GateError):
                assert_request_budget(state2, mode="exact_replay")


class TestMissingSecretAndProfile(unittest.TestCase):
    def test_missing_secret_gate(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=False,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_missing_profile_gate(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="first_seen",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=False,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()

    def test_replay_phrase_mismatch(self) -> None:
        auth = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_FIRST_PHRASE,
            mode="exact_replay",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )
        with self.assertRaises(D3GateError):
            auth.assert_live_allowed()
        auth_ok = build_authorization(
            enable_phrase=D3_ENABLE_PHRASE,
            send_phrase=D3_SEND_REPLAY_PHRASE,
            mode="exact_replay",
            apply=True,
            dry_run=False,
            environment="sandbox",
            concurrency=1,
            max_retries=0,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
        )
        auth_ok.assert_live_allowed()


if __name__ == "__main__":
    unittest.main()
