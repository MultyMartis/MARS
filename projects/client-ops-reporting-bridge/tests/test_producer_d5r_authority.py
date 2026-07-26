"""Phase 1B-D5R — SITE-002 authority alignment offline proofs (no network, no monitor exec)."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timedelta, timezone
from pathlib import Path

from support import PROJECT_ROOT, ExporterTestCase  # noqa: F401

from client_ops_reporting_bridge.cli import main
from client_ops_reporting_bridge.artifact_loader import load_artifacts
from client_ops_reporting_bridge.constants import STALE_AFTER_SECONDS
from client_ops_reporting_bridge.normalizer import normalize
from client_ops_reporting_bridge.producer_constants import (
    EXIT_NETWORK_NOT_AUTHORIZED,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
)
from client_ops_reporting_bridge.site002_adapter_constants import SOURCE_CONTRACT_VERSION


def _run_cli(argv: list[str]) -> tuple[int, str, str]:
    buf_out = io.StringIO()
    buf_err = io.StringIO()
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        code = main(argv)
    return code, buf_out.getvalue(), buf_err.getvalue()


def _iso(hours_ago: float) -> str:
    dt = datetime.now(timezone.utc) - timedelta(hours=hours_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_trio(
    run_dir: Path,
    *,
    monitor_class: str,
    run_class: str,
    onboarding: int,
    added: int = 0,
    removed: int = 0,
    baseline: int = 1737,
    hours_ago: float = 1.0,
    next_action_monitor: str = "monitor-next",
    next_action_run: str | None = None,
) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    observed = _iso(hours_ago)
    current = baseline + added - removed
    (run_dir / "monitor-classification.json").write_text(
        json.dumps(
            {
                "classification": monitor_class,
                "onboarding_needs_count": onboarding,
                "added_count": added,
                "removed_count": removed,
                "observed_at": observed,
                "next_action": next_action_monitor,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (run_dir / "changed-summary.json").write_text(
        json.dumps(
            {
                "baseline_url_count": baseline,
                "current_url_count": current,
                "added_count": added,
                "removed_count": removed,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (run_dir / "run-summary.json").write_text(
        json.dumps(
            {
                "run_id": run_dir.name,
                "status": "success",
                "exit_code": 0,
                "classification": run_class,
                "next_action": next_action_run
                if next_action_run is not None
                else next_action_monitor,
                "baseline_url_count": baseline,
                "current_url_count": current,
                "added_count": added,
                "removed_count": removed,
                "onboarding_needs_count": onboarding,
                "observed_at": observed,
                "finished_at": observed,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


class D5RAuthorityAlignmentTests(ExporterTestCase):
    """Categories A–T (selected offline proofs)."""

    def test_a_artifact_writer_semantic_mapping_contract_version(self) -> None:
        self.assertEqual(SOURCE_CONTRACT_VERSION, "site002-monitor-result-v1")

    def test_b_run_summary_semantic_role_conflict_not_health_layer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run-conflict"
            _write_trio(
                run_dir,
                monitor_class="ONBOARDING_REQUIRED",
                run_class="NO_ACTION_REQUIRED",
                onboarding=7,
                added=119,
                removed=2,
            )
            artifacts = load_artifacts(run_dir)
            result = normalize(artifacts)
            self.assertEqual(result.summary_code, "SOURCE_ARTIFACT_CONFLICT")
            self.assertEqual(result.normalized_status, "BLOCKED")
            # Metrics still trusted presence-wise; conflict is classification mismatch
            self.assertTrue(result.metrics_trusted)

    def test_c_monitor_classification_semantic_role_primary_when_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run-match-onboard"
            _write_trio(
                run_dir,
                monitor_class="ONBOARDING_REQUIRED",
                run_class="ONBOARDING_REQUIRED",
                onboarding=4,
                added=80,
            )
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.normalized_status, "ATTENTION")
            self.assertEqual(result.summary_code, "ONBOARDING_REQUIRED")
            self.assertEqual(result.source_status, "ONBOARDING_REQUIRED")

    def test_d_changed_summary_semantic_role_metrics_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run-quiet"
            _write_trio(
                run_dir,
                monitor_class="NO_ACTION_REQUIRED",
                run_class="NO_ACTION_REQUIRED",
                onboarding=0,
            )
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.metrics["baseline_count"], 1737)
            self.assertEqual(result.metrics["added_urls"], 0)
            self.assertEqual(result.normalized_status, "OK")

    def test_e_authority_precedence_mismatch_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run-hygiene-mismatch"
            _write_trio(
                run_dir,
                monitor_class="HYGIENE_REVIEW_REQUIRED",
                run_class="NO_ACTION_REQUIRED",
                onboarding=0,
                added=3,
            )
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.normalized_status, "BLOCKED")
            self.assertIn("RUN_SUMMARY_VS_MONITOR_CLASSIFICATION", result.reason_codes)

    def test_f_expected_disagreement_case_d5_candidate1_shape(self) -> None:
        """Emitter bug shape: action class vs runner default — must stay BLOCKED."""
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "2026-07-26_12-30-02"
            _write_trio(
                run_dir,
                monitor_class="ONBOARDING_REQUIRED",
                run_class="NO_ACTION_REQUIRED",
                onboarding=7,
                added=119,
                removed=2,
                next_action_run="Review run-summary.json and monitor-classification.json in run directory.",
            )
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.summary_code, "SOURCE_ARTIFACT_CONFLICT")
            self.assertFalse(result.ok)

    def test_g_genuine_conflict_case_onboarding_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run-count-conflict"
            _write_trio(
                run_dir,
                monitor_class="NO_ACTION_REQUIRED",
                run_class="NO_ACTION_REQUIRED",
                onboarding=2,
            )
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.summary_code, "SOURCE_ARTIFACT_CONFLICT")

    def test_h_run_health_action_state_not_split_via_run_summary_class(self) -> None:
        """Documented: run-summary.classification is not an independent health layer."""
        evidence = (
            PROJECT_ROOT
            / "evidence"
            / "phase-1b-d5r-site002-authority-alignment"
            / "ROOT-CAUSE-ANALYSIS.md"
        )
        text = evidence.read_text(encoding="utf-8")
        self.assertIn("MONITOR_ARTIFACT_GENERATION_BUG", text)
        self.assertIn("ROOT_CAUSE_CONFIRMED", text)
        self.assertNotIn("EXPECTED_DIFFERENT_SEMANTIC_LAYERS\n\n## Confirmation", text)

    def test_i_malformed_incomplete_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run-incomplete"
            run_dir.mkdir(parents=True, exist_ok=True)
            (run_dir / "monitor-classification.json").write_text("{", encoding="utf-8")
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.normalized_status, "BLOCKED")

    def test_j_freshness_separate_decision_documented(self) -> None:
        path = (
            PROJECT_ROOT
            / "evidence"
            / "phase-1b-d5r-site002-authority-alignment"
            / "FRESHNESS-SEMANTICS.md"
        )
        text = path.read_text(encoding="utf-8")
        self.assertIn("FRESHNESS_STATUS_SEMANTICS_REQUIRES_SEPARATE_REPAIR", text)
        self.assertEqual(STALE_AFTER_SECONDS, 93600)

    def test_k_stale_candidate_blocked_without_adapter_rewrite(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run-stale-ok"
            _write_trio(
                run_dir,
                monitor_class="NO_ACTION_REQUIRED",
                run_class="NO_ACTION_REQUIRED",
                onboarding=0,
                hours_ago=40,
            )
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.summary_code, "SOURCE_REPORT_STALE")
            self.assertEqual(result.normalized_status, "BLOCKED")
            self.assertTrue(result.stale)

    def test_l_preview_semantics_decision_file(self) -> None:
        path = (
            PROJECT_ROOT
            / "evidence"
            / "phase-1b-d5r-site002-authority-alignment"
            / "D5-CANDIDATE-REASSESSMENT.json"
        )
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(
            data["safe_existing_source"],
            "NO_SAFE_EXISTING_SOURCE_AVAILABLE_FOR_D5_RETRY",
        )
        for c in data["candidates"]:
            self.assertEqual(
                c["future_retry_safety"],
                "CANDIDATE_NOT_SAFE_FOR_FUTURE_D5_RETRY",
            )

    def test_m_deterministic_identity_unchanged_note(self) -> None:
        path = (
            PROJECT_ROOT
            / "evidence"
            / "phase-1b-d5r-site002-authority-alignment"
            / "EVENT-ID-IMPACT.json"
        )
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertFalse(data["interpretation_changed"])
        for c in data["candidates"]:
            self.assertFalse(c["changed"])
            self.assertEqual(c["old_event_id"], c["repaired_event_id"])

    def test_n_event_id_impact_fixtures_three_candidates(self) -> None:
        path = (
            PROJECT_ROOT
            / "evidence"
            / "phase-1b-d5r-site002-authority-alignment"
            / "EVENT-ID-IMPACT.json"
        )
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(len(data["candidates"]), 3)
        ids = {c["old_event_id"] for c in data["candidates"]}
        self.assertIn("e30ef970-7ea1-561b-ac2d-411201ba04c8", ids)

    def test_o_d5_candidates_reassessment_max_three(self) -> None:
        path = (
            PROJECT_ROOT
            / "evidence"
            / "phase-1b-d5r-site002-authority-alignment"
            / "D5-CANDIDATE-REASSESSMENT.json"
        )
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["d5r_candidate_rereads"], 3)
        self.assertEqual(data["d5r_raw_source_log_reads"], 0)
        self.assertLessEqual(len(data["candidates"]), 3)

    def test_p_d5_live_mode_remains_blocked(self) -> None:
        code, out, err = _run_cli(
            [
                "site002-controlled-live",
                "--source",
                str(
                    PROJECT_ROOT
                    / "fixtures"
                    / "site-002-real-source-adapter"
                    / "ok-no-action"
                ),
                "--latest",
                "--dry-run",
            ]
        )
        combined = out + err
        self.assertEqual(code, EXIT_NETWORK_NOT_AUTHORIZED)
        self.assertIn(NETWORK_DISPATCH_NOT_AUTHORIZED_D5, combined)

    def test_q_d5_charter_remains_unused_documented(self) -> None:
        path = (
            PROJECT_ROOT
            / "evidence"
            / "phase-1b-d5r-site002-authority-alignment"
            / "D5-CHARTER-STATE.md"
        )
        text = path.read_text(encoding="utf-8")
        self.assertIn("UNUSED", text)
        self.assertIn("charter_consumed", text)
        self.assertIn("false", text)
        decision = json.loads(
            (
                PROJECT_ROOT
                / "evidence"
                / "phase-1b-d5r-site002-authority-alignment"
                / "D5R-DECISION.json"
            ).read_text(encoding="utf-8")
        )
        self.assertFalse(decision["d5_charter"]["charter_consumed"])
        self.assertEqual(decision["d5_charter"]["real_http_requests"], 0)

    def test_r_no_monitor_execution_decision(self) -> None:
        decision = json.loads(
            (
                PROJECT_ROOT
                / "evidence"
                / "phase-1b-d5r-site002-authority-alignment"
                / "D5R-DECISION.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(decision["monitor_executions"], 0)
        self.assertEqual(decision["site002_repo_edits"], 0)

    def test_s_no_network_in_module(self) -> None:
        # Offline suite must not import requests for D5R tests file itself.
        import client_ops_reporting_bridge.normalizer as norm

        self.assertFalse(hasattr(norm, "requests"))

    def test_t_d4_d5_regression_conflict_still_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "regression-conflict"
            _write_trio(
                run_dir,
                monitor_class="ONBOARDING_REQUIRED",
                run_class="NO_ACTION_REQUIRED",
                onboarding=1,
                added=1,
            )
            result = normalize(load_artifacts(run_dir))
            self.assertEqual(result.normalized_status, "BLOCKED")
            self.assertEqual(result.summary_code, "SOURCE_ARTIFACT_CONFLICT")


if __name__ == "__main__":
    unittest.main()
