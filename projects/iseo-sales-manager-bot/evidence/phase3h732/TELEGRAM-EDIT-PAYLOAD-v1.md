# TELEGRAM EDIT PAYLOAD

Node: Edit Lead Card Message / Edit Lead Card Message Pending
Operation: editMessageText (n8n Telegram typeVersion 1.2)

Resolved fields:
- chatId: `={{$json.edit_chat_id}}`
- messageId: `={{$json.edit_message_id}}`
- text: `={{$json.edit_text}}`
- replyMarkup: inlineKeyboard (reopen OR pending_actions)
- parse_mode: HTML

Pre-repair initiator payload used edit_message_id=MSG_883 (stale).
Post-repair must use MSG_898 when operator clicks MSG_898.
