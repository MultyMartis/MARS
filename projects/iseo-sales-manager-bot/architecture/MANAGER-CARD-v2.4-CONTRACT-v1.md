# MANAGER CARD v2.4 CONTRACT

**message_format_version:** `sm-msg-v2.4`  
**parser_version:** `sm-parser-v3.3` (unchanged)  
**first_reply_version:** `sm-reply-v2.0`  
**Formatter:** `implementation/runtime-libs/formatter-lib.mjs`

## Logical sections (omit empty)

1. Lifecycle status  
2. Optional `🧪 Тестовая заявка` (only when `is_probable_test`)  
3. Client  
4. Contacts (phone / email / messenger — no duplicates)  
5. Website state (`Сайт` / `Сайт: отсутствует` when relevant)  
6. Alternative contact (`Telegram` / `WhatsApp` / `Другой контакт`) — never under Сайт  
7. Resolved interest  
8. Customer comment (literal customer wording)  
9. Form/source context (shortened; not duplicated into comment)  
10. Quality  
11. Missing information  
12. Recommended next step  
13. First-reply copy block  
14. Manual-send disclaimer  

## Copy block

Heading: `✉️ Ответ клиенту — нажмите, чтобы скопировать`  
Body: `<pre>{escaped first_reply_text}</pre>`  
Outside block: `Ответ клиенту автоматически не отправляется.`

### Suppressed drafts

- Test: `Черновик ответа не сформирован: тестовая заявка.` (+ disclaimer)  
- Damaged/missing contact: `Контактные данные требуют проверки.` (+ no ready copy block)

## Unchanged

- Buttons: `✅ Обработано` / `🚫 Спам`  
- Callback data / tokens  
- Delivery idempotency  
- AI OFF  

## Distinction

| Label | Content |
|-------|---------|
| Комментарий клиента | customer quote |
| Кратко / request_summary | deterministic interpretation (not shown as quote) |
| Следующий шаг | manager recommendation |
| Ответ клиенту | sendable draft |
