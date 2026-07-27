# Zero-Request Invariant

**Token:** `D6C2_ZERO_REQUEST_INVARIANT_ARMED`

Established **before** activate:

- planned_requests=0
- allow_webhook_requests=false
- webhook transport invocation budget=0
- production transport `allowWebhookPost=false`
- orchestrator forces `sendRequest=false` for dry charter
- local reject: `WEBHOOK_REQUEST_PROHIBITED_BY_CHARTER`
