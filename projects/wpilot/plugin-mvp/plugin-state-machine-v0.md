# WPilot Plugin State Machine v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** exact operational states for the first installable plugin MVP.

The state machine prevents implicit escalation. A route may operate only when its required state is active.

## States

| State | Meaning | Operational access |
|---|---|---|
| `disabled` | Plugin installed/activated, bridge off. Default state. | Only admin settings and unauthenticated `ping`. |
| `enabled-dev` | Administrator enabled bridge and confirmed DEV/test use. | Token generation and authenticated read readiness. |
| `token-generated` | Valid per-site token exists. | Authenticated read endpoints may operate after permission checks. |
| `read-only-active` | Token-authenticated read operations have passed state/auth checks. | Read endpoints only. |
| `write-enabled` | DEV confirmed, token valid, write settings valid. | Backup, dry-run, scoped replace, rollback routes may proceed through validation. |
| `rollback-available` | At least one plugin-created backup exists for a target. | Rollback may be requested for that target/backup only. |
| `emergency-disabled` | Bridge forcibly stopped by admin or fatal safety condition. | Operational endpoints refuse. Admin intervention required. |
| `invalid-config` | Required storage/options/schema/token state is missing or inconsistent. | Operational endpoints refuse. Admin repair/reinstall required. |
| `safe-unknown` | Plugin cannot safely classify current environment or target condition. | Refuse risky operation; allow limited reporting. |

## Initial State

After activation:

- State must be `disabled`.
- `dev_confirmed` must be false.
- No write endpoint may operate.
- No token is generated unless a human administrator explicitly requests it.

## Allowed Transitions

| From | To | Trigger | Required operator action |
|---|---|---|---|
| `disabled` | `enabled-dev` | Admin confirms DEV/test and enables bridge. | Explicit admin save with nonce/capability check. |
| `enabled-dev` | `token-generated` | Admin generates token. | Explicit token generation. |
| `token-generated` | `read-only-active` | Valid token used on read route. | Token supplied by operator. |
| `read-only-active` | `write-enabled` | Write route requested with valid token and approval reference. | Human approval reference for write-like operation. |
| `write-enabled` | `rollback-available` | Backup created for target. | Backup operation succeeds. |
| `rollback-available` | `write-enabled` | Rollback succeeds or operator continues testing. | Manual verification. |
| Any non-emergency state | `disabled` | Admin disables bridge. | Explicit admin action. |
| Any state | `emergency-disabled` | Admin emergency stop or critical safety failure. | Admin action or safety condition. |
| Any operational state | `invalid-config` | Storage/schema/token/options failure detected. | Admin repair required. |
| Any operation-specific state | `safe-unknown` | Environment/target cannot be classified safely. | Manual inspection required. |

## Forbidden Transitions

The MVP must not allow:

- `disabled` -> `token-generated` without DEV confirmation.
- `disabled` -> `write-enabled`.
- `enabled-dev` -> `write-enabled` without token.
- `token-generated` -> `write-enabled` without human approval for execution.
- `read-only-active` -> mutation without backup-first validation.
- `safe-unknown` -> `write-enabled` automatically.
- `invalid-config` -> operational state automatically.
- `emergency-disabled` -> operational state without explicit administrator action.
- Any state -> autonomous/background mutation.

## Emergency Stop Behavior

Emergency stop must:

- Set bridge operational state to `emergency-disabled`.
- Reject all operational REST endpoints.
- Preserve existing audit and backup records.
- Avoid deleting data automatically.
- Require administrator action to leave emergency state.

Emergency stop may be triggered by:

- Admin emergency button.
- Repeated critical audit/storage failures.
- Detection that write validation cannot be trusted.
- Suspected token exposure.
- Security incident.

## Operator Intervention Requirements

Operator intervention is required for:

- DEV/test confirmation.
- Enabling bridge.
- Token generation, rotation, and revocation.
- Moving from read-only inspection to write execution.
- Accepting dry-run result.
- Running rollback.
- Leaving `emergency-disabled`.
- Repairing `invalid-config`.
- Resolving `safe-unknown`.

## SAFE UNKNOWN State Handling

`safe-unknown` is a refusal state for risky operations.

Allowed:

- Return compact SAFE UNKNOWN response.
- Log refusal where possible.
- Suggest manual inspection.
- Allow unrelated safe read endpoints when global plugin state is healthy.

Not allowed:

- Automatic repair.
- Fallback to SQL/filesystem.
- Broadened permissions.
- Hidden mutation.
- Conversion to success.

## State Storage

Minimum option-backed state fields:

- `wpilot_enabled`
- `wpilot_dev_confirmed`
- `wpilot_emergency_disabled`
- `wpilot_schema_version`
- `wpilot_token_exists`
- `wpilot_last_safety_error`

Computed states may combine options, token metadata, storage availability, and per-target backup availability.

