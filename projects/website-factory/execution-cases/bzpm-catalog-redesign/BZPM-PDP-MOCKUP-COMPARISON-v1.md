# REPORT — BZPM PDP MOCKUP EXPLORATION

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-PDP-MOCKUP-COMPARISON-v1`  
**Phase:** W7 — PDP Mockup Exploration  
**Lane:** A (Website Factory)  
**Mode:** Visual direction comparison — no implementation  
**Date:** 2026-06-09  

**Artifacts compared:**

| ID | Direction | Document |
|----|-----------|----------|
| **Baseline** | Current PDP (audit) | W1A/W2 findings via approved artifacts |
| **A** | Conservative Evolution | [BZPM-PDP-MOCKUP-A-v1](BZPM-PDP-MOCKUP-A-v1.md) |
| **B** | Industrial Procurement | [BZPM-PDP-MOCKUP-B-v1](BZPM-PDP-MOCKUP-B-v1.md) |

**Shared IA (unchanged in both mockups):**  
[BZPM-REDESIGN-ARCHITECTURE-v1](BZPM-REDESIGN-ARCHITECTURE-v1.md) · [BZPM-BLUEPRINT-v1](BZPM-BLUEPRINT-v1.md) · [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md) · [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md) · [BZPM-PDP-WIREFRAME-ALPHA-v1](BZPM-PDP-WIREFRAME-ALPHA-v1.md)

**Reference SKU:** ВМЦ-П3-2/500 · серия ПРЕМИУМ-3

**Purpose:** Side-by-side comparison for stakeholder decision — **which direction feels closer to the future BZPM?** Not a final design pick.

---

## Executive Summary

Оба mockup реализуют Concept Alpha **«Серийная верификация»** и block map Wireframe Alpha (USR-PDP-00–21) без изменения decision flow. Различие — **только visual packaging**:

| | Mockup A — Conservative Evolution | Mockup B — Industrial Procurement |
|---|-----------------------------------|-----------------------------------|
| **Question** | «Что если текущий BZPM пересобрали правильно?» | «Что если BZPM проектировали вокруг скорости выбора?» |
| **Hero pattern** | Classic 2-column: gallery + buy box | Data panel: series band + grid + integrated commercial |
| **Series** | Line under H1 | Full-width band |
| **Density** | Moderate | High |
| **Stakeholder shock** | Low | Medium–High |

**Neither mockup** replaces final UI design, OpenCart work, or content production. Both require the same CMS/content prerequisites (series descriptors, in-series relations OQ-02, min spec rows).

---

## Mockup A — Summary

**Name:** Conservative Evolution

**Visual thesis:** Узнаваемая эволюция текущей PDP — исправления Alpha встроены в привычную двухколоночную композицию.

**First-screen signature:**

```text
[ Gallery ~40% ]  [ H1 + series line + BUY BOX ]
[──────── Fit strip: dims + critical attrs ────────]
```

**Best for:** stakeholder presentations where **recognizability** and **low rollout shock** dominate; mixed buyer base (visual + procurement).

**Key tradeoff:** Series visibility and WH-16 gallery void mitigation **weaker** than Mockup B.

→ Full artifact: [BZPM-PDP-MOCKUP-A-v1](BZPM-PDP-MOCKUP-A-v1.md)

---

## Mockup B — Summary

**Name:** Industrial Procurement

**Visual thesis:** Procurement-first instrument — series band + attribute grid + inline B2B signals; decorative footprint minimized.

**First-screen signature:**

```text
[══════ SERIES BAND: ПРЕМИУМ-3 ══════]
[thumb] │ H1 + article │ FIT GRID 2×4 │ COMMERCIAL ROW + B2B links
```

**Best for:** expert/sнабженец persona, series-first strategy continuation, explicit break from broken current PDP.

**Key tradeoff:** **Higher** overload and stakeholder resistance risk; implementation departs from current theme pattern.

→ Full artifact: [BZPM-PDP-MOCKUP-B-v1](BZPM-PDP-MOCKUP-B-v1.md)

---

## Density Comparison

### Quantitative model (visible facts, first screen, no tab)

| Layer | Current PDP | Mockup A | Mockup B |
|-------|-------------|----------|----------|
| Identity facts | 3 (H1, article, breadcrumb series) | 4 (+ explicit series link) | 5 (+ series band meta) |
| Dimensional / critical attrs | 4 (L×W×H×mass) | 8 (+ sections, bowl, material, construction) | 8 (same — grid layout) |
| Commercial facts | 3 (status, price, CTA) | 3–4 | 5–6 (+ delivery/dealer preview) |
| Actions | 1 (CTA) | 3 (+ labeled compare/fav) | 3 (integrated row) |
| **Approx. total** | **~6 decision-useful** | **~14** | **~18–20** |

*Approximation for comparison only — not a performance metric.*

### Qualitative dimensions

| Dimension | Current | Mockup A | Mockup B |
|-----------|---------|----------|----------|
| **Density** | Low — specs hidden in tabs (W1A-F-05) | **Moderate** — visible packaging increase | **High** — table-first |
| **Clarity** | Poor series/alternatives path | **Good** — familiar scaffold | **Very good** for experts; novices need learning |
| **Scan speed (expert)** | Fast price/article; slow fit | Good | **Best** |
| **Scan speed (novice)** | Slow (tab discovery) | **Best** (gallery anchor) | Medium |
| **Procurement suitability** | Weak near CTA (WH-15) | Improved on scroll | **Strongest** at P1 |

### Density visualization

```text
FIRST-SCREEN INFORMATION PAYLOAD (relative)

Current   ██░░░░░░░░░░░░░░░░░░  ~30%
Mockup A  ████████░░░░░░░░░░░░  ~65%
Mockup B  ██████████████░░░░░░  ~90%

DECORATIVE WHITESPACE (inverse = efficiency)

Current   ████████████████████  high void (WH-16)
Mockup A  ████████████░░░░░░░░  medium
Mockup B  ████░░░░░░░░░░░░░░░░  low
```

**Shared constraint (both mockups):** P-05 — no new backend fields for v1 sink minimum; density = repackaging only.

---

## Risk Analysis

### Side-by-side risk matrix

| Risk category | Current (baseline) | Mockup A | Mockup B |
|---------------|-------------------|----------|----------|
| **Information overload** | Under-informative (tabs) | Low–Medium (strip + min spec) | **High** (grid + band + B2B inline) |
| **Stakeholder resistance** | Status quo pain accepted | **Low** («finally fixed») | **Medium–High** («foreign UI») |
| **Implementation complexity** | N/A | **Low–Medium** (theme evolution) | **Medium–High** (new layout paradigm) |
| **Mobile first-screen fit** | CTA below gallery (MO-01) | Medium (P1 stack) | **High** (band + grid + commercial) |
| **Content dependency collapse** | Placeholders visible (W1A-F-03) | Medium — empty series line weak | **High** — empty band very visible |
| **Merchandising pushback** | Misaligned «Похожие» entrenched | Low — familiar carousel slot | Low — table alts less «marketing» |
| **Gallery / brand warmth** | High gallery, low info | **Preserves warmth** | **Reduced** — thumb-first |
| **ID-01 duplication** | Hero = 4 rows only | Medium — strip vs min spec | **Medium–High** — grid vs table |

### Mockup A — top risks

1. Fixes may look **cosmetic** if not annotated against audit findings
2. Series line **too subtle** — WH-13 partially unresolved visually
3. Gallery void **partially persists** (WH-16)

### Mockup B — top risks

1. **Stakeholder shock** — largest project risk
2. Mobile P1 **viewport overflow** (OQ-09)
3. Casual buyers **lose visual anchor** before decision

### Risks unchanged in both (content / engineering)

| ID | Risk | Impact |
|----|------|--------|
| OQ-01 | Non-sink category-critical props undefined | USR-PDP-05 incomplete outside моечные ванны |
| OQ-02 | «Похожие» CMS relation | USR-PDP-12 may need backend change |
| OQ-09 | Mobile P1 device validation | Both directions IMPL-DEPENDENT |
| U-02 | Compare populated UX | USR-PDP-13 feedback unknown |

---

## Comparison Matrix

| Criterion | Current | Mockup A | Mockup B |
|-----------|---------|----------|----------|
| **Information Density** | Low — 4 hero props; 2/3 tabs hidden | **Moderate** — +series, +critical, min spec visible | **High** — grid + band + B2B inline |
| **Series Visibility** | Breadcrumb only (WH-13) | **Line under H1** — readable, not dominant | **Prominent band** — strongest WH-13 fix |
| **SKU Validation** | L×W×H×mass only (WH-14 gap) | **Horizontal fit strip** — 8 attrs scannable | **2×4 grid** — fastest expert scan |
| **Procurement Support** | Header nav; weak at CTA (WH-15) | B2B on scroll (Zone 6) | **P1 integrated** delivery/dealer preview |
| **Mobile Readability** | Gallery pushes CTA down (MO-01) | Commercial P1; gallery P4 | Commercial P1; band + grid stack risk |
| **Commercial Clarity** | Strong price/status/CTA | **Familiar buy box** — clear hierarchy | Unified panel — dense but complete |
| **Stakeholder Risk** | Baseline (broken IA accepted) | **Low** — evolutionary | **Medium–High** — paradigm shift |
| **Implementation Risk** | N/A | **Low–Medium** — theme extend | **Medium–High** — new composition |

### Scoring guide (for workshop use)

Use **qualitative 1–5** in stakeholder session — not computed here:

```text
                    Current  A    B
Series Visibility      1     3    5
Procurement            2     3    5
Recognizability        4     5    2
Expert scan speed      2     4    5
Novice friendliness    2     4    3
Implementation ease    —     4    2
Stakeholder safety     —     5    2
```

*Scores illustrative — workshop should assign own weights per client priority.*

---

## First Screen — Visual Diff (side-by-side)

```text
MOCKUP A (Conservative)          MOCKUP B (Industrial)
─────────────────────────        ─────────────────────────
Breadcrumb                       Breadcrumb (compact)
                                 ╔══════════════════════╗
┌──────────┬─────────────┐       ║ SERIES BAND          ║
│ GALLERY  │ H1          │       ╚══════════════════════╝
│  large   │ series line │       ┌──┬──────────────────┐
│          │ ┌─────────┐ │       │th│ H1 + GRID + BUY  │
│          │ │ BUY BOX │ │       └──┴──────────────────┘
└──────────┴─────────────┘
[ fit strip ──────────── ]       (grid includes fit + commercial)

Same blocks: USR-PDP-00–07        Same blocks: USR-PDP-00–07
Same decision gates: D3·D6·D7     Same decision gates: D3·D6·D7
```

---

## Decision Flow — Unchanged in Both

Both mockups preserve UX Structure decision ladder:

```text
Correct Series?  → USR-PDP-02
Correct Model?   → USR-PDP-01 + USR-PDP-04/05 + USR-PDP-06
Correct Specs?   → USR-PDP-08/09/10/11
Available?       → USR-PDP-03 (+ USR-PDP-18)
Alternative?     → USR-PDP-12 (in-series ONLY)
Convert?         → USR-PDP-03 + USR-PDP-19 + USR-PDP-18
```

**Visual difference:** Mockup B surfaces more gates **on first screen**; Mockup A defers spec confirmation to **first scroll**.

---

## Recommendation

**No single winner declared.** Direction depends on stakeholder priorities and buyer persona weighting.

### When Mockup A is preferable

| Condition | Rationale |
|-----------|-----------|
| First client-facing design pass | Minimizes «why does our site look different?» |
| Mixed audience (visual + technical) | Gallery anchor helps novices |
| Implementation timeline constrained | Theme evolution vs new layout system |
| Management measures success by **acceptance** | Lower resistance path |
| Polygon / existing theme assets reused | Less throwaway UI work |

### When Mockup B is preferable

| Condition | Rationale |
|-----------|-----------|
| B2B / procurement persona dominates | P1 B2B integration addresses WH-15 directly |
| Client explicitly wants visible **break** from current PDP | Signals real redesign, not patch |
| Series-first strategy is strategic narrative | Band continues ПРЕМИУМ-3 benchmark (W2-F-10) onto PDP |
| Expert repeat buyers are primary revenue | Scan speed + grid density |
| Design team ready for **new composition system** | Not constrained to current 2-column |

### Hybrid path (valid next step — not a third mockup)

Workshop may identify **split adoption**:

| Element | Often borrowed from |
|---------|---------------------|
| Series band | Mockup B |
| Buy box familiarity | Mockup A |
| Fit presentation | A strip **or** B grid by family |
| In-series block density | Mockup B table on desktop; A carousel if marketing insists |

Hybrid requires **one more visual pass (W7.1)** — not implementation.

### What to test visually next (regardless of direction)

| # | Test | Why |
|---|------|-----|
| 1 | **Stakeholder side-by-side** — A vs B on same SKU | Core W7 deliverable |
| 2 | **Fold line photography** — 1366×768 and 375×667 | OQ-09 |
| 3 | **Series weight variants** — A line vs A badge vs B band | WH-13 sensitivity |
| 4 | **In-series block** — carousel (A) vs table (B) | W1A-F-06 fix perception |
| 5 | **Empty CMS states** — no series descriptor, no siblings | Content collapse risk |
| 6 | **CTA hierarchy** — cart vs consult vs dealer | PS-05 / CV-01 |
| 7 | **Non-sink SKU** — столы / тепловое placeholder | OQ-01 gap visibility |

**Suggested workshop sequence:**

1. Show **current pain** (3 screenshots: series in breadcrumb only, hidden tabs, misaligned «Похожие»)
2. Show **Wireframe Alpha** block map (IA agreement — already approved)
3. Place **Mockup A** and **Mockup B** side-by-side
4. Score comparison matrix with client weights
5. Decide: **A**, **B**, or **hybrid brief** for first hi-fi design (W8)

---

## IA Compliance Checklist

Both mockups validated against frozen IA:

| Rule | Mockup A | Mockup B |
|------|----------|----------|
| USR-PDP-00–21 block map preserved | ✓ | ✓ |
| No sibling SKU matrix (V-09) | ✓ | ✓ |
| In-series before cross-family (UX-15) | ✓ | ✓ |
| Misaligned «Похожие» suppressed | ✓ | ✓ |
| Min spec default-visible (W1A-F-05) | ✓ | ✓ |
| Consultative CTA elevated (UX-17) | ✓ | ✓ |
| Mobile commercial P1 (P-09) | ✓ | ✓ |
| No Trapeza taxonomy copy (R-01) | ✓ | ✓ |
| Placeholder/demo suppressed (CP-23) | ✓ | ✓ |
| ID-01 dedup rules acknowledged | ✓ | ✓ |

---

## Document Lineage

| Input | Role |
|-------|------|
| [BZPM-PDP-MOCKUP-A-v1](BZPM-PDP-MOCKUP-A-v1.md) | Direction A full artifact |
| [BZPM-PDP-MOCKUP-B-v1](BZPM-PDP-MOCKUP-B-v1.md) | Direction B full artifact |
| [BZPM-PDP-WIREFRAME-ALPHA-v1](BZPM-PDP-WIREFRAME-ALPHA-v1.md) | Shared structural baseline |
| [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md) | Shared concept «Серийная верификация» |

**Next phase:** Stakeholder workshop → optional W7.1 hybrid refinement → W8 first hi-fi PDP design (single direction or hybrid brief).

---

*BZPM-PDP-MOCKUP-COMPARISON-v1 — comparison only. No implementation. No OpenCart. No final design selection.*
