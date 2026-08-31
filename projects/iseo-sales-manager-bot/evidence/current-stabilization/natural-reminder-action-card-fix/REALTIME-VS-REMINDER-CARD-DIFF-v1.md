# REALTIME VS REMINDER CARD DIFF v1

## Comparison table

| Field | Group list path (51233/51237) | Natural exact lead (51238/51239 pre-fix) |
|---|---|---|
| Current lead resolver | group digest (many leads) | single lead from `sm:q:*` |
| Renderer | pending digest list | `buildFinalCard` pending card |
| Text payload | group header + lead buttons | full pending lead card text |
| Processed callback | n/a (list row uses `sm:q:*`) | `sm:p:<token>` populated |
| Spam callback | n/a | `sm:s:<token>` populated |
| Original request callback | n/a | `sm:i:<token>` populated |
| Full-card callback | optional | optional field present |
| Keyboard builder | Prepare flatten + Safe Reply KB bands | Edit Lead Card Message Pending |
| Telegram node | Safe Telegram Reply KB* (new message) | editMessageText (in-place) |
| skip_card_edits | `true` | `false` |
| Visible stray reply | none (digest preserved) | **`Карточка`** |

## Why realtime-looking paths had actions

Group-open and reply-with-buttons paths bind keyboards as **static fixedCollection + field expressions** (post reminder-inline-nav repair). Field flatten produces `rm_bN_*` slots consumed by Safe Telegram Reply KB bands.

## Why reminder exact-lead lacked actions

`Edit Lead Card Message Pending` still used a **whole-object IIFE expression** for `inlineKeyboard`. n8n silently omitted `reply_markup` while returning `ok: true` — same failure mode documented in `reminder-inline-navigation/ROOT-CAUSE-v1.md`.

Handle/resolver side matched working contracts; divergence is **Telegram node keyboard binding**, not a separate renderer.
