"""Phase 1B-D4 SITE-002 real-source adapter offline tests."""

from __future__ import annotations

import io
import json
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from support import PROJECT_ROOT, ExporterTestCase  # noqa: F401

from client_ops_reporting_bridge.cli import main
from client_ops_reporting_bridge.producer_constants import (
    EXIT_NETWORK_NOT_AUTHORIZED,
    RETRY_MANUAL_DEDUPE_CHECK_REQUIRED,
)
from client_ops_reporting_bridge.producer_d3 import build_d3_synthetic_envelope
from client_ops_reporting_bridge.site002_adapter import (
    RealSourceLiveDispatchNotAuthorized,
    adapt_source_dir,
    assert_live_dispatch_blocked,
    is_real_source_fixture,
    parse_source,
    reject_d3_real_source_usage,
    run_site002_adapter_dry_run,
    to_producer_input,
)
from client_ops_reporting_bridge.site002_adapter_constants import (
    REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
    SOURCE_CONTRACT_VERSION,
    STATUS_MAPPING,
)
from client_ops_reporting_bridge.site002_adapter_firewall import (
    Site002AdapterFirewallError,
)


D4_ROOT = "site-002-real-source-adapter"


def _run_cli(argv: list[str]) -> tuple[int, str, str]:
    buf_out = io.StringIO()
    buf_err = io.StringIO()
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        code = main(argv)
    return code, buf_out.getvalue(), buf_err.getvalue()


class TestD4SourceAuthorityFixtures(ExporterTestCase):
    def test_a_source_authority_contract_fixture(self) -> None:
        path = self.fixture(f"{D4_ROOT}/ok-no-action")
        self.assertTrue(is_real_source_fixture(path))
        meta = json.loads((path / "fixture-meta.json").read_text(encoding="utf-8"))
        self.assertEqual(
            meta["source_origin"], "SANITIZED_FROM_ACCEPTED_SITE002_EVIDENCE"
        )
        self.assertEqual(SOURCE_CONTRACT_VERSION, "site002-monitor-result-v1")


class TestD4ParsingAndValidation(ExporterTestCase):
    def test_b_source_schema_parsing(self) -> None:
        arts, redaction = parse_source(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertFalse(arts.missing)
        self.assertIsNotNone(arts.monitor_classification)
        self.assertFalse(redaction["run_log_loaded"])

    def test_c_required_fields(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/incomplete-missing-changed")
        )
        self.assertEqual(result.final_state, "ADAPTER_SOURCE_REJECTED")
        self.assertEqual(result.network_calls, 0)

    def test_d_status_mapping(self) -> None:
        self.assertEqual(STATUS_MAPPING["NO_ACTION_REQUIRED"], "OK")
        self.assertEqual(STATUS_MAPPING["ONBOARDING_REQUIRED"], "ATTENTION")
        self.assertEqual(STATUS_MAPPING["HYGIENE_REVIEW_REQUIRED"], "ATTENTION")
        self.assertEqual(STATUS_MAPPING["FAILURE_REVIEW_REQUIRED"], "FAILED")
        result = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertEqual(result.client_ops_status, "OK")
        att = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/attention-onboarding")
        )
        self.assertEqual(att.client_ops_status, "ATTENTION")

    def test_e_unknown_status_rejection(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/hostile-unknown-status")
        )
        self.assertEqual(result.client_ops_status, "BLOCKED")
        self.assertNotEqual(result.client_ops_status, "OK")
        self.assertEqual(result.network_calls, 0)


class TestD4Identity(ExporterTestCase):
    def test_f_run_identity_determinism(self) -> None:
        a = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        b = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertEqual(a.source_run_id, "2026-07-07_d4-ok-sanitized-01")
        self.assertEqual(a.source_run_id, b.source_run_id)

    def test_g_observed_at_preservation(self) -> None:
        a = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertEqual(a.source_observed_at, "2026-07-07T08:35:00Z")

    def test_h_same_source_same_event_id(self) -> None:
        a = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        b = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertIsNotNone(a.event_id)
        self.assertEqual(a.event_id, b.event_id)
        self.assertEqual(a.producer_input, b.producer_input)

    def test_i_different_run_different_event_id(self) -> None:
        a = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        b = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-different-run"))
        self.assertNotEqual(a.source_run_id, b.source_run_id)
        self.assertNotEqual(a.event_id, b.event_id)


class TestD4MetricsAndGates(ExporterTestCase):
    def test_j_metric_normalization(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/attention-onboarding")
        )
        self.assertEqual(result.metrics["baseline_count"], 1737)
        self.assertEqual(result.metrics["current_count"], 1817)
        self.assertEqual(result.metrics["added_urls"], 80)
        self.assertEqual(result.metrics["onboarding_needed_count"], 4)

    def test_k_missing_metric_semantics(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/hostile-invalid-fields")
        )
        self.assertIn(result.client_ops_status, {"BLOCKED"})
        self.assertNotEqual(result.client_ops_status, "OK")

    def test_l_completion_incomplete_source_gate(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/incomplete-missing-changed")
        )
        self.assertEqual(result.validation_result, "SOURCE_REJECTED")

    def test_m_stale_freshness_representation(self) -> None:
        # Historical fixture with pinned now_utc is allowed offline (not stale)
        result = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertFalse(result.producer_input["freshness"]["stale"])


class TestD4Firewall(ExporterTestCase):
    def test_n_source_firewall(self) -> None:
        with self.assertRaises(Site002AdapterFirewallError):
            parse_source(self.fixture(f"{D4_ROOT}/hostile-secrets"))

    def test_o_hostile_fields(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/hostile-secrets")
        )
        self.assertEqual(result.final_state, "ADAPTER_FIREWALL_REJECTED")
        self.assertEqual(result.network_calls, 0)

    def test_p_no_raw_source_passthrough(self) -> None:
        proc, _, _ = adapt_source_dir(self.fixture(f"{D4_ROOT}/ok-no-action"))
        producer_input = to_producer_input(proc)
        blob = json.dumps(producer_input).lower()
        self.assertNotIn("artifact_paths", blob)
        self.assertNotIn("x:\\ai mars storage", blob)
        self.assertNotIn("password", blob)


class TestD4ProducerCompatibility(ExporterTestCase):
    def test_q_producer_input_compatibility(self) -> None:
        result = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertEqual(result.producer_build_result, "BUILT")
        self.assertIn("run_id", result.producer_input or {})

    def test_r_producer_build_envelope_compatibility(self) -> None:
        result = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertIsNotNone(result.event_id)
        self.assertTrue(result.event_id.count("-") == 4)

    def test_s_mock_202(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/ok-no-action"),
            mock_response="202_accepted",
        )
        self.assertTrue(result.intake_accepted)
        self.assertFalse(result.telegram_delivery_known)
        self.assertEqual(result.network_calls, 0)
        self.assertEqual(result.business_result, "INTAKE_ACCEPTED")

    def test_t_mock_duplicate(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/ok-no-action"),
            mock_response="200_duplicate_suppressed",
        )
        self.assertEqual(result.business_result, "DUPLICATE_SUPPRESSED")
        self.assertEqual(result.network_calls, 0)

    def test_u_mock_conflict(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/ok-no-action"),
            mock_response="409_event_id_conflict",
        )
        self.assertEqual(result.business_result, "EVENT_ID_CONFLICT")
        self.assertEqual(result.network_calls, 0)

    def test_v_ambiguous_timeout(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/ok-no-action"),
            mock_response="read_timeout_ambiguous",
        )
        self.assertEqual(result.retry_decision, RETRY_MANUAL_DEDUPE_CHECK_REQUIRED)
        self.assertFalse(result.automatic_retry)
        self.assertEqual(result.network_calls, 0)

    def test_w_automatic_retry_remains_false(self) -> None:
        result = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        self.assertFalse(result.automatic_retry)


class TestD4LiveGuards(ExporterTestCase):
    def test_x_real_source_live_guard(self) -> None:
        with self.assertRaises(RealSourceLiveDispatchNotAuthorized):
            assert_live_dispatch_blocked(live=True)
        with self.assertRaises(RealSourceLiveDispatchNotAuthorized):
            assert_live_dispatch_blocked(apply=True)
        with self.assertRaises(RealSourceLiveDispatchNotAuthorized):
            assert_live_dispatch_blocked(transport="http")
        code, out, _ = _run_cli(
            [
                "site002-adapter-dry-run",
                "--source",
                str(self.fixture(f"{D4_ROOT}/ok-no-action")),
                "--live",
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4, out)
        self.assertIn('"network_calls": 0', out)

        code2, out2, _ = _run_cli(
            [
                "site002-adapter-dry-run",
                "--source",
                str(self.fixture(f"{D4_ROOT}/ok-no-action")),
                "--transport",
                "http",
            ]
        )
        # argparse rejects http choice — usage or D4 guard
        self.assertNotEqual(code2, 0)

        code3, out3, _ = _run_cli(
            [
                "producer-dry-run",
                "--fixture",
                str(self.fixture(f"{D4_ROOT}/ok-no-action")),
                "--live",
            ]
        )
        self.assertEqual(code3, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4, out3)

    def test_y_d3_synthetic_gate_rejects_real_source(self) -> None:
        with self.assertRaises(RealSourceLiveDispatchNotAuthorized):
            reject_d3_real_source_usage(self.fixture(f"{D4_ROOT}/ok-no-action"))
        with self.assertRaises(RealSourceLiveDispatchNotAuthorized):
            build_d3_synthetic_envelope(self.fixture(f"{D4_ROOT}/ok-no-action"))

    def test_z_local_evidence_sanitization(self) -> None:
        result = run_site002_adapter_dry_run(self.fixture(f"{D4_ROOT}/ok-no-action"))
        payload = result.to_sanitized_dict()
        blob = json.dumps(payload).lower()
        self.assertNotIn("password", blob)
        self.assertNotIn("x:\\ai mars storage", blob)
        self.assertNotIn("artifact_paths", blob)

    def test_aa_blocked_conflict_fixture(self) -> None:
        result = run_site002_adapter_dry_run(
            self.fixture(f"{D4_ROOT}/blocked-conflict")
        )
        self.assertEqual(result.client_ops_status, "BLOCKED")
        self.assertEqual(result.summary_code, "SOURCE_ARTIFACT_CONFLICT")

    def test_cli_latest_forbidden(self) -> None:
        code, out, _ = _run_cli(
            [
                "site002-adapter-dry-run",
                "--source",
                str(self.fixture(f"{D4_ROOT}/ok-no-action")),
                "--latest",
            ]
        )
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4, out)


if __name__ == "__main__":
    unittest.main()
