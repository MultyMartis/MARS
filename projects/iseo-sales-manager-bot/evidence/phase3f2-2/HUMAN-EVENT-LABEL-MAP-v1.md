# HUMAN EVENT LABEL MAP v1 — evidence snapshot

Lowercase labels for timeline bullets after em dash.

| Code | Human label |
|---|---|
| `lead_received` | заявка получена |
| `lead_parsed` | заявка разобрана |
| `lead_stored` | заявка сохранена |
| `telegram_sent` | заявка передана сотрудникам |
| `delivered_to_employee` | заявка передана сотрудникам |
| `lead_card_delivered` | заявка передана сотрудникам |
| `delivery_failed` | не удалось передать заявку сотруднику |
| `reply_generated` | подготовлен черновик ответа |
| `lifecycle_changed` + processed | статус изменён: обработан |
| `lifecycle_changed` + spam | статус изменён: спам |
| `lifecycle_reconciled` | статус восстановлен после технической ошибки |
| `external_workbook_synced` | данные синхронизированы с таблицей учёта |
| `sync_failed` | не удалось синхронизировать данные |
| `archive_migrated` | заявка перенесена в рабочий реестр |
| `manual_correction` | данные исправлены администратором |
| *(unknown)* | техническое событие |

Authoritative copy also: `implementation/HUMAN-EVENT-LABEL-MAP-v1.md`.
