# REMINDER WINDOW KEY v1

**Function:** `buildReminderWindowKey(localDate, hhmm, timezone)`.

## Format

```
pending-reminder:<YYYY-MM-DD>:<HH:MM>:<IANA timezone>
```

Example (sanitized, no PII): `pending-reminder:2026-08-05:10:00:Europe/Moscow`.

## Properties

- **Deterministic** — same local calendar date + configured time + configured timezone always produce the same key (harness #30).
- **No PII** — contains only date, time, and timezone; no lead ids, user ids, or chat ids.
- **One key per calendar day** at the configured time, per timezone — reconfiguring the timezone or time changes the key namespace, which is intentional (a time/timezone change should not silently suppress or duplicate the next run).
- Stored in `pending_reminder_last_window` (CONFIG) after a successful window completes, and used as the per-window namespace inside every `reminder_key` in `REMINDER_DELIVERIES` (`reminderDeliveryKey(windowKey, recipientRef)` — see [REMINDER-DELIVERY-LEDGER-v1.md](REMINDER-DELIVERY-LEDGER-v1.md)).

## Why this shape

A pure date+time+timezone key (rather than an execution id or timestamp) means:

1. Any of the 15-minute schedule checks that land inside the due window compute the **same** key — necessary for idempotency when the checker itself is not exactly-once.
2. Historical windows are never accidentally replayed after downtime, because the key is anchored to calendar date, not to "N runs since start".

*Related: [REMINDER-SCHEDULE-GATE-v1.md](REMINDER-SCHEDULE-GATE-v1.md), [REMINDER-DELIVERY-LEDGER-v1.md](REMINDER-DELIVERY-LEDGER-v1.md).*
