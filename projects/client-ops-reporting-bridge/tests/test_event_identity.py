"""Tests for deterministic event identity."""

from __future__ import annotations

import copy
import unittest
from datetime import datetime, timezone

from client_ops_reporting_bridge.envelope_builder import attach_envelope_with_security
from client_ops_reporting_bridge.event_identity import compute_event_id
from client_ops_reporting_bridge.pipeline import process_fixture_dir

from support import ExporterTestCase


class TestEventIdentity(ExporterTestCase):
    def test_deterministic_repeat(self) -> None:
        a = process_fixture_dir(self.fixture("fixture-ok"))
        b = process_fixture_dir(self.fixture("fixture-dedupe-repeat"))
        self.assertTrue(a.distributable and b.distributable)
        assert a.envelope and b.envelope
        self.assertEqual(a.envelope["event_id"], b.envelope["event_id"])

    def test_generated_at_does_not_affect_identity(self) -> None:
        path = self.fixture("fixture-ok")
        r1 = process_fixture_dir(path)
        r2 = process_fixture_dir(path)
        assert r1.envelope and r2.envelope
        # Force different generated_at via rebuild
        from client_ops_reporting_bridge.artifact_loader import (
            load_artifacts,
            load_fixture_meta,
        )
        from client_ops_reporting_bridge.normalizer import normalize

        meta = load_fixture_meta(path)
        base = normalize(load_artifacts(path), meta=meta)
        e1 = attach_envelope_with_security(
            copy.deepcopy(base),
            generated_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
            meta=meta,
        )
        e2 = attach_envelope_with_security(
            copy.deepcopy(base),
            generated_at=datetime(2026, 12, 31, tzinfo=timezone.utc),
            meta=meta,
        )
        assert e1.envelope and e2.envelope
        self.assertEqual(e1.envelope["event_id"], e2.envelope["event_id"])
        self.assertNotEqual(
            e1.envelope["generated_at"], e2.envelope["generated_at"]
        )

    def test_metric_change_changes_identity(self) -> None:
        metrics = {
            "baseline_count": 100,
            "current_count": 100,
            "added_urls": 0,
            "removed_urls": 0,
            "onboarding_needed_count": 0,
        }
        common = dict(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="r1",
            observed_at="2026-07-20T15:05:00Z",
            normalized_status="OK",
            summary_code="NO_ACTION_REQUIRED",
            reason_codes=["BASELINE_DELTA_ZERO"],
            action_code="NONE",
        )
        id1 = compute_event_id(metrics=metrics, **common)
        metrics2 = dict(metrics)
        metrics2["added_urls"] = 1
        id2 = compute_event_id(metrics=metrics2, **common)
        self.assertNotEqual(id1, id2)

    def test_status_change_changes_identity(self) -> None:
        metrics = {
            "baseline_count": 100,
            "current_count": 100,
            "added_urls": 0,
            "removed_urls": 0,
            "onboarding_needed_count": 0,
        }
        common = dict(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="r1",
            observed_at="2026-07-20T15:05:00Z",
            summary_code="NO_ACTION_REQUIRED",
            metrics=metrics,
            reason_codes=["BASELINE_DELTA_ZERO"],
            action_code="NONE",
        )
        id1 = compute_event_id(normalized_status="OK", **common)
        id2 = compute_event_id(normalized_status="BLOCKED", **common)
        self.assertNotEqual(id1, id2)

    def test_reason_code_order_irrelevant(self) -> None:
        metrics = {
            "baseline_count": 1,
            "current_count": 1,
            "added_urls": 0,
            "removed_urls": 0,
            "onboarding_needed_count": 0,
        }
        common = dict(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="r1",
            observed_at="2026-07-20T15:05:00Z",
            normalized_status="ATTENTION",
            summary_code="ONBOARDING_REQUIRED",
            metrics=metrics,
            action_code="REVIEW_ONBOARDING",
        )
        id1 = compute_event_id(
            reason_codes=["B", "A"], **common
        )
        id2 = compute_event_id(
            reason_codes=["A", "B"], **common
        )
        self.assertEqual(id1, id2)

    def test_no_route_delivery_in_identity(self) -> None:
        # Identity builder has no parameters for delivery/routing — smoke check
        eid = compute_event_id(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="r1",
            observed_at="2026-07-20T15:05:00Z",
            normalized_status="OK",
            summary_code="NO_ACTION_REQUIRED",
            metrics={
                "baseline_count": 1,
                "current_count": 1,
                "added_urls": 0,
                "removed_urls": 0,
                "onboarding_needed_count": 0,
            },
            reason_codes=[],
            action_code="NONE",
        )
        self.assertEqual(len(eid), 36)


if __name__ == "__main__":
    unittest.main()
