# LEGACY ARCHIVE MAP v1 — Phase 3F.2

## Purpose

Separate mixed pre-epoch corpus from the clean production ledger (`LEADS`, generation v2).

## Live archive tabs created

| Tab | Role |
|---|---|
| `ARCHIVE_CLEAN_PRE_2026-08-05` | Archive of mixed CLEAN corpus |
| `ARCHIVE_LEAD_EVENTS_PRE_2026-08-05` | Archive placeholder / events archive |
| `ARCHIVE_LEAD_DELIVERIES_PRE_2026-08-05` | Archive placeholder |
| `ARCHIVE_REMINDER_DELIVERIES_PRE_2026-08-05` | Archive placeholder |
| `ARCHIVE_DEDUP_PRE_2026-08-05` | Archive placeholder |
| `LEADS` | Authoritative production leads (v2) |
| `TEST_LEADS` / `TEST_LEAD_EVENTS` | Fixture-only |
| `SYNC_STATE` / `RAW_CURRENT` / `CLEAN_CURRENT` | Supporting |

Original operational tabs (`lead_clean_v2`, `CONFIG`, `ACCESS_CONTROL`, existing `LEAD_EVENTS`, etc.) were **not** deleted.

## Status

| Item | Status |
|---|---|
| Archive / canonical tabs created in backend workbook | **PASS** |
| Full CLEAN → `ARCHIVE_CLEAN_PRE_2026-08-05` row copy | **PARTIAL** — follow-up hit Sheets quota; originals retained |
| Production `/leads` / pending source = `LEADS` | **PASS** (Admin retarget) |
| Archive rows entering production stats | **0** by source design |

*Related: [LEGACY-BACKUP-VALIDATION-v1.md](LEGACY-BACKUP-VALIDATION-v1.md), [CLEAN-BACKEND-SCHEMA-v1.md](CLEAN-BACKEND-SCHEMA-v1.md).*
