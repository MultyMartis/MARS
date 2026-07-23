# CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION

**Date:** 2026-07-23
**Charter:** MetaBOT Programmer — Client Ops Capability Extension
**Baseline commit:** `791de1d71485c65440f4da88203b6500b36aa0eb`
**Extension commit:** `04cd01d1881bccf6fc0dfeebef5b891e378fef37`
**Phase 1B-B:** inactive sandbox created (see [PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md](PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md))

## Final status

| Area | Status |
|------|--------|
| MetaBOT Programmer capability intake | **COMPLETE** |
| Client Ops programmer extension | **COMPLETE** |
| Workflow template | **CREATED LOCALLY** |
| Offline n8n harness | **PASS** |
| Sandbox workflow | **CREATED INACTIVE** (`AUTH_BLOCKED_INACTIVE_ONLY`) |
| Webhook tests | **NOT SENT** |
| Telegram | **NOT CONNECTED** |
| Production | **UNCHANGED** |

## Decisions frozen

### Auth MVP

- Header: `X-MARS-Client-Ops-Token` (Bearer also accepted).
- Validated in Code before business validation.
- Secret never in Git/template/responses.
- Placeholder: `<<<HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET>>>`
- Live Phase 1B-B binding: **AUTH_BLOCKED_INACTIVE_ONLY** (native header credential create not evidenced; local secret prepared under gitignored `local/`, not bound into n8n).
- Hardening target: HMAC-SHA256(raw body + timestamp) — not implemented.

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
- `n8n/runners/run-client-ops-greenfield-create.mjs` (+ write client, prepare/validate helpers)
- `n8n/evidence/phase-1b-b-inactive-sandbox-create/`
- `projects/metabot-seo-content-agent/metabot-developer/client-ops-n8n-extension-v1.md`

## Harness usage

```bash
node projects/client-ops-reporting-bridge/n8n/harness/run-harness.mjs
node projects/client-ops-reporting-bridge/n8n/harness/validate-template.mjs
node projects/client-ops-reporting-bridge/n8n/runners/prepare-client-ops-apply-payload.mjs
node projects/client-ops-reporting-bridge/n8n/runners/validate-client-ops-apply-payload.mjs
node projects/client-ops-reporting-bridge/n8n/runners/run-client-ops-greenfield-create.mjs
```

## Unresolved HITL

1. Auth secret binding mechanism in live n8n (native header credential vs proven env) — still blocked.
2. Exact n8n application version.
3. Production dedupe store.
4. Authenticated POST test authorization.
5. Telegram bot / chat approvals (future display name: `Монитор bzpm.ru — MetaCODE`; avatar: bzpm.ru logo).
6. Production activation.

## Next charter

**Phase 1B-B1 — Native Webhook Auth Binding Intake and Controlled Apply** — do not begin without explicit operator charter. Authenticated sandbox POST validation remains after auth binding succeeds.
