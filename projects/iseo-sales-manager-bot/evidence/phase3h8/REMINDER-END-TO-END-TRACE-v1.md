# REMINDER END-TO-END TRACE — failed window 2026-08-13

| Step | Node | Result |
|---|---|---|
| 1 Schedule Trigger | Reminder Schedule Trigger | ran |
| 2 Read CONFIG | Read Reminder CONFIG | enabled=true, time=10:00, tz=Europe/Moscow |
| 3 Gate | Reminder Schedule Gate | proceed=true |
| 4 Read leads | Read CLEAN for Reminder → **LEADS** | 1 processed row |
| 5 Normalize / exclude tests/archive | Reminder Build Claims | pending=0 |
| 6 Min threshold | min=1 | fail → zero_pending |
| 7 Business date | windowKey set | yes |
| 8 Once-per-date | last_window not equal | not suppressing |
| 9 Recipients | ACCESS read (4 active) | reached but unused due to zero pending |
| 10 Claims | none | |
| 11 Telegram | none | |
| 12 Delivery ledger | none | |
| 13 Mark sent | config_write null | correct for zero pending |
| 14 Observability | decision not exposed pre-repair | repaired in 3H.8 |
