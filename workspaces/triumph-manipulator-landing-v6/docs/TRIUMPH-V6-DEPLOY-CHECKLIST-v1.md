# Triumph V6 — deploy checklist v1

**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Build:** `npm run build` → upload contents of `dist/`  
**No secrets in this document.**

---

## 1. Build (local)

- [ ] From workspace root: `npm run build` exits **0**.
- [ ] Confirm log does **not** copy `backend/config.local.php` into `dist/`.
- [ ] Confirm `dist/backend/.htaccess` exists (blocks public access to secrets).
- [ ] Confirm `dist/backend/config.local.php` is **absent** (create on server only).

---

## 2. What to upload from `dist/`

Upload the **full** `dist/` tree to the site document root (e.g. Beget `public_html/` or subdomain root):

| Path | Upload |
|------|--------|
| `dist/index.html`, `dist/*.html` (12 PPC landings) | **Yes** |
| `dist/assets/` (css, js, img, fonts, favicon, vendor) | **Yes** |
| `dist/backend/send-lead.php` | **Yes** |
| `dist/backend/site-config.php` | **Yes** |
| `dist/backend/lib/` | **Yes** |
| `dist/backend/config.php` | **Yes** (defaults; no SMTP password) |
| `dist/backend/.htaccess` | **Yes** |
| `dist/backend/config.local.php.example` | Optional (reference only) |
| `dist/robots.txt`, `dist/sitemap.xml` | **Yes** if present |
| Legal: `dist/privacy-policy/`, `dist/user-agreement/`, `dist/consent-personal-data/`, `dist/cookie-files-policy/` | **Yes** |

**Do not upload from repo (not in dist):**

- `backend/config.local.php` from dev machine — create fresh on server (see §3).
- `backend/api/forms/send.php` — legacy; excluded from build.
- `backend/recaptcha-debug.php` — diagnosis only; never leave on production.

---

## 3. Server-only: `backend/config.local.php`

Create on the host **next to** `send-lead.php` and `site-config.php`:

`public_html/backend/config.local.php` (path may vary by host layout).

**Format:** valid PHP array (copy structure from `backend/config.local.php.example`):

```php
<?php
return [
    'recaptcha_site_key' => 'PASTE_SITE_KEY',
    'recaptcha_secret_key' => 'PASTE_SECRET_KEY',
    'smtp' => [
        'password' => 'PASTE_SMTP_PASSWORD',
    ],
];
```

**Required for production forms:**

| Key | Purpose |
|-----|---------|
| `recaptcha_site_key` | Public; exposed via `site-config.php` only |
| `recaptcha_secret_key` | Server-only; used by `send-lead.php` |
| `smtp.password` | When `use_smtp` is true in `config.php` |

**Optional overrides:** `recipients`, `from_address`, `from_name` — see `config.local.example.php`.

**Never:** JSON file, HTML comments, or keys pasted outside `return [...]`.

**Permissions:** file not world-readable if host allows `chmod 640` (optional).

---

## 4. What must NOT be publicly exposed

| Resource | Expected HTTP access |
|----------|----------------------|
| `backend/config.local.php` | **403** / blank / error (`.htaccess` deny) |
| `backend/config.php` | **403** (deny direct browse; PHP `require` still works) |
| `backend/lib/*` | **403** (deny direct browse) |
| `backend/config/*` | **403** |
| `backend/recaptcha-debug.php` | Not deployed, or **403** if present |

Secrets must never appear in HTML, JS, or `site-config.php` JSON.

---

## 5. Verify `GET /backend/site-config.php`

After upload and `config.local.php` on server:

```text
GET https://manipulator-triumph.ru/backend/site-config.php
```

- [ ] HTTP **200**
- [ ] `Content-Type: application/json`
- [ ] Body shape: `{"recaptchaSiteKey":"<non-empty>"}`  
- [ ] **No** `recaptcha_secret_key`, **no** SMTP password, **no** extra secret fields

If `recaptchaSiteKey` is empty: fix `config.local.php` format on server (§3).

---

## 6. Test lead form

1. Open a live PPC page over **HTTPS** (not `file://`).
2. Open DevTools → Network; confirm `site-config.php` returns a site key.
3. Submit hero / modal / FAQ form with valid phone (+ consent if shown).
4. [ ] Response JSON success (not HTTP **422** «Проверка безопасности не пройдена…»).
5. [ ] Inbox receives mail with subject **«Заявка на МАНИПУЛЯТОР»** (`send-lead.php` constant).

**Metrika goal (after successful submit):**

- Counter ID: **109490539**, goal: **`form-lead`**.
- [ ] In Yandex Metrika → Goals, confirm conversion after test submit (or add `?metrika_debug=1` and check console `[metrika-debug]` logs).

---

## 7. Test reviews widget (SmartWidgets)

- [ ] Page source includes `https://res.smartwidgets.ru/app.js`.
- [ ] Reviews section `#reviews` contains `<div class="sw-app" data-app="8f230bf5383dad62ee32d7f63decfd43">`.
- [ ] Widget renders on live host (may require HTTPS; ad blockers can hide it).

---

## 8. Verify legal pages

Open each URL (adjust host if staging):

| Page | Path |
|------|------|
| Политика конфиденциальности | `/privacy-policy/` |
| Пользовательское соглашение | `/user-agreement/` |
| Согласие на обработку ПД | `/consent-personal-data/` |
| Политика Cookie | `/cookie-files-policy/` |

- [ ] Each returns **200**, readable Russian text, footer legal links work.
- [ ] **No** `/cookies/` path (removed; use `cookie-files-policy` only).

---

## 9. Pre-upload dist sanity (automated / grep)

After `npm run build`:

- [ ] **12** PPC HTML files at dist root (plus `index.html` if used).
- [ ] **4** legal page directories under `dist/`.
- [ ] No `{{...}}` template leftovers in `dist/**/*.html`.
- [ ] No `data-form-handler="mock"` in PPC dist HTML.
- [ ] No `backend/api/forms/send.php` references in dist HTML/JS.
- [ ] No `/cookies/` links in dist.
- [ ] `dist/backend/config.local.php` **missing**.
- [ ] `dist/backend/.htaccess` **present**.

Optional: `node tools/verify-final-wave-dist.mjs` from workspace root.

---

## 10. Post-deploy security smoke

```text
GET https://manipulator-triumph.ru/backend/config.local.php
```

- [ ] **Not** downloadable PHP source with keys.
- [ ] Prefer **403 Forbidden** (Apache + `.htaccess`).

If host uses nginx without `.htaccess`: replicate deny rules in server config or place `config.local.php` outside document root (host-specific — **SAFE UNKNOWN** until confirmed with provider).

---

## Architecture reference

| File | Role |
|------|------|
| `config.local.php` | Server-only secrets; blocked by `.htaccess` |
| `site-config.php` | Public JSON; site key only |
| `send-lead.php` | POST handler; reCAPTCHA + mail |
| `.htaccess` | Deny direct access to config and internal dirs |

**Build policy (v1.1):** Gulp does **not** copy local `config.local.php` into `dist/`. Operator creates it on the server after upload.
