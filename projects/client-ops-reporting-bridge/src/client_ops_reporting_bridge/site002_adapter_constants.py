"""Phase 1B-D4 SITE-002 real-source adapter constants (offline only)."""

from __future__ import annotations

from typing import Final, Mapping, Sequence

D4_PHASE_ID: Final[str] = "1B-D4"
SOURCE_CONTRACT_VERSION: Final[str] = "site002-monitor-result-v1"

REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4: Final[str] = (
    "REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4"
)

# Fixture-meta markers that identify real-source / D4 adapter inputs.
# D3 synthetic live charter must never authorize these.
D4_REAL_SOURCE_ORIGIN_MARKERS: Final[frozenset[str]] = frozenset(
    {
        "SANITIZED_FROM_ACCEPTED_SITE002_EVIDENCE",
        "REAL_SOURCE_ADAPTER_D4",
        "SITE002_REAL_SOURCE",
    }
)

D4_ALLOWED_TRANSPORTS: Final[frozenset[str]] = frozenset(
    {"disabled", "fixture", "mock"}
)

# Per-artifact allowlists (machine-meaningful keys only).
# Unknown keys are stripped unless they match a reject pattern.
MONITOR_CLASSIFICATION_ALLOWLIST: Final[frozenset[str]] = frozenset(
    {
        "classification",
        "onboarding_needs_count",
        "onboarding_needed_count",
        "observed_at",
        "finished_at",
        "captured_at",
        "completed_at",
        "added_count",
        "removed_count",
        "strict_garbage_hits_count",
        "hygiene_flags_count",
        "brand_violations",
        "false_positive_suppressed_count",
        "next_action",
    }
)

CHANGED_SUMMARY_ALLOWLIST: Final[frozenset[str]] = frozenset(
    {
        "baseline_url_count",
        "baseline_count",
        "current_url_count",
        "current_count",
        "added_count",
        "added_urls",
        "removed_count",
        "removed_urls",
        "onboarding_needs_count",
        "onboarding_needed_count",
        "delta_scale",
        "added_page_types",
        "captured_at",
    }
)

RUN_SUMMARY_ALLOWLIST: Final[frozenset[str]] = frozenset(
    {
        "run_id",
        "id",
        "classification",
        "started_at",
        "start_time",
        "finished_at",
        "completed_at",
        "end_time",
        "exit_code",
        "return_code",
        "duration_seconds",
        "duration_s",
        "added_count",
        "added_urls",
        "removed_count",
        "onboarding_needs_count",
        "onboarding_needed_count",
        "baseline_url_count",
        "current_url_count",
        "hygiene_flags_count",
        "strict_garbage_hits_count",
        "false_positive_suppressed_count",
        "status",
        "mode",
        "operation_id",
        "captured_at",
        "next_action",
    }
)

# Always stripped (never rejected solely for presence when known):
# presentation / path metadata that real monitor may emit.
ALWAYS_STRIP_KEYS: Final[frozenset[str]] = frozenset(
    {
        "artifact_paths",
        "duration_human",
        "run_summary_md",
        "run_log",
        "run_stderr_log",
    }
)

# Substring / exact key patterns that force hard reject when unexpected.
REJECT_KEY_FRAGMENTS: Final[Sequence[str]] = (
    "password",
    "passwd",
    "secret",
    "token",
    "authorization",
    "cookie",
    "stack",
    "traceback",
    "private_key",
    "api_key",
    "webhook_url",
    "ftp_",
    "sftp_",
    "ssh_",
    "db_",
    "database_",
    "sql",
    ".env",
    "command_output",
    "raw_log",
    "raw_html",
    "hosting",
)

ARTIFACT_ALLOWLISTS: Final[Mapping[str, frozenset[str]]] = {
    "monitor-classification.json": MONITOR_CLASSIFICATION_ALLOWLIST,
    "changed-summary.json": CHANGED_SUMMARY_ALLOWLIST,
    "run-summary.json": RUN_SUMMARY_ALLOWLIST,
}

# Status mapping (SITE-002 source → Client Ops) — documentation authority.
STATUS_MAPPING: Final[Mapping[str, str]] = {
    "NO_ACTION_REQUIRED": "OK",
    "ONBOARDING_REQUIRED": "ATTENTION",
    "HYGIENE_REVIEW_REQUIRED": "ATTENTION",
    "FAILURE_REVIEW_REQUIRED": "FAILED",
}

D4_LOCAL_RUNS_REL: Final[str] = "runs/d4-site002-adapter"
