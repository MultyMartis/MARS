# ADMIN OUTPUT POLISH v1

Commands rechecked: /help /status /ai_status /health /stats /last_error /config /unknown.

| Command | OK | Authorized | RU labels | Telegram delivered |
|---------|----|------------|-----------|--------------------|
| /help | PASS | true | yes | yes |
| /status | PASS | true | yes | yes |
| /ai_status | PASS | true | yes | yes |
| /health | PASS | true | yes | yes |
| /stats | PASS | true | yes | yes |
| /last_error | PASS | true | yes | yes |
| /config | PASS | true | yes | yes |
| /foobar_unknown | PASS | true | yes | yes |

Required CONFIG shape accepted:

```
Контур: разработка
Режим ИИ: выключен
Версия парсера: sm-parser-v3
Версия сообщений: sm-msg-v1
```

Auth polish: Check User Authorization reads identity from Normalize Command and collapses multi-row CONFIG reads. Last Error preserves identity after ERRORS reads.

Allowlist size: 1. Final `ai_enabled=false`. Private identifiers masked.
