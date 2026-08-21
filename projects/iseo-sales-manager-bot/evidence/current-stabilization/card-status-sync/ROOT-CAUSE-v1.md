# ROOT CAUSE — current card status sync regression

## Exact cause

**Empty third inline button on Telegram edit nodes.**

`Edit Lead Card Message` and `Edit Lead Card Message Pending` always sent a `🟢 Полная карточка` button bound to `$json.telegram_callback_full_card`.

That field is populated only on digest actions (`queue_open` / `full_card`).  
Status transitions (`spam` / `processed` / `reopen`) build canonical keyboards via Handle Callback Action **without** `telegram_callback_full_card`.

Result:

1. CLEAN + LEAD_EVENTS commit successfully.
2. Expand selects the clicked message correctly (`callback_initiator`).
3. `editMessageText` fails Telegram keyboard validation.
4. Operator still sees Pending UI + old action buttons.
5. Ack text still claims success (`Лид отмечен как спам.`).

## Not the root cause

- Stale card-instance / wrong `message_id` selection (3H.7.3.2 class) — disproved for exec `36629`.
- Missing status write.
- Duplicate lead identity.
- Early callback ack terminating the mutate path.

## Class

Production UX/state-sync defect on shared Spam/Processed edit path (same Edit nodes / same empty full_card button).
