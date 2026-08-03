# ROLE REVOKE NOTIFICATION v1

После успешной неидемпотентной `/moderator_remove CODE` строка ACCESS_CONTROL сохраняется с `role=moderator`, `status=revoked`; затем пользователю направляется точный текст:

```text
Ваши права модератора Sales Manager отозваны.

Публичные команды /start, /help и /my_status остаются доступны.
```

Повторное снятие already-revoked не отправляет уведомление повторно. Снять права Admin этой командой нельзя.

Harness: revoke success/failure, persistence при notify failure и repeated-remove no-resend — PASS.
