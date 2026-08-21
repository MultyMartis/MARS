# TELEGRAM EDIT RESULT — exec 36629

## Attempt

| Field | Value |
|-------|-------|
| Node | `Edit Lead Card Message` |
| operation | `editMessageText` |
| edit_chat_id_h8 | `3fbe2132` matched clicked chat |
| edit_message_id_h8 | `216da54b` matched clicked message |
| edit_text | canonical terminal spam card (has `🚫 Спам`, no Pending label) |
| edit_text_len | 447 |
| edit_keyboard_mode | `reopen` |
| Handle-built `telegram_reply_markup` | valid 2-row keyboard (Reopen + Raw) |

## Provider result

```text
Bad Request: can't parse InlineKeyboardButton: Text buttons are unallowed in the inline keyboard
```

## Cause of provider rejection

Edit node static `inlineKeyboard` included a third button:

- text: `🟢 Полная карточка`
- callback_data: `={{$json.telegram_callback_full_card}}`

On Spam/Processed/Reopen status paths, `telegram_callback_full_card` is **not set** (only set on digest `queue_open` / `full_card`).  
Empty/missing callback_data → Telegram treats the control as a plain text button → rejects inline keyboard → **edit fails**.

## Not causes (ruled out)

| Candidate | Ruled out because |
|-----------|-------------------|
| wrong message_id | clicked == selected |
| wrong chat_id | matched ADMIN_A |
| malformed HTML body | edit_text rendered; rejection is keyboard parse |
| edit node not reached | node ran; error returned |
| early ack abort | Answer Callback Early `onError=continueRegularOutput`; mutation continued |
| swallowed error | Aggregate recorded `bad_request` + sync warning |

## Aggregate truth

`card_sync_ok=0`, warning present, while semantic ack still said spam — matches operator UX.
