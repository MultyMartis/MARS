# PHASE 1B-D6G1A — Server Watchdog Scheduling, Residual Windows Hygiene and Server-Side Dispatch Kill Switch

## Summary

D6G1A formalized the server-side Client Ops dispatch kill switch (`CLIENT_OPS_DISPATCH_ENABLED`), proved live watchdog NO_SEND against today's scheduled terminal, hardened Post_1C monitor console hiding, and proved the Beget scheduling contour. **Beget watchdog cron could not be installed** because stored Hosting Panel credentials return API `AUTH_ERROR`.

## Evidence

`projects/client-ops-reporting-bridge/evidence/phase-1b-d6g1a-watchdog-windows-hygiene-kill-switch/`

## Readiness

`PARTIAL_D6G1A_WATCHDOG_CRON_NOT_ACTIVE`

## Operator follow-up

Add Beget panel cron `0 9 * * *` Europe/Moscow invoking watchdog HTTP gateway (token from local config), or refresh Beget API-capable panel password in SITE-002 secrets.
