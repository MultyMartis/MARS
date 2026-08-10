# MISSED LEAD ROOT CAUSE — Phase 3H.7

## Primary root cause
`GMAIL_OAUTH_INVALID_GRANT`

Operational node **Gmail Fetch Leads** returns:

> The provided authorization grant ... refresh token is invalid, expired, revoked...

Every ~2 minutes since at least 2026-08-09 (oldest retained execution in sample) and consistent with heartbeat freeze after 2026-08-07T09:04Z.

## Secondary defect (repaired)
Error Handler treated `telegram_ok === false` as Telegram delivery failure. Intake Gate sets `telegram_ok=false` on Gmail read failures, so ERRORS were poisoned with `telegram_delivery_failed` / `SYNTHETIC_TEST`.

## Repair applied
Operational **Error Handler** Phase 3H.7 patch: Telegram failure only when stage/code indicates `telegram_send`.

## Proof
`error-handler-post-patch-proof.json` → pass=true (`gmail_read_failed` preserved end-to-end).
