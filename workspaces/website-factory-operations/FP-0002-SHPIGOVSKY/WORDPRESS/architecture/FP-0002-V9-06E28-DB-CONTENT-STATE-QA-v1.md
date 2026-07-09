# FP-0002 V9-06E28 DB Content State QA

**Date:** 2026-07-09  
**Result:** PASS  
**Mode:** READ_ONLY

## Object counts

| Type | publish | trash | other |
|---|---:|---:|---|
| page | 15 | 8 | auto-draft 1 |
| post | 1 | — | — |
| service | 17 | — | — |
| nav_menu_item | 13 | — | — |

## Validation checks

| Check | Result | Notes |
|---|---|---|
| front_page_4_publish | PASS |  |
| privacy_page_3_publish | PASS |  |
| blog_archive_19_publish | PASS |  |
| demo_post_750_publish | PASS |  |
| service_73_publish | PASS |  |
| service_77_publish | PASS |  |
| service_84_publish | PASS |  |
| service_74_publish | PASS |  |
| page_9_trash | PASS |  |
| page_10_trash | PASS |  |
| page_17_trash | PASS |  |
| page_21_trash | PASS |  |
| page_25_trash | PASS |  |
| page_6_trash | PASS |  |
| page_7_trash | PASS |  |
| page_8_trash | PASS |  |
| page_on_front_is_4 | PASS |  |
| page_for_posts_is_19 | PASS |  |
| privacy_option_is_3 | PASS |  |
| permalink_blog_postname | PASS | /blog/%postname%/ |
| blog_public_recorded | PASS | 0 |
| critical_mojibake_absent | PASS |  |

## Options snapshot

| Option | Value |
|---|---|
| page_on_front | 4 |
| page_for_posts | 19 |
| permalink_structure | `/blog/%postname%/` |
| blog_public | 0 |
| wp_page_for_privacy_policy | 3 |

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/db-content-state-qa.json`
