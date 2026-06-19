# REPORT — WF-R01.2 STRUCTURAL BLOCKS CHARTER PASS

**Artifact ID:** WF-R01.2 Structural Blocks Layer — charter publication pass (v1)  
**Date:** 2026-06-19  
**Mode:** charter **publication** — **ACCEPTED** status; **no registry edits**, **no new IDs**, **no implementation**

**Inputs reviewed:**

| ID | Artifact |
|----|----------|
| Authority | [roadmap.md](../projects/mars-website-factory/roadmap.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) |
| Research | [rv-01-production-vocabulary.md](../research/foundry/rv-01-production-vocabulary.md) · [rv-02-website-production-systems.md](../research/foundry/rv-02-website-production-systems.md) · [rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md) |
| Vocabulary | [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) · [foundry-vocabulary-canon-charter-pass-v1.md](foundry-vocabulary-canon-charter-pass-v1.md) |
| WF-R01 | [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) · [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) · [wf-r01-2-structural-blocks-program-design-v1.md](wf-r01-2-structural-blocks-program-design-v1.md) |
| Validation | [website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) · [website-factory-validation-architecture-charter-v1.md](../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md) · [website-factory-vl3-domains-charter-v1.md](../projects/mars-website-factory/website-factory-vl3-domains-charter-v1.md) |

**Deliverable:** [wf-r01-2-structural-blocks-charter-v1.md](../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md) — **ACCEPTED**

**Honesty boundary:** This pass **published documentation only**. **Not** runtime, **not** registry content, **not** reference partials, **not** Blueprint edits.

---

## Executive Summary

WF-R01.2 Program Design (2026-06-19) определил Structural Blocks vocabulary, Tier A/B/C split, site-type impact, и readiness gates. До этого pass отсутствовал **официальный ACCEPTED charter** для Structural Blocks Layer как части FOUNDRY.

**Результат pass:** опубликован `wf-r01-2-structural-blocks-charter-v1.md` со статусом **ACCEPTED**. WF-R01.2 переведён **Design → ACCEPTED**. Charter фиксирует Structural Layer как **F3 Block → Structural Subtype**, Tier disposition, и Registry Readiness Rules — **zero registry rows**, **zero new IDs**.

**Все семь validation checks (S1–S7) PASS.**

```text
Gate 0  Design (program design report)     ✅
Gate 1  Charter ACCEPTED (this pass)        ✅
Gate 2  Registry v1.1 rows + matrices      ⏳ separate execution task
```

---

## Validation Results

### S1 — Vocabulary Compliance

**Verdict: PASS**

| Check | Result |
|-------|--------|
| Structural Block = Block Family (F3) → Structural Subtype | ✅ Not separate family |
| Six vocabulary families unchanged | ✅ No F7 introduced |
| REG-VOC-04 structural-before-marketing | ✅ Catalog ordering in charter |
| hero vs header_nav disambiguation | ✅ Binding rule |
| Commercial/Trust/SEO boundaries preserved | ✅ § What Structural Blocks are not |
| REG-VOC-05/06 pattern ≠ block | ✅ Patterns excluded from structural entities |

**Evidence:** [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) § F3 subtypes; charter § Vocabulary Alignment.

---

### S2 — Research Alignment

**Verdict: PASS**

| Research | In charter | Reference only |
|----------|------------|----------------|
| **RV-01** | Missing structural primitives priority; structural-before-marketing; minimal canon (Tier A = 3 terms); vertical deferral | Full industry tables; provisional STATUS cells; operational pages depth |
| **RV-02** | structural vs content_block boundary | 5-layer stack; canonical_asset glossary; content models |
| **RV-03** | — (orthogonal) | Orchestration loop; visual diff; pixel pipeline — WF-A03 only |

**Note:** Program design cited RV-01/02 as "not found" — **stale**; research files exist at `research/foundry/`. Charter pass uses current paths.

---

### S3 — Registry Independence

**Verdict: PASS**

| Check | Result |
|-------|--------|
| No `block_id` rows created | ✅ |
| No `page_type` rows created | ✅ |
| No `site_type_code` rows created | ✅ |
| No registry matrix edits | ✅ |
| Vocabulary terms cited as future promotion targets only | ✅ Tier A mandatory vocabulary ≠ registry rows |

**Charter remains above Registry** per AUTH-01..02; Gate 2 execution explicitly separated.

---

### S4 — Candidate Review

**Verdict: PASS — disposition fixed without creating IDs**

#### Tier A — Mandatory (vocabulary; future registry promotion)

| Candidate | Disposition |
|-----------|-------------|
| **HEADER_NAV** | **Mandatory** — Tier A minimal structural canon |
| **SEARCH** | **Mandatory** — CATALOG/ECOMMERCE |
| **FILTERS** | **Mandatory** — CATALOG/ECOMMERCE |

#### Tier B — Policy resolution (no v1.1 `block_id` by default)

| Candidate | Disposition |
|-----------|-------------|
| **BREADCRUMBS** | **Optional** — **layout-component policy** v1.1 |
| **PAGINATION** | **Optional** — **layout-component policy** v1.1 |
| **MEGA_MENU** | **HEADER_NAV variant** — not separate id |
| **THANK_YOU_POLICY** | **Deferred** — `CONFIRMATION_PAGE` page_type; no dedicated block v1.1 |

#### Tier C — Deferred

| Candidate | Disposition |
|-----------|-------------|
| SORT as separate id | **FILTERS sub-variant** — forbidden separate id |
| DEALER_LOCATOR, SPEC_TABLE, COMPARE_BAR, ACCOUNT_NAV | **Post-R01.2 / WF-R01.8** |

**Operator decisions pending in Vocabulary Canon SAFE UNKNOWN** — **resolved** by this charter for BREADCRUMBS/PAGINATION/MEGA_MENU/THANK_YOU.

---

### S5 — Site Type Impact

**Verdict: PASS**

| Site type | Structural impact documented | Aligns with design |
|-----------|------------------------------|-------------------|
| LANDING | None required; minimal header optional | ✅ |
| PROMO | HEADER_NAV obligatory | ✅ |
| CORPORATE | HEADER_NAV + optional catalog subtree | ✅ |
| CATALOG | HEADER_NAV + FILTERS + SEARCH obligatory | ✅ |
| ECOMMERCE | Above + utility nav composition | ✅ |
| MANUFACTURER* | CATALOG + CORPORATE composition | ✅ |
| AUTO* | Same as CATALOG | ✅ |
| MARKETPLACE** | Extended — hints only | ✅ |

\* Composition profile, not separate `site_type_code`.  
\** Extended type — out of Core Library v1.

---

### S6 — Template-Art Impact

**Verdict: PASS**

| Check | Result |
|-------|--------|
| TEMPLATE_ART SSOT = registries (WF-A01) | ✅ Acknowledged |
| Current effective scope LANDING-only | ✅ Documented |
| Structural prerequisites per site_type beyond LANDING | ✅ Table in charter |
| R01.2 ACCEPTED alone does not unlock multi-type Template-Art | ✅ Co-requires Gate 2 + R01.3 + R01.7 |
| LANDING-only interim policy until Gate 2 | ✅ Binding |

**Mandatory structural capabilities for Template-Art beyond LANDING:**

- **PROMO:** HEADER_NAV (+ optional SEARCH)
- **CATALOG / ECOMMERCE:** HEADER_NAV, FILTERS, SEARCH
- **CORPORATE:** HEADER_NAV (+ optional catalog subtree filters/search)

Implementation evidence (partials) — **WF-R01.3**, not this pass.

---

### S7 — Registry v1.1 Readiness

**Verdict: PASS — conditions defined; Gate 2 not met**

| Precondition | Status |
|--------------|--------|
| R1 — WF-R01.2 charter ACCEPTED | ✅ **This pass** |
| R2 — WF-R01.1 B1 ACCEPTED | ✅ |
| R3 — WF-R01.1 B3 STOP rule live | ⏳ Pending |
| R4 — Separate execution task authorized | ⏳ Not started |
| R5 — No mixed v0/v1 in target artifacts | ⏳ Verify at execution |

**Gate 2 deliverables enumerated:** BLOCK-CONTRACT rows (Tier A only), SITE-TYPE-BLOCK-MATRIX, PAGE/BLUEPRINT mappings, BLOCK-DEPENDENCY-RULES, GAPS closure audit.

**M3 metric:** 3/3 structural ids in **registry** — target for Gate 2, not Gate 1.

---

## Charter Publication

| Field | Value |
|-------|-------|
| **Path** | `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md` |
| **Status** | **ACCEPTED** |
| **Version** | v1 |
| **Date** | 2026-06-19 |
| **Registry rows created** | **0** |
| **New IDs created** | **0** |
| **WF-R01.2 subprogram state** | **Design → ACCEPTED** |

**Structure delivered:**

- Executive Summary
- Structural Layer Definition
- Structural Categories (S1–S4 + Tier summary)
- Vocabulary Alignment
- Research Alignment (RV-01/02/03)
- Site Type Impact
- Template-Art Impact
- Registry Readiness Rules (Gate 1/2)
- Non-Goals
- Risks
- SAFE UNKNOWN

---

## Vocabulary Alignment

Structural Blocks Layer is now **official FOUNDRY vocabulary authority** under:

```text
F3 Block → Structural Subtype
```

**Not** a seventh vocabulary family. Aligns with [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) § F3, REG-VOC-04, and glossary `hero` vs `header_nav`.

**Resolved from Vocabulary Canon SAFE UNKNOWN:**

| Item | Resolution |
|------|------------|
| BREADCRUMBS as `block_id` vs layout | **Layout-component policy** v1.1 |
| PAGINATION as `block_id` vs layout | **Layout-component policy** v1.1 |
| MEGA_MENU variant vs separate id | **HEADER_NAV variant** |

---

## Research Alignment

| Source | Charter integration |
|--------|---------------------|
| **RV-01** | Tier A/B/C disposition; structural-before-marketing; minimal canon = 3 terms; vertical deferral |
| **RV-02** | structural/content boundary only — stack layers reference-only |
| **RV-03** | No structural vocabulary claims — WF-A03 deferred |

Proxy-only evidence note in program design — **superseded** for charter pass; RV files are authoritative research inputs per WF-R01.0 integration.

---

## Site Type Impact

Charter § Site Type Impact adopts program design matrix unchanged. Key binding outcomes:

- **CATALOG/ECOMMERCE** — structural layer **obligatory** for honest blueprints
- **LANDING** — structural absence **intentional**
- **MANUFACTURER/AUTO** — composition over CATALOG + CORPORATE; no new `site_type_code`
- **MARKETPLACE** — Extended hints only

---

## Template-Art Impact

**Before R01.2 ACCEPTED:** LANDING-only interim mandatory.  
**After R01.2 ACCEPTED:** Vocabulary honest; production still LANDING-only until Gate 2 + R01.3 + R01.7.

WF-A01 `TEMPLATE_ART` registry SSOT requirement — **satisfied at vocabulary layer**; **not** at implementation layer.

---

## Registry Readiness

| Gate | Status |
|------|--------|
| Gate 0 — Design | ✅ |
| Gate 1 — Charter ACCEPTED | ✅ **This pass** |
| Gate 2 — Registry rows | ⏳ Blocked on R3 (B3) + execution task |

**Next authorized step (out of scope for this pass):** WF-R01.2 **execution** task — Tier A BLOCK-CONTRACT rows + matrix updates, **after** B3 STOP rule minimum.

---

## Risks

| Risk | Severity | Status |
|------|----------|--------|
| False "structural complete" after ACCEPTED | Critical | Mitigated — M3 = registry rows |
| TEMPLATE_ART on CATALOG before Gate 2 | Critical | LANDING-only interim remains |
| Scope creep beyond Tier A | Critical | Tier C explicit deferral |
| B3 not live before row edits | High | R3 pending — operator action |
| BREADCRUMBS layout policy vs future automation | Medium | Monitor — waiver charter if needed |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Named WF-R01.2 steward | **Not fixed** |
| WF-R01.1 B3–B8 implementation | **Pending** |
| T_cutover date | **Pending** |
| OCPilot SITE-001 v1 binding | **Not verified** |
| BZPM W3 blueprint delivery | **UNKNOWN** |
| Faceted SEO for FILTERS URLs | **FUTURE** — WF-R01.5 |
| JSON Schema for structural rows | **NOT DEFINED** |
| BREADCRUMBS/PAGINATION future block_id waiver | **Monitor** |

---

## Final Status

| Item | Value |
|------|-------|
| **WF-R01.2** | **ACCEPTED** (Gate 1 complete) |
| **Structural Layer in FOUNDRY** | **Official** — F3 subtype |
| **Registry changes** | **None** |
| **New IDs** | **None** |
| **Implementation** | **Not started** (Gate 2) |
| **S1–S7 validation** | **All PASS** |

**Authority updates applied:** cross-links in `roadmap.md` and `OPERATIONAL-INDEX.md` only.

**STOP AFTER REPORT — NO REGISTRY CHANGES — NO NEW IDS — NO IMPLEMENTATION**

---

*Pass artifact: `reports/wf-r01-2-structural-blocks-charter-pass-v1.md`*  
*Accepted charter: `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md`*
