# STATUS LIVE ACCEPTANCE v1

## ADMIN_A deliveries (acceptance packet)

| Command | Result |
|---|---|
| `/status` | `Последний обработанный лид: 05.08.2026 17:22 МСК` PASS |
| `/stats` | received=1; pending=0; processed=1; spam=0 PASS |
| `/pending_count` | 0 PASS |
| `/health` | contour OK · AI OFF PASS |
| `/reminder_status` | ON · 10:00 Europe/Moscow · recipients 3 PASS |
| `/last_error` | Активных ошибок нет PASS |

## Negative checks

- no `нет данных` on last processed line
- no `22:23`
- source `last_production_processed_at`
- contract `iseo-last-production-processed-v1.0`
