# Factual Acceptance — Manual Import

## Run

- `run_id`: `mars-20260807-114238-7cb452ec`
- `trigger_source`: `ADMIN_MANUAL`
- Poller disabled before launch: **YES** (`MARS_SITE_002_Import_Completion_Poller` Enabled=False)

## Classification

`OFFERS_INPUT_MISSING` / `ATTENTION_OFFERS_INPUT_MISSING` / `CATALOG_SUCCESS_OFFERS_INPUT_MISSING`

Matches live terminal + absent `offers0_*.xml`.

## Telegram (n8n execution 24972)

```
⚠️ Импорт 1С выполнен не полностью

Сайт: bzpm.ru
Время: 07.08.2026, 15:42

Каталог обработан успешно.
Файл с ценами и остатками от 1С не получен.

Цены и остатки товаров могли не обновиться.

Что проверить:
выгрузку предложений из 1С и наличие файла offers0_*.xml.
```

## Latency

- Terminal completed: `2026-08-07T11:42:42+03:00`
- Dispatch attempted: `2026-08-07T11:42:42+03:00` (SENT, HTTP 202)
- n8n started: `2026-08-07T08:42:42.639Z` (= same second)
- Terminal→n8n: ~seconds (not minutes)

## Gates

- `D6G1_MANUAL_IMPORT_COMPLETED_WITH_POLLER_DISABLED`
- `D6G1_SERVER_SIDE_REPORT_DELIVERED_WITH_POLLER_DISABLED`
- `D6G1_REAL_TELEGRAM_REPORT_FACTUALLY_ACCEPTED`
