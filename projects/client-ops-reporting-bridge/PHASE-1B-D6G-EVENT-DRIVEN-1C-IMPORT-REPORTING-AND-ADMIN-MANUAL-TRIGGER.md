# Phase 1B-D6G — Event-Driven 1C Import Reporting, Admin Manual Trigger and Live Acceptance

## Goal

Replace timer-assumption Telegram delivery with completion-driven reporting for SITE-002 1C imports, add OpenCart admin manual launch, keep scheduled import, and isolate no-import detection to a watchdog.

## Architecture

scheduled import OR admin manual launch
→ canonical import runner (`mars_1c_import_wrapper.php` v1.2.0)
→ unique run_id
→ catalog → offers
→ authoritative terminal.json
→ dispatch-inbox
→ Windows completion dispatcher (exact run_id)
→ n8n → Telegram → Data Table

## Evidence

`projects/client-ops-reporting-bridge/evidence/phase-1b-d6g-event-driven-1c-import-reporting/`

## Live acceptance (2026-08-06)

| Item | Value |
|------|-------|
| Manual run_id | `mars-20260806-160514-5d2cdb3b` |
| Classification | `OFFERS_INPUT_MISSING` |
| n8n execution | `24268` |
| Telegram | Delivered; factually accepted |
| Readiness | `READY_FOR_NORMAL_EVENT_DRIVEN_1C_OPERATION` |

## Final task model

1. Beget scheduled cron → canonical wrapper (`SCHEDULED`)
2. OpenCart admin → enqueue → same wrapper (`ADMIN_MANUAL`)
3. Completion poller/dispatcher → exact `run_id` → n8n → Telegram
4. 13:00 task → no-import watchdog only
