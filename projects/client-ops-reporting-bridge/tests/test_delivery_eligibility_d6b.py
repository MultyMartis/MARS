"""Phase 1B-D6B — source_status vs delivery_eligibility offline proofs.

Deterministic clock only. No network. No production apply.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from support import PROJECT_ROOT, ExporterTestCase  # noqa: F401

from client_ops_reporting_bridge.artifact_loader import load_artifacts
from client_ops_reporting_bridge.constants import STALE_AFTER_SECONDS
from client_ops_reporting_bridge.delivery_eligibility import (
    FRESH_AND_ELIGIBLE,
    NOT_SAFE_TO_SEND,
    SOURCE_VALID_BUT_STALE_REVIEW_REQUIRED,
    STALE_REVIEW_REQUIRED,
    is_live_delivery_authorized,
    is_stale_age,
)
from client_ops_reporting_bridge.envelope_builder import attach_envelope_with_security
from client_ops_reporting_bridge.normalizer import normalize
from client_ops_reporting_bridge.pipeline import process_fixture_dir
from client_ops_reporting_bridge.producer_d5 import (
    assess_preview_for_live,
    build_d5_real_source_envelope,
    build_source_preview,
)
from client_ops_reporting_bridge.producer_d5_gates import D5GateError
from client_ops_reporting_bridge.site002_adapter import adapt_source_dir


OBSERVED = datetime(2026, 7, 20, 12, 0, 0, tzinfo=timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_run(
    run_dir: Path,
    *,
    classification: str,
    onboarding: int,
    observed: datetime,
    run_id: str | None = None,
    run_class: str | None = None,
    exit_code: int = 0,
    baseline: int = 100,
    added: int = 0,
    removed: int = 0,
    omit_monitor: bool = False,
) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    rid = run_id or run_dir.name
    current = baseline + added - removed
    rc = classification if run_class is None else run_class
    if not omit_monitor:
        (run_dir / "monitor-classification.json").write_text(
            json.dumps(
                {
                    "classification": classification,
                    "onboarding_needs_count": onboarding,
                    "observed_at": _iso(observed),
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
                "onboarding_needs_count": onboarding,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (run_dir / "run-summary.json").write_text(
        json.dumps(
            {
                "run_id": rid,
                "classification": rc,
                "finished_at": _iso(observed),
                "exit_code": exit_code,
                "onboarding_needs_count": onboarding,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def _norm_at(run_dir: Path, now: datetime):
    return normalize(load_artifacts(run_dir), now_utc=now)


class TestD6BDeliveryEligibility(ExporterTestCase):
    def test_threshold_constant_unchanged(self) -> None:
        self.assertEqual(STALE_AFTER_SECONDS, 93600)

    def test_threshold_boundary_explicit(self) -> None:
        # Accepted operator: age > 93600 is stale; age == 93600 is fresh.
        self.assertFalse(is_stale_age(93600))
        self.assertTrue(is_stale_age(93601))

    def test_b1_fresh_onboarding_attention_eligible(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b1"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=3,
                observed=OBSERVED,
                added=3,
            )
            now = OBSERVED + timedelta(seconds=1000)
            r = _norm_at(run, now)
            self.assertEqual(r.normalized_status, "ATTENTION")
            self.assertEqual(r.delivery_eligibility, FRESH_AND_ELIGIBLE)
            self.assertFalse(r.stale)
            self.assertTrue(is_live_delivery_authorized(r))

    def test_b2_stale_onboarding_preserves_attention(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b2"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=3,
                observed=OBSERVED,
                added=3,
            )
            now = OBSERVED + timedelta(seconds=93601)
            r = _norm_at(run, now)
            self.assertEqual(r.normalized_status, "ATTENTION")
            self.assertEqual(r.summary_code, "ONBOARDING_REQUIRED")
            self.assertEqual(r.delivery_eligibility, STALE_REVIEW_REQUIRED)
            self.assertTrue(r.stale)
            self.assertFalse(is_live_delivery_authorized(r))
            self.assertNotEqual(r.normalized_status, "BLOCKED")
            self.assertNotEqual(r.summary_code, "SOURCE_REPORT_STALE")

    def test_b3_fresh_ok_eligible(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b3"
            _write_run(
                run,
                classification="NO_ACTION_REQUIRED",
                onboarding=0,
                observed=OBSERVED,
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=60))
            self.assertEqual(r.normalized_status, "OK")
            self.assertEqual(r.delivery_eligibility, FRESH_AND_ELIGIBLE)

    def test_b4_stale_ok_preserves_ok(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b4"
            _write_run(
                run,
                classification="NO_ACTION_REQUIRED",
                onboarding=0,
                observed=OBSERVED,
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=93601))
            self.assertEqual(r.normalized_status, "OK")
            self.assertEqual(r.delivery_eligibility, STALE_REVIEW_REQUIRED)
            self.assertNotEqual(r.normalized_status, "BLOCKED")

    def test_b5_fresh_failed_eligible(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b5"
            _write_run(
                run,
                classification="FAILURE_REVIEW_REQUIRED",
                onboarding=0,
                observed=OBSERVED,
                exit_code=1,
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=60))
            self.assertEqual(r.normalized_status, "FAILED")
            self.assertEqual(r.delivery_eligibility, FRESH_AND_ELIGIBLE)

    def test_b6_stale_failed_preserves_failed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b6"
            _write_run(
                run,
                classification="FAILURE_REVIEW_REQUIRED",
                onboarding=0,
                observed=OBSERVED,
                exit_code=1,
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=93601))
            self.assertEqual(r.normalized_status, "FAILED")
            self.assertEqual(r.delivery_eligibility, STALE_REVIEW_REQUIRED)
            self.assertNotEqual(r.normalized_status, "BLOCKED")

    def test_b7_authority_conflict_blocked_not_safe(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b7"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=3,
                observed=OBSERVED,
                added=3,
                run_class="NO_ACTION_REQUIRED",
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=60))
            self.assertEqual(r.normalized_status, "BLOCKED")
            self.assertEqual(r.delivery_eligibility, NOT_SAFE_TO_SEND)
            self.assertFalse(is_live_delivery_authorized(r))

    def test_b8_missing_authority_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b8"
            _write_run(
                run,
                classification="NO_ACTION_REQUIRED",
                onboarding=0,
                observed=OBSERVED,
                omit_monitor=True,
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=60))
            self.assertEqual(r.normalized_status, "BLOCKED")
            self.assertEqual(r.delivery_eligibility, NOT_SAFE_TO_SEND)

    def test_b9_exact_threshold_still_fresh(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b9"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=2,
                observed=OBSERVED,
                added=2,
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=93600))
            self.assertEqual(r.age_seconds, 93600)
            self.assertEqual(r.normalized_status, "ATTENTION")
            self.assertEqual(r.delivery_eligibility, FRESH_AND_ELIGIBLE)
            self.assertFalse(r.stale)

    def test_b10_age_93601_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b10"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=2,
                observed=OBSERVED,
                added=2,
            )
            r = _norm_at(run, OBSERVED + timedelta(seconds=93601))
            self.assertEqual(r.age_seconds, 93601)
            self.assertEqual(r.delivery_eligibility, STALE_REVIEW_REQUIRED)
            self.assertTrue(r.stale)

    def test_b11_same_event_id_fresh_then_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b11-same"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=4,
                observed=OBSERVED,
                added=4,
                run_id="run-identity-shared",
            )
            fresh = attach_envelope_with_security(
                _norm_at(run, OBSERVED + timedelta(seconds=100))
            )
            stale = attach_envelope_with_security(
                _norm_at(run, OBSERVED + timedelta(seconds=200000))
            )
            self.assertIsNotNone(fresh.envelope)
            self.assertIsNotNone(stale.envelope)
            self.assertEqual(fresh.envelope["event_id"], stale.envelope["event_id"])
            self.assertEqual(fresh.normalized_status, "ATTENTION")
            self.assertEqual(stale.normalized_status, "ATTENTION")
            self.assertEqual(fresh.delivery_eligibility, FRESH_AND_ELIGIBLE)
            self.assertEqual(stale.delivery_eligibility, STALE_REVIEW_REQUIRED)

    def test_b12_new_run_new_event_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run_a = Path(tmp) / "b12a"
            run_b = Path(tmp) / "b12b"
            obs_b = OBSERVED + timedelta(hours=2)
            _write_run(
                run_a,
                classification="ONBOARDING_REQUIRED",
                onboarding=4,
                observed=OBSERVED,
                added=4,
                run_id="run-a",
            )
            _write_run(
                run_b,
                classification="ONBOARDING_REQUIRED",
                onboarding=4,
                observed=obs_b,
                added=4,
                run_id="run-b",
            )
            a = attach_envelope_with_security(
                _norm_at(run_a, OBSERVED + timedelta(seconds=60))
            )
            b = attach_envelope_with_security(
                _norm_at(run_b, obs_b + timedelta(seconds=60))
            )
            self.assertNotEqual(a.envelope["event_id"], b.envelope["event_id"])

    def test_b13_stale_preview_no_customer_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b13"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=3,
                observed=OBSERVED,
                added=3,
            )
            now = OBSERVED + timedelta(seconds=200000)
            preview = build_source_preview(run, now_utc=now)
            decision = assess_preview_for_live(preview)
            self.assertEqual(preview["client_ops_mapped_status"], "ATTENTION")
            self.assertEqual(preview["delivery_eligibility"], STALE_REVIEW_REQUIRED)
            self.assertIsNone(preview["message_preview"])
            self.assertFalse(decision["approved"])
            self.assertEqual(decision["verdict"], SOURCE_VALID_BUT_STALE_REVIEW_REQUIRED)
            blob = json.dumps(preview)
            self.assertNotIn("AI MARS STORAGE", blob)
            self.assertNotIn("password", blob.lower())

    def test_b14_blocked_preview_no_live(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b14"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=3,
                observed=OBSERVED,
                added=3,
                run_class="NO_ACTION_REQUIRED",
            )
            preview = build_source_preview(run, now_utc=OBSERVED + timedelta(seconds=60))
            decision = assess_preview_for_live(preview)
            self.assertEqual(preview["client_ops_mapped_status"], "BLOCKED")
            self.assertEqual(preview["delivery_eligibility"], NOT_SAFE_TO_SEND)
            self.assertFalse(decision["approved"])
            self.assertIsNone(preview["message_preview"])

    def test_b15_fresh_attention_compatible_with_d5_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "b15"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=3,
                observed=OBSERVED,
                added=3,
            )
            now = OBSERVED + timedelta(seconds=120)
            (run / "fixture-meta.json").write_text(
                json.dumps(
                    {
                        "now_utc": _iso(now),
                        "generated_at": _iso(now),
                    }
                ),
                encoding="utf-8",
            )
            proc, _, _ = adapt_source_dir(run, now_utc=now, build_envelope=True)
            self.assertEqual(proc.normalized_status, "ATTENTION")
            self.assertEqual(proc.delivery_eligibility, FRESH_AND_ELIGIBLE)
            self.assertTrue(proc.distributable)
            self.assertIsNotNone(proc.simple_text)
            preview = build_source_preview(run, now_utc=now)
            decision = assess_preview_for_live(preview)
            self.assertTrue(decision["approved"])
            env = build_d5_real_source_envelope(run)
            self.assertEqual(env["run"]["normalized_status"], "ATTENTION")

    def test_stale_live_envelope_gate_rejects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            run = Path(tmp) / "stale-gate"
            _write_run(
                run,
                classification="ONBOARDING_REQUIRED",
                onboarding=3,
                observed=OBSERVED,
                added=3,
            )
            (run / "fixture-meta.json").write_text(
                json.dumps(
                    {
                        "now_utc": _iso(OBSERVED + timedelta(seconds=200000)),
                        "generated_at": _iso(OBSERVED + timedelta(seconds=200000)),
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(D5GateError):
                build_d5_real_source_envelope(run)

    def test_fixture_blocked_stale_legacy_name_now_ok_stale(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-blocked-stale"))
        self.assertEqual(r.normalized_status, "OK")
        self.assertEqual(r.delivery_eligibility, STALE_REVIEW_REQUIRED)
        self.assertTrue(r.stale)
        self.assertFalse(r.distributable)
        self.assertIsNone(r.simple_text)
        self.assertIsNotNone(r.envelope)

    def test_retry_concurrency_constants_unchanged(self) -> None:
        from client_ops_reporting_bridge.producer_config import DEFAULT_MAX_RETRIES
        from client_ops_reporting_bridge.producer_constants import DEFAULT_CONCURRENCY

        self.assertEqual(DEFAULT_MAX_RETRIES, 0)
        self.assertEqual(DEFAULT_CONCURRENCY, 1)


if __name__ == "__main__":
    unittest.main()
