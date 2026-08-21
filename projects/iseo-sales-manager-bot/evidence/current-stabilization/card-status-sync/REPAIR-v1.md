# REPAIR — conditional full_card button on Edit nodes

## Scope

Admin.dev only (`wLrLp4WQHm1VJmxz`).  
Nodes:

- `Edit Lead Card Message` (terminal / reopen keyboard)
- `Edit Lead Card Message Pending` (pending actions keyboard)

## Change

Replace static `inlineKeyboard` object (always included empty full_card row) with an expression that:

1. Always includes canonical status buttons (Reopen+Raw **or** Processed+Spam+Raw).
2. Appends `🟢 Полная карточка` **only if** `String($json.telegram_callback_full_card || '').trim()` is non-empty.

Digest path unchanged (still sets `telegram_callback_full_card`).  
Status path no longer sends an empty-callback button.

## What was not changed

- Handle Callback Action / Expand resolver / CLEAN writers / LEAD_EVENTS
- Canonical card renderer text
- Raw-source authorization
- Reminder / ACCESS / digest claim logic
- Operational.dev

## Apply evidence

| Item | Value |
|------|-------|
| PUT status | 200 |
| Admin remains active | true |
| Pre backup file sha16 | `FCA650F738960D19` |
| Post backup file sha16 | `238248E76B845C7E` |
| Post edit keyboard | expression with `telegram_callback_full_card` guard |

## Narrowness

No callback-system redesign. Shared Spam/Processed path fixed once.
