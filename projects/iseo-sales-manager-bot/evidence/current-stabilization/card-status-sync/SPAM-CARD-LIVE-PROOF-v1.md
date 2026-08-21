# SPAM CARD LIVE PROOF — post-repair

## Method

ADMIN_A-only callback inject into temporary Admin webhook → `Normalize Command` (same production path). Known operator test fixture reused. No moderator/customer messages.

## Exec `36654`

| Check | Result |
|-------|--------|
| action | spam |
| outcome | applied |
| prior → new | pending → spam |
| clicked == selected | YES |
| edit_ok | YES |
| card_sync_ok | 1 |
| edit_errors | none |
| edit_text has `🚫 Спам` | YES |
| edit_text has Pending | NO |
| edit_keyboard_mode | reopen |
| CLEAN updates | 1 |
| LEAD_EVENTS | 1 (`manager_marked_spam`) |
| reply | `Лид отмечен как спам.` |

## PASS criteria

Clicked current card visibly updated to terminal Spam representation; Pending label gone; status action keyboard replaced by canonical reopen keyboard path.
