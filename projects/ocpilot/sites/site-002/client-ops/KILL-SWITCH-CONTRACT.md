# SITE-002 — Server Kill Switch Contract

## Flag

`CLIENT_OPS_DISPATCH_ENABLED`

Location: protected **non-Git** local config (historically `mars_1c_wrapper.local.php` pattern on server).  
Accepted production state has been **enabled=true** when Client Ops live; treat live boolean as operational fact, not a secret — **do not print other secret values**.

## What it blocks

- Outbound completion dispatch to n8n / Telegram path.
- Watchdog outbound should **respect** the kill switch.

## What it does NOT block

- Import execution.
- Terminal run state recording.
- Admin ability to launch import (import still runs; only outbound may stop).

## Admin visibility

OpenCart admin includes **read-only** dispatch status visibility (`SITE002_ADMIN_DISPATCH_STATE_VISIBLE=YES` historically accepted).

## Related declarations

- `SITE002_SERVER_DISPATCH_KILL_SWITCH_READY=YES`
- `SITE002_SERVER_DISPATCH_ENABLED=YES` (when live enabled)

## Rule

**Terminal recording must remain decoupled from outbound dispatch.**
