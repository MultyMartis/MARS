# Project-Neutral Template

Use this template to start a new manager-assistant bot without copying client-specific data.

## CORE

- Runtime authority: one host, named workflows/services.
- Source authority: immutable full intake source.
- Operational model: normalized lead/task record.
- Lifecycle: minimal statuses with explicit button effects.
- Events/errors: append-only observability.
- Dedupe: source and delivery guards.
- Security: credentials by reference only.
- Acceptance: safe fixtures and evidence.

## ADAPTERS

| Adapter | Required contract |
|---------|-------------------|
| Intake | Full source capture before parse |
| Parser | Deterministic normalization with version marker |
| Persistence | PostgreSQL preferred; source and lead tables separated |
| Telegram | Card, actions, authorization, raw source |
| Reminder | Candidate query, schedule, no lifecycle mutation |
| Admin | Commands, callbacks, config, safe denial |
| Export | Optional Sheets/report layer |

## CLIENT CONFIG

Define per client:

- manager language and labels;
- authorized operators;
- delivery recipients;
- intake source and filters;
- reminder timezone and schedule;
- excluded test/archive rules;
- branding and message tone;
- escalation contacts;
- evidence retention.

## Forbidden Defaults

- No AI unless chartered.
- No Sheets-as-primary for new builds unless explicitly chosen.
- No raw PII in docs.
- No automatic CRM scope.
- No hidden workflow copies.

