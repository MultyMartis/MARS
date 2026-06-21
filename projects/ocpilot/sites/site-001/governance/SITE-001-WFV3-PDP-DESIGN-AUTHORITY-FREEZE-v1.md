# SITE-001 WF-V3 PDP Design Authority Freeze v1

**Type:** Design authority freeze — documentation only  
**Date:** 2026-06-11  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Artifact frozen:** WF-V3 Used-Car PDP (clean-room prototype)

**Explicit exclusions (honored):** No HTML · No SCSS · No JS · No OpenCart · No OCPilot implementation · No TEST · No FTP · No visual pass · No asset pass · No commit implied

**Supersedes as PDP design authority:** WF-V2 · W4/W5 experimental layers · TEST append-only CSS · all prior concept directions (Graphite Salon · Modern Dealer 2026 · WF V2 Light Clean) — retained only as error evidence in reports.

**Related:**

- [SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md](SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md)
- [SITE-001-WF-V3-PROTOTYPE-RESTORE-POINT-v1.md](../reports/SITE-001-WF-V3-PROTOTYPE-RESTORE-POINT-v1.md)
- [SITE-001-WFV3-PDP-CONCEPT-ANALYSIS-v1.md](../reports/SITE-001-WFV3-PDP-CONCEPT-ANALYSIS-v1.md)
- [SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md](../reports/SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md)
- [SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md](../../../governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md)

---

## Section 1 — Purpose

### Why this freeze exists

WF-V2 demonstrated a repeatable failure pattern on SITE-001:

- endless redesign loops (append-only CSS → cleanup → anatomy → layout → surface cleanup);
- architecture drift under cosmetic passes;
- competing design authorities without supersession;
- visual experiments replacing product decisions.

WF-V3 was introduced as a **clean-room** path: composition before decoration, prototype before merge, evidence before implementation.

This document **freezes** the approved WF-V3 PDP foundation so that:

1. Future WF-V3 work has a **stable reference point** — not a moving target.
2. Homepage and catalog prototypes **inherit** PDP authority instead of re-litigating PDP anatomy.
3. Integration phases (OpenCart, CRM, TEST) cannot silently reshape product architecture.

### Binding statement

**WF-V3 PDP is now the primary design authority for all future WF-V3 work.**

Any screen, component, or integration that touches SITE-001 visual identity must **align with** the frozen PDP anatomy, visual system, and Class B principles — unless a new **authority review** explicitly supersedes this freeze.

---

## Section 2 — Authority Sources

Only the following sources may define PDP direction. No other report, TEST state, legacy concept, or agent recommendation overrides them.

| # | Source | Path / label | Role |
|---|--------|--------------|------|
| 1 | **Concept PNG** | `projects/ocpilot/sites/site-001/design/wf-v3-concept/01-sibcar-v3-concept.png` | Target composition and visual grammar — zone geometry and hierarchy are authoritative |
| 2 | **WF-V3 PDP Prototype v0.1** | `workspaces/site-001-wf-v3-pdp-prototype/` · restore point `site-001-wf-v3-pdp-prototype-v0.1-20260611` | Clean-room architecture baseline — section order, 65/35 hero, DOM zones |
| 3 | **VISUAL PASS v0.2** | `workspaces/site-001-wf-v3-pdp-prototype/docs/VISUAL-PASS-v0.2-REPORT.md` | Showroom visual system — tokens, typography, surfaces, section polish **without** architecture change |
| 4 | **ASSET REALISM PASS v0.2.1** | `workspaces/site-001-wf-v3-pdp-prototype/docs/ASSET-REALISM-PASS-v0.2.1.md` | Asset-layer audit — placeholder vs production slots; does **not** authorize layout change |

**Conflict resolution:** Concept PNG wins on **composition**. Prototype v0.1 + v0.2 wins on **implemented anatomy** where PNG is ambiguous. Asset pass governs **asset replacement only**, not structure.

**Forbidden as PDP authority:** TEST live state · WF-V2 hooks · W4/W5 twig/CSS · agent perception scores · undocumented visual experiments.

---

## Section 3 — FROZEN

The following architectural decisions are **frozen**. Future work **must not modify** them without a new authority review (charter + operator HITL + supersession record).

### Overall page anatomy

Single-page **used-car PDP** — Class B **Digital Inventory Showroom**. Desktop-first visual model (≥ 1280px). Clean-room HTML partials with `wf-v3-*` class prefix. Maximum **two surface depths** per zone (`surface` + `surface-secondary`). No card-in-card. No shadow stacks. No legacy OpenCart DOM as layout authority.

### Section order (top → bottom)

| Order | Zone | ID (concept) |
|-------|------|--------------|
| 1 | Header stack (topbar + main nav + CTA) | Z0 |
| 2 | Promo / USP benefit row | Z1 |
| 3 | Breadcrumbs | Z2 |
| 4 | PDP title + status badges | Z3 |
| 5 | Hero split (gallery + offer) | Z4 |
| 6 | Trust row | Z5 |
| 7 | Equipment section | Z6 |
| 8 | Credit calculator section | Z7 |
| 9 | Banks section | Z8 |
| 10 | Related / offer links *(deferred in prototype — slot reserved)* | Z9 |
| 11 | Footer | Z10 |

**Rule:** No section insertion, removal, or reorder without authority review.

### Hero 65/35 structure

| Column | Share | Content |
|--------|-------|---------|
| **Left** | **~65%** | Main vehicle photo on flat studio surface; prev/next controls; thumbnail strip (active thumb = brand-red border) |
| **Right** | **~35%** | Offer column — see offer block order below |

Gallery dominates above-the-fold viewport. Not 50/50. Not symmetric catalog columns. Not H1 inside gallery replacing title row.

### Trust placement

Trust row sits **immediately below hero** (post-offer). Horizontal proof strip on `surface-secondary` — ~5 equal proof items (report, condition, accidents, mileage, etc.). Bridges offer → detail scroll. **Not** embedded inside offer column. **Not** moved above hero or below equipment without review.

### Equipment placement

Full-width **«Комплектация автомобиля»** section **after trust**, **before credit**. Multi-column feature list with checkmarks. Flat spec-sheet surface — not nested inside hero or credit card.

### Credit placement

Dedicated **credit / installment** section **after equipment**, **before banks**. Flat sales-module layout (no card-in-card on grey). Calculator + form co-located. Secondary conversion path to hero primary CTA.

### Banks placement

**«Партнёрские банки»** logo grid **after credit**, **before related links / footer**. Credibility reinforcement — not merged into credit panel or hero offer.

### Footer placement

Dark inverse footer **last** on page. Contact repeat, catalog link columns, legal links, callback CTA. Multi-band dark field — not light inline chrome.

### Primary reading flow

```text
Land → header identity + contact
  → USP benefit scan (supporting, not dominant)
  → breadcrumb orientation
  → vehicle title + status badges
  → gallery + price/CTA (one glance — car first, price second)
  → primary CTA «Купить в кредит» OR secondary trade-in / рассрочка
  → trust strip (verification anxiety reduction)
  → scroll: equipment → credit calculator → banks → related → footer contact
```

**Commercial idea (frozen):** «Конкретная машина на складе — цена ясна, проверка и кредит рядом». Promotion is **supporting**, not hero.

### Offer column internal order (frozen)

Within the **35% offer column**, top → bottom:

1. Price (+ strikethrough old price + monthly hint)
2. CTA row (one solid red primary + outlined secondaries)
3. Specs grid (labels uppercase / muted, values bold)
4. Discount lines (accent bar treatment)
5. Full-width outlined VIN check

### Header model (frozen for PDP + future WF-V3 screens)

- Dark topbar: city, hours, phone
- White main bar: logo left, centered nav, red pill callback
- USP benefit row as **separate light band** below nav (not OC marquee ticker)
- Static header — no sticky

### Visual class (frozen)

**Class B — Digital Inventory Showroom.** Principles P-01..P-20 from clean-room discovery apply. WF-V3 PDP embodies P-01 (car first), P-07 (flat surfaces), P-09 (one primary red CTA per zone), P-13 (single-vehicle stage), P-14 (price accent).

### Change gate

> **Future work must not modify frozen decisions without a new authority review.**

Authority review requires: written change request · impact on Homepage/Catalog alignment · operator HITL · updated freeze document or explicit supersession charter.

---

## Section 4 — ALLOWED CHANGES

The following may still evolve **without** reopening PDP architecture. Changes must preserve frozen anatomy and reading flow.

| Category | Examples | Constraint |
|----------|----------|------------|
| **Photos** | Production vehicle gallery; studio photography; aspect ratio match | Replace placeholders in existing gallery slots — no layout change |
| **Logos** | Official СИБКАР SVG mark; bank partner logos | Swap assets in frozen cells — no resize-driven layout experiments |
| **Content** | Copy, spec values, discount amounts, equipment list items | Phase 1 truth preserved; operator-verified claims only |
| **Trust evidence** | Wording, icons, proof labels | Same five-item strip model |
| **Bank assets** | Official SVG/PNG logo pack | Same grid cell grammar |
| **Icon system** | Unified icon file / FA subset | Replace inline duplicates — no new trust model |
| **Typography refinement** | Size ±2px, tracking, line-height within Inter stack | No font family change without review |
| **Spacing refinement** | Padding, gap tuning within sections | No section reorder or hero ratio change |
| **CRM integration** | Form POST endpoints, hidden fields, validation | Wire to frozen form zones only |
| **OpenCart integration** | Twig mapping, data binding, Swiper/Fancybox | Map 1:1 to frozen partials — **no** DOM recomposition in integration pass |
| **Mobile responsive** | Stack hero, wrap trust, collapse grids | Must preserve desktop frozen anatomy as source of truth |
| **Related links (Z9)** | Implement deferred section when content ready | Insert **only** in reserved slot between banks and footer |
| **Asset production** | Per `PRODUCTION-ASSET-REQUIREMENTS-v1.md` | Realism pass findings — not redesign |

---

## Section 5 — PROHIBITED WITHOUT REVIEW

The following require a **new authority review** before any work begins. Default answer is **NO** unless charter explicitly authorizes.

| Prohibition | Rationale |
|-------------|-----------|
| **New hero layout** | 65/35 split is P0 defining characteristic |
| **Moving sections** | Section order encodes conversion and trust model |
| **Replacing trust model** | Five-item post-hero strip is Class B verification grammar |
| **Replacing credit model** | Dedicated post-equipment module — not inline hero form |
| **Replacing information architecture** | Title row + hero + scroll depth is frozen reading path |
| **Redesigning PDP from scratch** | Repeats WF-V2 failure mode |
| **Merging banks into credit or hero** | Breaks credibility layering |
| **H1 inside gallery / removing title row** | Reverts to OC catalog-heading pattern |
| **50/50 or inverted gallery/offer** | Legacy template geometry |
| **Third promo strip / marquee ticker** | P-04 violation |
| **Card-in-card or shadow stacks** | P-07 violation; proven WF-V2 debt |
| **Sticky header** | Operator-rejected; P-11 |
| **Importing WF-V2 / TEST CSS hooks** | Clean-room contamination |
| **Multiple primary red CTAs per zone** | P-09 violation |
| **1780px container widen** | Legacy WF-V2 rule — concept uses standard width |
| **Agent-led visual score as authorization** | P-20 / P0-05 — operator HITL only |

---

## Section 6 — SUCCESSFUL DECISIONS

Lessons captured from WF-V3 PDP program — apply to Homepage and downstream work.

| Decision | Why it worked |
|----------|---------------|
| **Composition before decoration** | v0.1 locked anatomy; v0.2 polished surfaces without reordering — avoided WF-V2 cosmetic loop |
| **Clean-room before integration** | Isolated workspace with zero TEST CSS import — no legacy DOM ceiling |
| **Architecture before polish** | Operator accepted v0.1 on zones; visual pass deferred to v0.2 |
| **Assets after structure** | Asset realism pass v0.2.1 audited slots without triggering layout experiments |
| **Proof before implementation** | Side-by-side with concept PNG + screenshots before any OpenCart charter |
| **Single design authority** | One PNG + one prototype chain — no parallel concepts |
| **Restore point before polish** | `site-001-wf-v3-pdp-prototype-v0.1-20260611` enabled safe v0.2 pass |
| **Class prefix isolation** | `wf-v3-*` prevented accidental reuse of `wfv2-` / `w5c-` hooks |
| **Two-surface discipline** | Removed credit card-in-card — directly addressed W5-C / WF-V2 debt |
| **Operator architecture gate** | v0.1 APPROVED AS ARCHITECTURE before VISUAL PASS — correct sequencing |

**Anti-patterns avoided (explicit):** append-only CSS on TEST · anatomy patch after cosmetic pass · three competing design authorities · technical PASS substituting visual ACCEPT.

---

## Section 7 — WF-V3 PDP Status

| Layer | Status | Evidence |
|-------|--------|----------|
| **Architecture** | **COMPLETE** | v0.1 operator-approved; preserved through v0.2; restore point registered |
| **Visual System** | **COMPLETE** | VISUAL PASS v0.2 — tokens, typography, surfaces, section polish |
| **Asset Layer** | **PARTIAL** | ASSET REALISM PASS v0.2.1 complete — audit done; production photos, logo, bank SVGs still placeholder |
| **Integration Layer** | **NOT STARTED** | No OpenCart · no TEST · no CRM wiring |
| **Homepage Alignment** | **NOT STARTED** | Homepage prototype not built — largest perception gap remains |
| **Catalog Alignment** | **NOT STARTED** | Catalog card grammar not prototyped |

---

## Section 8 — Next Recommended Stage

### Recommendation: **WF-V3 Homepage Prototype**

Do **not** recommend OpenCart integration at this stage.

| Stage | Priority | Reason |
|-------|----------|--------|
| **WF-V3 Homepage Prototype** | **P0 — next** | Charter: [SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md](SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md) |
| OpenCart PDP merge | Deferred | Integration without homepage alignment repeats WF-V2 «PDP-only» gap |
| TEST deploy | Deferred | Prototype-first per P-16 |
| Catalog prototype | After Homepage v0.1 | Card grammar inherits PDP; homepage is entry route |

### Why Homepage is the largest perception gap

Evidence from program history:

- W4.1 Visual Proof Pack: homepage first screen **3/10**; visitor notice **NO**; PDP promo **partial** only.
- Clean-room discovery: homepage = carousel-first OC grammar; no search on first screen; fails 3-second Class B test.
- PDP freeze establishes **downstream** authority — but entry route `/` still reads as legacy dealer template.
- Operator mandate «заметно иначе без A/B» fails if visitor never reaches frozen PDP.

**Success path:** Homepage prototype built under charter → side-by-side with frozen PDP → operator confirms single brand and design system → then catalog card → then integration charter.

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Mobile layout authority | **SAFE UNKNOWN** — not in concept PNG; responsive pass is allowed change, not frozen desktop anatomy |
| Z9 related links in prototype | **PARTIAL** — reserved in IA; not implemented in v0.1/v0.2 |
| WF-V3 PDP CRITICAL DESIGN REVIEW doc | **NOT FOUND in repo** — asset pass notes SAFE UNKNOWN |
| Exact container px width | Directional ~1200–1400px — measure in prototype, not a freeze amendment |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 PDP Design Authority Freeze v1 — documentation only; no implementation; no commit implied.*
