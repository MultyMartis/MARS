# Config human display

**Phase:** 3G.2.2
**Status:** FILLED
**Sanitized labels only:** ADMIN_A · MOD_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Purpose

Record the corrected `/config` (Admin) human-readable output contract after the Config Truth forensic, so the displayed lines match the live contour rather than a stale CONFIG snapshot.

## 2. Corrected `/config` line set (pattern, sanitized)

```
Контур: Operational.dev активен · Admin.dev активен · Sales-Manager-v2 неактивен
Статистика с: 05.08.2026
Парсер: sm-parser-v3.3
Формат карточки: sm-msg-v2.4
Персонализация: iseo-recipient-name-v1.1
Резолвер профилей: iseo-reply-profile-resolver-v1.0
AI: выключен
Напоминания: выключены
Синхронизация отчётности: выключена
Активные получатели персонализации: 2
```

## 3. What changed vs pre-3G.2.2 `/config`

| Line | Before | After |
|------|--------|-------|
| Парсер | `sm-parser-v3.2` (stale CONFIG key) | `sm-parser-v3.3` (matches live `Parse Lead`) |
| Резолвер профилей | absent | `iseo-reply-profile-resolver-v1.0` |
| Синхронизация отчётности | absent / ambiguous | explicit «выключена» |
| Активные получатели персонализации | absent | `2` |

## 4. Formatting rules honoured

- No Telegram IDs, workbook IDs, chat IDs, or secrets in any line.
- Unavailable values render as «не задано», never blank or `undefined`.
- Timestamp lines use Moscow local time (`Europe/Moscow`), not raw ISO/UTC.
- Plain Russian labels only — no raw enum values (`true`/`false`, `active`) leak into the summary text.

## 5. Related authority

Wording authority: `architecture/TELEGRAM-TEXT-CONTRACT-v2.md` §8. Field truth source: `CONFIG-TRUTH-FORENSIC-v1.md`.

## Result

- [x] `/config` line set corrected to reflect live truth
- [x] Formatting/safety rules verified (no secrets, no IDs, human labels only)
