"""Phase 1B-D6E — producer binding tests (offline)."""

from __future__ import annotations

import unittest

from client_ops_reporting_bridge.producer_constants import (
    DEFAULT_CONCURRENCY,
    DEFAULT_MAX_RETRIES,
    RETRY_FUTURE_ELIGIBLE,
    RETRY_MANUAL_DEDUPE_CHECK_REQUIRED,
    RETRY_TERMINAL_FAILURE,
    RETRY_TERMINAL_SUCCESS,
)
from client_ops_reporting_bridge.retry_policy_binding import (
    AUTOMATIC_RETRIES_ENABLED,
    FINAL_FAILURE,
    MAX_AUTOMATIC_RETRIES,
    MAX_SAFE_CONCURRENCY,
    RECONCILE_BEFORE_RETRY,
    UNSAFE_TO_RETRY,
    assert_d6e_producer_defaults,
    evaluate_producer_binding,
    map_legacy_retry_decision,
    sanitized_binding_dict,
)


class TestD6ERetryPolicyBinding(unittest.TestCase):
    def test_defaults_remain_safe(self) -> None:
        assert_d6e_producer_defaults()
        self.assertEqual(DEFAULT_MAX_RETRIES, 0)
        self.assertEqual(DEFAULT_CONCURRENCY, 1)
        self.assertFalse(AUTOMATIC_RETRIES_ENABLED)
        self.assertEqual(MAX_AUTOMATIC_RETRIES, 0)
        self.assertEqual(MAX_SAFE_CONCURRENCY, 1)

    def test_ambiguous_maps_to_reconcile(self) -> None:
        self.assertEqual(
            map_legacy_retry_decision(RETRY_MANUAL_DEDUPE_CHECK_REQUIRED),
            RECONCILE_BEFORE_RETRY,
        )
        self.assertEqual(
            map_legacy_retry_decision(RETRY_FUTURE_ELIGIBLE),
            RECONCILE_BEFORE_RETRY,
        )

    def test_terminal_mappings(self) -> None:
        self.assertEqual(map_legacy_retry_decision(RETRY_TERMINAL_SUCCESS), UNSAFE_TO_RETRY)
        self.assertEqual(map_legacy_retry_decision(RETRY_TERMINAL_FAILURE), FINAL_FAILURE)

    def test_pending_never_auto_retry(self) -> None:
        r = evaluate_producer_binding(
            retry_decision=RETRY_FUTURE_ELIGIBLE,
            delivery_state="PENDING",
        )
        self.assertEqual(r["decision"], RECONCILE_BEFORE_RETRY)
        self.assertFalse(r["automatic_retry"])
        self.assertFalse(r["retry_authorized"])

    def test_telegram_success_pending_fails_closed(self) -> None:
        r = evaluate_producer_binding(
            retry_decision=RETRY_TERMINAL_SUCCESS,
            delivery_state="PENDING",
            telegram_outcome="SUCCESS",
        )
        self.assertEqual(r["decision"], UNSAFE_TO_RETRY)
        self.assertEqual(r["reason_code"], "TELEGRAM_SUCCESS_LEDGER_PENDING")

    def test_sent_terminal(self) -> None:
        r = evaluate_producer_binding(
            retry_decision=RETRY_TERMINAL_SUCCESS,
            delivery_state="SENT",
        )
        self.assertEqual(r["decision"], UNSAFE_TO_RETRY)

    def test_failed_terminal(self) -> None:
        r = evaluate_producer_binding(
            retry_decision=RETRY_TERMINAL_FAILURE,
            delivery_state="FAILED",
        )
        self.assertEqual(r["decision"], FINAL_FAILURE)

    def test_stale_blocks_retry(self) -> None:
        r = evaluate_producer_binding(
            retry_decision=RETRY_FUTURE_ELIGIBLE,
            delivery_eligibility="STALE_REVIEW_REQUIRED",
        )
        self.assertFalse(r["retry_authorized"])
        self.assertTrue(r["freshness_recheck_required"])

    def test_rejects_nonzero_max_retries(self) -> None:
        with self.assertRaises(RuntimeError):
            evaluate_producer_binding(retry_decision=RETRY_FUTURE_ELIGIBLE, max_retries=1)

    def test_sanitized_dict_strips_secrets(self) -> None:
        cleaned = sanitized_binding_dict(
            {"decision": UNSAFE_TO_RETRY, "api_key": "x", "token": "y"}
        )
        self.assertNotIn("api_key", cleaned)
        self.assertNotIn("token", cleaned)
        self.assertEqual(cleaned["decision"], UNSAFE_TO_RETRY)


if __name__ == "__main__":
    unittest.main()
