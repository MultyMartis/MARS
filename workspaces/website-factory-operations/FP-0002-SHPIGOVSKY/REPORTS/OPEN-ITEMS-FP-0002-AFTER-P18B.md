# OPEN-ITEMS — FP-0002 AFTER PROD-P18B

Statuses reflect P18B Dashboard reality sync + safe indexing control (2026-08-19).

P18A / P17 historical reports are unchanged. Do **not** reopen completed NS, `home`/`siteurl`, legacy 7/7 redirects, or legal DEMO owner.

## DONE / ACCEPTED (this wave)

| Item | Status |
|------|--------|
| MetaCODE Dashboard reflects current operator-visible production truth (no stale “future host” / “NS pending”) | DONE |
| Safe Admin indexing control (`SET SITE INDEXABILITY`) | DONE |
| Indexing remains **CLOSED** after reversible QA | VERIFIED |
| Olya (`admin`, Administrator) can use the control (`manage_options`) | VERIFIED |
| SMTP mailbox `noreply@shpigovsky.ru` exists at host | OPERATOR FACT |
| Fresh Beget backup | CONFIRMED BY OPERATOR |
| Core `0.3.11-p18b` | DEPLOYED 6/6 MATCH |

## REMAINING operational sequence

| # | Item | Status |
|---|------|--------|
| 1 | Bind public `https://shpigovsky.ru/` to **this** WordPress origin (public apex currently observed as **Craftum CMS**) | OPEN — before SMTP |
| 2 | SMTP configuration using `noreply@shpigovsky.ru` | PENDING — do not remove mail suppression until then |
| 3 | Real form delivery QA | AFTER SMTP |
| 4 | Yandex Metrika JS goals for forms | AFTER delivery QA — fire only on **backend-confirmed success**, not button click |
| 5 | Internal WordPress form lead statistics / lead registry | SEPARATE FORMS WAVE — not started |
| 6 | Indexing open | **ONLY after Olya approval** or explicit operator command |
| 7 | Sitemap submissions | AFTER indexing open — not automatic |
| 8 | Final crawl | LAST |

## Future forms wave (record only — not implemented in P18B)

**A. Metrika goals**

- Admin-configurable Yandex Metrika JS goal per form / form type.
- Fire rule: **BACKEND CONFIRMED SUCCESS → frontend JS goal fire**.
- Do **not** fire on button click alone.

**B. Internal lead registry**

Expected information model (to design later):

- timestamp
- form
- source page
- delivery status
- safe contact data
- UTM if present
- Metrika goal status if useful

## Intentionally retained

| Item | Until |
|------|-------|
| `blog_public=0` + WP origin robots `Disallow: /` | Olya / explicit operator indexing approval |
| `fp02-pre-cutover-mail-suppression.php` | SMTP wave |
| Temporary-host → final-domain 301 | after public apex stably serves WordPress |
| Cookie page `#24` analytics DEMO copy | OPERATOR CONTENT REQUIRED |

## Sequence now

P18B DASHBOARD + INDEXING CONTROL DONE (indexing CLOSED)  
→ bind public apex to WordPress  
→ SMTP (`noreply@shpigovsky.ru`)  
→ form delivery QA  
→ Metrika form goals (backend-confirmed)  
→ internal form statistics  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
