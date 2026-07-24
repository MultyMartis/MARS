# ISEO-SU WORDPRESS OBJECT AND TEMPLATE MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-07-24  
**Methods:** public REST + Playwright Admin read-only + SFTP theme read  

## Reading / homepage settings

| Setting | Value |
|---------|-------|
| `show_on_front` | `page` |
| Front page | **Главная** — id 1732 — slug `glavnaya` — template `page-home.php` — link `/` |
| Posts page | **Not set** |
| Permalink | `/blog/%postname%.html` |

## Pages (public)

| ID | Title | Slug | Status | Template | Editor content | ACF fields on edit | Notes |
|----|-------|------|--------|----------|----------------|--------------------|-------|
| 1732 | Главная | glavnaya | publish | page-home.php | empty | 0 | Hardcoded marketing homepage |
| 1730 | Блог | blog | publish | page-blog.php | empty | 0 | Blog hub loop |
| 1734 | Калькулятор тарифов | tariff-calc | publish | page-tariffcalc.php | empty | **157** | ACF-driven calculator |
| 1377 | Предложения | offers | publish | default | empty | 0 | Offers entry; CPT related |

## Posts / archive

| Item | Detail |
|------|--------|
| Hub | `/blog` via page template (not `page_for_posts`) |
| Single | `single.php` + ACF «Записи» |
| Sample public links | `/blog/{slug}.html` |
| Categories | news (157), seo (5), context (3), development (3), geo (2) — counts at capture |
| Category URLs | `/blog/category/{slug}` |
| Tags | present in WP; `/tag/` disallowed in robots |

## CPT

| CPT | Labels | public | has_archive | REST public | Template | Notes |
|-----|--------|--------|-------------|-------------|----------|-------|
| `offer` | Предложения | true | true | no (401 on type) | `single-offer.php` | Admin list ~20 rows; robots disallow `/offer/*` |

## Taxonomies (route-relevant)

`category`, `post_tag`, `nav_menu`

## Templates (theme `iseoblog`)

| File | Role |
|------|------|
| `page-home.php` | Homepage |
| `page-blog.php` | Blog hub |
| `page-tariffcalc.php` | Tariff calc shell |
| `single.php` | Blog singles |
| `single-offer.php` | Offer / KP singles |
| `page.php` | Default pages |
| `archive.php` | Archives |
| `header.php` / `footer.php` | WP chrome |
| `template-parts/content-topbar.php` | Hardcoded+structured top nav |
| `template-parts/content-footer.php` | Footer links |
| `template-parts/content-mobilemenu.php` | Mobile menu |
| `template-parts/tarif-calc.php` | Calculator UI + ACF reads |
| `template-parts/content-tarifs-*.php` | Tariff cards/popups |
| `template-parts/content-calc-*.php` | Calculator fragments |
| `template-parts/cases-*.php` | Case fragments for WP surfaces |

## ACF field groups

| ID | Title | Observed use |
|----|-------|--------------|
| 19 | Записи | Blog post fields (summary, TOC, hero image, read time, materials, …) |
| 1761 | Настройки калькулятора | Rates, tariffs, coefficients (`seo_rate`, `dev_rate`, `tariffs`, `k_*`, …) |
| 1742 | Настройки каналов и тарифов | Channel stages and tariff packages |
| 1382 | Предложения | Offer/KP fields (`site`, `region`, channels, tariff, discount, audit file, growth points, …) |

No `acf-json` directory found on disk. No `acf_add_options_page` in theme `functions.php` (calculator fields appear on tariff-calc page edit).

## Menus

| Item | Value |
|------|--------|
| Location | `menu-1` → Primary |
| Menu name | Меню 1 |
| Theme topbar | Also hardcodes many service URLs |

## Homepage / blog settings summary

Homepage is a **template-static-like WP page**. Blog hub is a **custom page template**, not the native posts page setting.

---

*WordPress object and template map v1 · 2026-07-24.*
