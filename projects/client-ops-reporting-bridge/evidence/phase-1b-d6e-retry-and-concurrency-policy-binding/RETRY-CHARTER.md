# RETRY-CHARTER

**Token:** `D6E_EXPLICIT_RETRY_CHARTER_DEFINED`

Module: `client-ops-retry-charter.mjs`

Required for any future manual `SAFE_TO_RETRY` path:

- `schema_version=1`, unique `charter_id`
- `retry_decision=SAFE_TO_RETRY`
- `automatic_retry=false`, `unattended=false`, `consumed=false`
- `max_retry_attempts=1`, `max_concurrency=1`
- `controlled_lifecycle_required=true`, `freshness_recheck_required=true`
- matching `event_id` + `source_identity_fingerprint`
- non-expired `expires_at_ms`, `retry_budget_remaining>=1`

D6E validates charters offline; **never** sets `retry_authorized=true` for execution.
