"""Frozen Phase 1A constants, aliases, and code catalogs.

All source-field aliases are centralized here. Do not scatter alias logic.
"""

from __future__ import annotations

from typing import Final, Mapping, Sequence

# ---------------------------------------------------------------------------
# Policy
# ---------------------------------------------------------------------------

STALE_AFTER_SECONDS: Final[int] = 93600
MAX_FUTURE_SKEW_SECONDS: Final[int] = 300

SCHEMA_NAME: Final[str] = "mars.client_ops.report"
SCHEMA_VERSION: Final[str] = "1.0"
SCHEMA_MAJOR: Final[int] = 1

EVENT_TYPE: Final[str] = "site.post_1c_monitor"
ENVIRONMENT_DEFAULT: Final[str] = "production"

SITE_ID: Final[str] = "SITE-002"
SITE_NAME: Final[str] = "╨Ч╨Я╨Ь"
SITE_DOMAIN: Final[str] = "bzpm.ru"

PRODUCER_NAME: Final[str] = "ocpilot.site-002.post-1c-exporter"
PRODUCER_VERSION: Final[str] = "1.0"

# Fixed non-secret UUID v5 namespace for Client Ops report event identity.
# Documented for determinism; not derived from credentials.
MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID: Final[str] = (
    "8f3c2a91-6b4e-4d7a-9c1f-2e5a8b0d4f67"
)

DISPLAY_TIMEZONE: Final[str] = "Europe/Moscow"
EVENT_TITLE: Final[str] = "Post-1C monitor"

REQUIRED_ARTIFACTS: Final[Sequence[str]] = (
    "monitor-classification.json",
    "changed-summary.json",
    "run-summary.json",
)
OPTIONAL_ARTIFACTS: Final[Sequence[str]] = ("run.log",)

# ---------------------------------------------------------------------------
# Source field aliases (approved only)
# ---------------------------------------------------------------------------

# monitor-classification.json
MONITOR_CLASSIFICATION_ALIASES: Final[Mapping[str, Sequence[str]]] = {
    "classification": ("classification",),
    "onboarding_needs_count": (
        "onboarding_needs_count",
        "onboarding_needed_count",
    ),
    "observed_at": (
        "observed_at",
        "finished_at",
        "captured_at",
        "completed_at",
    ),
}

# changed-summary.json тЖТ envelope metrics
CHANGED_SUMMARY_ALIASES: Final[Mapping[str, Sequence[str]]] = {
    "baseline_count": ("baseline_url_count", "baseline_count"),
    "current_count": ("current_url_count", "current_count"),
    "added_urls": ("added_count", "added_urls"),
    "removed_urls": ("removed_count", "removed_urls"),
    "onboarding_needs_count": (
        "onboarding_needs_count",
        "onboarding_needed_count",
    ),
}

# run-summary.json
RUN_SUMMARY_ALIASES: Final[Mapping[str, Sequence[str]]] = {
    "classification": ("classification",),
    "run_id": ("run_id", "id"),
    "started_at": ("started_at", "start_time"),
    "finished_at": ("finished_at", "completed_at", "end_time"),
    "exit_code": ("exit_code", "return_code"),
    "duration_seconds": ("duration_seconds", "duration_s"),
    "added_count": ("added_count", "added_urls"),
    "onboarding_needs_count": (
        "onboarding_needs_count",
        "onboarding_needed_count",
    ),
}

SUPPORTED_SOURCE_CLASSIFICATIONS: Final[frozenset[str]] = frozenset(
    {
        "NO_ACTION_REQUIRED",
        "ONBOARDING_REQUIRED",
        "HYGIENE_REVIEW_REQUIRED",
        "FAILURE_REVIEW_REQUIRED",
    }
)

NORMALIZED_STATUSES: Final[frozenset[str]] = frozenset(
    {"OK", "ATTENTION", "FAILED", "BLOCKED"}
)

# ---------------------------------------------------------------------------
# Summary / action / reason codes
# ---------------------------------------------------------------------------

SUMMARY_CODES: Final[frozenset[str]] = frozenset(
    {
        "NO_ACTION_REQUIRED",
        "ONBOARDING_REQUIRED",
        "HYGIENE_REVIEW_REQUIRED",
        "SOURCE_EXECUTION_FAILED",
        "SOURCE_REPORT_STALE",
        "SOURCE_ARTIFACT_MISSING",
        "SOURCE_ARTIFACT_MALFORMED",
        "SOURCE_ARTIFACT_CONFLICT",
        "SOURCE_SCHEMA_UNSUPPORTED",
        "SOURCE_TIME_INVALID",
        "ENVELOPE_SECURITY_REJECTED",
    }
)

ACTION_CODES: Final[frozenset[str]] = frozenset(
    {
        "NONE",
        "REVIEW_ONBOARDING",
        "REVIEW_HYGIENE",
        "REVIEW_SOURCE_FAILURE",
        "REVIEW_SCHEDULER_AND_ARTIFACTS",
        "REVIEW_SOURCE_ARTIFACTS",
        "REVIEW_SCHEMA_COMPATIBILITY",
        "REVIEW_SOURCE_TIME",
        "REVIEW_ENVELOPE_SECURITY",
    }
)

REASON_CODES: Final[frozenset[str]] = frozenset(
    {
        # Success / attention informational
        "BASELINE_DELTA_ZERO",
        "BASELINE_DELTA_NONZERO",
        "CATEGORY_PLP_ADDED",
        "ONBOARDING_COUNT_NONZERO",
        "HYGIENE_FLAGS_PRESENT",
        # Failure / blocked
        "SOURCE_EXIT_CODE_NONZERO",
        "SOURCE_CLASSIFICATION_CONFLICT",
        "SOURCE_METRIC_CONFLICT",
        "SOURCE_REQUIRED_ARTIFACT_MISSING",
        "SOURCE_JSON_MALFORMED",
        "SOURCE_REPORT_TOO_OLD",
        "SOURCE_TIME_IN_FUTURE",
        "SOURCE_CLASSIFICATION_UNKNOWN",
        "SOURCE_REQUIRED_FIELD_MISSING",
        "SOURCE_METRIC_NEGATIVE",
        # Contract / algorithm companion codes (Phase 0B)
        "REQUIRED_ARTIFACT_MISSING",
        "JSON_PARSE_FAILED",
        "REQUIRED_FIELD_MISSING",
        "NEGATIVE_METRIC",
        "METRIC_DELTA_INCONSISTENT",
        "CLASSIFICATION_MISMATCH",
        "RUN_SUMMARY_VS_MONITOR_CLASSIFICATION",
        "ONBOARDING_COUNT_CONFLICT",
        "SOURCE_STALE",
        "OBSERVED_AT_IN_FUTURE",
        "OBSERVED_AT_UNPARSEABLE",
        "CLOCK_SKEW_NEGATIVE_AGE",
        "UNSUPPORTED_SOURCE_VOCABULARY",
        "MONITOR_EXECUTION_FAILED",
        "UNKNOWN_PAGE_TYPE",
        # Security
        "ENVELOPE_SECRET_MARKER_DETECTED",
        "ENVELOPE_PATH_DETECTED",
        "ENVELOPE_NOT_REDACTED",
        "SECRET_MARKER_DETECTED",
        "ABSOLUTE_PATH_DETECTED",
        "RAW_LOG_DETECTED",
        "SECURITY_FLAGS_INVALID",
    }
)

# Safe human action texts (no paths, no secrets).
ACTION_TEXT: Final[Mapping[str, str]] = {
    "NONE": "none",
    "REVIEW_ONBOARDING": "╨┐╤А╨╛╨▓╨╡╤А╨╕╤В╤М ╨╜╨╛╨▓╤Л╨╡ ╨▓╨╡╤В╨║╨╕ ╨║╨░╤В╨░╨╗╨╛╨│╨░",
    "REVIEW_HYGIENE": "╨┐╤А╨╛╨▓╨╡╤А╨╕╤В╤М ╤Д╨╗╨░╨│╨╕ ╨│╨╕╨│╨╕╨╡╨╜╤Л ╨║╨░╤В╨░╨╗╨╛╨│╨░",
    "REVIEW_SOURCE_FAILURE": "╨┐╤А╨╛╨▓╨╡╤А╨╕╤В╤М ╤Б╨▒╨╛╨╣ ╨╝╨╛╨╜╨╕╤В╨╛╤А╨░ / ╨╕╤Б╤В╨╛╤З╨╜╨╕╨║╨░",
    "REVIEW_SCHEDULER_AND_ARTIFACTS": (
        "╨┐╤А╨╛╨▓╨╡╤А╨╕╤В╤М ╨┐╨╗╨░╨╜╨╕╤А╨╛╨▓╤Й╨╕╨║ ╨╕ ╤Б╨▓╨╡╨╢╨╡╤Б╤В╤М ╨░╤А╤В╨╡╤Д╨░╨║╤В╨╛╨▓"
    ),
    "REVIEW_SOURCE_ARTIFACTS": (
        "╤Б╨╛╤Б╤В╨╛╤П╨╜╨╕╨╡ ╤Б╨░╨╣╤В╨░ ╨╜╨╡ ╨┐╨╛╨┤╤В╨▓╨╡╤А╨╢╨┤╨╡╨╜╨╛ тАФ ╨┐╤А╨╛╨▓╨╡╤А╨╕╤В╤М ╨╕╤Б╤Е╨╛╨┤╨╜╤Л╨╡ ╨░╤А╤В╨╡╤Д╨░╨║╤В╤Л"
    ),
    "REVIEW_SCHEMA_COMPATIBILITY": (
        "╨┐╤А╨╛╨▓╨╡╤А╨╕╤В╤М ╤Б╨╛╨▓╨╝╨╡╤Б╤В╨╕╨╝╨╛╤Б╤В╤М ╤Б╤Е╨╡╨╝╤Л ╨╕╤Б╤Е╨╛╨┤╨╜╤Л╤Е ╨░╤А╤В╨╡╤Д╨░╨║╤В╨╛╨▓"
    ),
    "REVIEW_SOURCE_TIME": "╨┐╤А╨╛╨▓╨╡╤А╨╕╤В╤М ╨╝╨╡╤В╨║╨╕ ╨▓╤А╨╡╨╝╨╡╨╜╨╕ ╨╕╤Б╤Е╨╛╨┤╨╜╤Л╤Е ╨░╤А╤В╨╡╤Д╨░╨║╤В╨╛╨▓",
    "REVIEW_ENVELOPE_SECURITY": (
        "╨║╨╛╨╜╨▓╨╡╤А╤В ╨╛╤В╨║╨╗╨╛╨╜╤С╨╜ ╨┐╤А╨╛╨▓╨╡╤А╨║╨╛╨╣ ╨▒╨╡╨╖╨╛╨┐╨░╤Б╨╜╨╛╤Б╤В╨╕ тАФ ╨╜╨╡ ╨┐╤Г╨▒╨╗╨╕╨║╨╛╨▓╨░╤В╤М"
    ),
}

FORBIDDEN_ENVELOPE_TOP_LEVEL_KEYS: Final[frozenset[str]] = frozenset(
    {
        "delivery",
        "ai",
        "routing",
        "telegram",
        "chat_id",
        "bot_token",
        "webhook",
        "credentials",
        "secret",
        "secrets",
        "password",
        "token",
        "api_key",
        "openrouter",
        "atlas",
        "source_path",
        "absolute_path",
        "storage_path",
    }
)

# CLI exit codes (Phase 1A charter)
EXIT_SUCCESS: Final[int] = 0
EXIT_SOURCE_BLOCKED: Final[int] = 2
EXIT_USAGE: Final[int] = 3
EXIT_UNSAFE_OUTPUT_PATH: Final[int] = 4
EXIT_INTERNAL: Final[int] = 5
