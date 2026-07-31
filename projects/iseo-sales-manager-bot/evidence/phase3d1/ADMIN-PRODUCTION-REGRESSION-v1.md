# ADMIN-PRODUCTION-REGRESSION-v1

**Phase:** 3D.1  
**Method:** temporary Admin webhook sidecar → Normalize Command (removed after)  
**Auth:** operator allowlisted user (hash-only in logs)

## Commands

| Command | Authorized | Key checks |
|---------|------------|------------|
| `/status` | yes | production contour; AI off; error line non-active wording |
| `/health` | yes | sheets/gmail/telegram; AI off; probe skipped |
| `/stats` | yes | Уникальных заявок; Технических повторных попыток |
| `/last_error` | yes | Активных рабочих ошибок нет + последняя устранённая |
| `/config` | yes | production; AI off |
| `/ai_status` | yes | выключен; probe disabled |

## Gates

- Sales-Manager-v2 inactive
- Operational.dev active
- Admin.dev active after restore (sidecar removed)
- AI OFF

**PASS**
