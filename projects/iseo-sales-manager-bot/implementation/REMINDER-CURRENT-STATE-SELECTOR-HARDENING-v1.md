> **Phase 3H.9 (2026-08-17):** False «Недостаточно прав» on raw lead was ACCESS/CONFIG Google Sheets `invalid_grant` mislabeled as a permission deny. Reminder 10:00 windows 15–17 Aug failed at CONFIG read with the same credential error before evaluation; 429 retry path was not applicable. Admin deny text + Sheets error classifier patched. Live Sheets OAuth reconnect by operator is still required before ADMIN_A raw retest and the next natural 4-recipient 10:00. Soak not restarted. Phase 3I.1 blocked. AI OFF.

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
