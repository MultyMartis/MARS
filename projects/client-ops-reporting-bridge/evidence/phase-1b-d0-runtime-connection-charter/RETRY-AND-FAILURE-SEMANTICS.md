# Retry and Failure Semantics — Phase 1B-D0

**Status:** REQUIREMENTS (not enabled)
**Automatic retries in this phase:** **FORBIDDEN / not enabled**

## Producer / network

| Failure class | Producer action | Event ID behavior | Retry | Operator evidence |
|---------------|-----------------|-------------------|-------|-------------------|
| Connection timeout | Fail run; no assume accept | Retain same for later manual retry | Manual / future bounded | run_id, event_id, failure=`CONNECT_TIMEOUT` |
| Read timeout (ambiguous after possible accept) | **Do not** auto-repost without dedupe consultation | Same | Manual only until dedupe proves duplicate-safe | Mark `AMBIGUOUS_TIMEOUT`; check n8n executions |
| DNS/TLS failure | Fail closed | Same | Manual | failure=`TLS_OR_DNS` |
| HTTP 401/403 | Fail closed; do not retry blindly | Same | After secret fix | HTTP status only |
| HTTP 4xx validation/security | Fix envelope; new attempt may keep or change id per identity rules | Same if facts unchanged | No auto | response code + sanitized body class |
| HTTP 5xx | Hold | Same | Future bounded backoff | HTTP 5xx class |
| HTTP 202 | Treat intake accepted; delivery async (Pattern B) | Same | N/A for POST success | status 202 + execution id if known |
| Workflow inactive | Fail; no delivery expected | Same | After HITL activate | failure=`WORKFLOW_INACTIVE` |

**PROPOSED future bounds (not enabled):** max 5 attempts; backoff 1m→5m→15m→60m→6h; hard stop; dead-letter.

## n8n

| Failure class | Producer action | Event ID behavior | Retry | Operator evidence |
|---------------|-----------------|-------------------|-------|-------------------|
| Validation rejection | Do not send Telegram (already) | Same if unchanged | After exporter fix | INVALID_SCHEMA etc. |
| Security rejection | Stop | Same | After sanitization fix | SECURITY_REJECTED |
| Internal node failure | Treat as infra | Same | Manual | execution status failed |
| Credential missing | Stop | Same | After credential repair | sanitized credential id only |
| Workflow inactive | Stop | Same | HITL activate | active=false |
| Crash after 202 | Delivery uncertain | Same | Manual + dedupe inspect | execution incomplete |

## Telegram

| Failure class | Producer action | Event ID behavior | Retry | Operator evidence |
|---------------|-----------------|-------------------|-------|-------------------|
| Credential failure | n8n delivery FAILED | Same | Manual / future n8n bounded | Telegram node error class |
| API timeout | Delivery uncertain | Same | Manual until policy | timeout class |
| API reject | FAILED_RETRYABLE or TERMINAL per code | Same | Manual | sanitized API error |
| Success | Record SENT + message id if available | Same | No | message_id, execution_id |

### Telegram vs webhook response

- Telegram failure **does not** alter already-returned webhook response (Pattern B).
- Duplicates prevented by durable dedupe `SENT` state.
- Failed notifications retained in dedupe store for replay — **PROPOSED**.
- Operator sees: n8n execution + sanitized producer evidence + Telegram chat message only when SENT.

## Explicit D0 prohibition

Do **not** enable automatic producer or n8n retries under this charter.
