# REGRESSION RESULTS v1 — Phase 3F.2.2

| # | Check | Result | Notes |
|---|---|---|---|
| 28 | `/leads` lifecycle processed | PASS | Live pre-patch exec; formatter untouched |
| 29 | `/leads` service present | PASS | «Требует уточнения» |
| 30 | `/leads` comment present | PASS | |
| 31 | `/leads` source correct | PASS | Сайт i-seo.su |
| 32 | `/lead_history 1` recognized | PASS | Route + handler present |
| 33 | `/pending_count` zero | PASS | Live reply: нет |
| 34 | `/pending_leads` zero | PASS | Live reply: нет |
| 35 | `/reminder_status` OFF | PASS | выключены / 10:00 / Europe/Moscow |
| 36 | backend leads=1 | PASS | Contour unchanged; polish did not mutate LEADS |
| 37 | reporting leads=1 | PASS | Workbook not modified this phase |
| 38 | reporting stats 1/1/0/0 | PASS | Unchanged |
| 39 | reminders OFF | PASS | |
| 40 | AI OFF | PASS | Help lists AI commands; CONFIG not flipped |
| 41 | Operational unchanged | PASS | Same `updatedAt` before/after Admin patches |
| 42 | workflows created=0 | PASS | |
| 43 | access changes=0 | PASS | |
| 44 | real leads lost=0 | PASS | |
| 45 | real leads duplicated=0 | PASS | |

Admin nodes remain **82**. Operational nodes remain **45**.
