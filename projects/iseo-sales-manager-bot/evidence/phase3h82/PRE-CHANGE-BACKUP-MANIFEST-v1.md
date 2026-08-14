# PRE-CHANGE BACKUP MANIFEST v1

**Phase:** 3H.8.2  
**Stamp:** 2026-08-14T08-27-10-882Z (pre-change) and 2026-08-14T08-32-50-598Z (pre-patch)

Private copies live under `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\phase3h82-local\backups\` (outside Git).

| Artifact | Location (private) | Notes |
|---|---|---|
| Admin.dev | `pre-change-*/` and `pre-patch-*/Admin.dev.pre-patch.json` | 87 nodes, active |
| Operational.dev | same | 45 nodes, active; **not patched** |
| CONFIG reminder keys | sidecar snapshot 08:27Z | enabled=true, time=10:00, tz=Europe/Moscow, last_window=null |
| ACCESS_CONTROL | sidecar / later isolated read | 4 active staff (isolated read n=4) |
| lead_clean_v2 | later isolated read | 129 rows |
| REMINDER_DELIVERIES | snapshot | 0 rows in 08:27 sidecar (burst read empty/error) |
| ERRORS | snapshot | tail empty in burst sidecar |
| reminder schedule | Admin node `Reminder Schedule Trigger` | 15 min interval |
| `/reminder_status` | Code `Reminder Commands` | pre-patch lacked ERROR stage/retry lines |

No PII in this manifest. Full JSON remains private.
