# REMINDER CURRENT-STATE SELECTOR HARDENING v1

**Phase:** 3H.8.2.2  
**Admin.dev:** `wLrLp4WQHm1VJmxz` (same ID; 92 nodes)

## Change

- Replaced first-row pending dedupe in `Reminder Build Claims` with `iseo-reminder-current-state-selector-v1.0`.
- Library: `implementation/runtime-libs/reminder-current-state-selector-v1.mjs`
- Inline production Code mirror: `implementation/patches/ReminderBuildClaims.phase3h822.js`
- Observability: Mark Window Complete + `/reminder_status` counters (raw / unique / authoritative / SAFE_UNKNOWN)

## Non-goals (deferred)

`KNOWN FOLLOW-UP — CLEAN DUPLICATE ROW PRODUCTION SOURCE FORENSIC` — no row delete/compaction.

## Regression

Phase 3H.8.2 Sheets 429 resilience retained. Exactly-once claims unchanged. Operational.dev untouched.
