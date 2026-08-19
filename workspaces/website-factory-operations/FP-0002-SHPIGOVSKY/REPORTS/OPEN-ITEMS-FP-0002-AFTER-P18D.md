# OPEN-ITEMS — FP-0002 AFTER PROD-P18D-FU01

Statuses reflect fresh runtime intake plus actual FU01 closeout on 2026-08-19.

## DONE / ACCEPTED

| Item | Status |
|------|--------|
| Olya/Admin editorial DB changes treated as current production truth | VERIFIED |
| Fresh production file/code intake performed before mutation | VERIFIED |
| SMTP transport mismatch corrected: `none -> ssl` on port `465` | CORRECTED |
| SMTP test pass | VERIFIED |
| SMTP state `VERIFIED / ACTIVE` | ACHIEVED |
| Pre-cutover suppression MU physically removed | DONE |
| Post-removal QA form/mail smoke | PASS |
| Exact QA lead cleanup | DONE |
| Indexing re-closed after fresh intake detected live `blog_public=1` | DONE |
| Public `https://shpigovsky.ru/` currently serves WordPress | VERIFIED |

## Remaining operational sequence

| # | Item | Status |
|---|------|--------|
| 1 | P18E implementation charter from fresh runtime intake | READY AFTER operator/legal approval of P18E design |
| 2 | Public-domain finalization | OPEN only if operator later sees a routing regression |
| 3 | Olya indexing approval | REQUIRED before any opening |
| 4 | Sitemap submissions | AFTER indexing opens |
| 5 | Final crawl | LAST |

## Open business decision

| Item | Status |
|------|--------|
| Form lead retention days (`lead_retention_days=0`) | OPERATOR DECISION REQUIRED |
| Cookie/privacy implementation evidence model (browser-only vs hybrid/server event) | LEGAL / OPERATOR REVIEW REQUIRED |
| Consent lifetime / re-prompt policy | PRODUCT / LEGAL POLICY DECISION REQUIRED |

## Intentionally preserved

| Item | Until |
|------|-------|
| `blog_public=0` + `robots.txt` `Disallow: /` | Olya / explicit operator indexing approval |
| Current Admin-managed recipients | changed only by operator/editor intent |
| Current editorial/legal/services/specialists DB content | live production truth |
| Current SEO/Metrika settings owner | preserved until an explicit P18E implementation wave |

## Sequence now

P18C foundation  
→ P18C-FU01 admin menu  
→ P18C-FU02 recipient UX  
→ P18D technical intent  
→ **P18D-FU01 actual runtime closeout**  
→ **P18E consent/privacy design complete (no runtime mutation)**  
→ operator/legal approval for P18E implementation scope  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
