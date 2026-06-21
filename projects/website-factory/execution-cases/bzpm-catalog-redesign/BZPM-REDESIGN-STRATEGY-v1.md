# BZPM Redesign Strategy v1

**Execution case:** `bzpm-catalog-redesign`  
**Date:** 2026-06-08  
**Status:** **Approved strategic direction** — documentation only  
**Rule:** No redesign proposals, mockups, or implementation in this document.

This strategy synthesizes completed research (W0–W2, W1D) into **directional objectives**. Tactical UI decisions belong to W3 Blueprint phase.

---

## 1. Catalog Efficiency

**Objective:** Reduce decision friction in the catalog hierarchy without large-scale taxonomy restructuring — improve how buyers traverse type → family → series → SKU on an OEM product-database model.

**Rationale:**

- W1C observed chain type → family → series → SKU, but parent categories simultaneously expose chips and flat SKU grids — buyers can skip series context.
- W1B: parent «Моечные ванны» mixes five product families on page 1; 18 chips use overlapping axes (series × sections × type).
- W1D: market norm is product-database navigation (Trapeza, Abat); large taxonomy restructure is **rejected** at current stage (R-03).
- W2: series page «ПРЕМИУМ-3» is **less fragmented** than parent — coherent 10-SKU scope is the efficiency benchmark within existing structure.

**Evidence source:** W1B §6 Category hierarchy; W1C Buyer Journey Map; W1D Market Patterns; W2 §Series page analysis; [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md) R-03

---

## 2. Product Listing Cards

**Objective:** Increase **semantic density** of listing cards so buyers can discriminate models without opening every PDP — within the market-accepted thin-card pattern.

**Rationale:**

- W1B: cards show status, article, name (with embedded dims), price, CTA — no sections, material, series, or lead time fields.
- W1C: listing does not support meaningful compare-before-PDP (WH-06).
- W1D: Trapeza exposes brand/model and category-specific chips on listings; thin cards are market-norm (V-12) but BZPM **below Trapeza** on semantic fields (W2 WH-20).
- Factory codes in titles require buyer-side decoding (WH-03, V-03).

**Evidence source:** W1A IA-01; W1B §1 Product selection; W1D Trapeza Analysis §2–3; W2 F-10, Density Benchmark table

---

## 3. Product Page First Screen

**Objective:** Make the first screen answer **«is this the right model in the right series?»** before scroll — without assuming sibling-SKU matrix is market-standard.

**Rationale:**

- W1A FS-01: no series/lineage context on first screen; series visible only in breadcrumbs.
- W1A FS-02: placeholder mini-description undermines trust on evaluation screen.
- W1A MO-01: mobile gallery ~460px pushes price/CTA below fold.
- W1D V-09: sibling SKU matrix on PDP **not market standard** — strategy favors **series context + structured props**, not full matrix clone.
- W1D partial X-01: import-market PDPs show brand/model above fold; BZPM OEM series gap is **real** in own-catalog context.

**Evidence source:** W1A First Screen Findings; W1A Mobile Findings; W1D Hypothesis Validation (PS-02, FS-01); W2 PDP zone classification

---

## 4. Information Density

**Objective:** Improve **visible information packaging** — reduce space-to-meaning mismatch and fragmentation across surfaces, responding to owner feedback without treating it as automatically correct.

**Rationale:**

- W2: owner «empty space» **partially confirmed** on PDP gallery (520px, 1 image) and top catalog cards; «under-informative» **mixed** — 20+ specs exist but 2/3 tabs hidden; «scattered» **confirmed** (taxonomy on 3+ surfaces).
- W1A ID-01: hero props duplicate spec-table head rows.
- W2: dimensions on 4 surfaces; availability duplicated on cards.
- W1D: tabbed specs on PDP = Trapeza pattern (not anomaly); hiding is market-norm but reduces visible density.

**Evidence source:** W2 Executive Summary; W2 Information Fragmentation Analysis; W2 Information Duplication Analysis; W1A Information Density Findings; W1D Trapeza PDP workflow

---

## 5. Commercial Focus

**Objective:** Surface B2B procurement signals **at points of choice** (card, first screen, CTA zone) — price, availability, lead time, dealer/opt path — without duplicating full site-wide commercial blocks.

**Rationale:**

- W1A CV-01: PDP lacks B2B context near CTA (dealer, lead time, regional delivery) though present in header/category ecosystem.
- W1B: «Под заказ» + «Срок поставки 5–10 дней» on some cards but not systematic; `p-card__delivery` empty (W2-F-05).
- W2 Commercial Density: dealer form + certificates **repeat** on every catalog level — high space, low incremental value on deep pages.
- W1D: dealer/consultative offload common (Abat, Rational); self-serve + human CTA coexist.

**Evidence source:** W1A Conversion Findings; W1B §4 Information density; W2 Commercial Density Analysis; W1C Decision Point D7–D8

---

## 6. Repeated Content

**Objective:** Reduce **wasteful duplication** that increases scroll cost without adding decision value — especially identical commercial/trust blocks and redundant fields per card.

**Rationale:**

- W2: certificates slider + dealer form **identical** on `/katalog`, neutral equipment, and sink category pages.
- W2: availability duplicated in `p-card__top` and `p-card__body`; article ↔ name semantic duplication.
- W1A ID-01: L×W×H×mass in hero and spec-table header.
- W2: advantages blocks partially repeat header nav themes.

**Evidence source:** W2 F-07, F-11–F-12, F-19; W2 Information Duplication Analysis; W1A ID-01

---

## 7. Mobile Efficiency

**Objective:** Preserve desktop-equivalent **decision information** on mobile — especially filters and compare discoverability — without assuming mobile renders were verified on device.

**Rationale:**

- W1B §7: ≤1024px filters → fullscreen overlay; 18 chips → horizontal scroll without «more» indicator.
- W1A MO-01: 460px gallery consumes first screen on phone/tablet.
- W2 Mobile Density: filters hidden at ≤1024px — densest narrowing tool removed from visible layer; tips/popups hidden on cards.
- W1B: icon-only compare/favorite — lower discoverability on touch (W1A MO-04).

**Evidence source:** W1B §7 Mobile category UX; W1A Mobile Findings; W2 Mobile Density Analysis; UNKNOWN U-04 (no device screenshots)

---

## 8. Trapeza Lessons

**Objective:** Use Trapeza as **reference for product-database patterns** (filters, PDP structure, brand/model fields) — explicitly **not** as layout or taxonomy blueprint.

**Rationale:**

- Decision D-03 / R-01: Trapeza = distributor marketplace; BZPM = OEM catalog-platform — different model.
- Adoptable patterns (W1D): functional subtaxonomy for sinks; **section-count filters**; brand/model on cards; structured PDP specs; sort by popularity/price/stock; `/compare/` infrastructure.
- Non-adoptable: Trapeza brand-index-first navigation; 1000+ SKU marketplace scale; Q&A community as primary selection channel.
- BZPM-specific retained: OEM series as subcategories (W1D: **rare** market pattern) — strategy is to **clarify**, not replace with Trapeza taxonomy.

**Evidence source:** W1D Trapeza Analysis (§1–10); W1D Market Patterns; W1D Hypothesis Validation; [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md) D-03, R-01

---

## Strategy boundaries

| In strategy scope | Out of strategy scope (deferred/rejected) |
|-------------------|------------------------------------------|
| Directional objectives above | Wireframes, mockups, CSS/HTML changes |
| Evidence-linked rationale | Full nomenclature decoding (D-02, R-02) |
| Market-informed pattern adoption | Copy Trapeza directly (R-01) |
| Efficiency within existing taxonomy | Large-scale catalog restructuring (R-03) |
| W3 blueprint preparation | W1E taxonomy audit (D-01) |

---

## Evidence index

| Phase | Canonical source in repo |
|-------|--------------------------|
| W0–W2 | [BZPM-FINDINGS-REGISTER-v1.md](BZPM-FINDINGS-REGISTER-v1.md) |
| Decisions | [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md) |
| State | [BZPM-AUDIT-STATE-v1.md](BZPM-AUDIT-STATE-v1.md) |

**Prior session reports** (pre-consolidation): [BZPM W0 MARS Audit](2bb0e455-ec2f-4673-8a1d-9377e80e4e69) · [W1A Product Audit](dec26b4f-83b7-42b0-96cf-eb550523fe43) · [W1B Category Audit](0397a470-c60b-4ed0-99d9-e69c84c5cca5) · [W1C Buyer Decision Flow](c7e1734f-b81a-4868-9234-00c48b62c9fc) · [W1D Competitor Intelligence](287ed44a-d36e-43d3-a397-cefaa8f6469e) · [W2 Information Density](9573c283-675f-4f34-b4c0-f717ea396c38)

---

*BZPM Redesign Strategy v1 — strategic direction only; implementation requires W3 charter.*
