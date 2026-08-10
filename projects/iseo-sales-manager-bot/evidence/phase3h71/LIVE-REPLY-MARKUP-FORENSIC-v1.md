# LIVE REPLY MARKUP FORENSIC — Phase 3H.7.1

## Pre-patch
- `Edit Lead Card Message.inlineKeyboard.rows = []`
- Handle Callback terminal apply did not set `telegram_callback_reopen` / `edit_keyboard_mode='reopen'`
- `buildReopenButtons` defined but unused on terminal mutation path

## Post-patch
- Edit Lead Card Message contains button `↩️ Вернуть в обработку` bound to `={{$json.telegram_callback_reopen}}`
- Handle Callback sets `edit_keyboard_mode:'reopen'` + `buildReopenButtons(token)` on applied/idempotent/conflict terminal paths
- Live Telegram send+edit harness: spam/processed cards show reopen button (pass=true)
