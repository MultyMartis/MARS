# TELEGRAM-LIVE-REPORT

Exact production Telegram text delivered for manual import
`mars-20260806-160514-5d2cdb3b` (n8n execution `24268`, delivery SENT):

```
⚠️ Импорт 1С выполнен не полностью

Сайт: bzpm.ru
Время: 06.08.2026, 20:05

Каталог обработан успешно.
Файл с ценами и остатками от 1С не получен.

Цены и остатки товаров могли не обновиться.

Что проверить:
выгрузку предложений из 1С и наличие файла offers0_*.xml.
```

Notes:

- Visible format matches accepted D6F1B ATTENTION (offers missing) UX.
- No internal `run_id` / `event_id` / English enum labels in operator text.
- SITE-002 local time UTC+07 shown as `06.08.2026, 20:05` (observed_at from terminal completion).
