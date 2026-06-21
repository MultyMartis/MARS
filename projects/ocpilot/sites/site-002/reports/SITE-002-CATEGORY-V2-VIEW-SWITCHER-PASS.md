# REPORT — CATEGORY V2 VIEW SWITCHER PASS

**Project:** SITE-002 (BZPM / ZPM TEST)  
**Environment:** https://zpm.new-site.space/  
**Baseline (pre-pass):** `SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER`  
**Deploy stamp:** `20260609-205536`  
**Date:** 2026-06-10  
**Mode:** Agent — implemented and deployed to TEST  
**Commit:** NO · **Push:** NO

---

## 1. Baseline backup

**Folder:** `projects/ocpilot/sites/site-002/backups/SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER/`

| File | Remote path | Size | SHA256 |
|------|-------------|------|--------|
| `category.twig` | `catalog/view/theme/default/template/product/category.twig` | 3245 | `49bb0e98efee49b0ee91aa35a972afee5ab912dc34cd4dbb01e6e676b317235c` |
| `style.css` | `assets/css/style.css` | 268329 | `9ae7ac39174394fee130a177c09179bd00df9eb47fe099bda5267922e27d95a1` |
| `main.js` | `assets/js/main.js` | 181055 | `548c3a3e94d400c52a525ca76bca92a453789bd8a3ca97b1ffc82b2ed1eeb19f` |

**Manifest:** `stable-category-v2-pre-view-switcher-manifest.json`  
**Baseline report:** `SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER.md`

---

## 2. Изменённые файлы

| File | Work copy | Deployed SHA256 |
|------|-----------|-----------------|
| `category.twig` | `category-v2-view-switcher-work/category.twig` | `b636ad2ee1047411a8e590a19db4b1e4e52bd7b5f09ced26a71765ac7ba4934e` |
| `style.css` | `category-v2-view-switcher-work/style.css` | `3ce18510025690e876699d6f9ddc4e2d5d8d5555ccb757a01239a6e8c85ed948` |
| `main.js` | `category-v2-view-switcher-work/main.js` | `d69e586405008c26579d73857b7d2c2c08a590e39f53ff0b2a406f472cbced45` |

**Deploy manifest:** `backups/SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER/category-v2-view-switcher-deploy-manifest-20260609-205536.json`

**Frozen (не тронуты):** `productcard.twig`, PDP V4, `producthero.twig`, `producttabs.twig`, filter, certificates, dealers form, header, footer, mobile layout rules.

---

## 3. Реализация switcher

**Разметка** (`category.twig`) — блок между `.category__sort` и `.category__filters-btn`:

```html
<div class="category__view" data-category-view role="group" aria-label="Вид каталога">
  <button type="button" class="category__view-btn is-active"
          data-category-view-mode="grid" aria-pressed="true" aria-label="Сетка" title="Сетка">
    <i class="fal fa-th-large" aria-hidden="true"></i>
  </button>
  <button type="button" class="category__view-btn"
          data-category-view-mode="list" aria-pressed="false" aria-label="Список" title="Список">
    <i class="fal fa-list" aria-hidden="true"></i>
  </button>
</div>
```

**CSS** — pill-кнопки на базе `.category__sort-btn` (50px height, border-radius full, active = `--main-dark-color`).  
**Скрытие ≤1024:** `.page--category .category__view { display: none !important; }`

**Inline FOUC-guard** — sync read `localStorage` + `matchMedia('min-width: 1025px')` сразу после открытия `<section class="category">`.

---

## 4. Реализация localStorage

| Key | Values | Default |
|-----|--------|---------|
| `zpm_category_view` | `grid` \| `list` | `grid` |

**JS module** (конец `main.js`):

- `getStoredView()` / `setStoredView()` с fallback на `grid`
- `applyView()` — добавляет/снимает `category--view-list` на `section.category`
- Desktop guard: `matchMedia('(min-width: 1025px)')` — на ≤1024 всегда grid, класс снимается
- `resize` listener на `DESKTOP_MQ`
- `aria-pressed` + `.is-active` на кнопках

**Проверка:** click List → reload → `list_class: true`, `ls: "list"` — PASS

---

## 5. Реализация list mode

**Модификатор:** `section.category.category--view-list`  
**Scope:** только `.page--category`, только `@media (min-width: 1025px)`

| Column | Blocks | Rules |
|--------|--------|-------|
| **Фото 200px** | `.p-card__media-wrap`, `.p-card__img` | `width: 200px` (exact) |
| **Информация** | `.p-card__title`, `.p-card__article`, `.p-card__body .p-card__status` | `display: contents` + grid; title `line-clamp: 2`, `height: auto` |
| **Покупка** | `.p-card__prices`, `.p-card__footer` | col 3; footer column: цена → qty/cart → «Подробнее» |
| **Actions** | `.p-card__top .p-card__actions` | absolute top-right; status in top hidden |

**Дубль статуса:** top hidden, body shown (`body_status_display: flex`, `top_status_display: none`) — PASS  
**Grid mode:** без изменений (3 cols @1920, 2 cols @1280) — PASS  
**Карточка:** один partial, CSS-only reorder — без второго twig

---

## 6. Desktop screenshots

**Folder:** `projects/ocpilot/sites/site-002/qa/category-v2-view-switcher/`

| Viewport | GRID | LIST |
|----------|------|------|
| 1920 | `category-grid-1920.png` | `category-list-1920.png` |
| 1440 | `category-grid-1440.png` | `category-list-1440.png` |
| 1366 | `category-grid-1366.png` | `category-list-1366.png` |
| 1280 | `category-grid-1280.png` | `category-list-1280.png` |
| 1024 | `category-grid-1024.png` | `category-list-1024.png` |

---

## 7. QA results

**Reference URL:** `/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/`  
**Evidence:** `qa/category-v2-view-switcher/category-v2-view-switcher-qa-result.json`

### Desktop matrix

| Check | GRID | LIST |
|-------|------|------|
| 1920 — grid cols | 3 | 1 |
| 1440 — grid cols | 3 | 1 |
| 1366 — grid cols | 3 | 1 |
| 1280 — grid cols | 2 | 1 |
| 1024 — switcher hidden | yes | yes |
| Photo width (list) | — | 200px all desktop |
| Sort | PASS | PASS |
| Filter btn (mobile topbar) | PASS | PASS |
| Pagination | PASS | PASS |
| Cart / qty | PASS | PASS |
| Wishlist / compare | PASS | PASS |
| Horizontal overflow | none | none |
| localStorage persist | — | PASS |

**Note @1024:** switcher скрыт (`display: none`); list CSS inactive (`min-width: 1025px`); JS при init/resize снимает `category--view-list` — grid layout сохраняется.

### Mobile guard (768)

| Check | Result |
|-------|--------|
| Switcher hidden | PASS |
| `category--view-list` stripped on reload | PASS |
| Grid cols | 2 (`346.5px 346.5px`) |

**UNKNOWN:** handler `pagination__more[data-next]` («Показать ещё») — не найден в `main.js`; поведение не проверялось отдельным кликом.

---

## 8. Regression results

| Area | Check | Result |
|------|-------|--------|
| **PDP V4** | hero 3-col, commerce, content, docs, related | PASS |
| **Search** | `.category__grid` present, no `category--view-list` | PASS |
| **Category** | wishlist, compare, cart, qty hooks present | PASS |
| **Related products** | visible on PDP | PASS |

---

## 9. Rollback procedure

1. Verify SHA256 backup files match §1.
2. FTP upload from `backups/SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER/`:
   - `category.twig` → `catalog/view/theme/default/template/product/category.twig`
   - `style.css` → `assets/css/style.css`
   - `main.js` → `assets/js/main.js`
3. Clear `system/storage/cache/template/`.
4. Verify category PLP — no view switcher, grid unchanged.
5. Verify PDP V4 regression on SPKB SKU.

**One-command rollback script pattern:** `category-v2-view-switcher-deploy.py` with WORK_DIR pointed at baseline folder (manual).

---

## 10. Git status

```
?? projects/ocpilot/sites/site-002/
```

New artifacts under `site-002/` (backups, work dir, qa screenshots, reports) — **untracked**, no commit.

---

## SECURITY RISK

FTP credentials present in deploy/capture scripts (same pattern as prior SITE-002 passes). Treat scripts as sensitive; do not commit credentials to public repos.

---

**Deploy to TEST:** complete · **Grid baseline preserved** · **List mode functional on desktop ≥1025px**
