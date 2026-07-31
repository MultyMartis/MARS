# ADMIN-START-REAL-TRIGGER-ACCEPTANCE v1

**Phase:** 3D.2  
**Date:** 2026-08-01

## Live harness (Normalize → route → reply)

| Case | Result |
|------|--------|
| Authorized `/start` | PASS — production / AI OFF wording |
| `/start@bot_username` | PASS — normalized to `/start` |
| Unauthorized `/start` (synthetic id) | PASS — `Доступ запрещён.` |
| `/help` | PASS — lists `/start`; no `/test_lead` |
| `/config` | PASS — `Версия парсера: sm-parser-v3.1` |
| `/ai_status` | PASS — выключен |
| `/status` | PASS — рабочий контур; AI OFF |

Harness delivered replies to the operator-private chat via Safe Telegram Reply. Allowlist size remained 1.

## Telegram Trigger registration

- Trigger enabled, webhook present, updates=`message`
- Admin remained active after patch/restore cycles

## Operator-typed Trigger matrix

| Command | Typed Trigger execution |
|---------|-------------------------|
| `/start` | PENDING |
| `/help` | PENDING |
| `/status` | PENDING |
| `/config` | PENDING |
| `/ai_status` | PENDING |

Operator readiness notice was sent to the private Admin chat. No typed Trigger executions arrived during the bounded poll window (~4 min).

## Security

No user/chat IDs, tokens, or secrets recorded.
