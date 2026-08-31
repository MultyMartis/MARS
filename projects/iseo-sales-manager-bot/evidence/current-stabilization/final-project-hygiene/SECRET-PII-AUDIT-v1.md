# SECRET / PII AUDIT v1 — staging candidates

## Scope

Exact files planned for staging in final hygiene closeout:

1. `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-storage-hygiene-loss-assessment-v1.md`
2. `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-targeted-storage-loss-forensics-v1.md`
3. `governance/audits/ISEO-SALES-MANAGER-BOT-storage-hygiene-loss-assessment-2026-08-31.md`
4. `governance/audits/ISEO-SALES-MANAGER-BOT-targeted-storage-loss-forensics-2026-08-31.md`
5. `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-final-project-hygiene-stable-git-v1.md`
6. `projects/iseo-sales-manager-bot/evidence/current-stabilization/final-project-hygiene/**`

## Scan method

Case-insensitive pattern search for API keys, Bearer tokens, Telegram bot tokens, OAuth secrets, emails, RU phone patterns, raw lead payloads. Path mentions of `n8n-api.env` without values allowed.

## Results

| File family | Secrets | Client PII | Notes |
|---|---|---|---|
| Storage-loss project reports | **0** | **0** | Mentions credential *path existence* only; values not read/copied |
| Governance audits | **0** | **0** | Same; token validity = SAFE UNKNOWN |
| Hygiene evidence/report | **0** | **0** | Workflow IDs only (public operational identifiers); no tokens |

## Staging contract

| Counter | Value |
|---|---:|
| secrets staged | **0** |
| client PII staged | **0** |

Raw workflow PRE/POST JSON and `n8n-api.env` remain STORAGE-only — **not staged**.
