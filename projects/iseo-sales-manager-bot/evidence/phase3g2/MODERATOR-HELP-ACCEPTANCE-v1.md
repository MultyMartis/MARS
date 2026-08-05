# Moderator help acceptance

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Live `/help` moderator — profile block

```
👤 Профиль ответа
/my_reply_profile — мой профиль ответа клиенту
```

## Checks

| Check | Result |
|-------|--------|
| Among profile cmds, only `/my_reply_profile` | pass |
| No `/reply_profiles` / set / enable / disable listed | pass |
| Reminder: status only (no config cmds) | pass |
| Harness mod help role-safe (#30) | PASS |

## Result

- [x] Moderator help role-safe
