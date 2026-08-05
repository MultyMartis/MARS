# LEAD EVENT HISTORY v1

Append-only immutable history for production leads.

## Contract

- Corrections create **new** events; old rows are never updated/deleted.
- Required types include: `lead_received`, `lead_parsed`, `lead_stored`, `delivered_to_employee`, `delivery_failed`, `lifecycle_changed`, `lifecycle_reconciled`, `reply_generated`, `external_workbook_synced`, `sync_failed`, `archive_migrated`, `manual_correction`.
- Store UTC + Europe/Moscow business timestamps + IANA timezone.
- Actor display name + role for lifecycle mutations.
- Reconciliation events use `source=telegram_callback_reconciliation` and `reconciliation_state=reconciled`.

## Surfaces

- `/lead_history <n>` — recent 10 events, no internal IDs/tokens/workbook refs.
- Reporting workbook tab `История изменений` — employee-facing mirror (backend remains SoT).
