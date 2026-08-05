# /lead_history ROUTER REPAIR v1

## Defect

Normalize contained a comment mention only. **Route Command had no `/lead_history` rule** → Unknown Command.

## Repair

- Added nodes: `Read LEADS for History`, `Read LEAD_EVENTS for History`, `Lead History Handler`
- Route rule + connection aligned (history before Switch fallback)
- Auth: `/leads` + `/lead_history` in `STAFF_PENDING_COMMANDS` (Admin + active moderator); removed `/leads` from `ADMIN_ONLY_COMMANDS`
