# CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION

**Date:** 2026-07-23
**Charter:** MetaBOT Programmer — Client Ops Capability Extension
**Baseline commit:** `791de1d71485c65440f4da88203b6500b36aa0eb`
**Extension commit:** `04cd01d1881bccf6fc0dfeebef5b891e378fef37`
**Phase 1B-B:** inactive sandbox created (see [PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md](PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md))
**Phase 1B-B1:** native auth bound (see [PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md](PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md))
**Phase 1B-B2:** authenticated POST validated (see [PHASE-1B-B2-AUTHENTICATED-SANDBOX-POST-VALIDATION.md](PHASE-1B-B2-AUTHENTICATED-SANDBOX-POST-VALIDATION.md))

## Final status

| Area | Status |
|------|--------|
| MetaBOT Programmer capability intake | **COMPLETE** |
| Client Ops programmer extension | **COMPLETE** |
| Workflow template | **CREATED LOCALLY** |
| Offline n8n harness | **PASS** |
| Sandbox workflow | **CREATED INACTIVE + AUTH BOUND + POST VALIDATED** |
| Webhook tests | **SENT** (Phase 1B-B2 synthetic matrix; workflow returned inactive) |
| Telegram | **SANDBOX APPLY DONE** (`Telegram Notify Accepted` bound; inactive; one C1 delivery) |
| Production | **UNCHANGED** |

## Decisions frozen

### Auth MVP

- Header: `X-MARS-Client-Ops-Token` (Bearer also accepted by Code path historically; native Webhook Header Auth enforces the header credential).
- Live Phase 1B-B2 confirmation: **AUTH_NATIVE_HEADER_CREDENTIAL_CONFIRMED**.
- Observed native reject: HTTP **403** text `Authorization data is wrong!` (not workflow JSON 401).
- Credential display name: `MARS Client Ops Webhook Auth — bzpm.ru`.
- Credential type: `httpHeaderAuth`.
- Secret never in Git/template/responses/workflow JSON.
- Historical create placeholder: `<<<HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET>>>` (removed from live workflow after binding).
- Hardening target: HMAC-SHA256(raw body + timestamp) — not implemented.

### Dedupe sandbox

- **`DEDUPE_DEFERRED_SANDBOX`**
- Response may include `dedupe: "DEFERRED_SANDBOX"` / `DEDUPE_NOT_ENABLED_SANDBOX`
- Phase 1B-B2 duplicate `event_id` accepted twice — durable store still required later.
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

Webhook → Capture → Process Gates → IF → Prepare → Respond Accepted → **Telegram Notify Accepted** (Pattern B). Rejected path does not reach Telegram. No HTTP Request. No Storage write. Workflow remains inactive pending production activation charter.

### Rollback default

Leave inactive and mark abandoned. Delete only under explicit HITL.

## Created files (primary)

- `n8n/templates/mars-client-ops-bridge-bzpm-sandbox.template.json`
- `n8n/harness/*`
- `n8n/runbooks/*`
- `n8n/experience-pack/*`
- `n8n/runners/run-client-ops-greenfield-create.mjs` (+ write client, prepare/validate helpers)
- `n8n/runners/run-client-ops-credential-create.mjs` (+ credential client)
- `n8n/runners/run-client-ops-auth-binding-put.mjs` (+ workflow update client, prepare/validate helpers)
- `n8n/evidence/phase-1b-b-inactive-sandbox-create/`
- `n8n/evidence/phase-1b-b1-auth-binding/`
- `n8n/runners/run-client-ops-telegram-intake.mjs`
- `n8n/runners/run-client-ops-telegram-credential-create.mjs`
- `n8n/runners/validate-client-ops-telegram-message-contract.mjs`
- `n8n/runners/validate-client-ops-telegram-proposed-integration.mjs`
- `n8n/evidence/phase-1b-c-telegram-bot-intake/`
- `projects/metabot-seo-content-agent/metabot-developer/client-ops-n8n-extension-v1.md`

## Harness usage

```bash
node projects/client-ops-reporting-bridge/n8n/harness/run-harness.mjs
node projects/client-ops-reporting-bridge/n8n/harness/validate-template.mjs
node projects/client-ops-reporting-bridge/n8n/runners/prepare-client-ops-apply-payload.mjs
node projects/client-ops-reporting-bridge/n8n/runners/validate-client-ops-apply-payload.mjs
node projects/client-ops-reporting-bridge/n8n/runners/run-client-ops-greenfield-create.mjs
node projects/client-ops-reporting-bridge/n8n/runners/run-client-ops-telegram-intake.mjs
node projects/client-ops-reporting-bridge/n8n/runners/run-client-ops-telegram-credential-create.mjs
```

## Unresolved HITL

1. Exact n8n application version.
2. Concurrent atomicity / unique `event_id` enforcement (D1 sequential proven; concurrency unproven).
3. Post-Telegram durable `delivery_state=SENT` ledger (deferred).
4. Runtime producer live connection (D2 offline producer complete; live POST remains D3+; no live connection until later charter).
5. Production activation (separate charter; last).

## Architecture decisions captured in Phase 1B-D0

- Durable dedupe **before** any runtime producer connection.
- Preferred producer pattern **R1** (exporter → webhook); fallback **R3**.
- Preferred dedupe store: n8n **Data Table** (OpenAPI-proven); fallback producer ledger.
- Manual/HITL before scheduler; clean runtime checkout required for schedules (never dirty `X:\AI MARS`).
- Production activation remains forbidden until full gate list.

## Phase 1B-D1 result (inactive)

- Durable sequential dedupe proven: FIRST_SEEN / DUPLICATE / EVENT_ID_CONFLICT.
- Table `MARS Client Ops Dedupe — bzpm.ru` (`H6VYhwz7RXZCBMmu`) retained with one synthetic proof row.
- First attempt failed (`require('crypto')` disallowed; execution 3410) and was rolled back; successful path final executions=29.
- Classification: `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN`.

## Next charter

**Phase 1B-D2 — Sequential Runtime Producer Design and Offline Implementation** — COMPLETE offline (`READY_FOR_SEQUENTIAL_RUNTIME_PRODUCER_OFFLINE_BASELINE_COMMIT`); `push-webhook` returns `NETWORK_DISPATCH_NOT_AUTHORIZED_D2`. Do not call Client Ops webhook unless Phase 1B-D3 controlled connection is approved.
