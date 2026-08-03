# SHEETS ACCESS MAPPING MATRIX v1

| Workflow | Node | Tab | Operation | Header Match | Result |
|----------|------|-----|-----------|--------------|--------|
| Admin.dev | Read ACCESS_CONTROL | ACCESS_CONTROL | read | full header | auth input |
| Admin.dev | Upsert ACCESS_CONTROL | ACCESS_CONTROL | appendOrUpdate | telegram_user_id | RAW |
| Admin.dev | Append ACCESS_EVENTS | ACCESS_EVENTS | append | event schema | RAW |
| Admin.dev | Read Authorization Config | CONFIG | read | key/value | bootstrap |
| Admin.dev | Apply CONFIG Write | CONFIG | appendOrUpdate | key | existing |
| Operational.dev | (unchanged) | lead_clean_v2 / CONFIG / … | existing | existing | no access tabs |

No schema drift on CLEAN lead headers in this phase.
