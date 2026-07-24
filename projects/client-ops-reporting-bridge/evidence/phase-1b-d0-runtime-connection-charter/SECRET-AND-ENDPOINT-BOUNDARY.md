# Secret and Endpoint Boundary — Phase 1B-D0

**Status:** CONTRACT (no secret values written)
**Mode:** documentation only

## Existing local secret file (CURRENT)

| Item | Value |
|------|-------|
| Path | `local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env` |
| Exists | **Yes** (presence verified; values not printed) |
| Known key | `CLIENT_OPS_WEBHOOK_AUTH_SECRET` |
| Suitability | **Suitable** as the webhook Header Auth secret store for producer |

Telegram bot token remains in its own ignored local boundary (prior phases); not re-documented with values here.

## Future producer keys (PROPOSED names only)

### Secrets (ignored local only)

| Key | Purpose |
|-----|---------|
| `CLIENT_OPS_WEBHOOK_AUTH_SECRET` | Header Auth token (existing) |
| `CLIENT_OPS_TELEGRAM_BOT_TOKEN` | Only if a producer ever needs Bot API directly (**not** required for R1; n8n owns Telegram) |

### Non-secret endpoint / mode config (ignored local profile preferred)

| Key | Purpose |
|-----|---------|
| `CLIENT_OPS_WEBHOOK_BASE_URL` | Host base only — **never commit full URL with path if treated as sensitive ops surface**; prefer ignored profile |
| `CLIENT_OPS_WEBHOOK_PATH` | Webhook path segment — ignored local |
| `CLIENT_OPS_SITE_ID` | `SITE-002` |
| `CLIENT_OPS_SCHEMA_NAME` | `mars.client_ops.report` |
| `CLIENT_OPS_SCHEMA_VERSION` | `1.0` |
| `CLIENT_OPS_ENV_MODE` | `sandbox` \| `staging` \| `production` (production forbidden until gates) |
| `CLIENT_OPS_HTTP_TIMEOUT_MS` | Connect/read timeout |
| `CLIENT_OPS_RETRY_MAX` | Max retries |
| `CLIENT_OPS_RETRY_BACKOFF_MS` | Base backoff |

## Committed vs ignored

| Kind | Location | Rule |
|------|----------|------|
| Secrets | `local/.../secrets.local.env` (gitignored) | Never commit; never print |
| Endpoint route | Ignored local profile (e.g. `endpoint.local.env`) | Do **not** commit complete webhook URL |
| Site identity / schema constants | May live in committed site profile **without** route/secret | OK |
| Environment mode default | Committed docs say sandbox until activation | OK |

## Rotation (REQUIRED BEFORE PRODUCTION)

1. Generate new Header Auth secret offline.
2. Update n8n `httpHeaderAuth` credential under dedicated charter.
3. Update local ignored secret file.
4. Invalidate old secret.
5. Record sanitized rotation evidence (timestamps, credential id, no values).

## Redaction

Documents may mention: credential IDs/names, workflow IDs, header name `X-MARS-Client-Ops-Token`, key names.
Documents must not contain: secret values, full webhook URLs, Telegram tokens, n8n API keys, raw production logs.
