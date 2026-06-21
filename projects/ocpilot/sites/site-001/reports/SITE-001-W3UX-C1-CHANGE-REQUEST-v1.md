# SITE-001 W3UX-C1 Change Request v1 — Used Catalog Card Density

**Status:** **AUTHORIZED FOR EXECUTION** — operator task authorization  
**Type:** Formal change request — Phase 2 density optimization wave  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`

---

## Request

| Field | Value |
|-------|-------|
| **ID** | CR-SITE-001-W3UX-C1-2026-06 |
| **Site ID** | SITE-001 |
| **Phase** | W3UX-C1 — Used Catalog Card Density |
| **Charter** | [SITE-001-W3UX-C1-WRITE-CHARTER-v1.md](SITE-001-W3UX-C1-WRITE-CHARTER-v1.md) |
| **Audit input** | [SITE-001-W3UX-DENSITY-AUDIT-v1.md](SITE-001-W3UX-DENSITY-AUDIT-v1.md) — U-01–U-11 |
| **Checkpoint** | `site-001-phase1-stable-2026-06` |

---

## Objective

Increase information density of **used car catalog cards** on TEST via **CSS-only** spacing and hierarchy changes — reduce vertical card height **15–20%**, show more vehicles above the fold, strengthen price/title/spec/credit hierarchy — while preserving **100%** of current structure, content, and block order.

**This is NOT a redesign. This is NOT a visual style refresh.**

---

## Business reason

W3-V cosmetic refresh did not improve perceived UX. W3-UX discovery identified vertical inflation and weak in-card hierarchy as root cause. Used catalog (`/cars/`) is highest-traffic inventory surface; density gain yields immediate scan-speed improvement.

---

## Affected components

| Component | Change summary |
|-----------|----------------|
| `css/main.css` | Append W3UX-C1 block — `.used_catalog`-scoped density overrides (U-01–U-11) |
| `css/media.css` | Responsive density adjustments for used catalog cards where needed |

**Not affected:** all `.twig` templates, header, footer, new catalog, PDP, DB, JS, PHP.

---

## Density change targets

| Area | Target |
|------|--------|
| Image area | Remove excessive top spacing; reduce dead space; max-height ~180px with object-fit |
| Card padding | Reduce **15–25%** on info/tags zones |
| Title | Tighter line-height; reduced bottom margin |
| Price | **24px / 600** — visually dominant over title |
| Credit block | Compress vertical margins/padding; lighter border gap |
| Specs | Tighter list gap and margins |
| Buttons | Keep location; reduce top margin only |

---

## Verification

| URL | Check |
|-----|-------|
| `/cars/` | Card height ↓; price hierarchy; no overflow |
| `/cars/bmw/` | Brand category grid intact |
| `/cars/audi/` | Brand category grid intact |
| `/auto/` | **No change** — new cards baseline |
| `/` | Homepage catalog blocks unchanged (no `used_catalog` body) |

**Viewports:** desktop 1440×900 · tablet 768×1024 · mobile 390×844

**Regression checks:** no clipped text, no broken images, no JS regressions, forms/filters intact.

---

## Rollback

T1 — restore 2 files from `pre-w3ux-c1-*` backup.

---

## Approval

| Role | Status | Date |
|------|--------|------|
| Write approver (**Андрей**) | **AUTHORIZED** — W3UX-C1 execution | 2026-06-09 |
| Backup | **Required before write** | — |
