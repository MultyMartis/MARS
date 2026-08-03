# GUARANTEED RESPONSE CONTRACT v1

Every received text command must end in **exactly one** Telegram response.

| Outcome | Reply |
|---|---|
| Admin/moderator success | Normal command result |
| Known forbidden | Explicit denial (role-aware) |
| Unknown command | `Команда не найдена. Используйте /help.` |
| Registry technical failure (non-Admin bootstrap) | `Сервис временно недоступен. Попробуйте позже.` |
| Internal processing failure | `Не удалось обработать команду. Ошибка зарегистрирована.` |

No command branch may silently output zero items after the auth stage.
