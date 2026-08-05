# REPORTING WORKBOOK CREATION v1 — Phase 3F.2

## Intent

A separate reporting workbook (distinct from RAW/CLEAN) is the intended home for aggregate, real-only production statistics — scoped by [PRODUCTION-STATS-EPOCH-v1.md](PRODUCTION-STATS-EPOCH-v1.md) and excluding legacy/archive tabs per [LEGACY-ARCHIVE-MAP-v1.md](LEGACY-ARCHIVE-MAP-v1.md) and test rows per [TEST-DATA-SEPARATION-v1.md](TEST-DATA-SEPARATION-v1.md). This mirrors the existing project decision to keep RAW and CLEAN as separate workbooks rather than proliferating tabs inside CLEAN (`STATS_DAILY` was already flagged as optional/deferred in [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md) §4).

## What this evidence pass does and does not claim

- No workbook ID or URL is recorded anywhere in Phase 3F.2 evidence, by charter — regardless of whether one exists yet.
- This document does **not** assert that a reporting workbook has been created, populated, or connected to a live sync in production.

## Status

| Item | Status |
|---|---|
| Reporting workbook purpose/contract (this document + linked epoch/archive/test-separation docs) | **IMPLEMENTED** (design-level) |
| Actual workbook creation | **PENDING OPERATOR** |
| Tab layout inside the workbook | **PENDING OPERATOR** — depends on operator's chosen reporting tool/destination |

## SAFE UNKNOWN

- Whether a reporting workbook already exists outside this repository's tracked evidence (e.g. created manually by an operator). Not verifiable from this evidence pass without a workbook identifier, which is intentionally excluded.

*Related: [REPORTING-WORKBOOK-PRIVACY-v1.md](REPORTING-WORKBOOK-PRIVACY-v1.md), [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md).*
