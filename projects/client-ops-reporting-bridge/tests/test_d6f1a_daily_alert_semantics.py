"""Phase 1B-D6F1A — import condition + daily identity regression tests."""

from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone

from client_ops_reporting_bridge.event_identity import compute_event_id
from client_ops_reporting_bridge.import_condition import (
    CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
    FULL_SUCCESS,
    NO_FRESH_IMPORT,
    OFFERS_INPUT_ABSENT,
    OFFERS_INPUT_PRESENT_AND_PROCESSED,
    apply_import_condition_to_status,
    classify_import_report,
    classify_offers_state,
    offers_files_present,
)


class TestImportConditionD6F1A(unittest.TestCase):
    def test_t3_missing_offers_attention(self) -> None:
        r = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            offers_input_files=[],
            catalog_phase_ok=True,
            offers_phase_ok=True,
            offers_processed_count=0,
        )
        self.assertEqual(r["report_class"], CATALOG_SUCCESS_OFFERS_INPUT_MISSING)
        self.assertEqual(r["severity"], "ATTENTION")
        self.assertEqual(r["offers_state"], OFFERS_INPUT_ABSENT)
        self.assertIn("OFFERS0_XML_ABSENT", r["reason_codes"])

    def test_t4_no_fresh_import_attention(self) -> None:
        r = classify_import_report(fresh_import_confirmed=False)
        self.assertEqual(r["report_class"], NO_FRESH_IMPORT)
        self.assertEqual(r["severity"], "ATTENTION")

    def test_t5_catalog_alone_not_full_success(self) -> None:
        r = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            offers_input_files=[],
            catalog_phase_ok=True,
            offers_phase_ok=True,
            offers_processed_count=0,
        )
        self.assertNotEqual(r["report_class"], FULL_SUCCESS)
        self.assertEqual(r["severity"], "ATTENTION")

    def test_t6_offers_present_and_processed_ok(self) -> None:
        r = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            offers_input_files=["offers0_1.xml"],
            catalog_phase_ok=True,
            offers_phase_ok=True,
            offers_processed_count=10,
        )
        self.assertEqual(r["severity"], "OK")
        self.assertEqual(
            classify_offers_state(
                offers_input_files=["offers0_1.xml"],
                offers_phase_status="PASS",
                offers_processed_count=10,
            ),
            OFFERS_INPUT_PRESENT_AND_PROCESSED,
        )

    def test_offer_xml_literal_not_canonical(self) -> None:
        self.assertFalse(offers_files_present(["offer.xml", "offers.xml"]))
        self.assertTrue(offers_files_present(["offers0_1.xml"]))

    def test_t9_no_unsupported_disable_claim(self) -> None:
        r = classify_import_report(
            fresh_import_confirmed=True,
            catalog_input_files=["import0_1.xml"],
            offers_input_files=[],
            catalog_phase_ok=True,
            offers_phase_ok=True,
            offers_processed_count=0,
        )
        forbidden = " ".join(r.get("forbidden_claims") or []).lower()
        self.assertIn("disabled", forbidden)

    def test_apply_does_not_downgrade_failed(self) -> None:
        r = classify_import_report(fresh_import_confirmed=False)
        merged = apply_import_condition_to_status(current_status="FAILED", import_result=r)
        self.assertEqual(merged["normalized_status"], "FAILED")


class TestDailyRunIdentityD6F1A(unittest.TestCase):
    def _metrics(self) -> dict[str, int]:
        return {
            "baseline_count": 1879,
            "current_count": 1879,
            "added_urls": 10,
            "removed_urls": 10,
            "onboarding_needed_count": 0,
        }

    def test_t1_same_run_duplicate_same_event_id(self) -> None:
        kwargs = dict(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="2026-08-05_12-30-02",
            observed_at="2026-08-05T05:30:47Z",
            normalized_status="ATTENTION",
            summary_code="OFFERS_INPUT_MISSING",
            metrics=self._metrics(),
            reason_codes=["OFFERS0_XML_ABSENT"],
            action_code="REVIEW_MISSING_OFFERS",
        )
        a = compute_event_id(**kwargs)
        b = compute_event_id(**kwargs)
        self.assertEqual(a, b)

    def test_t2_next_day_same_condition_new_event_id(self) -> None:
        shared = dict(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            normalized_status="ATTENTION",
            summary_code="OFFERS_INPUT_MISSING",
            metrics=self._metrics(),
            reason_codes=["OFFERS0_XML_ABSENT"],
            action_code="REVIEW_MISSING_OFFERS",
        )
        day1 = compute_event_id(
            run_id="2026-08-05_12-30-02",
            observed_at="2026-08-05T05:30:47Z",
            **shared,
        )
        day2 = compute_event_id(
            run_id="2026-08-06_13-04-53",
            observed_at="2026-08-06T06:05:25Z",
            **shared,
        )
        self.assertNotEqual(day1, day2)

    def test_two_runs_same_day_distinct(self) -> None:
        shared = dict(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            normalized_status="OK",
            summary_code="FULL_IMPORT_SUCCESS",
            metrics=self._metrics(),
            reason_codes=["CATALOG_PROCESSED", "OFFERS_PROCESSED"],
            action_code="NONE",
        )
        a = compute_event_id(
            run_id="2026-08-06_12-30-02",
            observed_at="2026-08-06T05:30:00Z",
            **shared,
        )
        b = compute_event_id(
            run_id="2026-08-06_18-00-00",
            observed_at="2026-08-06T11:00:00Z",
            **shared,
        )
        self.assertNotEqual(a, b)

    def test_t8_test_gallery_namespace_differs(self) -> None:
        prod = compute_event_id(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="2026-08-06_13-04-53",
            observed_at="2026-08-06T06:05:25Z",
            normalized_status="ATTENTION",
            summary_code="HYGIENE_REVIEW_REQUIRED",
            metrics=self._metrics(),
            reason_codes=["HYGIENE_FLAGS_PRESENT"],
            action_code="REVIEW_HYGIENE",
        )
        gallery = compute_event_id(
            site_id="SITE-002",
            event_type="site.post_1c_monitor",
            run_id="d6f1a-gallery-G2",
            observed_at="2026-08-06T06:05:25Z",
            normalized_status="ATTENTION",
            summary_code="OFFERS_INPUT_MISSING",
            metrics=self._metrics(),
            reason_codes=["TEST_GALLERY", "OFFERS0_XML_ABSENT"],
            action_code="REVIEW_MISSING_OFFERS",
        )
        self.assertNotEqual(prod, gallery)


if __name__ == "__main__":
    unittest.main()
