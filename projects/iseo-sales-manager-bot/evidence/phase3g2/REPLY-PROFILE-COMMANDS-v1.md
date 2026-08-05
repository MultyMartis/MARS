# Reply profile commands acceptance

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Addressing

Number-based only. Username / display-name / Telegram-ID addressing obsolete.

## Live command results (sanitized)

### `/reply_profiles` (Admin)

```
👤 Профили ответов клиентам

1. ADMIN_A
Имя в ответе: Андрей
Персональный ответ: включён
Роль: Администратор
Доступ: Активен
Получает карточки: да

2. MOD_B_REVOKED
Имя в ответе: Оля
Персональный ответ: выключен
Роль: Модератор
Доступ: Доступ отозван
Получает карточки: нет

3. MOD_A
Имя в ответе: Михаил
Персональный ответ: включён
Роль: Модератор
Доступ: Активен
Получает карточки: да

4. MOD_C_REVOKED
Имя в ответе: Никита
Персональный ответ: выключен
Роль: Модератор
Доступ: Доступ отозван
Получает карточки: нет
```

### `/reply_profile 3` (Admin) — final enabled state

```
👤 Профиль ответа клиенту №3

Пользователь: MOD_A
Имя в ответе: Михаил
Персональный ответ: включён
Роль: Модератор
Доступ: Активен
Получает карточки: да

Пример представления:
"Меня зовут Михаил, компания INTLSEO."
```

### Mutations (Admin) — disable then enable restore

- Disable reply: personalization OFF for MOD_A; cards continue eligibility unchanged.
- Enable reply: personalization ON; name Михаил.
- Live Sheets oneshots + final readback: **PASS**.

### Invalid / deny

| Case | Reply (sanitized) |
|------|-------------------|
| `/reply_profile 999` | `Профиль с таким номером не найден. Посмотрите доступные номера командой /reply_profiles.` |
| Invalid multi-token name | Points to `/reply_name_set 3 Михаил` |
| Moderator `/reply_name_set` | `Эта команда доступна только администратору.` |
| Moderator `/reply_profiles` | `Эта команда доступна только администратору.` |

### `/my_reply_profile` (MOD_A)

Self card matches №3: name Михаил, enabled, moderator, active.

## Result

- [x] Number syntax live
- [x] Admin mutations + moderator view-only among profile cmds
