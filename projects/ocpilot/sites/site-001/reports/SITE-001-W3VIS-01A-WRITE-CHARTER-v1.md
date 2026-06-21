# SITE-001 W3VIS-01A Write Charter v1

**Type:** Phase 2 write authorization charter — W3VIS-01A PDP Hero Surface System  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W3VIS-01A — PDP Hero Surface System (CSS-only)

**Parent discovery:** [SITE-001-W3VIS-01-DISCOVERY-v1.md](SITE-001-W3VIS-01-DISCOVERY-v1.md)  
**Gate:** [SITE-001-W3VIS-01-DECISION-v1.md](SITE-001-W3VIS-01-DECISION-v1.md)

---

## 1. Objective

Устранить главную визуальную проблему PDP: фрагментированный hero (фото, цена, скидки, характеристики, CTA) должен восприниматься как **единый коммерческий блок** без изменения layout, порядка элементов, контента или Twig.

---

## 2. Allowed scope (W3VIS-01A)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Surface tokens** | `--vis-*` custom properties (append to `:root`) | FTP |
| **PDP hero L2** | `.car_main_info`, `.newcar_newDesign`, `.new_car_NEW__wrapper` | FTP |
| **Widget demotion L3** | Discount, specs, VIN, credit calculator | FTP |
| **CTA hierarchy** | Primary red / secondary outline on PDP buttons | FTP |
| **Price hierarchy** | Typography + spacing in hero column | FTP |
| **Responsive CSS** | W3VIS-01A block in `media.css` | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:** `css/main.css`, `css/media.css`

**Explicitly NOT in scope:** twig, PHP, JS, DB, SEO, routes, content, text, header/footer structure.

---

## 3. Tasks authorized

| ID | Task | Selectors |
|----|------|-----------|
| **A1** | Used + new PDP hero L2 surface | `.used_car_page .car_main_info`, `.new_car_page .newcar_newDesign`, `.new_car_NEW__wrapper` |
| **A2** | Discount widget L3 demotion | `.car_main_info__discount` |
| **A3** | CTA action zone | `.car_main_info__btns`, `.new_car_main_info__btns` |
| **A4** | Price hierarchy | `.car_main_info__price_*`, `.newcar_newDesign .car_main_info__price_*` |
| **A5** | VIN supportive action | `.car_vin_check` |
| **A6** | Credit calculator demotion | `.used_car__credit`, `.credit_calculator` |

---

## 4. Design rules

| Level | Use |
|-------|-----|
| L1 | Page canvas (`--w3v2-surface`) |
| L2 | Hero surface (unified border, radius, shadow) |
| L3 | Nested widgets (discount, action band, calculator rows) |

**Forbidden:** glassmorphism, gradients, redesign, new brand colors, new images, new blocks.

**Preserve:** W3-V, W3V2, W3UX-C1 active layers — append after W3V2 block.

---

## 5. Verification matrix (minimum)

| # | URL | Viewports |
|---|-----|-----------|
| 1 | `/` | desktop, tablet, mobile |
| 2 | `/about` | desktop |
| 3 | `/contact/` | desktop |
| 4 | `/cars/` | desktop |
| 5 | `/cars/bmw/` | desktop |
| 6 | `/auto/` | desktop |
| 7 | `/auto/haval/` | desktop |
| 8 | Used PDP sample | all three |
| 9 | `/baic-bj40-new` (new PDP) | all three |

---

## 6. Success criteria

PDP воспринимается как **единый коммерческий блок**, не набор OC-виджетов.

Self-review: *«Если скрыть логотип, выглядит ли PDP дороже без изменения структуры?»* — **YES** required.

---

## 7. Rollback

**T1:** Restore `css/main.css` + `css/media.css` from `pre-w3vis-01a-*` backup. See [SITE-001-W3VIS-01A-CHANGE-REQUEST-v1.md](SITE-001-W3VIS-01A-CHANGE-REQUEST-v1.md).

---

## 8. Status

**ACTIVE** — CSS-only execution authorized on TEST per operator W3VIS-01A charter (2026-06-09).

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3VIS-01A write charter |
