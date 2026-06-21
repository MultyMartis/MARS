# V6 reCAPTCHA deploy package check

**Project:** `workspaces/triumph-manipulator-landing-v6/`  
**Date:** 2026-05-30  
**Purpose:** Pre-upload checklist for reCAPTCHA backend on production  
**No secrets in this document.**

---

## Build

- [ ] Run `npm run build` from workspace root.
- [ ] Confirm build exits **0** and log shows `copyLocalBackendConfig` copied `backend/config.local.php` → `dist/backend/config.local.php`.

## Upload (full `dist/`)

- [ ] `dist/backend/config.local.php` — **must be uploaded** (PHP `return [...]` with `recaptcha_site_key` + `recaptcha_secret_key`; not JSON).
- [ ] `dist/backend/site-config.php` — **must be uploaded** (public JSON endpoint; reads config via `triumph_load_config()`).
- [ ] `dist/backend/send-lead.php` — **must be uploaded** (form POST handler; verifies token server-side).
- [ ] `dist/backend/lib/` — **must be uploaded** (`config-loader.php`, `recaptcha.php`, and any other files in folder).
- [ ] `dist/backend/config.php` — include if not already on host.
- [ ] Frontend assets (`dist/assets/js/`, pages, etc.) — upload full `dist/` as usual.

## Post-upload live checks

- [ ] `GET https://manipulator-triumph.ru/backend/site-config.php` → HTTP **200**, body `{"recaptchaSiteKey":"..."}` with **non-empty** value; **no** secret fields.
- [ ] `GET https://manipulator-triumph.ru/backend/config.local.php` → **403**, blank, or error — **not** visible PHP source, **not** JSON with keys.
- [ ] Submit one lead form on a live page → response **not** HTTP **422** with «Проверка безопасности не пройдена…».
- [ ] If still failing: check host PHP error log for `[triumph] recaptcha verify failed: <error-code>`.

## Optional diagnosis (remove after use)

- [ ] `dist/backend/recaptcha-debug.php` may be uploaded temporarily; **delete from hosting** after diagnosis.
- [ ] Debug page must never expose key values — status flags only.

## Common mistakes

| Mistake | Symptom |
|---------|---------|
| `config.local.php` contains JSON (`{"recaptchaSiteKey":...}`) instead of PHP array | Empty site key in `site-config.php`; verification fails |
| `config.local.php` missing on server | Empty `recaptchaSiteKey`; 422 on submit |
| `site-config.php` hardcodes keys or includes secret | Security leak; possible key/domain mismatch |
| Backend folder not uploaded | 404 on `/backend/site-config.php` and `/backend/send-lead.php` |
| Only frontend uploaded, not `dist/backend/` | Form loads but security check always fails |

## Architecture reminder

| File | Role |
|------|------|
| `config.local.php` | Private PHP config; real keys in `return [...]` |
| `site-config.php` | Public JSON; `recaptchaSiteKey` only via `triumph_load_config()` |
| `send-lead.php` | Uses secret from config; never exposes it |
