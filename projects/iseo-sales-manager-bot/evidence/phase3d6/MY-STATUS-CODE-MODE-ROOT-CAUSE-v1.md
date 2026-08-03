# MY-STATUS CODE MODE ROOT CAUSE v1

**Hotfix id:** `3d6b-my-status-code-mode`  
**Workflow:** Admin.dev `wLrLp4WQHm1VJmxz` (same ID; no new workflows)  
**Operational.dev:** untouched  

## Root cause

`My Status` was created with Code-node mode `runOnceForEachItem`, but the node footer used `$input.first()`.

In n8n, `.first()` is forbidden in for-each mode and raises:

`Can't use .first() here [line 14, for item 0]`

The node then returned **0 items**, so Capture / Restore / Safe Telegram Reply were never reached. The caller received **no Telegram reply**.

This was a Code-node mode bug, not an ACCESS_CONTROL / role-matrix defect.

## Same incompatible mode

`Finalize Access Notification` used the same `runOnceForEachItem` + `$input.first()` pattern and would have broken grant/revoke finalize the same way.

## Repair (live, in place)

| Node | Before | After |
|---|---|---|
| My Status | `runOnceForEachItem` | `runOnceForAllItems` |
| Finalize Access Notification | `runOnceForEachItem` | `runOnceForAllItems` |
| Restore Admin Reply Target | Prepare lookup fragile | hardened safe Prepare lookup |

Constraints preserved:

- Admin.dev remained **54** nodes
- connections unchanged
- Operational.dev untouched
- AI remained OFF
- no workflow copies
- no `require('crypto')`
- no temporary debug reply / test-only routing left in place

## Acceptance rule

- Code using `$input.first()` / `$input.all()` must run in a compatible all-items mode.
- Code in `runOnceForEachItem` must use the current item context and must not call `$input.first()`.
- Sanitized workflow acceptance must record Code-node `mode`.
- Zero-item Code failures must be detected before deployment.
