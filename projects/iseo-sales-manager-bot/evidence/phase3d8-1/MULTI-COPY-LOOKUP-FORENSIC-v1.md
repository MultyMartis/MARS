# MULTI-COPY LOOKUP FORENSIC v1

## Root cause

`Read LEAD_DELIVERIES for Sync` returned a single error item:

`Sheet with name LEAD_DELIVERIES not found`

Same failure on Operational `Read` / `Upsert` / `Append LEAD_DELIVERIES` (continueOnFail). Delivery still reached Telegram because fan-out is in-memory; ledger persistence was silently skipped.

## Expand behavior under error

Expand filtered error items poorly (pre-repair) and fell back to **initiator-only** edit → Admin card could update while moderator copy kept buttons.

## Repair

1. Created missing `LEAD_DELIVERIES` tab in CLEAN workbook
2. Wrote header row via Sheets Values API
3. Expand now ignores Sheets `error` items
4. Synthetic Phase 3D.8.1 deliveries: Append LEAD_DELIVERIES **error=null**, two roles recorded

## Matching fields

`stable_lead_ref` + `delivery_status=delivered` + `telegram_message_ref` + chat id column
