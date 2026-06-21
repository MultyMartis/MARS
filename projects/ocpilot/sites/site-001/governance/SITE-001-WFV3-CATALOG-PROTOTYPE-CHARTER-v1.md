# SITE-001 WF-V3 Catalog Prototype Charter v1

**Type:** Prototype scope charter — documentation only  
**Date:** 2026-06-14  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Precedes:** Catalog integration (not authorized by this document)

**Explicit exclusions (honored):** No OpenCart · No OCPilot · No TEST · No FTP · No Twig · No backend · No JS filter logic · No mobile version · No commit implied

**Binding authority:**

- [SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md](SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md)
- [SITE-001-WFV3-CATALOG-DISCOVERY-v1.md](../reports/SITE-001-WFV3-CATALOG-DISCOVERY-v1.md)
- [SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md](../reports/SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md)
- Frozen siblings: `workspaces/site-001-wf-v3-homepage-prototype/` · `workspaces/site-001-wf-v3-pdp-prototype/`

---

## Goal

Create a **Catalog prototype** (`/cars/`) as the **third anchor screen** of the same Class B **Digital Inventory Showroom** — same visual language, design system, container authority, and layout authority as Homepage and PDP.

Catalog answers the 3-second question: **«Это витрина склада — можно сравнивать и выбирать машины»**.

---

## Scope — Must Include (C0–C11)

Desktop-first only (≥ 1280px). Static visual prototype — no backend, no JS filter logic.

| Zone | Name | Requirement |
|------|------|-------------|
| **C0** | Header stack | Shared partial — identical grammar to H0 / Z0 |
| **C1** | USP benefit row | Shared partial — identical grammar to H1 / Z1 |
| **C2** | Breadcrumbs | Главная > Авто с пробегом |
| **C3** | Catalog heading | H1 + result count + sort control |
| **C4** | Filter zone | Desktop sidebar visual shell: Марка · Цена · Год · КПП · Кузов |
| **C5** | Active filter chips | Several active filters + reset link |
| **C6** | Results grid | `wf-v3-inventory-card` base from H4 — catalog extension fields |
| **C7** | Pagination | Static page numbers |
| **C8** | Trust layer | Catalog-scoped dealer + inventory proof |
| **C9** | Financing teaser | Lightweight credit band — no calculator |
| **C10** | Contact band | Same grammar as Homepage H9 |
| **C11** | Footer | Shared partial — identical grammar to H10 / Z10 |

---

## Must Not Include

- Carousel · sliders · sticky elements · popup · modal · accordion
- Card-in-card · shadow stacks · new color schemes
- Per-card solid red buttons · per-card image swiper
- OpenCart mapping · backend model · mobile responsive pass
- Reviews slider · bank carousel in catalog body

---

## Card Contract

Base: `wf-v3-inventory-card` from Homepage H4. Catalog extends with:

- Status badge (optional, one max)
- Spec chips (max 2)
- Monthly hint (muted)
- Text CTA «Подробнее» only

First fixture card (Audi A1, 2012) must align with PDP Z3–Z4 price and mileage.

---

## Layout Contract

- WF-GRID = PASS — `.wf-v3-container` authority unchanged
- WF-LAYOUT L-sidebar + L-grid — filter sidebar + results grid (3 columns desktop)
- First-screen cluster: filters + ≥2 card rows visible on desktop

---

## Deliverables

| Artifact | Path |
|----------|------|
| Workspace | `workspaces/site-001-wf-v3-catalog-prototype/` |
| Backup snapshot | `backups/post-v0.1-initial-build/` (after first successful build) |
| Screenshots | `screenshots/` — full-page, catalog-header, filters, inventory-grid, trust, finance |
| Session report | `docs/CATALOG-PROTOTYPE-v0.1-REPORT.md` |

---

## Success Criteria (HITL)

1. **3-second test** — «витрина склада — можно сравнивать машины»
2. **Sibling test** — side-by-side with Homepage + PDP — same brand shell
3. **Card continuity** — H4 → C6 → PDP on same Audi A1 fixture
4. **No new design language** — zero token or grammar divergence

---

## UNKNOWN

| Item | Status |
|------|--------|
| Sidebar exact width token | Prototype v0.1 decision |
| C9 include vs omit | Included in v0.1 per task brief |
| Shared partial package across 3 workspaces | OPEN — integration hygiene |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Catalog Prototype Charter v1 — scope only; no implementation implied beyond authorized prototype workspace.*
