# LEAD_DELIVERIES DATA MODEL v1

Immutable operational tab (same CLEAN workbook).

## Columns

delivery_timestamp, stable_lead_ref, recipient_ref, recipient_role, delivery_channel, delivery_status, attempt_number, telegram_message_ref, telegram_chat_ref_hash, card_version, lifecycle_status_at_send, error_code, last_attempt_at, delivered_at, updated_at, delivery_key, telegram_delivery_chat_id (runtime)

## Rules

- One row per recipient per lead (upsert on `delivery_key`).
- Do not overload CLEAN with unbounded message id lists.
- No raw Telegram IDs in git evidence.
