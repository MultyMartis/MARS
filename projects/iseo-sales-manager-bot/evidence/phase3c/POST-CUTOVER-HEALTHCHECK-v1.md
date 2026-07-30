# POST-CUTOVER HEALTHCHECK v1

## Method

Temporary Admin webhook entry per command; baseline restored; Telegram Trigger re-enabled.

## Results (sanitized previews)

### /status
```
Статус Sales Manager

Контур: рабочий контур
Рабочий процесс: включён
Админ-процесс: включён
Режим ИИ: выключен

Последний успех: 30.07.2026 22:49 МСК
Последняя ошибка: 30.07.2026 22:49 МСК
```
Validation: {"contourWorking":true,"opsOn":true,"adminOn":true,"aiOff":true}

### /ai_status
```
Режим ИИ
Состояние: выключен
Модель: не задана
Проверка провайдера ИИ: отключена
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
Telegram: доступен
Рабочий процесс: по CONFIG (см. /status)
Админ-процесс: включён
ИИ: выключен
Проверка провайдера ИИ: не запускалась
```
Validation: {"configOk":true,"gmailBound":true,"telegramOk":true,"aiProbeSkipped":true,"aiOff":true,"opsOnHint":true}

### /config
```
Сводка CONFIG

Контур: рабочий контур
Режим ИИ: выключен
Версия парсера: sm-parser-v3
Версия сообщений: sm-msg-v1
Администраторов: 1

Секреты и идентификаторы скрыты.
```

### /stats
```
Статистика за 7 дней

Всего заявок: 2
Новых: 0
Повторных: 0
Возможных повторов: 0
Повторных обработок: 2

Без ИИ: 2
С ИИ: 0
Использован шаблон: 0

Данных достаточно: 0
Нужно уточнение: 0
Недостаточно для связи: 0

Ошибок обработки: 0

Контур: рабочий контур
Тестовые заявки исключены.
```

### /last_error
```
Последняя рабочая ошибка

Время: 30.07.2026 22:49 МСК
Этап: отправка карточки в Telegram
Код: telegram_delivery_failed
Сообщение: Не удалось доставить карточку в Telegram.
```

## Notes

- AI probe not started
- No secret identifiers shown in replies
- `/last_error` uses production wording; residual historical error row may still be visible until a newer production error supersedes it (**SAFE UNKNOWN** whether prior synthetic failure row lacks SYNTHETIC marker)
