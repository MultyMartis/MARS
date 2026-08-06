# CURRENT PRODUCTION BASELINE v1

**Срез:** Phase 3H.4.1 `/status` last-processed readback repaired — final 48-hour pre-AI soak **restarted** 2026-08-06 16:20 Europe/Moscow.  
**Статус:** AI OFF; reminders ON 10:00 Europe/Moscow; reporting manual; active recipients=3 (Андрей, Оля, Михаил); Никита revoked; poll heartbeat v1.0; `/status` production line = `iseo-last-production-processed-v1.0` / CONFIG cache aligned to LEADS 17:22 МСК.

| Контур | Workflow ID | Active | Nodes | Роль |
|---|---|---:|---:|---|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | rollback; не активировать |
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Parser 3.3; multi-recipient; AI OFF; sole Gmail fetch |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 | profiles; callbacks; reminders ON; `/status` production processed cache |

## CONFIG (post-3H.4.1)

`ai_enabled=false` · `parser_version=sm-parser-v3.3` · `pending_reminders_enabled=true` · `pending_reminder_time=10:00` · `pending_reminder_timezone=Europe/Moscow` · `pending_reminder_min_count=1` · tests/archive excluded · `reporting_sync_mode=manual` · `reporting_sync_state=только вручную` · `last_production_processed_at` cache = production LEADS lifecycle_changed_at

## Profiles

1. Андрей — admin — active — cards — personalization ON  
2. Оля — moderator — active — cards — personalization ON  
3. Михаил — moderator — active — cards — personalization ON  
4. Никита — moderator — revoked — no cards  

## Statistics epoch

05.08.2026 16:02 МСК · received=1 · pending=0 · processed=1 · spam=0 (unless genuine new lead arrives during soak)

## Immutable soak baseline

See `product/PRODUCTION-BASELINE-PRE-AI-SOAK-v1.md`. Attempts 1–2 interrupted. Earliest soak PASS: **08.08.2026 16:20 МСК** (T+0 06.08.2026 16:20 МСК).
