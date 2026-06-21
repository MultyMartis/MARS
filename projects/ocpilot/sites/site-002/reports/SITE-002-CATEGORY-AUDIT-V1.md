# REPORT — CATEGORY AUDIT V1

**Project:** SITE-002 (ZPM TEST)  
**Baseline PDP (frozen):** `SITE-002-STABLE-PDP-V4-2026-06-10`  
**Audit date:** 2026-06-10  
**Mode:** READ ONLY — no FTP writes, no deploy, no Twig/CSS changes  
**Commit:** NO · **Push:** NO · **FTP changes:** NO · **Deploy:** NO

---

## Audit scope

| Item | Value |
|------|-------|
| Primary URL | https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/ |
| Category | Столы ПРЕМИУМ-600 (leaf PLP, 15 products/page, 2 pages) |
| Secondary probe | Parent `/stoly-serii-premium/` — subcategory chips present |
| Template | `catalog/view/theme/default/template/product/category.twig` |
| Product card | `catalog/view/theme/default/template/product/productcard.twig` |
| Filters | `catalog/view/theme/default/template/sections/filterssidebar.twig` |
| CSS | `/assets/css/style.css` (live = V4 baseline) |

---

## 1. Executive Summary

Страница категории **функциональна и узнаваема**, но **визуально и структурно отстаёт от завершённого PDP V4**. Каркас (sidebar + grid + mobile overlay) реализован аккуратно; фильтры богатые; карточки `.p-card` содержат полный commerce-набор (статус, артикул, цена, корзина, wishlist, compare).

**Сильные стороны:** единая дизайн-система ZPM; рабочие фильтры с accordion/range/toggles; адаптивная сетка без горизонтального скролла; pagination + «Показать ещё»; breadcrumbs и H1; блок сертификатов и форма дилеров.

**Слабые стороны:** нет описания категории и SEO-текста на аудируемой странице; карточка не синхронизирована с новым PDP (commerce-card, FA Pro icons, service patterns); фиксированная высота заголовка → пустоты/обрезка; дублирование статуса в DOM; пустой `alt` у изображений; sidebar-фильтр чрезмерно длинный; на desktop sort/topbar живёт в блоке с классом `--mobile`; переключателей вида (grid/list) нет.

**Вывод:** рекомендуется следующий этап **CATEGORY V2** — целевой redesign PLP с переиспользованием паттернов PDP V4, а не точечный CATEGORY V1.

---

## 2. Screenshots

Evidence directory: `projects/ocpilot/sites/site-002/qa/category-audit-v1/`

### Desktop

| Viewport | File | Grid cols | Card size (1st card) | Overflow |
|----------|------|-----------|----------------------|----------|
| 1920 | `category-desktop-1920.png` | 3 | 397×569 px | none |
| 1440 | `category-desktop-1440.png` | 3 | 315×539 px | none |
| 1366 | `category-desktop-1366.png` | 3 | 290×539 px | none |
| 1280 | `category-desktop-1280.png` | 2 | 393×539 px | none |
| 1024 | `category-desktop-1024.png` | 3 | 310×429 px | none |

### Mobile

| Viewport | File | Grid cols | Card size (1st card) | Overflow |
|----------|------|-----------|----------------------|----------|
| 768 | `category-mobile-768.png` | 2 | 347×429 px | none |
| 576 | `category-mobile-576.png` | 2 | 256×415 px | none |
| 390 | `category-mobile-390.png` | 2 | 163×434 px | none |
| 375 | `category-mobile-375.png` | 2 | 155×434 px | none |
| 360 | `category-mobile-360.png` | 1 | 305×434 px | none |

QA JSON: `projects/ocpilot/sites/site-002/qa/category-audit-v1/category-audit-qa-result.json`

---

## 3. Current DOM Structure

```
body
└── header (.zpm-header)
└── nav.breadcrumbs
│   └── ol.breadcrumbs__list → 6 items (Главная … Столы ПРЕМИУМ-600)
└── section.page-intro
│   └── h1.page-intro__title
└── main.main
    └── section.category
        └── .container
            └── .category__layout                    [grid: sidebar 340px + content]
                ├── aside.category__sidebar[data-filter-sidebar]
                │   ├── .category__sidebar__overlay
                │   ├── .category__sidebar__panel[role=dialog]
                │   │   ├── .zpm-popup_manager__head  «Поиск по параметрам»
                │   │   ├── button[data-filter-close]
                │   │   └── .filter-mobile__body
                │   │       └── .flt[data-filters] → form.flt__form
                │   │           ├── price range
                │   │           ├── availability toggles (4)
                │   │           ├── attribute groups (dynamic, accordion)
                │   │           └── dimension ranges (length/width/height)
                └── .category__content
                    ├── .zpm-sub-cat-chips            [optional; empty on leaf category]
                    ├── .category__topbar--mobile
                    │   ├── .category__sort + [data-sort-menu]
                    │   └── button.category__filters-btn[data-filter-open]
                    ├── .category__grid
                    │   └── article.p-card × N        [via productcard.twig loop]
                    └── nav.pagination
                        ├── .pagination__pages
                        └── button.pagination__more[data-next]
    └── {{ seotext }}                                 [empty on audited URL]
    └── section.certificates
    └── section (dealers form) {{ blockdealersform }}
└── footer (.zpm-footer)
```

**Зафиксировано по блокам:**

| Block | Present | Notes |
|-------|---------|-------|
| Breadcrumbs | ✅ | 6 уровней, `aria-label`, current page marked |
| H1 | ✅ | `page-intro__title`, без подзаголовка |
| Описание категории | ❌ | Нет intro/description под H1 |
| Подкатегории | ⚠️ | Twig-ready (`zpm-sub-cat-chips`); на leaf-категории пусто; на parent `/stoly-serii-premium/` — ~10 chips |
| Фильтр | ✅ | Desktop: постоянный sidebar; ≤1024: overlay panel |
| Сортировка | ✅ | Dropdown, 5 опций; нет desktop-only duplicate |
| Переключатели вида | ❌ | Нет grid/list toggle в HTML |
| Список товаров | ✅ | 15 cards, `.p-card` |
| Пагинация | ✅ | Страницы 1–2 + «Показать ещё» |
| SEO-текст | ❌ | `{{ seotext }}` не рендерится (пустой) |
| Footer | ✅ | Стандартный ZPM footer |

Live HTML snapshot: `projects/ocpilot/sites/site-002/category-audit-v1-work/category-live.html`

---

## 4. Product Card Audit

**Template:** `productcard.twig` (4699 bytes, FTP read-only)

### Structure

```
article.p-card.p-card--{in-stock|order}
├── .p-card__top [absolute]
│   ├── .p-card__status → .p-card__status-Yes|None + .p-card__delivery
│   └── .p-card__actions → compare + wishlist (data-compare-toggle, data-fav-toggle)
├── .p-card__media-wrap
│   ├── a.p-card__media → img.p-card__img
│   └── .p-card__buy-ok[hidden]
├── .p-card__body
│   ├── .p-card__article → copy SKU (zpm-copy)
│   ├── .p-card__status [duplicate; hidden desktop, shown ≤490px]
│   ├── a.p-card__title
│   └── .p-card__prices → .p-card__price + optional old/discount
└── .p-card__footer
    ├── .product-card__actions → [data-cart-add] + .zpm-qty--card
    └── a.btn-no-text → PDP link
```

### Checklist (audited category, 15 in-stock items)

| Element | Status | Notes |
|---------|--------|-------|
| Фото | ✅ | 400×400 cache, `object-fit: contain`, height 160px (140px ≤1024) |
| Название | ✅ | Link, fixed `height: 105px`, `overflow: hidden` |
| Артикул | ✅ | Copy-to-clipboard with tooltip |
| Статус | ✅ | Green dot + qty; duplicated in top + body |
| Цена | ✅ | Bold, ruble formatted |
| Старая цена | ⚠️ | Twig supports; 0 instances on audited page |
| Скидка | ⚠️ | Twig supports `priceproc`; none visible |
| Кнопка корзины | ✅ | Same `data-cart-add` / qty pattern as PDP |
| Wishlist | ✅ | Top-right icon button |
| Compare | ✅ | Top-right icon button |
| Hover | ✅ | Border accent by stock class (`--in-stock` / `--order`) |
| Высота карточки | ⚠️ | ~429–569px; title block creates rigid height |
| Переносы названий | ⚠️ | 3–4 lines then clip; long names truncated |

### Improvements identified

1. Remove duplicate status block or unify for all breakpoints.
2. Replace fixed title height with line-clamp (2–3 lines) for even grid rhythm.
3. Populate `img alt` from product name.
4. Align status typography/colors with PDP commerce-card (`product-hero__commerce`).
5. Surface old price / discount badge when data exists (currently invisible in sample).
6. Consider compact card variant for dense grids at 390–576px (cards ~155–163px wide).

---

## 5. Grid Audit

CSS base: `.category__grid { grid-template-columns: repeat(3, 1fr) }`  
Breakpoints: 2 cols `@1310px`, 2 cols `@1024px` (with sidebar collapse), 1 col `@360px` (observed).

| Viewport | Cards/row | Readability | Density | Balance |
|----------|-----------|-------------|---------|---------|
| 1920 | 3 | High | Low–medium | Wide gutters; sidebar 340px eats horizontal space |
| 1440 | 3 | High | Medium | Sidebar narrows to 290px |
| 1366 | 3 | Good | Medium | Cards ~290px — titles tight |
| 1280 | 2 | Good | Medium | Break at 1310px; cards widen to ~393px |
| 1024 | 3* | Acceptable | High | Sidebar hidden; filter via button; cards ~310px |
| 768 | 2 | Good | Medium | Topbar stack; filter overlay |
| 576 | 2 | Fair | High | Narrow cards, long titles wrap heavily |
| 390 | 2 | Fair | Very high | ~163px cards; status hidden in body until ≤490px logic |
| 375 | 2 | Fair | Very high | Same as 390 |
| 360 | 1 | Good | Low | Single column; footer CTA stacks |

\*At 1024px CSS sets 3 columns while sidebar is overlay — visually dense but readable.

**Пустоты:** large vertical gap between grid and certificates/dealers blocks; no category intro fills above-the-fold left void on leaf categories.

---

## 6. Filter Audit

**Component:** `.flt` in `filterssidebar.twig` (10.9 KB)

| Aspect | Assessment |
|--------|------------|
| UX desktop | Rich but overwhelming — 15+ accordion groups on table category |
| UX mobile | Full-screen dialog; close + overlay; usable |
| Price range | Present; on audited page `min=max=0` on range inputs — **SAFE UNKNOWN** if data bug or empty price spread |
| Toggles | «Только в наличии», «Под заказ», «С только ценой», «Со скидкой» |
| Attributes | Dynamic groups from `filter_groups` |
| Dimensions | Length / width / height mm ranges |
| Actions | «Показать товары», «Сбросить все», «Копировать ссылку» |
| Placement | Desktop left column; ≤1024 fixed overlay |
| A11y | Accordion `aria-expanded`; dialog `aria-modal` on mobile panel |

**Issues:** extreme scroll length; no «active filters» chips above grid; filter button class `--mobile` but sort row visible on all widths; desktop users cannot collapse sidebar.

---

## 7. Pagination Audit

```html
<nav class="pagination" aria-label="Пагинация">
  <div class="pagination__pages">…links 1, 2…</div>
  <button class="btn pagination__more" data-next="…?page=2">Показать еще</button>
</nav>
```

| Aspect | Status |
|--------|--------|
| Numbered pages | ✅ Desktop visible |
| Load more | ✅ AJAX-friendly `data-next` |
| Mobile | Pages hidden ≤ breakpoint; «Показать ещё» full-width pill |
| Position | Below grid, above certificates |
| UX | Clear; dual pattern (pages + load more) may confuse — pick one primary |

---

## 8. SEO Block Audit

| Check | Result |
|-------|--------|
| Exists on audited URL | ❌ No |
| Twig hook | ✅ `{{ seotext }}` after `</section.category>` |
| Placement | Would sit between catalog and certificates |
| UX impact | Neutral (absent = no harm); missed SEO opportunity |
| Parent/other categories | **SAFE UNKNOWN** — not probed exhaustively |

Recommendation: populate `seotext` for key categories; keep below grid, collapsible «Подробнее о категории» if long.

---

## 9. Top 10 UX Problems

1. **Visual gap vs PDP V4** — category feels like pre-redesign layer while PDP is polished.
2. **No category description** — H1 only; user lacks context.
3. **No SEO text** on audited leaf category.
4. **Fixed title height (105px)** — uneven whitespace or clipped names.
5. **Duplicate status markup** — maintenance and responsive complexity.
6. **Filter sidebar too long** — high cognitive load, pushes grid far down on tall viewports.
7. **Cramped cards at 390–576px** — 2-column grid with 155–163px width.
8. **Empty image alt** — accessibility and SEO deficit.
9. **Misleading class `category__topbar--mobile`** — sort bar on desktop too.
10. **No view density control** — missing grid/list or «compact» toggle.

---

## 10. Top 10 Quick Wins

1. Fill `alt="{{ name }}"` in `productcard.twig`.
2. Replace fixed title height with `-webkit-line-clamp: 3`.
3. Remove duplicate `.p-card__status` from body (keep top OR body per breakpoint via single node).
4. Add 1–2 sentence category intro from OC category description field.
5. Hide numbered pagination on mobile consistently (already partial) — single «Показать ещё».
6. Sticky «Показать N товаров» filter CTA on mobile panel scroll.
7. Active filter chips row above grid (client-side from form state).
8. Collapse filter groups by default except price + availability.
9. Align status dot/colors with PDP `--accent-color-01/02` tokens (already shared — verify contrast).
10. Lazy-load below-fold certificate slider on PLP.

---

## 11. Reusable Patterns From PDP (V4)

| PDP V4 pattern | Category reuse potential |
|----------------|-------------------------|
| `product-hero__commerce-card` visual (head + body, dark header) | Price/stock block styling on cards or quick-view |
| `product-hero__service-card` + FA Pro icons | Optional «Быстрый заказ» / «Задать вопрос» on card hover or PLP banner |
| `data-cart-add` + `.zpm-qty` stepper | ✅ Already shared — keep |
| `#zpmFbCallback` / `#zpmFbQuestion` hooks | Lead CTAs in category empty-state or dealer strip |
| Status typography (`statusText`, delivery) | Unify card status with hero commerce body |
| FA Pro icon set (`fal fa-shield-check`, etc.) | Service trust row in category header |
| Mobile pass breakpoints (768→360) | Apply same spacing/typography scale to PLP topbar/cards |
| Breadcrumb + `page-intro` | Already shared via header — extend with description |
| Wishlist/compare active states | Same `.p-card__action.active` — already consistent |
| Documents/content sidebar pattern | N/A on PLP; relevant for category landing with rich content |

**Not reusable as-is:** 3-column hero layout, tabs/content grid, documents sidebar — PLP needs own grid/filter architecture.

---

## 12. Recommendation

### Next stage: **CATEGORY V2**

| Option | When | Rationale |
|--------|------|-----------|
| CATEGORY V1 | Minor CSS fixes only | Insufficient — structural and visual debt too large vs PDP V4 |
| **CATEGORY V2** | **Recommended** | Dedicated PLP wave: card redesign, topbar, filter UX, mobile pass, SEO block, alignment with PDP tokens |

### Proposed V2 work packages (planning only)

1. **Card pass** — sync with PDP commerce visual language; line-clamp; alt text; optional compact breakpoint.
2. **Topbar pass** — sort + filter + optional view toggle; rename `--mobile` class semantics.
3. **Filter pass** — collapse defaults, active chips, mobile sticky apply.
4. **Content pass** — category intro + `seotext` template with collapsible long text.
5. **Grid pass** — revisit 3→2 column thresholds for 1366/1280; 1 col at ≤400px.
6. **Mobile pass** — mirror PDP mobile-pass methodology (screenshot matrix + QA JSON).
7. **Baseline** — capture `SITE-002-STABLE-CATEGORY-V1-YYYY-MM-DD` before first deploy.

### Preconditions

- PDP remains frozen at `SITE-002-STABLE-PDP-V4-2026-06-10`.
- Read-only audit artifacts committed separately only if operator requests.
- Admin/content needed to populate category descriptions and SEO texts.

---

## Artifacts (read-only session)

| Path | Purpose |
|------|---------|
| `category-audit-v1-work/category-audit-probe.py` | Live HTML fetch + probe |
| `category-audit-v1-work/category-audit-screenshot.py` | Playwright screenshots |
| `category-audit-v1-work/category-audit-fetch-twig.py` | FTP read twig templates |
| `category-audit-v1-work/category-live.html` | Live HTML snapshot |
| `category-audit-v1-work/category-probe-result.json` | Probe summary |
| `category-audit-v1-work/templates/*` | Twig copies (category, filter, productcard) |
| `qa/category-audit-v1/*.png` | 10 viewport screenshots |
| `qa/category-audit-v1/category-audit-qa-result.json` | Grid/card metrics |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| SEO text on other categories | SAFE UNKNOWN — only audited URL confirmed empty |
| Price filter min/max=0 | SAFE UNKNOWN — may be category-specific data issue |
| View-switch icons in design | Not in live HTML; screenshot AI artifact — **not confirmed** |
| FTP credentials | Used read-only from existing project scripts; not stored in this report |

---

**Git:** no commit · **Push:** no · **FTP changes:** none · **Deploy:** none
