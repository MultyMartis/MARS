# ADMIN ACTIVATION WINDOW RECEIPT v1

## Windows

| Event | Time (UTC) | Notes |
|-------|------------|-------|
| First activate + readiness ping | 2026-07-30T20:11:31.114Z | sidecar WH ping; Trigger enabled |
| Re-register + second ping | 2026-07-30T20:17:46.604Z | force Trigger webhook rebind |
| Clean Trigger-only activate | 2026-07-30T20:19:42.966Z | sidecar removed |
| Final deactivate | 2026-07-30T20:34:36.006Z | Admin active=false |

## Guards during window

- Operational.dev active: **false** (verified)
- Sales-Manager-v2 active: **true** (verified)
- Allowlist size: **1** (CONFIG)
- Readiness listed canonical commands only (no alias instructions)

## Temporary activations count

**3**

## Final

- Admin.dev active: **false**
