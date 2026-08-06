"""Phase 1B-D2 offline sequential runtime producer tests."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

from support import PROJECT_ROOT, ExporterTestCase  # noqa: F401 — sets sys.path

from client_ops_reporting_bridge.cli import main
from client_ops_reporting_bridge.constants import EXIT_SUCCESS
from client_ops_reporting_bridge.event_identity import compute_event_id
from client_ops_reporting_bridge.pipeline import process_fixture_dir
from client_ops_reporting_bridge.producer_classify import (
    classify_transport_response,
    plan_retry_attempt,
)
from client_ops_reporting_bridge.producer_config import (
    ProducerConfigError,
    offline_default_profile,
    parse_producer_profile,
)
from client_ops_reporting_bridge.producer_constants import (
    EXIT_CONCURRENCY_REJECTED,
    EXIT_NETWORK_NOT_AUTHORIZED,
    MOCK_FIXTURE_NAMES,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    RETRY_MANUAL_DEDUPE_CHECK_REQUIRED,
)
from client_ops_reporting_bridge.producer_dispatch_guard import (
    SequentialDispatchError,
    SequentialDispatchGuard,
    reset_default_guard_for_tests,
)
from client_ops_reporting_bridge.producer_evidence import (
    build_evidence_document,
    write_producer_evidence,
)
from client_ops_reporting_bridge.producer_firewall import (
    SourceFirewallError,
    extract_allowlisted_from_hostile,
    normalize_producer_input,
)
from client_ops_reporting_bridge.producer_pipeline import (
    build_retry_simulation,
    run_producer_offline,
)
from client_ops_reporting_bridge.producer_request import (
    assert_no_secret_leak,
    build_outbound_request,
)
from client_ops_reporting_bridge.producer_transport import (
    NetworkDispatchNotAuthorized,
    MockTransport,
    create_transport,
)

def _run_cli(argv: list[str]) -> tuple[int, str, str]:
    buf_out = io.StringIO()
    buf_err = io.StringIO()
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        code = main(argv)
    return code, buf_out.getvalue(), buf_err.getvalue()


class TestProducerConfig(unittest.TestCase):
    def test_valid_profile(self) -> None:
        p = parse_producer_profile(
            {
                "webhook_base": "https://n8n.example.invalid",
                "webhook_route": "/webhook/x",
                "request_timeout_ms": 30000,
                "connect_timeout_ms": 5000,
                "environment": "sandbox",
                "site_id": "SITE-002",
                "max_retries": 0,
                "concurrency": 1,
            }
        )
        self.assertEqual(p.concurrency, 1)
        sanitized = p.sanitized_dict()
        self.assertTrue(sanitized["endpoint_identity"]["route_configured"])
        self.assertNotIn("webhook_base", sanitized)

    def test_invalid_timeout_zero(self) -> None:
        with self.assertRaises(ProducerConfigError):
            parse_producer_profile({"request_timeout_ms": 0, "concurrency": 1})

    def test_invalid_timeout_extreme(self) -> None:
        with self.assertRaises(ProducerConfigError):
            parse_producer_profile(
                {"request_timeout_ms": 999999, "concurrency": 1}
            )

    def test_concurrency_rejected(self) -> None:
        with self.assertRaises(ProducerConfigError):
            parse_producer_profile({"concurrency": 2})

    def test_route_rejects_full_url(self) -> None:
        with self.assertRaises(ProducerConfigError):
            parse_producer_profile(
                {"webhook_route": "https://evil.example/webhook?x=1"}
            )


class TestEventIdentityProducer(ExporterTestCase):
    def test_same_source_same_id(self) -> None:
        a = process_fixture_dir(self.fixture("fixture-ok"), build_envelope=True)
        b = process_fixture_dir(self.fixture("fixture-ok"), build_envelope=True)
        self.assertIsNotNone(a.envelope)
        self.assertEqual(a.envelope["event_id"], b.envelope["event_id"])

    def test_retry_preserves_event_id(self) -> None:
        proc = process_fixture_dir(self.fixture("fixture-ok"), build_envelope=True)
        env = dict(proc.envelope)
        first = run_producer_offline(
            envelope=env,
            transport_mode="mock",
            mock_fixture="500_internal",
            retry_count=0,
        )
        second = build_retry_simulation(
            first, env, mock_fixture="202_accepted"
        )
        self.assertEqual(first.event_id, second.event_id)
        self.assertEqual(first.event_id, env["event_id"])
        self.assertEqual(second.retry_count, 1)

    def test_changed_status_new_id(self) -> None:
        m = {
            "baseline_count": 1,
            "current_count": 1,
            "added_urls": 0,
            "removed_urls": 0,
            "onboarding_needed_count": 0,
        }
        a = compute_event_id(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="r1",
            observed_at="2026-07-22T10:00:00Z",
            normalized_status="OK",
            summary_code="NO_ACTION_REQUIRED",
            metrics=m,
            reason_codes=["BASELINE_DELTA_ZERO"],
            action_code="NONE",
        )
        b = compute_event_id(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="r1",
            observed_at="2026-07-22T10:00:00Z",
            normalized_status="FAILED",
            summary_code="SOURCE_EXECUTION_FAILED",
            metrics=m,
            reason_codes=["MONITOR_EXECUTION_FAILED"],
            action_code="REVIEW_SOURCE_FAILURE",
        )
        self.assertNotEqual(a, b)


class TestSourceFirewall(unittest.TestCase):
    def test_supported_statuses(self) -> None:
        for status in ("OK", "ATTENTION", "FAILED", "BLOCKED"):
            out = normalize_producer_input({"status": status, "site_id": "SITE-002"})
            self.assertEqual(out["status"], status)

    def test_unsupported_status_rejected(self) -> None:
        with self.assertRaises(SourceFirewallError):
            normalize_producer_input({"status": "WARN"})

    def test_hostile_rejected(self) -> None:
        path = (
            PROJECT_ROOT
            / "fixtures"
            / "producer-hostile"
            / "input-with-secrets.json"
        )
        raw = json.loads(path.read_text(encoding="utf-8"))
        with self.assertRaises(SourceFirewallError):
            extract_allowlisted_from_hostile(raw)


class TestRequestBuilder(unittest.TestCase):
    def test_auth_redacted(self) -> None:
        from client_ops_reporting_bridge.producer_config import ProducerSecrets

        profile = offline_default_profile()
        secrets = ProducerSecrets(
            auth_secret_present=True,
            _auth_secret="SYNTHETIC_SECRET_VALUE_FOR_TEST_ONLY",
        )
        env = {
            "schema_name": "mars.client_ops.report",
            "event_id": "11111111-1111-4111-8111-111111111111",
        }
        req = build_outbound_request(env, profile, secrets)
        self.assertEqual(req.method, "POST")
        self.assertTrue(req.auth_header_present)
        redacted = json.dumps(req.sanitized_dict())
        self.assertIn("<redacted>", redacted)
        self.assertTrue(
            assert_no_secret_leak(redacted, secrets.get_auth_secret())
        )


class TestSequentialGuard(unittest.TestCase):
    def test_concurrency_gt1(self) -> None:
        g = SequentialDispatchGuard()
        with self.assertRaises(SequentialDispatchError):
            g.acquire(concurrency=2)

    def test_parallel_acquire_rejected(self) -> None:
        g = SequentialDispatchGuard()
        g.acquire(concurrency=1)
        with self.assertRaises(SequentialDispatchError):
            g.acquire(concurrency=1)
        g.release()


class TestResponseClassifier(unittest.TestCase):
    def test_all_mock_fixtures(self) -> None:
        profile = offline_default_profile()
        env = {"event_id": "22222222-2222-4222-8222-222222222222", "schema_name": "mars.client_ops.report"}
        req = build_outbound_request(env, profile)
        for name in MOCK_FIXTURE_NAMES:
            resp = MockTransport(fixture_name=name).dispatch(req)
            cls = classify_transport_response(resp)
            self.assertFalse(cls.automatic_retry)
            self.assertFalse(cls.telegram_delivery_known)
            if name == "202_accepted":
                self.assertTrue(cls.intake_accepted)
                self.assertEqual(cls.business_result, "INTAKE_ACCEPTED")
            if name == "read_timeout_ambiguous":
                self.assertEqual(
                    cls.retry_decision, RETRY_MANUAL_DEDUPE_CHECK_REQUIRED
                )


class TestRetryAndAmbiguous(ExporterTestCase):
    def test_ambiguous_no_auto_retry(self) -> None:
        proc = process_fixture_dir(self.fixture("fixture-ok"), build_envelope=True)
        env = dict(proc.envelope)
        result = run_producer_offline(
            envelope=env,
            transport_mode="mock",
            mock_fixture="read_timeout_ambiguous",
        )
        self.assertEqual(result.event_id, env["event_id"])
        self.assertEqual(
            result.retry_decision, RETRY_MANUAL_DEDUPE_CHECK_REQUIRED
        )
        self.assertFalse(result.automatic_retry)
        plan = plan_retry_attempt(
            event_id=result.event_id or "",
            envelope=env,
            classification=classify_transport_response(
                MockTransport("read_timeout_ambiguous").dispatch(
                    build_outbound_request(env, offline_default_profile())
                )
            ),
            retry_count=0,
            max_retries=0,
        )
        self.assertFalse(plan["automatic_retry"])
        self.assertFalse(plan["dispatch_triggered"])
        self.assertTrue(plan["requires_manual_dedupe_check"])

    def test_202_not_telegram_sent(self) -> None:
        result = run_producer_offline(
            fixture_dir=self.fixture("fixture-ok"),
            transport_mode="mock",
            mock_fixture="202_accepted",
        )
        self.assertTrue(result.intake_accepted)
        self.assertFalse(result.telegram_delivery_known)
        self.assertIsNone(result.telegram_message_id)
        self.assertIsNone(result.n8n_execution_id)


class TestEvidenceWriter(ExporterTestCase):
    def test_sanitized_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = run_producer_offline(
                fixture_dir=self.fixture("fixture-ok"),
                transport_mode="mock",
                mock_fixture="202_accepted",
                evidence_dir=Path(tmp),
            )
            doc = build_evidence_document(result)
            text = json.dumps(doc)
            self.assertNotIn("Authorization", text)
            self.assertIsNone(doc["result"]["n8n_execution_id"])
            paths = list(Path(tmp).glob("*.json"))
            self.assertEqual(len(paths), 1)


class TestNetworkGuard(ExporterTestCase):
    def test_push_webhook_blocked(self) -> None:
        code, out, _ = _run_cli(["push-webhook", "--live"])
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D2, out)

    def test_live_flag_blocked(self) -> None:
        code, out, _ = _run_cli(
            [
                "producer-dry-run",
                "--fixture",
                str(self.fixture("fixture-ok")),
                "--live",
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn('"network_calls": 0', out)

    def test_http_transport_blocked(self) -> None:
        with self.assertRaises(NetworkDispatchNotAuthorized):
            create_transport("http")

    def test_no_urlopen(self) -> None:
        with mock.patch("urllib.request.urlopen") as urlopen:
            code, out, _ = _run_cli(
                [
                    "producer-dry-run",
                    "--fixture",
                    str(self.fixture("fixture-ok")),
                    "--mock-response",
                    "202_accepted",
                ]
            )
            self.assertEqual(code, EXIT_SUCCESS)
            urlopen.assert_not_called()
            self.assertIn('"network_calls": 0', out)

    def test_concurrency_cli_rejected(self) -> None:
        code, out, _ = _run_cli(
            [
                "producer-dry-run",
                "--fixture",
                str(self.fixture("fixture-ok")),
                "--concurrency",
                "4",
            ]
        )
        self.assertEqual(code, EXIT_CONCURRENCY_REJECTED)


class TestSite002Representative(ExporterTestCase):
    def test_normalize_and_produce(self) -> None:
        fx = self.fixture("fixture-site-002-representative")
        proc = process_fixture_dir(fx, build_envelope=True)
        self.assertTrue(proc.distributable)
        env = proc.envelope
        assert env is not None
        text = json.dumps(env)
        self.assertNotIn("X:\\", text)
        self.assertNotIn("password", text.lower())
        result = run_producer_offline(
            envelope=env,
            transport_mode="mock",
            mock_fixture="202_accepted",
        )
        self.assertEqual(result.event_id, env["event_id"])
        self.assertEqual(result.network_calls, 0)


class TestOfflineDemos(ExporterTestCase):
    def test_demo_sequence_same_event_id(self) -> None:
        reset_default_guard_for_tests()
        proc = process_fixture_dir(
            self.fixture("fixture-site-002-representative"), build_envelope=True
        )
        env = dict(proc.envelope)
        r202 = run_producer_offline(
            envelope=env, transport_mode="mock", mock_fixture="202_accepted"
        )
        r_to = run_producer_offline(
            envelope=env,
            transport_mode="mock",
            mock_fixture="read_timeout_ambiguous",
        )
        r_dup = run_producer_offline(
            envelope=env,
            transport_mode="mock",
            mock_fixture="200_duplicate_suppressed",
        )
        self.assertEqual(r202.event_id, r_to.event_id)
        self.assertEqual(r202.event_id, r_dup.event_id)
        self.assertEqual(r_dup.business_result, "DUPLICATE_SUPPRESSED")
        self.assertEqual(
            r_to.retry_decision, RETRY_MANUAL_DEDUPE_CHECK_REQUIRED
        )


class TestCliPreserved(ExporterTestCase):
    def test_validate_only_still_works(self) -> None:
        code, _, _ = _run_cli(
            ["validate-only", "--fixture", str(self.fixture("fixture-ok"))]
        )
        self.assertEqual(code, EXIT_SUCCESS)


if __name__ == "__main__":
    unittest.main()
