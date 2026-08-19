# OPEN-ITEMS — FP-0002 AFTER PROD-P18E-A/B

Statuses reflect fresh P18E-A intake plus live P18E-B foundation deploy on 2026-08-19.

## DONE / ACCEPTED

| Item | Status |
|------|--------|
| Fresh Olya/Admin production truth re-intake | VERIFIED |
| Fresh tracker/storage reality recheck | VERIFIED |
| Bounded legal/provider baseline recheck | VERIFIED |
| `PrivacyConsent` core owner in `shpigovsky-core` | LIVE |
| Explicit consent states + version contract | LIVE |
| `Настройки сайта → Cookie и конфиденциальность` discoverable | PASS |
| Consent foundation Dashboard truth update | LIVE |
| Public Metrika loading intentionally unchanged | VERIFIED |
| Current form-goal runtime intentionally unchanged | VERIFIED |
| Indexing remains closed | VERIFIED |

## Remaining operational sequence

| # | Item | Status |
|---|------|--------|
| 1 | P18E-C/D public cookie notice + real Metrika consent-gating | NEXT |
| 2 | P18E-E/F form-goal consent gating + withdrawal/policy integration | AFTER P18E-C/D |
| 3 | Public-domain finalization | ONLY IF regression appears |
| 4 | Olya indexing approval | REQUIRED before any opening |
| 5 | Sitemap submissions | AFTER indexing opens |
| 6 | Final crawl | LAST |

## Open legal / product decisions

| Item | Status |
|------|--------|
| Consent evidence model beyond browser-state foundation | LEGAL / OPERATOR DECISION REQUIRED |
| Consent lifetime policy beyond current product default `365` days | PRODUCT / LEGAL POLICY DECISION REQUIRED |
| Evidence retention policy if server-side evidence is later added | DEFERRED |
| Final Cookie Policy legal text | NEEDS LEGAL CONTENT REVIEW |
| Final treatment of `sessionStorage['fp02_utm']` in public legal text | LEGAL / OPERATOR REVIEW REQUIRED |

## Intentionally preserved

| Item | Until |
|------|-------|
| `blog_public=0` + `robots.txt` `Disallow: /` | Olya / explicit operator indexing approval |
| Existing Metrika counter source in SEO / integrations | P18E-D actual gating wave |
| Current form-goal runtime | P18E-E |
| Current legal/editorial DB content | changed only by operator/editor intent |

## Sequence now

P18D-FU01 SMTP closeout  
→ P18E design  
→ **P18E-A/B foundation live**  
→ **P18E-C/D public notice + gating**  
→ **P18E-E/F goal gating + withdrawal/policy**  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
