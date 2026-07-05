# FP-0002 V9-06D9-S Controlled Reviews Options Seed Report

**Phase:** V9-06D9-S  
**Date:** 2026-07-06  
**Verdict:** PARTIAL PASS

---

## Summary

Controlled seed applied 10 review rows from static V9 fallback into ACF Options (`reviews_enabled`, `reviews_section_heading`, `reviews_items`). DB checkpoint created before writes. Home #4 and orphan teaser meta unchanged. Frontend still uses **FALLBACK** because runtime ACF resolves `reviews_items` subfields to legacy `author_label`/`text` (field key collision with page reviews group); D9-R helper reads `review_author`/`review_text` only. Visual output preserved (10 slides, ALL_200 routes).

---

## Safety preflight

| Check | Result |
|-------|--------|
| Volume X / AI WS | PASS |
| Branch `mars/canonical-post-recovery` | PASS |
| Local HEAD | `a129f7083ad6b45f8f3f3a616169fab8c413495c` |
| Remote HEAD | `a129f7083ad6b45f8f3f3a616169fab8c413495c` |
| Required D9-R HEAD | `a84ec2e8032bf4409538b32885566a7e1fe6f4d8` (ancestor) |
| Ahead / Behind | 0 / 0 |
| Strict HEAD gate | PARTIAL — tip advanced; D9-R ancestor verified |
| Foreign WIP | Present; excluded from staging |
| Pre-existing staged files | None |

---

## Seed results

| Area | Result |
|------|--------|
| DB checkpoint | PASS |
| Options seed apply | PASS — 3 top-level fields |
| DB verification | PASS — 10 rows, enabled, heading |
| Admin validation | PASS — DB evidence; screenshots PARTIAL |
| Frontend validation | PARTIAL — 10 slides, source mode FALLBACK |
| No-scope-drift | PASS — 0 source/theme/JSON changes |
| Screenshots | PARTIAL — headless run |

---

## Blocker

**ACF field key collision:** `field_fp02_reviews_items` used by both `group_fp02_page_reviews` and `group_fp02_site_options_reviews`. Runtime subfields: `author_label`, `text`, `metadata`, `source`. Helper expects `review_author`, `review_text`. Options rows are populated in admin/DB but not consumed on frontend.

---

## DB checkpoint

`X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9s-controlled-reviews-options-seed-pre-20260706-005734/`

Evidence: `validation/v9-06d9s-controlled-reviews-options-seed/db-checkpoint.json`

---

## Recommended next action

**OPERATOR_DECISION_REQUIRED** — authorize D9-T schema key fix + helper normalization before admin visual QA.

---

## Safety statement

Target folder: `X:\AI MARS`  
V9-06D9-S performed: PARTIAL  
Database checkpoint: YES  
Reviews options seeded: YES (10 rows)  
Source mode after seed: FALLBACK  
Source/theme changes: 0  
ACF JSON changes: 0  
Runtime delivery: NO  
Production migration: NO
