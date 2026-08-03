# FINAL WORKFLOW STATE v1

**As of:** Phase 3D.5.2 closeout (post live acceptance)

| Workflow | ID | active | nodes |
|---|---|---|---:|
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | 19 |
| i-SEO Sales Manager - Operational.dev | xSnXPy8cEHoZw6xG | true | 36 |
| i-SEO Sales Manager - Admin.dev | wLrLp4WQHm1VJmxz | true | 51 |

| Counter | Value |
|---|---|
| Active Gmail intake (`Gmail Fetch Leads`) | 1 |
| Active Telegram Trigger owners (Sales Manager bot) | 1 (Admin.dev) |
| OpenRouter AI on Operational | disabled |
| Workflows created this phase | 0 |
| Rollback | no |

## ACCESS_CONTROL (operator-attested at acceptance close)

| Metric | Value |
|---|---:|
| Administrators (active) | 1 |
| Moderators (active) | 1 (Olya) |
| Action-capable | 2 |
| Effective auth source | ACCESS_CONTROL |

## CONFIG

- environment=production
- ai_enabled=false
- parser_version=sm-parser-v3.2
- message_format_version=sm-msg-v2.2
- admin_user_ids = recovery-only bootstrap
- manager_action_user_ids = legacy/non-authoritative
