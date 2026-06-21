# BZPM M9.5 — Neutral Root Category UX Specification v1

**Program:** BZPM Product Roadmap  
**Milestone:** M9.5 Neutral Root Category UX  
**Environment:** https://zpm.new-site.space/ (TEST only)  
**Specification UTC:** 2026-06-15  
**Mode:** Specification only — no code, deploy, DB, or image generation  
**Authority:** M7.1 Launch Mode · M8.3 Cleanup · M9 Filter Profile System · live TEST `/katalog/nejtralnoe-oborudovanie` · SITE-002 category/homepage patterns

---

# REPORT — BZPM M9.5 Neutral Root Category UX Specification

## Executive Summary

**Проблема:** корневая категория **Нейтральное оборудование** (`category_id` **79**, URL `/katalog/nejtralnoe-oborudovanie`) сейчас рендерится как **обычный PLP**: sidebar-фильтр + смешанная product grid (**608** active SKU из семи несовместимых семейств). Глобальный фильтр на root **не помогает** — атрибуты столов, ванн, зонтов, тележек и подтоварников требуют разных профилей (M9 Phase 1–3 уже разделены на ветках **80, 207, 301, 322, 326**).

**Решение M9.5:** превратить root **79** в **category-selection hub** — первичный UX = **subcategory grid** на базе существующих **`zpm-cat-card`** / **`zpm-cat-sections`**, без нового визуального языка.

**Рекомендуемая политика (safest launch):**

| Область | Решение |
| --- | --- |
| Primary UX | Subcategory grid (`zpm-cat-card`) |
| Product grid | **Скрыть полностью** на root (Option A) |
| Filter | **Скрыть полностью** на root — special **hub profile** для cat 79 |
| Empty subcategories (0 SKU) | **Не показывать** до появления SKU + card image |
| Chips (`zpm-sub-cat-chips`) | **Убрать** на hub root — заменяются card grid |

**Scope:** specification only. Implementation = отдельный milestone после operator sign-off.

---

## Current Root Page Audit

**URL (TEST):** `https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie`  
**Evidence:** live fetch 2026-06-15 · baseline controller/template `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` · M9 Phase 3 QA (`legacy pool` note for root)

### Page stack (top → bottom)

| # | Block | Present | Implementation | Notes |
| ---: | --- | :---: | --- | --- |
| 1 | Header + megamenu | ✅ | `common/header.twig` + `common/megamenu.twig` | Launch Mode: «Каталог» → `/katalog/nejtralnoe-oborudovanie` (M7.1) |
| 2 | Breadcrumbs | ✅ | `Breadcrumbs` via `category.php` | Главная → **Каталог** → Нейтральное оборудование |
| 3 | Page intro (H1) | ✅ | `Pageintro` via `category.php` | H1 = «Нейтральное оборудование»; **description пустой** |
| 4 | Category layout | ✅ | `product/category.twig` → `section.category` | Desktop: sidebar + content grid |
| 5 | Filter sidebar | ✅ | `sections/filterssidebar.twig` in `aside.category__sidebar` | **Legacy attribute pool** на root (M9 resolver не матчит 79) |
| 6 | Subcategory chips | ⚠️ | `zpm-sub-cat-chips` in `category.twig` | Label «Подкатегории:» виден на live; chips = **direct children с SKU > 0** |
| 7 | Topbar (sort / view / filters) | ✅ | `category__topbar--mobile` | Sort «Умолчанию»; view switcher grid/list; кнопка «Фильтры» |
| 8 | Product grid | ✅ | `category__grid` + `productcard.twig` loop | **Смешанные семейства**: столы, тележки, зонты, столы+раковины… |
| 9 | Pagination | ✅ | `pagination.twig` | Полный subtree 608 SKU |
| 10 | SEO text | ❌ | `{{ seotext }}` | Пустой (`oc_category_description.description` = empty) |
| 11 | Certificates | ✅ | `sections/certificates.twig` | «Наши сертификаты» |
| 12 | Dealers form | ✅ | `sections/blockdealersform.twig` | «Дилерам и оптовикам» |
| 13 | Footer | ✅ | `common/footer.twig` | Standard ZPM |

**Not on root today:** `blockadvantagestop` / `blockadvantagesbottom` / `aboutteaser` (есть на `/katalog`, нет на category PLP).

### Current filter behavior (root 79)

| Aspect | State |
| --- | --- |
| Profile resolver | `FilterProfileResolver::findActiveProfileId(79)` → **null** (79 ∉ `registered_branch_roots`) |
| Filter source | Fallback: `getAttributesByCategory()` по subtree 79 + `global_hidden.php` |
| User value | **Low** — объединяет несовместимые commercial attrs (стол + мойка + зонт + dims) |
| M9 architecture | Root **79** ∉ `registered_branch_roots` (80, 207, 301, 322, 326 post–Phase 3); `filter_profile_active=false` → legacy `getAttributesByCategory()` pool; hub UX **not implemented** |

### Current subcategory chips logic

Из `catalog/controller/product/category.php`:

- `$data['categories']` = direct children of current category
- Child включается **только если** `getTotalProducts(subtree) > 0`
- Thumb: `resize(image)` или `placeholder.png`
- Name may append count if `config_product_count`

**Следствие:** пустые **Полки (83), Стеллажи (86), Тележки (85)** в chips **не попадают**; populated branches (301, 80, 322, 207, 326) — попадают. Parent **Подтоварники (82)** с 0 direct SKU **скрыт**; активная ветка — **322**.

### Current SEO / content

| Field | Value (baseline DB export) |
| --- | --- |
| `meta_title` | Нейтральное оборудование \| ООО «ЗПМ» |
| `meta_description` | Нейтральное оборудование для общепита и производств… |
| `description` (on-page) | **empty** |
| Canonical | Self on page 1 (`category.php`) |

### Reused templates (today)

| Template | Role on root 79 |
| --- | --- |
| `catalog/view/theme/default/template/product/category.twig` | Main PLP shell |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | Filter form |
| `catalog/view/theme/default/template/product/productcard.twig` | `.p-card` commerce cards |
| `catalog/view/theme/default/template/sections/certificates.twig` | Trust block |
| `catalog/view/theme/default/template/sections/blockdealersform.twig` | CTA block |

---

## Reusable Block Audit

### 1. Homepage category section

| Item | Detail |
| --- | --- |
| **Template** | `catalog/view/theme/default/template/sections/catalogsections.twig` |
| **Wrapper** | `section.zpm-cat-sections[data-cat-sections]` |
| **Grid** | `.zpm-cat-sections__grid` — CSS grid **3 cols** desktop → **2** @767 → **1** @580 |
| **Card** | `a.zpm-cat-card` |
| **Title** | `.zpm-cat-card__title` — max-width 190px, heading font tokens |
| **Image** | `.zpm-cat-card__img img` — `object-fit: contain`, max-height **300px** desktop / **150px** tablet / **100px** small mobile |
| **Arrow CTA** | `.zpm-cat-card__ico_arrow` + `#zpm_ico__goto_btn_arrow` |
| **CTA below grid** | `btn zm-inline-btn` → `catalog_primary_entry` |
| **Data source** | `cat-list-header` cache via `home.php` → `$data['categories']` |
| **Image field** | Twig: `cat.img` (**SAFE UNKNOWN:** cache builder in repo exports `thumb`/`thumb200`; live may alias `img`/`thumb300` — unify at implementation) |
| **Product count** | **Not shown** on homepage cards |

### 2. `/katalog` page

| Item | Detail |
| --- | --- |
| **Template** | `catalog/view/theme/default/template/product/katalog.twig` |
| **Pattern** | Same `zpm-cat-sections` + `zpm-cat-card` (no wrapper button) |
| **Image field** | `c.thumb300` |
| **Product count** | Computed in `katalog.php` (`count`, `tovar`) but **not rendered** in card twig |
| **Launch Mode** | `CategoryVisibility::applyCatalogNavData()` — `catlist` filtered to visible roots (only **79**) |
| **Below grid** | certificates, blockadvantagestop, blockdealersform, blockadvantagesbottom, SEO section |

### 3. Megamenu category tiles

| Item | Detail |
| --- | --- |
| **Template** | `catalog/view/theme/default/template/common/megamenu.twig` |
| **Tile** | `a.zpm-catalog__tile` |
| **Image** | `.zpm-catalog__tile-img img` ← `c.thumb300` |
| **Title** | `.zpm-catalog__tile-title` |
| **Count** | `.zpm-catalog__tile-list-counter` — «Товаров: N шт.» |
| **Layout** | Left: root tabs; right: pane grid per active root |
| **Reuse for M9.5** | **Reference only** for count display pattern; **primary hub grid = `zpm-cat-card`**, not megamenu tile (per task authority) |

### 4. PLP subcategory chips (current root)

| Item | Detail |
| --- | --- |
| **Template** | `category.twig` → `.zpm-sub-cat-chips[data-subcat-chips]` |
| **Chip** | `a.zpm-sub-cat-chip` + optional `.zpm-sub-cat-chip__icon` |
| **JS** | Expand/collapse toggle (`data-subcat-chips-toggle`) — v2.3.1 polish pass |
| **Fit for hub** | **Secondary** pattern — horizontal chips, not card hub; **replace** on root 79 |

### Comparative recommendation

| Pattern | Use on root hub |
| --- | --- |
| **`zpm-cat-card` + `zpm-cat-sections__grid`** | **Primary** — matches homepage + `/katalog` |
| `zpm-catalog__tile` | Optional future: add count line under title (megamenu parity) |
| `zpm-sub-cat-chips` | **Remove** on hub root |

---

## Target Structure

### Recommended page order (root 79 only)

```
1. Breadcrumbs          (existing — unchanged)
2. H1 + short intro     (Pageintro — add 1–2 sentences)
3. Subcategory grid     (NEW PRIMARY — zpm-cat-card block)
4. Optional SEO intro   (short commercial paragraph — category description OR dedicated partial)
5. [Product grid]       HIDDEN on root (Option A)
6. [Filter / sort]      HIDDEN on root
7. Certificates         (existing)
8. Dealers form         (existing)
9. [Extended SEO]       optional — reuse seotext partial when copy ready
```

### Layout mode flag (design)

Introduce conceptual **`category_display_mode`** for PLP controller output:

| Mode | category_id | Behavior |
| --- | ---: | --- |
| `hub` | **79** | Subcategory grid primary; no filter; no product grid |
| `branch` | 80, 207, 301, 322, 326, … | Current M9 PLP (filter + products + optional chips) |
| `nested` | descendants | Unchanged |

### Intro copy (draft — operator review)

**Pageintro description (under H1):**

> Выберите тип нейтрального оборудования: столы, моечные ванны, подтоварники, зонты или сервировочные тележки. В каждом разделе — свой каталог с подходящими фильтрами.

**Optional block below grid (2–3 sentences):** reuse themes from `/katalog` SEO section — производитель, оснащение кухни, индивидуальные размеры. **Not lorem** — edit from existing `katalog.twig` SEO paragraphs.

### Simplest safe launch option

**Hub-only root** without hybrid product listing:

- No «popular products» carousel (defers Option B)
- No collapsed filter accordion (defers partial hide)
- No new CSS system — **reuse** `.zpm-cat-sections` inside `.category__content`
- Chips removed when `hub` mode active

---

## Subcategory Grid Specification

### Inclusion rules

| Rule ID | Rule |
| --- | --- |
| **SG-01** | Show **direct launch branches** with **active SKU > 0** in subtree |
| **SG-02** | Hide categories with **0 active SKU** regardless of `status=1` |
| **SG-03** | Hide **empty parent** categories when a populated child exists (e.g. hide **82**, show **322**) |
| **SG-04** | Hide **duplicate / legacy** siblings with 0 SKU (**87** Столы производственные, **85** Тележки generic) |
| **SG-05** | Sort order: **commercial priority**, then `oc_category.sort_order` |
| **SG-06** | Card links → **SEO URL** of branch PLP (same as megamenu/chips) |

### Active subcategories (TEST baseline — show)

| Order | category_id | Display name | SEO path (verified M9 QA) | Active SKU | Show |
| ---: | ---: | --- | --- | ---: | :---: |
| 1 | **301** | Столы | `/katalog/nejtralnoe-oborudovanie/stoly/` | 420 | ✅ |
| 2 | **80** | Моечные ванны | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | 152 | ✅ |
| 3 | **322** | Подтоварники и подставки | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` | 11 | ✅ |
| 4 | **207** | Зонты вытяжные | `/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/` | 23 | ✅ |
| 5 | **326** | Тележки сервировочные | `/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/` | 3 | ✅ |

**Grid layout:** 5 cards → row of 3 + row of 2 on desktop (existing 3-col grid handles naturally).

### Empty / future subcategories (hide until ready)

| category_id | Name (DB) | Active SKU | M9.5 behavior | Unlock criteria |
| ---: | --- | ---: | --- | --- |
| **83** | Полки | 0 | **Hide** | ≥1 active SKU **and** card image assigned |
| **86** | Стеллажи | 0 | **Hide** | Same |
| **85** | Тележки | 0 | **Hide** | Same; do not confuse with **326** |
| **82** | Подтоварники (parent) | 0 | **Hide** — use **322** | N/A |
| **87** | Столы производственные | 0 | **Hide** | Taxonomy REVIEW (M9 RSK-M9-09) |
| **88** | Шкафы | 0 | **Hide** | ≥1 active SKU **and** card image |
| **89** | Крюки | 0 | **Hide** | Same |

**Safest rule:** *never show 0-SKU card* even with placeholder image — avoids dead-end PLP and false catalog breadth (Launch Mode discipline).

### Optional count on cards (Phase 2 enhancement)

Not required for M9.5 v1 launch. If added later:

- Pattern: megamenu `.zpm-catalog__tile-list-counter`
- Copy: «420 товаров» / pluralization via existing `true_wordform()` in `katalog.php`

### Card data contract (hub)

Each hub card object should expose:

| Key | Source |
| --- | --- |
| `category_id` | `oc_category` |
| `name` | `oc_category_description.name` |
| `href` | SEO URL via `$this->url->link('product/category', 'path=79_{id}')` |
| `thumb` / `thumb300` | `model_tool_image->resize(image, 300, 300)` |
| `count` | `getTotalProducts(subtree)` — optional display |
| `sort_order` | hub display sort (override table above) |

---

## Image Strategy

**Principle:** same visual treatment as homepage `/katalog` **`zpm-cat-card`** — no new art direction, no generation in M9.5.

### Existing reference

| Context | Path pattern | Example |
| --- | --- | --- |
| Root category image | `catalog/Category-image/` | `nejtralnoe-oborudovanie-2.webp` (cat **79**) |
| Empty child images | — | Controller falls back to `placeholder.png` |

### Required images list (for future asset pass — not M9.5)

| category_id | Suggested filename | Status |
| ---: | --- | --- |
| 301 | `catalog/Category-image/stoly.webp` | **Needed** — DB image empty |
| 80 | `catalog/Category-image/moechnye-vanny.webp` | **Needed** |
| 322 | `catalog/Category-image/podtovarniki-i-podstavki.webp` | **Needed** |
| 207 | `catalog/Category-image/zonty-vytyazhnye.webp` | **Needed** |
| 326 | `catalog/Category-image/telezhki-servirovochnye.webp` | **Needed** |
| 83 | `catalog/Category-image/polki.webp` | Deferred (0 SKU) |
| 86 | `catalog/Category-image/stellazhi.webp` | Deferred |

### Technical requirements

| Parameter | Value |
| --- | --- |
| **Master aspect** | ~**1:1** square canvas; product/hero shot centered |
| **Master size** | **600×600 px** minimum source (resize pipeline downscales) |
| **Card render size** | Resize **300×300** via `model_tool_image->resize()` (align `thumb300`) |
| **CSS display** | `object-fit: contain`; max-height 300/150/100px per breakpoint |
| **Format** | **WebP** preferred (matches root 79); PNG acceptable |
| **Naming** | `catalog/Category-image/{seo-slug}.webp` — slug = last segment of category SEO URL |
| **Alt text** | Category `name` (fix empty alt on `/katalog` cards at implementation) |
| **Background** | Transparent or light — match existing category card exports |

### Fallback behavior

| Condition | Behavior |
| --- | --- |
| `oc_category.image` empty | `placeholder.png` resize (current controller pattern) |
| Broken file | Same placeholder — no broken icon |
| 0 SKU category | **Do not render card** (hide before image concern) |
| Launch without custom art | Placeholder acceptable for **v1 TEST**; replace in asset milestone |

---

## Product Grid Policy

### Options evaluated

| Option | Description | Pros | Cons |
| --- | --- | --- | --- |
| **A — Hide grid** | No products on root | Clearest hub UX; no mixed-family confusion; minimal code | Users must click a branch |
| **B — Popular products** | Curated cross-family set | Merchandising surface | Needs selection rules, stale risk, conflicts with hub goal |
| **C — Secondary full grid** | Keep paginated grid below cards | Familiar PLP | **Defeats purpose** — mixed filters/products remain |

### Recommendation: **Option A — hide product grid on root 79**

**Rationale:**

1. Task objective = **category-selection hub**, not aggregated catalog.
2. Mixed grid today shows incompatible specs (sink dims on tables, etc.) — poor decision UX.
3. M9 invested in **branch profiles** — value is on child PLPs.
4. Simplest rollback: single `hub` flag gates product query + grid markup.
5. Search / direct SKU entry remain available via site search and deep links.

### Implementation notes (future)

- Skip `getProducts()` / `productcards` loop when `hub` mode
- Hide pagination
- Hide sort + view switcher (nothing to sort)
- Breadcrumb + SEO unchanged — URLs still valid

---

## Filter Policy

### Options evaluated

| Option | Description | Assessment |
| --- | --- | --- |
| Hidden completely | No sidebar, no mobile filter btn | **Recommended** |
| Collapsed | Empty accordion / «Фильтры недоступны» | Adds UI noise without value |
| Disabled | Visible but greyed out | Implies broken feature |
| Special root profile | M9 profile 79 with dims-only | Still wrong for multi-family hub |

### Recommendation: **Filter hidden on root 79 (hub mode)**

**Mechanism (design — two equivalent paths, pick one at implementation):**

**Path 1 — Display mode (preferred for UX clarity):**

- `category_display_mode = hub` → do not render `aside.category__sidebar`, do not render `[data-filter-open]`, skip `filterssidebar.twig`

**Path 2 — M9 root hub profile (complementary):**

- Add `79_neutral_hub.php` profile with **`filters_enabled: false`** OR empty allowlist + controller guard
- Ensures even direct `?filters=` URL params do not rebuild sidebar on hub

**Both paths:** branch PLPs (**80, 207, 301, 322, 326**) **unchanged** — full M9 profiles remain.

### Subcategory filter checkboxes

`filter_subcategories` in sidebar (checkbox list of children) — **suppress on hub** together with main filter. Navigation = cards only.

---

## Implementation Plan

**No implementation in M9.5.** Likely touch points for next milestone:

### Controllers

| File | Change |
| --- | --- |
| `catalog/controller/product/category.php` | Detect `category_id === 79` → set `category_display_mode = hub`; build `$data['hub_categories']` with card contract; skip product query + filter_groups when hub |
| `catalog/controller/product/katalog.php` | *(optional)* shared helper for card resize/count — DRY with hub |
| `system/library/zpm/category_visibility.php` | *(optional)* `isNeutralHubCategory($id)` constant `NEUTRAL_HUB_CATEGORY_ID = 79` |
| `system/library/zpm/filter_profile_resolver.php` | *(optional)* hub guard — return no filters for 79 |

### Twig templates

| File | Change |
| --- | --- |
| `catalog/view/theme/default/template/product/category.twig` | Conditional: if hub → render subcategory grid partial; omit sidebar, topbar, grid, chips |
| `catalog/view/theme/default/template/sections/catalogsections.twig` | **Reuse** via include **OR** extract `sections/category_hub_grid.twig` (same markup, different data var) |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | No change if hub skips include |
| `catalog/view/theme/default/template/product/productcard.twig` | Unchanged |

### CSS

| File | Change |
| --- | --- |
| `assets/css/style.css` | **Minimal** — hub grid inside `.category__content` may need spacing modifier (e.g. `.category--hub .zpm-cat-sections { margin-bottom: … }`); reuse existing `.zpm-cat-*` |

### JS

| File | Change |
| --- | --- |
| Category filter JS | **None** on hub (sidebar absent) |
| `zpm-sub-cat-chips` toggle | **None** on hub (block absent) |
| View switcher | **None** on hub |

### Data / admin (post-spec)

| Item | Action |
| --- | --- |
| `oc_category.image` | Upload branch images per Image Strategy |
| `oc_category_description.description` | Optional intro/SEO copy for root |
| Cache | Flush `cat-list-header` after image updates |

### QA checklist (implementation milestone)

| # | Check |
| ---: | --- |
| 1 | `/katalog/nejtralnoe-oborudovanie` — 5 branch cards, no product grid |
| 2 | No filter sidebar desktop; no «Фильтры» mobile |
| 3 | Each card → correct branch PLP with M9 profile intact |
| 4 | Empty cats (83, 85, 86) not visible |
| 5 | `/stoly/`, `/moechnye-vanny/` etc. — **regression** unchanged |
| 6 | Breadcrumbs + canonical unchanged |
| 7 | Launch Mode nav entry still → root hub |

### Dependency graph

```
M9 Phase 3 (done) → M9.5 spec (this doc) → M9.5 implementation → asset pass (images) → operator sign-off
```

---

## Risks

| ID | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| RSK-M95-01 | **Placeholder-only hub** looks unfinished | Medium | Accept for TEST v1; schedule image milestone; real photos per branch |
| RSK-M95-02 | **SEO expectation** of product listing on root | Medium | Keep meta_title/description; add intro copy; monitor Search Console |
| RSK-M95-03 | **Deep links** with `?filters=` on root | Low | Hub mode ignores filter build; 302 not required |
| RSK-M95-04 | **`cat.img` vs `thumb300` inconsistency** in cache | Medium | Unify cache builder keys in implementation |
| RSK-M95-05 | **Taxonomy drift** (87 vs 301, 82 vs 322) | Medium | SG-03/SG-04 rules; document in admin |
| RSK-M95-06 | **User habit** from mixed grid | Low | Hub is clearer; search retained |
| RSK-M95-07 | **Accidental hub flag** on wrong category | High | Gate **only** `category_id === 79` + unit test / QA assert |

---

## Recommended Next Step

1. **Operator review** of this spec — confirm Option A (hide grid + hide filter) and 5-card launch set.
2. **Implementation milestone** (M9.5 build) on TEST only:
   - `hub` mode in `category.php` + `category.twig`
   - Reuse `zpm-cat-card` grid
   - No filter, no products on root
3. **Asset milestone** (separate): upload 5 branch images to `catalog/Category-image/` per naming table.
4. **QA gate** using checklist above; regression M9 Phase 3 branch PLPs.
5. **Defer:** product count on cards, extended SEO block, Полки/Стеллажи cards until SKU import.

---

## Document metadata

| Field | Value |
| --- | --- |
| Changed files | `projects/website-factory/execution-cases/bzpm-roadmap/BZPM-M9.5-NEUTRAL-ROOT-UX-v1.md` (created) |
| Git commit | **No** (per task) |
| Deploy | **No** |
| UNKNOWN | Exact live `cat-list-header` cache keys (`img` vs `thumb300`); whether live `/katalog` renders single root card under Launch Mode in browser (M7.1 code confirms filter; visual not re-verified in this pass) |
