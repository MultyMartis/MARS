# AUTHORIZATION RUNTIME EVIDENCE v1

## Unauthorized synthetic path

| Check | Result |
|-------|--------|
| authorized | false |
| reply | Недостаточно прав. |
| privileged CONFIG leak | no |
| allowlist mutated | no |

Nodes observed: Normalize Command → Read Authorization Config → Check User Authorization → IF Authorized → Deny Reply → Capture Admin Reply → Safe Telegram Reply.

## Authorized path

Real Telegram Trigger authorized path: **not confirmed** (no operator Trigger executions in the activation window).

Harness (non-trigger) authorized replies: PASS for allowlisted operator identity after Normalize Command body-wrap fix.
