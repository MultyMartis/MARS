# FINALIZER-UPDATE-MODEL

**Classification:** `D6A_FINALIZER_UPDATE_MODEL=LOOKUP_VALIDATE_UPDATE_SEQUENTIAL_ONLY`

## Rationale

- n8n Data Table has update with filters (`event_id` + `delivery_state=PENDING`).
- Native atomic CAS under concurrency is **not proven** (D1: SAFE UNKNOWN).
- Current max safe concurrency remains **1**.

## Offline / workflow behavior

1. Lookup/validate current row semantics in Code classifier + transition rules.
2. Update filtered to `delivery_state=PENDING` (soft conditional).
3. If already SENT/FAILED, filter matches 0 rows → safe no-op at table layer; pure finalizer returns `ALREADY_FINALIZED` for idempotent calls.

Do **not** claim `ATOMIC_CONDITIONAL` until proven under concurrency (workstream E).
