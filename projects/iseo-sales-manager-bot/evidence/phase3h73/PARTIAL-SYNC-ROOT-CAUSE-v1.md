# PARTIAL SYNC ROOT CAUSE

## Chain
1. Resurface writes LEAD_DELIVERIES with **empty** `telegram_delivery_chat_id` (privacy shortcut).
2. `Expand Card Sync Copies` requires `telegram_message_ref && (telegram_delivery_chat_id || telegram_chat_id)`.
3. New resurface cards are **excluded** from sync set.
4. Historical initial deliveries (with chat ids) are edited instead — some stale/deleted → edit failures.
5. `Aggregate Card Sync Result` (3H.7.2) replaced semantic spam ack with:
   «Статус сохранён. Не все копии карточки удалось обновить.»

## Repair
- Authoritative instance registry: one current card per recipient
- Prefer latest `operator_resurface` when present
- Ignore superseded historical for current sync failure accounting
- Keep semantic ack independent of sync result
- Store chat_id on resurface deliveries (required for sync)
