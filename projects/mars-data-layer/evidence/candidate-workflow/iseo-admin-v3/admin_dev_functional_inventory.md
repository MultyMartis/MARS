# Admin.dev → Admin.v3.dev functional parity matrix

Source: active `Admin.dev` `wLrLp4WQHm1VJmxz` (Sheets SoT).
Target: inactive `Admin.v3.dev` `Zk9b1BiXpYN9rMMo` (PG `app_iseo_sales`).

| Current function | Sheets READ | Sheets WRITE | Target PG contract | Parity |
|---|---|---|---|---|
| `/help` | no | no | static/help via `admin_runtime_call('help')` | PASS (offline) |
| `/status` | CONFIG / CLEAN sample | no | `get_admin_status_snapshot()` | PASS — AVAILABLE FROM PG |
| `/ai_status` | CONFIG | no | config keys via snapshot / `get_active_config` | PASS — live AI not flipped |
| `/health` | Sheets deps (abort risk) | no | `get_admin_health()` component status | PASS — degraded components allowed |
| `/stats` | CLEAN / events | no | `get_admin_stats()` | PASS — AVAILABLE FROM PG; legacy Sheets history = LEGACY HISTORY ONLY |
| `/last_error` | ERRORS | no | `get_last_error()` → `errors` | PASS |
| `/config` | CONFIG | Apply CONFIG Write | `get_active_config` / `set_config_value` | PASS — secrets rejected |
| `/ai_on` / `/ai_off` | CONFIG | Apply CONFIG Write | `set_config_value` on approved keys only | PASS contract; live AI unchanged in tests |
| `/leads` | lead_clean_v2 | no | `list_leads_page` | PASS |
| Reminder digest | CLEAN + REMINDER_DELIVERIES + CONFIG | claim/delivered/window CONFIG | `list_pending_lead_groups` + `claim_reminder_window` + `record_reminder_delivery` | PASS |
| Reminder group navigation | CLEAN (429 risk) | no | `get_pending_leads_in_group` | PASS — PG only |
| Exact-lead navigation | CLEAN / LEAD_DELIVERIES | no | `get_lead_card_payload` | PASS |
| Callback Processed / Spam | CLEAN + ACCESS | Update CLEAN + Append LEAD_EVENTS | `admin_callback_lead_action` → `change_lead_status` | PASS + idempotent |
| Canonical card sync | LEAD_DELIVERIES | (via lifecycle/events) | `get_lead_card_payload` + `update_delivery_message_binding` / deliveries | PASS contract; dry-run Telegram |
| ACCESS lookups | ACCESS_CONTROL | Upsert ACCESS_CONTROL + ACCESS_EVENTS | `access_rules` + `check_access` | PASS read parity; no revoke/restore in wave |
| Deliveries / message IDs | LEAD_DELIVERIES | REMINDER_DELIVERIES upserts | `deliveries` | PASS |
| Current-state reads | lead_clean_v2 / lead_raw_v2 | Update CLEAN Lifecycle | `leads` current row | PASS |
| Errors / reminder 429 | ERRORS | Append ERRORS Reminder 429 | `record_error` / `errors` | PASS — Sheets 429 path eliminated |
| PROFILE_EVENTS append | PROFILE sample | Append PROFILE_EVENTS | DEFERRED / audit via lead_events+audit where applicable | DEFERRED — not critical SoT for Admin.v3 runtime |

## Notes

- Google Sheets nodes on Admin.v3 critical path: **0**.
- Synthetic Telegram / Olya / customer traffic: **0**.
- Malformed `LEGACY INVALID ROW` delivery excluded from card payload queries.
