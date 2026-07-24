# Client Ops n8n Experience Pack

**Status:** PARTIAL — CREATE + AUTH BINDING + AUTHENTICATED POST CAPTURED
Telegram and production activation remain incomplete.

## Contents

| File | Purpose |
|------|---------|
| `CLIENT-OPS-N8N-PATTERNS.md` | Accepted patterns |
| `CLIENT-OPS-N8N-ANTI-PATTERNS.md` | Forbidden patterns |
| `CLIENT-OPS-N8N-SYNTAX-MATRIX.md` | Live-evidenced syntax |
| `CLIENT-OPS-N8N-APPLY-EVIDENCE-TEMPLATE.md` | Apply evidence template |
| `CLIENT-OPS-N8N-ROLLBACK-EVIDENCE-TEMPLATE.md` | Rollback evidence template |

## Facts learned from Phase 1B-B inactive create

- Greenfield `POST /api/v1/workflows` with `{name, nodes, connections, settings}` creates inactive workflow successfully.
- Server-managed fields observed on create/re-GET: `id`, `versionId`, `createdAt`, `updatedAt`, plus `settings.callerPolicy` / `settings.availableInMCP`.
- n8n may assign `webhookId` on inactive create even when omitted from the client payload — treat as server-managed; do not embed client-invented webhook IDs.
- Credential binding pattern for create phase: **AUTH_BLOCKED_INACTIVE_ONLY** — no n8n credential created; local gitignored secret prepared; Code placeholder retained.
- Read-back matched client-managed graph (names/types/typeVersions/disabled/connections); no material unexpected graph drift.
- Apply runner lessons: separate write client from GET-only exporter; require `--apply` + exact confirmation phrase; re-GET immediately; sanitize evidence; never activate.
- Rollback boundary: leave inactive; delete HITL-only; no credential orphan in create phase.

## Facts learned from Phase 1B-B1 native auth binding

- Live OpenAPI documents `POST /api/v1/credentials` and states list responses omit credential secrets.
- Credential schema endpoint `GET /api/v1/credentials/schema/httpHeaderAuth` returns `{name, value}` fields on this installation.
- Correct credential type name is `httpHeaderAuth` (type name `headerAuth` returns 404).
- Webhook@2.1 accepts `parameters.authentication = "headerAuth"` with credentials key `httpHeaderAuth: {id, name}`.
- Credential create payload shape (sanitized): `{ name, type: "httpHeaderAuth", data: { name: "<Header-Name>", value: "<secret>" } }` — value never stored in Git.
- Safe secret-loading pattern: read gitignored `secrets.local.env` into process memory only; never print; never pass on argv; never write into workflow JSON.
- Controlled auth-only PUT pattern: allowlisted workflow ID client; strip `webhookId`/read-only fields; require `--apply` + confirmation phrase; compare `versionId` pre-PUT; save gitignored rollback; immediate re-GET.
- After native binding, remove Code placeholder shared-secret comparison and retain `auth_mode=NATIVE_HEADER_AUTH` marker.
- Rollback lesson: leave inactive after successful auth-only PUT; retain ignored raw rollback; do not auto-delete credential.

## Facts learned from Phase 1B-B2 authenticated POST

- Preferred POST mode when test-listen API is absent: controlled temporary activation + production webhook route class + deactivate in `finally`.
- Native Header Auth reject: HTTP 403 plain text `Authorization data is wrong!`; no business execution.
- Valid authenticated envelopes: HTTP 202 `ACCEPTED` with `dedupe: DEFERRED_SANDBOX`.
- Validation/security rejects: HTTP 400 with `INVALID_SCHEMA` / `SECURITY_REJECTED`.
- Unsupported Content-Type: workflow HTTP 415 after auth.
- Malformed JSON and oversized payloads: native HTTP 422 parse failure may occur before workflow gates (no execution).
- Duplicate event_id under deferred dedupe: both submissions accepted.
- Evidence redaction: never store full webhook URL/path, auth secret, or raw execution payloads in Git.

## Still incomplete until later charters

- Telegram delivery
- Production activation
- Durable dedupe store
