# Phase 1B-B2 — Authenticated Sandbox POST Validation (evidence)

**Workflow:** `MARS Client Ops Bridge — bzpm.ru` (`tkM4H0G0gM3q9Foi`)
**Credential:** `MARS Client Ops Webhook Auth — bzpm.ru` (`WKHmPaw6QBp7WnzP`)
**POST mode:** `POST_MODE_CONTROLLED_TEMPORARY_ACTIVATION`
**Verdict:** COMPLETE — matrix passed; workflow returned `active=false`

## Contents

| File | Role |
|------|------|
| `POST-MODE-DISCOVERY.json` | Mode selection |
| `PRE-TEST-MANIFEST.json` | Pre-test live state |
| `TEST-CASE-MANIFEST.json` | T01–T28 matrix |
| `SANITIZED-CASE-RESULTS.json` | Observed HTTP results |
| `EXECUTION-CORRELATION.json` | Execution metadata |
| `RESPONSE-CONTRACT-OBSERVATIONS.json` | Intended vs observed |
| `STRUCTURAL-STATE-DIFF.json` | Pre/post structural compare |
| `CONTAINMENT-STATUS.md` | Deactivation evidence |
| `TEST-RESULTS.md` | Gate + matrix summary |
| `SECURITY-REVIEW.md` | Secret/URL leakage review |

## Explicitly absent

- Auth secret
- Full webhook URL / path
- Raw request bodies
- Raw execution payloads
- n8n API key
- Telegram tokens
