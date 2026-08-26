# PATCH-DESIGN-v1

## Scope

Operational.dev only. No Admin, ACCESS, reminder schedule, AI, poll cadence, or storage migration.

## Changes

1. **Append or Update CLEAN v2:** `appendOrUpdate`, `matchingColumns: [lead_id]`; manager_status mapping preserves lifecycle on `reprocessed`.
2. **Append DEDUP_INDEX:** `appendOrUpdate`, `matchingColumns: [dedup_key]`.
3. **Classify Duplicate:** on `gmailMatch`, do **not** force `manager_status`; set `manager_status` only when `!gmailMatch`.

## Non-goals

- No historical row merge/delete.
- No PostgreSQL / Service Account migration.
- No false-dedupe of distinct SOURCE_EVENT_IDs (match remains `lead_id` / gmail identity).

## Applied

Live Ops `updatedAt` 2026-08-26T11:08:16.779Z; active=true. POST backup SHA256 `dca6b25c...`.
