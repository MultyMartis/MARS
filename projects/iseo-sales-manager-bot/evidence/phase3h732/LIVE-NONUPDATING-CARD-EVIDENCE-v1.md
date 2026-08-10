# LIVE NON-UPDATING CARD EVIDENCE — Phase 3H.7.3.2

Alias: LIVE_CARD_PROOF_1 (lead suffix 6e4c68e4 / REAL_REOPEN_A)

## Operator observation
- Reopen ack: `Лид возвращён в обработку.` — visible card unchanged
- Spam ack: `Лид отмечен как спам.` — visible card unchanged

## Execution evidence
| Exec | Action | Semantic ack | Initiator callback msg | Expand edit msg | Same? | Telegram initiator result |
|---|---|---|---|---|---|---|
| 27668 | reopen | returned to processing | MSG_900 (other lead card in same chat) | MSG_891 | NO | edits on stale set |
| 27669 | spam | marked spam | MSG_898 | MSG_883 | NO | `message to edit not found` |

## Proven working layers
callback reception · authorization · lead lookup · LEADS mutation · LEAD_EVENTS · semantic ack

## Broken layer
current Telegram card mutation (wrong message_id selected)
