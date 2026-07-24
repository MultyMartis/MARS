# Client Ops n8n Syntax Matrix

**Status:** PARTIAL — refreshed during Phase 1B-B
**Authority:** MetaBOT live/reference exports + Phase 1B-B create/re-GET evidence

| Node | type | typeVersion | Notes |
|------|------|-------------|-------|
| Webhook | `n8n-nodes-base.webhook` | `2.1` | Prefer `responseMode=responseNode`; Phase 1B-B1 bound `authentication=headerAuth` + `credentials.httpHeaderAuth` |
| Code | `n8n-nodes-base.code` | `2` | `return [{ json: {...} }]` |
| IF | `n8n-nodes-base.if` | `2.3` | true=`main[0]`, false=`main[1]` |
| Switch | `n8n-nodes-base.switch` | `3` / `3.2` | Not used in first sandbox template |
| Set | `n8n-nodes-base.set` | `2` | Evidenced; first template prefers Code@2 |
| HTTP Request | `n8n-nodes-base.httpRequest` | `4` / `4.4` | Not in first sandbox |
| Telegram | `n8n-nodes-base.telegram` | `1` / `1.2` | Not in first sandbox |
| Respond to Webhook | `n8n-nodes-base.respondToWebhook` | `1.1` | Live sandbox-get evidence + Client Ops create |

## Expressions

- `={{ ... }}`
- `$json`
- `$('Node Name').first().json`

## Phase 1B-B create notes

- Inactive create omitted `webhookId`; server assigned one.
- Create payload schema accepted without top-level `active` (workflow remained inactive).
- Auth mode used at create: `AUTH_BLOCKED_INACTIVE_ONLY`.
- Auth mode after Phase 1B-B1: `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND`.
- Auth mode after Phase 1B-B2: `AUTH_NATIVE_HEADER_CREDENTIAL_CONFIRMED`.

## Phase 1B-B1 auth notes

- Credential type: `httpHeaderAuth` (schema confirmed live).
- Webhook param: `authentication: "headerAuth"`.
- Credential reference shape: `{ credentials: { httpHeaderAuth: { id, name } } }`.
- Header name: `X-MARS-Client-Ops-Token`.
- Credential create: `POST /api/v1/credentials` with write-only `data`.
- List/GET workflow exposes credential id/name only.

## Phase 1B-B2 POST notes

- Activate: `POST /api/v1/workflows/{id}/activate` (allowlisted ID only).
- Deactivate: `POST /api/v1/workflows/{id}/deactivate` in `finally`.
- Production webhook route class used after temporary activation (URL never stored in Git evidence).
- Native auth reject: HTTP 403 text `Authorization data is wrong!`.
- Valid accept: HTTP 202 `{ ok:true, result:"ACCEPTED", dedupe:"DEFERRED_SANDBOX" }`.
- Malformed JSON / oversized: native HTTP 422 `Failed to parse request body` (may skip workflow execution).
- Content-Type reject: workflow HTTP 415 `UNSUPPORTED_MEDIA_TYPE` after auth.
- Duplicate event_id: both accepted under deferred dedupe.

## SAFE UNKNOWN

- Exact n8n application version.
- Authenticated/unauthorized webhook POST HTTP status/body semantics (deferred to Phase 1B-B2).
- Data Store availability.
- Secure Code-node access to env secrets (not required after native Header Auth).
