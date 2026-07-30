# RUNTIME SUCCESS STATE ACCEPTANCE v1

## Verdict

**PASS** (CONFIG ops keys via Operational.dev runtime writer)

## Writes after success gate

| Key | Observed |
|-----|----------|
| last_success_at | set (ISO timestamp) |
| last_processed_at | set |
| last_processed_lead_id | safe SYNTHETIC reference |
| last_processing_mode | ai_off |
| last_delivery_status | delivered |
| workflow_version | Operational.dev |

## Failure isolation

Controlled Telegram failure does **not** clear `last_success_at`; sets `last_delivery_status=failed` and error keys only.

## /status harness shape

```
Статус Sales Manager
Контур: разработка
Режим ИИ: выключен
Последний успех: 2026-07-30 19:49:48 UTC (синтетический прогон)
Последняя ошибка: 2026-07-30 19:49:59 UTC
Код ошибки: telegram_delivery_failed
```

Internal lead identifiers are not shown in Telegram status text.
