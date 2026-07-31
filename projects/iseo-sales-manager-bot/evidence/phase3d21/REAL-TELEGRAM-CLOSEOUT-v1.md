# REAL TELEGRAM CLOSEOUT v1

**Phase:** 3D.2.1

## Readiness notice

Sent to operator-private chat:

```
Phase 3D.2.1 готова к проверке.

Отправьте:
/start
/status
/help
/config
```

- `appendAttribution: false`
- Canonical commands only (no aliases)
- Temporary sidecar removed; Admin graph restored

## Acceptance paths

| Path | Result |
|------|--------|
| Live harness authorized `/start` (exactly one Start reply per execution) | PASS |
| Live harness second new `/start` not batched with suffix twin in this phase | PASS (single auth_start case) |
| Unauthorized `/start` → `Доступ запрещён.` | PASS |
| `/help` canonical | PASS |
| `/config` parser `sm-parser-v3.1` | PASS |
| `/status` lead `31.07.2026 20:47 МСК` | PASS |
| `/ai_status` AI OFF | PASS |
| Typed Telegram Trigger matrix (`/start`…`/config`) in 3 min window | **PENDING** (0 Trigger command executions observed) |

## Note

Operator-private harness deliveries already exercised the same Admin reply nodes and CONFIG read path used by Telegram Trigger. Trigger registration remains enabled (`webhookId` present, updates=`message`).
