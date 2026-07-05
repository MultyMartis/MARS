# FP-0002 V9-06D9O Baseline Required Field Diagnostic v1

**Date:** 2026-07-05  
**Task:** V9-06D9-O

## Summary

Baseline read-only diagnostic for `home_reviews_teaser` in `group_fp02_page_home` before repair.

## Findings

| Check | Result |
|-------|--------|
| Field group | `group_fp02_page_home` (DB post ID 114) |
| Field key | `field_fp02_home_reviews_teaser` (DB post ID 128) |
| Field label | Reviews teaser |
| Field type | repeater |
| Canonical JSON `required` | 0 |
| Canonical JSON `min` | 0 |
| DB field post `required` | 0 |
| DB field post `min` | 0 |
| Runtime JSON before repair | **MISSING** |
| Home #4 value empty | No (operator test row count = 1) |
| Other required fields blocking Home group | None |
| D9-I/D9-H deferral | `SKIP_PRODUCTION_REVIEW` |

## Root cause hypothesis

Canonical Git JSON and DB schema already define the field as optional. Runtime drift: `wp-content/acf-json/group_fp02_page_home.json` was absent after D9-H delivery, leaving ACF JSON load path incomplete relative to documented architecture.

Evidence: `validation/v9-06d9o-acf-reviews-teaser-required-flag-repair/baseline-required-field-diagnostic.json`
