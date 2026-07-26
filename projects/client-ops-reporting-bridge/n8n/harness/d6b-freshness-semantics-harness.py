#!/usr/bin/env python3
"""Phase 1B-D6B offline semantics harness (B1–B15 + gates).

No network. No production apply. Deterministic clocks only.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
TESTS = ROOT / "tests"
sys.path.insert(0, str(SRC))
sys.path.insert(0, str(TESTS))

REQUIRED_CASE_METHODS = [
    "test_b1_fresh_onboarding_attention_eligible",
    "test_b2_stale_onboarding_preserves_attention",
    "test_b3_fresh_ok_eligible",
    "test_b4_stale_ok_preserves_ok",
    "test_b5_fresh_failed_eligible",
    "test_b6_stale_failed_preserves_failed",
    "test_b7_authority_conflict_blocked_not_safe",
    "test_b8_missing_authority_blocked",
    "test_b9_exact_threshold_still_fresh",
    "test_b10_age_93601_stale",
    "test_b11_same_event_id_fresh_then_stale",
    "test_b12_new_run_new_event_id",
    "test_b13_stale_preview_no_customer_payload",
    "test_b14_blocked_preview_no_live",
    "test_b15_fresh_attention_compatible_with_d5_gate",
]


def main() -> int:
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(
        "test_delivery_eligibility_d6b.TestD6BDeliveryEligibility"
    )
    result = unittest.TextTestResult(sys.stdout, True, 1)
    suite.run(result)

    # Ensure B1–B15 methods exist and are collected
    from test_delivery_eligibility_d6b import TestD6BDeliveryEligibility

    missing = [m for m in REQUIRED_CASE_METHODS if not hasattr(TestD6BDeliveryEligibility, m)]
    case_count = len(REQUIRED_CASE_METHODS)
    passed = result.wasSuccessful() and not missing
    out = {
        "phase": "1B-D6B",
        "harness": "d6b-freshness-semantics-harness",
        "token": (
            "D6B_OFFLINE_SEMANTICS_HARNESS_PASS"
            if passed
            else "D6B_OFFLINE_SEMANTICS_HARNESS_FAIL"
        ),
        "b1_b15_required": case_count,
        "b1_b15_missing": missing,
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "pass": passed,
        "live_apply_performed": False,
        "stale_after_seconds": 93600,
        "threshold_boundary": "age==93600 FRESH; age==93601 STALE (operator >)",
    }
    print(json.dumps(out, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
