# CANONICAL-CARD-CONTRACT-v1

## Semantic entry

All routes resolve **current authoritative logical lead** (CLEAN/DEDUP by token/lead_id), then:

`renderCanonicalLeadCard(lead, context)` → text + keyboard from **lifecycle status**, not entry point.

## ACTIVE / PENDING

- Header: working card (`📋 Лид` in list; full card on open)
- Actions required: `✅ Обработано` (`sm:p:`), `🚫 Спам` (`sm:s:`), `📄 Исходная заявка` (`sm:i:`)
- `answer_text` on queue_open: **Карточка** (never standalone `Лид`)
- `edit_keyboard_mode`: `pending_actions`

## TERMINAL

- No pending action triad; terminal/archive presentation per existing contract.

## Context

May add navigation (group, list position). Must not change lifecycle truth.
