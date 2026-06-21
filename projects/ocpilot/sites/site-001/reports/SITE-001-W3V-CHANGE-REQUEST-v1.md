# SITE-001 W3-V Change Request v1 — Visual Layer Refresh

**Status:** **READY FOR EXECUTION** — operator task authorization  
**Type:** Formal change request — Phase 2 visual-only wave  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Request

| Field | Value |
|-------|-------|
| **ID** | CR-SITE-001-W3V-2026-06-09 |
| **Site ID** | SITE-001 |
| **Phase** | W3-V — Visual Layer Refresh |
| **Charter** | [SITE-001-W3V-WRITE-CHARTER-v1.md](SITE-001-W3V-WRITE-CHARTER-v1.md) |
| **Visual spec** | [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) (tokens adapted per W3-V radius targets) |
| **Rollback plan** | [SITE-001-W3V-ROLLBACK-PLAN-v1.md](SITE-001-W3V-ROLLBACK-PLAN-v1.md) |
| **Checkpoint** | `site-001-phase1-stable-2026-06` |

---

## Objective

Modernize visual appearance of SITE-001 on TEST via **CSS-only** changes: border radius, shadows, button/form/card styling, vertical rhythm, and price/CTA hierarchy — while preserving **100%** of current structure, content, and block order.

---

## Business reason

Phase 1 brand replacement complete; W3-C footer structural reduction **rolled back** (operator rejected structural changes). Phase 2 must focus on **visual refresh only** — softer modern look without layout or content risk.

---

## Affected components

| Component | Change summary |
|-----------|----------------|
| `css/main.css` | Add W3-V design tokens in `:root`; append visual override block for buttons, forms, cards, shadows, hierarchy |
| `css/media.css` | Responsive card/button spacing adjustments where needed |

**Not affected:** all `.twig` templates, header, footer structure, navigation, DB, extensions, third-party scripts, OpenCart logic.

---

## Visual change targets

| Area | Target |
|------|--------|
| Border radius | Small: **8px** · Large blocks: **12px** · Buttons: **8–10px** |
| Shadows | Soft modern; restrained values; no glassmorphism |
| Buttons | Preserve colors/CTA meaning; improve height, padding, hover, radius |
| Forms | Improve inputs, textarea, submit spacing and focus — fields unchanged |
| Cards | Catalog, advantage (`.new_car_bonus__item`), bank (`.partner_banks__item`), info (`.fancy_two_blocks__item`) |
| Vertical rhythm | Unified spacing tokens |
| Hierarchy | Price and primary CTA visually stronger |

---

## Verification

| URL | Check |
|-----|-------|
| `/` | Cards, slider CTA, no layout shift |
| `/about` | Information cards, no broken CSS |
| `/contact/` | Form styling, contact blocks |
| `/cars/` | Catalog cards, price hierarchy |
| `/auto/` | New catalog cards |
| Used PDP | Price, CTA buttons, forms present |
| New PDP | Price, CTA buttons, bonus cards |

**Regression checks:** no overlap, no hidden content, no missing forms/buttons.

---

## Rollback

T1 — restore 2 files from `pre-w3v-*` backup (see rollback plan).

---

## Approval

| Role | Status | Date |
|------|--------|------|
| Write approver (**Андрей**) | **AUTHORIZED** — operator task | 2026-06-09 |
| Backup | **Required before write** | — |
