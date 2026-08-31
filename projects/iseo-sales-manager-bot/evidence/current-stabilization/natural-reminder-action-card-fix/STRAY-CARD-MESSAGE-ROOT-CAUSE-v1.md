# STRAY CARD MESSAGE ROOT CAUSE v1

## Visible message

Standalone Telegram chat text: **`Карточка`**

## Source node chain

1. **Handle Callback Action** — sets `answer_text: 'Карточка'` for `queue_open` / `queue_opened` (semantic toast title; not intended as chat body when card edit succeeds).
2. **Aggregate Card Sync Result** — `resolveSemanticAck()` falls through to `h.answer_text`; assigns `reply_text: answer` → `'Карточка'`.
3. **Prepare Callback Answer** — digest view branch collapses to `reply_text` (non-empty).
4. **Capture Admin Reply** — forwards item downstream.
5. **IF Telegram Has Buttons** — false on exact-lead edit path (no reply keyboard on new message).
6. **Safe Telegram Reply** — sends `reply_text` as visible message.

## Classification

- Not `answerCallbackQuery` leak (late answer already skipped elsewhere).
- **Secondary Send Message** after successful in-place card edit.
- Navigation title / ack text incorrectly reused as chat payload.

## Repair principle

Preserve ack semantics in `answer_text`; **suppress visible `reply_text`** when in-place card edit succeeds (`queue_opened` / `full_card_viewed`, `card_sync_ok > 0`, zero failures). Do not replace with another placeholder string.
