# STATUS CALLBACK CONTRACT v1

Read-only static proof — no status clicks executed in this task.

## Required pending actions (unchanged contracts)

| Button | Callback pattern | Handler |
|---|---|---|
| ✅ Обработано | `sm:p:<stable_token>` | existing processed transition in Handle / downstream status apply |
| 🚫 Спам | `sm:s:<stable_token>` | existing spam transition |
| 📄 Исходная заявка | `sm:i:<stable_token>` | existing raw-source inspect path |

## Post-fix binding

Edit node binds **expressions** to fields already populated by Handle Callback Action on `queue_open`:

- `telegram_callback_processed`
- `telegram_callback_spam`
- `telegram_callback_raw_source`

Same field names used by working reply-with-buttons cards and prior canonical-card unification.

## Terminal leads

When current authoritative status is processed/spam/terminal, Handle selects non-`pending_actions` edit mode — pending action trio not exposed. Unchanged by this patch.

## Proof method

Execution 51239 pre-fix showed non-empty callback fields matching contract. Patch only fixes Telegram binding + stray reply; does not rebuild status logic.
