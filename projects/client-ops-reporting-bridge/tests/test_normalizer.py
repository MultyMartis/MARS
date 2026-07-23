"""Tests for deterministic normalization."""

from __future__ import annotations

import unittest

from client_ops_reporting_bridge.artifact_loader import load_artifacts, load_fixture_meta
from client_ops_reporting_bridge.normalizer import normalize
from client_ops_reporting_bridge.pipeline import process_fixture_dir

from support import ExporterTestCase


class TestNormalizer(ExporterTestCase):
    def _norm(self, name: str):
        path = self.fixture(name)
        return normalize(load_artifacts(path), meta=load_fixture_meta(path))

    def test_ok(self) -> None:
        r = self._norm("fixture-ok")
        self.assertEqual(r.normalized_status, "OK")
        self.assertEqual(r.summary_code, "NO_ACTION_REQUIRED")
        self.assertEqual(r.action_code, "NONE")

    def test_attention_onboarding(self) -> None:
        r = self._norm("fixture-attention-onboarding")
        self.assertEqual(r.normalized_status, "ATTENTION")
        self.assertEqual(r.summary_code, "ONBOARDING_REQUIRED")

    def test_attention_hygiene(self) -> None:
        r = self._norm("fixture-attention-hygiene")
        self.assertEqual(r.normalized_status, "ATTENTION")
        self.assertEqual(r.summary_code, "HYGIENE_REVIEW_REQUIRED")

    def test_failed_execution(self) -> None:
        r = self._norm("fixture-failed-execution")
        self.assertEqual(r.normalized_status, "FAILED")
        self.assertEqual(r.summary_code, "SOURCE_EXECUTION_FAILED")

    def test_stale(self) -> None:
        r = self._norm("fixture-blocked-stale")
        self.assertEqual(r.normalized_status, "BLOCKED")
        self.assertEqual(r.summary_code, "SOURCE_REPORT_STALE")
        self.assertTrue(r.stale)

    def test_future_time(self) -> None:
        r = self._norm("fixture-blocked-invalid-time")
        self.assertEqual(r.normalized_status, "BLOCKED")
        self.assertEqual(r.summary_code, "SOURCE_TIME_INVALID")

    def test_missing_baseline(self) -> None:
        r = self._norm("fixture-blocked-missing-baseline")
        self.assertEqual(r.normalized_status, "BLOCKED")
        self.assertEqual(r.summary_code, "SOURCE_ARTIFACT_MISSING")
        self.assertFalse(r.metrics_trusted)

    def test_unknown_status(self) -> None:
        r = self._norm("fixture-blocked-unknown-status")
        self.assertEqual(r.normalized_status, "BLOCKED")
        self.assertEqual(r.summary_code, "SOURCE_SCHEMA_UNSUPPORTED")

    def test_classification_conflict(self) -> None:
        r = self._norm("fixture-blocked-classification-conflict")
        self.assertEqual(r.normalized_status, "BLOCKED")
        self.assertEqual(r.summary_code, "SOURCE_ARTIFACT_CONFLICT")
        self.assertIn("CLASSIFICATION_MISMATCH", r.reason_codes)
        self.assertIn("RUN_SUMMARY_VS_MONITOR_CLASSIFICATION", r.reason_codes)

    def test_metric_conflict(self) -> None:
        r = self._norm("fixture-blocked-metric-conflict")
        self.assertEqual(r.normalized_status, "BLOCKED")
        self.assertEqual(r.summary_code, "SOURCE_ARTIFACT_CONFLICT")
        self.assertIn("METRIC_DELTA_INCONSISTENT", r.reason_codes)

    def test_missing_artifact(self) -> None:
        r = self._norm("fixture-blocked-missing-artifact")
        self.assertEqual(r.summary_code, "SOURCE_ARTIFACT_MISSING")

    def test_malformed(self) -> None:
        r = self._norm("fixture-blocked-malformed-json")
        self.assertEqual(r.summary_code, "SOURCE_ARTIFACT_MALFORMED")

    def test_explicit_zero_values(self) -> None:
        r = process_fixture_dir(self.fixture("fixture-ok"))
        self.assertEqual(r.metrics["added_urls"], 0)
        self.assertEqual(r.metrics["removed_urls"], 0)
        self.assertEqual(r.metrics["onboarding_needed_count"], 0)


if __name__ == "__main__":
    unittest.main()
