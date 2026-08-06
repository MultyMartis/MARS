# FINAL WORKFLOW STATE v1 — Phase 3H.4

## Workflows

| Name | ID | Active | Nodes | Notes |
|---|---|---:|---:|---|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Gmail poll heartbeat v1.0 |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 | Reminder/Status/Health repaired |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | Rollback only |

## Patch summary

- workflows_created = **0**
- Temporary webhook nodes: introduced briefly, **removed** — final Admin count **85**
- Same workflow IDs throughout

## CONFIG highlights

- AI OFF
- Reminders ON · 10:00 Europe/Moscow
- `pending_reminder_active_recipients_count=3`
- `last_production_processed_at=2026-08-05T14:22:55.186Z`
- `last_production_processed_lead_id=lead_19fd2052066e18b7`
- `gmail_poll_heartbeat` contract `iseo-gmail-poll-heartbeat-v1.0`

## Branch / base

- Branch: `agent/iseo-sm-phase3h4-soak-observability-repair`
- Base: `origin/mars/canonical-post-recovery` @ `380cebd7`
