# REAL-DUPLICATE-END-TO-END-v1

## Selected cluster

`lead_19fcce0e42028e45` — 16 CLEAN rows, **1** `source_message_id` = `19fcce0e42028e45`, created ~every 30s on 2026-08-04 13:05:36→13:13:12. Parser stamp on rows: `sm-parser-v3.2` (historical). Classification: PRODUCTION_REAL_DUPLICATE.

## Proven chain (current architecture applied to historical pattern)

1. **Gmail/source event** — single Gmail message id (SOURCE_EVENT_ID).
2. **Poll execution** — Ops Gmail poll (historical cadence/overlap possible; ~30s spacing matches repeated processing, not new mail).
3. **RAW write** — Ops RAW path (not mutated this wave).
4. **Parser** — sm-parser family → `lead_id` = `lead_` + message id (same id every time).
5. **Dedupe guard** — Classify Duplicate *can* set `reprocessed` if DEDUP hit; historical rows show `duplicate_status=new` → DEDUP miss and/or race; **regardless**, next node always appended.
6. **CLEAN write** — node named "Append or Update CLEAN v2" but operation was **`append`** with empty matchingColumns → **always new row**.
7. **Ledger/DEDUP** — Append DEDUP_INDEX also **`append`** only → duplicate index rows possible.
8. **Subsequent duplicate write** — next poll/retry repeats steps 4–7 → +1 CLEAN row same `lead_id`.

## Root class

`DEDUP_GUARD_BYPASSED` + `RETRY_REAPPEND` / always-append (live path defect).

## Not this incident

- Not two distinct Gmail events (`unique_sid=1`).
- Not Admin callback writing new CLEAN leads.
- Not display-name collision.
