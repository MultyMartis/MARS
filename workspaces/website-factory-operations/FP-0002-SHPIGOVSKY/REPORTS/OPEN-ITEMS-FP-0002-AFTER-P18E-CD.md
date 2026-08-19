# OPEN-ITEMS — FP-0002 AFTER PROD-P18E-C/D

Statuses reflect fresh P18E-C/D deploy + live QA on 2026-08-19.

## DONE / ACCEPTED

| Item | Status |
|------|--------|
| Public cookie notice with `Принять` / `Только необходимые` / `Настроить` | LIVE |
| Versioned fail-closed browser record `fp02_cookie_consent` | LIVE |
| Analytics allowed only after explicit consent | VERIFIED |
| Necessary-only / undecided / tampered / old-version analytics blocking | VERIFIED |
| Yandex Metrika unconditional theme/bootstrap path removed | LIVE |
| `custom_head_code` / `custom_footer_code` Metrika bypass stripped at render time | LIVE |
| `noscript` Metrika bypass removed from theme owner path | LIVE |
| Contacts-page Yandex map embed no longer auto-loads third-party tracking before consent | LIVE |
| Dashboard truth updated to active consent + consent-gated analytics | LIVE |
| Indexing remains closed | VERIFIED |

## Remaining operational sequence

| # | Item | Status |
|---|------|--------|
| 1 | P18E-E/F form-goal consent gating + permanent footer/privacy reopen entry | NEXT |
| 2 | Consent withdrawal/policy integration copy polish | WITH P18E-E/F |
| 3 | Server-side consent evidence model | DEFERRED LEGAL / OPERATOR DECISION |
| 4 | Olya indexing approval | REQUIRED before any opening |
| 5 | Sitemap submissions | AFTER indexing opens |
| 6 | Final crawl | LAST |

## Open legal / product decisions

| Item | Status |
|------|--------|
| Consent evidence model beyond browser-state cookie | LEGAL / OPERATOR DECISION REQUIRED |
| Consent lifetime policy beyond current product default `365` days | PRODUCT / LEGAL POLICY DECISION REQUIRED |
| Evidence retention policy if server-side evidence is later added | DEFERRED |
| Final Cookie Policy legal text | NEEDS LEGAL CONTENT REVIEW |
| Final treatment of `sessionStorage['fp02_utm']` in public legal text | LEGAL / OPERATOR REVIEW REQUIRED |

## Intentionally preserved

| Item | Until |
|------|-------|
| `blog_public=0` + `robots.txt` `Disallow: /` | Olya / explicit operator indexing approval |
| Existing Metrika form-goal JS helper harmless no-op on missing `window.ym` | P18E-E |
| Current legal/editorial DB content | changed only by operator/editor intent |

## Sequence now

P18E-A/B foundation live  
→ **P18E-C/D public notice + consent-gated Metrika live**  
→ **P18E-E/F goal gating + withdrawal/policy entry**  
→ Olya indexing approval  
→ sitemap submissions  
→ final crawl
