"""Phase 1B-D2 sequential runtime producer constants (offline).

Real HTTP dispatch is FORBIDDEN in D2. Automatic retries default to 0.
"""

from __future__ import annotations

from typing import Final, Mapping

# ---------------------------------------------------------------------------
# Phase / activation gates
# ---------------------------------------------------------------------------

D2_PHASE_ID: Final[str] = "1B-D2"
D3_PHASE_ID: Final[str] = "1B-D3"
NETWORK_DISPATCH_NOT_AUTHORIZED_D2: Final[str] = (
    "NETWORK_DISPATCH_NOT_AUTHORIZED_D2"
)
NETWORK_DISPATCH_NOT_AUTHORIZED_D3: Final[str] = (
    "NETWORK_DISPATCH_NOT_AUTHORIZED_D3"
)
D3_ACTIVATION_GATE: Final[str] = "PHASE_1B_D3_CONTROLLED_CONNECTION_CHARTER"

# D3 confirmation phrases (exact match required for live HTTP)
D3_ENABLE_PHRASE: Final[str] = (
    "ENABLE CLIENT OPS CONTROLLED PRODUCER HTTP D3 BZPM"
)
D3_ACTIVATE_PHRASE: Final[str] = (
    "ACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM"
)
D3_SEND_FIRST_PHRASE: Final[str] = (
    "SEND ONE CLIENT OPS PRODUCER FIRST SEEN D3 BZPM"
)
D3_SEND_REPLAY_PHRASE: Final[str] = (
    "SEND ONE CLIENT OPS PRODUCER EXACT REPLAY D3 BZPM"
)
D3_DEACTIVATE_PHRASE: Final[str] = (
    "DEACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM"
)
D3_EMERGENCY_DEACTIVATE_PHRASE: Final[str] = (
    "EMERGENCY DEACTIVATE CLIENT OPS PRODUCER D3 BZPM"
)

D3_PRODUCER_MARKER: Final[str] = "mars-client-ops-producer-live-d3"
D3_MAX_REAL_REQUESTS: Final[int] = 2
D3_ALLOWED_ENVIRONMENTS: Final[frozenset[str]] = frozenset(
    {"sandbox", "sandbox_controlled"}
)
D3_APPROVED_HOST: Final[str] = "n8n.ai-metacode.com"
D3_ROUTE_PREFIX: Final[str] = "/webhook/"
D3_RUNS_REL: Final[str] = "runs/d3-controlled-live"
D3_CHARTER_STATE_FILENAME: Final[str] = "charter-state.json"
D3_ENVELOPE_FILENAME: Final[str] = "d3-synthetic-envelope.json"

AUTH_HEADER_NAME: Final[str] = "X-MARS-Client-Ops-Token"
CONTENT_TYPE_JSON: Final[str] = "application/json"

# Transport modes (D2)
TRANSPORT_DISABLED: Final[str] = "disabled"
TRANSPORT_FIXTURE: Final[str] = "fixture"
TRANSPORT_MOCK: Final[str] = "mock"
TRANSPORT_HTTP: Final[str] = "http"  # future-only; blocked in D2

D2_ALLOWED_TRANSPORTS: Final[frozenset[str]] = frozenset(
    {TRANSPORT_DISABLED, TRANSPORT_FIXTURE, TRANSPORT_MOCK}
)

# Local config key names (values never committed)
SECRET_KEY_WEBHOOK_AUTH: Final[str] = "CLIENT_OPS_WEBHOOK_AUTH_SECRET"
PROFILE_KEYS: Final[frozenset[str]] = frozenset(
    {
        "webhook_base",
        "webhook_route",
        "request_timeout_ms",
        "connect_timeout_ms",
        "environment",
        "site_id",
        "max_retries",
        "concurrency",
        "host_class",
    }
)

# Timeout defaults / bounds (milliseconds)
DEFAULT_CONNECT_TIMEOUT_MS: Final[int] = 5_000
DEFAULT_REQUEST_TIMEOUT_MS: Final[int] = 30_000
MIN_TIMEOUT_MS: Final[int] = 100
MAX_TIMEOUT_MS: Final[int] = 120_000
DEFAULT_MAX_RETRIES: Final[int] = 0  # automatic retries disabled
DEFAULT_CONCURRENCY: Final[int] = 1
DEFAULT_HOST_CLASS: Final[str] = "n8n-client-ops"
DEFAULT_ENVIRONMENT: Final[str] = "sandbox"

# Local ignored paths (relative to repo local/)
LOCAL_SITE_REL: Final[str] = "client-ops-reporting-bridge/bzpm.ru"
SECRETS_FILENAME: Final[str] = "secrets.local.env"
PRODUCER_PROFILE_FILENAME: Final[str] = "producer.local.json"
RUNS_DIRNAME: Final[str] = "runs"

# Response / failure classifications
CLASS_HTTP_202_INTAKE_ACCEPTED: Final[str] = "HTTP_202_INTAKE_ACCEPTED"
CLASS_HTTP_200_DUPLICATE_SUPPRESSED: Final[str] = "HTTP_200_DUPLICATE_SUPPRESSED"
CLASS_HTTP_409_EVENT_ID_CONFLICT: Final[str] = "HTTP_409_EVENT_ID_CONFLICT"
CLASS_HTTP_400_AUTH_OR_VALIDATION: Final[str] = "HTTP_400_AUTH_OR_VALIDATION"
CLASS_HTTP_401_403_AUTH: Final[str] = "HTTP_401_403_AUTH"
CLASS_HTTP_5XX: Final[str] = "HTTP_5XX"
CLASS_CONNECT_FAILURE: Final[str] = "CONNECT_FAILURE"
CLASS_DNS_FAILURE: Final[str] = "DNS_FAILURE"
CLASS_TLS_FAILURE: Final[str] = "TLS_FAILURE"
CLASS_READ_TIMEOUT_AMBIGUOUS: Final[str] = "READ_TIMEOUT_AMBIGUOUS"
CLASS_NETWORK_UNKNOWN: Final[str] = "NETWORK_UNKNOWN"
CLASS_WORKFLOW_INACTIVE: Final[str] = "WORKFLOW_INACTIVE"
CLASS_UNEXPECTED_RESPONSE: Final[str] = "UNEXPECTED_RESPONSE"
CLASS_MALFORMED_RESPONSE: Final[str] = "MALFORMED_RESPONSE"
CLASS_TRANSPORT_DISABLED: Final[str] = "TRANSPORT_DISABLED"
CLASS_DISPATCH_NOT_AUTHORIZED: Final[str] = "DISPATCH_NOT_AUTHORIZED"

# Retry decisions
RETRY_NONE: Final[str] = "NONE"
RETRY_TERMINAL_SUCCESS: Final[str] = "TERMINAL_SUCCESS"
RETRY_TERMINAL_FAILURE: Final[str] = "TERMINAL_FAILURE"
RETRY_FUTURE_ELIGIBLE: Final[str] = "FUTURE_RETRY_ELIGIBLE"
RETRY_MANUAL_DEDUPE_CHECK_REQUIRED: Final[str] = "MANUAL_DEDUPE_CHECK_REQUIRED"
RETRY_NOT_AUTHORIZED_D2: Final[str] = "NOT_AUTHORIZED_D2"

# Business / dedupe results (producer-visible)
BUSINESS_INTAKE_ACCEPTED: Final[str] = "INTAKE_ACCEPTED"
BUSINESS_DUPLICATE_SUPPRESSED: Final[str] = "DUPLICATE_SUPPRESSED"
BUSINESS_EVENT_ID_CONFLICT: Final[str] = "EVENT_ID_CONFLICT"
BUSINESS_REJECTED: Final[str] = "REJECTED"
BUSINESS_ERROR: Final[str] = "ERROR"
BUSINESS_AMBIGUOUS: Final[str] = "AMBIGUOUS_ACCEPTANCE"
BUSINESS_NOT_DISPATCHED: Final[str] = "NOT_DISPATCHED"

DEDUPE_FIRST_SEEN: Final[str] = "FIRST_SEEN"
DEDUPE_DUPLICATE: Final[str] = "DUPLICATE"
DEDUPE_CONFLICT: Final[str] = "EVENT_ID_CONFLICT"
DEDUPE_UNKNOWN: Final[str] = "UNKNOWN"
DEDUPE_NA: Final[str] = "NA"

# Mock fixture names → classification seeds
MOCK_FIXTURE_NAMES: Final[Mapping[str, str]] = {
    "202_accepted": CLASS_HTTP_202_INTAKE_ACCEPTED,
    "200_duplicate_suppressed": CLASS_HTTP_200_DUPLICATE_SUPPRESSED,
    "409_event_id_conflict": CLASS_HTTP_409_EVENT_ID_CONFLICT,
    "400_validation": CLASS_HTTP_400_AUTH_OR_VALIDATION,
    "403_auth": CLASS_HTTP_401_403_AUTH,
    "500_internal": CLASS_HTTP_5XX,
    "connect_failure": CLASS_CONNECT_FAILURE,
    "dns_failure": CLASS_DNS_FAILURE,
    "tls_failure": CLASS_TLS_FAILURE,
    "read_timeout_ambiguous": CLASS_READ_TIMEOUT_AMBIGUOUS,
    "malformed_response": CLASS_MALFORMED_RESPONSE,
    "unexpected_response": CLASS_UNEXPECTED_RESPONSE,
    "workflow_inactive": CLASS_WORKFLOW_INACTIVE,
    "network_unknown": CLASS_NETWORK_UNKNOWN,
}

# Allowlist for producer-side normalized input (beyond artifact pipeline)
PRODUCER_INPUT_ALLOWLIST: Final[frozenset[str]] = frozenset(
    {
        "site_id",
        "domain",
        "observed_at",
        "event_type",
        "status",
        "normalized_status",
        "source_status",
        "summary_code",
        "reason_codes",
        "action_code",
        "action_required",
        "action_text",
        "run_id",
        "metrics",
        "freshness",
        "producer",
        "schema_name",
        "schema_version",
        "environment",
        "security",
        "generated_at",
    }
)

RAW_MONITOR_FORBIDDEN_KEYS: Final[frozenset[str]] = frozenset(
    {
        "path",
        "paths",
        "filepath",
        "file_path",
        "absolute_path",
        "source_path",
        "storage_path",
        "ftp_password",
        "sftp_password",
        "db_password",
        "database_password",
        "password",
        "passwd",
        "secret",
        "secrets",
        "token",
        "api_key",
        "authorization",
        "cookie",
        "cookies",
        "stack_trace",
        "traceback",
        "raw_sql",
        "sql",
        "env",
        "environment_variables",
        "hostname_user",
        "username",
        "local_user",
        "command_output",
        "raw_log",
        "raw_output",
        "file_contents",
        "hosting_id",
        "ftp_host",
        "ssh_key",
        "private_key",
    }
)

# CLI exit for blocked live dispatch
EXIT_NETWORK_NOT_AUTHORIZED: Final[int] = 6
EXIT_CONCURRENCY_REJECTED: Final[int] = 7
EXIT_CONFIG_INVALID: Final[int] = 8
