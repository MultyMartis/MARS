# ROOT-CAUSE-PROVEN-v1

## Exact duplicate cluster

`lead_19fcce0e42028e45` (16 CLEAN / 1 SOURCE_EVENT_ID). Confirmed sibling pattern: `lead_19fb7df740e51e26` (6/1).

## Source event identity

Gmail message id = CLEAN `source_message_id` = `19fcce0e42028e45`.

## First write / duplicate write

First CLEAN append ~2026-08-04 13:05:36; subsequent appends same `lead_id` through 13:13:12.

## Exact node/path responsible

Operational.dev `xSnXPy8cEHoZw6xG` → **Append or Update CLEAN v2** with `operation: append` and empty `matchingColumns` after Classify Duplicate. No IF gate stopping reprocess from reaching append.

## Guard that should have prevented it

DEDUP-IMPLEMENTATION-SPEC-v1 §5: same `gmail_message_id` → update CLEAN, **do not append**. DEDUP_INDEX upsert by `dedup_key`.

## Why guard failed/bypassed

1. Sheets node always appended despite "Append or Update" name.
2. Classify `reprocessed` did not divert write path.
3. DEDUP_INDEX also append-only → weak second barrier.
4. Historical rows marked `new` show DEDUP miss/race compounded the defect; **even with DEDUP hit**, append would still duplicate.

## Current vs historical

**Bug is CURRENT** (proven in live PRE backup 2026-08-26). Historical clusters are symptoms; live path could still reproduce until patched.

## Classes

`DEDUP_GUARD_BYPASSED`, `RETRY_REAPPEND`, `LEDGER_WRITE_AFTER_CLEAN_WRITE` risk (DEDUP after CLEAN), `EXACTLY_ONCE_LEDGER_NOT_CHECKED`.
