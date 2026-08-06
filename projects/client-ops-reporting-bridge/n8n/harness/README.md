# Client Ops n8n offline harness

**Status:** OFFLINE ONLY
**Network:** forbidden
**Live n8n:** not invoked

## Purpose

Validate Client Ops webhook intake JavaScript (`Code@2`-compatible) against synthetic envelopes before any sandbox workflow create.

## Commands

```bash
node projects/client-ops-reporting-bridge/n8n/harness/generate-cases.mjs
node projects/client-ops-reporting-bridge/n8n/harness/run-harness.mjs
node projects/client-ops-reporting-bridge/n8n/harness/build-template.mjs
node projects/client-ops-reporting-bridge/n8n/harness/validate-template.mjs
```

## Auth test secret

Harness uses only:

`SYNTHETIC_CLIENT_OPS_HARNESS_SECRET_v1_NOT_A_REAL_CREDENTIAL`

This is **not** a production credential and must never be copied into live n8n credentials.

## Files

| Path | Role |
|------|------|
| `client-ops-validator.mjs` | Pure validation library |
| `run-harness.mjs` | Case runner |
| `cases/*.json` | Synthetic fixtures |
| `build-template.mjs` | Builds inactive local template |
| `validate-template.mjs` | Pre-create structural gates |

## Required case families

1–4 valid statuses · schema/site/event rejects · security rejects · auth rejects · oversized · duplicate-deferred sandbox
