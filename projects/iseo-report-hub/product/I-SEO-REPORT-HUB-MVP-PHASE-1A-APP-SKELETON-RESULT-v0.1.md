# I-SEO Report Hub — MVP Phase 1A App Skeleton Result v0.1

**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Wave:** MVP Phase 1A App Skeleton + Config Baseline 01

---

## 1. Status

- **Phase 1A complete**
- **Source-only** — writes limited to Active Brain `app-source` + programme docs
- **App-source path:** `X:\AI MARS\projects\iseo-report-hub\app-source\`
- **Runtime not synced** — `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` untouched
- **No DB** — no creation, no connection, no SQL
- **No secrets** — no `.env` / `.env.local` created

---

## 2. What Was Added

- `app/bootstrap.php` — paths, session, config load, service wiring
- Simple `Router` — exact GET/POST matching, 404 / 405
- Views + layout — dashboard, login, health, not-found + partials
- Controllers — Base, Dashboard, Auth, Health
- Services — ConfigService, AuthService, CsrfService
- Helpers — `e()`, path helpers, flash helpers
- Health / login / dashboard stubs via front controller

---

## 3. Source Files Changed

### Created

- `app-source/app/bootstrap.php`
- `app-source/app/routes.php`
- `app-source/app/Controllers/BaseController.php`
- `app-source/app/Controllers/DashboardController.php`
- `app-source/app/Controllers/AuthController.php`
- `app-source/app/Controllers/HealthController.php`
- `app-source/app/Services/AuthService.php`
- `app-source/app/Services/ConfigService.php`
- `app-source/app/Services/CsrfService.php`
- `app-source/app/Support/helpers.php`
- `app-source/app/Support/Response.php`
- `app-source/app/Support/Router.php`
- `app-source/app/Support/View.php`
- `app-source/app/Views/layout.php`
- `app-source/app/Views/pages/dashboard.php`
- `app-source/app/Views/pages/login.php`
- `app-source/app/Views/pages/health.php`
- `app-source/app/Views/pages/not-found.php`
- `app-source/app/Views/partials/header.php`
- `app-source/app/Views/partials/footer.php`
- `app-source/app/Views/partials/flash.php`
- `app-source/config/routes.example.md`
- `product/I-SEO-REPORT-HUB-MVP-PHASE-1A-APP-SKELETON-RESULT-v0.1.md`
- `reports/REPORT-iseo-report-hub-mvp-phase-1a-app-skeleton-config-baseline-01.md`

### Modified

- `app-source/README.md`
- `app-source/app/README.md`
- `app-source/public/index.php`
- `app-source/public/health.php`
- `app-source/public/assets/css/app.css`
- `app-source/public/assets/js/app.js`
- `OPERATIONAL-INDEX.md`

---

## 4. What Works in Source

- PHP built-in server review command (operator-optional):  
  `php -S 127.0.0.1:8088 -t public public/index.php`
- Dashboard route `GET /`
- Login stub `GET /login` + stub `POST /login`
- Health route `GET /health` (+ standalone `public/health.php`)
- 404 route fallback
- CSRF skeleton (session token + form field + validate)
- Config skeleton (defaults from `config/*.example.php`; optional future `.env.local` parse)

---

## 5. What Does Not Exist Yet

- Runtime sync (source → Localhost)
- Database / schema migrations / seeds execution
- Real users / password auth
- Reports CRUD
- Client publishing / token URLs
- File uploads pipeline
- Composer / frameworks
- Vhost / hosts mapping

---

## 6. Security Notes

- No secrets committed or generated
- `.env.local` **not** created
- Output escaping helper `e()`
- CSRF skeleton present on login form
- No DB connection
- No credentials beyond `.env.example` placeholders (`CHANGE_ME`)

---

## 7. Next Phase

**Recommended:** Phase 1B — source → runtime sync + local smoke.

**Alternative:** DB creation charter only after runtime skeleton smoke.

---

## 8. SAFE UNKNOWN

- Whether operator will prefer Laragon vhost (`iseo-report-hub.test`) vs built-in server for first runtime smoke after Phase 1B
- Exact future auth store (table/columns) remains as schema draft only until a DB charter
- Whether optional `.env.local` will be introduced in Phase 1B or deferred to a DB/auth charter
