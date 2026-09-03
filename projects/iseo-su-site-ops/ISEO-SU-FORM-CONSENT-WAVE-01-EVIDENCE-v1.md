# ISEO-SU FORM CONSENT WAVE 01 EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-FORM-CONSENT-WAVE-01`  
**Date:** 2026-09-03  
**Site:** `https://i-seo.su/`  
**Decision:** **PASS / COMPLETE**

---

## 1. Scope

WAVE 1 only: mandatory personal-data processing consent on all production contact forms of i-seo.su, enforced client-side and server-side. No WAVE 2/3 work.

## 2. Requirement

Visible wording (approved):

> Я соглашаюсь с политикой конфиденциальности и даю согласие на обработку персональных данных

«политикой конфиденциальности» links to the verified privacy-policy URL. Checkbox not pre-checked. Direct POST without valid consent must not send mail.

## 3. Privacy Policy URL Verification

| Check | Result |
|-------|--------|
| Candidate | `https://i-seo.su/privacy-policy.html` |
| HTTP | **200** |
| Content | Russian privacy / personal-data policy page |
| Alternate canonical policy | Not found as a competing production authority |
| Footer / form links | Use `/privacy-policy.html` |
| Redirect | No conflicting alternate required |

**PRIVACY POLICY URL:** `https://i-seo.su/privacy-policy.html`

## 4. Form Inventory

Contact/personal-data forms map to **12** root handlers:

| Handler | form_id |
|---------|---------|
| `callback__FORM.php` | callback |
| `page__FORM.php` | page |
| `audit__FORM.php` | audit |
| `calc__FORM.php` | calc |
| `tariff_1__FORM.php` … `tariff_4__FORM.php` | tariff_1…4 |
| `bonus__FORM.php` | bonus |
| `career__FORM.php` | career |
| `partners__FORM.php` | partners |
| `review__FORM.php` | review |

All call `iseo_form_guard_request()` then mail. Shared security: `iseo-form-security.php`. Client submit path: `js/common.js` → `checkEmptyFields()`.

Non-consent checkboxes retained separately: audit qualification `cf_agree*`, tariff extras `tarif*_dop`.

## 5. Form Families

| Family | Markup authority | Consent added |
|--------|------------------|---------------|
| Footer / shared callback | `theme/iseoblog/footer.php` | YES |
| Homepage | `theme/iseoblog/page-home.php` | YES |
| Calc / audit / SEO form parts | `template-parts/content-calc-*.php`, `content-form-seo.php` | YES |
| SEO / tariff popups | `content-seo-popups.php`, `content-tarifs-popups.php` | YES |
| Static HTML with live `<form>` | production static files (scoped transform + upload) | YES where forms exist |
| WP-rendered service/blog/glossary | theme partials / footer (HTTP body) | YES |

Static files that only contain `__FORM` string markers without `<form>` tags are **not** form instances (deploy “uncovered” 61 = false positives). Live HTTP coverage scan: **LIVE_UNCOVERED = 0**.

## 6. Consent Field Contract

| Field | Value |
|-------|-------|
| Name | `personal_data_consent` |
| Accepted | exact string `"1"` |
| Reject | missing, empty, `"0"`, `"false"`, arbitrary non-`"1"` |
| Pre-checked | **NO** |
| Mail body | Consent **not** added to notification mail (server validates only; avoids clutter) |

## 7. Client-Side Validation

- Native `required` on checkbox where markup supports it.
- `js/common.js` `checkEmptyFields()` requires presence, checked state, and value `'1'` before POST.
- Unchecked: no POST; validation cue; no JS error.

## 8. Server-Side Enforcement

In `iseo_form_guard_request()` after rate-limit checks:

- Read `personal_data_consent` via `iseo_form_post_scalar`.
- Require `=== "1"`; else `iseo_form_reject($form_id, "consent")` → client body `false`, **zero mail**.

Centralized for all 12 handlers.

## 9. Security Preservation

Unchanged: HMAC architecture/secret, token issue/validate, honeypot, min-fill-time, rate limit, duplicate suppression, CRLF/header protection, scalar rules, recipient routing, test_mode architecture.

## 10. Recipient Preservation

| Field | Value |
|-------|-------|
| Normal recipient | `nikel007i33@yandex.ru` **only** |
| Count | **1** |
| `test_mode` after closeout | **OFF / false** |
| `im.work@mail.ru` in normal routing | **NO** |
| `im.work@nail.ru` | **ABSENT** |
| Hidden CC/BCC | **NO** |

Bounded positive test temporarily enabled `test_mode` (recipient `im.work@mail.ru` only), then restored OFF.

## 11. Source Changes

- `production-source/forms/iseo-form-security.php`
- `production-source/js/common.js`
- `production-source/css/main.css`
- `production-source/theme/iseoblog/footer.php`
- `production-source/theme/iseoblog/page-home.php`
- `production-source/theme/iseoblog/template-parts/content-calc-audit.php`
- `production-source/theme/iseoblog/template-parts/content-calc-seo.php`
- `production-source/theme/iseoblog/template-parts/content-form-seo.php`
- `production-source/theme/iseoblog/template-parts/content-seo-popups.php`
- `production-source/theme/iseoblog/template-parts/content-tarifs-popups.php`
- Tools: `tools/consent_transform.py`, `tools/consent_wave_post_tests.py`, `tools/consent_live_coverage_scan.py`

## 12. Production Backup

Scoped under:

`X:\AI MARS\local\sites\iseo-su-production\_form-consent-wave-01\`

Includes `backups/`, `backup-manifest.json`, `deploy-receipt.json` (SHA-256 before deploy recorded in manifest).

## 13. Deployment

Scoped SFTP upload of core (security/JS/CSS), theme partials, and transformed static HTML with real forms. Remote `security_checks` on receipt: consent reject present, exact `"1"`, `test_mode` false, prod recipient nikel, JS consent check, typo nail absent.

## 14. Negative Direct-POST Tests

Fresh HMAC + empty honeypot + ≥3s wait; distinct handlers to avoid rate-limit ambiguity:

| Case | Handler | Result |
|------|---------|--------|
| No consent field | `page__FORM.php` | **REJECT** body `false` |
| `personal_data_consent=0` | `callback__FORM.php` | **REJECT** |
| `=false` | `audit__FORM.php` | **REJECT** |
| `=random` | `calc__FORM.php` | **REJECT** |

**MAIL SENT ON NEGATIVE TESTS:** **0**

Evidence file: `tools/_consent_post_tests.json` (local tool output; not required in Git).

## 15. Positive Validation

| Step | Result |
|------|--------|
| Enable `test_mode` via config file only | OK |
| POST page form with `personal_data_consent=1` | body `true` |
| Expected test recipient | `im.work@mail.ru` only |
| Restore `test_mode=false` | **VERIFIED** |
| Production routing restored | **YES** |

## 16. All-Handler Regression

All 12 handlers contain `iseo_form_guard_request` → shared consent path.

**ALL HANDLERS CONSENT-PROTECTED:** **YES**  
**HANDLER COUNT:** **12**

## 17. UI Validation

Representative live pages (homepage, services, region/abroad SEO, blog, glossary, tariff-calc, privacy-policy): HTTP 200; `personal_data_consent` present in HTML where contact forms render.

## 18. Production Regression

Smoke URLs returned expected HTTP 200; no PHP fatal observed; forms/consent present; no unrelated SEO mutations in this wave.

## 19. Production / Source Alignment

Changed production surfaces match MARS `production-source/` for security helper, common.js, CSS, and theme form partials. Static HTML transforms applied on production with backup; no intentional production-only hotfix tail for consent logic.

## 20. Rollback

Restore files from `_form-consent-wave-01/backups` / manifest SHA-256 set; re-upload prior versions; confirm `test_mode` false and recipient unchanged; promote rollback into `production-source` if lasting.

## 21. Final Decision

**COMPLETE — ISEO-SU FORM CONSENT WAVE 01 / ALL CONTACT FORMS REQUIRE PERSONAL-DATA CONSENT / WAVE 2 NEXT**

Do **not** start WAVE 2 or WAVE 3 in this task.
