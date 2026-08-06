# REMINDER CONFIG INVARIANTS v1

## Production CONFIG (post-repair)

| Key | Expected value |
|---|---|
| `pending_reminders_enabled` | true |
| `pending_reminder_time` | 10:00 |
| `pending_reminder_timezone` | Europe/Moscow |
| `pending_reminder_min_count` | 1 |
| `pending_reminder_include_tests` | false |
| `pending_reminder_active_recipients_count` | **3** (backfilled in 3H.4) |

## Invariants

1. Reminder source sheet = **LEADS** (not lead_clean_v2)
2. Active recipients only; revoked (Nikita) excluded from delivery set
3. Zero pending → zero sends (fail-closed suppression armed)
4. `/reminder_status` must never go silent on recognized command
5. Admin long-form and moderator short-form paths both syntactically valid post-repair

## Backfill note (Phase 3H.4)

`pending_reminder_active_recipients_count=3` corrected in CONFIG to match live ACCESS_CONTROL active card recipients.

## Contract reference

`architecture/DAILY-PENDING-REMINDER-CONTRACT-v1.md`
