# CLEAN-WRITER-INVENTORY-v1

**Workflows:** Operational.dev `xSnXPy8cEHoZw6xG`; Admin.dev `wLrLp4WQHm1VJmxz`  
**Status:** ALL CURRENT CLEAN WRITERS ACCOUNTED FOR

## Operational.dev (ingest owner)

| Node | Op (pre→post) | Target | Trigger | Guard | Idempotency | Can run twice same event? |
|------|---------------|--------|---------|-------|-------------|---------------------------|
| Append or Update CLEAN v2 | append → **appendOrUpdate** match `lead_id` | CLEAN sheet | Gmail poll → parse → classify | Classify Duplicate + DEDUP lookup | `lead_id` match | Yes (poll/retry) — now upsert-safe |
| Append DEDUP_INDEX | append → **appendOrUpdate** match `dedup_key` | DEDUP_INDEX | after CLEAN | Classify keys | `dedup_key` | Yes — now upsert-safe |
| Classify Duplicate | code | in-memory | after DEDUP lookup | sets reprocessed/repeat/possible | n/a | Always runs; post-patch preserves lifecycle on gmailMatch |

Parser: `sm-parser-v3.3`. Heartbeat: `iseo-gmail-poll-heartbeat-v1.0`. Poll ~2 min. Single-flight lock present (not changed this wave).

## Admin.dev (lifecycle)

| Node class | Op | Target | Notes |
|------------|-----|--------|-------|
| Read CLEAN* | read | CLEAN | many reads (callback/reminder) |
| Update CLEAN (callback paths) | update | CLEAN | status/group/claim fields — **not** ingest append of new leads |

Admin `updatedAt` 2026-08-26T09:48:03Z — **unchanged** by this wave's Ops patch (11:08:16Z).

## Explicit non-writers for ingest duplicates

- Callback paths: update existing rows.
- Reminder paths: read + Telegram; no CLEAN append for new leads.
- No migration/test admin append path left active for production ingest.

## Verdict

Ingest duplicates originate from **Ops Append CLEAN** always-`append` + missing reprocess branch — not from Admin.
