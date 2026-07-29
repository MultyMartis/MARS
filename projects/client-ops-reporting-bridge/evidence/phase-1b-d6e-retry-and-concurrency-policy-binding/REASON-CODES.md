# REASON-CODES

**Token:** `D6E_REASON_CODES_DEFINED`

Stable codes from `client-ops-retry-reason-codes.mjs`:

| Code | Notes |
|------|-------|
| `PRE_TRANSMISSION_SEMANTIC_FAILURE` | Pre-tx semantic reject → FINAL_FAILURE |
| `PRE_TRANSMISSION_TRANSIENT_NO_SIDE_EFFECT` | Pre-tx transient, no side effect → SAFE_TO_RETRY class (charter still required) |
| `PRE_TRANSMISSION_CHARTER_OR_READINESS` | Charter/readiness block pre-tx |
| `SOURCE_NOT_ELIGIBLE` | delivery_eligibility NOT_SAFE_TO_SEND |
| `SOURCE_STALE_REVIEW_REQUIRED` | STALE_REVIEW_REQUIRED blocks retry |
| `AMBIGUOUS_TRANSPORT` | Transport acceptance unknown |
| `HTTP_202_SENT_TERMINAL` | 202 + SENT |
| `HTTP_202_PENDING_RECONCILE` | 202 + PENDING |
| `HTTP_202_FAILED_TERMINAL` | 202 + FAILED |
| `HTTP_200_DUPLICATE_SENT` | 200 duplicate + SENT |
| `HTTP_200_DUPLICATE_PENDING` | 200 duplicate + PENDING |
| `HTTP_200_DUPLICATE_FAILED` | 200 duplicate + FAILED |
| `EVENT_CONFLICT` | HTTP 409 |
| `HTTP_AUTH_REJECTED` | 401/403 |
| `HTTP_VALIDATION_REJECTED` | 400/422 |
| `WORKFLOW_INACTIVE_BEFORE_POST` | 404 / inactive before POST |
| `HTTP_5XX_CLAIM_UNKNOWN` | 5xx; claim unknown → reconcile |
| `NO_ROW_AMBIGUOUS` | No row + non-authoritative absence |
| `NO_ROW_AUTHORITATIVE_NO_INTAKE` | Authoritative no-intake proof |
| `PENDING_NEVER_AUTO_RETRY` | PENDING never auto-retried |
| `ALREADY_SENT` | SENT terminal |
| `DELIVERY_FAILED_TERMINAL` | FAILED terminal (no auto-retry) |
| `TELEGRAM_SUCCESS_LEDGER_PENDING` | Telegram SUCCESS + PENDING fails closed |
| `TELEGRAM_UNKNOWN_PENDING` | Telegram UNKNOWN + PENDING → reconcile |
| `TELEGRAM_FAILED_TERMINAL` | Telegram definite failure + FAILED |
| `CONTAINMENT_FAILED` | Containment failure blocks retry |
| `CONTAINMENT_ANOMALY_SENT_TERMINAL` | Recontain anomaly + SENT |
| `CONTAINMENT_ANOMALY_PENDING_RECONCILE` | Recontain anomaly + PENDING |
| `SAME_EVENT_CONCURRENCY_FORBIDDEN` | Same-event parallel forbidden |
| `GLOBAL_CONCURRENCY_LIMIT` | Different-event / session concurrency=1 |
| `LIFECYCLE_LOCK_HELD` | Lifecycle lock held by other |
| `REQUEST_BUDGET_EXHAUSTED` | Request budget exhausted |
| `RETRY_CHARTER_REQUIRED` | Explicit retry charter missing/invalid |
| `RETRY_CHARTER_EVENT_MISMATCH` | Charter event_id mismatch |
| `RETRY_CHARTER_SOURCE_MISMATCH` | Charter source fingerprint mismatch |
| `RETRY_BUDGET_EXHAUSTED` | Manual retry budget < 1 |
| `NEW_SOURCE_RUN_NOT_RETRY` | New source run is not a retry |
| `HISTORICAL_PENDING_BLIND_RETRY_PROHIBITED` | Historical PENDING + Telegram success evidence |
| `RESPONSE_LOST_SENT_TERMINAL` | Response lost + SENT |
| `RESPONSE_LOST_FAILED_TERMINAL` | Response lost + FAILED |
| `RESPONSE_LOST_PENDING_RECONCILE` | Response lost + PENDING |
| `EVIDENCE_SANITIZED_OK` | Evidence sanitization marker |
