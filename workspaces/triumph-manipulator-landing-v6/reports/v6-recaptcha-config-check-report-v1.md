# REPORT — V6 reCAPTCHA config check

**Project:** `workspaces/triumph-manipulator-landing-v6/`  
**Date:** 2026-05-29  
**Scope:** Local config, build output, source wiring, git security, server deploy checklist  
**No commit / no push.** Secrets not recorded in this document.

---

## 1. Config file check (`backend/config.local.php`)

| Check | Result |
|-------|--------|
| File exists | **yes** |
| `recaptcha_site_key` in returned PHP array | **no** |
| `recaptcha_secret_key` in returned PHP array | **no** |
| Values look non-placeholder (structured config) | **no** |
| Raw reCAPTCHA key material present in file body (unstructured) | **yes** |
| Valid `<?php` + `return [...]` config format | **no** |
| `config.local.php` gitignored (`backend/.gitignore`) | **yes** |
| `config.local.php` tracked in git | **no** |
| `config.local.php` staged | **no** |

**Finding:** The local file exists but is **not** in the format expected by `triumph_load_config()` (`config-loader.php` requires a PHP file that `return`s an array). Current content appears to be pasted Google console notes (HTML comments + bare key lines), not `recaptcha_site_key` / `recaptcha_secret_key` entries. Until reformatted to match `backend/config.local.php.example`, `site-config.php` will not expose a site key and production verification will fail.

**Recommended local fix (human-operated, not applied by this check):**

1. Copy structure from `backend/config.local.php.example`.
2. Set `recaptcha_site_key` and `recaptcha_secret_key` using the same keys already obtained from Google (do not commit this file).

---

## 2. Build check (`npm run build`)

**Command:** `npm run build` — **exit 0** (gulp `build` completed).

| Artifact | Expected | Result |
|----------|----------|--------|
| `dist/backend/send-lead.php` | exists | **yes** |
| `dist/backend/config.local.php` | must NOT exist | **absent** |
| `dist/backend/config.local.php.example` | exists | **yes** |
| `dist/backend/site-config.php` | exists | **yes** |
| `dist/backend/lib/recaptcha.php` | exists | **yes** |
| `dist/backend/lib/config-loader.php` | exists | **yes** |

Gulp `backend()` task explicitly excludes `!backend/config.local.php` and ships `config.local.php.example` only.

---

## 3. reCAPTCHA flow check (source wiring)

### Frontend (`src/js/form.js`)

| Requirement | Status |
|-------------|--------|
| Loads public config from `backend/site-config.php` | **yes** — `SITE_CONFIG_ENDPOINT`, `loadSiteConfig()` |
| Site key from backend JSON (`recaptchaSiteKey`) | **yes** |
| `grecaptcha.execute()` used | **yes** — `appendRecaptchaToken()` |
| `g-recaptcha-response` sent with POST | **yes** — `formData.set('g-recaptcha-response', token)` + hidden field |

Skipped when: `file://` preview, `data-form-handler="mock"`, empty/placeholder site key.

### Backend

| Requirement | Status |
|-------------|--------|
| `send-lead.php` calls reCAPTCHA verification | **yes** — `triumph_verify_recaptcha()` before mail send; **422** on failure |
| `lib/recaptcha.php` posts to Google `siteverify` | **yes** |
| Production host requires valid token | **yes** — host contains `manipulator-triumph.ru` via `triumph_is_production_host()` |
| Placeholder / missing secret rejected on production | **yes** — empty or `PASTE_SECRET_KEY_HERE` → `false` on production |

**Google API:** Not called during this local check (no live POST to `siteverify`).

### Analytics

| Requirement | Status |
|-------------|--------|
| Metrika counter `109490539` in layout | **yes** — `analytics-yandex-metrika.html` |
| Goal `form-lead` on successful production submit | **yes** — `trackLeadGoal()` in `form.js` |

---

## 4. Security check

| Check | Result |
|-------|--------|
| `git ls-files` lists `config.local.php` | **no** (only `backend/config.local.php.example` tracked) |
| `git check-ignore` for `backend/config.local.php` | **ignored** via `backend/.gitignore` |
| `config.local.php` in `git status` / staged | **not shown** (ignored untracked) |
| `dist/backend/config.local.php` after build | **absent** |
| Secrets printed in this report | **no** |

---

## 5. Server deploy checklist

Use after uploading **`dist/`** to hosting (`manipulator-triumph.ru` or staging with production host rules).

- [ ] **1.** Copy full `dist/` tree to the web root (or equivalent docroot) on the server.
- [ ] **2.** On the server, create `backend/config.local.php` next to `send-lead.php` (not shipped in dist).
- [ ] **3.** Paste the **same** reCAPTCHA v3 keys as local (site + secret) in PHP array form per `config.local.php.example`.
- [ ] **4.** Confirm `backend/config.local.php` is **not** web-accessible (outside public docroot or blocked by server rules).
- [ ] **5.** Open `https://<host>/backend/site-config.php` — response must be JSON with **site key only** (`recaptchaSiteKey`), no secret fields.
- [ ] **6.** Submit a test lead form on a real page (HTTPS, not `file://`).
- [ ] **7.** Confirm response is **not** HTTP **422** with reCAPTCHA security message.
- [ ] **8.** Confirm lead email received at configured recipients.
- [ ] **9.** In Yandex Metrika (counter `109490539`), confirm goal **`form-lead`** fired after successful submit.

**Post-deploy smoke URLs (replace host):**

- Public config: `/backend/site-config.php`
- Form endpoint: `/backend/send-lead.php` (POST only)

---

## 6. Regression risks

1. **Invalid local `config.local.php` format** — site key never reaches frontend; tokens not generated; production returns **422**.
2. **Missing server `config.local.php`** — same as above on production after deploy.
3. **Secret only in dist by mistake** — mitigated by gulp exclude; still verify server file permissions.
4. **Non-production host** — verification may be skipped if secret unset (by design); do not rely on this for prod sign-off.
5. **Client-side reCAPTCHA load failure** — form may submit without token; backend policy decides (production should reject).
6. **`mail()` / SMTP on host** — reCAPTCHA can pass while email still fails (**500**); separate ops check required.

---

## 7. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live Google `siteverify` response for current keys | **UNKNOWN** — not tested (no safe local PHP/runtime call in this session) |
| End-to-end form submit on production host | **UNKNOWN** — requires human deploy + browser test |
| Email delivery (SPF/DKIM/mail transport) | **UNKNOWN** |
| Metrika goal visibility in reporting UI | **UNKNOWN** — requires browser/network verification after deploy |
| Whether unstructured keys in current local file were rotated/exposed in editor logs | **UNKNOWN** — treat as hygiene review |

---

## 8. Git status (repository root)

- **Branch / remote:** not evaluated in depth for this task.
- **`config.local.php`:** ignored, not tracked, not staged.
- **Workspace:** many unrelated modified/untracked paths under `C:\AI MARS` (governance, ORCA packs, survivability, etc.); **no** `config.local.php` entry in short status sample.
- **This report:** new file `reports/v6-recaptcha-config-check-report-v1.md` (report-only; commit not requested).

---

**NO COMMIT · NO PUSH**
