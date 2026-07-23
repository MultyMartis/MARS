# PHASE-1B-B — Inactive Sandbox Workflow Generation

**Date:** 2026-07-23
**Workflow name:** `MARS Client Ops Bridge — bzpm.ru`
**Live workflow ID:** `tkM4H0G0gM3q9Foi`
**Status:** CREATED INACTIVE AND STRUCTURALLY VERIFIED

## Live state

| Field | Value |
|-------|-------|
| active | `false` |
| executions observed | `0` |
| webhook calls | `0` |
| Telegram | absent |
| node count | 9 |
| auth binding | `AUTH_BLOCKED_INACTIVE_ONLY` at create; superseded by Phase 1B-B1 `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND` |
| dedupe | `DEDUPE_DEFERRED_SANDBOX` |

## Auth binding verdict

`AUTH_BLOCKED_INACTIVE_ONLY`

Evidence:

- Live webhook nodes on this n8n instance do not demonstrate native header-auth credential parameters.
- Credential list API is readable, but no accepted Client Ops / MetaBOT header-auth credential-create payload shape is evidenced.
- Exact Code@2 env/credential secret access syntax remains SAFE UNKNOWN — not invented.
- Local secret prepared at gitignored `local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env` (`CLIENT_OPS_WEBHOOK_AUTH_SECRET`) and **not** written into workflow JSON or n8n credentials.
- Workflow retains `<<<HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET>>>` and rejects auth as unresolved if ever executed without a later binding charter.

Preferred credential display name (future): `MARS Client Ops Webhook Auth — bzpm.ru` — **not created** in this phase.

## Server-managed observation

n8n assigned a `webhookId` on inactive create. Documented as server-managed; create payload omitted `webhookId`.

## No test POST

Authenticated HTTPS POST was **not** performed.

## No Telegram

Bot display name reserved for a later gated phase:

`Монитор bzpm.ru — MetaCODE`

Avatar requirement for later: bzpm.ru logo.
Token: to be supplied later through local non-Git secret boundary.
No Telegram node/credential/message in this phase.

## Rollback

Default: leave inactive. Deletion HITL-only. Rollback required now: **NO**.

## Next HITL gates

1. **Phase 1B-B1 — Native Webhook Auth Binding** — **COMPLETE** (see `PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md`).
2. **Phase 1B-B2 — Authenticated Sandbox POST Validation** (separate charter) — do not activate; validate unauthorized/authorized POST behavior only under explicit charter.
3. Later Telegram bot/credential/message charter.
4. Production activation remains blocked.

## Evidence

`projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-b-inactive-sandbox-create/`
