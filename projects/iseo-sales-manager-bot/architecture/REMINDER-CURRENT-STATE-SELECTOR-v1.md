# REMINDER CURRENT-STATE SELECTOR v1

**Contract id:** `iseo-reminder-current-state-selector-v1.0`  
**Phase:** 3H.8.2.2

## Purpose

Reminder pending eligibility must count **unique current business leads**, not CLEAN row inflation and not “first pending row wins”.

## Resolution

For each unique `lead_id` / business key:

1. `LEADS_CURRENT` — authoritative current-state (`lead_clean_v2` manager lifecycle in this product)
2. `LEAD_EVENTS_LATEST` — latest valid status transition (when bulk events available)
3. `CLEAN_LATEST_FALLBACK` — latest provable CLEAN projection
4. Else `SAFE_UNKNOWN` → `eligible=false`

## Pending count

`pending_count = count(unique lead_id where resolved_status=pending and eligible=true)`

## Quota

Bulk in-memory resolution only. Production Reminder Build Claims adds **zero** per-lead Sheets calls and **zero** extra sheet reads beyond the existing CONFIG/CLEAN/ACCESS/LEDGER set.

## Failure

`ERROR_CURRENT_STATE_RESOLUTION` → fail closed (no claims, no Telegram, no day stamp).
