# REMINDER CONFIG CONTRACT v1

**Version key:** `pending_reminder_version = sm-pending-reminder-v1.0`.

## CONFIG keys (additive; CLEAN workbook `CONFIG` tab)

| Key | Default | Type | Mutable by |
|---|---|---|---|
| `pending_reminders_enabled` | `false` | boolean-string | Admin only |
| `pending_reminder_time` | `10:00` | `HH:MM` (24h) | Admin only |
| `pending_reminder_timezone` | `Europe/Moscow` | IANA timezone | Admin only |
| `pending_reminder_min_count` | `1` | integer-string | Admin only |
| `pending_reminder_include_tests` | `false` | boolean-string | Admin only |
| `pending_reminder_last_window` | *(empty)* | window key | system (schedule run) |
| `pending_reminder_last_success_at` | *(empty)* | ISO-8601 | system |
| `pending_reminder_last_recipient_count` | *(empty)* | integer-string | system |
| `pending_reminder_last_pending_count` | *(empty)* | integer-string | system |
| `pending_reminder_last_error_safe` | *(empty)* | safe string | system |
| `pending_reminder_version` | `sm-pending-reminder-v1.0` | string | fixed |

`DEFAULT_REMINDER_CONFIG` in `implementation/runtime-libs/pending-leads-lib.mjs` is the single source of truth for these defaults.

## Validation

- `validateHhMm(s)` — must match `^([01]\d|2[0-3]):([0-5]\d)$`; anything else (e.g. `25:99`) is rejected.
- `validateIanaTimezone(tz)` — must resolve via `Intl.DateTimeFormat` with that `timeZone`; malformed strings (e.g. `Not/AZone`) are rejected.
- Admin commands (`/reminder_time`, `/reminder_timezone`) reject invalid input **without** writing CONFIG — the prior valid value remains in force.

## Mutation authority

Only `/reminder_on`, `/reminder_off`, `/reminder_time`, `/reminder_timezone`, `/reminder_min` mutate these keys, and all five are Admin-only per `authorizePendingCommand` (see [COMMAND-AUTHORIZATION-v1.md](COMMAND-AUTHORIZATION-v1.md)). Moderators may only read status via `/reminder_status`.

## Production state as of Phase 3F.1 closeout

`pending_reminders_enabled=false`; `pending_reminder_time=10:00`; `pending_reminder_timezone=Europe/Moscow` — restored to the safe default after the controlled live acceptance window (see [CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md](CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md)).

## Harness coverage

Checks 20–21, 38–42 in `implementation/harness/phase3f1-harness.mjs`.

*Related: [../../architecture/PENDING-REMINDER-v1.md](../../architecture/PENDING-REMINDER-v1.md), [../../implementation/REMINDER-CONFIG-COMMANDS-v1.md](../../implementation/REMINDER-CONFIG-COMMANDS-v1.md).*
