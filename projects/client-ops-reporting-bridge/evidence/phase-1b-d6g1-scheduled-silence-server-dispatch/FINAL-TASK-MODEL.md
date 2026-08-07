# Final Task Model (D6G1)

## SERVER

| Component | Schedule | Role |
|-----------|----------|------|
| Beget scheduled 1C import → `mars_1c_http_gateway.php?mode=run` → canonical wrapper | `0 8 * * *` Moscow (~12:00 +07) | Import only + **server-side completion dispatch** |
| OpenCart admin `tool/mars_1c_exchange` | on demand | ADMIN_MANUAL enqueue → same wrapper → **server-side completion dispatch** |
| Server-side completion dispatcher (`mars_1c_completion_dispatch.php`) | immediate after terminal | SUCCESS / ATTENTION / FAILED → n8n → Data Table → Telegram |
| Server-side no-import watchdog (+ HTTP gateway) | intended `0 9 * * *` Moscow (~13:00 +07) via Beget panel | NO_FRESH_IMPORT only |
| Bounded `--dispatch-recover` | operator/manual | PENDING/FAILED_RETRYABLE only; no uncontrolled loops |

## WINDOWS

| Component | State | Role |
|-----------|-------|------|
| MARS_SITE_002_Import_Completion_Poller | **DISABLED_AND_RETIRED** | must not run |
| MARS_SITE_002_Client_Ops_Producer (watchdog) | **DISABLED** | replaced by server watchdog |
| MARS_SITE_002_Post_1C_Catalog_Monitor | Enabled | sitemap/catalog hygiene only (not completion reporting) |

## Gate

`D6G1_FINAL_TASK_MODEL_MINIMIZED`
