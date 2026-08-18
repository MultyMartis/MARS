# ISEO-SU GLOSSARY PAGE_SCENE SERVICES ALIGNMENT EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT  
**Date:** 2026-08-18  
**Production stamp:** `20260818T062716Z`

---

## 1. Operator Requirement

Replace the glossary `page_scene` (archive + all public term singles) with an exact structural copy of the current production `/services.html` `page_scene`. Adapt only glossary content. Omit `.page_scene__rates`. CTA label `Подробнее` → `#SecondScreen` with existing smooth-scroll behavior. No new CSS. No `/services.html` mutation. No glossary article/DB mutation.

## 2. Source Hero

| Field | Value |
|-------|-------|
| Public URL | `https://i-seo.su/services.html` |
| Authoritative source file | docroot `services.html` (static PHP-capable HTML) |
| Block | `<div class="page_scene">` inside `<header id="header_template">` |
| SHA-256 (pre and post task) | `ce6ee776b5d82936ccb1d7ae9f1482c7362d60eb87d9395b95dc7615d8288bac` — **unchanged** |

Copied structure (rates not carried):

- `page_scene` → `container` → `row` → `page_scene_inner`
- `page_scene__description`: breadcrumbs, H1, optional `span`, `page_scene__btns` / `page_scene__btn_order`, `see_more_btn`
- `page_scene__info` / `page_scene__info_wrap` / existing asset `/img/services_title_img.svg`

Services CTA in source: `<a href="#callback__FORM_popup" class="modalbox page_scene__btn_order">Бесплатная консультация</a>`. Global `js/common.js` binds `$(".modalbox").fancybox()`. Glossary CTA keeps `page_scene__btn_order` and **omits** `modalbox`.

## 3. Previous Glossary Hero

Previous archive/single heroes were the privacy-policy compact `page_scene`: breadcrumbs + H1 + `see_more_btn` only (no illustration column, no `page_scene__btns`, no description `span` in the hero). Archive intro lived in `content_block` as a `<p>`. `id="SecondScreen"` was already on `<main>`.

Production pre-task copies:

- `archive-glossary.php` / `single-glossary.php` (theme root)
- rollback dir `projects/iseo-su-site-ops/_glossary-scratch/hero-align/rollback-20260818T062716Z/`
- remote `.bak-glossary-heroalign-20260818T062716Z`

## 4. Implementation

Shared helper: `wp-content/themes/iseoblog/template-parts/content-glossary-page-scene.php`  
Called from `archive-glossary.php` (`context=archive`) and `single-glossary.php` (`context=single`).

| Piece | Archive | Single |
|-------|---------|--------|
| Structure | services `page_scene` | same |
| Breadcrumb | Главная → Глоссарий (current) | Главная → Глоссарий → `the_title()` |
| H1 | `Глоссарий` | `the_title()` |
| Description `span` | exact operator sentence | omitted |
| CTA | `Подробнее` `href="#SecondScreen"` `page_scene__btn_order` | same |
| Rates | not rendered | not rendered |
| `#SecondScreen` | existing `<main>` (search / alphabet / listing) | existing `<main>` (article) |

Asset path translated from root-relative `img/services_title_img.svg` to `/img/services_title_img.svg` so WP routes under `/glossary/` resolve the existing production SVG.

Smooth scroll: existing `see_more_btn` handler in `js/common.js` reused as-is. Additional glossary-only `wp_add_inline_script` on `iseoblog-common` duplicates that animate for `.page_scene a.page_scene__btn_order[href='#SecondScreen']`. No global JS file change. Native hash jump remains if JS is off.

## 5. Archive Behavior

Anonymous `https://i-seo.su/glossary` HTTP **200**. One `page_scene`. H1 `Глоссарий`. Exact description once in hero `span`. CTA `Подробнее` → `#SecondScreen`. Zero `.page_scene__rates`. Search + alphabet unchanged. **184** unique published term links.

## 6. Single Behavior

Checked: `/glossary/apdejt-algoritma`, `/nofollow`, `/geo`, `/e-e-a-t`, `/core-web-vitals`, `/robots-txt`, `/kanonicheskij-url`, `/snippet`. All HTTP **200**. Dynamic breadcrumb includes current title. No hero description / empty span / archive sentence. Article excerpt/body/related terms unchanged (still inside `#SecondScreen`).

## 7. SecondScreen / Smooth Scroll

Exactly one `id="SecondScreen"` per page, on `<main>`. Playwright: desktop and mobile click on `Подробнее` increased `scrollY` (archive desktop 0 → 1050; nofollow mobile 0 → 621). `see_more_btn` continues to use production `common.js`.

## 8. No-New-Style Validation

No new CSS file, selector, or inline style. No glossary-specific background. Decorative image is the existing services SVG. Visual system is existing `main.css` / `media.css` `page_scene*` rules.

## 9. Files Changed

Local package / production theme:

- `archive-glossary.php` (replaced)
- `single-glossary.php` (replaced)
- `template-parts/content-glossary-page-scene.php` (new)
- `inc/glossary-helpers.php` (enqueue only)

Not changed: `services.html`, glossary post bodies, CPT exposure, sitemap, menus, `js/common.js`, shared CSS.

## 10. Production Validation

| Check | Result |
|-------|--------|
| Archive 200 / one scene / no rates / exact desc / CTA | PASS |
| 184 unique term links | PASS |
| Search `glossary_q=nofollow` | PASS (1 term; no rates) |
| 8 singles 200 / no hero desc / CTA | PASS |
| Playwright scroll archive + 2 singles, desktop + mobile | PASS |
| `/services.html` SHA + consult + rates | PASS unchanged |
| `/`, `/blog/`, `/tariff-calc`, `/offers`, `/privacy-policy.html` | 200, no PHP fatal |
| Mobile 390px glossary `scrollWidth` 395 vs 390 | **5px** — WP theme `style.css` `.row` padding on glossary routes; `services.html` does not load that file. No new CSS added. |

## 11. Rollback

1. Restore the four theme files from `*.bak-glossary-heroalign-20260818T062716Z` or local `rollback-20260818T062716Z/`.
2. Delete only the new `template-parts/content-glossary-page-scene.php` if restoring the previous archive/single heroes that inlined markup.
3. Do not revert glossary posts/statuses.

## 12. Final State

Glossary archive and singles use the services `page_scene` visual system with glossary content, `#SecondScreen` CTA, and no rates. `/services.html` and the 184 published articles are unchanged.

---

*Evidence v1 · 2026-08-18 · stamp 20260818T062716Z.*
