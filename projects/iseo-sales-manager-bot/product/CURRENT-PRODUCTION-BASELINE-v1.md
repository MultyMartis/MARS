# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3H.6 four-recipient baseline · soak T+0 **2026-08-06 20:28 Europe/Moscow**  
**Статус:** AI OFF; reminders ON 10:00 Europe/Moscow; reporting manual; poll heartbeat v1.0; **active recipients=4** (Андрей, Оля, Михаил, Никита). Workflows Ops 45 / Admin 85 / v2 inactive.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | rollback; не активировать |
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Parser 3.3; multi-recipient; AI OFF; sole Gmail fetch |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 | profiles; callbacks; reminders ON; live ACCESS reminder count |

## CONFIG (post-3H.6)

`ai_enabled=false` · `parser_version=sm-parser-v3.3` · `pending_reminders_enabled=true` · `pending_reminder_time=10:00` · `pending_reminder_timezone=Europe/Moscow` · `pending_reminder_min_count=1` · tests/archive excluded · `pending_reminder_active_recipients_count=4` · `reporting_sync_mode=manual` · `/reminder_status` prefers live ACCESS

## Profiles

1. Андрей — admin — active — cards — personalization ON  
2. Оля — moderator — active — cards — personalization ON  
3. Михаил — moderator — active — cards — personalization ON  
4. Никита — moderator — active — cards — personalization ON  

## Prior soak note

Attempt 3 / prior T+0 STOP reclassified via erratum: operator-approved baseline change 3→4 (not a security incident). See Phase 3H.6 report.

## Immutable soak baseline

See `product/PRODUCTION-BASELINE-PRE-AI-SOAK-FOUR-RECIPIENT-v1.md`.
