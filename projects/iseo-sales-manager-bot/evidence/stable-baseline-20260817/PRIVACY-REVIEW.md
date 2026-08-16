# Privacy / Secrets Review — Stable Baseline Freeze 2026-08-17

## Scope

Git-bound evidence under `projects/iseo-sales-manager-bot/evidence/stable-baseline-20260817/` and baseline docs under `projects/iseo-sales-manager-bot/baselines/`.

## Denied from commit

| Class | Status |
|-------|--------|
| Gmail credentials | Not committed |
| Telegram credentials / chat IDs | Not committed (hashes/redactions only) |
| n8n API secrets | Not committed (read from local tokens file only) |
| Google Sheets credentials / document IDs | Not committed in freeze evidence |
| Webhook secrets | Not committed |
| Full production Gmail bodies | Not committed |
| Phone / email / IP / lead PII | Not committed |
| Private acceptance payloads | Remain under STORAGE `private/` only |

## Allowed

- Workflow IDs and names (already public within project evidence)
- Code/content hashes
- CONFIG non-secret keys (`ai_enabled`, reminder schedule flags)
- Lead id reference `LEAD_4CC52CE3F311` without body

## Gate

`SM_STABLE_PRIVACY_PASS`
