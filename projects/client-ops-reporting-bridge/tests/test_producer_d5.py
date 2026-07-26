"""Phase 1B-D5 first manual SITE-002 real-source controlled-live gates (offline)."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from support import PROJECT_ROOT, ExporterTestCase  # noqa: F401

from client_ops_reporting_bridge.cli import main
from client_ops_reporting_bridge.producer_constants import (
    D3_ENABLE_PHRASE,
    D3_SEND_FIRST_PHRASE,
    D5_ENABLE_PHRASE,
    D5_PRODUCER_MARKER,
    D5_REAL_SOURCE_CHARTER_CONSUMED,
    D5_SEND_PHRASE,
    D5_SOURCE_PROVENANCE,
    EXIT_NETWORK_NOT_AUTHORIZED,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
    SECOND_REAL_SOURCE_POST_NOT_AUTHORIZED,
)
from client_ops_reporting_bridge.producer_d5 import (
    apply_d5_real_source_markers,
    assess_preview_for_live,
    build_source_preview,
)
from client_ops_reporting_bridge.producer_d5_gates import (
    D5GateError,
    assert_request_budget,
    build_authorization,
    load_charter_state,
    record_attempted_request,
    reject_forbidden_discovery_flags,
    save_charter_state,
    sanitize_source_label,
    validate_explicit_source_path,
)
from client_ops_reporting_bridge.site002_adapter_constants import (
    REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
    SOURCE_CONTRACT_VERSION,
)


def _run_cli(argv: list[str]) -> tuple[int, str, str]:
    buf_out = io.StringIO()
    buf_err = io.StringIO()
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        code = main(argv)
    return code, buf_out.getvalue(), buf_err.getvalue()


def _fresh_iso(hours_ago: float = 1.0) -> str:
    dt = datetime.now(timezone.utc) - timedelta(hours=hours_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_ok_run(run_dir: Path, *, hours_ago: float = 1.0) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    observed = _fresh_iso(hours_ago)
    run_id = run_dir.name
    (run_dir / "monitor-classification.json").write_text(
        json.dumps(
            {
                "classification": "NO_ACTION_REQUIRED",
                "onboarding_needs_count": 0,
                "added_count": 0,
                "removed_count": 0,
                "observed_at": observed,
                "next_action": "none",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (run_dir / "changed-summary.json").write_text(
        json.dumps(
            {
                "baseline_url_count": 1737,
                "current_url_count": 1737,
                "added_count": 0,
                "removed_count": 0,
                "onboarding_needs_count": 0,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (run_dir / "run-summary.json").write_text(
        json.dumps(
            {
                "run_id": run_id,
                "classification": "NO_ACTION_REQUIRED",
                "started_at": observed,
                "finished_at": observed,
                "exit_code": 0,
                "duration_seconds": 120,
                "added_count": 0,
                "removed_count": 0,
                "onboarding_needs_count": 0,
                "baseline_url_count": 1737,
                "current_url_count": 1737,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


class TestD5SourcePathGates(unittest.TestCase):
    def test_a_source_path_allowlist(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "post-1c"
            run = root / "2026-07-26_10-00-00"
            _write_ok_run(run)
            with mock.patch(
                "client_ops_reporting_bridge.producer_d5_gates.resolve_approved_source_root",
                return_value=root,
            ):
                resolved = validate_explicit_source_path(run)
            self.assertEqual(resolved, run.resolve())

    def test_b_explicit_single_source_only(self) -> None:
        with self.assertRaises(D5GateError):
            validate_explicit_source_path(Path("latest"))

    def test_c_latest_glob_watch_rejection(self) -> None:
        with self.assertRaises(D5GateError):
            reject_forbidden_discovery_flags(latest=True)
        with self.assertRaises(D5GateError):
            reject_forbidden_discovery_flags(watch=True)
        code, out, _ = _run_cli(
            [
                "site002-controlled-live",
                "--source",
                str(PROJECT_ROOT / "fixtures" / "site-002-real-source-adapter" / "ok-no-action"),
                "--latest",
                "--dry-run",
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D5, out)

    def test_e_sanitized_fixture_rejected_as_live_real_source(self) -> None:
        fixture = (
            PROJECT_ROOT / "fixtures" / "site-002-real-source-adapter" / "ok-no-action"
        )
        with self.assertRaises(D5GateError):
            validate_explicit_source_path(fixture)


class TestD5PreviewAndIdentity(ExporterTestCase):
    def test_h_source_preview_and_i_message_security(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "post-1c"
            run = root / "2026-07-26_11-00-00"
            _write_ok_run(run)
            with mock.patch(
                "client_ops_reporting_bridge.producer_d5_gates.resolve_approved_source_root",
                return_value=root,
            ):
                validate_explicit_source_path(run)
            preview = build_source_preview(run)
            self.assertEqual(preview["network_calls"], 0)
            self.assertNotIn("AI MARS STORAGE", json.dumps(preview))
            decision = assess_preview_for_live(preview)
            self.assertTrue(decision["approved"])
            self.assertEqual(
                decision["verdict"], "REAL_SOURCE_PREVIEW_APPROVED_FOR_ONE_LIVE_POST"
            )

    def test_g_freshness_manual_assessment_stale_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "2026-07-01_12-00-00"
            _write_ok_run(run, hours_ago=72)
            preview = build_source_preview(run)
            decision = assess_preview_for_live(preview)
            self.assertFalse(decision["approved"])
            self.assertEqual(
                decision["verdict"], "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST"
            )

    def test_j_event_id_deterministic_double_build(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "2026-07-26_12-00-00"
            _write_ok_run(run)
            from client_ops_reporting_bridge.site002_adapter import adapt_source_dir

            a = adapt_source_dir(run, build_envelope=True)[0]
            b = adapt_source_dir(run, build_envelope=True)[0]
            self.assertEqual(a.envelope["event_id"], b.envelope["event_id"])
            marked = apply_d5_real_source_markers(dict(a.envelope))
            self.assertEqual(marked["event_id"], a.envelope["event_id"])
            self.assertEqual(marked["producer"]["name"], D5_PRODUCER_MARKER)

    def test_l_d5_marker(self) -> None:
        env = {"event_id": "x", "producer": {"name": "old"}}
        out = apply_d5_real_source_markers(env)
        self.assertEqual(out["producer"]["name"], D5_PRODUCER_MARKER)
        self.assertEqual(out["event_id"], "x")


class TestD5LiveGates(unittest.TestCase):
    def _auth(self, **overrides):
        base = dict(
            enable_phrase=D5_ENABLE_PHRASE,
            send_phrase=D5_SEND_PHRASE,
            apply=True,
            dry_run=False,
            environment="manual_real_source_controlled",
            site_id="SITE-002",
            domain="bzpm.ru",
            source_contract=SOURCE_CONTRACT_VERSION,
            source_provenance=D5_SOURCE_PROVENANCE,
            concurrency=1,
            max_retries=0,
            automatic_retry=False,
            producer_marker_present=True,
            profile_present=True,
            secret_present=True,
            source_path_ok=True,
            preview_approved=True,
            event_unseen=True,
            d3_charter_consumed=True,
            d4_live_blocked=True,
        )
        base.update(overrides)
        return build_authorization(**base)

    def test_m_n_o_concurrency_retries(self) -> None:
        with self.assertRaises(D5GateError):
            self._auth(concurrency=2).assert_live_allowed()
        with self.assertRaises(D5GateError):
            self._auth(max_retries=1).assert_live_allowed()
        with self.assertRaises(D5GateError):
            self._auth(automatic_retry=True).assert_live_allowed()

    def test_p_q_exact_phrases(self) -> None:
        self._auth().assert_live_allowed()
        with self.assertRaises(D5GateError):
            self._auth(enable_phrase="WRONG").assert_live_allowed()
        with self.assertRaises(D5GateError):
            self._auth(send_phrase=D3_SEND_FIRST_PHRASE).assert_live_allowed()

    def test_r_missing_apply_rejected(self) -> None:
        with self.assertRaises(D5GateError):
            self._auth(apply=False).assert_live_allowed()

    def test_s_wrong_environment_rejected(self) -> None:
        with self.assertRaises(D5GateError):
            self._auth(environment="sandbox").assert_live_allowed()

    def test_t_missing_secret_profile_rejected(self) -> None:
        with self.assertRaises(D5GateError):
            self._auth(secret_present=False).assert_live_allowed()
        with self.assertRaises(D5GateError):
            self._auth(profile_present=False).assert_live_allowed()

    def test_v_d3_charter_cannot_authorize_d5(self) -> None:
        with self.assertRaises(D5GateError):
            self._auth(enable_phrase=D3_ENABLE_PHRASE).assert_live_allowed()

    def test_w_d4_live_must_remain_blocked_flag(self) -> None:
        with self.assertRaises(D5GateError):
            self._auth(d4_live_blocked=False).assert_live_allowed()

    def test_x_y_charter_budget_one_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runs = Path(tmp)
            state = load_charter_state(runs)
            assert_request_budget(state)
            state = record_attempted_request(state, event_id="evt-1")
            save_charter_state(runs, state)
            state2 = load_charter_state(runs)
            with self.assertRaises(D5GateError) as ctx:
                assert_request_budget(state2)
            self.assertEqual(ctx.exception.code, D5_REAL_SOURCE_CHARTER_CONSUMED)
            self.assertIn(SECOND_REAL_SOURCE_POST_NOT_AUTHORIZED, str(ctx.exception))

    def test_u_generic_live_mode_remains_blocked(self) -> None:
        code, out, _ = _run_cli(
            [
                "push-webhook",
                "--live",
                "--apply",
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D2, out)

    def test_d4_live_remains_blocked_on_adapter_cli(self) -> None:
        fixture = (
            PROJECT_ROOT / "fixtures" / "site-002-real-source-adapter" / "ok-no-action"
        )
        code, out, _ = _run_cli(
            [
                "site002-adapter-dry-run",
                "--source",
                str(fixture),
                "--apply",
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4, out)

    def test_sanitize_label_no_absolute_path(self) -> None:
        label = sanitize_source_label(Path(r"X:\AI MARS STORAGE\ocpilot\x\2026-07-26_12-30-02"))
        self.assertEqual(label, "site002-post-1c-run/2026-07-26_12-30-02")
        self.assertNotIn("STORAGE", label)

    def test_cli_missing_apply_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "post-1c"
            run = root / "2026-07-26_13-00-00"
            _write_ok_run(run)
            with mock.patch(
                "client_ops_reporting_bridge.producer_d5_gates.resolve_approved_source_root",
                return_value=root,
            ):
                code, out, _ = _run_cli(
                    [
                        "site002-controlled-live",
                        "--source",
                        str(run),
                        "--confirm-enable",
                        D5_ENABLE_PHRASE,
                        "--confirm-send",
                        D5_SEND_PHRASE,
                    ]
                )
            self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
            self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D5, out)
            self.assertIn('"network_calls": 0', out)


class TestD5NoNetworkOnImport(unittest.TestCase):
    def test_ac_no_network_on_import(self) -> None:
        import client_ops_reporting_bridge.producer_d5 as d5
        import client_ops_reporting_bridge.producer_d5_gates as gates

        self.assertTrue(hasattr(d5, "run_producer_d5_controlled"))
        self.assertTrue(hasattr(gates, "D5LiveAuthorization"))


if __name__ == "__main__":
    unittest.main()
