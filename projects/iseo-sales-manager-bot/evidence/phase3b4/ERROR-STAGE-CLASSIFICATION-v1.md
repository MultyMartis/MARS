# ERROR STAGE CLASSIFICATION v1

## Stable stages

parse_lead, raw_write, config_read, deterministic_processing, ai_request, ai_validation, dedupe_lookup, clean_write, telegram_send, gmail_labels, runtime_state

## Controlled Telegram failure

| Field | Value |
|-------|-------|
| code | telegram_delivery_failed |
| stage | telegram_send |
| message | Не удалось доставить карточку в Telegram. |

## /last_error harness shape

```
Последняя ошибка
Этап: отправка карточки в Telegram
Код: telegram_delivery_failed
Сообщение: Не удалось доставить карточку в Telegram.
```

No stack traces, raw HTTP bodies, chat IDs, or credentials in operator-facing text.
