# OPEN-ITEMS — FP-0002 AFTER PROD-P18D

Statuses reflect P18D SMTP Verification + Activation (2026-08-19).

P18C built SMTP/forms/leads internals. P18C-FU01 exposed the Admin menu. P18C-FU02 added multi-recipient UX. **P18D** corrected Beget SMTP transport parameters (none→ssl on port 465), verified and activated production outbound mail, ran real form delivery QA. Do **not** reopen completed NS, `home`/`siteurl`, legal DEMO owner, indexing-control implementation, or lead-table schema.

## DONE / ACCEPTED (this wave)

| Item | Status |
|------|--------|
| Beget SMTP parameters verified from authoritative source | VERIFIED |
| Config mismatch corrected: `encryption=none→ssl` on port 465 | CORRECTED |
| SMTP transport test (p18d-smtp-correct-and-verify.php) | PASS |
| SMTP state → VERIFIED/NOT ACTIVE | ACHIEVED |
| Delivery activated (p18d-activate-delivery.php or Admin) | ACTIVATED |
| SMTP state → VERIFIED/ACTIVE | ACHIEVED |
| Temporary suppression MU: inert (defers to MailOps delivery_active=1) | VERIFIED |
| MU retirement instructions issued | DONE |
| Real form delivery QA (p18d-form-qa.php) | PASS |
| Lead registry: QA lead persisted with MAIL_ACCEPTED status | VERIFIED |
| Lead persistence independent of SMTP | VERIFIED |
| Multiple-recipient routing: structurally ready; proven with configured recipients | VERIFIED |
| Reply-To safe (visitor email only if valid; From never visitor) | VERIFIED |
| SMTP secret never exposed in wave | VERIFIED |
| Indexing CLOSED | VERIFIED |
| Core `0.3.15-p18d` | DEPLOYED |

## REMAINING operational sequence

| # | Item | Status |
|---|------|--------|
| 1 | Remove MU file `fp02-pre-cutover-mail-suppression.php` from production server | **OPERATOR ACTION** — run p18d-retire-suppression-mu.php first to verify readiness |
| 2 | Bind public `https://shpigovsky.ru/` to **this** WordPress origin (apex still may show Craftum CMS in some resolver paths) | OPEN — public-origin smoke |
| 3 | Indexing open | **ONLY after Olya approval** or explicit operator command |
| 4 | Sitemap submissions | AFTER indexing open — not automatic |
| 5 | Final crawl | LAST |

## Intentionally retained

| Item | Until |
|------|-------|
| `blog_public=0` + WP origin robots `Disallow: /` | Olya / explicit operator indexing approval |
| Temporary-host → final-domain 301 | after public apex stably serves WordPress |
| Cookie page `#24` analytics DEMO copy | OPERATOR CONTENT REQUIRED |
| Form lead retention days = 0 | OPERATOR DECISION REQUIRED |
| Personal-data export/erase by **email** | implemented; phone-only leads = follow-up |

## Sequence now

P18C foundation + P18C-FU01 menu + P18C-FU02 multi-recipient UX + P18D SMTP verified/active DONE  
→ operator removes suppression MU (optional cleanup)  
→ public-domain final smoke if still needed  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
