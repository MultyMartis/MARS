# ADMIN-START-COMMAND-CONTRACT v1

**Phase:** 3D.2  
**Workflow:** Admin.dev (same ID)

## Authorized `/start`

```
Sales Manager Admin запущен.

Контур: рабочий
Режим ИИ: выключен

Используйте /help, чтобы посмотреть доступные команды.
```

Dynamic mapping:

| CONFIG | Wording |
|--------|---------|
| `environment=production` | Контур: `рабочий` |
| `environment=dev` (etc.) | Контур: `разработка` |
| `ai_enabled=true` | Режим ИИ: `включён` |
| `ai_enabled=false` | Режим ИИ: `выключен` |

## Normalization

- `/start@bot_username` → `/start`
- Payload after `/start` is not a privileged alternate command

## Authorization

- Allowlist size remains **1** (operator only)
- Unauthorized → `Доступ запрещён.`
- Unauthorized must not receive environment, AI state, health, stats, config, or command list

## Routing

- New Code node: `Start`
- `Route Command` includes `start` output
- `Start` → `Capture Admin Reply` → Safe Telegram Reply

## Help

`/start` listed under «Начало»; `/test_lead` remains omitted.
