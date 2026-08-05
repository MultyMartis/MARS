# LIVE PROFILE READBACK — Phase 3G.1.1

**Date:** 2026-08-06  
**Method:** Admin path simulation — Read ACCESS_CONTROL for Reply Profiles + reply profile helper libs  
**Classification:** sanitized transcript — labels ADMIN_A / MOD_A only

## `/reply_profiles` (Admin aggregate)

```
Профили ответа клиенту

• ADMIN_A: Андрей · вкл · доступ: активен
• MOD_A: Михаил · вкл · доступ: активен
• MOD_B_REVOKED: Оля · выкл · доступ: revoked
• MOD_C_REVOKED: Никита · выкл · доступ: revoked
```

## `/my_reply_profile` — ADMIN_A

```
Пользователь: ADMIN_A
Имя для клиента: Андрей
Персональный ответ: включён
Роль: Админ
Статус доступа: Активен
Получатель карточек: да
```

## `/my_reply_profile` — MOD_A

```
Пользователь: MOD_A
Имя для клиента: Михаил
Персональный ответ: включён
Роль: Модератор
Статус доступа: Активен
Получатель карточек: да
```

## AI status (unchanged)

- OpenRouter nodes remain **disabled**
- `/ai_status` expected: **OFF**

## Verdict

Live readback **matches** `REPLY-PROFILE-CONTRACT-v1` and seeded values in `APPROVED-PROFILE-VALUES-v1.md`.  
Operator visual acceptance of Telegram **cards** remains pending (see T1/T3 acceptance artifacts).
