# SETTINGS PAGE — P18C-FU01

Direct `MailFormsSettings::render_page()` after menu fix (CLI, user `mars`).

| Check | Result |
|-------|--------|
| H1 Почта и формы | PASS |
| Отправка почты | PASS |
| SMTP host/port/encryption/auth/username | present |
| Новый пароль input empty | PASS |
| Existing secret not in HTML | PASS (`mail_contains_secret=false`; password NOT CONFIGURED) |
| Отправитель | present (default `noreply@shpigovsky.ru`) |
| Получатели repeater | PASS |
| Цель Яндекс.Метрики | PASS |
| Counter not duplicated (SEO owner) | PASS |
| Проверка block | present; test button hidden until complete |
| SMTP state | NOT CONFIGURED |

No credentials entered.
