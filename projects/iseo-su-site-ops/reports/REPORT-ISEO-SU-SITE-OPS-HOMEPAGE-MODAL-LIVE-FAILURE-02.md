# REPORT — ISEO-SU-SITE-OPS-HOMEPAGE-MODAL-LIVE-FAILURE-02

**Lane:** ISEO-SU-SITE-OPS  
**Task:** HOMEPAGE MODAL LIVE FAILURE 02  
**Date:** 2026-09-09  
**FINAL STATUS:** COMPLETE — HOMEPAGE MODAL LIVE FAILURE 02 / REAL BROWSER FAILURE PROVEN + FIXED / LIVE SUCCESS UI VERIFIED

---

## Summary

Operator live failure on https://i-seo.su/ modal “Получить бесплатный аудит вашего сайта” (`#audit__FORM`) confirmed in a real browser. Blank optional site was rejected by `audit__FORM.php` (`class=site`), yielding AJAX `false` and the generic error UI. Prior HOMEPAGE FORM REGRESSION 01 PASS (callback/page family) is superseded for this modal. Minimal fix: optional site on server + `preventDefault` on audit submit. Live browser retest shows success UI with blank and filled site; smoke suite PASS; `test_mode` OFF; security stack unchanged.

---

## Hard check

| Field | Value |
|-------|--------|
| OPERATOR FAILURE CONFIRMED | YES |
| MODAL FORM ID | `#audit__FORM` |
| HANDLER | `audit__FORM.php` |
| REQUEST URL BEFORE | `https://i-seo.su/audit__FORM.php` |
| HTTP BEFORE | 200 |
| RESPONSE BEFORE | `false` (events: `site` reject) |
| PAGE RELOAD BEFORE | NO |
| SUCCESS UI BEFORE | FAIL |
| PF_CONTACT / phone / site family | `af_contact` / `af_phone` / `af_site` |
| SITE FIELD OPTIONAL | YES (HTML + JS + PHP after fix) |
| PHONE VALIDATION RESULT | OK (operator-style phone accepted when site filled) |
| ROOT CAUSE | `audit__FORM.php` required meaningful `af_site` even when blank |
| ROOT CAUSE PROVEN | YES |
| FILES CHANGED | `production-source/forms/audit__FORM.php`, `production-source/js/common.js` (+ evidence/reports/tools) |
| REQUEST URL AFTER | `https://i-seo.su/audit__FORM.php` |
| HTTP AFTER | 200 |
| RESPONSE AFTER | `true` |
| PAGE RELOAD AFTER | NO |
| SUCCESS UI AFTER | PASS |
| GENERIC ERROR AFTER | NO |
| VALID WITH SITE BLANK | PASS |
| VALID WITH SITE FILLED | PASS |
| MAIN HOMEPAGE FORM | PASS |
| WEBINAR | PASS |
| RESTAURANT | PASS |
| CITY | PASS |
| NICHE | PASS |
| ISOLATED MAIL TEST | YES (`test_mode` ON during validation) |
| TEST RECIPIENT | `im.work@mail.ru` |
| PRODUCTION TEST MAIL SENT | NO (post-fix retests under test_mode only) |
| NORMAL RECIPIENT | `nikel007i33@yandex.ru` |
| TEST MODE FINAL | OFF |
| HMAC / HONEYPOT / MIN-FILL / RATE / DUP / CONSENT | ACTIVE |
| DESIGN / SEO / MENU / SITEMAP | NO |
| PRODUCTION/SOURCE ALIGNED | YES |
| FOREIGN WIP PRESERVED | YES |
| REMOTE SYNC | (see git wave) |

---

## Changed files (MARS)

### Modified

- `projects/iseo-su-site-ops/production-source/forms/audit__FORM.php`
- `projects/iseo-su-site-ops/production-source/js/common.js`

### Created

- `ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-HOMEPAGE-MODAL-LIVE-FAILURE-02.md`
- `reports/ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02-RU.md`
- `evidence/homepage-modal-live-failure-02/*`
- `tools/_homepage-modal-live-failure-02-*.py`

Production backup (out of git): `X:\AI MARS\local\sites\iseo-su-production\_homepage-modal-live-failure-02\`
