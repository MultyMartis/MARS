# CURRENT-STATE SOURCE PRECEDENCE v1

Contract: `iseo-reminder-current-state-selector-v1.0`

| Priority | Source value | Rule |
|---|---|---|
| 1 | `LEADS_CURRENT` | Authoritative current-state row. In this product, `lead_clean_v2` manager lifecycle fields **are** the LEADS current-state store. Latest by `manager_status_updated_at` / related authority timestamps. |
| 2 | `LEAD_EVENTS_LATEST` | If LEADS_CURRENT unavailable: most recent valid status transition (`marked_spam`, `marked_processed`, `reopened`, `status_pending`, …). Library/harness; production Build Claims does **not** add a Sheets EVENTS read (quota). |
| 3 | `CLEAN_LATEST_FALLBACK` | Latest provable CLEAN projection when manager authority fields absent. |
| fail | `SAFE_UNKNOWN` | Conflict / unprovable ordering → `eligible=false`. |

Resolution result object fields: `lead_id`, `resolved_status`, `source`, `source_timestamp`, `confidence`, `reminder_eligible`, `exclusion_reason`.
