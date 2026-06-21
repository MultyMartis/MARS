# SITE-001 W3UX-C1 Discovery v1

**Type:** Pre-execution discovery — used catalog card CSS selectors  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3UX-C1 — Used Catalog Card Density  
**Audit input:** [SITE-001-W3UX-DENSITY-AUDIT-v1.md](SITE-001-W3UX-DENSITY-AUDIT-v1.md)

**Methods:** FTP read of live `css/main.css` + `css/media.css` (post-W3-V) · HTTP body-class probe · Playwright card measurement · W2/W3-UX audit cross-reference

**Evidence (local, not in git):** `.recovery-temp/site-001-w3ux-c1-result.json` · backup `pre-w3ux-c1-20260609-0416`

---

## 1. Route and scope confirmation

| Route | Body class | Template (read-only) | In scope |
|-------|------------|----------------------|----------|
| `/cars/` | `used_catalog` | `product/category.twig` | **YES** |
| `/cars/bmw/` | `used_catalog` | `product/category.twig` | **YES** |
| `/cars/audi/` | `used_catalog` | `product/category.twig` | **YES** |
| `/auto/` | `new_catalog` | `product/categorynew.twig` | **NO** — control |
| `/` | *(none)* | `common/home.twig` | **NO** — control |

**Scoping strategy:** All W3UX-C1 overrides prefixed with `.used_catalog` — avoids homepage slider cards and new catalog.

---

## 2. Card shell selectors

| Zone | Primary selector | Pre-change values (live FTP) | Role |
|------|------------------|------------------------------|------|
| Grid wrap | `.catalog_wrap` | `margin: -10px` | Grid gutter |
| Card shell | `.catalog_item` | `padding: 10px; width: 25%` | Outer cell |
| Card face | `.catalog_item > a`, `.catalog_item > div` | flex column; border 1px | Clickable shell |
| Image face | `.catalog_item__face` | border-bottom 1px | Image carousel zone |
| Tags overlay | `.catalog_item__tags` | `padding: 15px; gap: 15px` | Stock badges |
| Image wrapper | `.catalog_item__img` | **`margin-top: 30px`**; `padding: 0 15px` | **Primary waste** |
| Slide image | `.catalog_item__face .swiper-slide img` | height auto | Unconstrained height |
| Info block | `.catalog_item__info` | `padding: 15px` | Content stack |
| Title | `.catalog_item__name` | `margin-bottom: 15px`; title 20px/500 | Equal weight with price |
| Specs | `.catalog_item__specific` | `margin-bottom: 15px` | Spec list |
| Spec items | `.catalog_item__specific > ul > li` | 14px; gap 5×10 | Row spacing |
| Price row | `.catalog_item__price` | flex space-between | Price + VIN |
| Price main | `.catalog_item__price_main` | 20px/500 (W3-V: 22px/600 global) | Needs used-only boost |
| VIN block | `.catalog_item__vin` | 80px wide; pad 5px | Side column |
| Credit | `.catalog_item__credit` | **mt/mb 20px; pt 15px; border-top** | **55px block** |
| CTA | `.catalog_item__btn` | `margin-top: 15px; padding: 9px` | Bottom action |

**New-car exception (unchanged):** `.new_auto .catalog_item .catalog_item__img { margin-top: 0 }` — used cards lack this override.

---

## 3. W3-V interaction

| Finding | Implication |
|---------|-------------|
| W3-V block at EOF in `main.css` | W3UX-C1 block appended **after** W3-V |
| W3-V sets global `.catalog_item { padding: var(--w3v-space-xs) }` | W3UX-C1 overrides with `.used_catalog .catalog_item` |
| W3-V price 22px/600 global | W3UX-C1 raises to 24px/600 under `.used_catalog` |

---

## 4. Baseline measurements (pre-change)

**Viewport:** Playwright · `/cars/` · first `.catalog_item` · 2026-06-09

| Viewport | Card height (px) | Card width (px) |
|----------|------------------|-----------------|
| Desktop 1440×900 | **530** | 339 |
| Tablet 768×1024 | **573** | 372 |
| Mobile 390×844 | **451** | 180 |

**Note (N-W3UX-C1-01):** TEST inventory sparse on `/cars/` root at probe time — 1 measured card; `/cars/audi/` returned 14 `catalog_item` HTML hits. Density math validated on first visible card geometry.

---

## 5. Change map (U-01–U-11 → selectors)

| ID | Selector | Current → target |
|----|----------|------------------|
| U-01 | `.used_catalog .catalog_item__img` | margin-top 30 → **8px** |
| U-02 | `.used_catalog .catalog_item__tags` | padding 15 → **8px** |
| U-03 | `.used_catalog .catalog_item__info` | padding 15 → **10px** |
| U-04 | `.used_catalog .catalog_item__name` | mb 15 → **6px**; lh tighter |
| U-05 | `.used_catalog .catalog_item__specific` | mb 15 → **6px** |
| U-06 | `.used_catalog .catalog_item__specific > ul > li` | 14 → **13px**; gap tighter |
| U-07 | `.used_catalog .catalog_item__price_main` | 22 → **24px / 600** |
| U-08 | `.used_catalog .catalog_item__vin` | compact 72px width |
| U-09 | `.used_catalog .catalog_item__credit` | mt/mb 20 → **8/0**; pt 15 → **8** |
| U-10 | `.used_catalog .catalog_item__btn` | mt 15 → **8px**; min-h **40px** |
| U-11 | `.used_catalog .catalog_item__face .swiper-slide img` | max-h **180px**; object-fit cover |

**Tokens added:** `--w3ux-space-xs/sm/md/lg`, `--w3ux-card-img-max-h`

---

## 6. Forbidden files confirmed untouched

| File | Status |
|------|--------|
| `header.twig` | **NOT MODIFIED** |
| `footer.twig` | **NOT MODIFIED** |
| `product.twig` | **NOT MODIFIED** |
| `productnew.twig` | **NOT MODIFIED** |
| `categorynew.twig` | **NOT MODIFIED** |
| `category.twig` | **NOT MODIFIED** (read-only discovery) |

---

## 7. Rollback anchor

| Artifact | Path |
|----------|------|
| Pre-write backup | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3ux-c1-20260609-0416\` |
| Manifest | `BACKUP-MANIFEST.md` |
| T1 restore | FTP STOR `css/main.css` + `css/media.css` from backup |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3UX-C1 discovery; selectors U-01–U-11 mapped |

*SITE-001 W3UX-C1 Discovery v1 — discovery complete; CSS write authorized.*
