# RISK-AND-UNKNOWN-REGISTER-v14

**Evidence classification:** LIVE_API_EXPORT

## Known unknowns

- Exact Intake → Worker invocation mechanism — **SAFE UNKNOWN**
- Whether Admin is always reached via Intake — **SAFE UNKNOWN**
- Live Worker version parity with v14 naming — verify in n8n UI
- Webhook production URLs — redacted; live paths require operator verification
- Google Sheets table/column truth — **SAFE UNKNOWN** from export alone

## Security risks

- No commit-blocking pattern labels flagged in sanitizer stats.

## Residual review labels (REVIEW_LABEL_ONLY)

### SEO Content Agent Beta.v14 - Intake

- Google Sheets URL (redacted)
- Google Sheets URL host
- webhookId reference
- chat_id reference
- user_id reference

### SEO Content Agent Beta.v14 - Worker

- Google Sheets URL (redacted)
- Google Sheets URL host
- webhookId reference
- chat_id reference
- user_id reference
- Authorization reference

### SEO Content Agent Beta.v14 - Admin

- Google Sheets URL (redacted)
- Google Sheets URL host
- webhookId reference
- chat_id reference
- user_id reference

## Operator gates

1. Review sanitized JSON manually before commit.
2. Confirm `SANITIZATION-REPORT.md` safe-to-commit status.
3. Never commit raw exports from `raw/` folder.
4. Live workflow changes require separate operator charter.
