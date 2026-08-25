# SITE-002 — Current Production Architecture (1C + Client Ops)

**Canonical generation:** server-side completion dispatch (D6G / D6G1 / D6G1A / D6G1B).  
**Do not redesign production in documentation-only waves.**

## FLOW 1 — Scheduled import

```
Beget import cron (Europe/Moscow; historically 0 8 * * *)
  → /storage/mars-tools/cron/mars_1c_import_wrapper.php
  → singleton import lock
  → canonical import runner
      → catalog phase (import0_*.xml)
      → offers phase (offers0_*.xml)
  → terminal run state (authoritative)
  → mars_1c_completion_dispatch.php (if CLIENT_OPS_DISPATCH_ENABLED)
  → n8n workflow tkM4H0G0gM3q9Foi
  → Data Table dedupe (H6VYhwz7RXZCBMmu)
  → Telegram «Монитор bzpm.ru — MetaCODE»
```

## FLOW 2 — Admin manual import

```
Authenticated OpenCart admin
  → Система → Обмен с 1С → Запустить импорт 1С
  → POST + session/user_token (or current equivalent)
  → singleton lock (shared)
  → SAME canonical runner as FLOW 1
  → terminal (trigger_source=ADMIN_MANUAL)
  → server dispatcher → n8n → Telegram
```

Manual launch processes what the server **currently has**. It does **not** necessarily cause external 1C to generate/upload files.

## FLOW 3 — No-import watchdog

```
Beget watchdog cron (Europe/Moscow; historically 0 9 * * *)
  → server watchdog / HTTP gateway
  → condition evaluation (no qualifying import)
  → respects kill switch
  → n8n / Telegram when condition applies
```

Operator-created Beget cron is accepted; Beget API create historically AUTH_ERROR.

## FLOW 4 — Hygiene monitor (optional)

```
Windows Scheduled Task MARS_SITE_002_Post_1C_Catalog_Monitor
  → hidden/noninteractive runner (self-hide)
  → catalog/sitemap/onboarding hygiene diagnostics
  → NOT Client Ops Telegram authority
  → NOT required for normal production reporting
```

## Authority vs diagnostics

| Concern | Authority |
|---------|-----------|
| Did import run / terminal classification | Server terminal state |
| Outbound Client Ops event | Server completion dispatcher + n8n |
| No-import alert | Server watchdog |
| Operator notification | Telegram via n8n |
| Catalog hygiene after category changes | Optional Post_1C Windows monitor |

## Key server components (repo mirrors)

Under `X:\AI MARS\projects\ocpilot\sites\site-002\tools\`:

- `mars_1c_import_wrapper.php`
- `mars_1c_completion_dispatch.php`
- `mars_1c_no_import_watchdog.php`
- `mars_1c_watchdog_http_gateway.php`

Live deployment path pattern: `/storage/mars-tools/cron/…` on Beget. Protected non-Git local config holds dispatch enablement and secrets — **do not commit secrets**.
