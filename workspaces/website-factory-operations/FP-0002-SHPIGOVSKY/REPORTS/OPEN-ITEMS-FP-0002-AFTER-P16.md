# OPEN-ITEMS — FP-0002 AFTER PROD-P16

Statuses reflect P16 typography residual closeout (2026-08-17).

## DONE / ACCEPTED

| Item | Status |
|------|--------|
| P07–P13-FU01 product UI | ACCEPTED |
| P14 stabilization / baseline / git checkpoint | ACCEPTED |
| P06 / P15 environment & migration cleanup | ACCEPTED |
| **P16 typography residual** | **DONE (this wave)** |

## DEFERRED / FUTURE (real remaining)

| # | Item | Status |
|---|------|--------|
| 1 | PRE-CUTOVER audit | FUTURE |
| 2 | Final domain / DNS / SSL / siteurl/home / canonical | FUTURE / FINAL CUTOVER |
| 3 | SMTP (after domain/DNS) | FUTURE |
| 4 | robots/indexing opening | FUTURE / FINAL CUTOVER |
| 5 | Sitemap submission Yandex/Google | FUTURE |
| 6 | Final production crawl | FUTURE |

## Intentionally retained until later waves

| Item | Until |
|------|-------|
| siteurl/home on shpigovsky.beget.tech | domain cutover |
| blog_public=0 + robots Disallow | indexing open |
| `fp02-pre-cutover-mail-suppression.php` (`pre_wp_mail`) | SMTP wave |
| Temporary host hardcoded content URLs (beget) | domain cutover |

## Recommended sequence

PRE-CUTOVER → domain/DNS/SSL → SMTP → robots/indexing → sitemap submissions → final crawl
