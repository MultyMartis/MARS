# PATCH DESIGN v1

Scope: **Admin.dev only** (`wLrLp4WQHm1VJmxz`). Operational.dev untouched.

## Patch 1 — Action keyboard on in-place edit

**Node:** `Edit Lead Card Message Pending`

Replace whole-object `inlineKeyboard` IIFE with static fixedCollection rows:

| Button | callback expression |
|---|---|
| ✅ Обработано | `={{$json.telegram_callback_processed}}` |
| 🚫 Спам | `={{$json.telegram_callback_spam}}` |
| 📄 Исходная заявка | `={{$json.telegram_callback_raw_source}}` |

Optional full-card row omitted in minimal fix (not in required UX trio).

## Patch 2 — Suppress stray visible reply after successful card edit

**Nodes:** `Aggregate Card Sync Result`, `Prepare Callback Answer`, `Capture Admin Reply`

Contract: `iseo-card-edit-suppress-reply-v1.0`

When `queue_opened` / `full_card_viewed` (or actions `queue_open` / `full_card`) AND `card_sync_ok > 0` AND `failed === 0`:

- `reply_text: ''`
- `suppress_visible_reply: true`
- keep `answer_text: 'Карточка'` for semantic ack only

Prepare honors `suppress_visible_reply`. Capture skips empty suppressed items (no Safe Telegram Reply).

## Explicitly NOT changed

- Handle Callback Action
- Reminder schedule / delivery / dedupe
- CLEAN / DEDUP appendOrUpdate
- Group selector / KB1–KB8 / `Все`
- Operational.dev
- ACCESS / MOD_B Olya
- Status transition business logic

## Source patches (repo)

- `implementation/patches/AggregateCardSyncResult.natural-reminder-action-card-fix.js`
- `implementation/patches/PrepareCallbackAnswer.natural-reminder-action-card-fix.js`
- `implementation/patches/CaptureAdminReply.natural-reminder-action-card-fix.js`

Deploy: `natural-reminder-action-card-fix-20260831-local/run-deploy-natural-reminder-action-card-fix.mjs`
