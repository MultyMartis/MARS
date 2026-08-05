# Start text acceptance

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Admin `/start` (live)

```
INTLSEO Sales Manager готов к работе.

Бот принимает заявки с сайта i-seo.su, готовит персональный первый ответ и ведёт историю обработки.

Ваш доступ: Администратор

ИИ: выключен
Напоминания: выключены

Основные команды:
/pending_count — необработанные заявки
/leads — история лидов
/reply_profiles — имена сотрудников в ответах
/help — все команды
```

## Moderator `/start` (live)

```
INTLSEO Sales Manager готов к работе.

Бот принимает заявки с сайта i-seo.su и готовит персональный первый ответ с вашим утверждённым именем.

Ваш доступ: Модератор

Основные команды:
/pending_count
/pending_leads
/leads
/my_reply_profile
/help
```

## Checks

| Check | Result |
|-------|--------|
| INTLSEO branding present | pass |
| Russian role labels | pass |
| AI/reminders OFF shown to Admin | pass |
| Moderator tips `/my_reply_profile` | pass |
| Start node hash | `43243C4CE1526570` |

## Result

- [x] Role-aware `/start` matches TEXT-CONTRACT-v2
