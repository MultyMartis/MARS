# REPORT — ISEO-SU-SITE-OPS-HOMEPAGE-FORM-REGRESSION-01

**Lane:** ISEO-SU-SITE-OPS  
**Task:** HOMEPAGE + MODAL FORM REGRESSION DIAGNOSIS / GUARDED FIX 01  
**Date:** 2026-09-09  
**FINAL STATUS:** COMPLETE — HOMEPAGE + MODAL FORM REGRESSION ROOT CAUSE PROVEN / LIVE LEAD INTAKE RESTORED / SECURITY PRESERVED

---

## Summary

Operator-reproduced live lead loss on `https://i-seo.su/`: blank “Адрес сайта” caused JS to treat the field as mandatory, then native HTML submit (no `preventDefault`) reloaded the page — no AJAX, no success UI, no mail. Same defect on main `#page__FORM` and modal `#callback__FORM`.

HTML and PHP already treated site as optional. Minimal fix in `js/common.js` only: add `preventDefault`/`return false` on both homepage submit buttons; enforce site emptiness only when the input has HTML `required`. Live deployed and byte-aligned with source. Isolated `test_mode` mail to `im.work@mail.ru` proven; `test_mode` returned OFF. Security controls unchanged.

---

## Changed files (MARS)

### Created

- `ISEO-SU-HOMEPAGE-FORM-REGRESSION-01-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-HOMEPAGE-FORM-REGRESSION-01.md`
- `reports/ISEO-SU-HOMEPAGE-FORM-REGRESSION-01-RU.md`
- `tools/_homepage-form-regression-01-*.py` (local diagnostics; may remain on dirty main only)
- `evidence/homepage-form-regression-01/` (JSON)

### Modified

- `production-source/js/common.js` (homepage/modal handlers + site validation semantics only)

Production backup (out of git): `X:\AI MARS\local\sites\iseo-su-production\_homepage-form-regression-01\`

---

## FINAL HARD CHECK

FORM A: `#page__FORM` / `#page__FORM_send` → `page__FORM.php`  
FORM B: `#callback__FORM` / `#callback__FORM_send` → `callback__FORM.php`

FORM A FAILURE REPRODUCED: YES  
FORM B FAILURE REPRODUCED: YES

SITE URL FIELD: `pf_site` / `cf_site`  
BROWSER REQUIRED: NO  
JS REQUIRED: YES (pre-fix accidental) → NO (post-fix, unless HTML required)  
SERVER REQUIRED: NO (empty allowed)  
EXPECTED FINAL SEMANTICS: OPTIONAL

FORM A SUBMIT INTERCEPT BEFORE: NO (blank-site path; native submit)  
FORM B SUBMIT INTERCEPT BEFORE: NO (blank-site path)

FORM A REQUEST BEFORE: none to handler (blank)  
FORM B REQUEST BEFORE: none to handler (blank)

FORM A SERVER RESPONSE BEFORE: n/a (blank)  
FORM B SERVER RESPONSE BEFORE: n/a (blank)

FORM A PAGE RELOAD BEFORE: YES  
FORM B PAGE RELOAD BEFORE: YES

FORM A MAIL PATH BEFORE: NOT REACHED (blank)  
FORM B MAIL PATH BEFORE: NOT REACHED (blank)

ROOT CAUSE FORM A: PROVEN — JS mandatory site + missing preventDefault  
ROOT CAUSE FORM B: PROVEN — same  
COMMON ROOT CAUSE: YES

FILES CHANGED: `production-source/js/common.js` (+ evidence/reports)

FORM A SUBMIT INTERCEPT AFTER: YES  
FORM B SUBMIT INTERCEPT AFTER: YES

FORM A REQUEST AFTER: `https://i-seo.su/page__FORM.php` POST  
FORM B REQUEST AFTER: `https://i-seo.su/callback__FORM.php` POST

FORM A SERVER RESULT AFTER: PASS (`true`)  
FORM B SERVER RESULT AFTER: PASS (`true`)

FORM A SUCCESS UI: PASS  
FORM B SUCCESS UI: PASS

FORM A PAGE RELOAD AFTER: NO  
FORM B PAGE RELOAD AFTER: NO

VALID WITHOUT SITE URL: PASS  
VALID WITH SITE URL: PASS

ISOLATED MAIL TEST: PASS  
TEST RECIPIENT: im.work@mail.ru  
PRODUCTION MAIL TEST SENT: NO (diagnosis incidental filled-site pre-fix accepts noted in evidence; post-fix positives under test_mode)

WEBINAR REGRESSION: NONE  
RESTAURANT REGRESSION: NONE  
CITY REGRESSION: NONE  
NICHE REGRESSION: NONE

NORMAL RECIPIENT: nikel007i33@yandex.ru  
TEST MODE FINAL: OFF  
HMAC: ACTIVE  
HONEYPOT: ACTIVE  
MIN-FILL: ACTIVE  
RATE LIMIT: ACTIVE  
DUPLICATE PROTECTION: ACTIVE  
CONSENT SERVER GUARD: ACTIVE

DESIGN CHANGED: NO  
SEO CHANGED: NO  
MENU CHANGED: NO  
SITEMAP CHANGED: NO

PRODUCTION/SOURCE ALIGNED: YES (`5894E145…`)  
UNRELATED FILES CHANGED: 0 (in scoped commit)  
FOREIGN WIP PRESERVED: YES  
REMOTE SYNC: COMPLETE (after push)

FINAL STATUS:

COMPLETE — HOMEPAGE + MODAL FORM REGRESSION ROOT CAUSE PROVEN / LIVE LEAD INTAKE RESTORED / SECURITY PRESERVED
