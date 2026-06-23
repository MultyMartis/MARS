# FP-0002 Triumph Form Contract Audit v1

**Date:** 2026-06-23  
**Authority workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Evidence:** `projects/triumph-manipulator-landing/frontend-workspace.md`, `triumph-workspace-authority-map-v1.md` (referenced), Git history on `mars/post-cycle8-live-tests`, active Triumph v6 `src/js/form.js`, `src/js/modal.js`, `backend/send-lead.php`, `backend/site-config.php`

## Canonical Triumph v6 confirmation

| Item | Value |
|------|-------|
| Canonical workspace | `workspaces/triumph-manipulator-landing-v6/` |
| Form JS authority | `src/js/form.js` |
| Modal JS authority | `src/js/modal.js` |
| Backend endpoint default | `backend/send-lead.php` |
| Public captcha config | `backend/site-config.php` → `recaptchaSiteKey` |
| Captcha provider | Google reCAPTCHA v3 (`grecaptcha.execute`) |

## Triumph form source files

| Area | File |
|------|------|
| Form init/validation/submit | `src/js/form.js` |
| Modal open/close/focus | `src/js/modal.js` |
| Modal markup | `src/partials/components/callback-modal.html` |
| Backend transport | `backend/send-lead.php` |
| Public site key | `backend/site-config.php` |
| reCAPTCHA verify | `backend/lib/recaptcha.php` |

## Function contract map

| Function | Triumph source file | Function/class | Dependency | Portable | FP-0002 adaptation |
| -------- | ------------------- | -------------- | ---------- | -------: | ------------------ |
| modal open | `modal.js` | `openModal` | `data-modal-open` | YES | `data-modal-open="consultation"` + FP-0002 `modal-consultation` markup |
| modal close | `modal.js` | `closeModal` | `data-modal-close` | YES | same hook contract |
| overlay click | `modal.js` | overlay listener `event.target === overlay` | none | YES | `.modal-consultation__overlay` |
| Escape close | `modal.js` | `keydown` Escape | none | YES | ported |
| focus trap | `modal.js` | `trapFocus` | Tab key | YES | ported |
| focus return | `modal.js` | `lastFocusedElement` | none | YES | ported |
| body scroll lock | `modal.js` | `BODY_LOCK_CLASS` | none | YES | `body[data-modal-state=open]` |
| required fields | `form.js` | `validateField` / `validateForm` | `required`, `data-validate` | YES | `data-lead-form` + native `required` |
| name validation | `form.js` | min length 2 | none | YES | ported |
| phone validation | `form.js` | `PHONE_DIGITS_MIN` | mask | YES | Inputmask completeness check |
| Inputmask | FP-0002 existing | Inputmask CDN | Inputmask | YES | kept FP-0002 mask `+7 999 999 - 99 - 99` |
| paste handling | `form.js` | `bindPhoneMask` input handler | none | PARTIAL | Inputmask handles paste in FP-0002 |
| consent required | `form.js` | checkbox validation | none | YES | FP-0002 consent copy |
| field error rendering | `form.js` | `.is-invalid`, `[data-form-error]` | none | YES | `[data-lead-field-error]` + BEM modifiers |
| error clearing | `form.js` | input/change revalidate | none | YES | ported |
| submit lock | `form.js` | `submitLock` + `is-loading` | none | YES | `data-lead-form-state=loading` |
| duplicate submit protection | `form.js` | early return on lock | none | YES | ported |
| captcha initialize | `form.js` | `loadRecaptchaScript` lazy | site config | YES | architecture ported, config BLOCKED |
| captcha token | `form.js` | `grecaptcha.execute` | site key | YES | hook only |
| captcha reset | `form.js` | new token per submit | none | YES | on submit path |
| captcha failure | `form.js` | security message | none | YES | ported message |
| payload build | `form.js` | `collectPayload` / hidden fields | none | YES | `form_context`, `lead_source`, `page_url`, `page_title` |
| request transport | `form.js` | `fetch` POST FormData | endpoint | YES | endpoint BLOCKED for FP-0002 |
| success state | `form.js` | response JSON `ok`/`success` | backend | YES | only after confirmed response |
| error state | `form.js` | HTTP / JSON failure | backend | YES | honest blocked/error messages |
| form reset | `form.js` | after confirmed success only | none | YES | ported |
| backend response verification | `form.js` | `response.ok` + JSON flags | none | YES | ported |
| anti-spam honeypot | `form.js` | `company_url` hidden field | backend | NOT PORTED | no FP-0002 backend contract confirmed |
| Metrika goal | `form.js` | `trackLeadGoal` | Triumph counter | NO | Triumph-domain analytics |

## Endpoint and captcha boundary

| Item | Triumph value | FP-0002 value | Reusable |
| ---------------------- | ------------- | ------------- | -------: |
| Endpoint | `backend/send-lead.php` | **BLOCKED** (empty `LEAD_FORM_CONFIG.endpoint`) | NO |
| Captcha provider | Google reCAPTCHA v3 | Google reCAPTCHA v3 architecture only | PARTIAL |
| Public site key | from Triumph `config.local.php` via `site-config.php` | **BLOCKED** (empty `siteConfigEndpoint`) | NO |
| Form action identifier | `data-form-id` / hidden `form_id` | `form_context` + `lead_source` | PARTIAL |
| CSRF/nonce | SAFE UNKNOWN in Triumph frontend | SAFE UNKNOWN | NO |
| Success contract | HTTP 200 + JSON without `ok:false` / `success:false` | same contract when backend exists | YES |
| Error contract | HTTP error or JSON `message` | same contract when backend exists | YES |

## FP-0002 honest mode

```text
FORM FRONTEND CONTRACT — IMPLEMENTED
BACKEND — BLOCKED
CAPTCHA CONFIG — BLOCKED
FALSE SUCCESS — PROHIBITED
```
