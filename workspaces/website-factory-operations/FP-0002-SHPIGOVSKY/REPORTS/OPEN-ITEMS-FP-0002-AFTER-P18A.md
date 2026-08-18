# OPEN-ITEMS — FP-0002 AFTER PROD-P18A

Statuses reflect P18A live-domain reality intake + legal demo-state fix (2026-08-18).

P17 historical reports are unchanged. NS and WordPress `home`/`siteurl` are **no longer pending**.

## DONE / ACCEPTED (this wave)

| Item | Status |
|------|--------|
| Operator live-domain cutover intake (`home`/`siteurl` = `https://shpigovsky.ru`) | CANONIZED |
| Public NS delegation to Beget | OBSERVED (system resolver: Beget NS set) |
| Legal DEMO banner owner | FIXED — `legal_demo_marker` explicit false preserved |
| Indexing remains closed (`blog_public=0`, robots `Disallow: /`) | VERIFIED |
| Mail suppression MU | STILL PRESENT (correct) |

## REMAINING launch sequence

| # | Item | Status |
|---|------|--------|
| 1 | **SSL finalize** + bind public apex/www to the **WordPress** origin | IN PROGRESS / NOT FINAL |
| 2 | Final-domain HTTPS smoke (WordPress on `https://shpigovsky.ru/`) | PENDING — public A still served a **legacy** origin at intake |
| 3 | Canonical / www / temporary-host redirects after smoke | READY TO PLAN; **not** activated |
| 4 | Exact remaining URL cleanup (robots sitemap host still `shpigovsky.beget.tech`; bounded P17 manifest) | AFTER HTTPS PASS |
| 5 | SMTP | PENDING |
| 6 | Form delivery QA | AFTER SMTP |
| 7 | robots / indexing open | AFTER SMTP + HTTPS smoke |
| 8 | Sitemap submissions | AFTER indexing open |
| 9 | Final crawl | LAST |

## Intentionally retained

| Item | Until |
|------|-------|
| `blog_public=0` + robots Disallow | indexing gate |
| `fp02-pre-cutover-mail-suppression.php` | SMTP wave |
| Temporary-host → final-domain 301 | after WordPress HTTPS PASS (no loop) |
| Cookie page `#24` `[ДЕМО: перечень подключённых систем аналитики]` | OPERATOR CONTENT REQUIRED |
| P14 full backup as last complete dump | replace after next freeze if a large mutation wave needs it |

## Sequence now

CURRENT LIVE DOMAIN (WP URLs + NS done)  
→ SSL finalize / public A → WordPress  
→ final-domain HTTPS smoke  
→ host/canonical/temp-host redirects  
→ exact remaining URL cleanup  
→ cache/rewrite  
→ SMTP  
→ form delivery QA  
→ robots/indexing  
→ sitemap submissions  
→ final crawl
