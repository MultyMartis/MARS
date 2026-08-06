# STATUS READBACK ROOT CAUSE v1

## Defect class

**CONFIG cache write produced empty values; Status fail-closed correctly.**

## Exact cause

1. Phase 3H.4 Status patch stopped using synthetic `last_lead_success_at` (22:23 МСК) — correct.
2. Phase 3H.4 CONFIG backfill created keys `last_production_processed_at` / `last_production_processed_lead_id` (and aligned `last_processed_*`) with **empty `value` cells**.
3. Root of empty write: backfill webhook body nesting — Prep Rows read `.first().json.processed_at` but n8n Webhook placed payload under `body`, so values became `''`.
4. Status resolver saw empty production keys → `нет данных`.
5. Production LEADS row remained authoritative and unchanged (processed @ 2026-08-05T14:22:55.186Z = 17:22 МСК).

## Not causes

- Production lead missing
- Stats/leads wrong
- Timestamp parser rejecting valid ISO (never reached a non-empty value)
- Hardcoded date
