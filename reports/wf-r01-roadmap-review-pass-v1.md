# REPORT — WF-R01 ROADMAP REVIEW PASS

**Artifact ID:** WF-R01 Roadmap Review Pass v1  
**Date:** 2026-06-19  
**Mode:** audit / review only — **no roadmap edits**, **no implementation**  
**Authority reviewed:**

| Surface | Path |
|---------|------|
| Roadmap | [roadmap.md](../projects/mars-website-factory/roadmap.md) |
| Operational index | [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) |

**Recent artifacts cross-checked:**

| ID | Artifact | Observed status |
|----|----------|-----------------|
| — | [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) | **ACCEPTED** |
| WF-R01.1 | [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) | **ACCEPTED** |
| WF-R01.2 | [wf-r01-2-structural-blocks-charter-v1.md](../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md) | **ACCEPTED** |
| WF-R01.3.1 | [wf-r01-3-1-coverage-model-charter-v1.md](../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md) | **ACCEPTED** |
| WF-R01.0 | [wf-r01-0-research-canon-integration-design-v1.md](wf-r01-0-research-canon-integration-design-v1.md) | **DESIGN** (exit via Vocabulary Canon) |
| WF-R01.3 | [wf-r01-3-reference-expansion-program-design-v1.md](wf-r01-3-reference-expansion-program-design-v1.md) | **DESIGN** |
| WF-R01.3.0 | [wf-r01-3-0-coverage-baseline-snapshot-v1.md](wf-r01-3-0-coverage-baseline-snapshot-v1.md) | **Published snapshot** |
| RV-01–03 | [research/foundry/](../research/foundry/) | **Research artifacts** (immutable snapshots) |

**Honesty boundary:** This pass compares **documented roadmap/index state** to **repo-evidenced Factory maturity**. **Not** runtime proof, **not** registry execution status beyond cited artifacts.

---

## Executive Summary

`roadmap.md` и `OPERATIONAL-INDEX.md` **частично отстают** от фактического состояния Website Factory после серии charter passes 2026-06-19. Ядро authority chain (WF-A01 ✅, WF-A02 ✅, WF-R01 CHARTERED, WF-A03 DEFERRED) **корректно**; подпрограммы WF-R01.1 и WF-R01.2 **отражены** в changelog и OPERATIONAL-INDEX Core Run.

**Главные расхождения:**

1. **Foundry Vocabulary Canon (ACCEPTED)** и **WF-R01.3.1 Coverage Model (ACCEPTED)** — фактически действуют как operator authority, но **не имеют** отдельных строк в roadmap § Factory architecture items.
2. **WF-R01.3** (Reference Expansion) и **WF-R01.3.0** (Coverage Baseline Snapshot) — существуют как design + metrics snapshot; roadmap **не фиксирует** G0 baseline и пятимерную модель.
3. **Подпрограммы WF-R01.4–R01.8** — описаны в program design, но roadmap сводит их к одной фразе «R01.1–R01.8» **без статусов**.
4. **OPERATIONAL-INDEX** обновлён по содержанию до 2026-06-19 (Vocabulary Canon, WF-R01.1/2), но **не содержит** WF-R01.3 / coverage baseline; footer **«Last updated: 2026-06-13»** устарел.
5. **Waves 1–6**, execution cases (Triumph V6, ISBD, BZPM), foundry audits — **существенная операционная реальность**, отсутствующая в roadmap phase table.
6. **RV-01–03** — цитируются в Vocabulary Canon и changelog; **нет** явного research marker в roadmap architecture table.

**Вердикт:** roadmap/index **пригодны** как entry surface для WF-A01/A02 и стартового WF-R01, но **недостаточны** как SSOT зрелости Registry/Reference Layer после Vocabulary Canon + Coverage Model. Рекомендуется **editorial roadmap pass** (отдельная задача) — не в рамках этого review.

---

## Program Inventory

### R1 — Phases 0–7 (`roadmap.md` phase table)

| Phase | Name | Status | Notes |
|-------|------|--------|-------|
| **0** | Registration and architecture | **COMPLETE** | Pack registered; cross-links exist |
| **1** | Registries and contracts | **COMPLETE** (doc) | Site Type / Block registries v0; handoff contracts |
| **2** | Artifact semantics and workflow depth | **COMPLETE** (doc) | Artifact Architecture v0, agent cards, workflow v0; optional wire examples = **SAFE UNKNOWN** |
| **3** | Prompt standards and QA gates | **COMPLETE** (doc) | Prompt Standards Layer v0 full stack |
| **4** | Execution semantics and operational methodology | **COMPLETE** (doc) | Execution Semantics, Reference Project, Semantic Relationship, Artifact Bus, Validation Runtime Model v0 |
| **5** | Cursor-based assisted production | **COMPLETE** (doc) | First Operational Runbook, Reference Case #1, Operational Templates v0 |
| **6** | Runtime-assisted execution | **DEFERRED** | Depends on MARS planned runtime — no repo evidence |
| **7** | Production automation experiments | **DEFERRED** | Governance + evals precondition |

### R1 — Factory architecture items (WF-Axx / WF-R01)

| ID | Name | Status | Evidence |
|----|------|--------|----------|
| **WF-A01** | Production Modes Contract | **COMPLETE** | Charter + implementation pass 01 |
| **WF-A02** | Validation Architecture | **COMPLETE** | Pass 01 + VL3 Pass 02 |
| **WF-R01** | Registry Expansion Program | **CHARTERED** | Program charter; execution **not ACTIVE** |
| **WF-A03** | Pixel Factory Expansion | **DEFERRED** | Explicit non-goals; R01 Gate 2+ precondition |

### R1 — WF-R01 subprograms (program design SoT + repo facts)

| ID | Name | Status | Notes |
|----|------|--------|-------|
| **WF-R01.0** | Research Canon Integration | **COMPLETE** (via design exit) | [wf-r01-0-research-canon-integration-design-v1.md](wf-r01-0-research-canon-integration-design-v1.md); exit criterion satisfied by Vocabulary Canon ACCEPTED |
| **—** | Foundry Vocabulary Canon | **ACCEPTED** | Cross-cutting authority; **not** numbered R01.x in roadmap |
| **WF-R01.1** | v0 → v1 Operational Binding | **ACCEPTED** (charter) | B1 satisfied; B3–B8 implementation **pending** |
| **WF-R01.2** | Structural Blocks Layer | **ACCEPTED** (charter) | Gate 1 complete; Gate 2 registry rows **not started** |
| **WF-R01.3** | Reference Implementation Expansion | **DESIGN** | Program design published; wave execution **not authorized** |
| **WF-R01.3.1** | Coverage Model & Metrics | **ACCEPTED** | Normative RC/RPC/RSC/SC/PC + G0–G4 gates |
| **WF-R01.3.0** | Coverage Baseline Snapshot | **Published** | G0 metrics snapshot; **not** roadmap-registered |
| **WF-R01.4** | Commercial Pattern Library v0 | **DESIGN** | Scope in program design only |
| **WF-R01.5** | SEO Content Pattern Slice | **DESIGN** | Scope in program design only |
| **WF-R01.6** | Blueprint & Registry Hygiene Pass | **DESIGN** | Scope in program design only |
| **WF-R01.7** | Template-Art Multi-Site-Type Charter | **DESIGN** | Scope in program design only |
| **WF-R01.8** | Execution Case → Registry Vocabulary Feed | **DESIGN** | Scope in program design only |
| **WF-R01.X** | Metrics, Gates & Roadmap Registration | **CHARTERED** (partial) | Parent program registered; subprogram table **incomplete** in roadmap |

### R1 — OPERATIONAL-INDEX waves and packs (factual, not in roadmap)

| Entity | Status | Roadmap presence |
|--------|--------|------------------|
| Wave 1 normalization | **COMPLETE** | ❌ Absent |
| Wave 2 foundation systems | **COMPLETE** | ❌ Absent |
| Wave 3 reference implementation | **COMPLETE** | ❌ Absent |
| Wave 4 production acceleration | **COMPLETE** | ❌ Absent |
| Wave 5 production hardening | **COMPLETE** | ❌ Absent |
| Wave 6 production consolidation | **COMPLETE** | ❌ Absent |
| Frontend Evolution Pack v1 | **COMPLETE** | ❌ Absent |
| Production Standards Governance Pack | **COMPLETE** | ❌ Absent |
| Enforcement Pack + Compliance + Failure Attribution | **COMPLETE** | ❌ Absent |
| Asset Identity Collision failure class | **ACCEPTED** (doc) | ❌ Absent |

### R1 — Supporting audits and discovery (inputs to WF-R01)

| Artifact | Status | Roadmap presence |
|----------|--------|------------------|
| [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) | **Published** | ❌ |
| [foundry-system-wide-layer-audit-v1.md](foundry-system-wide-layer-audit-v1.md) | **Published** | ❌ |
| [foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md) | **Published** | ❌ |
| [foundry-program-discovery-pass-v1.md](foundry-program-discovery-pass-v1.md) | **Published** (stale vs 2026-06-19) | ❌ |

### R1 — Live execution surfaces (factual Factory activity)

| Entity | Status | OPERATIONAL-INDEX | Roadmap |
|--------|--------|-------------------|---------|
| `website-factory-reference-v1` (9 partials) | **Active** | ✅ Wave 3–6 | ❌ |
| Triumph Manipulator V6 | **Active client** | ✅ Core Run | ❌ |
| ISBD Care Landing | **Client delivery case** | ✅ Core Run | ❌ |
| BZPM catalog redesign | **Research / pending enrollment** | ✅ execution-cases | ❌ |
| OCPilot SITE-001/002 | **Adjacent delivery** (OpenCart) | Partial (via cases) | ❌ |

---

## Missing Roadmap Items

### R2 — Entities that exist factually but are absent or under-registered in roadmap

| # | Entity | Factual evidence | Gap |
|---|--------|------------------|-----|
| M1 | **Foundry Vocabulary Canon** | ACCEPTED charter in `projects/mars-website-factory/` | No architecture-table row; only changelog bullet |
| M2 | **WF-R01.3.1 Coverage Model** | ACCEPTED metrics charter | Not in roadmap WF-R01 notes or OPERATIONAL-INDEX WF-R01 row |
| M3 | **WF-R01.3.0 Coverage Baseline Snapshot** | Published G0 metrics (RC 29/32, RPC 9/32) | Not registered as milestone |
| M4 | **WF-R01.3 program design** | Design artifact complete | Parent subprogram status **DESIGN** not surfaced in roadmap row |
| M5 | **WF-R01.0** | Design complete; exit via Vocabulary Canon | No explicit subprogram row (implicit in changelog only) |
| M6 | **Foundry audit trilogy** | Three audits — direct inputs to WF-R01 charter | Not cited in roadmap (acceptable as reports, but operators lack traceability) |
| M7 | **Waves 1–6 operational maturity** | OPERATIONAL-INDEX documents real reference blocks, QA, freeze | Phase table treats Phase 5 as «done» without waves — **understates** production consolidation work |
| M8 | **Execution cases registry** | Triumph V6, ISBD, BZPM registered | Absent from roadmap; OPERATIONAL-INDEX only |
| M9 | **Research Canon index row** | RV-01–03 in `research/foundry/` | No dedicated roadmap marker (R6) |
| M10 | **G0–G4 readiness gates** | Normative in WF-R01.3.1 | Roadmap still cites legacy «9/29 ~31%» framing in program design cross-refs |

**Severity:** M1–M4 = **high** (authority drift risk). M5–M10 = **medium** (discoverability / metrics honesty).

---

## Outdated Roadmap Items

### R3 — Stale elements after Vocabulary Canon, Coverage Model, Research Canon

| # | Location | Stale content | Current truth |
|---|----------|---------------|---------------|
| O1 | `roadmap.md` WF-R01 row | «registry row execution **not started**» only | Still true for Gate 2, but **omits** R01.3.1 ACCEPTED and G0 baseline |
| O2 | `roadmap.md` changelog 2026-06-19 (first entry) | «**no** WF-R01.2» | **Superseded** — R01.2 ACCEPTED same day (later changelog entry) |
| O3 | `roadmap.md` WF-R01 row | «subprograms R01.1–R01.8» without statuses | R01.1/2 ACCEPTED; R01.3 DESIGN; R01.3.1 ACCEPTED; R01.4–8 DESIGN |
| O4 | Program design + older cross-refs | RPC denominator **9/29 (~31%)** | WF-R01.3.1 binding: **9/32 (~28%)** preferred denominator post–R01.2 |
| O5 | WF-A03 deferred marker | «WF-R01 Gate 2+» | Align with WF-R01.3.1 **G2** definition (RPC ≥ 20/32 + catalog scaffold + structural T1+) |
| O6 | `OPERATIONAL-INDEX` WF-R01 Core Run row | Lists R01.1/2 only | Missing R01.3 design, R01.3.1 ACCEPTED, baseline snapshot |
| O7 | `OPERATIONAL-INDEX` footer | «Last updated: 2026-06-13» | Body includes 2026-06-19 packs — **metadata stale** |
| O8 | [foundry-program-discovery-pass-v1.md](foundry-program-discovery-pass-v1.md) | R01.1 = PROPOSAL; R01.2 «Not authorized» | **Stale** vs ACCEPTED charters (discovery predates acceptance passes) |
| O9 | Vocabulary Canon REG-VOC rules | Reference WF-R01.4–7 as **future** | Correct directionally, but roadmap does not show **dependency graph** Vocabulary → R01.2 → R01.3 |
| O10 | `registries.md` / curated-library v0 naming | SEO Pattern Library «planned»; v0 block names | WF-R01.5 and R01.1 B3–B5 **pending** — known drift, not yet reflected in roadmap remediation plan |

**Not outdated (still accurate):**

- WF-A01/A02 COMPLETE markers
- WF-A03 DEFERRED + explicit non-goals
- CHARTERED ≠ ACTIVE distinction for WF-R01
- Phase 6–7 dependency honesty on MARS runtime

---

## Coverage Baseline Impact

### R5 — Should Coverage Baseline Snapshot be registered as milestone?

**Recommendation: YES** — register **WF-R01.3.0 Coverage Baseline Snapshot** as **G0 milestone** under WF-R01.3.

| Field | Value |
|-------|-------|
| **Artifact** | [wf-r01-3-0-coverage-baseline-snapshot-v1.md](wf-r01-3-0-coverage-baseline-snapshot-v1.md) |
| **Gate** | **G0 (Baseline)** per WF-R01.3.1 |
| **Key metrics** | RC **29/32** (90.6%) · RPC **9/32** (~28.1%) · RSC **1/10** · SC **0/8** full · PC **0/1** formal |
| **Operator rule** | Registry completeness **≠** buildability — cite RPC + SC, not RC alone |

**Rationale:**

1. First **official measured** Reference Layer state after ACCEPTED coverage charter.
2. Establishes **reproducible baseline** for wave planning and WF-A03 precondition honesty.
3. Without roadmap registration, operators may continue citing legacy **9/29** or curated-library row count as proxy truth.

**Registration shape (recommended, future editorial pass):**

- Roadmap changelog entry + WF-R01 subprogram note: `R01.3.0 G0 BASELINE — published YYYY-MM-DD`
- OPERATIONAL-INDEX Core Run row append: link to snapshot + WF-R01.3.1 charter
- **Not** a new WF-Axx program — milestone under WF-R01.3 only

---

## Research Integration Impact

### R6 — Should RV-01, RV-02, RV-03 be linked in roadmap markers?

**Recommendation: YES** — add explicit **Research Canon (RV-01–03)** markers.

| Research | Primary roadmap consumers | Suggested marker role |
|----------|---------------------------|----------------------|
| **RV-01** | WF-R01.2, R01.4, R01.5, R01.7, Vocabulary Canon F1–F6 | Vocabulary / structural priority evidence |
| **RV-02** | WF-R01.6, layer-map, blueprint discipline | Production stack reference architecture |
| **RV-03** | WF-A03 (deferred), WF-A02 crosswalk | Pixel pipeline — **WF-A03 only**; forbidden in registry charters |

**Current state:**

| Surface | RV linkage |
|---------|------------|
| `foundry-vocabulary-canon-charter-v1.md` | ✅ Full RV-01–03 sections |
| `roadmap.md` changelog | ✅ Mentions RV-01–03 for Vocabulary Canon |
| `roadmap.md` architecture table | ❌ No research row |
| `OPERATIONAL-INDEX` Vocabulary Canon pack | ✅ `research/foundry/` link |
| `OPERATIONAL-INDEX` Core Run | ⚠️ Integration design linked from Vocabulary row only |
| WF-R01 program charter | ❌ No RV file paths |

**Authority model (from WF-R01.0 design — still valid):**

```text
Research Artifact (RV-01–03)  →  immutable snapshots
        ↓ selective tiering (WF-R01.0)
Vocabulary Canon (ACCEPTED)  →  family rules, REG-VOC-*
        ↓ human charter pass
Registry rows / charters      →  WF-R01.1+
```

**Anti-pattern to avoid:** treating RV gap tables as registry STATUS without re-audit (RV-01 provisional counts).

---

## Recommended Roadmap Changes

*Recommendations only — **not applied** in this pass.*

### Priority A — WF-R01 subprogram status table

Add expandable subsection under WF-R01 in `roadmap.md`:

| Subprogram | Status |
|------------|--------|
| R01.0 Research integration | COMPLETE (design exit) |
| Vocabulary Canon | ACCEPTED |
| R01.1 v0→v1 binding | ACCEPTED (impl pending) |
| R01.2 Structural blocks | ACCEPTED (Gate 2 pending) |
| R01.3 Reference expansion | DESIGN |
| R01.3.1 Coverage model | ACCEPTED |
| R01.3.0 G0 baseline | Published milestone |
| R01.4–R01.8 | DESIGN |
| R01.X metrics | Partial |

### Priority B — OPERATIONAL-INDEX sync

1. Extend **Registry Expansion / WF-R01** Core Run row with R01.3, R01.3.1, baseline snapshot links.
2. Update footer date to 2026-06-19 (or later when edited).
3. Optional: dedicated **Research Canon (RV-01–03)** Core Run row per WF-R01.0 § Roadmap Impact.

### Priority C — Metrics honesty

1. Replace legacy **9/29** citations in roadmap-adjacent summaries with **9/32** per WF-R01.3.1.
2. Align WF-A03 precondition text with **G2** semantics from coverage charter.

### Priority D — Vocabulary Canon registration

Add architecture item or WF-R01 cross-cutting row:

**Foundry Vocabulary Canon — ACCEPTED** (authority between Research and Registry).

### R4 — Official designation of WF-R01.4–R01.7

**Recommendation: YES** — already **defined** in [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md); roadmap should **surface explicit DESIGN status** for each:

| ID | Name | Official? | Roadmap action |
|----|------|-----------|----------------|
| **WF-R01.4** | Commercial Pattern Library v0 | ✅ In program design | Add status row |
| **WF-R01.5** | SEO Content Pattern Slice | ✅ In program design | Add status row |
| **WF-R01.6** | Blueprint & Registry Hygiene Pass | ✅ In program design | Add status row |
| **WF-R01.7** | Template-Art Multi-Site-Type Charter | ✅ In program design | Add status row |

**Not required:** new program IDs or WF-Axx numbers — subprogram enumeration suffices.

**Sequencing note (from charters):** R01.4/R01.5 may run **parallel** with R01.3 waves after R01.1 B3; R01.7 **depends** on R01.2 + R01.3 minimum gates.

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Authority drift** — operators use roadmap without Vocabulary Canon / Coverage Model | High | Editorial pass Priority A–D |
| **False readiness** — «29 blocks in registry» interpreted as Factory-ready | High | Mandate G0 snapshot + five-dimension REPORTs in wave charters |
| **Stale discovery pass** — R01.1 PROPOSAL wording misleads new operators | Medium | Archive note on discovery pass or supersede banner |
| **CHARTERED ≠ ACTIVE confusion** persists despite text | Medium | Keep STOP rules visible in OPERATIONAL-INDEX |
| **Research proxy** — audits cited without RV chain | Medium | Research Canon row in index |
| **OPERATIONAL-INDEX date footer** undermines trust | Low | Update metadata |
| **WF-A03 precondition ambiguity** (Gate 2 vs G2) | Medium | Unify terminology in deferred marker |
| **BZPM / OCPilot vocabulary mined into canon without enrollment** | High | WF-R01.8 + explicit HITL (already in charters; not in roadmap) |

---

## SAFE UNKNOWN

| Item | Unknown | Would verify via |
|------|---------|------------------|
| Named **WF-R01.3 human owner / steward** | Not fixed in repo | Operator charter assignment |
| **WF-R01.1 B3–B8** completion date | Implementation not started | Implementation pass REPORT |
| **BZPM W3** blueprint delivery date | UNKNOWN in charters | Client program status |
| **OCPilot SITE-001** Factory binding / `production_mode` | Not verified in audits | Enrollment charter |
| **Curated-library v2** (v1 `block_id` sync) schedule | Deferred to R01.3.X | Wave charter |
| **Phase 2** optional `task-contract-v0` wire examples | SAFE UNKNOWN schedule | Roadmap Phase 2 row |
| **Exact RSC denominator** (page types) | «~1/10+» — partial count | PAGE-TYPE-REGISTRY audit |
| Whether **separate WF-Axx row** needed for Vocabulary Canon vs WF-R01 cross-cut | Design choice | Operator governance decision |

---

## Recommended Next Step

**STOP** — no roadmap edits in this pass.

**Suggested follow-on (human-chartered editorial task):**

1. **Roadmap editorial pass v1** — apply Priority A–D recommendations (subprogram table, G0 milestone, RV markers, metrics denominator).
2. **OPERATIONAL-INDEX sync pass** — WF-R01 Core Run row + footer date + optional Research Canon row.
3. **WF-R01.1 implementation pass P2** — banner, STOP rule (B3), onboarding (B4) per binding charter (execution, not roadmap).

**Do not start** before editorial pass unless operator explicitly waives discoverability gap.

---

*Review artifact: `reports/wf-r01-roadmap-review-pass-v1.md`*
