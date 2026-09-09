# REPORT — ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01

**Lane:** ISEO-SU-SITE-OPS  
**Task:** FORM CONTRACT REGRESSION AUDIT + FIX 01  
**Date:** 2026-09-09  
**Handler:** `/page__FORM.php` (unchanged)  
**FINAL STATUS:** COMPLETE — ISEO-SU FORM CONTRACT REGRESSION AUDIT + FIX / ALL PROVEN PF_CONTACT-PF_PHONE DEFECTS CLOSED

---

## Summary

After the webinar form defect (`visible phone name="pf_contact"`, missing `pf_phone`, handler body `false`), the live site was audited for the **same** proven contract family.

- **137** live `/page__FORM.php` surfaces scanned (146 URLs).
- **90** forms matched the proven defect before.
- **18** remote source authorities patched (1 shared SEO include + 17 inline files). 75 include-only pages inherited the shared include fix.
- GET rescan after: **0** remaining proven defects.
- Restaurant page: BROKEN → HEALTHY.
- Security (HMAC, honeypot, min-fill, rate limit, duplicate, consent guard) **ACTIVE**. Recipient `nikel007i33@yandex.ru`. `test_mode` **OFF**.
- Handler and `common.js` **not** changed. No SEO / menu / content / design mutations.

---

## Changed files (MARS)

### Created

- `ISEO-SU-FORM-CONTRACT-REGRESSION-01-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01.md`
- `reports/ISEO-SU-FORM-CONTRACT-REGRESSION-01-RU.md`
- `tools/_form-contract-regression-01-inventory.py`
- `tools/_form-contract-regression-01-discover.py`
- `tools/_form-contract-regression-01-walk.py` (hung; not re-run)
- `tools/_form-contract-regression-01-walk-targeted.py`
- `tools/_form-contract-regression-01-backup-patch.py`
- `tools/_form-contract-regression-01-rescan-after.py`
- `tools/_form-contract-regression-01-validate.py`
- `tools/_form-contract-regression-01-ui-smoke.py`
- `evidence/form-contract-regression-01/` (JSON + screenshots)

### Modified

- `production-source/theme/iseoblog/template-parts/content-form-seo.php`
- `production-source/static-html/blog.html`
- `production-source/static-html/blog-article.html`
- `ISEO-SU-CURRENT-STATE-v1.md`
- `OPERATIONAL-INDEX.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`

Fifteen live inline service HTML files were patched **on production only**. They were **not** invented under `production-source/`.

---

## FINAL HARD CHECK

LIVE PAGE__FORM SURFACES: **137**  
BROKEN CONTRACT FORMS FOUND: **90** before / **0** after GET  
AFFECTED URLS: 90 (see `evidence/form-contract-regression-01/live-inventory.json`)  
SOURCE AUTHORITIES: **18** remote files (1 shared include + 17 inline)  
RESTAURANT FORM BEFORE: **BROKEN**  
RESTAURANT FORM AFTER: **HEALTHY**

PF_CONTACT MISUSED AS VISIBLE PHONE BEFORE: **90**  
PF_CONTACT MISUSED AS VISIBLE PHONE AFTER: **0**  
PF_PHONE MISSING BEFORE: **90**  
PF_PHONE MISSING AFTER: **0** (on previously affected `/page__FORM.php` forms)

FORMS FIXED: **18** remote authorities (75 include-only pages inherit GROUP A)  
VALID SUBMIT TESTS: events.log `accept`/`mail` + restaurant UI body `true`  
NEGATIVE CONSENT TESTS: events.log `consent`/`reject`  
HONEYPOT TESTS: events.log `honeypot`/`reject`

HMAC: **ACTIVE**  
HONEYPOT: **ACTIVE**  
MIN-FILL: **ACTIVE**  
RATE LIMIT: **ACTIVE**  
DUPLICATE PROTECTION: **ACTIVE**  
CONSENT SERVER GUARD: **ACTIVE**  
NORMAL RECIPIENT: `nikel007i33@yandex.ru`  
TEST MODE FINAL: **OFF**

UNAFFECTED FORM REGRESSION: **NONE** (homepage + webinar GET/UI OK)

TITLE CHANGED: **NO**  
DESCRIPTION CHANGED: **NO**  
H1 CHANGED: **NO**  
CANONICAL CHANGED: **NO**  
SITEMAP CHANGED: **NO**  
MENU CHANGED: **NO**  
DESIGN CHANGED: **NO**

PRODUCTION/SOURCE ALIGNED: **YES** for shared include + `blog.html`; `blog-article.html` contract-aligned not byte-identical; 15 inline HTML live-only  
PROJECT-OWNED UNCOMMITTED: **NONE** (scoped worktree allowlist only)  
FOREIGN WIP PRESERVED: **YES**  
REMOTE SYNC: **COMPLETE** — no-force push onto `origin/mars/canonical-post-recovery`. Fix `450b2998`; docs SHA `deac99fb`.

---

## Git

Worktree: `X:\AI MARS STORAGE\git-sync-iseo-su-form-contract-regression-01\repo`  
Branch: `iseo-su-form-contract-regression-01` from `origin/mars/canonical-post-recovery` @ `70c1a312`  
Fix commit: `450b299807f4404580088a0eda6ce0b90991b0e4` — `fix(iseo-su): repair legacy page form contract`  
Docs SHA: `deac99fb8961e936487eb1a9e37f0387a4cee9f5`  
Push: `70c1a312..deac99fb` `HEAD -> mars/canonical-post-recovery` (no force)
