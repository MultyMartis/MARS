# SITE-002 — No-Import Watchdog Contract

## Purpose

Alert when no qualifying 1C import has occurred within the expected window (operator-facing via Client Ops).

## Server-side authority

- Logic: `mars_1c_no_import_watchdog.php`
- HTTP gateway: `mars_1c_watchdog_http_gateway.php` (tokenized; **do not print tokens**)
- Schedule: Beget cron — historically **`0 9 * * *`**, timezone **Europe/Moscow**
- Declared: `SITE002_SERVER_WATCHDOG_CODE_READY=YES`, `SITE002_SERVER_WATCHDOG_CRON_ACTIVE=YES` (reconcile live if conflicted)

## Operator-created cron

Beget API historically returned AUTH_ERROR for programmatic cron create; **operator-created** cron is the accepted path.

## Kill switch

Watchdog outbound respects `CLIENT_OPS_DISPATCH_ENABLED`.

## Dedupe

No-import events must follow Client Ops event identity / Data Table rules (no spam loops).

## Stale `_current` lesson

Do not treat stale `_current` pointers as truth without validation — historically caused false skip. Prefer terminal / validated freshness semantics.
