# FUNCTION-TESTS-v1

**Harness:** `tests/iseo_sales/04_extended_local_validation.sql`  
**Result:** PASS

| Function | Valid | Duplicate/idempotent | Invalid | Event/audit side effects |
|----------|-------|----------------------|---------|--------------------------|
| register_inbound_event | PASS | PASS | PASS | PASS |
| upsert_lead | PASS | PASS | PASS | PASS |
| change_lead_status | PASS | PASS (idempotency key) | PASS (stale version/status) | PASS |
| enqueue_delivery | PASS | covered | PASS | delivery row only (no Telegram) |
| enqueue_job | PASS | covered | PASS | job row state |

**Notes (test harness fixes only — not migration SQL):**

- `enqueue_delivery` call order aligned to `(lead_id, channel, …)`.
- PL/pgSQL variable rename to avoid ambiguous `lead_id`.
- Unique run IDs via `gen_random_uuid()` to avoid fixture pollution across re-runs.
