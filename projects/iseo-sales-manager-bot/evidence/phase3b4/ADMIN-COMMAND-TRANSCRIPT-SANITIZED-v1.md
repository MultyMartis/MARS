# ADMIN COMMAND TRANSCRIPT SANITIZED v1

## Source

Harness-injected authorized commands after Phase 3B.4 patches. **Not** real Telegram Trigger transcript.

## Transcript

### /help
```
Команды Sales Manager Admin

Чтение:
/help — список команд
/status — состояние контура
/ai_status — режим ИИ
/health — проверка доступности
/stats — сводка за период
/last_error — последняя ошибка
/config — безопасная сводка CONFIG

Только для оператора (allowlist):
/ai_on — включить ИИ в CONFIG
/ai_off — выключить ИИ в CONFIG
/test_lead — синтетическая тестовая заявка
```

### /status
```
Статус Sales Manager
Контур: разработка
Режим ИИ: выключен
Последний успех: 2026-07-30 19:49:48 UTC (синтетический прогон)
Последняя ошибка: 2026-07-30 19:49:59 UTC
Код ошибки: telegram_delivery_failed
```

### /ai_status
```
Режим ИИ
Режим ИИ: выключен
Модель: —
Проверка AI: запрещена
```

### /health
```
Проверка Sales Manager

CONFIG: доступна
RAW v2: доступна
CLEAN v2: доступна
LEAD_EVENTS: доступна
ERRORS: доступна
DEDUP_INDEX: доступна
Gmail: привязка найдена, письма не читались
Telegram sandbox: доступен
Operational.dev: выключен, как и требуется
Admin.dev: тестовый режим
ИИ: выключен
Проверка AI: не запускалась
```

### /stats
```
Статистика за 7 дней

Всего заявок: 4
Новых: 2
Повторных: 0
Возможных повторов: 0
Повторных обработок: 0

Без ИИ: 4
С ИИ: 0
Fallback на шаблон: 0

Данных достаточно: 1
Нужно уточнение: 3
Недостаточно для связи: 0

Ошибок обработки: 0

Контур: разработка
В статистике учитываются только SYNTHETIC_TEST.
```

### /last_error
```
Последняя ошибка
Этап: отправка карточки в Telegram
Код: telegram_delivery_failed
Сообщение: Не удалось доставить карточку в Telegram.
```

### /config
```
Сводка CONFIG
Контур: разработка
Режим ИИ: выключен
Версия парсера: sm-parser-v3
Версия сообщений: sm-msg-v1
Администраторов в allowlist: 1
(секреты и идентификаторы скрыты)
```

### unknown
```
Неизвестная команда. Используйте /help.
```

### /ai_on
```
AI включён в CONFIG (dev). Workflow не активированы. Провайдер не вызывался.
```

### /ai_off
```
AI выключен в CONFIG. Режим AI OFF.
```
