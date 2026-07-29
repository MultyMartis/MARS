"""Phase 1B-D6E — offline retry policy binding for producer (no auto-retry).

Canonical evaluator lives in n8n/runners/lib/client-ops-retry-policy.mjs.
This module binds producer classification constants to D6E decision vocabulary
without enabling automatic retries or changing max_retries=0.
"""

from __future__ import annotations

from typing import Any, Mapping, Optional

from .producer_constants import (
    DEFAULT_CONCURRENCY,
    DEFAULT_MAX_RETRIES,
    RETRY_FUTURE_ELIGIBLE,
    RETRY_MANUAL_DEDUPE_CHECK_REQUIRED,
    RETRY_NONE,
    RETRY_TERMINAL_FAILURE,
    RETRY_TERMINAL_SUCCESS,
)

# ---------------------------------------------------------------------------
# Canonical D6E decision values (must match JS evaluator)
# ---------------------------------------------------------------------------

SAFE_TO_RETRY = "SAFE_TO_RETRY"
UNSAFE_TO_RETRY = "UNSAFE_TO_RETRY"
RECONCILE_BEFORE_RETRY = "RECONCILE_BEFORE_RETRY"
FINAL_FAILURE = "FINAL_FAILURE"

D6E_DECISIONS = frozenset(
    {SAFE_TO_RETRY, UNSAFE_TO_RETRY, RECONCILE_BEFORE_RETRY, FINAL_FAILURE}
)

AUTOMATIC_RETRIES_ENABLED = False
MAX_AUTOMATIC_RETRIES = 0
MAX_SAFE_CONCURRENCY = 1


def assert_d6e_producer_defaults() -> None:
    """Fail closed if producer defaults drift from D6E safety baseline."""
    if DEFAULT_MAX_RETRIES != 0:
        raise RuntimeError("D6E requires DEFAULT_MAX_RETRIES=0")
    if DEFAULT_CONCURRENCY != 1:
        raise RuntimeError("D6E requires DEFAULT_CONCURRENCY=1")
    if MAX_AUTOMATIC_RETRIES != 0 or AUTOMATIC_RETRIES_ENABLED:
        raise RuntimeError("D6E automatic retries must remain disabled")
    if MAX_SAFE_CONCURRENCY != 1:
        raise RuntimeError("D6E requires MAX_SAFE_CONCURRENCY=1")


def map_legacy_retry_decision(retry_decision: str) -> str:
    """Map historical producer retry_decision strings to D6E top-level states.

    Does not authorize execution. Ambiguity → RECONCILE_BEFORE_RETRY.
    """
    rd = (retry_decision or "").upper()
    if rd == RETRY_TERMINAL_SUCCESS:
        return UNSAFE_TO_RETRY  # terminal success / no retry
    if rd == RETRY_TERMINAL_FAILURE:
        return FINAL_FAILURE
    if rd == RETRY_MANUAL_DEDUPE_CHECK_REQUIRED:
        return RECONCILE_BEFORE_RETRY
    if rd == RETRY_FUTURE_ELIGIBLE:
        # Historical "future eligible" is NOT automatically SAFE_TO_RETRY.
        # Without durable non-delivery proof → reconcile first.
        return RECONCILE_BEFORE_RETRY
    if rd == RETRY_NONE:
        return FINAL_FAILURE
    return RECONCILE_BEFORE_RETRY


def evaluate_producer_binding(
    *,
    retry_decision: str,
    delivery_state: Optional[str] = None,
    telegram_outcome: Optional[str] = None,
    delivery_eligibility: Optional[str] = None,
    max_retries: int = DEFAULT_MAX_RETRIES,
) -> dict[str, Any]:
    """Sanitized binding result for producer observations.

    Always sets automatic_retry=False and retry_authorized=False.
    """
    assert_d6e_producer_defaults()
    if max_retries != 0:
        raise RuntimeError("D6E forbids max_retries != 0 on producer binding")

    ds = (delivery_state or "").upper() or None
    tg = (telegram_outcome or "").upper() or None
    elig = (delivery_eligibility or "").upper() or None

    if ds == "SENT":
        decision = UNSAFE_TO_RETRY
        reason = "ALREADY_SENT"
    elif ds == "FAILED":
        decision = FINAL_FAILURE
        reason = "DELIVERY_FAILED_TERMINAL"
    elif tg == "SUCCESS" and ds == "PENDING":
        decision = UNSAFE_TO_RETRY
        reason = "TELEGRAM_SUCCESS_LEDGER_PENDING"
    elif ds == "PENDING":
        decision = RECONCILE_BEFORE_RETRY
        reason = "PENDING_NEVER_AUTO_RETRY"
    else:
        decision = map_legacy_retry_decision(retry_decision)
        reason = f"MAPPED_FROM_{retry_decision}"

    if elig in {"STALE_REVIEW_REQUIRED", "NOT_SAFE_TO_SEND"}:
        return {
            "decision": FINAL_FAILURE if decision == SAFE_TO_RETRY else decision,
            "reason_code": elig,
            "retry_authorized": False,
            "automatic_retry": False,
            "freshness_recheck_required": True,
            "controlled_lifecycle_required": True,
            "requires_new_charter": False,
            "max_automatic_retries": 0,
            "max_safe_concurrency": 1,
        }

    return {
        "decision": decision,
        "reason_code": reason,
        "retry_authorized": False,
        "automatic_retry": False,
        "freshness_recheck_required": True,
        "controlled_lifecycle_required": True,
        "requires_new_charter": decision == SAFE_TO_RETRY,
        "max_automatic_retries": 0,
        "max_safe_concurrency": 1,
        "event_identity_preserved": True,
    }


def sanitized_binding_dict(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return evidence-safe copy (no secrets)."""
    forbidden = {
        "api_key",
        "authorization",
        "token",
        "secret",
        "webhook_url",
        "password",
    }
    return {k: v for k, v in result.items() if k.lower() not in forbidden}
