# MINIMUM PRODUCTION-SAFE MODEL — Before “UNATTENDED CLIENT OPS DELIVERY READY”

`D6_MINIMUM_PRODUCTION_SAFE_MODEL_DEFINED`

This is the **minimum** architecture that must exist before the phrase
`UNATTENDED CLIENT OPS DELIVERY READY`
may be used honestly. **We are not there now.**

## Mandatory capabilities

| Capability | Minimum bar |
|------------|-------------|
| Source authority | Explicit completed SITE-002 run artifacts only; authority JSON match; dedicated runtime pin clean |
| Freshness | Separate `source_status` vs `delivery_eligibility`; stale ≠ BLOCKED |
| Deterministic identity | Stable event_id for same source run; double-build proof |
| Durable dedupe | FIRST_SEEN claim before Telegram (already proven) |
| Terminal delivery state | SENT / FAILED persisted after Telegram; PENDING not acceptable as long-term success |
| Retry reconciliation | GET-only DT + execution reconcile before any same-event retry; ambiguous timeout never auto-POSTs |
| Activation lifecycle | Documented C3 (or stronger C4) with always-deactivate + emergency path; default inactive otherwise |
| Runtime cleanliness | HEAD exact pin; porcelain EMPTY; no MAIN WIP coupling |
| Scheduler overlap | Single-flight / lease; no overlapping monitor+producer races |
| Containment | Kill-switch deactivate; generic live producer remains gated |
| Security | Header auth; secrets local-ignored; no raw logs in payloads; least privilege API keys |
| Audit evidence | Sanitized run evidence for each unattended attempt (HTTP class, exec id, delivery_state, message_id) |

## Explicit non-claims

- `CLIENT_OPS_UNATTENDED_PRODUCTION_READY=NO`
- `CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO`
- First verified manual delivery ≠ unattended readiness
