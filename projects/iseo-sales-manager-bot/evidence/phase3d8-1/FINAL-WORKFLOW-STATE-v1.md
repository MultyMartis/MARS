# FINAL WORKFLOW STATE v1

| Workflow | ID | active | nodes | Notes |
|----------|-----|--------|-------|-------|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 | Sole Gmail intake; claim-before-send; buttons |
| Admin.dev | wLrLp4WQHm1VJmxz | true | **59** | +early ack nodes; callback repair |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | **false** | — | Untouched |

## Admin trigger

Telegram Trigger updates: `message` + `callback_query`

## Config

- environment=production
- ai_enabled=false
- parser_version=sm-parser-v3.2
- message_format_version=sm-msg-v2.2

## Access (intentional)

- Андрей admin/active
- Мопс moderator/active
- Оля revoked (unchanged)
- Никита revoked (unchanged)
