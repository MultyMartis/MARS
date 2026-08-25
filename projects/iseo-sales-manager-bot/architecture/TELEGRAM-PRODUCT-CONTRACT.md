# Telegram Product Contract

**Audience:** authorized managers and operators  
**Authority:** [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)

## Manager Card

Telegram is the primary product surface for managers. Each production card should be concise, scannable, and based on CLEAN normalized data.

The card may show operational fields such as contact/request/site summary when available, but it must not expose secrets, internal stack traces, raw AI JSON, or unnecessary technical identifiers.

## Production Actions

Buttons:

- `✅ Обработано`
- `🚫 Спам`
- `📄 Исходная заявка`

Russian labels are part of the UX contract.

## Action Semantics

| Button | Semantics |
|--------|-----------|
| `✅ Обработано` | Lifecycle action: lead handled |
| `🚫 Спам` | Lifecycle action: lead rejected as spam |
| `📄 Исходная заявка` | Read-only source display |

## Raw-Source Message

`📄 Исходная заявка` returns the original visible source as literally as production allows:

- original wording and order;
- original line/paragraph structure where preserved;
- minimal privacy and Telegram-safe cleanup;
- no field reconstruction;
- no CLEAN substitution;
- IP omitted.

## Authorized Manager Boundary

Callbacks and admin commands must be limited to authorized Telegram users as configured by production CONFIG/n8n. Unauthorized users should receive a short denial and no sensitive detail.

## Product Non-Goals

- No CRM pipeline in Telegram.
- No AI-generated manager advice in the stable baseline.
- No automatic task list mutation from raw clicks or reminders.
- No public/debug data in manager-facing messages.

## Failure Handling

If a card action cannot be resolved safely, prefer a clear operator-safe error over guessing. Do not infer a lead from broad sheet scans when a `lead_id`-scoped lookup is required.

