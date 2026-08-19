# REPORT — FP-0002 PROD-P18H Privacy / Retention Decisions + Launch-Tail Readiness

**Wave:** PROD-P18H  
**Date:** 2026-08-20  
**Status:** **PASS** (READY WITH NON-BLOCKING LEGAL NOTE)

---

## 1. Status

**PASS** — Privacy/legal/product decisions resolved within authoritative evidence bounds. Launch-tail ready for P18I. Indexing untouched (OPEN — human-approved).

---

## 2. Current Production Truth

**P18H CURRENT PRODUCTION / EDITORIAL TRUTH VERIFIED**

| Surface | Value |
|---------|--------|
| Domain | `https://shpigovsky.ru/` |
| Core | `0.3.20-p18g` |
| Indexing | **OPEN** — Olya (human-approved) |
| P18G guard | ACTIVE |
| Cookie consent | ACTIVE |
| Metrika | CONSENT-GATED (counter `98284776`) |
| Form goals | CONSENT-GATED |
| Cookie reopen | ACTIVE |
| SMTP | VERIFIED / ACTIVE |
| Leads | ACTIVE (`lead_retention_days=0`) |
| Consent lifetime | **365** days |
| Consent version | **1** |

Evidence: `REPORTS/evidence/prod-p18h-privacy-decisions/01-production-intake.json`

---

## 3. Legal Basis

**P18H RUSSIAN PRIVACY / COOKIE LEGAL BASIS RECHECKED**

See `RU-LEGAL-BASIS-MATRIX.md`. Statutory requirements (152-FZ Art. 5, 9) separated from product recommendations.

---

## 4. Legal Copy Audit

**CURRENT LEGAL COPY FACTUALLY MATCHED AGAINST LIVE RUNTIME**

Cookie Policy: **FACTUALLY COMPLETE**. Privacy Policy: retention «неограничен» — **LEGAL REVIEW NEEDED** when applying 730d retention.

---

## 5. Decision A — Cookie Policy

**COOKIE POLICY FINAL STATUS EXPLICITLY CLASSIFIED**

| | |
|---|---|
| **Status** | **B — FACTUALLY COMPLETE / OPERATOR-READY** |
| **Legal sign-off** | PENDING |
| **P18H mutation** | None (Olya editorial preserved) |

---

## 6. Decision B — Consent Evidence

**CONSENT EVIDENCE MODEL RECOMMENDATION GROUNDED IN AUTHORITATIVE EVIDENCE**

**Recommendation: browser-only** (`fp02_cookie_consent`). No server-side consent DB in P18H.

---

## 7. Decision C — Consent Lifetime

**CONSENT LIFETIME AND REPROMPT POLICY RESOLVED**

| | |
|---|---|
| **Lifetime** | **365 days** (production Admin value) |
| **Re-prompt** | Version change, expiry, tampered record, material new provider/purpose |

---

## 8. Decision D — UTM

**UTM SESSION STORAGE TREATMENT IS FACTUALLY DEFINED**

`sessionStorage['fp02_utm']` — five UTM keys, 120-char cap, session scope, disclosed in Cookie Policy §2.3, submitted to lead registry on form post.

---

## 9. Decision E — Lead Retention

**FORM LEAD RETENTION RECOMMENDATION PRODUCED**

| | |
|---|---|
| **Recommended** | **730 days** |
| **Production config** | **0** (unchanged) |
| **Historical purge** | **None** |

**NO HISTORICAL REAL LEADS DELETED WITHOUT EXPLICIT AUTHORITY**

---

## 10. Operator Decision Matrix

| ID | Auto-resolved | Operator/legal still required |
|----|---------------|------------------------------|
| A Cookie Policy | Factual completeness | Final legal sign-off |
| B Consent evidence | browser-only | Only if counsel rejects browser-only |
| C Consent lifetime | 365d + re-prompt rules | No |
| D UTM | Disclosure + bounds | No |
| E Lead retention | 730d recommendation | Apply Admin value + Privacy Policy alignment |

Full matrix: `DECISION-MATRIX.md`

---

## 11. Cookie Policy Safety

No production Cookie Policy edit in P18H — **COOKIE POLICY UPDATE PRESERVES CURRENT OLYA EDITORIAL TRUTH**

---

## 12. Dashboard

Source updates (deploy optional): consent evidence row, lead retention recommendation row, P18H wave label. Production meta may lag until next deploy.

---

## 13. Indexing

**INDEXING OPEN — HUMAN APPROVED**

**P18H DOES NOT MUTATE HUMAN INDEXING DECISION**

---

## 14. Sitemap

**SITEMAP SUBMISSION TARGETS VERIFIED BEFORE SUBMISSION**

`https://shpigovsky.ru/wp-sitemap.xml` — submit in P18I to GSC + Yandex Webmaster.

---

## 15. Launch Tail

**FINAL LAUNCH-TAIL READINESS CLASSIFIED:** **READY WITH NON-BLOCKING LEGAL NOTE**

---

## 16. Documentation

**CURRENT LAUNCH DOCS CONSISTENT WITH HUMAN-APPROVED OPEN INDEXING**

Updated: RUNBOOK, OPEN-ITEMS-AFTER-P18H, PROJECT-STATUS, DECISIONS.md

---

## 17. Olya Safety

**OLYA CURRENT EDITORIAL STATE PRESERVED THROUGH P18H**

---

## 18. WP Forge Knowledge

Added: FORM-RETENTION rules in FORMS-AND-SMTP-STANDARD; P18H row in knowledge assimilation index.

---

## 19. Git

Commits on `fp-0002-p18h` → `origin/mars/canonical-post-recovery`. Secret scan: PASS.

---

## 20. Next Wave

**P18I — SITEMAP SUBMISSIONS + FINAL PRODUCTION CRAWL + LAUNCH CLOSEOUT**

---

## 21. Acceptance

**FP-0002 P18H COMPLETE** — remaining privacy/cookie/retention questions resolved as far as authoritative Russian legal, regulator, provider and runtime evidence allow.

---

## Expected decision output (summary)

| Decision | Output |
|----------|--------|
| **A Cookie Policy** | FACTUALLY COMPLETE — pending legal sign-off |
| **B Consent evidence** | **browser-only** |
| **C Consent lifetime** | **365 days** + version/expiry/tamper/provider re-prompt |
| **D UTM sessionStorage** | Disclosed session attribution; bounded keys; flows to lead registry |
| **E Lead retention** | **730 days recommended**; production **0** until operator applies |
