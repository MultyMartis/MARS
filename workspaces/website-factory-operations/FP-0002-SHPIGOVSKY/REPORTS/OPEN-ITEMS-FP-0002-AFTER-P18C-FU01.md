# OPEN-ITEMS — FP-0002 AFTER PROD-P18C-FU01

Statuses reflect P18C-FU01 Admin menu exposure (2026-08-19).

P18C built SMTP/forms/leads internals. **P18C-FU01** made **Настройки сайта → Почта и формы** actually visible in the left menu. Do **not** reopen completed NS, `home`/`siteurl`, legal DEMO owner, indexing-control implementation, or lead-table schema.

## DONE / ACCEPTED (this wave)

| Item | Status |
|------|--------|
| Admin menu exposure for Почта и формы | DONE — visible after SEO, parent `fp02-site-settings-general` |
| One registration owner `MailFormsSettings` | DONE |
| Leads **Заявки** reachable | VERIFIED |
| SMTP still NOT CONFIGURED | VERIFIED |
| Mail suppression ON | VERIFIED |
| Indexing CLOSED | VERIFIED `blog_public=0` |
| Core `0.3.13-p18c-fu01` | DEPLOYED 4/4 MATCH |

## REMAINING operational sequence

| # | Item | Status |
|---|------|--------|
| 1 | Operator enters SMTP host/port/encryption/username/password + recipients in **Почта и формы**, then Save | **OPERATOR ACTION** — next |
| 2 | SMTP verification test (explicit Admin action) | AFTER settings saved |
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

## Sequence now

P18C foundation + P18C-FU01 menu discoverability DONE (credentials not entered; suppression ON; indexing CLOSED)  
→ operator SMTP + recipients in Admin  
→ SMTP verification  
→ real form delivery QA  
→ public-domain final smoke if still needed  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
