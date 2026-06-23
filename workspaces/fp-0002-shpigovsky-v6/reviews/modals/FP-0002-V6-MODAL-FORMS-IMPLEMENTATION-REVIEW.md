# FP-0002 V6 MODAL FORMS IMPLEMENTATION REVIEW

**Date:** 2026-06-23  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Pre-modals tag:** `fp-0002-v6-pre-modals-operator-stable-01` (`0f78f6d`)

## Pre-modals stable release

`FP-0002-V6-PRE-MODALS-OPERATOR-STABLE-01` — VERIFIED. External ZIP SHA-256 `b05bdda7e34fdf51b7e560bcd8937ea1dcccd6501e20ba8d43828bee11a52f93`. Restore test PASS.

## Operator source protection

Operator-authored SCSS overlay on rehabilitation CTA band and therapy article WebP assets preserved. No section regressions introduced by modal work.

## Triumph v6 authority

`workspaces/triumph-manipulator-landing-v6/` confirmed via `projects/triumph-manipulator-landing/frontend-workspace.md`.

## Triumph form files audited

`src/js/form.js`, `src/js/modal.js`, `src/partials/components/callback-modal.html`, `backend/send-lead.php`, `backend/site-config.php`, `backend/lib/recaptcha.php`.

## Functional contract ported

Modal open/close/overlay/Escape/focus trap/focus return/scroll lock; unified `data-lead-form` validation; Inputmask phone; consent; submit lock; captcha lifecycle hooks; payload hidden fields; response verification logic.

## Functionality not portable

Triumph CSS/DOM naming, Triumph endpoint, Triumph reCAPTCHA site key, Metrika goals, Triumph honeypot without FP-0002 backend contract.

## CTA trigger inventory

8 modal triggers connected. See `reviews/modals/FP-0002-V6-MODAL-TRIGGER-INVENTORY-v1.md`.

## Modal component

`src/partials/components/modal-consultation.html` — single instance before `</body>`.

## Modal variants

One modal; context via `data-modal-title`, `data-modal-subtitle`, `data-modal-submit-text`, `data-modal-source` (consultation / callback / appointment).

## Modal form fields

Name, phone, message (required), consent (required). Email = 0.

## Consent

FP-0002 final-form consent text and legal links `/consent-personal-data/`, `/privacy-policy/`.

## Required field validation

Custom validation with `aria-invalid`, `aria-describedby`, first-invalid focus — ACTIVE.

## Phone mask and paste

Inputmask `+7 999 999 - 99 - 99` — ACTIVE. Completeness validation — ACTIVE.

## Captcha provider

Google reCAPTCHA v3 (Triumph architecture).

## Captcha configuration

**BLOCKED** — `LEAD_FORM_CONFIG.siteConfigEndpoint` empty; Triumph key not copied.

## Captcha lifecycle

Lazy load + token on submit path implemented; inactive without config.

## Endpoint

**BLOCKED** — `LEAD_FORM_CONFIG.endpoint` empty.

## Payload

`form_context`, `lead_source`, `page_url`, `page_title`, form fields, optional `g-recaptcha-response`.

## Submit locking

ACTIVE during validation/submit.

## Success contract

Only after HTTP OK + JSON without `ok:false` / `success:false`. Not reachable while backend BLOCKED.

## Error contract

Validation errors, captcha security message, backend blocked honest message, network/HTTP errors when endpoint configured.

## False-success protection

No mock success; blocked backend shows honest error — ZERO false success.

## Accessibility

`role=dialog`, `aria-modal`, `aria-labelledby`, `aria-hidden`, Escape, focus trap, focus return, `aria-live` status.

## Focus management

Focus into first field on open; return to trigger on close.

## Responsive validation

Overflow check all false at 320–1398. Modal internal scroll on short viewport — ACTIVE.

## Existing final form regression

`data-lead-form` unified controller; visual regression screenshot captured.

## Site regression

Swiper ×3, Fancybox comfort, header/footer unchanged visually — NONE reported.

## Build

`npm run build` — succeeded.

## Remaining blocked integrations

FP-0002 `backend/send-lead.php` equivalent, public `site-config.php` with reCAPTCHA site key approved for Shpigovsky domain.

## Final verdict

**MODAL SYSTEM — IMPLEMENTED_PENDING_OPERATOR_REVIEW** (PARTIAL integration: backend + captcha config BLOCKED; false success PROHIBITED).
