# ROLE GRANT NOTIFICATION v1

После успешной неидемпотентной `/moderator_add CODE` сначала фиксируется ACCESS_CONTROL: `role=moderator`, `status=active`; затем пользователю направляется точный текст:

```text
Вам выданы права модератора Sales Manager.

Теперь вы можете работать с карточками лидов и отмечать их обработанными или как спам.

Используйте /start или /help.
```

Повторная выдача уже active moderator не создаёт новую запись ACCESS_CONTROL, ACCESS_EVENTS или уведомление.

Harness: grant success/failure, persistence при notify failure и repeated-add no-resend — PASS.
