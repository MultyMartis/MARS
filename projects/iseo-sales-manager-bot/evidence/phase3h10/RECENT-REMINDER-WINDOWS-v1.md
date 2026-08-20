# RECENT REMINDER WINDOWS — Phase 3H.10

Timezone: **Europe/Moscow**. Inspected natural slots 2026-08-18 … 2026-08-20.

| Exec | MSK | Status | Last node | Classification |
|------|-----|--------|-----------|----------------|
| 34185 | 2026-08-18 10:00 | error | Wait Reminder Sheets Retry | ERROR_BEFORE_DECISION |
| 35004 | 2026-08-19 10:00 | error | Wait Reminder Sheets Retry | ERROR_BEFORE_DECISION |
| 35821 | 2026-08-20 10:00 | error | Wait Reminder Sheets Retry | ERROR_BEFORE_DECISION |
| 35830 | 2026-08-20 10:15 | error | Wait Reminder Sheets Retry | ERROR_BEFORE_DECISION |
| 35838 | 2026-08-20 10:30 | success | Apply Reminder Window CONFIG Write | SHOULD_SKIP (OUTSIDE_WINDOW) |

## Pattern (all 10:00 / 10:15 SHOULD-evaluate slots)

1. Schedule trigger **TRIGGER_RAN**
2. CONFIG read **HEALTHY**
3. Gate proceeds into evaluation window
4. CLEAN read **HEALTHY**
5. ACCESS_CONTROL read → **RATE_LIMIT_429**
6. Classify → retry path
7. **Wait Reminder Sheets Retry** fails: invalid `dateTime` → execution **error**
8. Claims **0** · Telegram attempts **0** · selector not completed

10:30 slot: gate returns `SKIPPED_OUTSIDE_WINDOW` (success path, no send).

Pending count at failing windows: **not_computed** (Build Claims / selector not reached after Wait failure).
