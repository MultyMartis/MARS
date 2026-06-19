# WF-R01.3.2 — LANDING Completion Wave Charter v1

**Subprogram ID:** WF-R01.3.2 — LANDING Completion Wave  
**Program parent:** WF-R01.3 — Reference Expansion Program (design: [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md))  
**Grandparent:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-19  
**Charter pass:** [wf-r01-3-2-landing-completion-charter-pass-v1.md](../../reports/wf-r01-3-2-landing-completion-charter-pass-v1.md)  
**Design basis:** [wf-r01-3-2-landing-completion-wave-design-v1.md](../../reports/wf-r01-3-2-landing-completion-wave-design-v1.md)

**Honesty boundary:** WF-R01.3.2 — **documentation and wave execution charter** (human-operated). **Не** runtime, **не** orchestration engine, **не** автоматическое создание partials. **ACCEPTED** authorizes **controlled** reference-layer execution passes per wave discipline — **not** proof that G1 is reached.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Charter sign-off

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Acceptance state** | LANDING Completion Wave structure, G1 exit criteria, execution case routing, and wave A–D sequencing are **normative operator authority** for WF-R01.3.2 execution passes |
| **Authority state** | WF-R01.3.2 = **ACCEPTED** · WF-R01.3 program design = **DESIGN** (sibling tracks R01.3.3–R01.3.5 remain design until individually chartered) · WF-R01 program = **CHARTERED** |
| **T0** | **2026-06-19** — date of ACCEPTED publication |
| **Owner** | Website Factory operator governance (human-operated sign-off via charter pass; **named steward SAFE UNKNOWN**) |
| **Prior state** | DESIGN — [wf-r01-3-2-landing-completion-wave-design-v1.md](../../reports/wf-r01-3-2-landing-completion-wave-design-v1.md) |
| **Hard prerequisites** | WF-R01.3.1 **ACCEPTED** · WF-R01.1 **ACCEPTED** · WF-R01.2 **ACCEPTED** · WF-R01.2 Gate 2 **COMPLETE** (RC **32/32**; structural registry rows exist) · G0 baseline published |
| **Blocks** | WF-R01.3.4 catalog execution claiming G2; WF-A03; Template-Art multi-type production beyond LANDING |

**ACCEPTED means:** Operator may execute Wave A–D **one block per pass** under extraction discipline, build validation, and five-dimension REPORTing. **Does not** mean partials exist, G1 is reached, SC production pass for LANDING, or parent WF-R01.3 program is ACTIVE.

---

## Executive Summary

WF-R01.3.2 — **первая ACCEPTED execution-oriented волна** Reference Expansion Program. Цель: закрыть **LANDING composition truth gap** и достичь **Gate G1** — RPC **≥ 14/32** (~44%) — при сохранении inequality `RC ≥ RPC` и honesty boundary «registry completeness ≠ buildability».

**Текущая позиция (post–Gate 2, charter T0):**

| Dimension | Value | Notes |
|-----------|-------|-------|
| **RC** | **32/32** | WF-R01.2 Gate 2 complete — structural rows exist; **RPC unchanged** |
| **RPC** | **9/32** (~28%) | G0 baseline |
| **RSC** | **1/10** global; **1/1** LANDING wave | `index.html` — stub manifest **pending** |
| **SC** | **1/8** partial (LANDING HITL pilot) | Production Template-Art **blocked** until G1 |
| **PC** | **0/1** LANDING | Reference Composition **not published** |

**Суть волны:** **+5** partial-file equivalents minimum (консервативная G1 math) плюс документарные артефакты (Reference Composition, RSC stub-declaration, five-dimension exit REPORT).

**Архитектурное решение (binding):** WF-R01.3.2 **владеет LANDING content gap** (Wave A) и **координирует** shell closure с **WF-R01.3.3** (Waves B–C). `FILTERS` / `SEARCH` **вне scope** (→ R01.3.4 / G2). Post–Gate 2: `HEADER_NAV` **registry row satisfied** — Wave C requires **partial only** (WF-R01.1 B3).

---

## Wave Structure

Internal execution waves A–D bundle program-design W1 (R01.3.2) and W2 shell slice (R01.3.3 coordination) under **единый G1 exit**.

```text
G0 (RPC 9/32)
    │
    ├── Wave A — LANDING content (R01.3.2 core)     [parallel]
    │       BENEFITS → PROCESS → TESTIMONIALS split
    │
    ├── Wave B — Shell content blocks (R01.3.3 coord.) [parallel with A]
    │       FOOTER + LEGAL_LINKS (layout → sections/ T1+)
    │
    ├── Wave C — Structural shell (R01.3.3 coord.)   [row satisfied; partial pending]
    │       HEADER_NAV partial (minimal LANDING nav)
    │
    └── Wave D — Documentation (R01.3.2)            [parallel throughout]
            LANDING_PAGE Reference Composition
            RSC stub manifest · golden slice pointer · five-dimension exit REPORT
```

### Wave A — LANDING content (no structural registry dependency)

| Step | `block_id` | Rationale |
|------|------------|-----------|
| A1 | `BENEFITS` | REQUIRED in LANDING matrix; value-prop gap |
| A2 | `PROCESS` | REQUIRED; narrative flow after BENEFITS |
| A3 | `TESTIMONIALS` + TRUST narrow | Split hygiene from `social_proof.html` |

**Rule:** One block per execution pass; extraction REPORT + `npm run build` PASS per block.

### Wave B — Shell content blocks (no Gate 2 dependency)

| Step | `block_id` | Rationale |
|------|------------|-----------|
| B1 | `FOOTER` | Promote layout stub → `sections/` T1+ |
| B2 | `LEGAL_LINKS` | REQUIRED shell; slot or standalone per BLOCK-DEPENDENCY-RULES |

**Parallelism:** A and B may run in separate operator sessions.

### Wave C — HEADER_NAV (registry row **satisfied** post–Gate 2)

| Step | Deliverable | Status at charter T0 |
|------|-------------|----------------------|
| C1 | WF-R01.2 Gate 2 row + BLOCK-CONTRACT | ✅ **COMPLETE** per [wf-r01-2-gate-2-execution-pass-v1.md](../../reports/wf-r01-2-gate-2-execution-pass-v1.md) |
| C2 | `HEADER_NAV` T1+ partial | ⏳ **Pending** — minimal LANDING nav; not BZPM megamenu depth |

**Hard stop (WF-R01.1 B3):** Partial **must not** claim T1+ RPC without v1 registry row — row exists; partial work authorized.

### Wave D — Documentation (continuous)

| Artifact | Metric |
|----------|--------|
| `LANDING_PAGE` Reference Composition | **PC** |
| RSC stub-declaration for `index.html` | **RSC** honesty |
| Updated [golden-implementation-slice-v1.md](golden-implementation-slice-v1.md) | Operator onboarding |
| G1 five-dimension exit REPORT | RC/RPC/RSC/SC/PC together |

### Explicitly out of scope

| Terms | Routing |
|-------|---------|
| `FILTERS`, `SEARCH` | G2 / WF-R01.3.4 W4 |
| `SERVICES`, `TEAM`, `ABOUT` | G2 / WF-R01.3.2 W3 design track |
| `MAP` | OPTIONAL — may remain absent at G1 |
| Catalog / commerce blocks | R01.3.4 / R01.3.5 |

### Rejected alternative

«Shell first» (HEADER_NAV before content) — **rejected**: delays RPC gains; content waves have no registry dependency.

---

## G1 Coverage Targets

Per [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) § Readiness Gates.

| Dimension | G0 | G1 exit | Delta |
|-----------|-----|---------|-------|
| **RPC** | 9/32 (~28%) | **≥ 14/32** (~44%) | **+5** partial-file equivalents |
| **RC** | 32/32 | **32/32** maintained | No new registry IDs |
| **RSC** | 1/10 | LANDING **1/1** with stub manifest | Formal honesty record |
| **SC** | LANDING partial | LANDING **production** Template-Art | Full checklist pass |
| **PC** | 0/1 | **1/1** LANDING composition published | Reference Composition doc |

### RPC minimum set (+5)

| # | `block_id` | Wave | Owner |
|---|------------|------|-------|
| 1 | `BENEFITS` | A | R01.3.2 |
| 2 | `PROCESS` | A | R01.3.2 |
| 3 | `TESTIMONIALS` | A | R01.3.2 |
| 4 | `HEADER_NAV` | C | R01.3.3 coord. |
| 5 | `FOOTER` **and/or** `LEGAL_LINKS` | B | R01.3.3 coord. |

**Gate math:** W1 (+3) + shell (+2–3) ≈ 15; G1 target **14** is **conservative** — acceptable per coverage charter. Declare counting method (partial files vs strict unique `block_id`) in every wave REPORT.

### G1 completion criteria (all required)

| ID | Criterion | Evidence |
|----|-----------|----------|
| **G1-1** | RPC **≥ 14/32** | Manual count + build PASS |
| **G1-2** | LANDING SC checklist **pass** | Template-Art minimum set |
| **G1-3** | `LANDING_PAGE` Reference Composition **published** | PC numerator |
| **G1-4** | Golden slice includes new blocks in documented order | `index.html` + golden doc |
| **G1-5** | TRUST/TESTIMONIALS split **documented** | Disposition note / R01.6 coordination |
| **G1-6** | `HEADER_NAV` registry row present **and** T1+ partial **or** explicit SC cap waiver REPORT | Row ✅ post–Gate 2; partial required for honest G1 |
| **G1-7** | Five-dimension exit REPORT published | RC, RPC, RSC, SC, PC |
| **G1-8** | No **new** `block_id` minted | Charter boundary |

### Unlocks at G1

| Unlock | Statement |
|--------|-----------|
| LANDING Template-Art | **Production** (not HITL pilot only) |
| Global shell honesty | FOOTER + LEGAL_LINKS + minimal HEADER_NAV |
| PROMO / CATALOG | **Still blocked** until **G2** |
| WF-A03 | **Not** unlocked — G2 recommended precondition |

---

## Reference Partial Standard (T1+ minimum)

Per design W6 — binding for each new partial:

| Layer | Requirement |
|-------|-------------|
| **HTML** | `partials/sections/{snake_case}.html`; `data-section` + `data-block-id` per WF-R01.1 |
| **SCSS** | Scoped `scss/sections/_{name}.scss`; imported in `style.scss` |
| **JS** | Optional only; `data-module`; no inline scripts |
| **Registry** | BLOCK-CONTRACT semantics; LANDING matrix stance |
| **Build** | `npm run build` **PASS** in reference workspace |
| **QA** | [operational-qa-entry-v1.md](operational-qa-entry-v1.md); RU → [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) |
| **Extraction** | [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md) |

**Filename discipline:** v1 `block_id` UPPER_SNAKE; partial file snake_case; curated v0 names = operational view only.

---

## Execution Case Feed

| Case | Role in WF-R01.3.2 | RPC impact |
|------|-------------------|------------|
| **Triumph** | **Primary driver** — BENEFITS, PROCESS, TESTIMONIALS, FOOTER/LEGAL_LINKS extraction | **Increases RPC** |
| **ISBD** | **Secondary** — adoption/freeze discipline; composition peer review | **Does not** drive W1 extraction |
| **FP-0002** | **Negative evidence** — VL3 false-green, asset collision lessons | **Must NOT inflate RPC** |
| **BZPM** | **Excluded** from LANDING wave — vocabulary mining → R01.3.4 only | **No** OpenCart → Factory equivalence |

**Anti-patterns (binding):**

- Do not auto-canonicalize Triumph v6 full tree
- Do not promote FP-0002 PIXEL sections without scope change
- Do not mine BZPM for LANDING partials

---

## WF-R01.3.3 Coordination

Program design assigns W2 shell blocks to R01.3.3. This charter **bundles** FOOTER, LEGAL_LINKS, HEADER_NAV partial work under **G1 exit** with explicit coordination:

| Artifact | Primary owner | G1 role |
|----------|---------------|---------|
| FOOTER, LEGAL_LINKS partials | R01.3.3 (executed under 3.2 charter) | Shell RPC |
| HEADER_NAV partial | R01.3.3 (executed under 3.2 charter) | Structural RPC |
| BREADCRUMBS / PAGINATION policy | R01.3.3 residual | **Not** G1 |
| Global shell scaffold depth | R01.3.3 post-G1 | Follow-on charter |

WF-R01.3.3 remains **DESIGN** until its own charter pass — overlap **does not** block 3.2 execution for listed shell blocks.

---

## Future Wave Handoff

| Downstream | Consumes from 3.2 |
|------------|-------------------|
| **WF-R01.3.3** | Residual shell policy; nav depth extension |
| **WF-R01.3.4** | HEADER_NAV minimal baseline; FILTERS/SEARCH partials (rows exist) |
| **WF-R01.3.5** | LANDING composition baseline; BENEFITS/PROCESS for PROMO scaffolds |

**Stop rule:** G2 catalog work **must not** claim Template-Art until G1 exit REPORT accepted.

---

## Upstream authority alignment

| Charter | Relationship |
|---------|--------------|
| **Foundry Vocabulary Canon** | F3 content vs structural subtype; REG-VOC-04 — FILTERS/SEARCH deferred to G2; hero ≠ header_nav |
| **WF-R01** parent | R01.3.2 = P0 LANDING completion; M2 = RPC |
| **WF-R01.1** | B3 STOP; v1 `block_id` on all partials |
| **WF-R01.2** | Tier A in denominator 32; Gate 2 **COMPLETE** — Wave C partial authorized |
| **WF-R01.3.1** | G1 gate math; five-dimension REPORT contract |
| **WF-A01** | SC gates Template-Art; LANDING-only interim until G2 for other types |
| **WF-A03** | **DEFERRED**; G2 precondition unchanged |

---

## Non-goals (this charter)

- No automatic batch partial creation
- No registry row edits or new IDs
- No FILTERS / SEARCH partials
- No PROMO / CATALOG / ECOMMERCE scaffolds
- No curated-library v2 implementation
- No WF-A03 charter or implementation
- No OPERATIONAL-INDEX / roadmap edit (optional hygiene pass)

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| False G1 from RC **32/32** alone | Critical | Five-dimension exit REPORT; RPC **9/32** until partials exist |
| TRUST/TESTIMONIALS split breaks curated library | Medium | R01.6 coordination; v0 labels |
| Layout footer mistaken for FOOTER RPC | Medium | Explicit promotion path |
| Triumph-specific selectors in reference | Medium | Extraction discipline |
| TEMPLATE_ART multi-type before G2 | Critical | Interim LANDING-only policy |
| FP-0002 inflating RPC | Medium | Explicit exclusion |
| FOOTER + LEGAL_LINKS one vs two partials | Low | Declare in wave REPORT; +5 budget |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **FOUNDRY** as named product/path | **Not found** |
| **WF-R01.3.2 human steward** | **Not fixed** |
| **ISBD workspace `src/` in monorepo** | **Not verified** at charter T0 |
| **Triumph BENEFITS-dedicated section** | Split from trust-cards — operator judgment at extraction |
| **Strict vs file RPC for gate sign-off** | Declare in each REPORT |
| **WF-R01.7** vs coverage-derived Template-Art matrix | R01.7 **pending** |
| **OPERATIONAL-INDEX Gate 2 status line** | May lag execution pass — cite Gate 2 REPORT |
| **Curated library v2 timeline** | R01.3.X |

---

*Charter artifact: `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md`*
