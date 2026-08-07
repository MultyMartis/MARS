# Kill Switch Contract

## Key

Preferred: `CLIENT_OPS_DISPATCH_ENABLED`  
Accepted equivalent: `server_dispatch_enabled`  

Location: non-Git `storage/mars-tools/cron/mars_1c_wrapper.local.php`

## Values

- `true` (default production after D6G1A): dispatch allowed
- `false`: outbound blocked

## Behavior when false

- Import runs normally
- Terminal still written
- Completion dispatcher status: `BLOCKED_BY_KILL_SWITCH`
- Watchdog: skip reason `BLOCKED_BY_KILL_SWITCH`
- No webhook / Telegram / Data Table mutation
- Recovery: set true + recovery sweep / explicit dispatch of pending/blocked runs (idempotent via delivered marker)

## Not controlled

- 1C import execution
- OpenCart admin page availability
- Status inspection
- Workflow active flag
