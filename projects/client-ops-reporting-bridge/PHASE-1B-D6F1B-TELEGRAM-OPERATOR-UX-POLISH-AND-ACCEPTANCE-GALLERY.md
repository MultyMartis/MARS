# Phase 1B-D6F1B — Telegram Operator UX Polish and Acceptance Gallery

**Status:** COMPLETE (operator UX polish + 4/4 acceptance + canonical integration)  
**Date:** 2026-08-06  
**Site:** SITE-002 / bzpm.ru

## Operator decision

Approved Russian compact operator messages, SITE-002 local time UTC+07 (`DD.MM.YYYY, HH:mm`), factual filenames, no synthetic counters, four-scenario acceptance gallery only, normal automation remains enabled.

## Message formatting owner

| Layer | Role |
|-------|------|
| `client-ops-telegram-operator-message.mjs` / `telegram_operator_message.py` | **Authoritative** visible Russian operator message contract |
| Producer `action.text` | Carries full operator/test body when formatter applied |
| n8n Telegram node expression | Pass-through for `🧪/✅/⚠️/❌` bodies; compact Russian fallback otherwise; `parse_mode=HTML` |

## Success gates

See evidence/`D6F1B-DECISION.json`.

## Next

Phase 1B-D6F1C — Next Natural SITE-002 Report Factual Acceptance (not started).
