# SECURITY-REVIEW

**Token:** `D6A_LEDGER_SECURITY_MODEL_PASS`

## Data minimization

| Forbidden in DT / evidence | Status |
|----------------------------|--------|
| Telegram bot token | Not persisted |
| Webhook secret | Not persisted |
| Raw auth headers | Not persisted |
| Full Telegram API response | Not persisted |
| Raw stack traces | Not persisted |
| Customer payload beyond approved event fields | Not expanded |
| Filesystem paths / raw logs | Not persisted |

## Allowed

- Sanitized numeric `message_id` in classify audit (not a new DT column in D6A)
- Sanitized error class codes only

## Scan

Validator secret regex scan over pack + new libs + fixtures: PASS (allowlisted credential ids only, already public in Client Ops allowlists).
