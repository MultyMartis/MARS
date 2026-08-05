# LEGACY ARCHIVE MAP v1 — Phase 3F.2

## Purpose

Map which CLEAN/RAW tabs are **current** (`v2`, in scope for real-production stats and reconciliation) versus **legacy/archive** (preserved, read-compatible, but excluded from the [PRODUCTION-STATS-EPOCH-v1.md](PRODUCTION-STATS-EPOCH-v1.md) `archive_excluded` filter).

## Tab map (per architecture/LEAD-DATA-MODEL-v1.md §1)

| Workbook | Tab | Classification | Stats scope |
|---|---|---|---|
| RAW | `lead-base` | **Legacy** — historical, preserved, not mutated | Excluded |
| RAW | `lead_raw_v2` | **Current** | Included |
| CLEAN | `lead-base-processed` | **Legacy** — historical, preserved, not mutated | Excluded |
| CLEAN | `lead_clean_v2` | **Current** | Included |
| CLEAN | `CONFIG`, `LEAD_EVENTS`, `ERRORS`, `DEDUP_INDEX` | **Current, supporting** | Not lead-count rows; not in scope for the lead-count stats but relevant for [LEAD-EVENT-HISTORY-v1.md](LEAD-EVENT-HISTORY-v1.md) |

## Legacy compatibility rule

Legacy tabs are **read-compatible only** for the pending-view fallback described in [../phase3f1/PENDING-SOURCE-FORENSIC-v1.md](../phase3f1/PENDING-SOURCE-FORENSIC-v1.md) (rows with no `manager_status`/`lifecycle_status`/`close_reason` populated default to "pending" rather than being silently dropped). They are **not** rewritten, migrated in place, or merged into `v2` tabs — per the operator-approved "keep separate, do not consolidate" decision already recorded in [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md) §1.

## Full archive tab copy (backup completeness)

A full sheet-level copy of the legacy tabs into the backup baseline (`X:\AI MARS STORAGE\backups\iseo-sales-manager-bot\2026-08-05-clean-ledger-baseline\sheets\`) has **not** been performed — that folder is currently empty (see [LEGACY-BACKUP-VALIDATION-v1.md](LEGACY-BACKUP-VALIDATION-v1.md)).

## Status

| Item | Status |
|---|---|
| Tab classification map (this document) | **IMPLEMENTED** — documentation-level, grounded in the existing architecture spec |
| Full archive tab copy into backup baseline | **PENDING OPERATOR** — not performed in this pass; do not treat as done |
| Enforcement of `archive_excluded` in a live query | **PENDING OPERATOR** — see [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md) |

*Related: [CLEAN-BACKEND-SCHEMA-v1.md](CLEAN-BACKEND-SCHEMA-v1.md), [PRODUCTION-STATS-EPOCH-v1.md](PRODUCTION-STATS-EPOCH-v1.md).*
