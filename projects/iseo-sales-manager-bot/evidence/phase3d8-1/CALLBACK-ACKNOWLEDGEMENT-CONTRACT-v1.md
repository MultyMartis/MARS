# CALLBACK ACKNOWLEDGEMENT CONTRACT v1

## Required sequence

1. Receive `callback_query`
2. Validate basic `sm:p:` / `sm:s:` structure
3. **answerCallbackQuery immediately**
4. Continue authorization + mutation
5. Durable feedback via card edit and/or Safe Telegram Reply

## Texts

| Case | Early toast |
|------|-------------|
| Valid pending action | `Обрабатываю…` |
| Malformed callback | `Не удалось распознать действие.` |
| Denied | `Недостаточно прав для изменения статуса.` |

## Live repair (Admin.dev)

- Added `Prepare Early Callback Ack` + `Answer Callback Early` on Route callback branch
- Late `Answer Callback Query` bypassed on success path (query already answered)
- `Answer Callback Deny` text aligned
- `onError=continueRegularOutput` on early answer

Final durable texts remain on Safe Telegram Reply / card body.
