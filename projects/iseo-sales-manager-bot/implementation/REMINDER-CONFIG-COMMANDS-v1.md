# REMINDER CONFIG COMMANDS v1 — implementation spec

**Target workflow:** `i-SEO Sales Manager - Admin.dev` (`wLrLp4WQHm1VJmxz`)
**Phase:** 3F.1

---

## 1. New commands

| Command | Class | Effect |
|---|---|---|
| `/reminder_status` | staff read | Render current reminder config (short form for moderator, extended form for Admin — see `formatReminderStatusReply`) |
| `/reminder_on` | Admin config | `pending_reminders_enabled=true` |
| `/reminder_off` | Admin config | `pending_reminders_enabled=false` |
| `/reminder_time HH:MM` | Admin config | Validate + set `pending_reminder_time` |
| `/reminder_timezone <IANA>` | Admin config | Validate + set `pending_reminder_timezone` |
| `/reminder_min <n>` | Admin config | Set `pending_reminder_min_count` |

Invalid `/reminder_time` or `/reminder_timezone` input is rejected with a usage message and **no CONFIG write** — the previous valid value remains active.

## 2. Node additions

| # | Stable name | Type | Responsibility |
|---|---|---|---|
| a | Format Reminder Status | `code` | `formatReminderStatusReply()`, role-aware verbosity |
| b | Validate Reminder Time | `code` | `validateHhMm()` |
| c | Validate Reminder Timezone | `code` | `validateIanaTimezone()` |
| d | Apply Reminder CONFIG Write | `googleSheets` (update) | Write validated reminder keys; audit via existing `Audit Config Change` pattern |
| e | Reminder Schedule Trigger | `scheduleTrigger` | Fires every **15 minutes**; internal to Admin.dev |
| f | Read Reminder CONFIG (Gate) | `googleSheets` (read, bounded) | Feeds `isReminderWindowDue()` |
| g | Reminder Window Gate | `code` | `isReminderWindowDue()` — stops pipeline when not due |
| h | Read CLEAN for Reminder | `googleSheets` (read, bounded) | Feeds `buildPendingView()` for the reminder message |
| i | Read ACCESS_CONTROL for Reminder | `googleSheets` (read, bounded, fail-closed) | Feeds `selectActiveStaffRecipients()` |
| j | Read REMINDER_DELIVERIES (window) | `googleSheets` (read, bounded) | Idempotency check for the current window |
| k | Claim Reminder Delivery | `googleSheets` (upsert) | Claim-before-send per recipient |
| l | Format Reminder Message | `code` | `formatReminderMessage()` |
| m | Send Reminder | `telegram` | Per-recipient send |
| n | Stamp Reminder Delivery | `googleSheets` (update) | Mark `delivered` + safe message ref |
| o | Finalize Reminder Window | `googleSheets` (update CONFIG) | `pending_reminder_last_window`, `*_last_success_at`, `*_last_recipient_count`, `*_last_pending_count` |

## 3. Sheets additions

`REMINDER_DELIVERIES` tab created (additive; headers per `REMINDER_DELIVERY_HEADERS` in `implementation/runtime-libs/pending-leads-lib.mjs`) — see `implementation/SHEETS-MIGRATION-SPEC-v1.md` §Phase 3F.1 addendum. No existing tab schema changed.

## 4. Authorization

`/reminder_status` uses the staff-read class; all five mutating commands use the admin-config class of `authorizePendingCommand()` — identical precedence rules (revoked/pending/public denied first) as the rest of the Admin surface.

## 5. Safety defaults

`pending_reminders_enabled` defaults to `false` on first deploy and was **not** flipped to `true` as part of Phase 3F.1 implementation or acceptance — see `evidence/phase3f1/REMINDER-CONFIG-CONTRACT-v1.md`.

## 6. Node count impact

Combined with `implementation/PENDING-COMMANDS-v1.md`, Admin.dev moved **59 → 79 nodes** (+20 total).

---

*Related: [../architecture/PENDING-REMINDER-v1.md](../architecture/PENDING-REMINDER-v1.md), [../architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md](../architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md), `../evidence/phase3f1/REMINDER-CONFIG-CONTRACT-v1.md`, `../evidence/phase3f1/CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md`.*
