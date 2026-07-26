# HTTP 202 Evidence Provenance

## Load-bearing distinction

| Layer | Result |
|-------|--------|
| Producer stdout JSON parse | **FAILED** |
| Authoritative post-request GET-only evidence | HTTP **202** / `Respond Accepted` success / `intake_state=FIRST_SEEN` |

Do **not** claim that producer stdout itself cleanly parsed HTTP 202.

## Recovery basis (sanitized)

From D5R2A `HTTP-RESULT.json` / `HTTP-RECOVERY-GETONLY.json`:

1. n8n execution `3416` mode=`webhook` status=`success`
2. node `Respond Accepted` execution_status=`success`
3. Data Table row for event with `intake_state=FIRST_SEEN`
4. Established Client Ops pattern: Respond Accepted ⇒ intake HTTP 202

## Sources

- `evidence/phase-1b-d5r2a-temporary-activation-one-shot/HTTP-RESULT.json`
- `evidence/phase-1b-d5r2a-temporary-activation-one-shot/HTTP-RECOVERY-GETONLY.json`
- `evidence/phase-1b-d5r2a-temporary-activation-one-shot/LIVE-POST-CONSOLE-SANITIZED.json`
