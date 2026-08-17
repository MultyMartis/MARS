> **Phase 3H.9 (2026-08-17):** False «Недостаточно прав» on raw lead was ACCESS/CONFIG Google Sheets `invalid_grant` mislabeled as a permission deny. Reminder 10:00 windows 15–17 Aug failed at CONFIG read with the same credential error before evaluation; 429 retry path was not applicable. Admin deny text + Sheets error classifier patched. Live Sheets OAuth reconnect by operator is still required before ADMIN_A raw retest and the next natural 4-recipient 10:00. Soak not restarted. Phase 3I.1 blocked. AI OFF.

# REMINDER SHEETS 429 RESILIENCE v1

> **Phase 3H.8.2.2 (2026-08-14):** Reminder pending eligibility uses `iseo-reminder-current-state-selector-v1.0` — unique `lead_id` → authoritative current status → eligibility. First CLEAN pending row no longer wins. Production Reminder Build Claims adds no per-lead Sheets calls. Duplicate CLEAN row source forensic is deferred. Real 10:00 acceptance still pending.


**Phase:** 3H.8.2  
**Workflow:** Admin.dev `wLrLp4WQHm1VJmxz` (92 nodes after patch)  
**Contract:** `iseo-sheets-429-retry-v1.0`

## Proven defect

Real window **2026-08-14 10:00 Europe/Moscow**:

- exec **30813** — CLEAN succeeded; ACCESS HTTP 429; `ERROR_BEFORE_DECISION`; claims=0; Telegram=0; `last_window` not stamped.
- exec **30821** (10:15) — same ACCESS 429. Window is 20 minutes; 10:15 is a same-window recovery slot.

Root class: `REMINDER_EVALUATION_ABORTED_BY_SHEETS_429`.

## Patch (Admin.dev only)

Added nodes:

- `Reminder Classify Sheets Error`
- `IF Reminder Sheets Retry`
- `Wait Reminder Sheets Retry`
- `Reminder Stamp Sheets Error`
- `Append ERRORS Reminder 429`

ACCESS error output → Classify → IF retry? → Wait → **same** `Read ACCESS_CONTROL for Reminder`.  
Else → Stamp → Append ERRORS → `Reminder Mark Window Complete` **without** `last_window`.

Operational.dev unchanged. No new persistent workflows. Reminder time remains 10:00.

## Same-window recovery

Schedule interval: 15 minutes. Gate window: 20 minutes from configured time.

Allowed evaluations for 10:00: **10:00** and **10:15**. 10:30 is `outside_window`.

A 10:00 transient 429 can recover by:

1. bounded retries inside the 10:00 execution; and/or
2. the 10:15 scheduled evaluation if no successful send claim / `last_window` exists.

## Observability

On pre-decision ERROR:

- `pending_reminder_last_evaluation_at`
- `pending_reminder_last_decision` = `ERROR` (or `ERROR_SHEETS_429_ACCESS` class on the error fields)
- `pending_reminder_last_error_class` / `_stage` / `_at` / `_safe`
- `pending_reminder_last_retry_attempts`
- `pending_count` = `not_computed` when ACCESS/CLEAN never completed

Not stamped on failed runs: `last_window`, `last_success_at`, sent recipient count.

`/reminder_status` shows: Состояние / Время / Часовой пояс / Получателей / Последняя проверка / Последнее решение: Ошибка / Этап / Причина: лимит Google Sheets API / Повторные попытки.

## Patches (Git copies of live Code)

- `implementation/patches/ReminderClassifySheetsError.phase3h82.js`
- `implementation/patches/ReminderStampSheetsError.phase3h82.js`
- `implementation/patches/ReminderMarkWindowComplete.phase3h82.js`
- `implementation/patches/ReminderCommands.phase3h82.js`

## Harness

`implementation/harness/phase3h82-sheets-429-harness.mjs` — 23/23 PASS. Isolated; no production customer data.
