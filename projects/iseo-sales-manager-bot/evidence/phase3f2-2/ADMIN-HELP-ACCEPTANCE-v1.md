# ADMIN HELP ACCEPTANCE v1

## Template

Rebuilt Admin `helpReply('admin')` with sections: Начало, Работа с заявками, Состояние системы, ИИ, Пользователи, Настройки, Только для администратора.

## Checks

| Check | Result |
|---|---|
| `/ai_on` intact in `<code>` | PASS |
| `/ai_off` separate line | PASS |
| `/lead_history` + HTML `&lt;номер&gt;` (renders `<номер>`) | PASS |
| `/pending_count` + `/pending_leads` | PASS |
| `/reminder_status` | PASS |
| Admin-only reminder config labelled | PASS |
| No `история лидаn` / merged AI block | PASS |
| Balanced `<code>` tags | PASS |

## Samples

Sanitized rendered text: `help-admin.sample.txt` (HTML parse_mode source).

## Live Telegram

Operator must send `/help` once after 3F.2.2 deploy for visual confirmation. Code on live Admin.dev verified patched.
