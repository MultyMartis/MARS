# Project-Neutral Client Ops Template (OpenCart/ocStore + 1C)

## CORE

- run identity
- terminal state
- event classification
- dedupe
- dispatch
- delivery
- watchdog
- audit

## ADAPTERS

- OpenCart importer
- 1C / CommerceML
- n8n (or future service)
- Telegram (future: email/Slack/MAX)
- State backend: Data Table **or** PostgreSQL

## SITE CONFIG

- site ID (e.g. SITE-00N)
- domain
- schedules + timezone
- filename families (`import0_*`, `offers0_*`)
- bot destination
- event wording (locale)
- watchdog SLA
- kill switch location (non-Git)

Reproduce via `REPRODUCE-1C-CLIENT-OPS-FOR-NEW-SITE.md`.
