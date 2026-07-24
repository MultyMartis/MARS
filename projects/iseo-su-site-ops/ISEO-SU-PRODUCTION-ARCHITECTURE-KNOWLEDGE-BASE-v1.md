# ISEO-SU PRODUCTION ARCHITECTURE KNOWLEDGE BASE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-COMPLETE-PRODUCTION-ARCHITECTURE-ROUTE-KNOWLEDGE-CAPTURE  
**Site:** https://i-seo.su/  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Status:** COMPLETE / ARCHITECTURE KNOWLEDGE READY FOR SITE WORK  
**Evidence date:** 2026-07-24  
**Mode:** read-only production discovery (SFTP + public HTTP/REST + Playwright WP Admin; no saves)

No secrets, credentials, customer proposal bodies, or mail recipients are stored here.

---

## 1. Knowledge Status

| Field | Value |
|-------|-------|
| Knowledge package | **READY** for ordinary site work |
| Generic onboarding | **NOT REQUIRED** after this package |
| Production mutated in this task | **No** |
| WPilot bridge / writes / REST | **Disabled / not invoked** |
| Remaining SAFE UNKNOWN | Named; **do not block** ordinary work |
| Authority for future tasks | See §24 and [ISEO-SU-TASK-ROUTING-GUIDE-v1.md](ISEO-SU-TASK-ROUTING-GUIDE-v1.md) |

**Primary companions:**

1. [ISEO-SU-TASK-ROUTING-GUIDE-v1.md](ISEO-SU-TASK-ROUTING-GUIDE-v1.md)
2. [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)
3. This knowledge base
4. Component maps (page/source, WP objects, static PHP, forms/web-KP, global components)
5. Historical Phase 0–6C-P reports (immutable evidence)

---

## 2. Executive Architecture Summary

i-seo.su is a **hybrid production site** on Beget:

1. **WordPress root install** in the same docroot as marketing files (`public_html`).
2. **Physical `.html` marketing trees** (`*.html`, `services/`, `cases/`) coexist and win when the file exists (Apache `!-f` / `!-d` before WP rewrite).
3. **`.html` is PHP-capable** via `.htaccess` `AddType application/x-httpd-php .html .htm`.
4. **Homepage `/`** is a WordPress page (`glavnaya`, id 1732) rendered by theme template `page-home.php` that embeds a full static-like document and shared `/css` `/js` — **not** classic WP chrome / `the_content`.
5. **Parallel file** `home.html` is publicly reachable and is a **legacy/parallel** drift twin of the live homepage template.
6. **Blog** is WordPress-owned (`/blog`, template `page-blog.php`, singles under permalink `/blog/%postname%.html`).
7. **Calculator / tariffs** are **hybrid**: WP page `/tariff-calc` + ACF field groups + theme `tarif-calc.php` + shared `js/common.js` + root `*__FORM.php` mail handlers (also copied under `services/**`).
8. **Commercial proposals (“web-KP” candidate)** = CPT `offer` + page `/offers` + template `single-offer.php` + ACF group «Предложения». Exact operator nickname “web-KP” remains a naming SAFE UNKNOWN; the technical surface is mapped.
9. **Report Hub** at `/report-hub/` is a **sibling product surface**, not core marketing Site Ops by default.
10. **Active theme:** `iseoblog` only. **ACF PRO** active. **Yoast**, **Jetpack**, **WPilot RC6** active. **WP-Optimize** and **Akismet** inactive on disk/Admin.

---

## 3. Production Runtime Layout

| Role | Location |
|------|----------|
| Hosting | Beget |
| Docroot / WP root | `…/i-seo.su/public_html` (account redacted) |
| Staging | **Absent** |
| WordPress | 7.0.2 (generator + `version.php`) |
| PHP runtime | **SAFE UNKNOWN** (Site Health parse inconclusive; core requires ≥ 7.4) |
| Theme | `wp-content/themes/iseoblog` |
| Shared assets | `css/`, `js/`, `libs/`, `img/`, `fonts/`, `favicon/`, `video/` |
| Custom apps | `report-hub/`, `reports/` |
| Form handlers | docroot `*__FORM.php` + copies under `services/**` |
| WPilot | `wp-content/plugins/metacode-wpilot/` (active RC6) |
| RC5 rollback sibling | `wp-content/plugins/.mars-rollback-metacode-wpilot-rc5-phase6c-r/` |

No on-server Node/Gulp source tree (`package.json` / `gulpfile` / `src` / `scss` absent).

---

## 4. Request Routing Model

```
Request URL
  → HTTPS / www→apex redirects (.htaccess)
  → If physical file or directory exists → serve it
       (HTML may execute as PHP)
  → Else → WordPress front controller index.php
       → page / post / CPT / taxonomy templates
```

**Implications:**

- Editing a WordPress page does **not** change a same-path `.html` file if the file exists.
- Deleting or renaming a physical file can suddenly expose a WP route (or 404).
- `home.html` and `blog.html` do **not** own `/` and `/blog`.

---

## 5. WordPress Architecture

| Setting | Value |
|---------|-------|
| `show_on_front` | `page` |
| Front page | id **1732**, slug `glavnaya`, template **`page-home.php`** |
| Posts page | **not set** (`— Выбрать —`) |
| Blog UI page | id **1730**, slug `blog`, template **`page-blog.php`**, URL `/blog` |
| Tariff page | id **1734**, slug `tariff-calc`, template **`page-tariffcalc.php`** |
| Offers page | id **1377**, slug `offers`, template **default**, URL `/offers` |
| Permalink | custom **`/blog/%postname%.html`** |
| Public pages via REST | exactly these 4 published pages |
| CPT | `offer` (public, has_archive, UI visible; REST type not public — 401) |
| Nav location | `menu-1` / Primary; WP menu name «Меню 1» |
| ACF groups | «Записи», «Настройки калькулятора», «Настройки каналов и тарифов», «Предложения» |

Active plugins (Admin, 2026-07-24): ACF PRO, Auto Version, Cyr-To-Lat, Disable Gutenberg, Duplicate Page, FeedbackWP/Rate My Post, Jetpack, MetaCODE WPilot, Post View Count, Simple User Avatar, Yoast SEO.

Inactive: Akismet, Hello Dolly, No Category Base (WPML), WP-Optimize.

---

## 6. Static and PHP Marketing Architecture

Root marketing HTML (non-exhaustive): `about.html`, `services.html`, `contacts.html`, `cases.html`, `reviews.html`, `partners.html`, `bonuses.html`, `career.html`, `guarantees.html`, `privacy-policy.html`, `user-agreement.html`, `cookie-files-policy.html`, plus verification files and `readme.html`.

Trees: `services/**` (seo, adv, audit, development, serm, ai-optimization), `cases/**`, `docs/`, `video/`.

`sitemap-static.xml` lists **71** marketing URLs. Yoast `sitemap.xml` is a sitemap **index** that includes `sitemap-static.xml` plus WP sitemaps.

Marketing pages embed header/footer markup and load shared `css/main.css`, `css/media.css`, `js/common.js`, `libs/*`. They are **not** driven by WP menus for chrome (theme topbar is a separate WP chrome).

---

## 7. Hybrid and Composite Surfaces

| Surface | Why hybrid |
|---------|------------|
| `/` homepage | WP routing + hardcoded template + shared static assets + calculator/tariff/forms markup |
| `/tariff-calc` | WP page + ACF calculator settings + theme part + shared JS + mail handlers |
| Blog chrome | WP templates + shared `/css` `/js` + Rate My Post + common.js forms |
| Tariff cards on marketing HTML | Static markup + `js/common.js` + `tariff_*__FORM.php` |
| Offers / proposals | WP CPT + ACF + `single-offer.php`; listing page `/offers` |

---

## 8. Homepage

| Question | Answer |
|----------|--------|
| Front-page setting | Page `glavnaya` (1732) |
| Template | `page-home.php` («Home») |
| Editor content used? | **No** (content length 0 on edit screen) |
| ACF on home edit? | UI present; **0** fields attached to this page |
| Rendering | Full HTML document hardcoded in template; assets from docroot `css/`, `js/`, `libs/` |
| `get_header` / `get_footer` | **Not used** |
| `home.html` | Public **200**; parallel/legacy; **same title**; different byte size (~59KB vs ~64KB template) |
| Safe edit | Prefer **theme `page-home.php`** for live `/`; treat `home.html` as drift twin — sync or leave untouched deliberately |
| Backup | Theme file + optional `home.html` if also published/linked |

---

## 9. Blog

| Item | Detail |
|------|--------|
| Hub URL | `/blog` (trailing slash normalizes) |
| Owner | WP page 1730 + `page-blog.php` + post loop |
| Singles | `single.php` + ACF group «Записи»; URL `/blog/{slug}.html` |
| Categories | `/blog/category/{slug}` (news, seo, context, development, geo) |
| Tags | Disallowed in `robots.txt` (`/tag/`) |
| Parallel file | `blog.html` — **LEGACY_OR_PARALLEL**, not live `/blog` |
| Chrome | Theme `header.php` / `footer.php` + `content-topbar.php` / `content-footer.php` / `content-mobilemenu.php` |
| Shared JS | Theme enqueues docroot `js/common.js` among others |

---

## 10. Marketing Pages

Class: **STATIC_HARDCODED** (PHP-capable HTML).  
Edit via SFTP to the physical file. Shared chrome is **copied markup**, not WP menus. Forms post via `js/common.js` to root handlers (or relative copies under `services/`).

Note: `/services.html` returned **500** once during discovery and **200** on retry — treat as intermittent risk; validate after edits.

---

## 11. Calculator and Tariffs

| Layer | Owner |
|-------|-------|
| Public WP UI | `/tariff-calc` → `page-tariffcalc.php` → `template-parts/tarif-calc.php` |
| ACF data | Group «Настройки калькулятора» (keys include `seo_rate`, `dev_rate`, `text_rate`, `tariffs`, `k_*`, …); group «Настройки каналов и тарифов» for channel/tariff content |
| Front-end logic | `js/common.js` |
| Mail handlers | `calc__FORM.php`, `tariff_1__FORM.php`…`tariff_4__FORM.php` (+ service-tree copies) |
| Theme mirrors | `content-tarifs-*.php`, `content-calc-*.php`, popups |
| Marketing pages | Calculator/tariff markup embedded in homepage template and many HTML pages |

**Do not** submit live calculator/mail requests in audits. Structural only.

---

## 12. Forms and Handlers

Shared client: `js/common.js` posts to endpoints such as:

`callback__FORM.php`, `page__FORM.php`, `audit__FORM.php`, `calc__FORM.php`, `tariff_1..4__FORM.php`, `bonus__FORM.php`, `career__FORM.php`, `partners__FORM.php`, `review__FORM.php`

Server: PHP `mail()`-style handlers; recipient emails **not recorded**. SMTP path **SAFE UNKNOWN**. Spam protection: Akismet **inactive**; no dedicated CAPTCHA plugin identified.

See [ISEO-SU-FORMS-CALCULATORS-AND-WEB-KP-MAP-v1.md](ISEO-SU-FORMS-CALCULATORS-AND-WEB-KP-MAP-v1.md).

---

## 13. Web-KP and Offers

| Evidence | Finding |
|----------|---------|
| `/web-kp/`, `/kp/`, `/offers.html` | **404** |
| `/offers` | WP page 1377, title «Предложения», generator WordPress |
| CPT `offer` | Registered public + archive; Admin list reachable (~20 rows observed; titles **not** harvested) |
| Single template | `single-offer.php` + ACF keys `site`, `region`, `tariff(s)`, `discount`, `deadline`, `stages`, `ways`, `growth`, `audit_file` |
| Robots | `Disallow: /offer/*` and `/blog/offer/*` |
| REST type | Not publicly readable (401) |
| Operator label “web-KP” | **SAFE UNKNOWN** naming; **technical ownership mapped** as offers/CPT/ACF |

Treat proposal content as **protected / private**. Do not dump customer KP bodies into Git.

---

## 14. Header, Footer, and Shared Components

| Surface | Chrome owner |
|---------|--------------|
| Marketing HTML / `page-home.php` | Hardcoded markup + shared CSS/JS |
| WP blog / tariff / offer templates | `header.php` + `content-topbar.php` + `footer.php` + `content-footer.php` + mobile menu |
| WP Primary menu | Exists («Меню 1») but theme topbar also contains **hardcoded** service links |

**Task impact:** a “header change” may require **both** static HTML files **and** theme template-parts — never assume one channel updates all.

---

## 15. Theme and Plugin Dependencies

Architecture-relevant only:

| Component | Role |
|-----------|------|
| `iseoblog` | All WP templates / CPT registration / enqueues |
| ACF PRO | Blog fields, calculator settings, channel/tariffs, offers |
| Yoast SEO | Sitemap index + SEO metaboxes |
| Jetpack | Present/active; WAF dir on disk |
| WPilot RC6 | Active; bridge/writes off; token local-only; REST not for Site Ops content yet |
| Disable Gutenberg | Classic editor posture |
| Rate My Post / Post View Count | Blog engagement |
| WP-Optimize | **Inactive** — do not assume cache purge behavior |
| Cyr-To-Lat | Slug transliteration |

---

## 16. ACF and CPT Structures

| Group ID | Title | Primary use |
|----------|-------|-------------|
| 19 | Записи | Blog post structured fields |
| 1761 | Настройки калькулятора | Calculator constants/rates/tariffs on `/tariff-calc` |
| 1742 | Настройки каналов и тарифов | Channel stages/tariff packages |
| 1382 | Предложения | CPT `offer` commercial proposals |

CPT `offer` supports title/editor/thumbnail; rewrite `with_front => false`.

---

## 17. Shared Assets

| Path | Role | Blast radius |
|------|------|--------------|
| `css/main.css`, `css/media.css` | Global marketing + home template | **Sitewide** |
| `js/common.js` | Forms, calculator, tariffs | **Sitewide leads/revenue** |
| `libs/*` | jQuery, Owl, Fancybox, etc. | Sitewide |
| Theme `js/script.js` | Blog/theme behaviors | WP surfaces |
| `wp-content/uploads/` | Media | Content |

---

## 18. Ownership and Historical Context

| Surface | Business owner | Technical history | Runtime SoT |
|---------|----------------|-------------------|-------------|
| Programme / ops | Андрей (operator) | MARS Site Ops | this locus |
| Marketing HTML | i-SEO | **SAFE UNKNOWN** (Андрей / Антон / shared) | production files |
| Homepage live `/` | i-SEO | evolved hybrid | `page-home.php` |
| Blog posts | i-SEO editorial | WordPress | WP DB + ACF «Записи» |
| Calculator settings | i-SEO | ACF + theme | ACF on tariff page + `tarif-calc.php` |
| Offers / KP | i-SEO commercial | CPT + ACF | `offer` + `single-offer.php` |
| Report Hub | sibling programme | separate | `report-hub/` |

Do not invent freelancer attribution beyond operator-known facts.

---

## 19. Safe Editing Rules

1. Classify the route via the ownership matrix **before** editing.
2. Prefer the **runtime source of truth**, not the parallel twin.
3. Never edit `.htaccess`, `wp-config.php`, core, or form handlers without an exact charter.
4. Shared `css/` / `js/common.js` require HITL + broad regression.
5. Do not use WPilot for static HTML, theme PHP, ACF options, offers, or forms until separately chartered.
6. Fresh **Beget full backup** before first production mutation wave.
7. Validate public URL + status + title/marker + no fatal after change.

---

## 20. Backup and Rollback Model

| Layer | Method |
|-------|--------|
| Default pre-change | Full Beget hosting backup (operator) |
| File edits | Keep pre-change copy of exact files; SFTP restore |
| WP content | Native revisions / re-edit; optional WPilot backup only when write path authorized |
| Theme | Restore exact template files from backup |
| WPilot plugin | RC5 rollback sibling retained (cleanup pending); or restore from Beget |
| Database | Beget restore only under DB charter — **not** routine Site Ops |

---

## 21. Validation Model

Minimum after any production change:

1. Target URL status 200 (or expected redirect)
2. Final canonical URL correct
3. Title / H1 / safe marker matches intent
4. No maintenance mode / fatal
5. If shared asset: spot-check `/`, `/blog`, one marketing HTML, `/tariff-calc`
6. If form/calc adjacent: **do not** send real leads; structural smoke only if chartered

---

## 22. Protected Zones

See [ISEO-SU-PROTECTED-ZONES-v1.md](ISEO-SU-PROTECTED-ZONES-v1.md). Default = protect-all until charter names paths.

---

## 23. SAFE UNKNOWN

See [ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md](ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md). Highlights after this capture:

- Exact PHP runtime version
- Operator confirmation that “web-KP” ≡ offers/CPT (technical map ready)
- Mail SMTP vs `mail()` delivery path details
- Canonical offline Git/build source (U-022)
- Exact ACF location-rule dump (groups identified; UI location panels incompletely scraped)
- Why `/services.html` intermittently 500
- Full WP menu item URL list (menu exists; item harvest incomplete)

None of the above blocks ordinary classified site work if the route matrix is followed.

---

## 24. Knowledge Maintenance Rules

1. After material production discovery, update the route matrix + this KB summary; do **not** rewrite historical REPORT files.
2. Task-specific accepted evidence outranks this KB when fresher.
3. Scratch JSON under `_arch-knowledge-scratch/` is **not** authority (gitignored).
4. Never commit secrets, tokens, customer KP content, or handler recipient emails.
5. When architecture drifts, add a dated note and bump affected maps — keep classification vocabulary stable.

---

*ISEO-SU Production Architecture Knowledge Base v1 · 2026-07-24 · read-only capture.*
