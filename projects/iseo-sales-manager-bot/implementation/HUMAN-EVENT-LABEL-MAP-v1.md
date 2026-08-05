# HUMAN EVENT LABEL MAP v1

**Status:** live on Admin.dev `/lead_history` (Phase 3F.2.2)  
**Surface:** Telegram timeline bullets (lowercase after em dash)

| Code | Label |
|---|---|
| `lead_received` | заявка получена |
| `lead_parsed` | заявка разобрана |
| `lead_stored` | заявка сохранена |
| `telegram_sent` | заявка передана сотрудникам |
| `delivered_to_employee` | заявка передана сотрудникам |
| `lead_card_delivered` | заявка передана сотрудникам |
| `delivery_failed` | не удалось передать заявку сотруднику |
| `reply_generated` | подготовлен черновик ответа |
| `lifecycle_changed` + `processed` | статус изменён: обработан |
| `lifecycle_changed` + `spam` | статус изменён: спам |
| `lifecycle_reconciled` | статус восстановлен после технической ошибки |
| `external_workbook_synced` | данные синхронизированы с таблицей учёта |
| `sync_failed` | не удалось синхронизировать данные |
| `archive_migrated` | заявка перенесена в рабочий реестр |
| `manual_correction` | данные исправлены администратором |
| unknown | техническое событие |

Raw codes may appear in backend logs only — never in employee Telegram text.
