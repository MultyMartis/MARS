# SITE-001 W3VIS-01B Write Charter v1

**Type:** Phase 2 write authorization charter — W3VIS-01B PDP Commercial Authority  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W3VIS-01B — PDP Commercial Authority (CSS-only)

**Parent baseline:** [SITE-001-W3VIS-01A-EXECUTION-v1.md](SITE-001-W3VIS-01A-EXECUTION-v1.md) (post-W3VIS-01A)

---

## 1. Objective

Усилить **коммерческую иерархию** PDP без redesign: страница должна читаться как «авто доступно и готово к покупке», а не как «запись в базе данных». Целевой commercial score: **7/10** (baseline после 01A: **4/10**).

**Eye path:** Photo → Price → Primary CTA → Specs (support).

---

## 2. Allowed scope (W3VIS-01B)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Commercial tokens** | `--visb-*` custom properties | FTP |
| **Price dominance (B1)** | Typography, spacing, L3 price zone | FTP |
| **CTA hierarchy (B2)** | Primary / secondary / tertiary button tiers | FTP |
| **Hero focus (B3)** | Demotion discount, specs, VIN, calculator | FTP |
| **VIN reclassification (B4)** | Trust/support styling, not conversion | FTP |
| **Specs compression (B5)** | Scan density, muted hierarchy | FTP |
| **Surface levels (B6)** | L1–L5 strict stacking | FTP |
| **Flex visual order** | CTA before specs in hero column (CSS `order`) | FTP |
| **Responsive CSS** | W3VIS-01B block in `media.css` | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:** `css/main.css`, `css/media.css`

**Explicitly NOT in scope:** twig, PHP, JS, DB, SEO, routes, content, header, footer, homepage, catalog cards, forms, banks, reviews.

---

## 3. Tasks authorized

| ID | Task | Selectors |
|----|------|-----------|
| **B1** | Price dominance system | `.car_main_info__main__top_wrap`, `.car_main_info__price_*`, `.newcar_newDesign .car_main_info__price_*` |
| **B2** | Primary CTA dominance | `.car_main_info__btns`, `.new_car_main_info__btns`, `.newcar_config__item_main > .btns` |
| **B3** | Hero commercial focus | Discount, specs, VIN, credit demotion |
| **B4** | VIN reclassification | `.car_vin_check` |
| **B5** | Specs compression | `.car_main_info__characteristics*` |
| **B6** | Commercial surface levels L1–L5 | PDP page + hero + price + CTA + support widgets |

---

## 4. Design rules

| Level | Role |
|-------|------|
| **L1** | Page canvas (`#content` background) |
| **L2** | Hero PDP surface (`.car_main_info`, `.newcar_newDesign`, `.new_car_NEW__wrapper`) |
| **L3** | Price zone (red accent band, 44px/700 price) |
| **L4** | Primary CTA (52px, shadow at rest, flex dominance) |
| **L5** | Support widgets (discount, specs, VIN, credit — flat, muted) |

**Forbidden:** new colors for beauty, premium shadows for decoration, new blocks, layout rebuild, content edits.

**Preserve:** W3VIS-01A, W3V2, W3UX-C1 — append after W3VIS-01A block.

---

## 5. Verification matrix (minimum)

| # | URL | Viewports | Screenshots |
|---|-----|-----------|-------------|
| 8 | Used PDP `/audi-a1-2012-s-probegom-149-000-km-799` | desktop, tablet, mobile | **REQUIRED** before/after |
| 9 | New PDP `/baic-bj40-new` | desktop, tablet, mobile | **REQUIRED** before/after |

Regression smoke (no screenshots required): homepage, catalog, about, contact — HTTP 200.

---

## 6. Success criteria

Operator immediately sees: **1) Car 2) Price 3) Action** — everything else second.

Self-test: *«If logo is hidden, does PDP look like a modern dealer inventory page (B) vs old OpenCart template (A)?»* — target **B**.

---

## 7. Rollback

**T1:** Restore `css/main.css` + `css/media.css` from `pre-w3vis-01b-*` backup. See [SITE-001-W3VIS-01B-CHANGE-REQUEST-v1.md](SITE-001-W3VIS-01B-CHANGE-REQUEST-v1.md).

---

## 8. Status

**ACTIVE** — CSS-only execution authorized on TEST (2026-06-09).

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3VIS-01B write charter |
