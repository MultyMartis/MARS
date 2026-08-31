# NATURAL LIVE DEFECT v1

Date: 2026-08-31 (Europe/Moscow morning window)  
Workflow: Admin.dev `wLrLp4WQHm1VJmxz`  
Path: scheduled reminder → group (`sm:g:*`) → exact lead (`sm:q:*`)

## Operator-visible defect (production, not soak)

1. Lead card **text correct** after selecting exact lead from natural reminder navigation.
2. **No inline action buttons** on the edited card:
   - missing `✅ Обработано`
   - missing `🚫 Спам`
   - missing `📄 Исходная заявка`
3. Separate chat message **`Карточка`** appeared after the card.

## Anchor executions (today)

| Exec | Callback | Action | Outcome | Card edit | Stray reply |
|---|---|---|---|---|---|
| 51238 | `sm:q:c422c6ec15b5` | `queue_open` | `queue_opened` | ok (pending edit ran) | `reply_text: Карточка` |
| 51239 | `sm:q:3183ec40e360` | `queue_open` | `queue_opened` | ok (pending edit ran) | `reply_text: Карточка` |

Supporting group navigation (working list, no card edit):

| Exec | Callback | Outcome | Notes |
|---|---|---|---|
| 51233 | `sm:g:c:ade3cbdc59` | `group_opened` | digest list preserved; `skip_card_edits: true` |
| 51237 | `sm:g:c:e130bfb8c3` | `group_opened` | same pattern |

## Status

Pre-fix production defect confirmed from live natural traffic. Prior harness PASS claims do not override this evidence.
