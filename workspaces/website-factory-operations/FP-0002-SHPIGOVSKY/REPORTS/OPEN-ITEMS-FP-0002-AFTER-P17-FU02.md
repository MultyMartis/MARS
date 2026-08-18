# OPEN-ITEMS — FP-0002 AFTER PROD-P17-FU02

Statuses reflect P17-FU02 final pre-cutover tail closure (2026-08-18).

Internal WordPress/MARS tails from P06–P16 and P17 discovery are **closed**.

## DONE / ACCEPTED

| Item | Status |
|------|--------|
| P07–P16 product / env / typography | ACCEPTED |
| P17 PRE-CUTOVER + CONT1 legacy 301s + DNS inventory | ACCEPTED |
| **P17-FU02 internal pre-cutover tails** | **DONE (this wave)** |
| `mars-runtime/` public leftover | REMOVED (obsolete + security) |
| Public webroot hygiene | PASS |
| Production users/admin set | CLEAN |
| 7/7 legacy redirects | PASS |
| Cutover DB/file mutation plans | EXECUTABLE WITHOUT DISCOVERY |
| Freeze + manual NS handoff runbooks | READY |

## REMAINING (launch sequence only)

| # | Item | Status |
|---|------|--------|
| 1 | **MANUAL NS SWITCH** in REG.RU (after freeze + fresh backup) | OPERATOR ACTION REQUIRED |
| 2 | Final DNS verification (delegation, A/www/MX/TXT) | WAITING FOR NS SWITCHED |
| 3 | SSL / final domain (`home`/`siteurl` + exact URL migration) | P18 |
| 4 | SMTP | P18 PHASE B |
| 5 | robots / indexing opening | P18 PHASE C |
| 6 | Sitemap submissions (Yandex / Google) | P18 |
| 7 | Final crawl | P18 |

## Intentionally retained until P18

| Item | Until |
|------|-------|
| siteurl/home on shpigovsky.beget.tech | domain cutover |
| blog_public=0 + robots Disallow | indexing open after SMTP smoke |
| `fp02-pre-cutover-mail-suppression.php` | SMTP wave |
| Temporary-host absolute URLs listed in the mutation plan | domain cutover |
| Current public NS `ns1/ns2.hosting.reg.ru` | operator NS switch |
| P14 full backup as last complete dump | **must be replaced** after freeze |

## Sequence

freeze → fresh backup → **operator NS switch** → DNS verify → SSL → siteurl/URLs → smoke (indexing closed) → SMTP → forms → robots/indexing → sitemaps → crawl
