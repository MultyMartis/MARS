# REPORT — WF-R01.3.2 LANDING COMPLETION WAVE DESIGN

**Subprogram ID:** WF-R01.3.2 — LANDING Completion Wave  
**Program parent:** WF-R01.3 — Reference Expansion Program (**DESIGN**)  
**Grandparent:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-19  
**Mode:** wave design — **documentation only**; **no** partials, **no** registry changes, **no** new IDs, **no** implementation

**Authority consumed:**

| ID | Artifact | Status |
|----|----------|--------|
| Roadmap / index | [roadmap.md](../projects/mars-website-factory/roadmap.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Current |
| Coverage model | [wf-r01-3-1-coverage-model-charter-v1.md](../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md) | **ACCEPTED** |
| G0 baseline | [wf-r01-3-0-coverage-baseline-snapshot-v1.md](wf-r01-3-0-coverage-baseline-snapshot-v1.md) | Published |
| Vocabulary | [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) | **ACCEPTED** |
| Program design | [wf-r01-3-reference-expansion-program-design-v1.md](wf-r01-3-reference-expansion-program-design-v1.md) | **DESIGN** |
| WF-R01 parent | [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) | **CHARTERED** |
| Structural layer | [wf-r01-2-structural-blocks-charter-v1.md](../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md) | **ACCEPTED** (Gate 2 rows **not started**) |
| Research | [rv-01-production-vocabulary.md](../research/foundry/rv-01-production-vocabulary.md) · [rv-02-website-production-systems.md](../research/foundry/rv-02-website-production-systems.md) · [rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md) | Published |

**Evidence surfaces (repo fact, 2026-06-19):**

| Surface | Location |
|---------|----------|
| Reference partials | `workspaces/website-factory-reference-v1/src/partials/sections/` |
| Layout ad-hoc shell | `workspaces/website-factory-reference-v1/src/partials/layout/header.html`, `footer.html` |
| Golden slice | `src/pages/index.html` · [golden-implementation-slice-v1.md](../projects/mars-website-factory/golden-implementation-slice-v1.md) |
| LANDING matrix | [SITE-TYPE-BLOCK-MATRIX-v2.md](../workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md) § LANDING |
| Extraction discipline | [implementation-extraction-discipline-v1.md](../projects/mars-website-factory/implementation-extraction-discipline-v1.md) |
| Execution cases | Triumph `workspaces/triumph-manipulator-landing-v6/` · ISBD overview only · FP-0002 stress (QA boundary) |

**Honesty boundary:** This document **designs** the first execution-oriented wave of Reference Expansion. **Not** runtime, **not** wave execution authorization by itself (requires separate operator charter pass + ACCEPTED if program pattern holds), **not** proof that G1 is reached.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

WF-R01.3.2 — **первая execution-oriented волна** Reference Expansion Program. Цель: закрыть **LANDING composition truth gap** и достичь **Gate G1** (RPC **14/32**, ~44%) при сохранении honesty boundary «registry completeness ≠ buildability».

**Текущая позиция (G0):** RC **29/32**, RPC **9/32**, RSC **1/10**, SC **1/8 partial** (LANDING HITL pilot only), PC **0/1** (LANDING composition doc не опубликован).

**Суть волны:** довести LANDING reference set от «conversion path ~69%» до **production Template-Art** по [wf-r01-3-1-coverage-model-charter-v1.md](../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md) § Template-Art minimum sets — через **+5 partial-file equivalents** (консервативная математика G1) плюс **документарные** артефакты (Reference Composition, RSC stub-declaration).

**Ключевое архитектурное решение:** WF-R01.3.2 **владеет LANDING content gap** (W1: `BENEFITS`, `PROCESS`, `TESTIMONIALS` split) и **координирует** shell closure с **WF-R01.3.3** (W2: `HEADER_NAV`, `FOOTER`, `LEGAL_LINKS`). G1 **не достижим** только контентными partials без shell; FILTERS/SEARCH **вне scope** этой волны (→ R01.3.4 / G2).

**Explicit non-goals (this design pass):** создание partials, registry row edits, curated-library v2 implementation, enrollment BZPM workspace, WF-A03, новые `block_id`.

---

## Landing Inventory

### W1 — LANDING reference partial inventory

Inventory scope = **LANDING-relevant** `block_id` из [SITE-TYPE-BLOCK-MATRIX-v2.md](../workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md) § LANDING + Template-Art minimum shell из coverage charter.

#### Present — T1+ reference partials (9 files → 8 unique `block_id`)

| Partial file | v1 `block_id` | LANDING matrix status | Tier (curated) | Notes |
|--------------|---------------|----------------------|----------------|-------|
| `hero.html` | `HERO` | REQUIRED | battle-tested | ✓ |
| `social_proof.html` | `TRUST` | REQUIRED | experimental | **Collapses** TRUST + testimonial quotes — split target W1 |
| `cases.html` | `CASES` | OPTIONAL | validated | ✓ |
| `pricing.html` | `PRICING` | OPTIONAL | validated | ✓ |
| `lead_form.html` | `LEAD_FORM` | REQUIRED | battle-tested | ✓ |
| `cta_band.html` | `CTA` | REQUIRED | validated | ✓ |
| `sticky_cta.html` | `CTA` (module) | REQUIRED | validated | Sub-variant; no `data-block-id` |
| `faq.html` | `FAQ` | REQUIRED | validated | ✓ |
| `contact_block.html` | `CONTACTS` | REQUIRED | validated | ✓ |

**LANDING conversion path covered:** HERO → TRUST (partial) → CASES → PRICING → LEAD_FORM → CTA → FAQ → CONTACTS — **без** BENEFITS, PROCESS, distinct TESTIMONIALS, production shell.

#### Present — ad-hoc layout (not RPC numerator)

| File | Intended role | RPC? |
|------|---------------|------|
| `layout/header.html` | Global chrome stub | **No** — not `sections/` T1+ `HEADER_NAV` |
| `layout/footer.html` | Global footer stub | **No** — not promoted `FOOTER` partial |
| `layout/modal_callback.html` | Conversion utility | **No** — not LANDING `block_id` |

#### Missing — LANDING G1 block gaps

| `block_id` | Matrix status | Registry row | Reference partial | G1 priority |
|------------|---------------|--------------|-------------------|-------------|
| `BENEFITS` | REQUIRED | T0 (documented) | **Absent** | P0 |
| `PROCESS` | REQUIRED | T0 | **Absent** | P0 |
| `TESTIMONIALS` | OPTIONAL (Template-Art minimum) | T0 | **Absent** (collapsed in TRUST) | P0 — split hygiene |
| `FOOTER` | REQUIRED | T0 | **Absent** (layout stub only) | P0 — shell |
| `LEGAL_LINKS` | REQUIRED | T0 | **Absent** | P0 — shell |
| `HEADER_NAV` | Shell minimum (Template-Art) | **No row** (vocabulary only) | **Absent** | P0 — structural; **Gate 2 co-required** |
| `MAP` | OPTIONAL | T0 | **Absent** | **Deferred** — not in G1 RPC budget |

#### Explicitly out of LANDING wave scope

| Terms | Reason |
|-------|--------|
| `FILTERS`, `SEARCH` | Structural Tier A — **G2 / R01.3.4 W4**; requires WF-R01.2 Gate 2 + catalog corridor |
| `SERVICES`, `TEAM`, `ABOUT` | PROMO — **R01.3.2 W3 / G2** |
| Catalog / commerce blocks | CATALOG / ECOMMERCE waves |

#### TRUST / TESTIMONIALS disposition (reference hygiene, not registry change)

| Current state | Target state (W1) |
|---------------|-------------------|
| `social_proof.html` → `TRUST` only | Retain `TRUST` partial; **narrow** to logo/metric strip semantics |
| Testimonial quotes embedded in TRUST or absent | New `TESTIMONIALS` partial — curated quote cards |
| Curated library row `social_proof` | Coordinate with R01.6 hygiene — **no new IDs** |

**Inventory verdict:** LANDING has **9/12–14** Template-Art block classes at T1+ depending on counting (8 unique `block_id` + sticky module). **Five to six** net-new partial promotions required for honest G1.

---

## Delta To G1

### W2 — Confirmed delta vs baseline snapshot

Authority: [wf-r01-3-0-coverage-baseline-snapshot-v1.md](wf-r01-3-0-coverage-baseline-snapshot-v1.md) § Delta To Next Gate · [wf-r01-3-1-coverage-model-charter-v1.md](../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md) § Readiness Gates.

| Dimension | G0 (now) | G1 target | Delta |
|-----------|----------|-----------|-------|
| **RPC** | **9/32** (~28%) | **14/32** (~44%) | **+5** partial-file equivalents |
| **RC** | 29/32 | 29/32 minimum; **32/32** if structural rows added | **+3** registry rows (WF-R01.2 Gate 2) for honest HEADER_NAV/FILTERS/SEARCH vocabulary — **G1 minimum: HEADER_NAV row** |
| **RSC** | 1/10 global; 1/1 LANDING wave | LANDING scaffold **stub-declared** | Formal stub manifest for `index.html` |
| **SC** | 1/8 partial (LANDING HITL) | LANDING **production** Template-Art | Full LANDING checklist pass |
| **PC** | 0/1 LANDING | 1/1 — `LANDING_PAGE` Reference Composition **published** | **+1** composition doc |

### RPC partials required for G1 (minimum set)

| # | `block_id` | Subprogram owner | Baseline confirms |
|---|------------|------------------|-------------------|
| 1 | `BENEFITS` | R01.3.2 W1 | ✓ snapshot § Delta |
| 2 | `PROCESS` | R01.3.2 W1 | ✓ |
| 3 | `TESTIMONIALS` | R01.3.2 W1 (split) | ✓ |
| 4 | `HEADER_NAV` | R01.3.3 W2 | ✓ — **+ WF-R01.2 Gate 2 row** |
| 5 | `FOOTER` **and/or** `LEGAL_LINKS` | R01.3.3 W2 | ✓ — operator sequences within +5 budget |

**Gate math note:** W1 (+3) + W2 shell (+2–3) ≈ **15** new; G1 target **14** is **conservative** — acceptable per coverage charter. Counting policy: **9 partial files** baseline; CTA sticky **does not** add second RPC slot.

### Non-RPC G1 deliverables (mandatory for SC / PC)

| Deliverable | Metric | Owner |
|-------------|--------|-------|
| `LANDING_PAGE` Reference Composition (markdown) | **PC** 0→1 | R01.3.2 |
| Golden slice stack update + pointer doc | SC evidence | R01.3.2 |
| RSC stub-declaration record for `index.html` | RSC honesty | R01.3.2 |
| WF-R01.2 Gate 2: `HEADER_NAV` registry row + BLOCK-CONTRACT | **RC** structural | **Parallel track** — blocks honest HEADER_NAV claims |
| TRUST/TESTIMONIALS disposition note | R01.6 coordination | W1 exit |

### Baseline reconciliation

| Check | Verdict |
|-------|---------|
| Snapshot deficit **5** partials | **Confirmed** — matches program design W1+W2 |
| Strict `block_id` **8/32** vs file **9/32** | Wave REPORT must declare counting method |
| `MAP` optional | **Excluded** from G1 minimum — does not block SC production pass |
| FILTERS/SEARCH in denominator 32 but not G1 numerator | **Expected** — vocabulary in scope; partials deferred to G2 |

---

## Priority Waves

### W3 — Internal execution waves (recommended order)

Program design maps W1→R01.3.2 and W2→R01.3.3. WF-R01.3.2 **charter execution** bundles both tracks under **G1 exit** with internal sub-waves:

```text
G0 (9/32)
    │
    ├── Wave A — LANDING content (R01.3.2 core)     [parallel]
    │       BENEFITS → PROCESS → TESTIMONIALS split
    │
    ├── Wave B — Shell promotion (R01.3.3 coord.)   [parallel with A]
    │       FOOTER + LEGAL_LINKS (layout → sections/ T1+)
    │
    ├── Wave C — Structural shell (R01.3.3)         [after Gate 2 OR waiver doc]
    │       HEADER_NAV partial + registry row
    │
    └── Wave D — Documentation (R01.3.2)            [parallel throughout]
            LANDING_PAGE Reference Composition
            RSC stub manifest · golden slice pointer · five-dimension exit REPORT
```

#### Wave A — LANDING content (P0, no structural deps)

| Step | Block | Rationale |
|------|-------|-----------|
| A1 | `BENEFITS` | REQUIRED in LANDING matrix; closes value-prop gap before PROCESS |
| A2 | `PROCESS` | REQUIRED; depends on narrative flow after BENEFITS (composition, not code) |
| A3 | `TESTIMONIALS` + TRUST narrow | Split hygiene; unblocks honest TRUST vs quote variant |

**Parallelism:** A1–A3 may run **one block per execution pass** (pixel-perfect / extraction discipline); A1 and B1 may run **concurrently** in separate operator sessions.

#### Wave B — Shell content blocks (P0, partial Gate 2 independence)

| Step | Block | Rationale |
|------|-------|-----------|
| B1 | `FOOTER` | Promote `layout/footer.html` → `sections/footer.html` T1+; matrix REQUIRED |
| B2 | `LEGAL_LINKS` | Slot inside FOOTER or standalone partial per BLOCK-DEPENDENCY-RULES |

**Dependency:** `LEGAL_LINKS` **requires** Legal Pack v1 reference in production claims — reference partial may use placeholder URLs with honesty flag.

#### Wave C — HEADER_NAV (P0 for G1, **hard** Gate 2 dependency)

| Step | Block | Rationale |
|------|-------|-----------|
| C1 | WF-R01.2 Gate 2 row | Registry + BLOCK-CONTRACT for `HEADER_NAV` |
| C2 | `HEADER_NAV` partial | Minimal LANDING nav — not BZPM megamenu depth |

**Sequencing:** C1 **before** C2 for honest RC/RPC reporting. **Exception:** FOOTER/LEGAL_LINKS **do not** require Gate 2.

#### Wave D — Documentation (continuous)

| Artifact | Gate evidence |
|----------|---------------|
| Reference Composition `LANDING_PAGE` | PC numerator |
| Updated [golden-implementation-slice-v1.md](../projects/mars-website-factory/golden-implementation-slice-v1.md) | Operator onboarding |
| Wave extraction REPORTs (per block) | T2 promotion path |
| G1 five-dimension snapshot REPORT | RC/RPC/RSC/SC/PC exit |

### Why this order (REG-VOC-04 alignment)

RV-01 / Vocabulary Canon: **content blocks before marketing-heavy expansion** — within LANDING, **BENEFITS/PROCESS** precede optional **MAP**. Structural **HEADER_NAV** is shell — sequenced **after** Gate 2, parallel to content where rows exist. **FILTERS/SEARCH** intentionally **last** (G2) — catalog discovery, not LANDING URL policy.

### Alternative rejected: «shell first»

Promoting HEADER_NAV before BENEFITS **blocks** on Gate 2 **and** delays LANDING content RPC gains. **Rejected** — Wave A runs first for immediate RPC growth without registry dependency.

---

## Structural Dependencies

### W4 — HEADER_NAV, FILTERS, SEARCH dependency analysis

| Term | Tier | WF-R01.2 Gate 2 row | G1 need | WF-R01.3.2 scope | Parallel with W1? |
|------|------|----------------------|---------|------------------|-------------------|
| `HEADER_NAV` | A | **Required** for honest RPC | **Yes** — Template-Art shell minimum | Wave C (coord. R01.3.3) | **Partial** — row creation parallel; partial **after** row |
| `FOOTER` | Content shell (existing `block_id`) | No | **Yes** | Wave B | **Yes** — fully parallel |
| `LEGAL_LINKS` | Content shell | No | **Yes** | Wave B | **Yes** |
| `FILTERS` | A | **Required** | **No** (G2) | **Out of scope** → R01.3.4 W4 | **No** — requires catalog scaffold |
| `SEARCH` | A | **Required** | **No** (G2) | **Out of scope** → R01.3.4 W4 | **No** |

### Dependency diagram

```text
WF-R01.1 B3 (v1 block_id STOP) ────────► all partials
WF-R01.2 Gate 2 ───────────────────────► HEADER_NAV honest RPC
        │                                      │
        │ (also required later)                ▼
        └──────────────────────────────► FILTERS, SEARCH (G2 — R01.3.4)
        
Wave A (BENEFITS, PROCESS, TESTIMONIALS) ──► no Gate 2 dependency
Wave B (FOOTER, LEGAL_LINKS) ──────────────► no Gate 2 dependency
Wave C (HEADER_NAV) ───────────────────────► HARD dependency on Gate 2
```

### WF-R01.2 Gate 2 co-execution policy

| Policy | Statement |
|--------|-----------|
| **Parallel allowed** | Gate 2 registry row authoring **in parallel** with Wave A/B partial work |
| **Hard stop** | HEADER_NAV partial **must not** claim T1+ RPC until row exists (WF-R01.1 B3) |
| **G1 without Gate 2** | **Not honest** if HEADER_NAV counted in RPC/SC — waiver requires explicit REPORT |
| **FILTERS/SEARCH rows** | May be authored in Gate 2 pass **early** but partials **deferred** to R01.3.4 |

### Layout-component boundary (out of wave)

| Item | Disposition |
|------|-------------|
| `BREADCRUMBS`, `PAGINATION` | WF-R01.2 layout-component policy — **not** G1 LANDING |
| `modal_callback` | Stays layout utility — not promoted |

---

## Execution Case Feed

### W5 — Triumph, ISBD, FP-0002 routing for LANDING layer

#### Triumph (`triumph-manipulator-landing-v6/`) — **Primary driver**

| Source surface | Target `block_id` / pattern | Wave | Extraction notes |
|----------------|----------------------------|------|------------------|
| `screen-03-trust-reviews.html` — trust-cards grid | `BENEFITS` **or** TRUST narrow | A1 / A3 | Split: card grid → BENEFITS; review panel → TESTIMONIALS |
| Same file — `review-panel`, `review-list` | `TESTIMONIALS` | A3 | Primary quote extraction source |
| `dark-proof-strip.html` | `TRUST` metrics strip | TRUST refactor | Keep in TRUST after split — not BENEFITS |
| `v5-ppc/*/screen-02b-order-steps.html` — `order-steps--process` | `PROCESS` | A2 | `scroll_process_timeline` = **Commercial Pattern** (F4) inside PROCESS block — **not** new `block_id` |
| `landing-footer.html` | `FOOTER` + `LEGAL_LINKS` | B1–B2 | Shell promotion candidate |
| Already extracted: faq, pricing, cases, lead_form, hero patterns | — | — | **Do not re-extract** |
| RU landing QA preset | QA gate for Wave A/B | D | [ru-landing-qa-preset-v1.md](../projects/mars-website-factory/ru-landing-qa-preset-v1.md) |
| Full v6 multi-page PPC tree | PROMO W3 only | **Out of scope** | Anti-pattern: auto-canonicalize v6 |

**Triumph boundary:** Client workspace authority parallel to LOC — extract **structure**, neutralize copy/assets per [implementation-extraction-discipline-v1.md](../projects/mars-website-factory/implementation-extraction-discipline-v1.md).

#### ISBD (`isbd-care-landing/`) — **Secondary / validation**

| Contribution | LANDING wave use | Notes |
|--------------|------------------|-------|
| Care-vertical LANDING composition | Reference Composition **peer review** | Lighter Factory binding |
| Semantic freeze + adoption pattern | Wave D validation template | [reference-case-overview-v1.md](../projects/mars-website-factory/reference-cases/isbd-care-landing/reference-case-overview-v1.md) |
| `FEATURES`, `REVIEWS` | **Not W1** — R01.3.5 W7 | Program design routing |
| Live workspace `src/` in monorepo | **SAFE UNKNOWN** — overview doc only at design T0 | Extraction **blocked** until workspace verified on disk |

**ISBD role in 3.2:** adoption/freeze discipline for **pilot validation after G1** — **not** primary extraction source for BENEFITS/PROCESS.

#### FP-0002 (`fp-0002-shpigovsky-frontend/`) — **Negative evidence only**

| Use | Forbidden |
|-----|-----------|
| VL3 false-green patterns for reference QA adoption | **Must not** inflate RPC |
| Asset identity collision lessons | **Must not** promote PIXEL sections to reference without scope change |
| Operator visual approval law reinforcement | **Must not** block Wave A on pixel fidelity |

**FP-0002 role:** parallel **WF-A02 adoption** track — informs extraction QA checklist, **not** block sourcing.

#### BZPM (doc-first, not execution case workspace)

HEADER_NAV depth, filters, megamenu — **vocabulary mining for R01.3.4** only. **Excluded** from LANDING wave extraction to avoid OpenCart → Factory false equivalence.

### Extraction feed workflow (binding)

```text
Case evidence → classify block_id → WF-R01.1 v1 binding check
    → strip/neutralize → port to reference-v1 → npm run build PASS
    → extraction REPORT → optional T2 curated → WF-R01.8 lesson index
```

---

## Reference Standards

### W6 — Definition of «complete» Landing Reference Partial

Minimum **T1+** package for each new partial in this wave:

| Layer | Requirement | Location / contract |
|-------|-------------|---------------------|
| **HTML** | One `partials/sections/{snake_case}.html`; root `data-section` + `data-block-id` matching v1 binding | [implementation-extraction-discipline-v1.md](../projects/mars-website-factory/implementation-extraction-discipline-v1.md) |
| **SCSS** | Scoped `scss/sections/_{name}.scss`; imported in `style.scss`; token hygiene | [block-quality-tiers-v1.md](../projects/mars-website-factory/block-quality-tiers-v1.md) |
| **JS** | **Optional** — only if interaction required; `data-module` + lifecycle destroy; **no** inline scripts | Progressive enhancement rules in AGENTS.md |
| **Registry contract** | BLOCK-CONTRACT semantics honored; SITE-TYPE-BLOCK-MATRIX LANDING stance respected | BLOCK-REGISTRY-v1 row (T0 minimum; HEADER_NAV needs Gate 2 row) |
| **Build evidence** | `npm run build` **PASS** in reference workspace | Mandatory per wave exit |
| **Documentation** | Extraction REPORT in `operational-examples/` for T2 path; wave REPORT cites block | Wave 5–6 discipline |
| **Composition binding** | Row in `LANDING_PAGE` Reference Composition doc | PC metric |
| **QA** | [operational-qa-entry-v1.md](../projects/mars-website-factory/operational-qa-entry-v1.md) compact PASS; RU landings → ru-landing-qa-preset | T1 floor |
| **Survivability** | `data-section` replace-safe or documented static-only | section-survivability-implementation-v1 |

#### Tier targets for this wave

| Block | Entry tier | Promotion path |
|-------|------------|----------------|
| BENEFITS, PROCESS, TESTIMONIALS | **validated** (T1+) | T2 after extraction REPORT + build |
| FOOTER, LEGAL_LINKS | **validated** | Layout promotion — may start **experimental** until Legal Pack linkage documented |
| HEADER_NAV | **validated** minimum | **battle-tested** deferred — minimal nav only |

#### Filename / binding discipline (WF-R01.1)

| Rule | Example |
|------|---------|
| v1 `block_id` UPPER_SNAKE in registry | `BENEFITS` |
| Partial file snake_case | `benefits.html` |
| `data-block-id` snake_case hook | `data-block-id="benefits"` |
| Curated library v0 names | Operational view only — **not** coverage truth |

#### Reference Composition doc (PC — wave-level deliverable)

Separate from PAGE-BLOCK-MAPPING registry matrix:

| Field | Content |
|-------|---------|
| `page_type` | `LANDING_PAGE` |
| Ordered stack | REQUIRED/OPTIONAL blocks with stub vs T1+ honesty |
| Stance | Derived from LANDING-BLUEPRINT-v1 + matrix |
| Golden slice crosswalk | Maps to `index.html` includes |

---

## Success Metrics

### W7 — RPC, SC, G1 completion criteria

#### Primary numeric targets

| Metric | G0 | G1 exit | Measurement |
|--------|-----|---------|-------------|
| **RPC** | 9/32 (~28%) | **≥ 14/32** (~44%) | Partial files in `sections/`; denominator **32** declared |
| **RC** | 29/32 | ≥29/32; **32/32** if Gate 2 complete | Core rows + HEADER_NAV row minimum for honest shell |
| **RSC** | 1/10 | 1/10 global unchanged; **LANDING 1/1** with stub manifest | `index.html` honesty record |
| **SC** | 1/8 partial | **LANDING full pass** (1/8 → production Template-Art for LANDING) | Template-Art minimum checklist |
| **PC** | 0/1 | **1/1** LANDING composition published | Reference Composition doc exists |

#### G1 completion criteria (all required)

| # | Criterion | Evidence type |
|---|-----------|---------------|
| G1-1 | RPC **≥ 14/32** | Manual count + build PASS |
| G1-2 | LANDING SC checklist **pass** — all REQUIRED blocks T1+ except declared OPTIONAL (`MAP`) | SC matrix vs partial inventory |
| G1-3 | `LANDING_PAGE` Reference Composition **published** | PC numerator |
| G1-4 | Golden slice includes new blocks in documented order | `index.html` + golden doc |
| G1-5 | TRUST/TESTIMONIALS split **documented** | Disposition note / R01.6 coordination |
| G1-6 | HEADER_NAV: registry row **or** explicit waiver with SC cap | Gate 2 artifact or HITL waiver REPORT |
| G1-7 | Five-dimension exit REPORT published | RC, RPC, RSC, SC, PC together |
| G1-8 | No **new** `block_id` minted | Charter boundary |

#### SC — LANDING checklist mapping (G1 pass)

| Requirement | G0 | G1 target |
|-------------|-----|-----------|
| HERO, BENEFITS, PROCESS | Partial | **All T1+** |
| TRUST + TESTIMONIALS | TRUST only | **Both** distinct or documented OPTIONAL waiver for TESTIMONIALS |
| FAQ, CASES, PRICING, CTA, LEAD_FORM, CONTACTS | T1+ | T1+ (unchanged) |
| FOOTER, LEGAL_LINKS, HEADER_NAV minimal | Missing / ad-hoc | **T1+** |
| LANDING_PAGE composition | Missing | **Published** |
| MAP | Missing | OPTIONAL — **may remain absent** |

#### Unlock at G1

| Unlock | Statement |
|--------|-----------|
| LANDING Template-Art | **Production** (not HITL pilot only) |
| Global shell honesty | FOOTER + LEGAL_LINKS + minimal HEADER_NAV |
| PROMO/CATALOG | **Still blocked** until G2 |
| WF-A03 | **Not** unlocked — G2 recommended precondition |

---

## Future Wave Impact

### W8 — Handoff to R01.3.3, R01.3.4, R01.3.5

```text
WF-R01.3.2 (this wave) ──► G1
        │
        ├─► WF-R01.3.3 Structural & Shell References
        │       Residual: HEADER_NAV depth, global shell scaffold policy
        │       BREADCRUMBS/PAGINATION layout-component decision
        │       Overlap: W2 FOOTER/LEGAL_LINKS may complete IN 3.2 — 3.3 becomes policy + depth
        │
        ├─► WF-R01.3.4 Catalog & Vertical Profile References (G2)
        │       FILTERS, SEARCH partials (Gate 2 rows)
        │       W5 catalog grids; PLP/PDP scaffolds
        │       BZPM vocabulary feed; MANUFACTURER/AUTO profiles
        │       **Depends on** HEADER_NAV T1+ from 3.2/3.3
        │
        └─► WF-R01.3.5 Corporate & Commerce Slices (G3–G4)
                W6 commerce chain; W7 FEATURES, REVIEWS, PARTNERS…
                ISBD FEATURES/REVIEWS extraction
                ECOMMERCE staging only until Legal E1–E4
```

#### Artifacts consumed by downstream waves

| Artifact from 3.2 | Consumer |
|-------------------|----------|
| LANDING Reference Composition | PROMO scaffolds inherit LANDING stack baseline |
| BENEFITS / PROCESS partials | PROMO `SERVICE_PAGE` scaffold (W3) |
| HEADER_NAV minimal partial | CATALOG W4 — nav depth extension, not greenfield |
| Extraction REPORT template | R01.3.4 BZPM-mined structural patterns |
| G1 five-dimension REPORT | R01.3.X gate sign-off series |
| TRUST/TESTIMONIALS split precedent | R01.6 registry hygiene; REVIEWS vs TESTIMONIALS in W7 |

#### Program position after successful 3.2

| Gate | RPC | Next authorized design/execution |
|------|-----|-----------------------------------|
| G1 reached | 14/32 | R01.3.4 catalog wave design/execution; R01.3.3 residual shell policy |
| G1 not reached | <14/32 | **Stop** — no G2 catalog work claiming Template-Art |

---

## Risks

| Risk | Severity | Mitigation in 3.2 design |
|------|----------|--------------------------|
| False G1 from RC **29/32** alone | Critical | Five-dimension exit REPORT mandatory |
| HEADER_NAV partial before Gate 2 row | Critical | Wave C hard dependency; B3 STOP |
| TRUST/TESTIMONIALS split breaks curated library | Medium | Coordinate W1 exit with R01.6; v0 name labels |
| Triumph-specific selectors in reference | Medium | Extraction discipline anti-poisoning rules |
| Layout footer mistaken for FOOTER RPC | Medium | Explicit promotion path layout → sections/ |
| Gate 2 delayed blocks entire wave | Medium | Wave A+B parallel; G1 waiver doc if HEADER_NAV deferred |
| ISBD workspace absent — false extraction plan | Medium | SAFE UNKNOWN; Triumph primary |
| FP-0002 sections promoted to reference | Medium | Explicit exclusion in execution feed |
| TEMPLATE_ART multi-type before G2 | Critical | Interim LANDING-only policy unchanged |
| Single-metric «+5 partials» without SC/PC | Medium | G1-1..G1-8 all required |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **FOUNDRY** as named product/path | **Not found** |
| **WF-R01.3.2 human steward** | **Not fixed** |
| **Whether 3.2 requires separate ACCEPTED charter pass** | Assumed **yes** per R01.1/R01.2 pattern — **not explicitly confirmed** for R01.3 |
| **ISBD workspace `src/` presence in monorepo** | Overview registered; tree **not verified** at design T0 |
| **Triumph BENEFITS-dedicated section** | No file named benefits — split from trust-cards **operator judgment** at extraction |
| **FOOTER + LEGAL_LINKS: one partial vs two** | BLOCK-DEPENDENCY allows slot — affects +5 counting |
| **Strict vs file RPC for gate sign-off** | Charter prefers **9/32** file count — wave must declare |
| **Curated library v2 timeline** | Spec deferred R01.3.X |
| **WF-R01.7** vs coverage-derived Template-Art matrix | R01.7 **pending** |
| **npm build in all operator environments** | G0 verified locally; others **UNKNOWN** |

---

## Recommended Next Step

1. **Operator review** of this design — confirm Wave A/B/C/D sequencing and G1 criteria G1-1..G1-8.
2. **Parallel unblock:** WF-R01.2 **Gate 2** execution pass for `HEADER_NAV` registry row (minimum); optionally pre-author `FILTERS`/`SEARCH` rows without partials.
3. **Charter pass WF-R01.3.2** — move subprogram from **DESIGN** to **ACCEPTED** (if program pattern applies) — **authorizes** wave execution, not this design doc alone.
4. **First execution pass:** Wave A1 `BENEFITS` — one block only; extraction REPORT; build PASS; **STOP** for HITL.
5. **Publish** `LANDING_PAGE` Reference Composition (Wave D) — may start **before** code as PC planning artifact with stub honesty.
6. **Do not** start R01.3.4 catalog partials or claim G2 until G1 exit REPORT accepted.

**STOP** — no partials, no registry changes, no new IDs, no implementation in this pass.

---

*Design artifact: `reports/wf-r01-3-2-landing-completion-wave-design-v1.md`*
