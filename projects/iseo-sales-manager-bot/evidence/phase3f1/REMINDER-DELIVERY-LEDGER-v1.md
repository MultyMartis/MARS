# REMINDER DELIVERY LEDGER v1

**Tab:** `REMINDER_DELIVERIES` (additive; CLEAN workbook). **Status:** created, empty in production (reminders not yet activated).

## Headers (`REMINDER_DELIVERY_HEADERS`)

`reminder_key`, `reminder_window`, `recipient_ref`, `role_snapshot`, `pending_count_snapshot`, `oldest_age_minutes_snapshot`, `claimed_at`, `sent_at`, `status`, `telegram_message_ref_safe`, `error_code_safe`, `reminder_version`, `reconciled_at`.

No PII column: `recipient_ref` is the same opaque reference used by `selectActiveStaffRecipients` (see [REMINDER-RECIPIENT-SNAPSHOT-v1.md](REMINDER-RECIPIENT-SNAPSHOT-v1.md)); no raw Telegram user id, chat id, phone, or lead content is stored on this tab.

## Key shape

`reminderDeliveryKey(windowKey, recipientRef)` → `<windowKey>|<recipientRef>`, e.g. `pending-reminder:2026-08-05:10:00:Europe/Moscow|<recipient_ref>`. One row per (window, recipient) pair — the natural per-recipient idempotency unit for a scheduled batch send.

## Row lifecycle

1. **Claim** — row created/updated with `claimed_at` set, `status=claimed`, before any Telegram send is attempted (claim-before-send, same discipline as `DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md` for lead cards).
2. **Sent** — on Telegram success, `sent_at` + `status=delivered` + safe message ref are written.
3. **Reconciled** — if a later check finds a `claimed` row whose Telegram outcome is uncertain, `reconciled_at` is stamped and the row is not blindly resent (see [REMINDER-IDEMPOTENCY-v1.md](REMINDER-IDEMPOTENCY-v1.md)).

## Additive-only migration

`REMINDER_DELIVERIES` is a **new** tab; no existing tab (`LEAD_DELIVERIES`, `CONFIG`, `lead_clean_v2`) was altered to create it. No historical row migration was required or performed.

*Related: [REMINDER-IDEMPOTENCY-v1.md](REMINDER-IDEMPOTENCY-v1.md), [../../architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md](../../architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md).*
