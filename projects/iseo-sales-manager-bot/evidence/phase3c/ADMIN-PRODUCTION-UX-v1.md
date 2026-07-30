# ADMIN PRODUCTION UX v1

| Command | Production behavior |
|---------|---------------------|
| /status | Контур: рабочий; рабочий процесс включён; админ включён; ИИ выключен |
| /ai_status | ИИ выключен; probe disabled |
| /health | v2 sheets available; Gmail binding found; Telegram available; AI probe skipped |
| /config | рабочий контур; secrets hidden |
| /stats | production filter wording; bounded 7-day counts |
| /last_error | production wording («рабочая ошибка») |
| /test_lead | remains deferred (not exercised) |

Admin.dev remained active through cutover (temporary webhook health windows restored Trigger).
