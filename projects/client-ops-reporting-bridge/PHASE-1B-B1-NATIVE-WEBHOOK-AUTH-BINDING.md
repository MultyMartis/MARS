# PHASE-1B-B1 — Native Webhook Auth Binding

**Date:** 2026-07-23
**Workflow name:** `MARS Client Ops Bridge — bzpm.ru`
**Live workflow ID:** `tkM4H0G0gM3q9Foi`
**Status:** NATIVE HEADER AUTH BOUND — WORKFLOW REMAINS INACTIVE

## Auth discovery

| Candidate | Evidence | Supported | Security assessment |
|-----------|----------|-----------|---------------------|
| Native Header Auth (`httpHeaderAuth`) | Live OpenAPI + `/api/v1/credentials/schema/httpHeaderAuth`; post-PUT Webhook `authentication=headerAuth` | YES | Preferred — secret outside workflow JSON |
| Basic Auth (`httpBasicAuth`) | Schema available | YES | Not preferred for PROFILE_B header token |
| Environment binding in Code@2 | Not evidenced | SAFE UNKNOWN | Not used |
| Code-node embedded secret | Forbidden by policy | NO | Would leak into workflow JSON |
| HMAC-SHA256 | Future hardening only | NO (this task) | Deferred |

**Authentication verdict:** `AUTH_NATIVE_HEADER_CREDENTIAL_CONFIRMED`

## Credential

| Field | Value |
|-------|-------|
| created | YES (exactly once) |
| id | `WKHmPaw6QBp7WnzP` |
| display name | `MARS Client Ops Webhook Auth — bzpm.ru` |
| type | `httpHeaderAuth` |
| header name | `X-MARS-Client-Ops-Token` |
| secret source | gitignored `local/.../secrets.local.env` key `CLIENT_OPS_WEBHOOK_AUTH_SECRET` |
| secret exposed | NO |

## Workflow PUT

| Field | Value |
|-------|-------|
| applied | YES (exactly once) |
| active | `false` |
| executions | `0` |
| webhook test | NO |
| Telegram | absent |
| auth placeholder | removed |
| auth mode | `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND` / `NATIVE_HEADER_AUTH` |
| dedupe | `DEDUPE_DEFERRED_SANDBOX` |

## Rollback

Raw pre-PUT snapshot under gitignored:

`local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-b1/`

Rollback required now: **NO**.

## Next permitted phase

**Phase 1B-C — Telegram Bot Intake and Sandbox Integration Preparation**

Phase 1B-B2 authenticated POST validation is **COMPLETE** — see [PHASE-1B-B2-AUTHENTICATED-SANDBOX-POST-VALIDATION.md](PHASE-1B-B2-AUTHENTICATED-SANDBOX-POST-VALIDATION.md).

## Evidence

`projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-b1-auth-binding/`
