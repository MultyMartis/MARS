# Admin help acceptance

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Live `/help` Admin (excerpt — profile section)

```
👤 Профили ответов клиентам
/reply_profiles — список профилей
/reply_profile <номер> — профиль по номеру
/reply_name_set <номер> <имя> — задать имя для клиента
/reply_name_enable <номер> — включить персональный ответ
/reply_name_disable <номер> — выключить персональный ответ
/my_reply_profile — мой профиль ответа
```

Also present: leads/pending, reminders (config Admin-only note), system (`/stats` — статистика с 05.08.2026), AI (ИИ wording; no auto-send), users, `/config`.

## Checks

| Check | Result |
|-------|--------|
| Full reply-profile section present | pass |
| Placeholders use `<номер>` (HTML-escaped outside code) | pass |
| No substring corruption of other sections | pass |
| Explicit template rebuild (not substring patch) | pass (Help hash `479EA53B607824A2`) |
| Harness admin help lines (#29) | PASS |

## Result

- [x] Admin help accepted against ROLE-AWARE-HELP-BUILDER-v2
