# TELEGRAM SEND PAYLOAD v1

## Pre-fix (exec 40019)

| Stage | Keyboard |
|---|---|
| Renderer / Build Claims | present (`telegram_inline_keyboard_ui`) |
| Merge Reminder Send Payload | present |
| Send Reminder Telegram node parameter | `inlineKeyboard: ={{$json.telegram_inline_keyboard_ui}}` (whole-object expression) |
| Telegram API result | **no `reply_markup`** |

## Root mechanism (probed)

n8n Telegram `sendMessage` **silently drops** `inlineKeyboard` when the entire keyboard value is a single expression object.

Static `fixedCollection` + **per-field** expressions (`={{$json.rm_b1_text}}` / `rm_b1_cb`) **preserves** `reply_markup`.

## Post-fix

`Send Reminder Telegram`:

- `replyMarkup: inlineKeyboard` (static)
- `inlineKeyboard`: packed static rows with field expressions `rm_b1`…`rm_b8`

Callback replies:

- `Prepare Callback Answer` flattens UI → `rm_b*` + `rm_kb_band`
- `Switch Reply Keyboard Band` → `Safe Telegram Reply KB4|8|12|14` (field expressions)

## Acceptance send proof (ADMIN_A)

| Message | message_id | has_reply_markup | buttons_sent |
|---|---|---|---|
| Digest | 1090 | true | 8 (6 real + pads) |
| Group | 1091 | true | 8 |
| Lead | 1092 | true | 4 |
