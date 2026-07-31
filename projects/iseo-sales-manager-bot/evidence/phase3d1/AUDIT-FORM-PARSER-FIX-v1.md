# AUDIT-FORM-PARSER-FIX-v1

**Phase:** 3D.1  
**Parser stamp:** `sm-parser-v3.1`  
**Workflow:** Operational.dev (same ID; in-place patch)

## Change

Replaced passthrough Parse Lead with label-delimited extraction:

- Labels: `От кого:` / `Имя:`, `Способ связи:`, `Контакт:`, `Телефон:`, `Email:` / `E-mail:` / `Почта:`, `Адрес сайта:` / `Сайт:`, `Комментарий:` / `Сообщение:`, `Отправлено со страницы:`
- Value ends at the **next** known label or form-title boundary (`Заявка на бесплатный аудит`)
- Supports multiline, collapsed single-line, optional spaces, Unicode/NBSP, case-insensitive labels
- First label occurrence wins (quoted/forwarded duplicates do not overwrite)

## Contact method

| Способ связи | Контакт handling |
|--------------|------------------|
| Телефон | phone if valid (≥10 digits; plus/spaces/parens/hyphens allowed) |
| Email / E-mail / Почта | email |
| Telegram | messenger (@handle / t.me) or phone if digits |
| WhatsApp | phone if digits else messenger |
| unknown | infer from bounded validation |

Rejects placeholders: `44`, `#ERROR!`, `UNKNOWN`, empty/generic tokens.

## Site

Accepts with/without scheme; strips surrounding punctuation only; **no** DNS/HTTP check; `.example` operator hosts accepted; `нет` rejected.

## Service

`Заявка на бесплатный аудит` → `form_name` set; Deterministic service rules still match Audit (also checks `form_name`).

## Deterministic touch

Service detection input includes `form_name` so comment-only `request_text` still classifies as Audit.

## Live patch

- Temporary deactivate Operational.dev → PUT → reactivate
- Sales-Manager-v2 remained inactive
- Admin.dev patched separately for stats/error lifecycle
- Node count remained **34**
- AI OFF preserved
- **0** new workflows
