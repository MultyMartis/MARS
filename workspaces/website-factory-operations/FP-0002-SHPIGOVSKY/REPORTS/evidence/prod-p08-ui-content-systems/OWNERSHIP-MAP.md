# PROD-P08 — Ownership Map (Stage A)

**Date:** 2026-08-14  
**Sources:** local FP-0002 `WORDPRESS/` + public production HTTP inspect (`/specyalisty/kostyuk/`)  
**Production mutation:** none (backup gate blocked)  
**Status:** Ownership clear enough to implement after Layer A; no ambiguous STOP on workstreams A–E at mapping level.

Canonical roots:

* Theme: `WORDPRESS/theme/shpigovsky/`
* Plugin/ACF PHP: `WORDPRESS/plugins/shpigovsky-core/`
* ACF JSON: `WORDPRESS/acf-json/`
* Production docroot theme: `/home/s/shpigovsky/shpigovsky.ru/public_html/wp-content/themes/shpigovsky/`

---

## 1. Slider navigation

### JS owner

`assets/js/v9-shell.js` — Swiper initializers:

| Init | Selector | Pagination | Navigation arrows today | Hero? |
|------|----------|------------|-------------------------|-------|
| `initHomeGallery` | `[data-gallery-slider]` | `[data-gallery-pagination]` | NO (`navigation: false`) | NO |
| `initServicesCategoryGalleries` | `[data-services-category-gallery]` | `[data-gallery-pagination]` (shared options) | NO | NO |
| `initReviews` | `[data-reviews-slider]` | `[data-reviews-pagination]` | NO | NO |
| `initSpecialists` | `[data-specialists-slider]` | `[data-specialists-pagination]` | NO | NO |
| `initHomeArticlesSlider` | `[data-articles-slider]` | `[data-articles-pagination]` | NO | NO |
| `initInfrastructureSliders` | `[data-inf-slider]` | **none** (`pagination: false`) | NO | NO — **out of P08 mobile-dots rule** (no dots) |
| `initHomeHeroSlider` | `[data-hero-slider]` | `[data-hero-pagination]` (ACF dots toggle) | optional `[data-hero-prev]` / `[data-hero-next]` | **YES — EXCLUDE** |
| `initServicesHeroSlider` | `[data-services-hero-slider]` | `[data-services-hero-pagination]` | optional prev/next | **YES — EXCLUDE** |

Shared gallery options factory: `window.shpigovskyGallerySwiperOptions` (Home gallery + `/uslugi/` category galleries + articles fallback).

### CSS owner

Primarily operator-owned `assets/css/v9-style.css`:

* Hero: `.hero__pagination`, `.hero__nav`, `.services-inner-hero-v2__pagination`, `.services-inner-hero-v2__nav`
* Non-hero dots: `.reviews__pagination`, `.home-gallery__pagination`, `.specialists__pagination`, `.home-articles__pagination`, `.services-category-section-v2__gallery-pagination`

**P08 CSS plan:** additive scoped rules (prefer new `fp02-*-mobile-slider-nav.css` or tightly scoped block in existing additive CSS) — **do not** globally restyle every `.swiper-pagination`. Explicitly exclude `.hero__*` and `.services-inner-hero-v2__*`.

### Markup owners (partials)

* Home gallery / specialists / reviews / articles: `template-parts/home/*`
* Alcohol / subdivision reuse: `template-parts/service/**`, comfort/specialists partials
* Services hub category galleries: services hub templates
* Heroes: Home hero partial + services-inner-hero-v2

### Inventory rule for conversion

Convert at `max-width: 767px` **only** non-Hero sliders that currently enable dot pagination.  
Infrastructure G1–G4 (`[data-inf-slider]`) already have no dots — no change unless QA finds dots.

### Hero exclusion contract

```text
BOTH HERO SLIDERS UNCHANGED
```

Selectors to protect: `[data-hero-slider]`, `[data-services-hero-slider]`, and their pagination/nav classes.

---

## 2. Typography

### Hardcoded / static PHP maps

| Owner file | Role |
|------------|------|
| `inc/v9-static-content.php` | Large V9 static fixture strings (cards, FAQ, CTAs, specialists fixtures) |
| `inc/reusable-blocks-helpers.php` | Block heading/link/CTA fallbacks |
| `inc/contacts-helpers.php` | Contacts fallbacks |
| `inc/service-section-helpers.php` | Section chrome fallbacks (i18n-wrapped) |
| `inc/service-general-helpers.php` | Leaf service helpers (P07 protected) |
| `inc/services-hub-helpers.php` | Hub helpers (P07 protected) |
| `inc/institutional-about-v9-content.php` | O-centre institutional copy |
| Theme partials / menus labels | Scattered UI chrome |

### ACF / Admin text

* Home / Services hub / Service section / Service general / Comfort / Reviews / Contacts / Blog article meta / Generic page lead+body
* Options pages: reusable blocks (`fp02-block-*`)
* WYSIWYG / HTML-capable: `generic_page_body`, article body (`post_content` + ACF WYSIWYG where used), service editorial fields
* Plain text: titles, leads, short descriptions, CTA labels, card headings

### Post/page content

* `page` / `service` / `post` titles + ACF fields + selected `post_content`
* Specialist child pages: currently `generic_page_lead` / `generic_page_body` (+ featured image)

### Do-not-typograph

URLs, slugs, emails (machine), HTML tags/attrs, shortcodes, JSON, CSS/JS, field keys, hashes, `tel:` href targets, analytics.

### Storage strategy (per owner)

| Context | Representation |
|---------|----------------|
| PHP HTML templates / HTML ACF | `&nbsp;` / HTML entities OK if render path is HTML |
| Plain text ACF + `esc_html` | Unicode NBSP `U+00A0` (never literal `&nbsp;` string) |
| Titles / menus | Unicode NBSP preferred |
| No global runtime typography filter | Prefer canonize at owner; bounded helper only if duplication requires it |

### Mutation map (to be filled at implement)

Counts by: hardcoded strings, pages, services, specialists, blog posts, options, ACF fields — with before/after snapshots. Exact-object DB updates only; no revision bulk rewrite.

---

## 3. Lifebuoy scroll motion

| Concern | Owner |
|---------|-------|
| Markup mount | `template-parts/layout/body-start.php` — `.fp02-lifebuoy-parallax` / `[data-fp02-lifebuoy-parallax]` |
| CSS | `assets/css/fp02-lifebuoy-parallax.css` — `position: fixed` layer; transform via CSS vars |
| JS | `assets/js/fp02-lifebuoy-parallax.js` — scroll progress → `--fp02-lb-x/y/scale/rotate` |
| Enqueue | `inc/assets.php` |
| Scroll source | `window.scrollY / (scrollHeight - innerHeight)` |
| Transform | CSS `transform: translate3d(var(--fp02-lb-x), var(--fp02-lb-y), 0) scale(...) rotate(...)` |
| Reduced motion | Freezes at `t=0.28` via `prefers-reduced-motion: reduce` |
| Sticky/fixed | Outer fixed full-viewport; image absolute |

### Suspected WebKit failure mode (to verify at implement)

Safari historically fails to reliably recomposite when **transform depends on CSS custom properties** updated from JS. Windows/Android Chromium update successfully → motion works; Apple appears “static”.

Preferred fix direction (scroll-driven, compositor-friendly):

* Keep rAF + passive scroll listener
* Apply `element.style.transform = ...` directly (or dual-write vars + transform)
* Preserve amplitude/easing model
* Keep reduced-motion freeze
* Avoid unrelated architectural rewrite

Physical Apple QA: operator-required if environment cannot run real iOS/macOS Safari.

---

## 4. Specialists

### Object model (current)

| Item | Value |
|------|-------|
| Type | `page` children of `/specyalisty/` (parent slug `specyalisty`, historical ID ~1030) |
| Template | `page-templates/generic.php` → `template-parts/generic/content-page.php` |
| Dedicated CPT | **None** |
| Dedicated Specialist ACF group | **None** (gap for P08) |
| Card data | Auto from child pages via `shpigovsky_get_specialists_cards()` |
| Role on cards | `post_excerpt` → meta `_shpigovsky_specialist_role` → content excerpt |
| Portrait | Featured image → meta photo asset → placeholder SVG |

### Known objects (local inventory CSV; confirm live IDs via DB/Admin before migrate)

| Slug | Title (historical) |
|------|--------------------|
| `shipovsky` | Сергей Юрьевич Шпиговский |
| `kazakov` | Максим Михайлович Казаков |
| `kostyuk` | Дарья Владимировна Костюк |
| `shapiguzova` | Шапигузова Татьяна Андреевна |

### Костюк live content ownership (public HTTP 2026-08-14)

Rendered via generic lead/body (ACF), not structured specialist fields:

* Name: page title
* Portrait: featured image
* Role: «Психолог, EMDR терапевт, телесно-ориентированный терапевт»
* Experience: «Опыт — 2,5 года»
* Specialty / Education / Specialization / Principles: freeform body sections
* Certificates/diplomas: images in body (bottom) — need gallery migration

### P08 target ownership

New ACF group (exact-group only), e.g. `group_fp02_specialist_profile`:

* portrait (or reuse featured image as SoT)
* role / profession
* experience
* specialty
* education
* specialization
* principles / approach
* additional_information (legacy catch-all)
* certificates gallery (gallery / repeater of images)

Frontend: site-native structured specialist template (not foreign card system); empty sections hidden; Fancybox if already cleanly available on route.

Preserve slugs/permalinks/SEO; no invented credentials.

---

## 5. Blog reading time

| Concern | Owner |
|---------|-------|
| Post type | `post` |
| ACF group | `group_fp02_blog_post_article_meta` (`WORDPRESS/acf-json/group_fp02_blog_post_article_meta.json`) |
| Field | `article_reading_time` / `field_fp02_article_reading_time` — **number**, min 0, label currently English «Reading time» |
| Render helper | `shpigovsky_get_blog_card_reading_time()` in `inc/blog-helpers.php` |
| Templates | `template-parts/blog/single-meta.php`, `single-hero.php`, archive card |
| Current behavior | Manual only; if `<= 0` → **empty string** (no auto calc) |
| Pluralization | Already Russian: `минута` / `минуты` / `минут` + `на чтение` |

### P08 plan

1. Reuse existing field; localize label/instructions («Время на чтение»; optional; empty → auto).
2. When empty/0: strip HTML/shortcodes from readable article text → word count → `/ 190` → `ceil` → min 1.
3. Do **not** write calculated values back to DB.
4. Priority: `MANUAL → AUTO`.

---

## 6. Cross-cutting / P07 protection

Do not regress:

* Desktop card equal-height / mobile natural heights
* Guest Visit contextual CTA
* Approach cards Admin/FE
* Generic Content long-form + reusable blocks
* FU01 Lorem/DEMO suppression on hub/alcohol helpers

ACF: exact affected groups only; no broad sync; preserve P07 groups.

WPilot: READ only; `write_enabled=false`.

---

## 7. Ambiguity / STOP subtasks

| Workstream | Ambiguity | Action |
|------------|-----------|--------|
| A Sliders | None material | Proceed after backup |
| B Typography | Large surface; HTML safety per field | Proceed bounded; stop individual fields if shortcode/HTML risk |
| C Lifebuoy | Root cause hypothesis strong; physical Apple QA external | Implement WebKit-safe path; flag operator physical QA |
| D Specialists | Mapping of freeform body → fields needs per-object care | Preserve unmapped text in additional_information |
| E Reading time | Field exists | Reuse; add auto path |

**No workstream ownership STOP** beyond the global **backup gate**.
