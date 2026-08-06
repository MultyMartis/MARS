# PHASE-1B-B2 — Authenticated Sandbox POST Validation

**Date:** 2026-07-24
**Workflow name:** `MARS Client Ops Bridge — bzpm.ru`
**Live workflow ID:** `tkM4H0G0gM3q9Foi`
**Credential:** `MARS Client Ops Webhook Auth — bzpm.ru` (`WKHmPaw6QBp7WnzP`)
**Status:** AUTHENTICATED SANDBOX POST MATRIX PASSED — WORKFLOW RETURNED INACTIVE

## POST mode

| Field | Value |
|-------|-------|
| Verdict | `POST_MODE_CONTROLLED_TEMPORARY_ACTIVATION` |
| Host class | approved MARS n8n |
| Route class | production webhook |
| URL exposed | NO |
| Activation changes | 2 (activate + deactivate) |
| Final active | `false` |

## Matrix summary

- T01/T02: native Header Auth reject HTTP **403** (`Authorization data is wrong!`); no business executions.
- T05–T08, T27–T28: HTTP **202** `ACCEPTED` + `dedupe=DEFERRED_SANDBOX`.
- T09–T17: HTTP **400** `INVALID_SCHEMA`.
- T18–T25: HTTP **400** `SECURITY_REJECTED`.
- T03: HTTP **415** workflow `UNSUPPORTED_MEDIA_TYPE`.
- T04: native HTTP **422** parse failure (no execution).
- T26: intended 413; observed native HTTP **422** parse failure for oversized body (safe reject; no execution; contract discrepancy documented).

## Executions

| Stage | Count |
|-------|-------|
| Baseline | 0 |
| Final | 24 |

Attribution: 28 POSTs − T01/T02 (native auth) − T04/T26 (native parse, no execution) = **24** workflow executions. All `workflowId=tkM4H0G0gM3q9Foi`, status `success`.

## Dedupe

`DEDUPE_DEFERRED_SANDBOX` — duplicate `event_id` accepted twice. Not production-ready durable dedupe.

## Telegram / production

| Item | State |
|------|-------|
| Telegram nodes | absent |
| Telegram messages | 0 |
| SITE-002 production | untouched |
| Exporter runtime POST | not implemented |

## Readiness

`READY_FOR_TELEGRAM_BOT_INTAKE`

Does **not** authorize Telegram integration yet.

Future bot (unchanged):

- display name: `Монитор bzpm.ru — MetaCODE`
- avatar: bzpm.ru logo
- token later via local secret boundary

## Evidence

`projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-b2-authenticated-post-validation/`

## Next permitted phase

**Phase 1B-C — Telegram Bot Intake and Sandbox Integration Preparation** — **COMPLETE** for intake; see [PHASE-1B-C-TELEGRAM-BOT-INTAKE-AND-INTEGRATION-PREPARATION.md](PHASE-1B-C-TELEGRAM-BOT-INTAKE-AND-INTEGRATION-PREPARATION.md). Next: **Phase 1B-C0**.
