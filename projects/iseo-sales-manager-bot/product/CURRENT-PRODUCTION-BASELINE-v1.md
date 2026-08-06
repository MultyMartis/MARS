# CURRENT PRODUCTION BASELINE v1

**Срез:** Final pre-AI soak **T+0 observation** 2026-08-06 19:52 Europe/Moscow — verdict `SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION` (MOD_C identity reactivated + card delivery). Final soak T+0 charter remains 2026-08-06 16:20 Europe/Moscow.  
**Статус:** AI OFF; reminders ON 10:00 Europe/Moscow; reporting manual; poll heartbeat v1.0 healthy; **access/delivery invariant broken for MOD_C** (requires operator remediation). Workflows Ops 45 / Admin 85 / v2 inactive unchanged.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | rollback; не активировать |
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Parser 3.3; multi-recipient; AI OFF; sole Gmail fetch |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 | profiles; callbacks; reminders ON; `/status` production processed cache |

## CONFIG (post-3H.4.1)

`ai_enabled=false` · `parser_version=sm-parser-v3.3` · `pending_reminders_enabled=true` · `pending_reminder_time=10:00` · `pending_reminder_timezone=Europe/Moscow` · `pending_reminder_min_count=1` · tests/archive excluded · `reporting_sync_mode=manual` · `reporting_sync_state=только вручную` · `last_production_processed_at` cache = production LEADS lifecycle_changed_at

## Profiles

**Desired soak baseline (charter):**  
1. Андрей — admin — active — cards — personalization ON  
2. Оля — moderator — active — cards — personalization ON  
3. Михаил — moderator — active — cards — personalization ON  
4. Никита — moderator — revoked — no cards  

**Live at T+0 observation:** MOD_C identity observed **active** with blank profile number after post-T+0 access upsert; received card on PROD_LEAD_3 — **STOP**.

## Statistics epoch

05.08.2026 16:02 МСК epoch remains. Post-T+0 genuine leads observed (aliases PROD_LEAD_2 / PROD_LEAD_3); exact `/stats` packet after T+0 not captured in-agent.

## Immutable soak baseline

See `product/PRODUCTION-BASELINE-PRE-AI-SOAK-v1.md`. Attempts 1–2 interrupted. T+0 observation **STOP**. Earliest soak PASS clock **08.08.2026 16:20 МСК** is not claimable under current STOP without remediation + explicit re-charter.
