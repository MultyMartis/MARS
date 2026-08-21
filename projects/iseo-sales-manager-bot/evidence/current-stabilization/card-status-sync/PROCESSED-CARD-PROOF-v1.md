# PROCESSED CARD PROOF — post-repair

## Shared path

Uses the same Expand → IF Pending Keyboard → Edit Lead Card Message chain as Spam.

## Exec `36657`

| Check | Result |
|-------|--------|
| action | processed |
| outcome | applied |
| prior → new | pending → processed |
| clicked == selected | YES |
| edit_ok | YES |
| card_sync_ok | 1 |
| edit_errors | none |
| edit_text has `✅ Обработан` | YES |
| edit_text has Pending | NO |
| edit_keyboard_mode | reopen |
| CLEAN updates | 1 |
| LEAD_EVENTS | 1 (`manager_marked_processed`) |
| reply | `Лид отмечен как обработанный.` |

## PASS

Processed updates the clicked current card on the shared repair.
