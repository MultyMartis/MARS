# SITE-002 — Manual Admin Import Contract

## Path

OpenCart admin → **Система → Обмен с 1С** → button **Запустить импорт 1С**

## Properties

- Authenticated admin access + permission boundary
- POST + `user_token` (or current equivalent CSRF/session token)
- Async execution
- Singleton lock shared with scheduled import
- **Same canonical runner** as Beget cron path — no separate importer logic
- Status polling in admin UI
- `trigger_source=ADMIN_MANUAL` on terminal

## Critical distinction

Manual launch processes files **already present on the server**.  
It does **NOT** necessarily cause external 1C to generate or upload new exchange files unless separately proven.

## Dispatch

After terminal: same server completion dispatcher → n8n → Telegram (if kill switch enabled).
