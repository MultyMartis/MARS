# FP-0002 V9-06E27A Route Health And Placeholder Audit v1

**Evidence:** `validation/v9-06e27a-obsolete-pages-cleanup-read-only-audit/route-health-placeholder-audit.json`

## Summary

| Metric | Value |
|---|---:|
| Routes checked | 38 |
| HTTP 200 | 37 |
| HTTP 404 | 1 |

## Required routes

| Route | Status | Classification | Recommendation |
|---|---|---|---|
| `/` | 200 | canonical | KEEP |
| `/o-centre/` | 200 | canonical | KEEP (E26A) |
| `/blog/` | 200 | canonical | KEEP (E26B) |
| `/blog/nazvanie-stati/` | 200 | demo | KEEP_DEMO_LOCAL #750 |
| `/uslugi/` | 200 | canonical | KEEP |
| `/uslugi/zavisimosti/` | 200 | ownership_debt | OPERATOR_DECISION (page #6 vs service #73) |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | canonical | KEEP service #74 |
| `/kontakty/` | 200 | canonical | KEEP |
| `/otzyvy/` | 200 | canonical | KEEP |
| `/privacy-policy/` | 200 | canonical legal | MUST_NOT_TOUCH #3 |

## Cleanup / obsolete route markers

| Route | Status | Notes |
|---|---|---|
| `/uslugi/genotipirovanie/` | 404 | Page #9 obsolete; trash candidate |
| `/specyalisty/` | 200 | Page #10 orphan placeholder |
| `/privacy-policy-page/` | 200 | Page #25 duplicate privacy URL |
| `/o-centre/intervyu-i-smi/` | 200 | Page #17 not in V9 manifest |
