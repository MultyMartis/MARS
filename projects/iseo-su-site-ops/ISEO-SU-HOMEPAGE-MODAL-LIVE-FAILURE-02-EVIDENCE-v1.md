# ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02 — EVIDENCE v1

**Task:** ISEO-SU-SITE-OPS-HOMEPAGE-MODAL-LIVE-FAILURE-02  
**Date:** 2026-09-09  
**Live:** https://i-seo.su/

## Supersedes prior PASS

Previous HOMEPAGE FORM REGRESSION 01 reported PASS for “homepage/modal” forms, but that wave targeted `#callback__FORM` (“Мы перезвоним вам”), not the operator modal “Получить бесплатный аудит вашего сайта”.

Operator live failure + this real-browser repro **supersede** any synthetic/direct-POST PASS for the audit modal. Direct PHP/POST alone is insufficient for this form.

## Modal contract (verified)

| Item | Value |
|------|--------|
| Title | Получить бесплатный аудит вашего сайта |
| Popup | `#audit__FORM_popup` |
| FORM ID | `#audit__FORM` |
| Submit | `#audit__FORM_send` (`type=submit`) |
| Fields | `af_name`, `af_contact`, `af_phone`, `af_site` (HTML not required), `af_comment`, `personal_data_consent` |
| Markup authority | `production-source/theme/iseoblog/page-home.php` |
| JS | `production-source/js/common.js` → POST `audit__FORM.php` |
| PHP | `production-source/forms/audit__FORM.php` |

**Not** the callback family (`#callback__FORM` / `callback__FORM.php`).

## Before (real browser)

Evidence: `evidence/homepage-modal-live-failure-02/_browser-repro-before.json`

| Case | Site | Request | Body / UI |
|------|------|---------|-----------|
| A | blank | POST `https://i-seo.su/audit__FORM.php` | generic error YES; success NO; reload NO |
| B | filled + operator-style phone `+7 (111) 111-11-11` | same endpoint | body `true`; success YES |

Events (remote):

- `2026-09-09T14:54:51Z` `form=audit class=site result=reject` (blank site)
- Earlier `13:56:49Z` same class (likely operator)
- Filled path `accept/mail` at `14:55:04Z`

## Root cause (proven)

`audit__FORM.php` rejected blank site via:

```php
if (!iseo_form_is_meaningful($site, 3)) {
    iseo_form_reject($form_id, "site");
}
```

HTML/JS treat `af_site` as optional (`required` absent; `checkEmptyFields` only enforces HTML-required). Blank site → AJAX → HTTP 200 body `false` → `ajaxComplete` shows “Не удалось отправить заявку…”.

Phone validation: operator-style phone accepted when site filled → **not** the failure mode.

Secondary hardening (same deploy): `#audit__FORM_send` lacked `preventDefault`/`return false` (homepage regression fixed page/callback only). Added for consistency; blank-site reject was the proven failure.

## Minimal fix

1. `audit__FORM.php` — site optional; reject only non-empty non-meaningful:
   - `if ($site !== "" && !iseo_form_is_meaningful($site, 3))`
2. `common.js` — `#audit__FORM_send`: `e.preventDefault()` + `return false`

## Backup / deploy

Dir: `X:\AI MARS\local\sites\iseo-su-production\_homepage-modal-live-failure-02\`  
Evidence: `evidence/homepage-modal-live-failure-02/_backup-deploy.json`  
Deployed ~`2026-09-09T14:56:44Z`

| File | SHA-256 after (live = source) |
|------|-------------------------------|
| `audit__FORM.php` | `C6DDCE7E8DBC40150F93F9EDFFD1C86E44512A0B0AF1C09C10BA37BBD4464D86` |
| `common.js` | `7681D979546F87E84929B13C23C9053B1DFDE5F293F6AE558533EC1CE5992012` |

## After (real browser, mandatory)

| Case | Evidence | Result |
|------|----------|--------|
| Audit site blank | `_validation-focused-retest.json` | POST 200 `true`; success UI early YES; generic error NO; reload NO |
| Audit site filled | same | PASS |
| Main homepage `#page__FORM` | `_validation-after.json` | PASS |
| Webinar | `_validation-after.json` | PASS |
| Restaurant / city / niche | `_validation-seo-smoke.json` | PASS (legacy `.required-checkbox` `cf_agree*` must be checked in smoke harness) |
| Consent negative (audit) | `_validation-after.json` | `checkEmptyFields=1`, request not sent |

Isolated mail: `test_mode` ON → recipient `im.work@mail.ru`; restored **OFF**. No intentional production test mail to `nikel007i33@yandex.ru` in post-fix retests.

## Security final

| Control | State |
|---------|--------|
| NORMAL RECIPIENT | `nikel007i33@yandex.ru` |
| TEST MODE | OFF |
| HMAC | ACTIVE (timing tokens `iseo_ft`/`iseo_fs`/`iseo_fid` accepted) |
| HONEYPOT | ACTIVE (`contact_company_url`) |
| MIN-FILL | ACTIVE |
| RATE LIMIT | ACTIVE |
| DUPLICATE PROTECTION | ACTIVE |
| CONSENT | ACTIVE (JS + server) |

## Non-changes

DESIGN / SEO / MENU / SITEMAP / unrelated form logic: **NO**

## Tools (local diagnostics)

`tools/_homepage-modal-live-failure-02-*.py`
