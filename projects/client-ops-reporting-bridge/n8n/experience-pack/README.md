# Client Ops n8n Experience Pack

**Status:** PARTIAL — CREATE + AUTH BINDING + AUTHENTICATED POST + TELEGRAM INTAKE + SEMANTICS CAPTURED
Telegram delivery sandbox apply is complete on the inactive Client Ops workflow (Phase 1B-C1; one delivery verified). Production activation remains pending.

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

## Facts learned from Phase 1B-C / 1B-C0 / 1B-C0R2 Telegram intake

- Credential type: `telegramApi` with `accessToken` (optional `baseUrl`).
- Dedicated credential name: `MARS Client Ops Telegram — bzpm.ru` (`2bIC5376l7ElXb4B`) — unbound.
- Bot username: `monitor_bzpm_metacode_bot` (ID `8852310960`).
- Live credential schema `GET /api/v1/credentials/schema/telegramApi` returns `{ accessToken, baseUrl }` (`additionalProperties: false`; `baseUrl` optional).
- Credential create uses `type: "telegramApi"` and `data.accessToken` from gitignored `telegram.secrets.local.env`.
- Telegram node credential reference key is `telegramApi` (MetaBOT precedent + live schema).
- Read-only Bot API intake allowlist: `getMe`, `getWebhookInfo`, conditional single `getUpdates` without `offset`.
- Phase 1B-C0 discovery confirmation phrase: `DISCOVER CLIENT OPS TELEGRAM CHAT TARGET`.
- Phase 1B-C0R2 final discovery confirmation phrase: `FINAL DISCOVER CLIENT OPS TELEGRAM CHAT TARGET`.
- Chat target may be absent after bot create until operator presses Start — does not block credential intake; Phase 1B-C0 returned 0 updates; Phase 1B-C0R2 confirmed one private chat after operator Start/`/start`.
- Proposed Pattern B: Respond to Webhook first, then Telegram `sendMessage` on accepted path only — **runtime-confirmed** in Phase 1B-C0S; **applied** to inactive Client Ops workflow in Phase 1B-C1.
- Phase 1B-D0 charter complete: durable dedupe **before** runtime producer; preferred pattern **R1**; preferred store n8n **Data Table**; dirty-main scheduling **forbidden**.

## Facts learned from Phase 1B-C0S semantics verification

- On this n8n host, nodes connected after `Respond to Webhook` continue to execute (`PATTERN_B_STRUCTURALLY_SUPPORTED`).
- Telegram `sendMessage` after Respond executes once with delivery marker (`PATTERN_B_CONFIRMED`).
- Temporary semantics workflow pattern: create inactive → activate → one POST → deactivate in `finally` → delete after evidence.
- Message budget for semantics: exactly one Telegram message total across the phase.
- Real Client Ops workflow must remain denylisted for mutation during semantics tests.

## Facts learned from Phase 1B-D0 (decision only)

- Live workflow GET-only reconfirmed inactive; executions remain 25; versionId unchanged.
- OpenAPI on this install documents **Data Table** APIs including upsert; legacy Data Store not present in OpenAPI.
- Duplicate `event_id` under deferred dedupe + Pattern B Telegram ⇒ durable dedupe is mandatory before runtime producer connection.
- Preferred first runtime pattern: exporter → authenticated webhook (R1); fallback file pickup adapter (R3).
- Scheduler ownership: dedicated Windows task later; never from dirty `X:\AI MARS`; use clean Storage runtime checkout when created.

## Facts learned from Phase 1B-D1 (inactive durable dedupe)

- Data Table workflow node `n8n-nodes-base.dataTable` typeVersion 1.1 works for get/insert.
- `require('crypto')` is disallowed in this n8n Code sandbox (failed execution 3410) → fingerprint is canonical JSON equality.
- Sequential proof: FIRST_SEEN → 202 + Telegram; EXACT_REPLAY → 200 DUPLICATE_SUPPRESSED no Telegram; EVENT_ID_CONFLICT → 409 no Telegram.
- Final inactive state: nodes=17; executions=29; table `H6VYhwz7RXZCBMmu` retained; one synthetic proof row.
- Classification: `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN`; post-Telegram SENT ledger deferred.

## Still incomplete until later charters

- Phase 1B-D2 Sequential Runtime Producer Design (offline)
- Runtime producer live HTTP connection (D2 offline producer done; D3 controlled charter later)
- Scheduler connection (after manual E2E)
- Concurrent atomicity / unique event_id enforcement
- Post-Telegram durable SENT ledger
- Production activation (last; separate charter)
