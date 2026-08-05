# Stale-text audit

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Pre-patch findings (FORENSIC-TEXT-INVENTORY)

| Finding | Severity | Disposition |
|---------|----------|-------------|
| Reply-profile help / error strings used username-token syntax (`/reply_name_set <пользователь> <имя>`) | High | Replaced with number syntax `<номер>` in live Reply Profile Commands + help templates |
| Help node mentioned user-token addressing; substring-style risk | High | Rebuilt via ROLE-AWARE-HELP-BUILDER-v2 explicit templates (no substring patch) |
| Upsert ACCESS_CONTROL schema lacked `reply_profile_number` | High | Schema extended; Prepare Access Upsert flattens reply fields |
| Stats node historically tied to CLEAN label risk | Medium | Stats refreshed to authoritative **LEADS** + epoch **05.08.2026** |
| Start / AI / Config / Reminder / Unknown wording drift vs post-3E–3G product | Medium | Nodes patched per PATCH-RECEIPT |
| Obsolete class: username-token profile addressing | Obsolete | Documented obsolete in text registry |

## Post-patch

- Live `/help` Admin includes number-based profile section.
- Live `/help` moderator lists only `/my_reply_profile` among profile cmds.
- Invalid name hint: `/reply_name_set 3 Михаил` (number example).
- Deny text: `Эта команда доступна только администратору.`
- Client-facing name for MOD_A remains **Михаил** (nickname never in customer copy).

## Result

- [x] Stale username-token addressing removed from live Admin command surfaces
- [x] Text contract surfaces refreshed
