# REMINDER IDEMPOTENCY v1

Same fail-closed / no-blind-resend discipline as lead-card delivery (`architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md`), applied to the reminder engine.

## Contracts

| Contract | Behavior | Harness |
|---|---|---|
| Window-level idempotency | `pending_reminder_last_window` equal to the computed window key → zero sends | #31, #36 |
| Recipient-level idempotency | A `delivered` row in `REMINDER_DELIVERIES` for `(window, recipient)` is never resent | #32 |
| Ledger read error | Read failure on `REMINDER_DELIVERIES` → zero sends (fail closed, contract) | #33 |
| Claim failure | Failed claim write for a recipient → zero sends for that recipient (contract) | #34 |
| Send-success + stamp uncertainty | Telegram succeeds but the post-send stamp write is uncertain → row marked for reconciliation, **not** blindly resent (contract) | #35 |
| Partial recipient success | One recipient already `delivered`; a second recipient not yet attempted → only the second is sent, first is not resent | #32 |

## Contract vs. proven-live distinction

Checks #33, #34, #35 are marked **(contract)** in the offline harness — they assert the documented policy rather than exercising a live Sheets failure inside the harness process. The controlled live acceptance window (see [CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md](CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md)) exercised the real fail-closed path against a live Sheets quota condition and observed the same zero-send outcome, which corroborates the contract without claiming a second independent proof of every branch.

## Why "no blind resend" matters here

A reminder is a **batch** notification, not a single lead card — a resend bug would multiply, not just duplicate, one message per active staff member per erroneous re-check. The 15-minute schedule interval combined with a 20-minute due window means a naive "if pending > 0, send" implementation could fire 1–2 extra times per day without the window-key and ledger guards above.

*Related: [REMINDER-SCHEDULE-GATE-v1.md](REMINDER-SCHEDULE-GATE-v1.md), [REMINDER-DELIVERY-LEDGER-v1.md](REMINDER-DELIVERY-LEDGER-v1.md), [../../architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md](../../architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md).*
