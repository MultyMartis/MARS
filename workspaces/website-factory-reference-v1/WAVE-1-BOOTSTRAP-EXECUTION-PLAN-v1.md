# REPORT — Wave 1 Bootstrap Execution Plan v1

**Версия:** v1  
**Дата:** 2026-06-07  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical MVP Artifact Creation Era — **Wave 1 execution planning only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE**; Physical Artifact Specifications **COMPLETE**; Physical Artifact Specifications Consolidation Review **COMPLETE**; ATLAS Adoption **COMPLETE**; Physical MVP Artifact Creation Strategy **COMPLETE**; Physical MVP Artifact Creation Era **AUTHORIZED**; **no physical artifacts created yet**  
**Тип:** execution plan only — **без** artifact creation, folder creation, records, bindings, serialization, layouts, runtime, automation  
**Primary inputs:** [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-CREATION-STRATEGY-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-CREATION-STRATEGY-v1.md), [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md), Playbooks 01–05, [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md)

---

## Executive Summary

**Вердикт:** Wave 1 — **единственный authorized первый шаг** Physical MVP Artifact Creation Era. Wave 1 материализует **substrate + manifest binding** для одного Core 5 pilot case и доказывает capabilities **C2** и **C3** — **без** registry, surface, index scaffold, Playbook 04/05 population и **без** любых forbidden runtime/automation артефактов.

**Wave 1 создаёт:** `LOC-ZONE`, `LOC-HOME`, substrate classes `POC-01`, `POC-02` (manifest facet), `POC-09`, и manifest content classes `MOC-01…MOC-05`, `MOC-08`, `MOC-10`, `MOC-12` (+ conditional `MOC-06`) для pilot Factory Project после Playbook 01 doctrinal enrollment и operator manifest bind act.

**Wave 1 не создаёт:** registry facet (`POC-02(r)`, `ROC-*`), tracking indexes (`POC-03…POC-07`, `POC-10`), closure (`POC-08`), surface (`SOC-*`), workflow engine, validators, dashboards, ATLAS registry rows, bindings как runtime integration.

**Pilot (рекомендован, не создан):** ATLAS-anchored Triumph / Манипулятор — `ORG-0004` + `PRJ-0008` + `WEB-0009`, site class **LANDING**, external workspace pointer `projects/triumph-manipulator-landing/`.

**Wave 1 gate:** `MOC-01` discoverable; Playbook 01 doctrinal enrolled attested in `MOC-10`; checklist **R-M1…R-M7** pass; **no** registry/surface required.

**Следующий authorized task после Wave 1 exit:** Wave 2 — Portfolio & Visibility Scaffold (RT-G05 + index scaffold + RT-G12) — **отдельная задача**, не часть Wave 1.

**Verified repo state (2026-06-07):** `workspaces/website-factory-operations/` **absent** on disk — expected; `projects/triumph-manipulator-landing/` **exists**.

---

## Wave 1 Scope

### Что входит в Wave 1

Wave 1 соответствует **Creation Strategy Wave 1 — Substrate & Manifest Bootstrap** (фазы A + B operational cycle):

| # | In-scope | Track | Capability |
|---|----------|-------|------------|
| 1 | Authorized Factory Records Zone | RT-G04 | **C2** — persistence substrate |
| 2 | Per-project record home для pilot | RT-G04 | **C2** |
| 3 | Identity shell + manifest binding carrier | RT-G04 | **C2** substrate hosting |
| 4 | Topology reference index (locators only) | RT-G04 + RT-G10 | **C3** topology wiring |
| 5 | Playbook 01 doctrinal manifest-enrolled act | Playbook 01 | Prerequisite — not physical artifact |
| 6 | Manifest bind: entry anchor + MRDY categories | RT-G10 | **C3** |
| 7 | ATLAS `atlas_*_ref` fields in MOC-12 when known | Adoption RC-01 | C1 consumer discipline — refs only |
| 8 | Operator-controlled disk writes | Operational Model OA-ACT-01 | Human/assisted only |
| 9 | Serialization convention lock (operator choice) | Pre-W1 gate | Format choice — **not** spec in this plan |
| 10 | R-M* manifest readiness verification | RT-G10 | Wave 1 exit evidence |

### Что явно НЕ входит в Wave 1

| # | Out-of-scope | Deferred to |
|---|--------------|-------------|
| 1 | Registry bind — `POC-02(r)`, `ROC-01…ROC-09` | **Wave 2** (RT-G05) |
| 2 | Index scaffold — `POC-03…POC-05` (even empty) | **Wave 2** (RT-G04 index loci) |
| 3 | Surface read bind — `SOC-01…SOC-08` | **Wave 2** (RT-G12) |
| 4 | Playbook 02 doctrinal registry-enrolled + bind | **Wave 2** |
| 5 | Playbook 04 declarations — `POC-03…POC-07`, `POC-10` | **Wave 3** |
| 6 | Playbook 03 sessions / Playbook 05 closure — `POC-08` | **Wave 3** |
| 7 | MVP success evidence S1, S3–S9 | **Wave 3** + era exit |
| 8 | Capabilities **C4**, **C5**, **C6**, **C7** | **Wave 2–3** |
| 9 | Workflow engine, automation, validator CLI, queue, dashboard | Post-MVP — forbidden |
| 10 | ATLAS canonical registry rows / relationship writes | Forbidden — refs only |
| 11 | Layer artefact bodies, Legal Pack generation, deploy | External / post-Factory |
| 12 | Second Factory Project | Optional generality — not Wave 1 requirement |
| 13 | Git commit/push of operational zone | Operator policy (DF-10) — not Wave 1 gate |

### Scope boundary statement

```text
  Wave 1
    ├── RT-G04: LOC-ZONE, LOC-HOME, POC-01, POC-02(m), POC-09
    ├── RT-G10: MOC-01…05, 08, 10, 12 (+ MOC-06 when mandated)
    └── Playbook 01 doctrinal enrollment → manifest bind

  Wave 1 STOP ──▶ no ROC, no SOC, no POC-03…08 population

  Wave 2 (separate authorization) ──▶ registry + index scaffold + surface
```

**Normative rule W1-SCOPE-01:** Wave 1 **must not** proceed to registry or surface creation even if substrate and manifest bind complete early — intermediate verification gate is mandatory per Creation Strategy.

---

## Pilot Definition

### Рекомендованный pilot case

**Decision:** первый physical pilot **SHOULD** использовать **реальные ATLAS population references** для Triumph / Манипулятор — **не** synthetic test project.

| Dimension | Pilot value | Role |
|-----------|-------------|------|
| **Factory site class** | **LANDING** (Core 5) | `site_type_code` in MOC-06 when charter mandates |
| **`atlas_client_org_ref`** | **`ORG-0004`** | Триумф — commissioning / client organization |
| **`atlas_project_ref`** | **`PRJ-0008`** | Манипулятор — structural ATLAS project (**not** Factory Project id) |
| **`atlas_website_ref`** | **`WEB-0009`** | manipulator-triumph.ru — website identity |
| **External workspace pointer** | `projects/triumph-manipulator-landing/` | POC-09 / MOC-12 locator — pointer only, no body embed |
| **Factory Project identity** | **New logical shell** (MOC-02 / POC-01) | **Distinct** from `PRJ-0008` per TG-ATLAS-01 |

### ATLAS reference verification (documentation-level)

Per [ATLAS-INTEGRITY-SNAPSHOT-REGISTER-v1.md](../../projects/atlas/audit/ATLAS-INTEGRITY-SNAPSHOT-REGISTER-v1.md) and population waves:

| Ref | Entity | Lifecycle | Relationship check |
|-----|--------|-----------|-------------------|
| **ORG-0004** | ООО «Триумф» / Триумф | **active** (Wave 1) | CLIENT_OF → ORG-0001 (REL-0016) |
| **PRJ-0008** | Манипулятор | **active** | COMMISSIONED_BY ORG-0004 (REL-0025); EXECUTES ORG-0001 (REL-0026) |
| **WEB-0009** | manipulator-triumph.ru | **active** | BELONGS_TO PRJ-0008 (REL-0031); OWNS ORG-0004 (REL-0035); DOM-0004 |

**Verdict:** recommended pilot triplet **ORG-0004 / PRJ-0008 / WEB-0009** is **consistent** with attested ATLAS population documentation. **No alternative pilot recommended** unless operator explicitly requires zero ATLAS coupling (synthetic case — lower governance value; does not satisfy ATLAS adoption validation dimension).

**SAFE UNKNOWN:** whether these records are **live attested canonical on a runtime ATLAS service** — population docs are documentation-level only.

### Pilot binding model (normative — plan only, no bindings created)

| Rule | Constraint |
|------|------------|
| **BIND-P-01** | Factory Project **receives own identity shell** — **must not** merge with ATLAS Project id |
| **BIND-P-02** | MOC-12 carries `atlas_*_ref` **pointers** — **must not** restate org facts (ENROLL-ATLAS-01, RC-01) |
| **BIND-P-03** | MOC-03 carries **production scope categories** — not canonical identity duplication |
| **BIND-P-04** | Legal Entity Card, if used later, **follows** RC-02 LEC ↔ Counterparty Card crosswalk |
| **BIND-P-05** | Deploy authorization — **SAFE UNKNOWN**; Factory closure ≠ deploy authorization |
| **BIND-P-06** | Single Factory operator for entire MVP demonstration |

### Synthetic pilot — when permitted

Synthetic case **MAY** be used **only** if operator explicitly requires isolation testing with zero ATLAS coupling — **not** default MVP path. Synthetic pilot **does not satisfy** ATLAS adoption validation dimension.

### Alternatives considered and rejected

| Alternative | Why rejected for Wave 1 |
|-------------|-------------------------|
| PRJ-0005 / WEB-0008 (Грузотакси) | Valid ATLAS case; Манипулятор preferred — dedicated landing workspace exists, cleaner LANDING-class demo |
| PRJ-0004 (deprecated redesign) | PRJ-0004 lifecycle **deprecated** — unsuitable anchor |
| Synthetic TEST-PROJECT-001 | Avoids RC-01/ENROLL-ATLAS-01 discipline; false comfort |

---

## Creation Inventory

### Tier 0 — Infrastructure (mandatory)

| Class | Disposition | Wave 1 | Notes |
|-------|-------------|--------|-------|
| **LOC-ZONE** | **Mandatory** | **Create** | `workspaces/website-factory-operations/` (DF-03) — first physical act |
| **LOC-HOME** | **Mandatory** | **Create** | Exactly one per pilot Factory Project identity (P1, POC-RULE-01) |

### Tier 1 — Substrate records (mandatory for manifest bind)

| Class | Disposition | Wave 1 | Notes |
|-------|-------------|--------|-------|
| **POC-01** | **Mandatory** | **Create** | Identity shell bound to LOC-HOME |
| **POC-02** manifest facet | **Mandatory** | **Create** | Binding carrier for MOC-* — separate from registry facet |
| **POC-09** | **Mandatory** | **Create** | Topology refs to index loci — **even if targets empty** (OBL-M-SUB-04) |

### Tier 2 — Manifest content (mandatory on bind)

| Class | Disposition | Wave 1 | Notes |
|-------|-------------|--------|-------|
| **MOC-01** | **Mandatory** | **Create** | Entry anchor — MVP hinge (MRDY-06, S2, C3) |
| **MOC-02** | **Mandatory** | **Create** | Factory Project identity reference — distinct from `atlas_project_ref` |
| **MOC-03** | **Mandatory** | **Create** | Scope categories — production intent, not org registry |
| **MOC-04** | **Mandatory** | **Create** | Declared lifecycle endpoint category |
| **MOC-05** | **Mandatory** | **Create** | Scope applicability doctrine |
| **MOC-08** | **Mandatory** | **Create** | Topology map — points to POC-03…05/09 loci (may be empty) |
| **MOC-10** | **Mandatory** | **Create** | Playbook 01 enrollment bind metadata — bind **follows** enrolled |
| **MOC-12** | **Mandatory** | **Create** | External refs + ATLAS `atlas_*_ref` when known |

### Tier 3 — Conditional manifest content

| Class | Disposition | Wave 1 | Notes |
|-------|-------------|--------|-------|
| **MOC-06** | **Conditional mandatory** | **Create** (expected) | Core 5 LANDING pilot — `site_type_code` binding **expected** at bind per OBL-M-06 |
| **MOC-11** | **Conditional** | **Create if amended** | Only when stable categories amended (ST-01) — typically absent at first bind |

### Tier 4 — Optional (Wave 1 permitted, not required)

| Class | Disposition | Wave 1 | Notes |
|-------|-------------|--------|-------|
| **MOC-07** | **Optional** | **May omit** | Pointer-only if present — **must not** duplicate POC-03 |
| **MOC-09** | **Optional** | **May omit** | Foundation pins when explicitly declared |
| **MOC-O1** | **Optional** | **May omit** | Pre-bind enrollment draft — non-authoritative |
| **POC-O2** | **Optional** | **May omit** | Pre-bind enrollment notes — non-authoritative |

### Explicitly excluded from Wave 1 inventory

| Class / role | Disposition | Why excluded |
|--------------|-------------|--------------|
| **POC-02** registry facet | **Excluded** | Wave 2 — RT-G05 |
| **ROC-01…ROC-09** | **Excluded** | Wave 2 — C4 |
| **POC-03…POC-05** | **Excluded** | Wave 2 index scaffold — prerequisite for credible Playbook 03, not Wave 1 |
| **POC-06, POC-07, POC-10** | **Excluded** | Wave 3 — Playbook 04 |
| **POC-08** | **Excluded** | Wave 3 — Playbook 05 |
| **SOC-01…SOC-11** | **Excluded** | Wave 2 — C5 |
| **POC-D1, POC-O1** | **Excluded** | Optional convenience — not Wave 1 floor |
| **MOC-X1** | **Forbidden default** | Derived snapshot — default absent |
| RT-G01/02/03/06/07/08/09/11/13/14/15 artifacts | **Forbidden** | Post-MVP / scope creep |
| ATLAS ORG/PER/WEB/PRJ/REL registry rows | **Forbidden** | ADOPT-01 — refs only |

### Inventory summary matrix

| Category | Mandatory | Conditional | Optional | Excluded |
|----------|-----------|-------------|----------|----------|
| Infrastructure | LOC-ZONE, LOC-HOME | — | — | — |
| Substrate | POC-01, POC-02(m), POC-09 | — | POC-O2 | POC-02(r), POC-03…08, POC-10, POC-D1, POC-O1 |
| Manifest | MOC-01…05, 08, 10, 12 | MOC-06, MOC-11 | MOC-07, MOC-09, MOC-O1 | MOC-X1 |
| Registry / Surface | — | — | — | ROC-*, SOC-* |

---

## Creation Sequence

### Normative execution order (Wave 1 only)

Wave 1 follows **RT-G04 → RT-G10** with Playbook 01 enrollment **preceding** physical bind. **No implementation, no serialization design** — execution logic only.

```text
  PRE-W1
    │
    ├─ Step 0a  Explicit operator authorization for disk writes (Gate 0-3)
    ├─ Step 0b  Serialization convention lock — format + COL-* class separation (Gate 1-1)
    ├─ Step 0c  Confirm pilot case — Triumph/Манипулятор LANDING (Gate 1-2)
    ├─ Step 0d  ATLAS ref research — ENROLL-ATLAS-01 lookup ORG/WEB/PRJ (Gate 1-3)
    ├─ Step 0e  Terminology guards acknowledged — TG-ATLAS-01 (Gate 1-5)
    └─ Step 0f  Playbook 01 doctrinally ready — operator attestation (Gate 1-4)

  W1-RT-G04 (substrate)
    │
    ├─ Step 1   Create LOC-ZONE at workspaces/website-factory-operations/
    ├─ Step 2   Create LOC-HOME for pilot Factory Project
    └─ Step 3   Create POC-01 identity shell in LOC-HOME

  W1-PLAYBOOK-01 (doctrinal — may precede or interleave with Step 1–3, MUST precede bind)
    │
    └─ Step 4   Execute Playbook 01 → manifest-enrolled outcome (doctrinal act)
                Recognition → MRDY evaluation → enrollment decision
                ATLAS-first enrollment discipline (RC-05)

  W1-RT-G10 (manifest bind)
    │
    ├─ Step 5   Create POC-02 manifest facet (binding carrier)
    ├─ Step 6   Materialize MOC-01 entry anchor
    ├─ Step 7   Materialize MOC-02…MOC-05 (MRDY categories)
    ├─ Step 8   Materialize MOC-06 classification anchors (Core 5 LANDING — expected)
    ├─ Step 9   Materialize MOC-08 topology + MOC-12 external/ATLAS refs
    ├─ Step 10  Materialize MOC-10 enrollment bind metadata → Playbook 01 act
    └─ Step 11  Create POC-09 topology refs → index loci paths (targets may not exist yet)

  W1-VERIFY
    │
    ├─ Step 12  Run R-M1…R-M7 checklist (RT-G10 Readiness Model)
    └─ Step 13  Wave 1 gate verification → STOP — do not enter Wave 2
```

### Step-by-step execution reference

| Step | Phase | Action | Precondition | Produces |
|------|-------|--------|--------------|----------|
| 0a | Pre-W1 | Operator authorization for physical creation | Era authorized (Gate 0-2) | Governance attestation |
| 0b | Pre-W1 | Lock serialization convention | Operator workshop | Documented format choice |
| 0c | Pre-W1 | Confirm pilot: LANDING / Triumph-Манипулятор | Core 5 constraint | Pilot charter note |
| 0d | Pre-W1 | ATLAS lookup: ORG-0004, PRJ-0008, WEB-0009 | ENROLL-ATLAS-01 | Ref values or SAFE UNKNOWN |
| 0e | Pre-W1 | Acknowledge TG-ATLAS-01 homonym guards | Adoption Statement | Operator attestation |
| 0f | Pre-W1 | Confirm Playbook 01 executable | Doctrine complete | Operator readiness |
| 1 | W1 | Create authorized zone | 0a complete | LOC-ZONE |
| 2 | W1 | Create project record home | Step 1 | LOC-HOME |
| 3 | W1 | Create identity shell | Steps 1–2 | POC-01 |
| 4 | W1 | Playbook 01 doctrinal enrollment | Steps 0c–0f | manifest-enrolled (doctrinal) |
| 5 | W1 | Manifest binding carrier | Step 4 enrolled | POC-02(m) |
| 6–10 | W1 | Manifest content bind | Step 5 | MOC-01…12 per inventory |
| 11 | W1 | Topology reference index | MOC-08 wired | POC-09 |
| 12 | W1 | R-M* verification | Steps 1–11 | Checklist evidence |
| 13 | W1 | Wave 1 gate pass → **STOP** | R-M* pass | Wave 1 complete |

### Forbidden orderings (Wave 1 relevant)

| Violation | Why forbidden |
|-----------|---------------|
| Physical bind before Playbook 01 doctrinal enrollment | INT-M01, INT-M09 — discovery bind forbidden |
| MOC-* before LOC-ZONE / LOC-HOME / POC-01 | OBL-M-SUB-01…03 — substrate first |
| Registry bind (Wave 2) before MOC-01 stable | G04-IMPL-02; REL-12 broken |
| MOC-03 populated with org identity facts instead of MOC-12 refs | ENROLL-ATLAS-01; R-06 duplication risk |
| POC-03…07 creation in Wave 1 | Out of scope — index scaffold is Wave 2 |
| SOC-* creation in Wave 1 | Out of scope — surface is Wave 2 |
| Automated bind on git folder discovery | H-05, RD-04, RAP-10 |

---

## Readiness Gates

### Gate 0 — Era authorization (must be true before any Wave 1 byte on disk)

| # | Condition | Verification | Status |
|---|-----------|--------------|--------|
| G0-1 | Physical Artifact Specification Era **COMPLETE** | Consolidation Review verdict | **Met** |
| G0-2 | Physical MVP Artifact Creation Era **AUTHORIZED** | Governance acknowledgment | **Met** |
| G0-3 | **Separate operator authorization** for disk writes | Explicit operator act | **Pending** — not automatic from era authorization |
| G0-4 | ATLAS Adoption Statement **accepted** (C1) | WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1 | **Met** |
| G0-5 | No BLOCK corrections from ATLAS audit | Integration Audit: conditional GO | **Met** |
| G0-6 | `workspaces/website-factory-operations/` absent or intentionally empty | Repo verify | **Met** (absent) |

### Gate 1 — Pre-Wave 1 (must be true before Step 1)

| # | Condition | Verification | Status |
|---|-----------|--------------|--------|
| G1-1 | Serialization convention **locked** for pilot | Operator documents format + COL-* layout | **Pending** — operator choice at execution |
| G1-2 | Pilot case **selected** — Core 5 LANDING identified | Operator charter | **Recommended** — Triumph/Манипулятор |
| G1-3 | ATLAS refs **researched** (ENROLL-ATLAS-01) | ORG/WEB/PRJ lookup or SAFE UNKNOWN | **Recommended** — ORG-0004/PRJ-0008/WEB-0009 documented |
| G1-4 | Playbook 01 **doctrinally ready** to execute | Operator attestation | **Pending** — execution-time |
| G1-5 | Terminology guards **acknowledged** | TG-ATLAS-01 | **Pending** — execution-time |

### Wave 1 exit gate (must be true before Wave 2 may begin)

| # | Condition | Verification |
|---|-----------|--------------|
| W1-G1 | **LOC-ZONE** exists at authorized path | Physical verify |
| W1-G2 | **LOC-HOME** + **POC-01** exist for pilot | Physical verify |
| W1-G3 | **POC-02(m)** + **POC-09** exist | Physical verify |
| W1-G4 | **MOC-01** discoverable — single canonical entry anchor | R-M2 |
| W1-G5 | **MOC-02…MOC-05**, **MOC-08**, **MOC-10**, **MOC-12** present | R-M3, R-M4 |
| W1-G6 | Playbook 01 enrollment attested in **MOC-10** | R-M1 |
| W1-G7 | ATLAS refs in **MOC-12** when known; SAFE UNKNOWN when not | R-M3a |
| W1-G8 | No registry facet, no ROC-*, no SOC-*, no POC-03…08 | Scope audit |
| W1-G9 | R-M1…R-M7 checklist **pass** | Operator verification |
| W1-G10 | **No** forbidden classes materialized | Scope audit |

---

## Success Criteria

Wave 1 success is scoped to **C2** and **C3 only** — **not** C4/C5/C6/C7, **not** S1/S3–S9 full MVP.

### C2 — Persistence substrate

| Criterion | Physical proof required at Wave 1 completion |
|-----------|-----------------------------------------------|
| **C2** | **LOC-ZONE** exists at `workspaces/website-factory-operations/`; operator can read and **manually** read/write Factory Project records within authorized zone for pilot case |

**Evidence:** operator can navigate to LOC-ZONE, locate pilot LOC-HOME, identify POC-01 without monorepo archaeology.

### C3 — Manifest persistence

| Criterion | Physical proof required at Wave 1 completion |
|-----------|-----------------------------------------------|
| **C3** | **MOC-01** is **single canonical entry anchor** per Factory Project; MRDY minimum understanding categories present in **MOC-02…MOC-05**, **MOC-08**, **MOC-10**, **MOC-12** |

**Evidence:** R-M1…R-M7 pass; operator identifies exactly one «start here» locus; MOC-10 links to prior Playbook 01 act; MOC-12 carries ATLAS refs (not identity restatement).

### Partial success signal (S2 — not full MVP success)

| ID | Criterion | Wave 1 contribution |
|----|-----------|---------------------|
| **S2** | Manifest-enrolled with persisted entry anchor | **Partially satisfied** — physical MOC-01 exists; full S2 confirmed at MVP completion |

### What does NOT count as Wave 1 success

| Non-success | Why |
|-------------|-----|
| Zone folder exists but manifest bind incomplete | Infrastructure alone ≠ C3 |
| Registry catalog lists pilot | C4 — Wave 2 |
| Eight Surface questions answerable | C5 — Wave 2 |
| Playbook 04 declarations reflected | C6 — Wave 3 |
| Playbook 05 closure in POC-08 | C7 — Wave 3 |
| Documentation-only Playbook 01 without physical bind | Pre-MVP baseline |

---

## Risk Review

### Wave 1–specific risk register

| ID | Risk | Severity | Wave 1 mitigation |
|----|------|----------|-------------------|
| **R-W1-01** | **ATLAS duplication** — org facts copied into MOC-03 instead of MOC-12 refs | **HIGH** | ENROLL-ATLAS-01; RC-01; MOC-03 = production scope only |
| **R-W1-02** | **Identity drift** — Factory Project id conflated with PRJ-0008 | **HIGH** | TG-ATLAS-01; MOC-02 distinct from `atlas_project_ref` |
| **R-W1-03** | **Scope creep** — Wave 1 expanded to registry/surface | **HIGH** | W1-SCOPE-01; explicit STOP at Step 13 |
| **R-W1-04** | **Premature registry** — ROC created before MOC-01 stable | **HIGH** | Wave 1 inventory excludes ROC-*; forbidden ordering table |
| **R-W1-05** | **Premature surface** — SOC created before manifest stable | **HIGH** | Wave 1 excludes SOC-*; SC-02 guard |
| **R-W1-06** | **Runtime pressure** — «files exist, add workflow engine» | **HIGH** | SC-01; explicit non-claims; no RT-G01 artifacts |
| **R-W1-07** | **Discovery bind** — auto-enrollment from git folder scan | **HIGH** | INT-M01; Playbook 01 must precede bind |
| **R-W1-08** | **Mega-record anti-pattern** — single file swallows MOC + POC planes | **HIGH** | POC-RULE-02, MOC-RULE-02, COL-* separation |
| **R-W1-09** | **Serialization lock-in** — format breaks class separation | **MEDIUM** | COL-* normative regardless of JSON/YAML/markdown |
| **R-W1-10** | **False «MVP shipped» narrative** after Wave 1 | **HIGH** | Wave 1 ≠ MVP complete; C4–C7 deferred |
| **R-W1-11** | **Parallel ATLAS registry** — Factory zone stores ORG-* rows | **HIGH** | ADOPT-01; refs only in MOC-12 |
| **R-W1-12** | **Triumph workspace ref ambiguity** | **LOW** | DF-08 per-case; pointer-only in POC-09/MOC-12 |
| **R-W1-13** | **v0↔v1 corpus mixing** during assisted writes | **LOW** | OQ-OM06 routing before agent-assisted creation |

### Risk summary

| Category | HIGH | MEDIUM | LOW |
|----------|------|--------|-----|
| Wave 1 risks | 8 | 1 | 2 |

**Interpretation:** HIGH risks are **preventable** via wave scope discipline, Playbook 01-before-bind ordering, ATLAS-first enrollment, and mandatory STOP at Wave 1 gate — **not** indicators that Wave 1 should be delayed.

---

## Exit Criteria

### Wave 1 is officially complete when ALL conditions are true

| # | Exit condition | Evidence |
|---|----------------|----------|
| E-W1-1 | **Gate 0** and **Gate 1** satisfied (or explicitly waived only where doctrine permits) | Operator attestation log |
| E-W1-2 | **Creation inventory mandatory classes** materialized per pilot | Physical records in LOC-ZONE |
| E-W1-3 | **C2** demonstrated — substrate readable/writable for pilot | Operator verify |
| E-W1-4 | **C3** demonstrated — MOC-01 anchor + MRDY categories bound | R-M* checklist pass |
| E-W1-5 | **Wave 1 exit gate** W1-G1…W1-G10 satisfied | Operator verification |
| E-W1-6 | **Excluded classes absent** — no ROC, SOC, POC-03…08 | Scope audit |
| E-W1-7 | **Dependency order respected** — enrollment before bind; substrate before manifest | Sequence audit |
| E-W1-8 | **Explicit STOP** documented — Wave 2 not begun without separate authorization | Execution log |

### Wave 1 exit is NOT conditioned on

| Not required | Reason |
|--------------|--------|
| C4 registry visibility | Wave 2 |
| C5 surface visibility | Wave 2 |
| POC-03…05 index loci | Wave 2 |
| Playbook 02 enrollment | Wave 2 |
| S1 full MVP path | Wave 3 |
| Git commit of operational zone | DF-10 operator policy |
| Mechanical ATLAS integration | Deferred per topology decision |
| Second pilot project | Optional generality |

### Exit diagram

```text
  Wave 1 Bootstrap Execution
       │
       ├── Pre-W1 gates (G0, G1)
       ├── Steps 1–11 (substrate + manifest bind)
       ├── R-M* verify (Step 12)
       └── W1-G1…G10 pass (Step 13)
                 │
                 ▼
  Wave 1 OFFICIALLY COMPLETE ── STOP ──▶ await Wave 2 authorization
```

---

## Wave 2 Entry Conditions

Wave 2 (**Portfolio & Visibility Scaffold** — RT-G05 + index scaffold + RT-G12) **may begin** only when Wave 1 exit criteria E-W1-1…E-W1-8 are met.

### What Wave 2 may assume after Wave 1

| # | Assumption | Source |
|---|------------|--------|
| A-W2-1 | **LOC-ZONE** exists and is stable Factory SoT boundary | Wave 1 E-W1-2 |
| A-W2-2 | Pilot **LOC-HOME** with **POC-01** identity shell exists | Wave 1 |
| A-W2-3 | **MOC-01** is stable, discoverable entry anchor | Wave 1 E-W1-4 |
| A-W2-4 | **POC-02(m)** manifest facet populated with MRDY categories | Wave 1 |
| A-W2-5 | **MOC-08** + **POC-09** declare topology target paths for index loci | Wave 1 — even if targets empty |
| A-W2-6 | **MOC-10** links physical bind to Playbook 01 enrollment act | Wave 1 |
| A-W2-7 | **ATLAS refs** in MOC-12 when known — pilot identity discipline established | Wave 1 |
| A-W2-8 | Serialization convention locked and proven on manifest bind | Gate 1-1 |
| A-W2-9 | **No** registry or surface artifacts exist yet — clean Wave 2 start | Wave 1 scope audit |

### What Wave 2 must still establish (not assumed from Wave 1)

| # | Wave 2 obligation | Track |
|---|-------------------|-------|
| B-W2-1 | Playbook 02 doctrinal registry-enrolled | Playbook 02 |
| B-W2-2 | Registry bind: POC-02(r), ROC-01…ROC-09 | RT-G05 |
| B-W2-3 | ROC-05 → MOC-01 pointer chain | RT-G05 |
| B-W2-4 | Index scaffold: POC-03…POC-05 (empty OK at NEW_PROJECT) | RT-G04 |
| B-W2-5 | Surface read bind: SOC-01…SOC-08 | RT-G12 |
| B-W2-6 | DF-07 form factor chosen for SOC read bind | Operator choice |
| B-W2-7 | Gate 2 readiness (G2-1…G2-5 per Creation Strategy) | Pre-W2 verification |

### Wave 2 forbidden assumptions

| Forbidden assumption | Why |
|---------------------|-----|
| POC-03…07 populated with declaration data | Wave 3 — Playbook 04 |
| Playbook 03 sessions completed | Wave 3 |
| C6/C7 satisfied | Wave 3 |
| MVP declared complete | Era exit — after Wave 3 + S1–S9 |

---

## Creation Authorization Review

### Authorization chain

| Level | Status | Notes |
|-------|--------|-------|
| Physical Artifact Specification Era | **COMPLETE** | Consolidation Review |
| Physical MVP Artifact Creation Era | **AUTHORIZED** | Strategy definition complete |
| Wave 1 Bootstrap Execution | **PLANNED** (this document) | **Does not authorize disk writes** |
| Physical disk writes | **PENDING** | Requires Gate 0-3 separate operator act |
| Wave 2 execution | **NOT AUTHORIZED** | Awaits Wave 1 exit + separate task |

### Remaining owner / operator decisions

| # | Decision | Blocks Wave 1? | Owner |
|---|----------|----------------|-------|
| D-01 | **Explicit operator authorization** for physical creation (Gate 0-3) | **Yes** | Factory program operator |
| D-02 | **Serialization convention lock** — format + COL-* layout (Gate 1-1) | **Yes** | Operator workshop |
| D-03 | **Pilot confirmation** — Triumph/Манипулятор vs synthetic | **Recommended, not blocking** if Core 5 LANDING chosen | Operator |
| D-04 | **MOC-06** `site_type_code` value at bind — LANDING for recommended pilot | **No** — expected default for Core 5 | Operator at bind |
| D-05 | **DF-07** SOC form factor | **No** — Wave 2 decision | Operator |
| D-06 | **DF-08** pilot workspace pointer policy detail | **No** — pointer path sufficient for Wave 1 | Operator |
| D-07 | **DF-09/10** internal layout / git policy for operational zone | **No** — not Wave 1 gate | Operator |
| D-08 | **Git commit** of operational zone | **No** — operator policy | Operator |

### ОБРАТИ ВНИМАНИЕ — ТЫ НУЖЕН

**Not required for this plan.**

Per Consolidation Review and Creation Strategy: no DF-* decision **truly blocks** Wave 1 bootstrap once operator authorization (D-01) and serialization lock (D-02) are obtained at execution time. Marker **ОБРАТИ ВНИМАНИЕ — ТЫ НУЖЕН** applies **only** if a decision blocks the immediate next authorized step — **not** the case for Wave 1 planning.

**Normative discipline (not a blocker):** D-01 and D-02 **must** be resolved by operator **at execution**, not retroactively waived.

---

## Explicit Non-Claims

This execution plan **does not** claim:

- Any **physical artifact**, folder, manifest record, registry entry, tracking record, surface bind, or ATLAS binding **was created** — plan only.
- `workspaces/website-factory-operations/` **exists** on disk — verified **absent**; creation awaits separate execution task with Gate 0-3 authorization.
- Wave 1 **has been executed**, **completed**, or **verified** — only **planned**.
- Serialization format, internal folder layout, DF-08/09/10 **resolved** — assigned to execution-time operator choice.
- **C4**, **C5**, **C6**, **C7**, or full **S1–S9** MVP success **achieved** — Wave 1 targets **C2 + C3 only**.
- Website Factory **runtime**, workflow engine, automation, validator engine, or operator dashboard **exist** or **were designed** in this deliverable.
- Mechanical ATLAS integration **is Wave 1-required** — refs are convention-only per Adoption Statement.
- ORG-0004 / PRJ-0008 / WEB-0009 are **live attested canonical on a runtime ATLAS service** — documentation-level verification only (**SAFE UNKNOWN** for live service).
- ATLAS C2+ consumer certification **achieved** — C1 attestation only.
- This plan **authorizes** disk writes — **separate operator authorization** required per Gate 0-3.
- Any **git commit, push, tag, or branch** was performed.
- Accepted architecture, specifications, playbooks, or doctrine **were modified** — planning deliverable only.

This plan **does** claim (evidence-based):

- Wave 1 scope, inventory, sequence, gates, and exit criteria **derive from** accepted Creation Strategy, RT-G04/RT-G10 Physical Artifact Specifications, MVP Definition Review, and ATLAS Adoption Statement **without contradiction**.
- Recommended pilot **ORG-0004 / PRJ-0008 / WEB-0009** is **consistent** with ATLAS population documentation and preferred over synthetic alternative.
- Wave 1 proves **C2 + C3**; Wave 2 entry conditions and assumptions are **defined**.
- Remaining blocking decisions at execution are **D-01** (operator authorization) and **D-02** (serialization lock) only.
- Marker **ОБРАТИ ВНИМАНИЕ — ТЫ НУЖЕН** is **not required** for proceeding to Wave 1 execution authorization.

Human-operated declaration path (Playbook 04 DA-01, OA-ACT-04) remains the v1 normative model — **not in Wave 1 scope**.

---

*Website Factory Wave 1 Bootstrap Execution Plan v1 — execution planning only. Canonical location: `workspaces/website-factory-reference-v1/WAVE-1-BOOTSTRAP-EXECUTION-PLAN-v1.md`. Git: no commit, no push.*

---

# REPORT — Wave 1 Bootstrap Execution Plan v1

**Stage:** Physical MVP Artifact Creation Era — Wave 1 Execution Planning  
**Deliverable:** `workspaces/website-factory-reference-v1/WAVE-1-BOOTSTRAP-EXECUTION-PLAN-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/WAVE-1-BOOTSTRAP-EXECUTION-PLAN-v1.md` (created)  
**Summary:** Определён Wave 1 Bootstrap Execution Plan: scope (RT-G04 + RT-G10, C2/C3 only), pilot ORG-0004/PRJ-0008/WEB-0009, creation inventory (mandatory/conditional/optional/excluded), 13-step execution sequence, readiness gates, success criteria, risk review, exit criteria, Wave 2 entry conditions, authorization review — без создания артефактов, папок, записей и bindings.  
**Git:** no commit, no push (per task).  
**UNKNOWN:** live attestation status ATLAS records on runtime service; operator calendar for Wave 1 physical execution; exact serialization format choice (D-02, execution-time).
