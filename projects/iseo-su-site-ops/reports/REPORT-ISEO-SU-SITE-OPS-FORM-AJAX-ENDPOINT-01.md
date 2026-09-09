# REPORT — ISEO-SU-SITE-OPS-FORM-AJAX-ENDPOINT-01

**Lane:** ISEO-SU-SITE-OPS  
**Task:** FORM AJAX ENDPOINT RESOLUTION AUDIT + GUARDED FIX 01  
**Date:** 2026-09-09  
**Handler:** `/page__FORM.php` (unchanged)  
**FINAL STATUS:** COMPLETE — FORM AJAX ENDPOINT DEFECT PROVEN + FIXED / ROOT-RELATIVE ENDPOINT / NO REGRESSION

---

## Summary

Shared SEO form JS used a **relative** AJAX URL `page__FORM.php`. Live Playwright POSTs from nested `/services/seo/*.html` went to `/services/seo/page__FORM.php` (HTTP 200 via existing thin delegate). That is a proven defect, not a theoretical risk.

Minimal fix: one string in `#page__FORM_send_seo` → `url: '/page__FORM.php'`. Scoped deploy of `js/common.js` only. Post-deploy, all seven charter pages POST to `https://i-seo.su/page__FORM.php`. HMAC/honeypot/min-fill/rate-limit/duplicate/consent remain ACTIVE. Recipient `nikel007i33@yandex.ru`. `test_mode` OFF. Handler, field contract, SEO, menu, CSS, content unchanged.

Other form families still use relative `page__FORM.php` **on purpose** (not proven nested from this charter). WAVE 01A lines already live in `common.js` were not staged (foreign WIP).

---

## Changed files (MARS)

### Created

- `ISEO-SU-FORM-AJAX-ENDPOINT-01-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-FORM-AJAX-ENDPOINT-01.md`
- `reports/ISEO-SU-FORM-AJAX-ENDPOINT-01-RU.md`
- `tools/_form-ajax-endpoint-01-network-probe.py`
- `tools/_form-ajax-endpoint-01-backup-deploy.py`
- `tools/_form-ajax-endpoint-01-regression.py`
- `tools/_form-ajax-endpoint-01-regression-resume.py`
- `evidence/form-ajax-endpoint-01/` (JSON)

### Modified

- `production-source/js/common.js` (SEO handler endpoint string only in live/working-tree; git origin commit applies the same one-string on origin-tip `common.js`)
- `ISEO-SU-CURRENT-STATE-v1.md`
- `OPERATIONAL-INDEX.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`

Production backup (out of git): `X:\AI MARS\local\sites\iseo-su-production\_form-ajax-endpoint-01\`

---

## FINAL HARD CHECK

STATIC ENDPOINT STRING BEFORE: `page__FORM.php` (SEO handler `#page__FORM_send_seo`)  
LIVE SHARED JS AUTHORITY: `X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js` (also `https://i-seo.su/js/common.js`)

HOME RESOLVED POST URL: `https://i-seo.su/page__FORM.php`  
WEBINAR RESOLVED POST URL: `https://i-seo.su/page__FORM.php`  
RESTAURANT RESOLVED POST URL: `https://i-seo.su/page__FORM.php` (was nested pre-fix)  
CITY RESOLVED POST URL: `https://i-seo.su/page__FORM.php`  
NICHE RESOLVED POST URL: `https://i-seo.su/page__FORM.php`  
USA RESOLVED POST URL: `https://i-seo.su/page__FORM.php`  
UAE RESOLVED POST URL: `https://i-seo.su/page__FORM.php`

ENDPOINT DEFECT REPRODUCED: **YES**  
ROOT CAUSE: relative AJAX endpoint `page__FORM.php` resolves against nested document path and posts to `/services/seo/page__FORM.php`  
FIX REQUIRED: **YES**

SHARED JS CHANGED: **YES** (one string, SEO handler only)  
ENDPOINT STRING AFTER: `/page__FORM.php`  
HANDLER CHANGED: **NO**  
FORM FIELD CONTRACT CHANGED: **NO**

VALID SUBMIT REGRESSION: **PASS** (webinar, restaurant, city, niche, homepage; isolated test_mode)  
CONSENT NEGATIVE TEST: **REJECT** (UI blocked POST; server POST body `false`)  
HONEYPOT NEGATIVE TEST: **REJECT** (canonical POST URL, body `false`)

NORMAL RECIPIENT: `nikel007i33@yandex.ru`  
TEST MODE FINAL: **OFF**  
HMAC: **ACTIVE**  
HONEYPOT: **ACTIVE**  
MIN-FILL: **ACTIVE**  
RATE LIMIT: **ACTIVE**  
DUPLICATE PROTECTION: **ACTIVE**  
CONSENT SERVER GUARD: **ACTIVE**

TITLE CHANGED: **NO**  
DESCRIPTION CHANGED: **NO**  
H1 CHANGED: **NO**  
CANONICAL CHANGED: **NO**  
ROBOTS CHANGED: **NO**  
SITEMAP CHANGED: **NO**  
MENU CHANGED: **NO**  
DESIGN CHANGED: **NO**  
CSS CHANGED: **NO**

PRODUCTION/SOURCE ALIGNED: **YES** (live `common.js` SHA-256 `B6D1F7E9…` == working-tree canonical source)  
UNRELATED JS REGRESSION: **NONE** (pre-existing console 409 noise unchanged)  
FOREIGN WIP PRESERVED: **YES**  
REMOTE SYNC: **COMPLETE** — no-force push onto `origin/mars/canonical-post-recovery`. Fix `1341440a`; docs SHA `2238cf5a`.

---

## Git

Worktree: `X:\AI MARS STORAGE\git-sync-iseo-su-form-ajax-endpoint-01\repo`  
Base: `origin/mars/canonical-post-recovery` @ `af5ca48788dac2e4ef9ff96fb6a45197ae3f909d`  
Fix: `1341440ac1e8381682273ff3392546b5afcd52ad` (`fix(iseo-su): use root-relative form endpoint`)  
Docs: `2238cf5a538dec0882f7f2282b5ef730c05327f2` (`docs(iseo-su): audit form ajax endpoint resolution`)  
Main workspace: dirty + 348 local-only commits; not used for this push.
