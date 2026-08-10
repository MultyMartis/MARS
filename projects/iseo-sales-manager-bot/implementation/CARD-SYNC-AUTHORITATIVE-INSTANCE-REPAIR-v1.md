# CARD SYNC AUTHORITATIVE INSTANCE REPAIR — Phase 3H.7.3

## Root cause

`Expand Card Sync Copies` synced **all** delivered rows with chat+message refs.
Resurface deliveries had empty chat ids → excluded.
Historical cards were edited; failures caused Aggregate to replace semantic ack with:

«Статус сохранён. Не все копии карточки удалось обновить.»

## Repair

1. Select one authoritative current instance per recipient.
2. Prefer `operator_resurface` over older initial.
3. Ignore superseded historical for current sync failure accounting.
4. Aggregate returns semantic ack (`Лид отмечен как спам.` / reopen / processed) even if sync is partial; sync warning is separate metadata.
5. Resurface/repair deliveries must store `telegram_delivery_chat_id`.

## Nodes patched

- Admin `Expand Card Sync Copies`
- Admin `Aggregate Card Sync Result`

Workflow ids unchanged: Admin `wLrLp4WQHm1VJmxz`, Operational `xSnXPy8cEHoZw6xG`.
