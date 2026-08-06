# FINAL SOAK REMINDER STATE T0 v1

Observed via Admin **Reminder Schedule Trigger** CONFIG reads after final T+0 (no reminder simulation).

| Key | Value |
|---|---|
| pending_reminders_enabled | true |
| pending_reminder_time | 10:00 |
| pending_reminder_timezone | Europe/Moscow |
| pending_reminder_min_count | 1 |
| pending_reminder_include_tests | false |
| pending_reminder_include_archive | false |
| pending_reminder_active_recipients_only | true |
| pending_reminder_once_per_business_date | true |
| pending_reminder_active_recipients_count | 3 (CONFIG; **stale vs live access after MOD_C reactivation**) |
| pending_reminder_last_window | empty |
| pending_reminder_last_success_at | empty |

## Since T+0

| Metric | Value |
|---|---:|
| Reminder schedule ticks observed | multiple (15-minute cadence) |
| Reminder proceed-true / sends | **0** |
| Reminder claims | **0** |
| Duplicate reminder sends | **0** |
| Reminder tick errors sampled | **0** |

## Windowing

- Final T+0 (16:20 МСК) is **after** 06.08.2026 10:00 reminder window — no production reminder required for that earlier window.
- First meaningful live reminder window inside final soak: **07.08.2026 10:00 Europe/Moscow** — not yet elapsed; not simulated.
- Next window remains **armed** by configuration; soak STOP does not disable reminders in this read-only checkpoint.
