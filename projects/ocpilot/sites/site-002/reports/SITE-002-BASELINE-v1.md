# REPORT — SITE-002 BASELINE

**Site ID:** SITE-002  
**Project:** ЗПМ (TEST)  
**Run:** 5 — Access Verification & Baseline  
**Date:** 2026-06-09  
**Environment:** https://zpm.new-site.space/  
**Mode:** Read-only — no site changes performed  
**Evidence (local, not in repo):** `C:\AI MARS\.recovery-temp\site-002-run5-verify.json`, `site-002-run5-db-meta.json`

---

## Executive summary

| Channel | Result |
|---------|--------|
| FTP | **OK** |
| OpenCart Admin | **BLOCKED** — credentials do not establish session |
| phpMyAdmin | **OK** |
| Storefront (HTTP) | **OK** — home, catalog, PDP reachable |

**Wave 1 readiness:** **BLOCKED**

---

## 1. FTP Verification

### Access

| Field | Value |
|-------|-------|
| Host | `polygonws.beget.tech` |
| Port | 21 |
| Protocol | FTP |
| Login result | **Success** |
| Effective root | Account chroot = OpenCart `public_html` (login PWD `/`) |
| Secrets `Root Path` | `/zpm.new-site.space/public_html/` — **not usable as FTP CWD** (550); content is already at login root |

### OpenCart structure (top level)

Confirmed standard OpenCart 3 layout plus site-specific paths:

| Path | Type | Notes |
|------|------|-------|
| `admin/` | dir | Admin application |
| `catalog/` | dir | Storefront MVC |
| `system/` | dir | Core, storage, OCMOD sources |
| `image/` | dir | Media; `image/cache/` present |
| `assets/` | dir | **Custom** front-end bundle (CSS/JS/fonts/img) |
| `1c_exchange/` | dir | **Custom** 1C exchange (`import0_1.xml`, `import_files/`) |
| `1c_incoming/` | dir | **Custom** |
| `Product_DOCs/` | dir | **Custom** |
| `config.php` | file | 1879 bytes |
| `index.php` | file | defines `VERSION` |
| `system/tweak.ocmod.xml` | file | Custom OCMOD (16025 bytes) |
| `system/tweak-54fz.ocmod.xml` | file | Custom OCMOD |

### Theme files

| Check | Result |
|-------|--------|
| Themes under `catalog/view/theme/` | **One theme:** `default` |
| `product.twig` | **Yes** — `catalog/view/theme/default/template/product/product.twig` (124 bytes; wrapper) |
| `category.twig` (standard path) | **No** — `template/category/category.twig` missing |
| Category template (actual) | **Yes** — `catalog/view/theme/default/template/product/category.twig` (3245 bytes; custom ZPM layout) |
| PDP partials | `producthero.twig`, `producttabs.twig`, `relproducts.twig`, `productcard.twig` |
| Section partials | `catalog/view/theme/default/template/sections/*` (ZPM blocks: filter sidebar, hero, maps, forms, etc.) |
| Theme CSS dir | `catalog/view/theme/default/stylesheet/stylesheet.css` (+ `paypal/` subdir) |
| Theme JS dir | **Absent** — `catalog/view/theme/default/javascript/` not present |

### CSS locations

| Layer | Entry points |
|-------|----------------|
| **Primary (live storefront)** | `/assets/css/style.css`, `/assets/css/style.min.css`, `/assets/css/sd.css` |
| Vendor | `/assets/css/vendor/swiper/`, `/assets/css/vendor/fancybox/` |
| OpenCart stock | `catalog/view/javascript/bootstrap/css/bootstrap*.css` |
| Theme default | `catalog/view/theme/default/stylesheet/stylesheet.css` (secondary) |
| Swiper (OC module path) | `catalog/view/javascript/jquery/swiper/css/*.css` |

### JS locations

| Layer | Entry points |
|-------|----------------|
| **Primary (live storefront)** | `/assets/js/main.js`, `/assets/js/main.min.js`, `/assets/js/main-and.js` |
| Vendor | `/assets/js/vendor/jquery/`, `inputmask/`, `swiper/` |
| OpenCart global | `catalog/view/javascript/common.js`, `qrcode.js`, `jquery/`, `bootstrap/` |
| External | Google reCAPTCHA v3 |

### Cache (filesystem, read-only)

| Location | Observation |
|----------|-------------|
| `system/storage/cache/` | 4 entries incl. `cache.catalog.language.*`, `cache.store.*`, `template/` subtree (38 items) |
| `image/cache/` | 7 entries |

---

## 2. Admin Verification

### Access

| Field | Value |
|-------|-------|
| URL | https://zpm.new-site.space/admin/ |
| Beget JS challenge | Present; bypassed with `beget=begetok` cookie for HTTP client |
| Login form | Loads (OpenCart 3 Russian build footer) |
| POST login | Returns login page (`<title>Авторизация</title>`); **no logout link, no dashboard chrome** |
| Session cookie | `OCSESSID` set, but **not authenticated** |
| Credentials tested | From external secrets only |

### Platform version (from source via FTP, not admin UI)

| Field | Value |
|-------|-------|
| Core constant | **OpenCart 3.0.3.9** (`index.php`, `admin/index.php`) |
| Distribution | Russian build (footer links: opencart-russia.ru) |
| ocStore branding | **Not confirmed** — presents as OpenCart 3.0.3.9 RU |

### Admin-only facts (could not verify)

| Item | Status |
|------|--------|
| Active theme (admin UI) | **SAFE UNKNOWN** — inferred `default` from filesystem + `oc_extension` |
| Modification manager state | **Partial** — see DB §; admin UI not reached |
| Developer / theme / Sass cache toggles | **SAFE UNKNOWN** |
| Custom modules list (admin) | **Partial** — see DB extensions + FTP controllers |

**Admin verdict:** **Access channel reachable; authentication BLOCKED with supplied credentials.**

---

## 3. Database Verification

### Access

| Field | Value |
|-------|-------|
| phpMyAdmin URL | https://bruma.beget.com/phpMyAdmin |
| Login | **Success** |
| Database | `polygonws_zpm` |
| Host (config.php) | `localhost` |
| Table prefix | `oc_` (runtime); PMA displays tables as `OC_*` |

### Structure

| Metric | Value |
|--------|-------|
| Table count | **146** |
| Engine (sample) | InnoDB predominant |
| MySQL/MariaDB exact version | **SAFE UNKNOWN** — ad-hoc SQL tab did not return parseable result; PMA 4.9.7 on Beget |

### Catalog scale (structure page row hints)

| Table | Rows (approx.) |
|-------|----------------|
| `oc_product` | 134 |
| `oc_category` | 190 |
| `oc_modification` | 3 |
| `oc_extension` | 42 |

### Registered modifications (`oc_modification`)

| ID | Name | Code | Author | Status |
|----|------|------|--------|--------|
| 1 | Localcopy OCMOD Install Fix | `localcopy-oc3` | opencart3x.ru | enabled (1) |
| 2 | Cache cleaner | `Cache_Cleaner` | opencart3x.ru | enabled (1) |
| 3 | SEO Pro (by opencart3x.ru) | `seo_pro` | opencart3x.ru | enabled (1) |

Filesystem OCMOD also present: `system/tweak.ocmod.xml`, `system/tweak-54fz.ocmod.xml` (status in DB not re-verified separately).

### Custom / non-core tables (sample)

`CRON`, `OC_ANKETA`, `OC_BLOG_POSTS`, `OC_BLOG_THEMES`, `OC_CATEGORY_DOCS`, `OC_CATEGORY_DOC_DESCRIPTION`, `OC_GOOGLESHOPPING_*`, `OC_PRODUCT_PRICE_INDEX`, `OC_BACKUP_MOVE_POLKA_TO_83`

### Extensions (`oc_extension` sample)

Notable: `theme/default`; modules `account`, `banner`, `carousel`, `category`, `featured`, `slideshow`; payments `cod`, `free_checkout`; shipping `flat`; totals standard set.

**No INSERT/UPDATE/DELETE executed.**

---

## 4. Theme Mapping

| Layer | Path / name | Role |
|-------|-------------|------|
| OpenCart theme id | **`default`** (only theme dir; `oc_extension` → `theme/default`) | OC theme registry |
| Presentation source | **`/assets/`** + **`template/sections/`** + **`template/product/*`** | ZPM custom UX |
| Layout chrome | `template/common/header.twig`, `footer.twig`, `megamenu.twig`, `quicksearch.twig` | Global shell |
| Category UX | `template/product/category.twig` | Filters, subcategory chips, mobile sidebar |
| Home | `template/common/home.twig` + multiple `sections/*` | Landing blocks |

**Note:** Heavily customized **`default`** theme — not a separate theme directory. CSS/JS primary entry is **`/assets/`**, not `catalog/view/theme/default/`.

---

## 5. PDP Mapping

### Template chain

```
catalog/view/theme/default/template/product/product.twig
  └── {{ producthero }}  → product/producthero.twig (+ sections/producthero.twig)
  └── {{ producttabs }}  → product/producttabs.twig (+ sections/producttabs.twig)
  └── {{ relproducts }}  → product/relproducts.twig
```

Backup/alternate files on disk: `product.twig__`, `producthero -backUp.twig`.

### Controllers (FTP)

| File | Notes |
|------|-------|
| `catalog/controller/product/product.php` | Core PDP controller (29896 bytes; customizations likely) |
| `catalog/controller/product/relproducts.php` | Related products |
| `catalog/controller/product/katalog.php` | Custom catalog route |

### Live PDP sample (HTTP)

URL pattern: SEO paths under `/katalog/.../` (example verified):

`https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850`

Markers on live page: `page__content`, `zpm-*` classes present.

### PDP assets (live)

| Type | Files |
|------|-------|
| CSS | `/assets/css/style.css`, `style.min.css`, `sd.css`, vendor swiper/fancybox |
| JS | `/assets/js/main.js` (via min bundle chain), vendor jquery/inputmask/swiper |

---

## 6. Category Mapping

| Item | Path / behavior |
|------|-----------------|
| Primary template | `catalog/view/theme/default/template/product/category.twig` |
| Standard OC path | `template/category/category.twig` — **missing** |
| Controller | `catalog/controller/product/category.php` |
| Layout features | `category__layout`, mobile filter sidebar (`data-filter-sidebar`), subcategory chips (`zpm-sub-cat-chips`), sort UI |
| Supporting sections | `sections/filterssidebar.twig`, `sections/categorylayout.twig` |
| Live URL | `/katalog/` and nested paths (example: `/katalog/nejtralnoe-oborudovanie/stoly`) |

---

## 7. Risks

| Risk | Severity | Detail |
|------|----------|--------|
| Admin credentials non-functional | **High** | Blocks admin-side verification, modification refresh audit, developer cache toggles |
| Secrets FTP root path inaccurate | **Medium** | Documents `/zpm.new-site.space/public_html/` but account roots at `public_html` content; automation must not rely on secrets path alone |
| Heavy customization in `default` theme | **Medium** | PDP/Catalog UX split across `product/*`, `sections/*`, `assets/*`, custom controllers — high coupling |
| 1C exchange + custom DB tables | **Medium** | `1c_exchange/`, `OC_PRODUCT_PRICE_INDEX`, `OC_CATEGORY_DOCS` — import/pricing side effects during changes |
| Enabled OCMOD pack (SEO Pro, cache cleaner, localcopy) | **Medium** | 3 DB modifications + `tweak*.ocmod.xml` — refresh order matters before Twig/CSS work |
| `index.php` debug flags on | **Low** | `display_errors` enabled in storefront `index.php` — operational leak risk on TEST |
| Backup / rollback unknown | **High** | No verified backup at Run 5 |
| Baseline match not selected | **Medium** | Registry still `SAFE UNKNOWN` vs `ocstore-3038-rs2` / other baselines |
| MySQL version unconfirmed | **Low** | PMA browse OK; version string not captured |

---

## 8. Wave 1 Readiness

### Decision: **BLOCKED**

### Blocking reasons

1. **OpenCart Admin authentication fails** with credentials from external secrets — session cookie set, dashboard not granted; Wave 1 cannot verify or safely operate admin-dependent steps (extensions, modifications refresh, developer cache, theme setting).
2. **Operator must rotate / confirm admin credentials** before any Wave 1 implementation or admin audit continuation.
3. **Backup status unknown** — no confirmed restore point before PDP/Catalog UX edits.
4. **Baseline match not selected** in OCPilot registry (`project-site-registry.md` → SAFE UNKNOWN).
5. **Intake / access brief gate** — repo still marks SITE-002 **AWAITING INTAKE**; Run 5 gate in `project-access-brief.md` is **NO** until operator updates charter.

### Ready elements (non-blocking enablers)

- FTP read access to full theme/assets/controllers.
- phpMyAdmin read access to schema and row counts.
- Storefront catalog + PDP reachable; template/asset map captured above.
- Platform version identified: **OpenCart 3.0.3.9 (RU build)**.

### Operator actions to unblock

1. Fix OpenCart Admin password or provide working admin account; re-run Admin verification.
2. Correct FTP root note in secrets (effective root = login `/`).
3. Confirm backup + rollback path on TEST.
4. Select baseline match candidate in OCPilot registry.
5. Update access brief Run 5 gate after operator approval.

---

## Baseline snapshot (fixed facts)

| Field | Value |
|-------|-------|
| Platform | OpenCart **3.0.3.9** (Russian build) |
| Theme id | **`default`** (ZPM-customized) |
| PDP template | `product/product.twig` → `producthero` + `producttabs` + `relproducts` |
| Category template | `product/category.twig` |
| CSS entry (live) | `/assets/css/style.css`, `style.min.css` |
| JS entry (live) | `/assets/js/main.js` / `main.min.js` |
| DB prefix | `oc_` |
| DB tables | 146 |
| Products / categories | ~134 / ~190 |
| Critical dependencies | SEO Pro OCMOD, Cache Cleaner, localcopy-oc3, `tweak*.ocmod.xml`, 1C exchange, `/assets` bundle, Google reCAPTCHA |

---

*Run 5 — read-only; no git commit; no site modifications.*
