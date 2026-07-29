# DEV WORKFLOW MANIFEST v1

| Workflow | ID | Active | Nodes | Source |
|----------|----|--------|-------|--------|
| i-SEO Sales Manager - Operational.dev | xSnXPy8cEHoZw6xG | false | 29 | live Sales-Manager-v2 + Operational patch |
| i-SEO Sales Manager - Admin.dev | wLrLp4WQHm1VJmxz | false | 22 | MetaBOT v14 Admin pattern stripped to Sales Manager commands |

## Operational.dev highlights

- Schedule Trigger disabled
- Manual Synthetic Trigger present
- AI #2 removed; single OpenRouter node disabled; AI OFF branch skips OpenRouter
- Telegram send disabled; formatter present
- Gmail mutate nodes disabled
- Sheets writes targeted at v2 tabs; disabled until synthetic enablement
- Telegram fail → ERROR path / Preserve Incoming (no PROCESSED)

## Admin.dev highlights

- Telegram Trigger disabled (coexistence decision pending)
- Safe Telegram Reply disabled
- Commands: /help /status /ai_status /ai_on /ai_off /health /stats /test_lead /last_error /config
- Unknown: `Неизвестная команда. Используйте /help.`
- Authorization fail-closed when admin_user_ids empty
- No Gmail lead processing

## Count gate

Exactly two new workflows. No disposable clones retained. Accidental probe workflow deleted during API capability probe.
