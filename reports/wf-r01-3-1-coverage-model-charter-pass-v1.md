# REPORT — WF-R01.3.1 COVERAGE MODEL CHARTER PASS

**Artifact ID:** WF-R01.3.1 Coverage Model & Metrics — charter publication pass (v1)  
**Date:** 2026-06-19  
**Mode:** charter **publication** — **ACCEPTED** status; **no partials**, **no registry edits**, **no new IDs**, **no implementation**

**Inputs reviewed:**

| ID | Artifact |
|----|----------|
| Design | [wf-r01-3-reference-expansion-program-design-v1.md](wf-r01-3-reference-expansion-program-design-v1.md) |
| Audits | [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) · [foundry-system-wide-layer-audit-v1.md](foundry-system-wide-layer-audit-v1.md) · [foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md) |
| Authority | [roadmap.md](../projects/mars-website-factory/roadmap.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) |
| Vocabulary | [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) |
| WF-R01 | [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) · [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) · [wf-r01-2-structural-blocks-charter-v1.md](../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md) |

**Deliverable:** [wf-r01-3-1-coverage-model-charter-v1.md](../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md) — **ACCEPTED**

**Honesty boundary:** This pass **published documentation only**. **Not** runtime, **not** reference partials, **not** registry content, **not** wave execution.

---

## Executive Summary

WF-R01.3 Program Design (2026-06-19) определил Reference Layer, пятимерную coverage model, readiness gates G0–G4, Template-Art minimum sets, execution case routing, и WF-A03 sequencing. До этого pass отсутствовал **официальный ACCEPTED charter** для Coverage Model как normative operator authority.

**Результат pass:** опубликован `wf-r01-3-1-coverage-model-charter-v1.md` со статусом **ACCEPTED**. WF-R01.3.1 переведён **Design → ACCEPTED**. Charter фиксирует RC/RPC/RSC/SC/PC, denominator policy (29 vs 32), G0–G4 gates, Template-Art minimum reference sets, execution case roles, и G2→WF-A03 precondition — **zero partials**, **zero registry rows**, **zero new IDs**.

**Все шесть validation checks (C1–C6) PASS.**

```text
WF-R01.3.1  Design → ACCEPTED (this pass)     ✅
WF-R01.3    parent program remains DESIGN     ◆ (tracks R01.3.2+ not started)
Current gate position                       G0 (9/32 baseline)
```

---

## Coverage Validation

### C1 — Coverage Dimensions

**Verdict: PASS — model sufficient; definitions correct**

| Symbol | Definition validated | Numerator | Denominator | Baseline confirmed |
|--------|---------------------|-----------|-------------|------------------|
| **RC** | Registry row + BLOCK-CONTRACT completeness | Defined rows | Phase-dependent (29 → 32) | **29/29** Core; **0/3** structural rows |
| **RPC** | T1+ partial in reference workspace | Build-pass partials | In-scope `block_id` set | **9/32** (~28%) |
| **RSC** | Stub-declared scaffolds per `page_type` | Scaffold pages | PAGE-TYPE-REGISTRY required set | **~1/10+** (LANDING only) |
| **SC** | Site-type Template-Art minimum checklist | Types passing SC | Core 5 (+ profiles) | **1/5** LANDING partial |
| **PC** | Published Reference Composition docs | Documented stacks | Primary/secondary pages per wave | Matrices exist; compositions **not published** |

**Sufficiency rationale:**

- Five dimensions **separate** vocabulary truth (RC) from build evidence (RPC/RSC/SC) and planning (PC) — directly addresses audit bottleneck `Registry Coverage > Reference Coverage > Site Coverage`.
- **PC orthogonality** correctly allows 100% planning with low RPC — essential for wave sequencing.
- **T1+ floor** for RPC prevents T0 registry-only inflation.
- **No sixth dimension required** at v1 — blueprint-instance rolls into SC; curated library is RPC operational view only.

**Coverage inequality confirmed:**

```text
RC ≥ RPC ≥ RSC (per page) ≥ SC (per site type)
PC ⊥ RPC (orthogonal)
```

---

## Gate Validation

### C2 — Gate Validation

**Verdict: PASS — G0–G4 correct; transition math acceptable**

| Gate | RPC target | % | Math check | Transition unlock |
|------|------------|---|------------|-------------------|
| **G0** | 9/32 | ~28% | ✅ Baseline repo fact; 9/29 (~31%) valid if denominator explicit | LANDING HITL pilot |
| **G1** | 14/32 | ~44% | ✅ Conservative vs W1+W2 sum ~15 | LANDING + shell |
| **G2** | 20/32 | ~63% | ✅ May trail wave sum ~22 — stub policy acceptable | PROMO/CATALOG pilot; WF-A03 precondition |
| **G3** | 29/32 | ~91% | ✅ W6+W7 additions; no double-count | ECOMMERCE/CORPORATE pilot |
| **G4** | 32/32 | 100% | ✅ Co-dependent WF-R01.2 Gate 2 rows + partials | Full Core SC |

**Cross-program dependencies validated:**

- WF-R01.1 B3 STOP → partial v1 binding
- WF-R01.2 Gate 2 → G1 structural registry rows minimum
- WF-R01.7 → multi-type SC claims (pending ACCEPTED)
- WF-R01.4 → conversion surfaces in scaffolds (parallel)

**Parent program alignment:** Gate targets match [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) M2 trajectory (9→14→20→29→32). Denominator **32** standardization resolves 9/29 vs 9/32 confusion from audits.

---

## Authority Alignment

### C3 — Authority Validation

**Verdict: PASS**

| Authority | Alignment |
|-----------|-----------|
| **Vocabulary Canon** | F3 Structural subtype → denominator 32; REG-VOC-04 catalog ordering supports RSC/RPC dependency; no new family introduced |
| **WF-R01 parent** | M2 = RPC; charter normativizes measurement; CHARTERED program unchanged |
| **WF-R01.1** | v1 `block_id` required for RPC numerator; v0 curated names labeled operational view only; B3 pending does not block charter ACCEPTED |
| **WF-R01.2** | Tier A (HEADER_NAV, FILTERS, SEARCH) in denominator; Gate 2 registry rows co-required for G1 catalog honesty; breadcrumbs/pagination layout policy preserved |
| **WF-A03** | DEFERRED; G2 recommended precondition documented; auto-start forbidden per roadmap |

**No conflicts detected** between coverage charter and ACCEPTED upstream charters. Charter **does not amend** WF-A01, WF-A02, or Vocabulary Canon — **consumes** and **measures** their outcomes.

---

## Template-Art Impact

### C4 — Template-Art Impact

**Verdict: PASS — minimum coverage levels defined for Core 4**

| site_type_code | Minimum coverage gate | Key RPC/RSC/PC requirements |
|----------------|----------------------|----------------------------|
| **LANDING** | **G0** pilot / **G1** production | Conversion + trust + shell blocks; `LANDING_PAGE` composition |
| **PROMO** | **G2** pilot | Full LANDING set + SERVICES/TEAM/ABOUT/PROCESS; multi-page scaffolds |
| **CATALOG** | **G2** pilot (scaffold) / **G3** broader SC | Structural HEADER_NAV/FILTERS/SEARCH + catalog grids; PLP/PDP/SEARCH scaffolds |
| **CORPORATE** | **G3** pilot | HEADER_NAV + ABOUT/TEAM/PARTNERS/CERTIFICATES/SERVICES; route-group scaffolds |

**Interim policy confirmed:** «TEMPLATE_ART — LANDING scope only» mandatory until **G2** — consistent with parent program and capability audit LANDING-only effective reality.

**Readiness matrix (coverage-derived):**

| Type | G0 | G1 | G2 | G4 |
|------|----|----|----|----|
| LANDING | Allowed (HITL) | Allowed | Allowed | Allowed |
| PROMO | Blocked | Blocked | Pilot | Allowed |
| CATALOG | Blocked | Blocked | Pilot | Allowed (HITL) |
| CORPORATE | Blocked | Blocked | Blocked | Pilot |

**Note:** WF-R01.7 Template-Art matrix **pending ACCEPTED** — this charter matrix is **interim binding** until R01.7 supersedes.

---

## WF-A03 Relationship

### C6 — WF-A03 Dependency

**Verdict: PASS — G2 is correct recommended precondition**

| Criterion | Assessment |
|-----------|------------|
| G2 = RPC ≥ 63% + catalog scaffold | ✅ Prevents pixel-layer false-green on missing structural/catalog surfaces |
| R01.3.1 ACCEPTED = stable baselines | ✅ **Satisfied by this pass** |
| Structural T1+ partials at G2 | ✅ Aligned with VL3 domain assumptions (shell/catalog exist) |
| No auto-start on G2 | ✅ Roadmap DEFERRED + explicit waiver path only |
| FP-0002 parallel track unaffected | ✅ PIXEL_PERFECT greenfield may proceed with VL3 — separate from reference RPC |

**Sequencing confirmed:**

```text
WF-R01.3  G0 → G1 → G2 → G3/G4
                      │
                      ▼ recommended precondition (not auto-start)
              WF-A03 Pixel Factory charter pass
```

G2 **correctly** balances composition truth (reference exists) before visual automation (WF-A03). Starting WF-A03 below G2 without waiver risks **false-green at pixel layer** on catalog/manufacturer surfaces — capability audit and FP-0002 forensic support this ordering.

---

## Execution Case Usage

### C5 — Execution Case Usage

**Verdict: PASS — roles confirmed in coverage model**

| Case | Role in coverage model | RPC impact | Primary waves |
|------|------------------------|------------|---------------|
| **Triumph** | **Primary driver** — LANDING/PROMO extraction source | **Increases RPC** via W1/W3 partials | W1, W3; W2 nav minimal |
| **ISBD** | **Primary driver** — care vertical; adoption template | **Increases RPC** via W7 (FEATURES, REVIEWS) | W7 |
| **BZPM** | **Primary driver (doc-first)** — catalog/manufacturer vocabulary | **Doc → RPC** via W4–W5; OpenCart **≠** reference | W4–W5; R01.8 lessons |
| **FP-0002** | **Parallel discipline / negative evidence** | **Must NOT inflate RPC** | QA adoption; Template-Art vs PIXEL boundary |

**Anti-patterns preserved:**

- Triumph v6 full tree — selective extraction only
- BZPM live OpenCart — vocabulary mining HITL only
- FP-0002 sections — no promotion without PIXEL→TEMPLATE scope change

---

## Risks

| Risk | Severity | Charter mitigation |
|------|----------|-------------------|
| False «Factory-ready» from RC alone | Critical | Five-dimension REPORT contract |
| TEMPLATE_ART on CATALOG before G2 | Critical | G2 gate + LANDING-only interim |
| Denominator confusion (29 vs 32) | Medium | Explicit policy in charter |
| Stub scaffolds as SC pass | Medium | RSC stub-declaration rule |
| WF-A03 before G2 | Medium | Recommended precondition; waiver discouraged |
| FP-0002 inflating RPC | Medium | Explicit exclusion |
| WF-R01.7 pending vs coverage matrix | Low | Interim matrix until R01.7 ACCEPTED |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact RSC denominator (page_type count) | **Not counted** at charter T0 |
| WF-R01.3 program steward | **Not fixed** in repo |
| BREADCRUMBS/PAGINATION RPC counting at W4 | Layout-component policy — affects numerator when W4 executes |
| BZPM Factory workspace enrollment | **Pending** post–G2 |
| OCPilot SITE-001 Factory binding | **Not verified** |
| Curated library v2 timeline | R01.3.X — spec only |
| WF-R01.7 ACCEPTED matrix | **Pending** — interim matrix binding |
| OPERATIONAL-INDEX update for R01.3.1 | **Not done** in this pass — optional follow-up |

---

## Final Status

| Field | Value |
|-------|-------|
| **Charter path** | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` |
| **Charter status** | **ACCEPTED** |
| **Pass report** | `reports/wf-r01-3-1-coverage-model-charter-pass-v1.md` |
| **WF-R01.3.1 subprogram** | **Design → ACCEPTED** |
| **Registry rows created** | **0** |
| **New IDs created** | **0** |
| **Partials created** | **0** |
| **Implementation started** | **No** |
| **Validation C1–C6** | **All PASS** |
| **Current gate** | **G0** (9/32 baseline) |
| **Recommended next step** | Baseline metrics snapshot (RC/RPC/RSC/SC/PC) as first R01.3.X REPORT; parallel WF-R01.2 Gate 2 + R01.3.2 LANDING completion charter |

**STOP** — no implementation, no partial creation, no registry changes in this pass.

---

*Pass artifact: `reports/wf-r01-3-1-coverage-model-charter-pass-v1.md`*
