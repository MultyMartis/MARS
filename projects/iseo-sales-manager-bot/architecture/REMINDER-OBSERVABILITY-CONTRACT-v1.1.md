> **Phase 3H.9 (2026-08-17):** False «Недостаточно прав» on raw lead was ACCESS/CONFIG Google Sheets `invalid_grant` mislabeled as a permission deny. Reminder 10:00 windows 15–17 Aug failed at CONFIG read with the same credential error before evaluation; 429 retry path was not applicable. Admin deny text + Sheets error classifier patched. Live Sheets OAuth reconnect by operator is still required before ADMIN_A raw retest and the next natural 4-recipient 10:00. Soak not restarted. Phase 3I.1 blocked. AI OFF.

> **Phase 3H.8.2.2 (2026-08-14):** Reminder pending eligibility uses `iseo-reminder-current-state-selector-v1.0` — unique `lead_id` → authoritative current status → eligibility. First CLEAN pending row no longer wins. Production Reminder Build Claims adds no per-lead Sheets calls. Duplicate CLEAN row source forensic is deferred. Real 10:00 acceptance still pending.

<!-- Phase 3H.8.2 addendum 2026-08-14 -->
## Phase 3H.8.2 addendum

- Contract: `iseo-sheets-429-retry-v1.0` on reminder-critical Sheets reads (Admin.dev only).
- ACCESS_CONTROL 429: explicit Wait 5s/15s/30s loop (max 4 attempts); fail closed `ERROR_SHEETS_429_ACCESS`; no stale ACCESS send fallback.
- `/reminder_status` exposes ERROR + stage + quota reason + retry count.
- Soak remains: **INTERRUPTED — REAL REMINDER WINDOW FAILED ON SHEETS 429** (not restarted).
- Next live acceptance: **2026-08-15 10:00 Europe/Moscow** with `REMINDER_ACCEPTANCE_LEAD_2` left pending.
- Do not claim REMINDER LIVE PASS until that scheduled window succeeds.
- Phase 3I.1 blocked; AI OFF; Admin **92** nodes; Ops **45**; v2 inactive.
- Evidence: [evidence/phase3h82/](evidence/phase3h82/) · Report: [reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md)

# REMINDER OBSERVABILITY CONTRACT v1.1

**Product:** i-SEO Sales Manager Bot  
**Contract id:** `iseo-reminder-observability-v1.1`  
**Phase:** 3H.8

`/reminder_status` must expose (no secrets/PII):

- enabled
- schedule time
- timezone
- minimum pending
- eligible recipients count
- last evaluation timestamp
- pending count at last evaluation
- last decision: `SENT` | `SKIPPED_ZERO_PENDING` | `SKIPPED_ALREADY_SENT` | `ERROR` (plus explicit skip classes if recorded)
- last successful send timestamp
- last successful send recipient count
- current active error if any

CONFIG keys (observability/cache only; evaluation must use live CLEAN):
- `pending_reminder_last_evaluation_at`
- `pending_reminder_last_decision`
- `pending_reminder_last_pending_count`
- `pending_reminder_last_success_at`
- `pending_reminder_last_recipient_count`
- `pending_reminder_last_window` (only after successful window completion)
- `pending_reminder_last_error_safe`
- `pending_reminder_last_error_class`
- `pending_reminder_last_error_stage`
- `pending_reminder_last_error_at`
- `pending_reminder_last_retry_attempts`

ERROR evaluations must not stamp `pending_reminder_last_window` / last successful send. ACCESS 429 exhaustion is `ERROR_SHEETS_429_ACCESS` (fail closed; no stale recipients).

