# CARD STATUS SYNC REGRESSION PROOF

Prior fix (commit `9a69ef08` / cherry-pick `5b8ca157`): include `🟢 Полная карточка` only when `telegram_callback_full_card` non-empty.

This wave:

- group/lead callbacks always emit non-empty `callback_data`
- Edit keyboard expressions unchanged (conditional full_card)
- harness empty_callback_buttons = **0**
