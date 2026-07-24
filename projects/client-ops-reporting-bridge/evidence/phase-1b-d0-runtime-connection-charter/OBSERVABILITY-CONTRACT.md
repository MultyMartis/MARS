# Observability Contract — Phase 1B-D0

**Status:** CONTRACT (future runtime runs)

## Mandatory fields (per runtime attempt)

| Field | Required |
|-------|----------|
| producer_run_id | Yes |
| event_id | Yes |
| source_timestamp / observed_at | Yes |
| site_id | Yes (`SITE-002`) |
| normalized_status | Yes |
| http_response_status | Yes (if POST attempted) |
| n8n_execution_id | Yes when observable |
| telegram_delivery_status | Yes when accept path |
| telegram_message_id | When available |
| dedupe_result | Yes |
| retry_count | Yes |
| failure_category | Yes if failed |
| elapsed_ms | Yes |
| final_state | Yes |
| redaction_status | Yes (`redacted=true`) |

## Retention locations

| Location | What | Git? |
|----------|------|------|
| Ignored local runtime evidence | Full sanitized producer traces | No |
| Committed milestone evidence | Pack summaries / manifests | Yes (sanitized) |
| n8n execution metadata | Platform executions | Platform only; do not dump raw payloads to Git |
| Client-facing Telegram | SIMPLE message only | N/A |
| Optional dashboard | Deferred | — |

## Redaction rules

- No secrets, tokens, full webhook URLs, raw production logs, absolute unnecessary Storage paths, stack traces, private keys.
- Credential IDs/names and workflow IDs allowed.

## Client visibility

Internal operator Telegram only for MVP. No client routing without separate Phase 3 charter.
