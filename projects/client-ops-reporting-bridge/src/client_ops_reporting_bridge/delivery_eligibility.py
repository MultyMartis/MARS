"""Delivery eligibility vs factual source status (Phase 1B-D6B).

Evaluation-time producer gate. Does not alter durable ledger states
(PENDING/SENT/FAILED) and must not rewrite factual normalized_status
solely because an artifact aged past STALE_AFTER_SECONDS.
"""

from __future__ import annotations

from typing import Final, Optional

from .constants import STALE_AFTER_SECONDS
from .errors import ProcessResult

# Factual source / Client Ops mapped status vocabulary (unchanged).
SOURCE_STATUS_OK: Final[str] = "OK"
SOURCE_STATUS_ATTENTION: Final[str] = "ATTENTION"
SOURCE_STATUS_FAILED: Final[str] = "FAILED"
SOURCE_STATUS_BLOCKED: Final[str] = "BLOCKED"

# Delivery eligibility (evaluation-time; not durable ledger state).
FRESH_AND_ELIGIBLE: Final[str] = "FRESH_AND_ELIGIBLE"
STALE_REVIEW_REQUIRED: Final[str] = "STALE_REVIEW_REQUIRED"
NOT_SAFE_TO_SEND: Final[str] = "NOT_SAFE_TO_SEND"

DELIVERY_ELIGIBILITY_VALUES: Final[frozenset[str]] = frozenset(
    {
        FRESH_AND_ELIGIBLE,
        STALE_REVIEW_REQUIRED,
        NOT_SAFE_TO_SEND,
    }
)

# Preview / live gate vocabulary for stale-but-valid authority.
SOURCE_VALID_BUT_STALE_REVIEW_REQUIRED: Final[str] = (
    "SOURCE_VALID_BUT_STALE_REVIEW_REQUIRED"
)

# Compatibility: historical summary_code used when age alone forced BLOCKED.
LEGACY_STALE_SUMMARY_CODE: Final[str] = "SOURCE_REPORT_STALE"


def is_stale_age(age_seconds: Optional[int], *, threshold: int = STALE_AFTER_SECONDS) -> bool:
    """Exact accepted operator: age_seconds > threshold (93600 is still fresh)."""
    if age_seconds is None:
        return False
    return int(age_seconds) > int(threshold)


def apply_delivery_eligibility(result: ProcessResult) -> ProcessResult:
    """Attach delivery_eligibility from factual status + age.

    Authority BLOCKED / security → NOT_SAFE_TO_SEND.
    Valid factual OK/ATTENTION/FAILED with age > threshold → STALE_REVIEW_REQUIRED
    (factual normalized_status preserved).
    Otherwise → FRESH_AND_ELIGIBLE.
    """
    result.freshness_threshold_seconds = STALE_AFTER_SECONDS
    age = result.age_seconds
    stale = is_stale_age(age)

    if result.normalized_status == SOURCE_STATUS_BLOCKED:
        result.delivery_eligibility = NOT_SAFE_TO_SEND
        result.stale = bool(stale)
        result.freshness_reason = (
            "SOURCE_AUTHORITY_NOT_SAFE_AND_STALE"
            if stale
            else "SOURCE_AUTHORITY_NOT_SAFE"
        )
        return result

    if age is None:
        result.delivery_eligibility = NOT_SAFE_TO_SEND
        result.stale = False
        result.freshness_reason = "AGE_UNKNOWN"
        return result

    if stale:
        result.stale = True
        result.delivery_eligibility = STALE_REVIEW_REQUIRED
        result.freshness_reason = "SOURCE_REPORT_TOO_OLD"
        return result

    result.stale = False
    result.delivery_eligibility = FRESH_AND_ELIGIBLE
    result.freshness_reason = "WITHIN_FRESHNESS_THRESHOLD"
    return result


def is_live_delivery_authorized(result: ProcessResult) -> bool:
    """Live POST requires FRESH_AND_ELIGIBLE and non-BLOCKED factual status."""
    if result.normalized_status == SOURCE_STATUS_BLOCKED:
        return False
    if result.security_rejected:
        return False
    return result.delivery_eligibility == FRESH_AND_ELIGIBLE


def is_customer_deliverable(result: ProcessResult) -> bool:
    """Customer-facing message only when live-delivery authorized and envelope ok."""
    return (
        is_live_delivery_authorized(result)
        and result.envelope is not None
        and not result.security_rejected
    )
