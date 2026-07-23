# Client Ops n8n Syntax Matrix

**Status:** SKELETON — TO BE COMPLETED AFTER FIRST SANDBOX APPLY
**Authority:** MetaBOT live/reference exports + accepted sandbox `respondToWebhook@1.1` evidence

| Node | type | typeVersion | Notes |
|------|------|-------------|-------|
| Webhook | `n8n-nodes-base.webhook` | `2.1` | Prefer `responseMode=responseNode` |
| Code | `n8n-nodes-base.code` | `2` | `return [{ json: {...} }]` |
| IF | `n8n-nodes-base.if` | `2.3` | true=`main[0]`, false=`main[1]` |
| Switch | `n8n-nodes-base.switch` | `3` / `3.2` | Not used in first sandbox template |
| Set | `n8n-nodes-base.set` | `2` | Evidenced; first template prefers Code@2 |
| HTTP Request | `n8n-nodes-base.httpRequest` | `4` / `4.4` | Not in first sandbox |
| Telegram | `n8n-nodes-base.telegram` | `1` / `1.2` | Not in first sandbox |
| Respond to Webhook | `n8n-nodes-base.respondToWebhook` | `1.1` | Accepted sandbox evidence |

## Expressions

- `={{ ... }}`
- `$json`
- `$('Node Name').first().json`

## SAFE UNKNOWN

- Exact n8n application version.
- Secure Code-node access to env/credential secrets (binding remains HITL_REQUIRED).
- Data Store availability.
