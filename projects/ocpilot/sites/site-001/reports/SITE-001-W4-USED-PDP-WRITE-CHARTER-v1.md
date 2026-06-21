# SITE-001 W4 Used PDP Write Charter v1

**Type:** Phase 2 write authorization charter — W4 Used PDP Structural Visual Slice  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W4 — Controlled structural-visual slice (used PDP only)

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md) | Block grouping, markup, CSS goals |
| [SITE-001-W4-USED-PDP-CHANGE-REQUEST-v1.md](SITE-001-W4-USED-PDP-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md](SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md) | T1 rollback instance |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Parent rollback tiers T1–T3 |

---

## 1. Operator direction (2026-06-09)

Stop W3COLOR / W3ATMOSPHERE / W3WF cosmetic waves. New direction: **W4 controlled structural-visual slice** on **one page type** — used car PDP.

**Target URL:** `https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799`

---

## 2. Allowed scope (W4)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Used PDP twig** | Wrapper divs, class additions, regroup existing elements inside `product.twig` | FTP |
| **CSS** | Scoped block under `.used_car_page` in `main.css` + `media.css` | FTP |
| **Visual composition** | Hero shell, gallery, offer panel, trust strip, equipment grid, credit panel | FTP |
| **Cache** | System + modification cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP logic | **FORBIDDEN** |
| JS logic | **FORBIDDEN** (inline scripts in twig preserved verbatim) |
| DB changes | **FORBIDDEN** |
| SEO / meta / content rewrites | **FORBIDDEN** |
| `header.twig`, `footer.twig` | **FORBIDDEN** |
| `productnew.twig`, `category.twig`, `categorynew.twig` | **FORBIDDEN** |
| Navigation, forms logic, catalog, new PDP | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |

---

## 4. Success criteria (visual)

Operator opens used PDP and **immediately** sees visible improvement — target **≥7/10** on used PDP:

1. No longer reads as OpenCart widget stack  
2. Hero feels like a real car offer  
3. Photo area stronger  
4. Price/action area clearly commercial  
5. VIN/check block = premium trust strip  
6. Equipment list easier to scan  
7. Credit form less cheap  

Regression: `/cars/`, `/cars/bmw/`, `/`, `/about`, `/contact/` unchanged in layout/function.

---

## 5. Status

**ACTIVE** — W4 execution authorized on TEST per operator task brief 2026-06-09.
