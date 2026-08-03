# NOTIFICATION FAILURE BOUNDARY v1

## Граница транзакции
Изменение ACCESS_CONTROL предшествует Telegram notification и **не откатывается** при delivery failure. Это относится и к выдаче, и к отзыву роли.

## Поведение
- Finalize Access Notification классифицирует недоступную цель и Telegram API/delivery error как failed.
- В ACCESS_EVENTS записывается соответствующий `*_notification_failed`.
- Admin получает точный безопасный ответ: `Права изменены, но уведомление пользователю доставить не удалось.`
- При успехе записывается `*_notification_sent`.

Ни raw Telegram IDs, ни стек ошибок в ответ не попадают. Harness cases 12, 14–16 PASS.
