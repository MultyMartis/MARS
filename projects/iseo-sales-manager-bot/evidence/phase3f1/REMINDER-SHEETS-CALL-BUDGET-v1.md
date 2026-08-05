# REMINDER SHEETS CALL BUDGET v1

The reminder engine lives inside **Admin.dev**, not Operational.dev, so it does not add to the Operational.dev call-budget baseline established in Phase 3E.2.3 (`architecture/SHEETS-CALL-BUDGET-v1.md`). It introduces its own bounded read/write pattern on a 15-minute schedule.

## Per-check budget (schedule tick, not due)

| Step | Sheets call | Notes |
|---|---|---|
| Read CONFIG (reminder keys) | 1 bounded read | Same CONFIG tab already read by other Admin commands; no new tab |
| Gate evaluation | 0 | Pure JS (`isReminderWindowDue`) |

When `due=false` (the overwhelming majority of the 96 checks/day at 15-minute intervals), the tick performs **one** CONFIG read and no further Sheets calls — no ACCESS_CONTROL read, no CLEAN read, no ledger read, no writes.

## Per-check budget (due window)

| Step | Sheets call | Notes |
|---|---|---|
| Read CONFIG | 1 (already counted above) | |
| Read ACCESS_CONTROL | 1 bounded snapshot | Same bounded/fail-closed pattern as lead delivery |
| Read `lead_clean_v2` for pending view | 1 bounded read | Reused for both `/pending_leads` and the reminder message |
| Read `REMINDER_DELIVERIES` (window, recipients) | 1 bounded read | Idempotency check |
| Claim writes | up to N (N = eligible recipients) | Claim-before-send, one write per recipient |
| Sent-stamp writes | up to N | One per successful Telegram send |
| CONFIG update (`pending_reminder_last_window`, `*_last_success_at`, …) | 1 | Only after all recipients processed |

With **2** eligible recipients (Phase 3F.1 access snapshot), a fully successful due-window run is bounded at roughly 4 reads + 4 writes + 1 CONFIG update — a small, fixed-size operation once per day, not a per-poll amplifier.

## Controlled live window observation

During the controlled reminder live acceptance (see [CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md](CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md)) the ACCESS_CONTROL read hit the same Sheets quota condition already documented in Phase 3E.2.2/3E.2.3, and the engine correctly failed closed rather than attempting a fallback broad read.

*Related: [../../architecture/SHEETS-CALL-BUDGET-v1.md](../../architecture/SHEETS-CALL-BUDGET-v1.md), [REMINDER-SCHEDULE-GATE-v1.md](REMINDER-SCHEDULE-GATE-v1.md).*
