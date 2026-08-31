# NATURAL CALLBACK TRACE v1

## End-to-end chain (exact lead from reminder)

```
Telegram Trigger (callback_query)
  → Normalize Command
  → Handle Callback Action          # queue_open / queue_opened; builds edit_text + callback fields
  → IF Skip Card Edits              # false for sm:q:*
  → Expand Card Sync Items
  → Edit Lead Card Message Pending  # in-place edit of reminder message
  → Aggregate Card Sync Result      # sets reply_text (pre-fix: "Карточка")
  → Prepare Callback Answer
  → Capture Admin Reply
  → IF Telegram Has Buttons         # false (no reply keyboard on this branch)
  → Safe Telegram Reply             # pre-fix: visible "Карточка"
```

## Exec 51239 trace (primary anchor)

| Stage | Field | Value |
|---|---|---|
| Execution ID | | `51239` |
| Started | | `2026-08-31T07:02:28.560Z` |
| callback_data | | `sm:q:3183ec40e360` |
| callback_action | | `queue_open` |
| callback_outcome | | `queue_opened` |
| edit_keyboard_mode | | `pending_actions` |
| telegram_edit | | `true` |
| skip_card_edits | | `false` |
| telegram_callback_processed | | `sm:p:3183ec40e360` |
| telegram_callback_spam | | `sm:s:3183ec40e360` |
| telegram_callback_raw_source | | `sm:i:3183ec40e360` |
| Edit Lead Card Message Pending | ran | `true`, `ok: true` |
| card_sync_ok | | `1` |
| aggregate reply_text | pre-fix | `Карточка` |
| prepare reply_text | pre-fix | `Карточка` |

## Exec 51238

Same pattern for `sm:q:c422c6ec15b5` — confirms reproducible defect class, not single-lead anomaly.

## Renderer / resolver

- Handle Callback Action resolves **current authoritative logical lead** from `sm:q:*` token.
- `buildFinalCard` / pending renderer produces correct card text (`hca_edit_text_len` 357–540).
- Callback action fields populated (non-empty `sm:p/s/i`).

No wrong-lead resolution observed on traced executions.
