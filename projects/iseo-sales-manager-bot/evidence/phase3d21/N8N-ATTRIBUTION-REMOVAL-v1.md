# N8N ATTRIBUTION REMOVAL v1

**Phase:** 3D.2.1

## Observation

Operator-facing readiness traffic in Phase 3D.2 used a temporary Telegram send sidecar with `additionalFields: {}` (attribution not disabled). Permanent Admin/Operational send nodes already carried `appendAttribution: false` from earlier phases; Phase 3D.2.1 re-asserted the flag on all Telegram send nodes.

## Patch

| Workflow | Node | Setting |
|----------|------|---------|
| Admin.dev | Safe Telegram Reply | `additionalFields.appendAttribution = false` |
| Operational.dev | Send Telegram Lead Card | `additionalFields.appendAttribution = false` |
| Phase 3D.2.1 readiness sidecar | Send Notice | `appendAttribution: false` (temporary; removed after send) |

## Verification

- Preflight attribution audit: Admin/Ops permanent nodes already `false`; patch idempotent.
- Readiness notice script forced `appendAttribution: false`.
- No credential change.
- Message body unchanged aside from Phase 3D.2.1 readiness copy.

## Required outcome

No `This message was sent automatically with n8n` footer and no n8n URL attribution on operator Admin messages when using the patched send path.
