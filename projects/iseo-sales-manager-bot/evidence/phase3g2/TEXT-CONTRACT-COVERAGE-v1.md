# Text contract coverage

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Authority

`architecture/TELEGRAM-TEXT-CONTRACT-v2.md` + registry S01–S26.

## Mapping

| Contract rule | Evidence |
|---------------|----------|
| Russian role/status labels | REPLY-PROFILE-COMMANDS / help / start live samples |
| Number-based profile surfaces | REPLY-PROFILE-COMMANDS-v1 |
| Admin-only deny wording | live `mod_denied_set` |
| Invalid number / name hints | live invalid cases |
| Explicit Admin vs moderator help | ADMIN/MODERATOR-HELP-ACCEPTANCE |
| AI OFF Russian ИИ | AI-TEXT-ACCEPTANCE |
| Stats epoch + LEADS | STATS-TEXT-ACCEPTANCE |
| Config non-secret | CONFIG-TEXT-ACCEPTANCE |
| Reminders OFF posture | REMINDER-TEXT-ACCEPTANCE |
| Client name = reply_sender_name only | PROFILE-NUMBER-READBACK + commands |
| No nickname in customer copy | MOD_A → Михаил |

## Result

- [x] Registry surfaces mapped to TEXT-CONTRACT-v2 rules
