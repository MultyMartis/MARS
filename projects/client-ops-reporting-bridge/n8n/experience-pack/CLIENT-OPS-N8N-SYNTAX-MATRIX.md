# Client Ops n8n Syntax Matrix

**Status:** PARTIAL — refreshed during Phase 1B-B
**Authority:** MetaBOT live/reference exports + Phase 1B-B create/re-GET evidence

| Node | type | typeVersion | Notes |
|------|------|-------------|-------|
| Webhook | `n8n-nodes-base.webhook` | `2.1` | Prefer `responseMode=responseNode`; live Admin webhook lacked `authentication` param |
| Code | `n8n-nodes-base.code` | `2` | `return [{ json: {...} }]` |
| IF | `n8n-nodes-base.if` | `2.3` | true=`main[0]`, false=`main[1]` |
| Switch | `n8n-nodes-base.switch` | `3` / `3.2` | Not used in first sandbox template |
| Set | `n8n-nodes-base.set` | `2` | Evidenced; first template prefers Code@2 |
| HTTP Request | `n8n-nodes-base.httpRequest` | `4` / `4.4` | Not in first sandbox |
| Telegram | `n8n-nodes-base.telegram` | `1` / `1.2` | Not in first sandbox |
| Respond to Webhook | `n8n-nodes-base.respondToWebhook` | `1.1` | Live sandbox-get evidence + Client Ops create |

## Expressions

- `={{ ... }}`
- `$json`
- `$('Node Name').first().json`

## Phase 1B-B create notes

- Inactive create omitted `webhookId`; server assigned one.
- Create payload schema accepted without top-level `active` (workflow remained inactive).
- Auth mode used: `AUTH_BLOCKED_INACTIVE_ONLY`.

## SAFE UNKNOWN

- Exact n8n application version.
- Secure Code-node access to env/credential secrets.
- Native webhook header-auth credential create payload shape on this instance.
- Data Store availability.
