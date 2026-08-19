# REPORT — FP-0002 PROD-P18E-A/B Cookie Consent Foundation

**Date:** 2026-08-19  
**Evidence:** `REPORTS/evidence/prod-p18e-ab-consent-foundation/`

## 1. Status

**PASS**

P18E-A fresh production/privacy/legal/tracker intake was re-run before mutation. P18E-B then shipped the first live consent foundation in production without changing visitor-facing behavior.

## 2. Olya/Admin Intake

**P18E-A CURRENT OLYA / ADMIN PRODUCTION TRUTH VERIFIED**

- Current WP/Admin DB state was treated as canonical truth.
- No old DB snapshot was restored.
- Production legal/editorial/settings content remained preserved.

## 3. Tracker Reality

**P18E-A TRACKER / STORAGE REALITY RECONFIRMED**

- Home and contacts still load Yandex Metrika immediately.
- `sessionStorage['fp02_utm']` runtime owner remains the theme shell path.
- Current cookie-related legal pages still exist in production.
- No new tracker class surfaced that forced a model change in this wave.

## 4. Legal / Provider Recheck

**P18E-A LEGAL / PROVIDER BASELINE STILL VALID**

- No material Russian-law/provider blocker appeared that invalidates the approved P18E design.
- Yandex Metrika deferred loading / storage / opt-out capabilities remain compatible with the later gating wave.
- Server-side consent evidence remains a deferred legal/operator choice.

## 5. Core Owner

**ONE COOKIE CONSENT CORE OWNER**

- Production owner: `Shpigovsky\Core\Privacy\PrivacyConsent`
- Scope: states, version, browser record contract, cookie attributes, settings, integration registry, status surface

## 6. Consent State

- `UNDECIDED`
- `NECESSARY_ONLY`
- `ANALYTICS_ALLOWED`

Necessary remains always true; impossible `necessary=false` is rejected.

## 7. Consent Version

**CONSENT VERSION CONTRACT IMPLEMENTED**

- Current version: `1`
- Older valid records are treated as `requires_redecision=true`

## 8. Browser Record

- Key: `fp02_cookie_consent`
- Schema: `version`, `necessary`, `analytics`, `decided_at`
- Format: compact JSON
- Validation: known keys only, integer version, strict booleans, bounded timestamp
- Tampered / unknown payload -> `UNDECIDED`
- Cookie attributes contract: `Secure` on HTTPS, `SameSite=Lax`, `Path=/`, bounded `Max-Age`, `HttpOnly=false`

## 9. Evidence Model

**NO UNAPPROVED CONSENT TRACKING DATABASE CREATED**

Actual P18E-A/B decision: **browser-only foundation / deferred legal decision**.

## 10. Admin

**COOKIE / PRIVACY ADMIN DISCOVERABILITY PASS**

Path: `Настройки сайта → Cookie и конфиденциальность`

- submenu visible once under the real Site Settings parent;
- page renders Banner / Categories / Integrations / State sections;
- save/reload persistence proven in production;
- no English debug label leakage in the normal editor surface.

## 11. Integrations

- `Yandex Metrika -> analytics`
- existing counter source of truth preserved in `SEO и интеграции`
- no duplicate counter-id owner introduced

## 12. Runtime Boundaries

**P18E-B DOES NOT YET CHANGE PUBLIC METRIKA LOADING**  
**P18E-B DOES NOT YET CHANGE FORM GOAL RUNTIME**

Verified post-deploy:

- homepage still includes current Metrika bootstrap;
- no banner appears publicly;
- no `fp02_cookie_consent` cookie is auto-written on ordinary visitor GET.

## 13. Dashboard

- foundation ready
- frontend pending
- gating pending
- cookie policy state surfaced as current / needs review
- indexing remains closed

## 14. Frontend Regression

**NO VISITOR-FACING BEHAVIOR CHANGE IN P18E-B**

- public pages still render normally;
- current Metrika behavior remains unchanged;
- no consent banner visible;
- no consent cookie written on ordinary GET;
- public domain still serves WordPress.

## 15. Olya Safety

**OLYA CURRENT EDITORIAL STATE PRESERVED**

- no legal copy rewrite;
- no SEO counter override;
- no footer/menu rewrite for cookie reopen links;
- no DB rollback over current editor/Admin truth.

## 16. Legal Decisions

- consent evidence model beyond browser-state foundation: deferred
- consent lifetime policy beyond current product default `365` days: deferred
- evidence retention if server-side evidence is later chosen: deferred
- final Cookie Policy legal text: needs legal review
- `sessionStorage['fp02_utm']` final public legal wording: needs legal/operator review

## 17. Indexing

**INDEXING REMAINS CLOSED**

- `blog_public=0`
- `robots.txt` still disallows crawl

## 18. Parity

**CODE PARITY PASS / EDITORIAL TRUTH PRESERVED**

- exact touched plugin files match source and production after deploy
- production code version: `0.3.17-p18e-ab`

## 19. WP Forge Knowledge

Proven lessons promoted:

- `PRIVACY-011` machine-state/version contract before frontend UI
- `PRIVACY-012` truthful Admin readiness, not fake ACTIVE state
- `PRIVACY-013` browser consent cannot authorize privileged server behavior
- `PRIVACY-014` integration classification is technical configuration

## 20. Git

- clean worktree from canonical remote used
- secret scan: PASS
- dirty main untouched
- commit/push status handled separately from production deploy evidence

## 21. Next Implementation Wave

Expected:

- `P18E-C/D` public cookie notice/settings + real conditional Yandex Metrika loading
- then `P18E-E/F` form-goal consent gating + policy/withdrawal integration

## 22. Acceptance

**FP-0002 P18E-A/B COMPLETE — CURRENT OLYA/ADMIN STATE AND TRACKER REALITY RECONFIRMED — COOKIE CONSENT HAS ONE CORE OWNER — EXPLICIT CONSENT STATES AND VERSION CONTRACT ARE IMPLEMENTED — A SAFE BROWSER RECORD CONTRACT EXISTS — NO UNAPPROVED VISITOR TRACKING DATABASE WAS CREATED — `НАСТРОЙКИ САЙТА → COOKIE И КОНФИДЕНЦИАЛЬНОСТЬ` IS DISCOVERABLE AND PERSISTENT — YANDEX METRIKA IS MAPPED TO ANALYTICS WITHOUT DUPLICATING ITS COUNTER SOURCE — PUBLIC METRIKA AND FORM-GOAL RUNTIME ARE INTENTIONALLY UNCHANGED — DASHBOARD TRUTHFULLY SHOWS FOUNDATION READY / FRONTEND PENDING — OLYA'S CURRENT EDITORIAL WORK IS PRESERVED — INDEXING REMAINS CLOSED**
