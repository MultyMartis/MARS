# ADMIN POLISH CHANGESET v1

**Phase:** 3B.5  
**Workflow:** i-SEO Sales Manager - Admin.dev (`wLrLp4WQHm1VJmxz`)  
**Method:** code-node-only polish (no graph/credential changes)

## Nodes patched

- Status
- AI Status
- AI On
- AI Off
- Help
- Health
- Stats
- Last Error
- Config Summary
- Synthetic Test Lead

## Intent

| Area | Change |
|------|--------|
| Time display | UTC storage unchanged; Telegram render `DD.MM.YYYY HH:mm МСК` (Europe/Moscow) |
| Terminology | ИИ / процессы / рабочий контур / использован шаблон / провайдер ИИ |
| Status | Dev synthetic labels; no raw error codes; process on/off lines |
| Health | Russian process labels; AI probe not run |
| Stats | Dev: SYNTHETIC_TEST only + note; Prod filter ready |
| Last error | Test vs working title; controlled synthetic type |
| Config / Help | Masked Russian summary; `/test_lead` removed from help |
| test_lead | Deferred Russian response (no third workflow / unsafe Ops coupling) |

## Not changed

- Telegram Trigger enabled state and credential
- Connections / Route Command rules
- Authorization allowlist logic
- Operational.dev / Sales-Manager-v2
