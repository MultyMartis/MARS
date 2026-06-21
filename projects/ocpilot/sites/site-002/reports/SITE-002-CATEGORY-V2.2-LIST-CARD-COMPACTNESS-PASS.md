# REPORT — CATEGORY V2.2 LIST CARD COMPACTNESS PASS

**Site:** SITE-002 (BZPM / ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Baseline:** CATEGORY V2.1 LIST CARD LAYOUT FIX  
**Deployed at (UTC):** 2026-06-09T21:45:16Z

---

## 1. Backup path

Pre-change live capture (FTP):

| File | Backup path |
|------|-------------|
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-list-card-compactness-pass.bak` |

Deploy manifest: `projects/ocpilot/sites/site-002/backups/category-v2.2-list-card-compactness-deploy-manifest-20260609-214513.json`

---

## 2. Changed file

| Local work copy | Remote path |
|-----------------|-------------|
| `category-v2.1-list-card-commerce-work/style.css` | `assets/css/style.css` |

**Twig / PHP / JS:** NOT touched.

Supporting (not deployed): `category-v2.2-list-card-compactness-work/` (deploy + QA scripts).

---

## 3. CSS selectors changed

**Scope only:** `@media (min-width: 1025px) { .page--category .category--view-list ... }`

| Selector | Change |
|----------|--------|
| `.category--view-list .category__grid` | `gap`: `--pad-gap-line` → `--pad-gap-mini` |
| `.category--view-list .p-card` | columns `200/180` → `160/170`; `column-gap` `--pad-gap` → `--pad-gap-line`; `row-gap` `10px` → `6px`; padding `20px` → `14px` vertical, `--pad-gap-line` horizontal |
| `.category--view-list .p-card__top` | `top` `20px` → `14px`; `right` `--pad-box` → `--pad-gap-line` |
| `.category--view-list .p-card__top .p-card__actions` | `gap` `10px` → `6px` |
| `.category--view-list .p-card__media-wrap` | `width` `200px` → `160px`; `align-self` `center` → `start` |
| `.category--view-list .p-card__media` | `width` `200px` → `160px` |
| `.category--view-list .p-card__img` | `200×160` → `160×135`; explicit `object-fit: contain` |
| `.category--view-list .p-card__title` | `margin: 0` |
| `.category--view-list .p-card__article` | `margin: 0` |
| `.category--view-list .p-card__body .p-card__status` | `margin: 0` |
| `.category--view-list .p-card__primary-specs` | `gap` `10px` → `6px` |
| `.category--view-list .p-card__primary-spec` | `gap` `10px` → `4px`; `padding: 0` |
| `.category--view-list .p-card__primary-spec-icon` | `24×24` → `20×20`; `font-size: 14px` |
| `.category--view-list .p-card__primary-spec-content` | `gap` `2px` → `0` |
| `.category--view-list .p-card__primary-spec dt/dd` | `line-height` → `1.2` |
| `.category--view-list .p-card__prices` | **unchanged** `margin-top: calc(40px + var(--pad-gap-mini))` — сохранён зазор под wishlist/compare (40px кнопки) |
| `.category--view-list .p-card__footer` | `width/max-width` `180px` → `170px`; gaps `10px` → `6px` |
| `.category--view-list .p-card__footer .product-card__actions` | `gap` `10px` → `6px` |

---

## 4. Что уплотнено

- **Межкарточный gap** в list-grid: 20px → 10px.
- **Колонка фото:** 200px → **160px** (≥150px по требованию); превью 160×135px, `contain`.
- **Межколоночный gap:** 30px → 20px.
- **Внутренние отступы карточки:** вертикаль 20px → 14px; горизонталь 20px → 20px (`--pad-gap-line`).
- **Вертикальные row-gap** в grid карточки: 10px → 6px.
- **Инфо-блок:** title / article / status — обнулены лишние margin.
- **Primary specs:** 4 в строку, без фона/border; иконки 20px; gap 6px/4px; плотнее dt/dd.
- **Commerce-колонка:** footer 170px; компактнее stack qty/cart/подробнее.
- **Высота карточки (1-й товар):** ~324px @1920–1366, ~343px @1280–1025 (было ~200px media + больше padding/gap до pass).

Дизайн-система (цвета, кнопки, скругления, шрифты, иконки FA, статусы) — **без изменений**.

---

## 5. QA — list mode

| Viewport | media | img | card_h | specs | overlap | overflow | Result |
|----------|-------|-----|--------|-------|---------|----------|--------|
| 1920 | 160px | 160×135 | 324px | 4 / 1 row | none | none | PASS |
| 1440 | 160px | 160×135 | 324px | 4 / 1 row | none | none | PASS |
| 1366 | 160px | 160×135 | 324px | 4 / 1 row | none | none | PASS |
| 1280 | 160px | 160×135 | 343px | 4 / 1 row | none | none | PASS |
| 1025 | 160px | 160×135 | 343px | 4 / 1 row | none | none | PASS |

Проверено на каждом viewport:

- list-card компактнее (меньше media, padding, gaps);
- нет наложений price ↔ wishlist/compare, cart ↔ details;
- фото ≥150px (фактически 160px);
- цена, cart, подробнее, wishlist, compare видны;
- primary specs видны, 4 в одну строку;
- qty DOM присутствует (`data-cart-qty`, скрыт до добавления в корзину — штатное поведение);
- horizontal overflow отсутствует.

QA JSON: `projects/ocpilot/sites/site-002/qa/category-v2.2-list-card-compactness/category-v2.2-list-card-compactness-qa-result.json`

---

## 6. Grid / mobile regression

| Context | Viewports | Result |
|---------|-----------|--------|
| Grid | 1920, 1440, 1366, 1280, 1025 | PASS — specs hidden |
| Mobile grid | 768, 576, 390, 375, 360 | PASS — specs hidden, switcher hidden, list class off |

---

## 7. PDP / shared regression

| Context | Result |
|---------|--------|
| PDP V4 | PASS — hero 3 cols, commerce, content intact |
| Search | PASS — 0 visible specs blocks |
| Wishlist | PASS — 0 visible specs blocks |
| Compare | PASS — 0 visible specs blocks |
| Related on PDP | PASS — 0 card specs in related |

---

## 8. Screenshot paths

`projects/ocpilot/sites/site-002/qa/category-v2.2-list-card-compactness/`

- `category-list-1920.png`, `category-list-1440.png`, `category-list-1366.png`, `category-list-1280.png`, `category-list-1025.png`
- `category-grid-1920.png`, `category-grid-1440.png`, `category-grid-1366.png`, `category-grid-1280.png`, `category-grid-1025.png`
- `category-mobile-grid-768.png`, `576`, `390`, `375`, `360`
- `pdp-v4-regression-1920.png`

---

## 9. Rollback procedure

1. FTP restore:
   - `projects/ocpilot/sites/site-002/backups/style.css.pre-list-card-compactness-pass.bak` → `assets/css/style.css`
2. Hard-refresh browser (CSS cache).

Or:

```text
py -3 projects/ocpilot/sites/site-002/category-v2.2-list-card-compactness-work/category-v2.2-list-card-compactness-deploy.py
```

(point deploy script at backup file if needed)

---

## 10. Git status

New/untracked under `projects/ocpilot/sites/site-002/`:

- `backups/style.css.pre-list-card-compactness-pass.bak`
- `backups/category-v2.2-list-card-compactness-deploy-manifest-*.json`
- `category-v2.1-list-card-commerce-work/style.css` (modified)
- `category-v2.2-list-card-compactness-work/`
- `qa/category-v2.2-list-card-compactness/`
- `reports/SITE-002-CATEGORY-V2.2-LIST-CARD-COMPACTNESS-PASS.md`

**Commit:** NO  
**Push:** NO
