# TELEGRAM-SUCCESS-AUTHORITY

**Token:** `D6A_TELEGRAM_SUCCESS_AUTHORITY_DEFINED`

## Success signal (authoritative)

All of:

1. Telegram node did not surface an error signal (`nodeError` / `ok===false` / error object absent).
2. Sanitized numeric `message_id` present on node output (`result.message_id` or top-level `message_id`).

Proven by D5R2A: node success + `message_id=7`.

## Failure signal (definite)

Node error / continue-on-fail error path / `ok===false` without successful message_id.

## Ambiguous

Node completed without error flag but **no** numeric message_id → do **not** mark SENT or FAILED; leave PENDING.

## message_id persistence

- **Needed for SENT?** No — success proof is required to *decide* SENT; storing message_id in DT is optional observability.
- D6A schema decision: do not add DT column; keep message_id in classify audit / n8n execution history.
