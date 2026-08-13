# PENDING SELECTOR FORENSIC — Phase 3H.8

## Root mismatch
| Path | Sheet |
|---|---|
| Operational append/update CLEAN | `lead_clean_v2` |
| Admin callback Update CLEAN Lifecycle | `lead_clean_v2` |
| Admin Read CLEAN for Reminder (pre-repair) | **`LEADS`** |
| Admin Read CLEAN for Pending (pre-repair) | **`LEADS`** |

`LEADS` uses a different schema (`lifecycle_status`) and was effectively empty/stale (1 processed row at window).
`lead_clean_v2` uses `manager_status` and holds live production leads.

## life() behavior
Build Claims treats non-processed/non-spam as pending (covers `pending`/`new`/blank). Selector failure was **sheet identity**, not status-label mismatch.
