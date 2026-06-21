# SITE-001 WF-V3 Homepage Prototype Charter v1

**Type:** Prototype scope charter — documentation only  
**Date:** 2026-06-11  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Precedes:** Homepage implementation (not authorized by this document)

**Explicit exclusions (honored):** No design · No implementation · No HTML · No SCSS · No JS · No OpenCart · No TEST · No FTP · No commit implied

**Binding authority for alignment:**

- [SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md](SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md)
- `projects/ocpilot/sites/site-001/design/wf-v3-concept/01-sibcar-v3-concept.png` *(homepage zones when available — PDP PNG is primary system reference until homepage concept exists)*
- [SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md](../reports/SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md) — Class B · P-01..P-20
- Frozen PDP prototype: `workspaces/site-001-wf-v3-pdp-prototype/` (v0.2 visual system)

---

## Goal

Create a **Homepage prototype** that matches the **approved PDP design authority**.

The homepage must read as the **same brand and design system** as the frozen WF-V3 PDP — shared header shell, token system, typography, red accent discipline, flat surfaces, and Class B **Digital Inventory Showroom** grammar.

Homepage answers the 3-second question: **«Это современный автосалон — можно сразу искать машину»** — not «промо-слайдер на шаблоне OpenCart».

---

## Scope — Must Include

Prototype v0.1 homepage (desktop-first, ≥ 1280px) must include the following zones. Order may be refined in a future homepage anatomy charter — **this document defines presence only**, not final pixel composition.

### 1. Header

Shared dealer shell with frozen PDP:

- Dark topbar (city, hours, phone)
- White main bar (logo, centered nav, red callback CTA)
- Static — no sticky
- Visual and DOM grammar **aligned with** PDP `layout/header.html` partial

### 2. Hero

First-screen hero that establishes Class B — **not** carousel-first promo:

- Stable headline / value proposition (inventory-first, not rotating offer text)
- Room for search-first entry (see §3)
- Vehicle or inventory presence in frame — car visible, not abstract banner
- One primary red CTA per hero zone

### 3. Search-first experience

Primary user job on homepage = **find a car**:

- Search / filter entry visible on **first screen** (P-05)
- May be overlapping hero or immediately below — implementation detail deferred
- Visual weight: search is a **first-class citizen**, not buried in nav-only catalog link

### 4. Featured inventory

Peek at real stock — proves «у них есть машины»:

- Featured used vehicles (card grammar consistent with future catalog)
- Car photography dominant; price visible
- Flat card surfaces — no card-in-card (P-07)

### 5. Trust layer

Dealer credibility without promo panic:

- Locality · contact · verification signals
- Integrated into homepage journey — not disconnected four-icon strip below unrelated carousel
- Tone aligned with PDP trust row (proof, not marquee CAPS)

### 6. Dealer advantages

USP / benefits communication:

- Equivalent role to PDP benefit row (Z1) — dealer strengths, credit hook, inspection claims
- Supporting layer — must not compete with search or featured inventory for first-screen dominance

### 7. CTA sections

Conversion paths without CTA noise:

- Callback / contact / credit entry points
- Secondary to search and inventory discovery
- One primary red action per viewport zone (P-09)

### 8. Footer

Shared with PDP authority:

- Dark inverse footer — same partial grammar as PDP `layout/footer.html`
- Contact repeat, catalog columns, legal links
- Ensures end-of-page brand continuity

---

## Scope — Must Not Include

The following are **explicitly out of scope** for the Homepage Prototype charter. A separate charter required for each.

| Excluded | Reason |
|----------|--------|
| **OpenCart integration** | Prototype-first per P-16; no Twig/PHP/FTP |
| **Catalog logic** | No product queries, pagination, or OC category engine |
| **Filters backend** | Search UI may be static — no server-side filter implementation |
| **CRM** | No form POST, lead routing, or webhook wiring |
| **Forms implementation** | Callback / credit forms = visual shells only (`href="#"`, display-only) |
| **TEST deploy** | Local workspace build only |
| **Mobile responsive pass** | May follow desktop ACCEPT — not blocking v0.1 charter scope definition |
| **New cars `/auto/` full flow** | Secondary persona — deferred per clean-room discovery |
| **PDP redesign** | PDP frozen — homepage inherits, does not redefine |
| **Token/atmosphere FINISHING-only passes** | Composition ACCEPT before polish-only loops |

---

## Alignment Rules

When Homepage prototype work is authorized (future implementation task), it **must**:

1. Reuse or mirror PDP **header** and **footer** partials — no divergent dealer shell.
2. Apply PDP v0.2 **token system** (`foundations/_tokens.scss` roles) — brand red, surfaces, typography (Inter).
3. Honor **P-01..P-20** from clean-room discovery — especially P-02 (inventory is hero), P-03 (one dealer shell), P-04 (no third promo strip), P-05 (search first-class), P-11 (static header).
4. Use `wf-v3-*` class prefix — no legacy `wfv2-` / `w5c-` / TEST hooks.
5. Preserve **Phase 1 frozen truth** — brand СИБКАР, phone, address, menu labels, legal link titles (P-19).

When Homepage prototype work is authorized, it **must not**:

1. Introduce a new visual class or competing design authority.
2. Reopen PDP frozen anatomy (see freeze document §3).
3. Import TEST `main.css` or append-only CSS workflow.

---

## Deliverable Shape (planned — not created by this charter)

Future implementation task (not this document) expected to produce:

```text
workspaces/site-001-wf-v3-homepage-prototype/   # name TBD at implementation charter
├── src/pages/index.html
├── src/partials/...                             # homepage sections + shared layout from PDP
├── src/scss/...                                  # extends PDP foundations
└── dist/index.html
```

Exact file tree defined in a future **Homepage Prototype Write Charter** — not here.

---

## Success Condition

An operator can open **Homepage** and **PDP** side-by-side (same viewport, same build) and **immediately understand they belong to the same brand and design system**.

### Operator-facing checklist (for future HITL)

| # | Criterion |
|---|-----------|
| 1 | Header is visually identical in shell grammar (topbar + nav + CTA) |
| 2 | Typography, red accent, and surface tokens match PDP v0.2 |
| 3 | Homepage first screen passes Class B 3-second read — search + inventory, not carousel promo |
| 4 | No OC three-band / marquee template silhouette on homepage |
| 5 | Featured inventory cards feel like siblings of future catalog / PDP vehicle stage |
| 6 | Trust and advantages layers use same proof tone as PDP trust row |
| 7 | Footer is shared system — not a separate dark theme experiment |
| 8 | Logo hidden test: visitor sentence matches «современный автосалон с витриной склада» |

**Authorization field:** `VISUAL_ACCEPT` — operator HITL only (P0-05). No agent scores.

---

## Sequencing

| Step | Action | Status |
|------|--------|--------|
| 1 | PDP design authority freeze | **DONE** — [freeze v1](SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md) |
| 2 | Homepage prototype charter (this document) | **DONE** |
| 3 | Operator ratification of charter | **OPEN** |
| 4 | Homepage prototype write charter + workspace creation | **NOT STARTED** |
| 5 | Homepage v0.1 build (desktop) | **NOT STARTED** |
| 6 | Side-by-side HITL: Homepage + PDP | **NOT STARTED** |
| 7 | Catalog card prototype | **NOT STARTED** |
| 8 | Integration charter (OpenCart) | **NOT STARTED — explicitly deferred** |

---

## Risks

| Risk | Mitigation |
|------|------------|
| No homepage concept PNG | Derive zones from clean-room discovery §4 Class B + W5 Blueprint homepage target; PDP tokens as system anchor |
| Header drift between pages | Mandate shared partial — copy from PDP workspace, do not redesign |
| Search UI becomes decorative | P-05 gate in HITL — search must be visible and weighted on first screen |
| Repeating WF-V2 homepage carousel | Explicit anti-pattern in freeze + discovery; charter forbids carousel-first |
| Starting integration before homepage ACCEPT | Freeze document §8 — integration deferred |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Homepage concept PNG | **SAFE UNKNOWN** — only PDP concept PNG confirmed in repo; homepage zones from discovery + blueprint |
| Exact homepage section order | **OPEN** — presence defined here; anatomy charter at implementation time |
| Shared workspace vs separate repo folder | **OPEN** — implementation charter decision |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Homepage Prototype Charter v1 — scope definition only; no design; no implementation; no commit implied.*
