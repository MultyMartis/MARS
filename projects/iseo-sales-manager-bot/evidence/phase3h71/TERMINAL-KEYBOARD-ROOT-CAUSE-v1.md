# TERMINAL KEYBOARD ROOT CAUSE — Phase 3H.7.1

## Root cause (proven)
1. `IF Pending Action Keyboard` true → `Edit Lead Card Message Pending` (processed/spam actions).
2. false → `Edit Lead Card Message` with **empty** inline keyboard rows.
3. Terminal spam/processed apply inherited `remove_keyboard:true` from `outBase` and never set `edit_keyboard_mode:'reopen'` nor `buildReopenButtons`.
4. Therefore Telegram edited the card text to terminal state and cleared the keyboard.

Archive `/leads` already had reopen from Phase 3H.7 (`Recent Leads` + `Safe Telegram Reply`).
