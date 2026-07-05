# FP-0002 V9-06D9L Admin Issue Baseline Diagnostic v1

**Date:** 2026-07-05  
**Task:** V9-06D9-L

## Root cause summary

Home page #4 edit screen showed an empty Gutenberg block editor because:

1. **Classic Editor was not installed** — block editor was active for pages and for post ID 4.
2. **ACF field groups were not synced to DB** — 13 groups existed in `wp-content/acf-json/` but `acf-field-group` post count was 0. Local JSON registration allowed frontend reads, but admin metabox visibility required DB registration after Classic Editor activation.

## Baseline state

| Check | Before state |
|---|---|
| WordPress | 7.0 |
| Theme | shpigovsky |
| Classic Editor | Not installed |
| Block editor (Home #4) | Active |
| Block editor (pages) | Active |
| ACF PRO | Active |
| ACF JSON local groups | 13 |
| ACF DB groups | 0 |
| Pending ACF sync | 13 |
| Home ACF values | Seeded (D9-I/D9-K) — intact |
| Front page | page #4 |

## Location rule note

`group_fp02_page_home` uses `page_type == front_page`, not explicit page ID. This is correct because `page_on_front = 4`.

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/admin-issue-baseline-diagnostic.json`
