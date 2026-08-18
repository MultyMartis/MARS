# ISEO-SU READ-ONLY PRODUCTION AUDIT v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-PHASE-2B-ACCESS-REVIEW-AND-READ-ONLY-PRODUCTION-AUDIT  
**Date:** 2026-07-24  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Site:** `https://i-seo.su/`  
**Status:** PHASE 2B — COMPLETE / READ-ONLY PRODUCTION ARCHITECTURE CAPTURED (with documented residual admin-UI gap)

No secrets are stored in this document.

---

## 1. Audit Status

| Field | Value |
|-------|-------|
| Local access presence | **COMPLETE** (FTP/SFTP + WordPress admin fields non-empty; Git-ignored) |
| Operator Beget backup | **CONFIRMED BY OPERATOR** — full hosting backup 2026-07-24 |
| External access | **PERFORMED** — read-only SFTP + public WordPress REST + bounded public page GETs |
| WordPress Admin UI via HTTP client | **PARTIAL** — login/session paths return a JS challenge shell (~273 bytes); no admin forms saved |
| Database | **NOT ACCESSED** |
| WPilot install/activation | **NOT PERFORMED** |
| Mutations | **NONE** |

---

## 2. Access Classes Used

| Class | Status in this task |
|-------|---------------------|
| A3 HOSTING READ-ONLY | Used only as filesystem listing via SFTP (not Beget panel login) |
| A4 WORDPRESS READ-ONLY | Authorized; Admin UI blocked by JS challenge; compensated by REST + SFTP |
| A5 FTP/SFTP READ-ONLY | **USED** — SFTP port 22 |
| A6 WPILOT READ-ONLY | **NOT AUTHORIZED** / not installed |
| A7 CONTROLLED WRITE | **NOT AUTHORIZED** |
| A8 EMERGENCY ROLLBACK | **NOT INVOKED** |

---

## 3. Hosting and Docroot

| Field | Value | Classification |
|-------|-------|----------------|
| Hosting | Beget | CONFIRMED BY OPERATOR + SFTP host class |
| Panel URL (metadata) | `https://cp.beget.com` (from local profile host only) | CONFIRMED BY LOCAL PROFILE |
| phpMyAdmin metadata URL | `https://mayday.beget.com/phpMyAdmin/` | OPERATOR-PROVIDED METADATA ONLY — **not opened** |
| Protocol used | SFTP | CONFIRMED BY AUDIT |
| Port | 22 | CONFIRMED BY AUDIT |
| Docroot (sanitized) | `/home/[REDACTED]/[REDACTED]/i-seo.su/public_html` | CONFIRMED BY SFTP |
| Staging | Absent | CONFIRMED BY OPERATOR (Wave A) |

---

## 4. Application Topology

**Factual hybrid model:**

1. **WordPress root install** lives in the same docroot as marketing files (`wp-config.php`, `wp-admin/`, `wp-content/`, `wp-includes/`, `index.php`).
2. **Physical `.html` trees** (`services/`, `cases/`, many root `*.html`) coexist and are served as real files when present (WordPress rewrite `!-f` / `!-d`).
3. **Apache treats `.html`/`.htm` as PHP** via `.htaccess` `AddType application/x-httpd-php .html .htm` — so “static HTML” is PHP-capable.
4. **Homepage `/`** is a WordPress Page (`glavnaya`, id 1732) using theme template `page-home.php`, which embeds a full static-like HTML document and shared `/css` `/js` assets (not a classic `wp_head` theme chrome).
5. **Parallel legacy/copy file** `home.html` exists on disk; `index.html_` appears to be a renamed former index.
6. **Blog** is WordPress-rendered (`/blog/`, generator `WordPress 7.0.2`).
7. **Custom tools** include SEO calculator + tariff UI (shared JS + `*__FORM.php` mail handlers; also mirrored in theme template-parts) and a separate `report-hub/` static HTML app.
8. **No on-server Node/Gulp source tree** (`package.json` / `gulpfile` / `src` / `scss` absent in docroot).

---

## 5. Static HTML Surface

Root marketing HTML (non-exhaustive): `about.html`, `services.html`, `contacts.html`, `cases.html`, `reviews.html`, `partners.html`, `bonuses.html`, `career.html`, `guarantees.html`, `privacy-policy.html`, `user-agreement.html`, `cookie-files-policy.html`, `blog.html`, `blog-article.html`, `home.html`.

Directories: `services/` (seo, adv, audit, development, serm, ai-optimization + many leaf HTML), `cases/` (case HTML pages), `docs/`, `video/`, `report-hub/`, `reports/`, shared `css/`, `js/`, `img/`, `fonts/`, `libs/`, `favicon/`.

`sitemap-static.xml`: **71** URLs sampled as static marketing inventory.

---

## 6. WordPress Physical Location

| Field | Value |
|-------|-------|
| Install type | **Root install** in docroot (not subdirectory-only) |
| Config | `wp-config.php` present and active signature |
| Table prefix | `wp_` |
| Multisite | **No** |
| WP_DEBUG | `true` (non-secret constant observed) |
| Custom content/plugin paths | Not redefined in inspected config metadata |

---

## 7. WordPress Runtime

| Field | Value | Source |
|-------|-------|--------|
| WordPress version | **7.0.2** | `wp-includes/version.php` + public `/blog/` generator meta |
| Site name (public REST) | INTLSEO Studio | `/wp-json/` |
| Site URL / Home | `https://i-seo.su` | REST |
| Show on front | `page` | REST |
| Front page | id **1732**, slug `glavnaya`, template `page-home.php` | REST |
| Posts page | not set as `page_for_posts` (0) | REST |
| PHP runtime version | **SAFE UNKNOWN** (Admin Site Health blocked; core requires PHP ≥ 7.4) | gap |
| Permalink example | postname-style public post URLs under site root / blog | REST samples |

---

## 8. Theme and Child Theme

| Field | Value |
|-------|-------|
| Theme directory | `wp-content/themes/iseoblog` (**only** theme present) |
| Child theme | **No** (`Template:` header absent; sole theme) |
| style.css theme header | **Absent** (file starts with CSS keyframes — custom/non-standard header) |
| Notable templates | `page-home.php`, `page-blog.php`, `page-tariffcalc.php`, `single-offer.php`, many `template-parts/content-tarifs-*`, `content-calc-*`, `tarif-calc.php` |

---

## 9. Plugins and MU Plugins

Filesystem plugin entries (versions from main plugin headers where readable):

| Plugin entry | Name / note | Version (header) |
|--------------|-------------|------------------|
| advanced-custom-fields-pro-main | Advanced Custom Fields PRO | 6.3.10 |
| wordpress-seo | Yoast SEO | 28.0 |
| jetpack | Jetpack | 14.8 |
| wp-optimize | WP-Optimize | 4.5.5 |
| akismet | Akismet | 5.3.6 |
| cyr2lat | Cyr-To-Lat | 6.3.0 |
| disable-gutenberg | Disable Gutenberg | 3.2.2 |
| duplicate-page | Duplicate Page | 4.5.4 |
| rate-my-post | FeedbackWP / Rate My Post | 4.3.0 |
| wp-simple-post-view | Post View Count | 2.0.2 |
| simple-user-avatar | Simple User Avatar | 4.7 |
| no-category-base-wpml | No Category Base (WPML) | 1.5.4 |
| wordpress-plugin-autoVersion-master | Auto Version | 1.1.0 |
| hello.php | Hello Dolly | 1.7.2 |

MU-plugins: **none** listed.  
WPilot: **absent**.  
WPBakery / The7: **not found**.

Active/inactive exact matrix: **SAFE UNKNOWN** for most plugins (Admin plugins screen blocked). REST namespaces confirm **Jetpack** and **Yoast** surfaces are live. WP-Optimize admin route returned HTTP 200 through challenge-era client only as status — treat activation as **operator-confirm later**.

---

## 10. ACF and Structured Data

| Field | Value |
|-------|-------|
| ACF PRO on disk | **Yes** (6.3.10) |
| `acf-json` | **Not found** under theme or `wp-content/acf-json` |
| Field groups / options pages | **SAFE UNKNOWN** (Admin UI blocked; no JSON sync dir) |
| Theme CPT registration | `offer` registered in `iseoblog/functions.php` |

---

## 11. Blog

| Field | Value |
|-------|-------|
| Blog route | `/blog/` WordPress-rendered |
| WP page | id 1730, slug `blog`, template `page-blog.php` |
| Public posts | REST returned 20 post samples (more may exist) |
| Taxonomies observed | `category`, `post_tag` (+ WP internal) |
| Physical `blog.html` | Exists (parallel static/PHP-capable file; not the live `/blog/` renderer) |

---

## 12. Header and Footer Ownership

| Surface | Ownership |
|---------|-----------|
| Marketing `.html` pages | Embedded header/footer markup inside each HTML file + shared `css/main.css` / `js/common.js` — **STATIC_FILE_OWNED** (PHP-capable) |
| WP blog / WP templates that call theme chrome | Theme `header.php` / `footer.php` + `template-parts/content-topbar.php`, `content-footer.php`, `content-mobilemenu.php` — **WORDPRESS_OWNED** |
| Homepage `/` | WP template `page-home.php` hardcodes chrome (static asset paths) — **SHARED_BUT_WORDPRESS_RENDERED** |

Drift risk: dual chrome (static HTML copies vs theme parts) can diverge.

---

## 13. Tariff Cards

Present in:

- Static/marketing markup + `js/common.js` (`#tariffs_slider`, tariff form posts)
- Root handlers `tariff_1__FORM.php` … `tariff_4__FORM.php` (and copies under `services/*`)
- Theme template-parts: `content-tarifs-main.php`, `content-tarifs-seo.php`, `content-tarifs-serm.php`, popups, etc.
- WP page `/tariff-calc` → `page-tariffcalc.php`

Classification: **SHARED** (static handlers + WP templates). Exact runtime surface per URL must be checked before edit.

---

## 14. SEO Calculator

| Evidence | Detail |
|----------|--------|
| Front-end | `js/common.js` calculator stages; posts to `calc__FORM.php` |
| Handlers | `calc__FORM.php` at docroot and under service subtrees |
| Theme mirrors | `template-parts/content-calc-seo.php`, `content-calc-audit.php`, `tarif-calc.php` |
| WP page | `tariff-calc` / template `page-tariffcalc.php` |

Classification: **SHARED** tool surface; mail via PHP `mail()`-style handlers (emails redacted in evidence).

---

## 15. Web-KP Tool

No dedicated `web-kp` / `kp` application directory or sitemap route was found.

**Candidates (not confirmed as “web-KP”):**

- CPT `offer` + WP page `/offers` + `single-offer.php`
- `report-hub/` (client/specialist report HTML app — different product surface)
- `varvara-new.php` (custom PHP page; purpose SAFE UNKNOWN)

**Classification:** **SAFE UNKNOWN** pending operator confirmation which production URL is “web-KP”.

---

## 16. Forms and Mail

Form/mail PHP handlers observed (filenames only):  
`callback__FORM.php`, `audit__FORM.php`, `page__FORM.php`, `calc__FORM.php`, `tariff_*__FORM.php`, `bonus__FORM.php`, `career__FORM.php`, `partners__FORM.php`, `review__FORM.php` (+ duplicates under service folders).

Signals: PHP `mail()` usage; literal recipient emails present in handlers (**not recorded**).  
No dedicated SMTP plugin confirmed active from Admin. Jetpack may provide mail-related features — **SAFE UNKNOWN**.

---

## 17. Shared Assets and Build Chain

| Asset root | Role |
|------------|------|
| `css/` | `main.css`, `media.css`, `normalize.css`, `fonts.css` |
| `js/` | `common.js` (forms, calculator, tariffs) |
| `libs/` | jQuery, Owl, Fancybox, html5shiv, isotope, respond |
| `img/`, `fonts/`, `favicon/`, `video/` | Media |
| `wp-content/uploads/` | WP media (years 2025/2026 present) |
| Build on server | **No** `package.json` / `gulpfile` / `src` / `scss` in docroot |

Source-of-truth for frontend build is **not on production** (or not deployed) — **SAFE UNKNOWN** for local/Git canonical source (U-022).

---

## 18. Routing and Rewrite

`.htaccess` (sanitized summary):

- Force HTTPS
- Block Bytespider UA
- `www.i-seo.su` → `https://i-seo.su`
- `AddType application/x-httpd-php .html .htm`
- Standard WordPress rewrite block to `/index.php`

Physical files win over WP rewrite. Missing files fall through to WordPress.

---

## 19. Source-of-Truth Candidates

| Surface | Strongest current SoT candidate |
|---------|----------------------------------|
| Marketing HTML pages | Production `.html` files in docroot / `services/` / `cases/` |
| Homepage | WP template `page-home.php` **and** parallel `home.html` (drift pair) |
| Blog posts | WordPress database + theme templates |
| Offers | CPT `offer` + theme `single-offer.php` |
| Calculator / tariffs UI | `js/common.js` + theme template-parts + `*__FORM.php` |
| Shared CSS/JS | Production `css/`, `js/`, `libs/` |
| Report Hub | `report-hub/*.html` |
| Plugins/core | WordPress plugin directories + core trees |

No maintained external Git/build tree was found on the server.

---

## 20. Production Drift Risks

1. Dual homepage: `page-home.php` vs `home.html`.
2. Dual blog: `/blog/` WP vs physical `blog.html`.
3. Tariff/calculator logic duplicated across static JS, PHP handlers, and theme parts.
4. Service-tree copies of `*__FORM.php` can diverge from root handlers.
5. `WP_DEBUG` enabled on production.
6. `debug.log` present under `wp-content/` (do not download/publish).
7. HTML executed as PHP increases include/injection risk surface.
8. Manual production edits without local SoT (U-022 / U-023).

---

## 21. WPilot Presence and Compatibility Inputs

| Input | Value |
|-------|-------|
| WPilot installed | **No** |
| WP version | 7.0.2 |
| PHP runtime | SAFE UNKNOWN (requires ≥ 7.4 per core/plugins) |
| Theme | custom `iseoblog` |
| Security/cache plugins | Jetpack present; WP-Optimize present; Akismet present |
| REST | Public `/wp-json/` works; Jetpack + Yoast namespaces present |
| Custom headers / JS challenge | Admin HTTP client blocked — browser/HITL needed for Admin |
| Staging | None |
| Backup | Operator full Beget backup confirmed 2026-07-24 |

**Not an install approval.**

---

## 22. Database Access State

| Item | State |
|------|-------|
| Credential source | production `wp-config.php` (exists; secrets **not** copied) |
| phpMyAdmin URL | recorded as metadata only; **not opened** |
| Direct DB access | **NOT AUTHORIZED / NOT REQUIRED** |
| Future DB access | requires separate explicit charter |

---

## 23. Evidence Collected

- SFTP inventory (sanitized) under programme scratch (local, not for Git secrets)
- Bounded reads: `.htaccess`, theme templates, form handler structure lines (redacted)
- Public REST: site, types, taxonomies, pages, posts, categories
- Public page GETs for ownership classification
- Local access presence validation (no secret values printed)

---

## 24. Conflicts

| Topic | Conflict | Resolution posture |
|-------|----------|--------------------|
| “Main pages are static HTML” vs WP front page | Homepage is WP-routed template that looks static | Record as hybrid: **SHARED_BUT_WORDPRESS_RENDERED** |
| `home.html` vs `/` | Two artifacts | Treat `/` (WP template) as live homepage unless operator proves otherwise |
| Web-KP existence | Operator context vs no dedicated route found | SAFE UNKNOWN; candidates listed |

---

## 25. SAFE UNKNOWN

- Exact PHP runtime version
- Exact active/inactive plugin matrix (Admin UI)
- ACF field groups / options pages contents
- Menus / widgets contents
- Which URL is the operator “web-KP”
- SMTP delivery path details
- Maintained canonical source outside production
- Whether `services/*.html` pages include PHP `include` of shared partials (PHP-capable HTML)

---

## 26. Audit Stop Condition

Reached:

- no production write;
- no upload;
- no WordPress save;
- no database login;
- no plugin install/activation;
- no token creation;
- no WPilot REST smoke;
- no cache purge;
- no Localhost / Storage / registry / ATLAS mutation;
- no Git stage/commit/push.

Await operator review.

---

*ISEO-SU READ-ONLY PRODUCTION AUDIT v1 · 2026-07-24 · secrets excluded.*
