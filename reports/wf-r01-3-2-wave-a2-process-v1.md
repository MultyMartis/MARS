# REPORT — WF-R01.3.2 WAVE A2 PROCESS

**Artifact ID:** WF-R01.3.2 Wave A2 — PROCESS reference partial (v1)  
**Date:** 2026-06-19  
**Mode:** controlled reference-layer execution pass — **one block only**  
**Authority:** [wf-r01-3-2-landing-completion-charter-v1.md](../projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md) (**ACCEPTED**)

**Honesty boundary:** Human-operated extraction pass. **Not** runtime, **not** G1 reached, **not** new `block_id` minted.

---

## Executive Summary

Официальный Reference Partial для `PROCESS` создан в `workspaces/website-factory-reference-v1/`. Структура извлечена из Triumph V6 `order-steps--process` (horizontal/vertical step timeline); приведён к **VF_PROCESS_STEP_TIMELINE** и wf-* conventions. `npm run build` — **PASS**. RPC: **10/32 → 11/32** (partial-file count, denominator 32).

Wave A2 scope **закрыт**. Следующий pass: Wave A3 `TESTIMONIALS` + TRUST narrow split only.

---

## Source Selection

### Candidates evaluated

| Source | Location | Verdict |
|--------|----------|---------|
| **Triumph V6** | `v5-ppc/zakaz/screen-02b-order-steps.html` + `_v5-order-steps.scss` (`order-steps--process`) | **Selected (primary)** — 4-step numbered timeline with connectors; maps to `PROCESS` / VF_PROCESS_STEP_TIMELINE |
| **Triumph V6 (legacy grid)** | `v5-page01/screen-02b-order-steps.html` (`order-steps__grid`) | **Rejected** — flat card grid without step-track semantics; weaker timeline signal |
| **Triumph (scroll pattern)** | [scroll-process-timeline-pattern-v1.md](../projects/mars-website-factory/scroll-process-timeline-pattern-v1.md) | **Rejected** — F4 Commercial Pattern (`scroll_process_timeline`); REG-VOC-06 — must not register as `block_id` |
| **ISBD** | `isbd-care-landing/src/partials/sections/process.html` | **Peer validation only** — explicit `process` naming confirms block semantics; client PNG assets and `isbd-*` scope not ported |
| **Reference assets** | VF_PROCESS_STEP_TIMELINE, `benefits.html` wf-section shell | **Applied** — wf-section header, token hygiene, neutral EN copy |

### Rationale (binding for this pass)

Charter assigns Triumph as **primary extraction driver**. V6 `order-steps--process` — closest TEMPLATE_ART-aligned standalone step timeline without scroll-driven F4 pattern or checkout stepper coupling. ISBD confirms naming and 4-step card flow but **does not** drive extraction per charter routing (secondary adoption case).

---

## Vocabulary Validation

| Term | Family / role | Boundary vs PROCESS |
|------|---------------|---------------------|
| **PROCESS** | F3 Content Block (`block_id`) | **Canonical target** — ordered engagement/purchase steps on a page band |
| **TIMELINE** | Visual/layout descriptor (not `block_id`) | Describes **presentation** of PROCESS steps (VF_PROCESS_STEP_TIMELINE); not a separate registry block |
| **STEPPER** | UI interaction pattern | Checkout/wizard UI (e.g. VF_CHECKOUT_FLOW_STEPS → CHECKOUT/PAYMENT); **not** marketing PROCESS on LANDING |
| **WORKFLOW** | Authoring / ops word | Internal process documentation; **not** F3 block unless promoted via charter (no promotion in this pass) |
| **ROADMAP** | Product/planning artifact | Program roadmap or product timeline pages; **not** customer-facing PROCESS block |
| **scroll_process_timeline** | F4 Commercial Pattern (`pattern_id`) | Scroll-driven vehicle/track animation — **must not** inflate PROCESS RPC or merge into partial |

**Verdict:** Partial implements **PROCESS** as content block with static step-timeline layout. No pattern-as-block violation (scroll timeline excluded). No stepper/checkout semantics. No new IDs.

---

## Partial Created

| Layer | Path | Notes |
|-------|------|-------|
| **HTML** | `src/partials/sections/process.html` | `data-section` + `data-block-id="process"`; 4 ordered steps; semantic `<ol>` |
| **SCSS** | `src/scss/sections/_process.scss` | Scoped under `.wf-section--process`; horizontal track ≥1024px, vertical timeline below |
| **JS** | — | **Not required** — static informational timeline; progressive enhancement safe without JS |
| **Import** | `src/scss/main.scss` | `@use 'sections/process'` after benefits |
| **Golden slice** | `src/pages/index.html` | Inserted **after BENEFITS**, before `social_proof` (TRUST) — LANDING stack order |

**Extraction discipline applied:** client brand stripped; no Font Awesome; no Triumph/ISBD images; no inline scripts; no embedded CTAs (INFORMATIONAL role; CTA block separate); no scroll-driven animation.

---

## Contract Alignment

### BLOCK-CONTRACT-v1 (`PROCESS`)

| Field | Registry value | Partial alignment |
|-------|----------------|-------------------|
| `block_id` | `PROCESS` | Filename `process.html`; hook `data-block-id="process"` |
| `block_name` | Process / how it works | Section eyebrow + h2 articulate engagement path |
| `block_category` | CONTENT | Content band after benefits |
| `purpose` | Step-by-step explanation of engagement or purchase path | Four numbered steps with title + body |
| `conversion_role` | INFORMATIONAL | No primary CTA in block |
| `allowed_site_types` | LANDING, PROMO, CORPORATE | Neutral reference — no site-type leakage |
| `required_or_optional` | Required (LANDING) | Placed in golden slice LANDING stack |
| `dependencies` | recommends HERO, BENEFITS before | Golden slice: HERO → BENEFITS → PROCESS |

### CC_BLOCK_PROCESS (content contract)

| Signal | Status |
|--------|--------|
| `process` (required) | **Satisfied** — four ordered step statements |
| `objection`, `cta`, `delivery` (optional) | **Absent** — acceptable for T1 reference floor |
| `review`, `legal_disclosure` (forbidden) | **Absent** |

### Visual pattern binding

| Pattern | Status |
|---------|--------|
| VF_PROCESS_STEP_TIMELINE | **Primary** — numbered steps + connectors |
| VF_PROCESS_PHASE_CARDS | **Not used** — fewer-phase variant deferred |

### Registry doc sync (no new IDs)

- [BLOCK-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) — reference partial pointer updated  
- [CORE-BLOCK-LIBRARY-v1.md](../workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md) — `process.html` row added  
- [BLOCK-GAPS-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md) — gap closed for PROCESS

---

## Coverage Impact

**Counting method:** partial-file equivalents; denominator **32** (29 Core + 3 structural Tier A in program scope).

| Dimension | Before (post-A1) | After Wave A2 | Delta |
|-----------|------------------|---------------|-------|
| **RPC** | **10/32** (~31.3%) | **11/32** (~34.4%) | **+1** (`process.html`) |
| **RC** | 32/32 | 32/32 | unchanged |
| **RSC** | 1/10 global · 1/1 LANDING | unchanged | golden slice stack extended; stub manifest still pending |
| **SC** | LANDING partial | LANDING partial — PROCESS checklist item **closed** | incremental |
| **PC** | 0/1 LANDING | 0/1 | Reference Composition doc not in A2 scope |

**Strict unique `block_id` RPC:** **10/32 → 11/32** (10 unique blocks with T1+ partials + CTA variant file accounting unchanged).

**G1 progress:** 11/32 toward target 14/32 — **3 partial-file equivalents remaining** for G1 minimum set.

---

## Validation

| Check | Result |
|-------|--------|
| `npm run build` (reference workspace) | **PASS** (2026-06-19) |
| Vocabulary Canon F3 content block | **PASS** — PROCESS as content block; not structural; not pattern-as-block |
| PROCESS ≠ TIMELINE/STEPPER/WORKFLOW/ROADMAP | **PASS** — documented boundaries; no ID collision |
| scroll_process_timeline excluded | **PASS** — static timeline only |
| WF-R01.1 v1 `block_id` on partial | **PASS** |
| No new IDs | **PASS** |
| JS optional rule | **PASS** — no JS added |
| Golden slice order HERO → BENEFITS → PROCESS → TRUST | **PASS** |

---

## Risks

| Risk | Severity | Mitigation in this pass |
|------|----------|-------------------------|
| Triumph inline CTAs omitted — reference less conversion-complete than live v6 | Low | INFORMATIONAL role + CTA block exists separately; documented |
| Icon placeholders vs Triumph FA / ISBD PNG | Low | CSS placeholder units; image variant deferred |
| Horizontal timeline weak on very narrow viewports | Low | Vertical timeline fallback at ≤1023px |
| Curated library v0 index still shows 9 rows | Low | Wave REPORT uses RPC 11/32; curated-library sync deferred to R01.3.X |
| Golden slice doc not updated | Low | `index.html` updated; golden-implementation-slice-v1.md = Wave D |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **Curated library row** for `process` | Not added in A2 — operational v0 index may lag |
| **T2 extraction REPORT** in `operational-examples/` | Not published — T1 floor sufficient for RPC |
| **RU landing QA preset** run on neutral EN slice | Not executed — supplementary QA optional |
| **WF-R01.3.2 human steward** | Not fixed in repo |
| **VF_PROCESS_PHASE_CARDS** reference variant | Not implemented — single VF binding sufficient for T1 |

---

## Final Status

| Criterion | Met? |
|-----------|------|
| E1 Source discovery documented | **Yes** |
| E2 Vocabulary validation documented | **Yes** |
| E3 PROCESS partial (HTML + SCSS) | **Yes** |
| E4 BLOCK-CONTRACT / registry alignment | **Yes** |
| E5 Golden slice placement | **Yes** |
| E6 Build PASS + compliance | **Yes** |
| E7 RPC 10/32 → 11/32 | **Yes** |
| One block only / no new IDs | **Yes** |

**Wave A2: COMPLETE — STOP.**

---

*Report artifact: `reports/wf-r01-3-2-wave-a2-process-v1.md`*
