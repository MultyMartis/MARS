# OPEN-ITEMS — FP-0002 AFTER PROD-P18C

Statuses reflect P18C SMTP / forms Admin foundation (2026-08-19).

P18B indexing control and P18A live-domain intake remain. Do **not** reopen completed NS, `home`/`siteurl`, legal DEMO owner, or indexing-control implementation.

## DONE / ACCEPTED (this wave)

| Item | Status |
|------|--------|
| One Admin owner: Настройки сайта → Почта и формы | DONE |
| SMTP field model + write-only password | DONE — password **NOT CONFIGURED** until operator enters it |
| Sender default `noreply@shpigovsky.ru` | DONE |
| Single PHPMailer SMTP transport owner | DONE — not active until verified + operator activate |
| Internal lead table `fp02_form_leads` + persist-before-mail | DONE / QA PASS (QA row deleted) |
| Admin **Заявки** list / detail / filters / stats | DONE |
| Metrika goal Admin field; counter remains SEO owner | DONE — goal empty; counter not duplicated |
| Goal fire only after backend-confirmed success | DONE in JS |
| Mail suppression remains ON | VERIFIED |
| Indexing remains CLOSED | VERIFIED `blog_public=0` |
| Core `0.3.12-p18c` | DEPLOYED 14/14 MATCH |
| FORM LEAD RETENTION PERIOD | SURFACED — operator decision required (0 days = no auto-delete) |

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

P18C SMTP / FORMS FOUNDATION DONE (credentials not entered; suppression ON; indexing CLOSED)  
→ operator SMTP + recipients in Admin  
→ SMTP verification  
→ real form delivery QA  
→ public-domain final smoke if still needed  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
