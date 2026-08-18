# Forge WordPress — Code ownership boundaries standard v1

**ID:** FW-S-32  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Extends:** [THEME-ARCHITECTURE](FORGE-WORDPRESS-THEME-ARCHITECTURE-STANDARD-v1.md) (FW-S-03) · [FUNCTIONALITY-PLUGIN](FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md) (FW-S-04)  
**Evidence:** FP-0002 `shpigovsky-core` vs theme `shpigovsky`; MU mail suppress; `mars-runtime` leftover

---

## 1. Survival test (primary rule)

Ask of every piece of code or schema:

**MUST THIS SURVIVE A THEME CHANGE?**

| Answer | Owner |
|--------|--------|
| **Yes** — CPTs, taxonomies, ACF schema, Site Settings, SEO storage, forms business logic, search index contract, Activity Log, importer, Admin modules, REST/AJAX business endpoints | **Functionality plugin** |
| **No** — markup, presentation CSS/JS, template routing, visual motion | **Theme** |
| **Must load even if all plugins in the plugins screen are deactivated** (rare) | **MU-plugin** — only infrastructure-critical |

If the answer is yes and the code still lives in the theme, that is a **BLOCKER** for a new site’s architecture review.

---

## 2. Theme owns

| Owns | Examples |
|------|----------|
| Visual templates | `front-page.php`, `page-*.php`, `single-{cpt}.php`, `404.php` |
| Component markup | `template-parts/components/*`, `template-parts/sections/*` |
| Frontend assets | compiled CSS/JS, fonts, theme images, sprite |
| Presentation-specific behavior | menu open/close animation, accordion height, slider UI, decorative parallax |
| Theme `functions.php` bootstrap | enqueue, `after_setup_theme`, `register_nav_menus`, image sizes **for presentation** |
| Template-only helpers | “render this card markup from already-resolved data” |

Theme may **consume** plugin helpers (`get_site_phone()`, SEO title). Theme must not **register** those systems.

---

## 3. Functionality plugin owns

| Owns | Examples |
|------|----------|
| CPTs / taxonomies | `register_post_type`, `register_taxonomy` |
| ACF schema | local JSON load path; field groups; options pages |
| Site Settings | options SoT, sanitization, capability |
| SEO ownership | title/description storage, `wp_head` output, verification/analytics **empty-safe** |
| Search | REST/AJAX contract, query groups, Admin config |
| Forms business logic | handler, validation, mail composition, rate limits |
| Activity Log | table, Admin screen, retention |
| Importer | DOCX (or equivalent) Admin tool |
| Reusable business modules | reading time calc, TOC ID assignment **if content-owned**; social registry |
| Admin functionality | Dashboard widget, menu hygiene, editor restrictions |
| Module registry | enable/disable, phase flags |
| Uninstall/deactivation | drop or retain tables per module contract |

One project functionality plugin is the default. Split only with a WAD.

---

## 4. MU-plugin owns (narrow)

MU-plugins are **not** a dumping ground.

**Allowed examples:**

- temporary cutover `pre_wp_mail` suppression **with** owner, created date, REMOVE WHEN, launch flag row
- environment/bootstrap guards required before normal plugins load (documented)

**Forbidden examples:**

- CPT registration
- ACF
- forms
- SEO
- “we might need this on every request”
- leftover QA scripts
- anything that should appear in the plugins screen so an operator can disable it

Every MU file is a **temporary infrastructure** row until proven permanent. Permanent MU still needs a WAD.

---

## 5. Third-party plugins

Governed by [PLUGIN-GOVERNANCE](FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md). They must not silently become a second owner of SEO, sitemap, forms, cache, or analytics.

---

## 6. WPilot

`metacode-wpilot` is **operational**. It is not the project functionality plugin and not the theme.

---

## 7. Decision table

| Concern | Theme | Functionality plugin | MU | Third-party |
|---------|:-----:|:--------------------:|:--:|:-----------:|
| `single-service.php` markup | ● | | | |
| `register_post_type('service')` | | ● | | |
| ACF JSON | | ● | | |
| Consultation AJAX | | ● | | |
| `v9-style.css` / component SCSS | ● | | | |
| Menu walker presentation | ● | | | |
| Native sitemap filters | | ● | | |
| SMTP transport | | | | ● (one) |
| Mail suppress until SMTP | | | ● (temp) | |
| Page cache | | | | ● (one) |
| WPilot REST | | | | operational plugin |

---

## 8. Violations

| Violation | Severity |
|-----------|----------|
| CPT / ACF / business REST in theme | **BLOCKER** |
| Forms handler only in theme JS with no plugin owner | **BLOCKER** |
| MU used for features | **BLOCKER** |
| Two SEO outputters | **BLOCKER** |
| Presentation templates inside the functionality plugin | **MAJOR** |

---

*FW-S-32 v1 — survival test first; FW-S-03/04 remain structural detail.*
