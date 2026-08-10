# LIVE SPAM CARD FORENSIC — Phase 3H.7.1

## Aliases
- LIVE_SPAM_LEAD_A
- LIVE_SPAM_LEAD_B

## Observed operator symptom
After Spam: terminal body + actor/timestamp + reply `Лид отмечен как спам.` but **no** `↩️ Вернуть в обработку`.

## Live Admin executions (pre-patch)
- exec 27436 action=spam outcome=idempotent edit_keyboard_mode=null remove_keyboard=true reopen_markup=false edit_terminal_node=true
- exec 27435 action=spam outcome=applied edit_keyboard_mode=null remove_keyboard=true reopen_markup=false edit_terminal_node=true
- exec 27433 action=spam outcome=applied edit_keyboard_mode=null remove_keyboard=true reopen_markup=false edit_terminal_node=true

Proven: terminal apply routed to **Edit Lead Card Message** with empty keyboard while `remove_keyboard=true`.
