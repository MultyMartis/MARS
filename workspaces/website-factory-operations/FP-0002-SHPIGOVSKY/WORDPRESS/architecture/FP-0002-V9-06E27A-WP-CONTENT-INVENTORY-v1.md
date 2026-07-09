# FP-0002 V9-06E27A WP Content Inventory v1

**Wave:** V9-06E27A Obsolete Pages Cleanup Read-Only Audit  
**Date:** 2026-07-09  
**Evidence:** `validation/v9-06e27a-obsolete-pages-cleanup-read-only-audit/wp-content-inventory.json`

## Summary

| Object type | Total | Draft | Published | Private | Trash | Notes |
|---|---:|---:|---:|---:|---:|---|
| page | 24 | 1 | 22 | 0 | 0 | +1 auto-draft excluded from inventory |
| post | 1 | 0 | 1 | 0 | 0 | Demo post #750 |
| service | 17 | 0 | 17 | 0 | 0 | No E25 duplicate draft #746 present |
| nav_menu_item | 13 | 0 | 13 | 0 | 0 | Primary, Footer, Legal |
| acf-field-group | 47 | 0 | 43 | 0 | 3 | 3 trashed duplicate reviews groups |
| terms | 5 | — | — | — | — | Includes default category |

## Key options

| Option | Value |
|---|---|
| page_on_front | 4 |
| page_for_posts | 19 |
| permalink_structure | `/blog/%postname%/` |
| blog_public | 0 |
| wp_page_for_privacy_policy | 3 |

## Cleanup candidates (pages)

| ID | Path | Status | Category |
|---:|---|---|---|
| 9 | `/uslugi/genotipirovanie/` | publish | CLEANUP_CANDIDATE_TRASH (404) |
| 10 | `/specyalisty/` | publish | CLEANUP_CANDIDATE_TRASH |
| 17 | `/o-centre/intervyu-i-smi/` | publish | CLEANUP_CANDIDATE_TRASH |
| 21 | `/pravovaya-informaciya-pilzovatelyu/` | draft | CLEANUP_CANDIDATE_DRAFT |
| 25 | `/privacy-policy-page/` | publish | CLEANUP_CANDIDATE_TRASH |

## Ownership debt (operator decision)

| ID | Path | Conflicts with service CPT |
|---:|---|---|
| 6 | `/uslugi/zavisimosti/` | #73 |
| 7 | `/uslugi/psihicheskoe-zdorovie/` | #77 |
| 8 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | #84 |

## Must preserve

- Privacy canonical: page **#3**
- Front page: **#4**
- Blog posts page: **#19**
- Demo blog post: **#750** (`KEEP_DEMO_LOCAL`)
