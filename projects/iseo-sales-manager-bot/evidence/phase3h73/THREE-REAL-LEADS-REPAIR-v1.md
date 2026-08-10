# THREE REAL LEADS REPAIR

Strategy: prefer **in-place edit** of malformed resurface cards using recipient chat ids from ACCESS_CONTROL; on edit failure, send exactly one corrected current card per recipient. Append new authoritative delivery rows **with** `telegram_delivery_chat_id`. No new LEADS rows.

## Results
- **REAL_REOPEN_A** (6e4c68e4): spam→pending cards 4/4 strategies={"send":4}
- **REAL_REOPEN_B** (259d186f): pending→pending cards 4/4 strategies={"send":4}
- **REAL_REOPEN_C** (d0f1e764): pending→pending cards 4/4 strategies={"send":4}

- events_appended: 1
- deliveries_appended: 12
- business_leads_created: 0
