/**
 * Phase 1B-D6D — Unattended Monitor-to-Client-Ops Integration constants.
 * OFFLINE contract only. Production enablement remains NO.
 */

export const D6D_PHASE = '1B-D6D';
export const D6D_PRODUCER_SCHEMA_VERSION = 1;
export const D6D_SITE_ID = 'SITE-002';
export const D6D_PRODUCER_IDENTITY = 'mars.client-ops.site-002.unattended-producer';

export const STALE_AFTER_SECONDS = 93600;
export const MAX_FUTURE_SKEW_SECONDS = 300;
export const MAX_AUTOMATIC_RETRIES = 0;
export const AUTOMATIC_RETRIES_ENABLED = false;
export const MAX_SAFE_CONCURRENCY = 1;
export const MAX_CANDIDATES_PER_RUN = 1;

export const AUTHORITATIVE_ARTIFACTS = Object.freeze([
  'run-summary.json',
  'monitor-classification.json',
  'changed-summary.json',
]);

/** Primary authority document within the completed run directory. */
export const AUTHORITATIVE_PRIMARY = 'run-summary.json';

export const COMPLETION_MARKER_FILENAME = 'run-complete.marker';

export const STATUS_MAPPING = Object.freeze({
  NO_ACTION_REQUIRED: 'OK',
  ONBOARDING_REQUIRED: 'ATTENTION',
  HYGIENE_REVIEW_REQUIRED: 'ATTENTION',
  FAILURE_REVIEW_REQUIRED: 'FAILED',
});

export const SOURCE_STATUSES = Object.freeze({
  OK: 'OK',
  ATTENTION: 'ATTENTION',
  FAILED: 'FAILED',
  BLOCKED: 'BLOCKED',
});

export const DELIVERY_ELIGIBILITY = Object.freeze({
  FRESH_AND_ELIGIBLE: 'FRESH_AND_ELIGIBLE',
  STALE_REVIEW_REQUIRED: 'STALE_REVIEW_REQUIRED',
  NOT_SAFE_TO_SEND: 'NOT_SAFE_TO_SEND',
});

export const KILL_SWITCH_MODES = Object.freeze({
  DISABLED: 'DISABLED',
  DRY_RUN: 'DRY_RUN',
  ENABLED: 'ENABLED',
});

export const CURSOR_STATES = Object.freeze({
  DISCOVERED: 'DISCOVERED',
  VALIDATED: 'VALIDATED',
  EVALUATED: 'EVALUATED',
  BLOCKED: 'BLOCKED',
  DELIVERY_ATTEMPT_STARTED: 'DELIVERY_ATTEMPT_STARTED',
  DELIVERY_OUTCOME_AMBIGUOUS: 'DELIVERY_OUTCOME_AMBIGUOUS',
  DELIVERY_TERMINAL: 'DELIVERY_TERMINAL',
  RECONCILIATION_REQUIRED: 'RECONCILIATION_REQUIRED',
  ALREADY_HANDLED: 'ALREADY_HANDLED',
  NO_CANDIDATE: 'NO_CANDIDATE',
  DEFERRED_UNSTABLE: 'DEFERRED_UNSTABLE',
});

/** Numeric exit codes for future scheduler observability (not retry-safe by default). */
export const EXIT_CODES = Object.freeze({
  SUCCESS_NO_CANDIDATE: 0,
  SUCCESS_DRY_RUN: 10,
  SUCCESS_DELIVERED: 11,
  SUCCESS_ALREADY_HANDLED: 12,
  BLOCKED_KILL_SWITCH: 20,
  BLOCKED_STALE: 21,
  BLOCKED_NOT_SAFE: 22,
  BLOCKED_CONFLICT: 23,
  BLOCKED_BOOTSTRAP: 24,
  BLOCKED_OVERLAP: 25,
  RECONCILIATION_REQUIRED: 30,
  FAILED_PREFLIGHT: 40,
  FAILED_ACTIVATION: 41,
  FAILED_READINESS: 42,
  FAILED_REQUEST_AMBIGUOUS: 43,
  FAILED_CONTAINMENT: 44,
  FAILED_LOCAL_STATE: 45,
  FAILED_RUNTIME_CONTRACT: 46,
  FAILED_CONFIG: 47,
});

export const EXIT_CLASS_BY_CODE = Object.freeze(
  Object.fromEntries(Object.entries(EXIT_CODES).map(([k, v]) => [v, k])),
);

export const FORBIDDEN_TEMP_SUFFIXES = Object.freeze([
  '.part',
  '.tmp',
  '.temp',
  '.swp',
  '~',
]);

export const EVENT_TYPE = 'site.post_1c_monitor';
export const SCHEMA_MAJOR = 1;
export const MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID =
  '8f3c2a91-6b4e-4d7a-9c1f-2e5a8b0d4f67';

export const EXPECTED_WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
export const EXPECTED_VERSION_ID = 'dc8746bf-df9c-425d-9b3f-4ace452ac5ef';
export const HISTORICAL_PENDING_EVENT_ID = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
export const D6A2_SENT_EVENT_ID = 'd6a2a001-27d6-4a2e-bd6a-000000000001';

export const REQUIRED_ABC_E_ANCESTORS = Object.freeze([
  '12e4c6ad1f4199458b6f091d084f33ca5f8a965d', // A
  '94d06c05ea79eb22780588d91064006c3edf2a05', // B
  '79c2071dd8ae8096506d45bc189e1f732b310d35', // C
  '7f9fd29fa037939a7f6f13bdb02cb18801bc7fbd', // E
]);

export const FUTURE_PRODUCER_TASK_NAME = 'MARS_SITE_002_Client_Ops_Producer';
export const EXISTING_MONITOR_TASK_NAME = 'MARS_SITE_002_Post_1C_Catalog_Monitor';

export const FUTURE_PRODUCER_RUNTIME =
  'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo';
export const MONITOR_RUNTIME =
  'X:\\AI MARS STORAGE\\runtime-checkouts\\site-002-monitor\\repo';
export const FORBIDDEN_MAIN_ROOT = 'X:\\AI MARS';

export const DEFAULT_ARTIFACT_ALLOWLIST_ROOTS = Object.freeze([
  'X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\scheduled-monitors\\post-1c',
]);

export const GATE_ORDER = Object.freeze([
  'acquire_producer_singleton_lock',
  'verify_kill_switch',
  'discover_candidates',
  'validate_stabilize_artifact',
  'derive_event_identity_fingerprint',
  'inspect_local_cursor',
  'derive_source_status',
  'compute_freshness_eligibility',
  'reject_blocked_stale_not_safe',
  'get_durable_dedupe_ledger',
  'evaluate_retry_reconciliation_policy',
  'build_explicit_lifecycle_charter',
  'acquire_lifecycle_lock',
  'verify_initial_workflow_state',
  'activate',
  'readiness_get',
  'revalidate_freshness_dedupe_policy',
  'send_max_one_request',
  'classify_http_durable_outcome',
  'close_window',
  'deactivate',
  'verify_recontainment',
  'update_sanitized_cursor_receipt',
]);
