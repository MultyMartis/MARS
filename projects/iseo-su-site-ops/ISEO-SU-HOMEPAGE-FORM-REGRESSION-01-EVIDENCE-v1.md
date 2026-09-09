# ISEO-SU HOMEPAGE FORM REGRESSION 01 — EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-HOMEPAGE-FORM-REGRESSION-01`  
**Date:** 2026-09-09  
**Lane:** ISEO-SU-SITE-OPS  
**Final status:** COMPLETE — HOMEPAGE + MODAL FORM REGRESSION ROOT CAUSE PROVEN / LIVE LEAD INTAKE RESTORED / SECURITY PRESERVED

---

## 1. Operator Symptoms

On `https://i-seo.su/`:

1. Main homepage form: “Адрес сайта” behaved mandatory; visual submit possible; full page reload; no success UI; no production mail.
2. Modal/callback form: same pattern.

Live lead-intake regression (HIGH).

---

## 2. Form Inventory

| | FORM A | FORM B |
|--|--------|--------|
| ID | `#page__FORM` | `#callback__FORM` |
| Family | homepage main | homepage modal |
| Action | `""` (empty) | `""` |
| Method | `post` | `post` |
| Submit | `#page__FORM_send` (`type=submit`) | `#callback__FORM_send` |
| JS | `js/common.js` click handler | same file, separate handler |
| AJAX URL | `page__FORM.php` (root `/` → `/page__FORM.php`) | `callback__FORM.php` |
| Site field | `pf_site` / `#pf_site` | `cf_site` / `#cf_site` |
| HTML `required` on site | **false** | **false** |
| Consent | `personal_data_consent=1` | same |
| Honeypot | `contact_company_url` | same |
| HMAC/timing | `iseo_ft` / `iseo_fs` / `iseo_fid` | same |
| Markup authority | `production-source/theme/iseoblog/page-home.php` | same |
| PHP handler | `production-source/forms/page__FORM.php` | `callback__FORM.php` |

Handlers do **not** require non-empty site content: `iseo_form_first_scalar` accepts `""`; meaningful checks are name/method/contact only.

---

## 3. Browser Reproduction

JSON: `evidence/homepage-form-regression-01/_browser-repro.json` (started 2026-09-09T13:08:47Z).

| FORM | Site | Submit intercepted? | AJAX to handler? | HTTP | Page reload? | Success UI? | Mail path? |
|------|------|---------------------|------------------|------|--------------|-------------|------------|
| A | blank | partial (JS validation) | **NO** | n/a | **YES** (`nav_count=2`) | NO | NO |
| A | filled | YES (AJAX) | YES `/page__FORM.php` | 200 | NO | YES (pre-fix path) | YES (accept/mail) |
| B | blank | partial | **NO** | n/a | **YES** | NO | NO |
| B | filled | YES | YES `/callback__FORM.php` | 200 | NO | YES | YES |

Blank-site path matches operator: JS marks site error (`checkEmptyFields=1`), no AJAX, native submit → `action=""` → reload.

---

## 4. Site Field Validation

| Layer | Result |
|-------|--------|
| BROWSER REQUIRED? | **NO** (`required` attribute absent on live + source) |
| JS REQUIRED? | **YES (pre-fix)** — `checkEmptyFields` forced every `input[name$="_site"]` empty → error unless `*_site_no` checked; **no** `*_site_no` in markup |
| SERVER REQUIRED? | **NO** for content — empty string accepted; reject only if field missing as POST key (`null`) |
| EXPECTED FINAL SEMANTICS | **OPTIONAL** (canonical HTML + PHP; operator expectation confirmed) |

---

## 5. Submit Event Forensic

Pre-fix origin/`common.js` (SHA-256 `B6D1F7E9…`):

- `#page__FORM_send` / `#callback__FORM_send`: `function()` **without** `preventDefault` / `return false`.
- On validation failure, click handler returns; browser continues default submit for `type=submit`.
- Recent `#page__FORM_send_seo` root-relative endpoint fix did **not** alter homepage handlers.

---

## 6. common.js Review

| | Value |
|--|-------|
| LIVE SHA-256 before | `B6D1F7E941DECDC89A6B0C5EF7A209BA9FFAEEB01A25110B0CA31707C9F892D8` |
| LIVE/SOURCE after | `5894E145C10FC7FDF66543FFE421ADA4255829109C68B1962927A66C37D3FD13` |
| Backup | `X:\AI MARS\local\sites\iseo-su-production\_homepage-form-regression-01\` |
| Deploy record | `evidence/homepage-form-regression-01/_backup-deploy.json` |

Minimal hunks only:

1. Homepage/modal click handlers: `function(e){ e.preventDefault(); … return false; }`
2. Site loop: require empty-site error only if `$(this).prop('required') && !noSite`

Dirty-main vs origin tip for `common.js` contained **only** these hunks (no foreign WIP in that file vs `origin/mars/canonical-post-recovery`).

---

## 7. Handler Contract

**FORM A:** `page__FORM.php` — required meaningful: name, contact method, phone; site/comment optional empty; consent via `iseo_form_guard_request`; success body `true`; fail `false`.

**FORM B:** `callback__FORM.php` — same security guard; site optional empty.

Security stack unchanged: HMAC, honeypot, min-fill, rate, duplicate, consent.

---

## 8. Mail Path

| Phase | Path |
|-------|------|
| Blank site **before** | **A** no request to handler (native reload) |
| Filled site before / after | Guard → accept → `mail()` when not rate/dup |
| Intermediate validation | Some `false` bodies = `duplicate` / `rate` (ACTIVE anti-spam), **not** form-broken |
| Isolated test_mode | ON during positive mail proofs; recipient path uses test recipient `im.work@mail.ru`; restored **OFF** |

Events (UTC): blank/filled accepts after fix include `13:39:18`/`13:40:06` page + `13:39:41`/`13:40:29` callback `accept/mail` under test_mode.

---

## 9. Root Cause

**FORM A:** (1) JS treated optional site as mandatory; (2) missing `preventDefault` → native reload when validation failed.  
**FORM B:** same.  
**COMMON ROOT CAUSE:** YES.

---

## 10. Fix

File: `production-source/js/common.js` only (live + source aligned). No handler/PHP/markup/security/SEO changes.

---

## 11. Positive Validation

`_validation-positive-retest.json` (after rate window cleared): `all_pass: true`

| Case | Body | Success UI | Reload |
|------|------|------------|--------|
| A blank site | `true` | YES | NO |
| B blank site | `true` | YES | NO |
| A filled site | `true` | YES | NO |
| B filled site | `true` | YES | NO |

Earlier `_validation-after.json`: intercept/AJAX/no-reload proven; consent missing blocked client-side; honeypot → server `false`; cross-form honeypot smokes hit `/page__FORM.php` without reload.

---

## 12. Negative Validation

| Test | Result |
|------|--------|
| missing consent | JS `checkEmptyFields=1`, no POST |
| honeypot populated | POST → `false` / event `honeypot` |
| rate/duplicate | ACTIVE (observed rejects) |

---

## 13. Cross-Form Regression

Webinar / restaurant / city / niche: honeypot smoke — intercepted, canonical `/page__FORM.php`, body `false`, no reload. No production mail for smokes.

---

## 14. Security

| Control | Final |
|---------|-------|
| NORMAL RECIPIENT | `nikel007i33@yandex.ru` |
| TEST MODE | OFF |
| HMAC | ACTIVE |
| HONEYPOT | ACTIVE |
| MIN-FILL | ACTIVE |
| RATE LIMIT | ACTIVE |
| DUPLICATE | ACTIVE |
| CONSENT | ACTIVE |
| NEW CC/BCC | NO |

---

## 15. Production/Source Alignment

Live HTTP SHA-256 == worktree/source `common.js` == `5894E145…`. Production-only hotfix avoided.

---

## 16. Final Decision

COMPLETE — homepage + modal lead intake restored; site URL optional as intended; security preserved; scoped JS fix only.
