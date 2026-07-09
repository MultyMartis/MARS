# FP-0002 V9-06E28 ACF Admin Structure QA

**Date:** 2026-07-09  
**Result:** PARTIAL

## ACF state

| Item | Value |
|---|---|
| ACF PRO active | True |
| Field groups registered | 44 |
| Runtime ACF JSON files | 8 |
| Removed Global Heroes / reviews alias | not detected |

## Spot checks

| Scope | Field | Result | Notes |
|---|---|---|---|
| page_11_o_centre | `institutional_intro` | WARN | empty=True |
| page_11_o_centre | `institutional_blocks` | WARN | empty=True |
| page_11_o_centre | `institutional_team` | WARN | empty=True |
| page_19_blog_archive | `blog_archive_intro` | PASS | empty=False |
| page_19_blog_archive | `blog_archive_featured` | WARN | empty=True |
| post_750_demo | `article_intro` | WARN | empty=True |
| post_750_demo | `article_body` | WARN | empty=True |
| post_750_demo | `article_conclusion` | WARN | empty=True |
| post_750_demo | `article_sources` | WARN | empty=True |
| post_750_demo | `article_cta` | WARN | empty=True |
| service_73 | `hero_lead` | PASS | empty=False |
| service_73 | `programme_items` | PASS | empty=False |
| service_73 | `stages` | PASS | empty=False |
| service_73 | `faq_items` | PASS | empty=False |
| service_74 | `intro_note` | PASS | empty=False |
| service_74 | `signs_items` | PASS | empty=False |
| service_74 | `programme_items` | PASS | empty=False |

## Finding

`/o-centre/` page `#11` institutional ACF fields (`institutional_intro`, `institutional_blocks`, `institutional_team`) are empty in DB but page renders via template/runtime content from E26A port. Classified **MINOR** — admin seed gap, not route blocker.

Blog archive `#19`, demo post `#750`, and service structured fields PASS spot checks.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/acf-admin-structure-qa.json`
