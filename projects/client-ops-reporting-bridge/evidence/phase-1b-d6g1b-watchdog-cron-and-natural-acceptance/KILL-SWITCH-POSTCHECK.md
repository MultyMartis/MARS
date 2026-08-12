# Kill Switch Postcheck

Production `mars_1c_wrapper.local.php`:

- `CLIENT_OPS_DISPATCH_ENABLED=true`
- `server_dispatch_enabled=true`
- `watchdog_enabled=true`

Computed UI label from dispatcher helper:

- `Отчёты в Telegram: Включены`

Natural scheduled reports Aug 8–12 themselves prove outbound dispatch remained enabled.

No kill-switch toggle performed in this phase.

Gate: `D6G1B_SERVER_KILL_SWITCH_ENABLED`
