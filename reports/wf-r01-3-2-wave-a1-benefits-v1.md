# REPORT — WF-R01.3.2 WAVE A1 BENEFITS

**Artifact ID:** WF-R01.3.2 Wave A1 — BENEFITS reference partial (v1)  
**Date:** 2026-06-19  
**Mode:** controlled reference-layer execution pass — **one block only**  
**Authority:** [wf-r01-3-2-landing-completion-charter-v1.md](../projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md) (**ACCEPTED**)

**Honesty boundary:** Human-operated extraction pass. **Not** runtime, **not** G1 reached, **not** new `block_id` minted.

---

## Executive Summary

Первый официальный Reference Partial для `BENEFITS` создан в `workspaces/website-factory-reference-v1/`. Структура извлечена из Triumph V2 (`advantages.html`); card grid приведён к паттерну **VF_BENEFITS_OUTCOME_GRID** и wf-* conventions reference workspace. `npm run build` — **PASS**. RPC: **9/32 → 10/32** (partial-file count, denominator 32).

Wave A1 scope **закрыт**. Следующий pass: Wave A2 `PROCESS` only.

---

## Source Selection

### Candidates evaluated

| Source | Location | Verdict |
|--------|----------|---------|
| **Triumph V2** | `workspaces/triumph-manipulator-landing-v2/src/partials/sections/advantages.html` | **Selected (primary)** — standalone 3-column outcome grid; maps to `BENEFITS` / VF_BENEFITS_OUTCOME_GRID |
| **Triumph V6** | `hero-proof` inside `screen-01-hero.html` | **Rejected** — hero-adjacent strip; violates standalone content-block placement (hero ≠ benefits per Vocabulary Canon glossary) |
| **Triumph V2 live index** | `problem-solution-matrix`, `segments-applications-grid` | **Rejected** — commercial/composition patterns (F4-adjacent); not registry-pure `BENEFITS` |
| **ISBD** | `workspaces/isbd-care-landing/src/partials/sections/benefits.html` | **Peer validation only** — explicit `benefits` naming confirms block semantics; client raster assets and `isbd-*` scope not ported |
| **Reference assets** | `cases.html`, `faq.html`, design VF_BENEFITS_OUTCOME_GRID | **Applied** — wf-section shell, header eyebrow, token hygiene |

### Rationale (binding for this pass)

Charter assigns Triumph as **primary extraction driver**. Dedicated Triumph BENEFITS partial **не найден** on v6 production stack (SAFE UNKNOWN acknowledged in charter). Operator judgment: **V2 `advantages.html`** — closest TEMPLATE_ART-aligned standalone grid without hero coupling. ISBD confirms naming and card semantics but **does not** drive extraction per charter routing (secondary adoption case).

---

## Partial Created

| Layer | Path | Notes |
|-------|------|-------|
| **HTML** | `src/partials/sections/benefits.html` | `data-section` + `data-block-id="benefits"`; 3 outcome cards; neutral EN copy |
| **SCSS** | `src/scss/sections/_benefits.scss` | Scoped under `.wf-section--benefits`; foundation tokens only |
| **JS** | — | **Not required** — static informational grid; progressive enhancement safe without JS |
| **Import** | `src/scss/main.scss` | `@use 'sections/benefits'` after hero |
| **Golden slice** | `src/pages/index.html` | Inserted **after HERO**, before social_proof — aligns LANDING stack |

**Extraction discipline applied:** client brand stripped; no Font Awesome; no Triumph/ISBD images; no inline scripts; no project-specific BEM roots.

---

## Contract Alignment

### BLOCK-CONTRACT-v1 (`BENEFITS`)

| Field | Registry value | Partial alignment |
|-------|----------------|-------------------|
| `block_id` | `BENEFITS` | Filename `benefits.html`; hook `data-block-id="benefits"` |
| `block_name` | Benefits / value props | Section eyebrow + h2 articulate value |
| `block_category` | CONTENT | Content band below hero |
| `purpose` | Value propositions, outcomes, differentiators | Three outcome cards with title + body |
| `conversion_role` | INFORMATIONAL | No primary CTA in block |
| `allowed_site_types` | LANDING, PROMO, CORPORATE | Neutral reference — no site-type leakage |
| `required_or_optional` | Required (LANDING) | Placed in golden slice LANDING stack |

### CC_BLOCK_BENEFITS (content contract)

| Signal | Status |
|--------|--------|
| `benefit` (required) | **Satisfied** — three outcome statements |
| `price`, `payment`, `legal_disclosure`, `consent` (forbidden) | **Absent** |

### Registry doc sync (no new IDs)

- [BLOCK-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) — reference partial pointer updated  
- [CORE-BLOCK-LIBRARY-v1.md](../workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md) — `benefits.html` row added  
- [BLOCK-GAPS-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md) — gap closed for BENEFITS

---

## Coverage Impact

**Counting method:** partial-file equivalents; denominator **32** (29 Core + 3 structural Tier A in program scope).

| Dimension | Before (G0) | After Wave A1 | Delta |
|-----------|-------------|---------------|-------|
| **RPC** | **9/32** (~28.1%) | **10/32** (~31.3%) | **+1** (`benefits.html`) |
| **RC** | 32/32* | 32/32 | unchanged |
| **RSC** | 1/10 global · 1/1 LANDING | unchanged | golden slice stack extended; stub manifest still pending |
| **SC** | LANDING partial | LANDING partial — BENEFITS checklist item **closed** | incremental |
| **PC** | 0/1 LANDING | 0/1 | Reference Composition doc not in A1 scope |

\*Post–WF-R01.2 Gate 2 baseline per charter T0; baseline snapshot used 29/32 RC — operator should cite latest Gate 2 REPORT for RC truth.

**Strict unique `block_id` RPC:** **9/32 → 10/32** (was 8/32 strict pre-A1 if CTA double-file excluded from unique count; now **9 unique** + 1 CTA variant file = 10 files).

**G1 progress:** 10/32 toward target 14/32 — **4 partial-file equivalents remaining** for G1 minimum set.

---

## Validation

| Check | Result |
|-------|--------|
| `npm run build` (reference workspace) | **PASS** (2026-06-19) |
| Vocabulary Canon F3 content block | **PASS** — BENEFITS as content block; not structural; not pattern-as-block |
| hero ≠ benefits boundary | **PASS** — standalone section, not hero child |
| BENEFITS ≠ FEATURES | **PASS** — outcome copy, not spec/capability grid |
| WF-R01.1 v1 `block_id` on partial | **PASS** |
| No new IDs | **PASS** |
| JS optional rule | **PASS** — no JS added |

---

## Risks

| Risk | Severity | Mitigation in this pass |
|------|----------|-------------------------|
| Triumph v6 lacks dedicated BENEFITS — reference diverges from live Triumph stack | Medium | Documented source = V2 `advantages`; v6 hero-proof explicitly rejected |
| ISBD card-with-image variant not represented | Low | VF_BENEFITS_OUTCOME_GRID allows icon/visual unit; CSS placeholder used — image variant deferred |
| Curated library v0 index still shows 9 rows | Low | Wave REPORT uses RPC 10/32; curated-library sync deferred to R01.3.X hygiene |
| Golden slice doc not updated | Low | `index.html` updated; [golden-implementation-slice-v1.md](../projects/mars-website-factory/golden-implementation-slice-v1.md) update = Wave D / follow-on |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **Curated library row** for `benefits` | Not added in A1 — operational v0 index still 9 rows |
| **T2 extraction REPORT** in `operational-examples/` | Not published — T1 floor sufficient for RPC |
| **RU landing QA preset** run on neutral EN slice | Not executed — supplementary QA optional |
| **WF-R01.3.2 human steward** | Not fixed in repo |
| **RC numerator post–Gate 2** | Cite Gate 2 execution pass if RC claim differs from G0 snapshot |

---

## Final Status

| Criterion | Met? |
|-----------|------|
| E1 Source selection documented | **Yes** |
| E2 BENEFITS partial (HTML + SCSS) | **Yes** |
| E3 BLOCK-CONTRACT alignment | **Yes** |
| E4 Vocabulary Canon compliance | **Yes** |
| E5 Build PASS | **Yes** |
| E6 RPC 9/32 → 10/32 | **Yes** |
| One block only / no new IDs | **Yes** |

**Wave A1: COMPLETE — STOP.**

---

*Report artifact: `reports/wf-r01-3-2-wave-a1-benefits-v1.md`*
