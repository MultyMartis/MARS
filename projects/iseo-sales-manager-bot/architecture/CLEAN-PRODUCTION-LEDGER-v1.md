# CLEAN PRODUCTION LEDGER v1

**Phase:** 3F.2 · **Status:** active  
**Timezone:** Europe/Moscow · **Generation:** v2 · **Legacy mode:** archive_excluded

## Purpose

Authoritative production lead accounting begins with the first confirmed real lead of the clean epoch. Mixed historical/test rows remain archived and never enter production statistics, `/leads`, pending views, reminders, or the employee reporting workbook.

## Authoritative table

`LEADS` — one row = one logical real lead. Recipient delivery rows are not leads.

Required invariants for production rows: `is_real_lead=true`, `is_probable_test=false`, `stats_included=true`, `archive_state=active`, `production_generation=v2`.

## Related tabs

- `LEAD_EVENTS` / append-only history (see LEAD-EVENT-HISTORY-v1)
- `LEAD_DELIVERIES`, `REMINDER_DELIVERIES`
- `TEST_LEADS`, `TEST_LEAD_EVENTS` — fixtures only
- `SYNC_STATE` — reporting sync status
- `CONFIG`, `ACCESS_CONTROL` — operational, not reset
- Archive tabs `ARCHIVE_*_PRE_2026-08-05` — forensic only

## Epoch boundary

Human display start: **05.08.2026**. Exact ledger boundary: authoritative Gmail `internalDate` of the first real lead (Клиент A). See PRODUCTION-STATS-EPOCH-v1.


## 3F.2.1 note

Human-facing list/history adapters must read LEADS field names (`lifecycle_status`, `resolved_service_label`, `client_comment`, `source_display`). Do not assume legacy CLEAN `manager_status`/`service`/`summary` alone.

## Phase 3G.1 ledger note

LEADS remains one-row-per-business-lead. Personalized reply texts belong in `RECIPIENT_REPLIES` or extended `LEAD_DELIVERIES`, not duplicated LEADS rows. Reporting workbook keeps shared template id only. Stats counting invariant unchanged.
