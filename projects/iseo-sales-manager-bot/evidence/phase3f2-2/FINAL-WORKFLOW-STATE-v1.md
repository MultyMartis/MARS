# FINAL WORKFLOW STATE v1 — Phase 3F.2.2

| Workflow | ID | Active | Nodes | Notes |
|---|---|---|---:|---|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | **Unchanged** this phase |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 82 | Patched Help + Lead History Handler only |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | Inactive |

## Admin triggers

- Telegram Trigger: `message` + `callback_query` — present
- Reminder Schedule Trigger — present (reminders remain OFF via CONFIG)
- Manual Admin Synthetic Trigger — present

## Patch boundary

- Nodes updated: `Help`, `Lead History Handler`
- Workflows created: **0**
- Operational mutations: **0**
- AI / reminders / access / ledger / reporting workbook: **unchanged**
