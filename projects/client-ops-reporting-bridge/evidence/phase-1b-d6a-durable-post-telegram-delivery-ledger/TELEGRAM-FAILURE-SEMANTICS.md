# TELEGRAM-FAILURE-SEMANTICS

**Token:** `D6A_FAILURE_SEMANTICS_DEFINED`
Also: `D6A_TELEGRAM_FAILURE_PERSISTENCE_DEFINED`

## Model

| Case | delivery_state | Notes |
|------|----------------|-------|
| 1. Telegram node definite failure | FAILED | Written in same execution after classify |
| 2. Telegram outcome ambiguous | PENDING | No FAILED; no resend |
| 3. Execution interrupted before Telegram | PENDING | Claim exists; reconcile via execution |
| 4. DT finalize fails after Telegram success | PENDING | Critical; see POST-TELEGRAM-LEDGER-WRITE-FAILURE |
| 5. Crash after PENDING before Telegram attempt | PENDING | No automatic resend |

## Error metadata

Persist only sanitized class in classify output / evidence:

- `TELEGRAM_NODE_ERROR`
- `TELEGRAM_API_ERROR`

Do **not** store raw stack traces, tokens, URLs, or full Telegram API bodies in Data Table.

## FAILED ≠ event_status

`delivery_state=FAILED` does not rewrite `event_status` (e.g. ATTENTION stays ATTENTION).
