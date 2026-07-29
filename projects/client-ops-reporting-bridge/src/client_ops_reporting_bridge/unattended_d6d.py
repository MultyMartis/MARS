"""Phase 1B-D6D — language boundary: Python artifact discovery/status mapping.

Node owns B/C/E orchestration and the unattended producer harness.
Python owns SITE-002 artifact parsing/status mapping (reuse D4 adapter + D6B).

This module documents the contract and exposes pure helpers for offline tests.
It does NOT enable production, schedulers, webhooks, or Telegram.
"""

from __future__ import annotations

from typing import Final, Mapping

from .delivery_eligibility import (
    FRESH_AND_ELIGIBLE,
    NOT_SAFE_TO_SEND,
    STALE_REVIEW_REQUIRED,
    apply_delivery_eligibility,
    is_stale_age,
)
from .constants import STALE_AFTER_SECONDS
from .site002_adapter_constants import STATUS_MAPPING

D6D_PHASE: Final[str] = "1B-D6D"
D6D_UNATTENDED_PRODUCTION_ENABLED: Final[bool] = False
D6D_AUTHORITATIVE_ARTIFACTS: Final[tuple[str, ...]] = (
    "run-summary.json",
    "monitor-classification.json",
    "changed-summary.json",
)
D6D_COMPLETION_MARKER: Final[str] = "run-complete.marker"
D6D_LANGUAGE_BOUNDARY: Final[str] = (
    "Python: SITE-002 artifact discovery/parsing/source mapping; "
    "Node: Client Ops B/C/E orchestration + unattended producer offline engine"
)


def map_monitor_classification_to_source_status(classification: str) -> str:
    """Factual mapping only — no freshness/retry/delivery mixing."""
    key = str(classification or "").upper()
    return STATUS_MAPPING.get(key, "BLOCKED")


def producer_input_contract_keys() -> tuple[str, ...]:
    return (
        "site_id",
        "artifact_reference",
        "artifact_hash",
        "source_run_id",
        "source_observed_at",
        "source_factual_status",
        "kill_switch_mode",
        "producer_clock",
        "cursor_state",
        "read_only_or_live_mode",
        "charter_reference",
    )


def producer_output_contract_keys() -> tuple[str, ...]:
    return (
        "candidate_decision",
        "event_identity",
        "delivery_eligibility",
        "dedupe_observation",
        "retry_policy_decision",
        "lifecycle_authorization_state",
        "request_authorization_state",
        "cursor_transition",
        "receipt",
        "exit_class",
    )


def assert_freshness_binding() -> Mapping[str, object]:
    """Workstream B binding: age > 93600 means stale."""
    assert STALE_AFTER_SECONDS == 93600
    assert is_stale_age(93600) is False
    assert is_stale_age(93601) is True
    return {
        "stale_after_seconds": STALE_AFTER_SECONDS,
        "operator": "age_seconds > STALE_AFTER_SECONDS",
        "eligibility_values": [
            FRESH_AND_ELIGIBLE,
            STALE_REVIEW_REQUIRED,
            NOT_SAFE_TO_SEND,
        ],
        "apply_delivery_eligibility": apply_delivery_eligibility.__name__,
    }
