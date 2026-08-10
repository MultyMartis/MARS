# CARD SYNC MESSAGE REFERENCE REPAIR — Phase 3H.7.3.2

## Proven defect
Live Spam/Reopen mutated LEADS and returned correct semantic acks, but the operator-visible Telegram card did not change.

Execution `27669` (Spam):
- OPERATOR_VISIBLE message_id alias `MSG_898`
- WORKFLOW_EDIT_TARGET message_id alias `MSG_883` (operator_resurface_parity)
- Telegram API for initiator: `message to edit not found`
- Aggregate: 3/4 ok on stale cards + 1 fail; semantic ack still `Лид отмечен как спам.`

## Root cause
`preferAuthoritative` / Expand scoring used:

```
if (key.includes('operator_resurface_parity')) s += 120;
if (key.includes('operator_resurface')) s += 100;
```

`operator_resurface_parity` matched **both** → score 240.
`acceptance_canonical` scored 160 only.
Therefore newer acceptance cards (operator-visible) lost to older parity rows.

## Repair (minimal)
1. Exclusive delivery-class scoring (`iseo-authoritative-card-instance-v1.2`).
2. Callback initiator chat prefers clicked `callback_message_id`.
3. Archive / pending-view deliveries excluded from current sync.
4. Aggregate records per-card results + Telegram failure class (no false global PASS from status alone).

## Scope
Admin.dev `wLrLp4WQHm1VJmxz` only — Expand Card Sync Copies + Aggregate Card Sync Result.
Operational.dev unchanged.
