# LAST-PROCESSED STATUS READBACK REPAIR v1

**Phase:** 3H.4.1  
**Verdict:** `PHASE 3H.4.1 COMPLETE — STATUS READBACK REPAIRED; FINAL 48-HOUR SOAK RESTARTED`

## Problem

After Phase 3H.4, `/stats` and `/leads` correctly showed one production processed lead (17:22 МСК), but `/status` showed `Последний обработанный лид: нет данных`.

## Root cause

1. Status correctly stopped using synthetic `last_lead_success_at` (22:23 МСК).
2. Phase 3H.4 CONFIG backfill created `last_production_processed_*` keys with **empty values** (webhook body nesting: `processed_at` not read from `body`).
3. Status fail-closed to `нет данных` — correct given empty cache; LEADS truth was never missing.

## Repair (Admin.dev only · same workflow ID · 85 nodes)

1. Status Code → resolver for `iseo-last-production-processed-v1.0` (ISO/Date, Moscow format, exclusions, CONFIG cache, optional LEADS/LEAD_EVENTS hints).
2. CONFIG cache rewritten from authoritative LEADS processed row (no LEADS/LEAD_EVENTS mutation).

## Result

`Последний обработанный лид: 05.08.2026 17:22 МСК`

## Non-goals

- No AI enablement
- No Phase 3I.1
- No reminder / profile / reporting changes
- No Operational.dev topology change
- No production lead rewrite

## Evidence

`evidence/phase3h4-1/`
