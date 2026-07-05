# FP-0002 V9-06D9-M — Native Content Inventory v1

**Phase:** V9-06D9-M  
**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9m-native-page-content-cleanup/native-content-inventory.json`

## Summary

Inventory of all WordPress pages in `mars_wp_fp0002` (`fp02_posts`) for obsolete native `post_content`.

| Classification | Count | Page IDs |
|---|---:|---|
| CLEAN_POST_CONTENT (applied) | 13 | 4, 5, 11–16, 18, 20, 22–24 |
| OPERATOR_REVIEW_REQUIRED | 10 | 3, 6–10, 17, 19, 21, 25 |
| KEEP (empty) | 0 | — |

## Detection criteria applied

1. **Obsolete starter placeholder** — identical 431-byte garbled mojibake seed text containing `frontend handoff` signature (SHA-256 `0f00e812…`).
2. **Template-managed** — named `page-templates/*` or front page #4 (`front-page.php` + ACF).
3. **Not rendered on frontend** — theme partials/ACF drive output; native editor content unused.

## Operator-confirmed target

- **Home #4** — operator screenshot (D9-L) showed broken-encoding placeholder in Classic Editor native area.

## Deferred (OPERATOR_REVIEW_REQUIRED)

| ID | Title | Reason |
|---:|---|---|
| 3 | Политика конфиденциальности | Draft; 20 026 chars; different content (legal seed candidate) |
| 6–10 | Hub child stubs | Default `page.php` uses `the_content()` — not template-managed |
| 17 | Интервью и СМИ | Default template; `the_content()` path |
| 19 | Статьи | Default template |
| 21 | Правовая информация | Default template |
| 25 | Политика конфиденциальности (системная) | Default template |

## Frontend route mapping (cleaned pages)

| ID | Route | Template |
|---:|---|---|
| 4 | `/` | front-page (ACF) |
| 5 | `/uslugi/` | services-hub.php |
| 11 | `/o-centre/` | institutional.php |
| 20 | `/kontakty/` | contacts.php |
| 22–24 | legal slugs | legal.php |
