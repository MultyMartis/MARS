# FIRST DIVERGENCE v1

## Proven classes (two defects, same path)

### A — Missing action buttons

**Class:** `ACTION_KEYBOARD_NOT_ATTACHED`

**First divergence point:** `Edit Lead Card Message Pending` → Telegram API payload

- Upstream: Handle Callback Action produced correct `edit_text`, `telegram_callback_processed/spam/raw_source`, `edit_keyboard_mode: pending_actions`.
- Node ran successfully (`card_sync_ok: 1`, `edit_pending_ok: true`).
- **Divergence:** whole-object `inlineKeyboard` expression → outbound edit without `reply_markup`.

### B — Stray `Карточка` message

**Class:** `SEPARATE_TITLE_MESSAGE_BRANCH` (+ callback ack leaking to Send Message)

**First divergence point:** `Aggregate Card Sync Result` final `reply_text`

- Handle sets `answer_text: 'Карточка'` for semantic ack on `queue_open`.
- Card in-place edit succeeded (`skip_card_edits: false`, `card_sync_ok > 0`).
- Aggregate copied ack into **`reply_text`** (not suppressed for card-edit-success path).
- `DIGEST_GROUP_PRESERVE` only applies when `skip_card_edits: true` (group list), not exact lead.
- Prepare → Capture → IF Telegram Has Buttons (false) → **Safe Telegram Reply** emitted visible `Карточка`.

## Not the root cause

- `WRONG_RENDERER_BRANCH` — false; pending card text correct
- `ACTION_CALLBACK_FIELDS_EMPTY` — false on traced execs
- `QUEUE_OPEN_TEXT_ONLY` — false; edit attempted with actions mode
- `UNKNOWN` — rejected; both branches proven from execution 51238/51239
