# FAILED REMINDER WINDOW TIMELINE — Phase 3H.8

## Alias
- `REMINDER_PROD_LEAD_A` — genuine lead that remained pending overnight and was marked Spam after the window
- `REMINDER_PROD_LEAD_B` — second genuine spam lead (not reopened)

## Business date
**2026-08-13** Europe/Moscow (expected window 10:00–10:20)

## Timeline (factual)
| # | Event | Evidence |
|---|---|---|
| 1 | Lead received (CONFIG last_processed) | `2026-08-12T19:30:15.461Z` → evening prior to window |
| 2 | Status pending overnight | Operator evidence + later spam callback at 10:40 MSK |
| 3 | Reminder Schedule Trigger @ 10:00:21 MSK | exec `29969` mode=trigger success |
| 4 | Gate: proceed=true window `pending-reminder:2026-08-13:10:00:Europe/Moscow` | exec nodeOut |
| 5 | Read CLEAN for Reminder | **1 row only**, `lifecycle_status=processed` (obsolete `LEADS` tab) |
| 6 | Reminder Build Claims | `reminder_send=false`, `reminder_skip_reason=zero_pending`, `pending_count_snapshot=0` |
| 7 | IF Reminder Send → false | no Telegram path |
| 8 | Mark Window Complete | `config_write=null` (zero-pending did **not** stamp last_window) |
| 9 | Operator marked Spam @ 10:40:34 / 10:40:47 MSK | execs `29992`, `29993` ack «Лид отмечен как спам.» |

No inference from current status alone: window reconstruction uses execution payloads.
