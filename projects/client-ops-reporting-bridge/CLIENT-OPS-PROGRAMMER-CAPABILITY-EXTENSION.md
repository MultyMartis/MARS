# CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION

**Date:** 2026-07-23
**Charter:** MetaBOT Programmer — Client Ops Capability Extension
**Baseline commit:** `791de1d71485c65440f4da88203b6500b36aa0eb`
**Live mutations:** none

## Final status

| Area | Status |
|------|--------|
| MetaBOT Programmer capability intake | **COMPLETE** |
| Client Ops programmer extension | **COMPLETE** |
| Workflow template | **CREATED LOCALLY, NOT APPLIED** |
| Offline n8n harness | **PASS** |
| Sandbox workflow | **NOT CREATED** |
| Webhook tests | **NOT SENT** |
| Telegram | **NOT CONNECTED** |
| Production | **UNCHANGED** |

## Decisions frozen

### Auth MVP

- Header: `X-MARS-Client-Ops-Token` (Bearer also accepted).
- Validated in Code before business validation.
- Secret never in Git/template/responses.
- Placeholder: `<<<HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET>>>`
- Binding strategy: **HITL_REQUIRED** (exact Code@2 env/credential access syntax SAFE UNKNOWN).
- Hardening target: HMAC-SHA256(raw body + timestamp) — not implemented in first sandbox.

### Dedupe sandbox

- **`DEDUPE_DEFERRED_SANDBOX`**
- Response may include `dedupe: "DEFERRED_SANDBOX"` / `DEDUPE_NOT_ENABLED_SANDBOX`
- Production durable store still required later (Data Store unproven).

### Response contract

- ACCEPTED → HTTP 202
- DUPLICATE → HTTP 200
- UNAUTHORIZED → 401
- UNSUPPORTED_MEDIA_TYPE → 415
- INVALID_SCHEMA → 400
- SECURITY_REJECTED → 400
- PAYLOAD_TOO_LARGE → 413
- INTERNAL_ERROR → 500

### Workflow stages (sandbox)

Webhook → Capture → Process Gates (CT/auth/schema/security/event_id/dedupe) → IF → Prepare → Respond. No Telegram. No HTTP Request. No Storage write.

### Rollback default

Leave inactive and mark abandoned. Delete only under explicit HITL.

## Created files (primary)

- `n8n/templates/mars-client-ops-bridge-bzpm-sandbox.template.json`
- `n8n/harness/*`
- `n8n/runbooks/*`
- `n8n/experience-pack/*`
- `n8n/runners/run-client-ops-greenfield-create.skeleton.mjs`
- `projects/metabot-seo-content-agent/metabot-developer/client-ops-n8n-extension-v1.md`

## Harness usage

```bash
node projects/client-ops-reporting-bridge/n8n/harness/run-harness.mjs
node projects/client-ops-reporting-bridge/n8n/harness/validate-template.mjs
```

## Unresolved HITL

1. Auth secret binding mechanism in live n8n (env vs credential vs UI).
2. Exact n8n application version.
3. Production dedupe store.
4. Inactive sandbox create authorization (next charter).
5. Authenticated POST test authorization.
6. Telegram bot / chat approvals.
7. Production activation.

## Next create-sandbox task

**Phase 1B-B Inactive Sandbox Workflow Generation** — generate/apply inactive workflow through Cursor without manual n8n node assembly. Not started by this document.
