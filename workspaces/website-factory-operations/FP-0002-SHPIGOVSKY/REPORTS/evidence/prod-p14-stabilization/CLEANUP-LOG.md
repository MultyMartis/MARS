# CLEANUP-LOG — PROD-P14

## 1. Activity Log QA rows (proven)

| Field | Value |
|-------|-------|
| Owner | MARS QA (PROD-P13-FU01 HTTP persist probes) |
| Why obsolete | Synthetic titles `FP02 FU01 HTTP*` — not Olya/operator content |
| Exact objects | `fp02_user_activity_log` ids **68, 69, 70, 71** (object_ids 2028/2029) |
| Before | 4 rows present |
| After | 4 rows deleted |
| Rollback | Restore from DB dump `X:\AI MARS STORAGE\backups\fp-0002\prod-p14-full-20260816-173046\db-shpigovsky_main.sql.gz` (pre-cleanup? — cleanup ran before full backup download completed; rows may already be absent in backup). Prefer Layer B evidence JSON `CLEANUP-QA-AND-META.json` for identity; if restore needed, re-insert from that JSON or earlier P13 FU01 DB snapshot. |

Note: QA posts #2028/#2029 were already absent; only log rows removed.

## 2. Stale dashboard service record

| Field | Value |
|-------|-------|
| Owner | shpigovsky-core SystemDashboard (P13) |
| Why obsolete | P08/P09/P10-era concise table no longer reflects accepted baseline |
| Exact object | `SystemDashboard.php` + option `fp02_metacode_system_meta` |
| Before | Short P13 table |
| After | P14 sectional widget + meta |
| Rollback | Layer B `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p14-layer-b-pre\` |

## 3. Not removed

- Real Activity Log history (Olya specialist/service updates)
- Migration MU plugin file
- robots.txt
- Storage backups / evidence reports
- Schema version options

## Required

`ONLY PROVEN OBSOLETE SERVICE/QA RESIDUE REMOVED`
