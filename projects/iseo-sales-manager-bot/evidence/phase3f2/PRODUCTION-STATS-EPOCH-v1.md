# PRODUCTION STATS EPOCH v1 — Phase 3F.2

## Purpose

Define the single, unambiguous point-in-time from which "real production" statistics (as opposed to test/synthetic fixture volume or pre-migration legacy volume) are counted, so future stats never silently drift depending on which tab or which timestamp field happens to be read.

## Epoch definition

| Field | Value |
|---|---|
| Display date (operator-facing) | **05.08.2026** |
| Exact epoch instant | Клиент A's authoritative `received_at` — Gmail `internalDate` = `2026-08-05T13:02:57.000Z` = 05.08.2026 16:02:57 МСК (Europe/Moscow) |
| Why this instant | Клиент A is the first confirmed real (non-test) lead in the current forensic window — see [CURRENT-REAL-LEAD-SAFETY-v1.md](CURRENT-REAL-LEAD-SAFETY-v1.md) — so it is the natural, evidence-backed start of the "real production" counting window |
| Timezone | Europe/Moscow, consistently, matching the existing project convention (`pending_reminder_timezone` default, Telegram human-date formatting) |

## Filter generation

| Tag | Meaning |
|---|---|
| `generation v2` | Counts are scoped to the `lead_raw_v2` / `lead_clean_v2` tab generation only — see [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md) §1 |
| `legacy archive_excluded` | Historical `lead-base` / `lead-base-processed` tabs are **excluded** from this stats view — they remain preserved but out of scope; see [LEGACY-ARCHIVE-MAP-v1.md](LEGACY-ARCHIVE-MAP-v1.md) |
| `real-only-v1` | Rows where `is_probable_test`/synthetic markers evaluate true (per `isProbableTest()` in `implementation/runtime-libs/pending-leads-lib.mjs`) are excluded — see [TEST-DATA-SEPARATION-v1.md](TEST-DATA-SEPARATION-v1.md) |

## Composite rule

A row counts toward "real production stats" if and only if: it is in a `v2` tab, its `received_at` (or best-available timestamp) is `>=` the epoch instant above, and `is_probable_test` (and equivalent synthetic markers) evaluate `false`.

## Status

| Item | Status |
|---|---|
| Epoch definition and filter contract | **IMPLEMENTED** (documentation-level decision, grounded in forensic facts) |
| Wired into a live reporting workbook/query | **PENDING OPERATOR** — see [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md); not claimed as live in this pass |

*Related: [EVGENIY-LEAD-FORENSIC-v1.md](EVGENIY-LEAD-FORENSIC-v1.md), [LEGACY-ARCHIVE-MAP-v1.md](LEGACY-ARCHIVE-MAP-v1.md).*
