# OPEN-ITEMS — FP-0002 AFTER PROD-P18C-FU02

Statuses reflect P18C-FU02 multi-recipient Admin UX (2026-08-19).

P18C built SMTP/forms/leads internals. P18C-FU01 made **Почта и формы** visible. **P18C-FU02** added Add/Remove recipient rows. Operator SMTP credentials are stored. Do **not** reopen completed NS, `home`/`siteurl`, legal DEMO owner, indexing-control implementation, or lead-table schema.

## DONE / ACCEPTED (this wave)

| Item | Status |
|------|--------|
| Multi-recipient Admin UX (Add / Remove) | DONE |
| Existing recipient preserved 1:1 | VERIFIED `client.leads@polygon-ws.ru` / MetaCODE |
| SMTP non-secret fields preserved | VERIFIED |
| Password remains CONFIGURED | VERIFIED YES |
| Save/reload QA cases 1–5 | PASS |
| Mail suppression ON | VERIFIED |
| SMTP NOT VERIFIED | VERIFIED |
| Indexing CLOSED | VERIFIED `blog_public=0` |
| Core `0.3.14-p18c-fu02` | DEPLOYED 8/8 MATCH |

## REMAINING operational sequence

| # | Item | Status |
|---|------|--------|
| 1 | Operator adds remaining business recipients in **Почта и формы**, then Save | **OPERATOR ACTION** — next |
| 2 | SMTP verification test (explicit Admin action) | AFTER recipients ready |
| 3 | Operator activates real outbound delivery | AFTER verified |
| 4 | Real form delivery QA | AFTER activation |
| 5 | Bind public `https://shpigovsky.ru/` to **this** WordPress origin (public apex still observed as **Craftum CMS**) | OPEN — public-origin smoke |
| 6 | Indexing open | **ONLY after Olya approval** or explicit operator command |
| 7 | Sitemap submissions | AFTER indexing open — not automatic |
| 8 | Final crawl | LAST |

## Intentionally retained

| Item | Until |
|------|-------|
| `blog_public=0` + WP origin robots `Disallow: /` | Olya / explicit operator indexing approval |
| `fp02-pre-cutover-mail-suppression.php` | SMTP VERIFIED + operator activates sending (then retire MU) |
| Temporary-host → final-domain 301 | after public apex stably serves WordPress |
| Cookie page `#24` analytics DEMO copy | OPERATOR CONTENT REQUIRED |
| Form lead retention days = 0 | OPERATOR DECISION REQUIRED |
| Personal-data export/erase by **email** | implemented; phone-only leads = follow-up |
| SMTP encryption stored as `none` with port `465` | OPERATOR REVIEW (not changed in FU02) |

## Sequence now

P18C foundation + P18C-FU01 menu + P18C-FU02 multi-recipient UX DONE (credentials stored; not verified; suppression ON; indexing CLOSED)  
→ operator confirms all recipients + Save  
→ SMTP verification  
→ real form delivery QA  
→ public-domain final smoke if still needed  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
