# REPORT — FOUNDRY VOCABULARY CANON CHARTER PASS

**Artifact ID:** Foundry Vocabulary Canon Charter — publication pass (v1)  
**Date:** 2026-06-19  
**Mode:** charter **publication** — **ACCEPTED** status; **no registry edits**, **no new IDs**, **no WF-Axx/WF-Rxx status changes**

**Inputs reviewed:**

| ID | Artifact |
|----|----------|
| Design | [foundry-vocabulary-canon-charter-design-v1.md](foundry-vocabulary-canon-charter-design-v1.md) |
| WF-R01.0 | [wf-r01-0-research-canon-integration-design-v1.md](wf-r01-0-research-canon-integration-design-v1.md) |
| RV-01 | [research/foundry/rv-01-production-vocabulary.md](../research/foundry/rv-01-production-vocabulary.md) |
| RV-02 | [research/foundry/rv-02-website-production-systems.md](../research/foundry/rv-02-website-production-systems.md) |
| RV-03 | [research/foundry/rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md) |
| WF-A01 | [website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) |
| WF-A02 | [website-factory-validation-architecture-charter-v1.md](../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md) |
| VL3 | [website-factory-vl3-domains-charter-v1.md](../projects/mars-website-factory/website-factory-vl3-domains-charter-v1.md) |
| WF-R01 | [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) |
| WF-R01.1 | [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) |

**Deliverable:** [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) — **ACCEPTED**

**Honesty boundary:** This pass **published documentation only**. **Not** runtime, **not** registry content, **not** subprogram execution.

---

## Executive Summary

Vocabulary Canon Design (2026-06-19) определил шесть registry-aligned families, constraint graph, authority model и REG-VOC-* constraints. До этого pass отсутствовал **официальный канонический слой** между Research (RV-01–03) и Registry.

**Результат pass:** опубликован `foundry-vocabulary-canon-charter-v1.md` со статусом **ACCEPTED**. Charter содержит **Tier A rules only** — **zero registry rows**, **zero new IDs**. Все пять validation checks (V1–V5) **PASS**.

**Цепочка authority теперь замкнута на doc-уровне:**

```text
Research (RV-01–03) → Vocabulary Canon Charter (ACCEPTED) → WF-R01.x → Registry
```

WF-R01.0 proposed exit criterion (Vocabulary Canon ACCEPTED + authority in OPERATIONAL-INDEX) — **satisfied** by this pass.

---

## Validation Results

### V1 — Authority Alignment

**Verdict: PASS — no conflicts detected**

| Authority | Relationship to Vocabulary Canon | Conflict? |
|-----------|-------------------------------|-----------|
| **WF-A01** Production Modes | Production Mode explicitly **excluded** from vocabulary families; orthogonal fidelity contract per AUTH-06 and design § Non-Goals NG-12 | **No** |
| **WF-A02** Validation Architecture | VL1 **consumes** registry vocabulary; validation layers do not define families; charter cites WF-A02 as upstream, does not amend | **No** |
| **VL3 Domains** | Composition/extract domains orthogonal to vocabulary families; RV-03 failure classes → Reference Library crosswalk only | **No** |
| **WF-R01** Registry Expansion | Vocabulary Canon is **upstream feed** to subprograms R01.1–R01.8; program charter unchanged; no status modification in this pass | **No** |
| **WF-R01.1** v0→v1 Binding | Harmonizes `site_type_id` → `site_type_code`; glossary alignment only; binding charter unchanged | **No** |

**Evidence:** WF-A01 §1 defines production mode as orthogonal to Forge/operational modes — same pattern applied to vocabulary. WF-R01 §4 authority chain unchanged. WF-R01.1 § Upstream authority explicitly states no amendment to WF-A01.

---

### V2 — Family Validation

**Verdict: PASS — six families sufficient; no mandatory family missing**

| Family | RV-01 coverage | Assessment |
|--------|----------------|------------|
| F1 Site Type | Site type level | **Required** — whole-project binding |
| F2 Page Type | Page type + absorbed listing/detail | **Required** — listing type not split (design rationale confirmed) |
| F3 Block | Section/block/component | **Required** — with structural/content subtypes |
| F4 Commercial Pattern | Commercial patterns | **Required** — distinct from blocks |
| F5 Trust Pattern | Trust patterns | **Required** — largest documented gap |
| F6 SEO Surface | SEO content surfaces | **Required** — page≠SERP separation |

**Excluded terms correctly relegated:** Production Mode (WF-A01), Blueprint (instance), Component/Token (implementation), Content Model (Tier C), SERP Tactic (glossary).

**No new families added** — design six-family set adopted unchanged.

---

### V3 — Boundary Validation

**Verdict: PASS — families non-overlapping with documented disambiguation**

| Boundary pair | Rule in charter | Overlap risk |
|---------------|-----------------|--------------|
| **Block vs Pattern** | REG-VOC-05/06; glossary pattern/block; F4/F5 vs F3 | **Mitigated** |
| **Commercial vs Trust** | Separate F4/F5 definitions; different purpose (narrative vs proof stack) | **Clear** |
| **SEO Surface vs Page Type** | F2 vs F6; default mapping overridable; not 1:1 mandatory | **Clear** |
| **Blueprint vs Vocabulary** | AUTH-04; blueprint instantiates, does not mint IDs | **Clear** |

**Constraint graph** adopted over strict linear model — prevents oversimplification of overlay relationships (patterns parallel to block composition).

---

### V4 — Registry Independence

**Verdict: PASS — charter creates no registry IDs**

| Check | Result |
|-------|--------|
| No normative `block_id` rows | ✅ Charter cites examples as vocabulary terms only; AUTH-02 |
| No normative `site_type_code` rows | ✅ Family definitions only |
| No normative `page_type` rows | ✅ Expansion vocabulary = glossary annex |
| No normative `pattern_id` rows | ✅ F4 binding unit documented; no new pattern rows |
| REG-VOC-* rules constrain **future** work | ✅ No authorization to execute |

**Charter remains above Registry** in authority flow per AUTH-01..06.

---

### V5 — Research Alignment

**Verdict: PASS — tiering matches WF-R01.0 design**

| Research | In Canon (Tier A) | Reference Only |
|----------|-------------------|----------------|
| **RV-01** | 6 families, minimal_canon policy, maturity attribute, structural/content split, trust/commercial separation, page≠SERP, FAQ obsolete tactic, page type expansion glossary | Vertical site types, rare blocks, provisional STATUS cells, full industry tables |
| **RV-02** | — (not vocabulary families) | Production stack (Tier B), canonical_asset glossary (Tier B), lifecycle (Tier B), content models (Tier C), cross-project libraries (Tier C) |
| **RV-03** | — (not vocabulary) | Failure classes (Tier B crosswalk), HITL model (Tier B); orchestration/visual diff (Tier C / WF-A03) |

---

## Charter Publication

| Field | Value |
|-------|-------|
| **Path** | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` |
| **Status** | **ACCEPTED** |
| **Version** | v1 |
| **Date** | 2026-06-19 |
| **Registry rows created** | **0** |
| **New IDs created** | **0** |

**Structure delivered:**

- Executive Summary
- Vocabulary Families (F1–F6 + subtypes + cross-cutting attributes)
- Family Boundaries (Block/Pattern, Commercial/Trust, SEO/Page Type, Blueprint/Vocabulary + glossary)
- Constraint Graph
- Authority Model (AUTH-01..06, tiering)
- Registry Rules (REG-VOC-01..12, subprogram alignment)
- Research Alignment (RV-01/02/03 disposition)
- Non-Goals (NG-01..15)
- Risks
- SAFE UNKNOWN

---

## Authority Impact

### Files modified

| File | Change |
|------|--------|
| [roadmap.md](../projects/mars-website-factory/roadmap.md) | Changelog entry — Vocabulary Canon ACCEPTED; cross-link only |
| [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Core Run row — Foundry Vocabulary Canon |

### Files created

| File | Role |
|------|------|
| [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) | ACCEPTED canonical charter |
| [foundry-vocabulary-canon-charter-pass-v1.md](foundry-vocabulary-canon-charter-pass-v1.md) | This pass report |

### Statuses NOT changed (per task constraint)

| Item | Status preserved |
|------|------------------|
| WF-A01 | Complete (Pass 01) |
| WF-A02 | Complete (Pass 01 + Pass 02) |
| WF-A03 | DEFERRED |
| WF-R01 | CHARTERED |
| WF-R01.1 | ACCEPTED |

### New programs

**None created.**

---

## Research Alignment

### Adopted into Vocabulary Canon (Tier A)

From **RV-01:**

- Registry family hierarchy (6 families)
- `minimal_canon` vs `expansion_backlog` promotion gate
- Maturity attribute (`standard` / `common` / `specialized` / `obsolete`)
- Structural-before-marketing priority
- Trust pattern and commercial pattern as first-class families
- `page_reality` ≠ `serp_reality`
- FAQ rich result obsolete (2026)
- Page type expansion glossary (not registry rows)

From **RV-02:** Nothing as vocabulary family (production stack → Reference Library Tier B).

From **RV-03:** Nothing as vocabulary family (pipeline terms → WF-A03 Tier C; failure classes → Reference Library Tier B).

### Remains Reference Only

| Source | Content | Tier |
|--------|---------|------|
| RV-01 | Full vertical site type lists, rare ecommerce blocks, provisional gap STATUS | C |
| RV-02 | 5-layer stack, lifecycle governance, content models, token engine | B/C |
| RV-03 | Orchestration loop, visual baseline, render diff, tool survey | C (WF-A03) |

---

## Risks

| Risk | Severity | Post-publication posture |
|------|----------|--------------------------|
| Research Canon ≠ Foundry Canon drift | High | AUTH rules + OPERATIONAL-INDEX discoverability |
| Level mixing persists in operational usage | High | REG-VOC constraints; WF-R01.x gates |
| Trust pattern remains implicit until R01.4 | High | F5 family defined; catalog deferred |
| v0/v1 dual vocabulary during cutover | Medium | WF-R01.1 binding; glossary legacy map |
| Operators skip charter, use RV tables directly | Medium | Tiering policy; research ≠ registry |
| Named vocabulary steward unset | Medium | SAFE UNKNOWN — human assignment pending |

---

## SAFE UNKNOWN

| Unknown | What would verify |
|---------|-------------------|
| Named **vocabulary steward** | Human governance assignment |
| RV-01 minimal site types → v1 `site_type_code` 1:1 map | WF-R01.8 workshop |
| Expansion page types: registry rows vs glossary-only | WF-R01.6 charter |
| BREADCRUMBS / PAGINATION as `block_id` vs layout policy | WF-R01.2 decision |
| Trust Pattern binding unit final form | WF-R01.4 charter |
| F6 standalone registry file vs blueprint field | WF-R01.5 architecture decision |
| Operational pages (login, account) in v1 scope | WF-R01.7 |
| Live registry audit confirming RV-01 gap counts | Post–R01.1 B3 audit |
| Reference Library Tier B artifacts (`production-systems-stack-v1`, `rv03-vl3-failure-crosswalk-v1`) | Optional parallel pass — not blocking |

---

## Final Status

| Criterion | Result |
|-----------|--------|
| V1 Authority Alignment | **PASS** |
| V2 Family Validation | **PASS** |
| V3 Boundary Validation | **PASS** |
| V4 Registry Independence | **PASS** |
| V5 Research Alignment | **PASS** |
| Charter published ACCEPTED | **DONE** |
| Pass report published | **DONE** |
| Authority cross-links (roadmap, OPERATIONAL-INDEX) | **DONE** |
| Registry content changes | **NONE** (forbidden) |
| WF-Axx / WF-Rxx status changes | **NONE** (forbidden) |

**WF-R01.0 exit criterion:** Vocabulary Canon Charter v1 **ACCEPTED** + authority model in OPERATIONAL-INDEX — **SATISFIED**.

---

**STOP — NO REGISTRY CHANGES · NO NEW IDS · NO SUBPROGRAM EXECUTION**

---

*Pass artifact: `reports/foundry-vocabulary-canon-charter-pass-v1.md`*
