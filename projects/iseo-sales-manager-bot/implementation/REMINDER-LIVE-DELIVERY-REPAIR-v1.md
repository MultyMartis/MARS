# REMINDER LIVE DELIVERY REPAIR v1

**Phase:** 3H.9  
**Workflow:** Admin.dev only. Operational.dev unchanged.

## Proven failure stage

For 2026-08-17 10:00 and 10:15 Europe/Moscow (and 15–16 Aug 10:00/10:15):

1. `Reminder Schedule Trigger` **TRIGGER_RAN**
2. `Read Reminder CONFIG` failed: Google Sheets OAuth **invalid_grant**
3. `Reminder Classify Sheets Error` labeled **SHEETS_PERMANENT** because it did not read string `json.error`
4. 429 Wait retry **not reached** (error was not 429; retry is ACCESS-429-only)
5. `Reminder Schedule Gate` / current-state selector / claims / Telegram **not executed**
6. `reminder_mark_window_complete=false` — last_window **not** stamped (invariant held)
7. 10:15 **did run**; same CONFIG credential failure — not suppressed by stale last_window

Primary cause: **Sheets credential invalid_grant before evaluation**.  
Secondary: classifier mislabeled credentials as permanent; observability writes also failed on the same credential.

## Patch (narrow)

- Classifier extracts string `json.error` and classifies `invalid_grant` as `SHEETS_CREDENTIALS`.
- No retry on credential errors (retry cannot restore OAuth).
- Still does not mark the business date complete.
- Current-state selector, 10:00 Europe/Moscow, 4 production recipients, no stale ACCESS fallback: unchanged.

Operator must reconnect n8n credential **Google Sheets account (Multy Martis)** before any natural 10:00 can send.

Patch: `implementation/patches/ReminderClassifySheetsError.phase3h9.js`.
