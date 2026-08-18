# OPEN-ITEMS — FP-0002 AFTER PROD-P17 CONT1

Statuses reflect P17 PRE-CUTOVER + CONT1 (2026-08-18).

## DONE / ACCEPTED

| Item | Status |
|------|--------|
| P07–P16 product / env / typography | ACCEPTED |
| **P17 PRE-CUTOVER + legacy 301s + DNS inventory** | **DONE (this wave)** |

## DEFERRED / FUTURE (real remaining)

| # | Item | Status |
|---|------|--------|
| 1 | Prepare Beget DNS zone in panel (copy MX/SPF/mail hosts; replace website A) | OPERATOR / BEFORE NS |
| 2 | Final NS switch + SSL + siteurl/home / canonical | FUTURE / FINAL CUTOVER |
| 3 | SMTP (after domain/DNS/SSL) | FUTURE |
| 4 | robots/indexing opening | FUTURE / FINAL CUTOVER |
| 5 | Sitemap submission Yandex/Google | FUTURE |
| 6 | Final production crawl | FUTURE |

## Intentionally retained until later waves

| Item | Until |
|------|-------|
| siteurl/home on shpigovsky.beget.tech | domain cutover |
| blog_public=0 + robots Disallow | indexing open |
| `fp02-pre-cutover-mail-suppression.php` | SMTP wave |
| Temporary host hardcoded content URLs (beget) | domain cutover |
| Current public NS `ns1/ns2.hosting.reg.ru` | NS cutover charter |

## Recommended sequence

legacy redirects DONE → Beget zone prep → NS → SSL → siteurl → smoke (indexing closed) → SMTP → forms → robots/indexing → sitemaps → crawl
