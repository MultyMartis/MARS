# Watchdog Regression

## Live NO_SEND (production)

- Invoked: HTTP gateway `mars_1c_watchdog_http_gateway.php`
- Result: `skipped=true`, `reason=TERMINAL_EXISTS`
- Today already has scheduled terminal `mars-20260807-080002-5bbdaf1c`
- No Telegram / no Data Table mutation expected or observed from this invocation

## Missing-run sandbox (server PHP 8.3)

Offline script `mars_1c_d6g1a_offline_regression.php`:

- R5 missing date → CREATE
- R6 same date → DEDUPE
- R7 next date → new event

PASS on server.

## Kill switch vs watchdog

Brief production config flip `CLIENT_OPS_DISPATCH_ENABLED=false` → watchdog reason `BLOCKED_BY_KILL_SWITCH` → restored `true`.
