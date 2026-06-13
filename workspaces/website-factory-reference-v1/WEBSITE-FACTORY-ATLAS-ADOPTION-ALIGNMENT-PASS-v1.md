# REPORT — Website Factory ATLAS Adoption Alignment Pass v1

**Дата:** 2026-06-07  
**Тип:** adoption alignment pass only — **без** Creation Era, **без** physical artifact creation, **без** runtime, **без** redesign ATLAS или Factory  
**Область:** Website Factory (`workspaces/website-factory-reference-v1/`) ↔ ATLAS (`projects/atlas/`)  
**Upstream:** [WEBSITE-FACTORY-ATLAS-INTEGRATION-AUDIT-v1.md](WEBSITE-FACTORY-ATLAS-INTEGRATION-AUDIT-v1.md)  
**Reviewed (conditional update):** [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md)

**Repo evidence:** оба корпуса — **documentation-first**; shipped Website Factory runtime и ATLAS runtime/API **отсутствуют** в репозитории.

---

## Executive Summary

**Вердикт alignment pass:** Website Factory **семантически aligned** с ATLAS ownership model на уровне архитектуры (Engine boundary, physical artifact classes, consumer contract by design). **Документально не fully aligned** — пять рекомендаций audit RC-01…RC-05 **не закрыты** в Factory canon; drift-риск остаётся **операционным**, не архитектурным.

| Вопрос | Ответ |
|--------|-------|
| Factory fully aligned с ATLAS? | **Нет — conditional; gaps документируемы** |
| Creation Era may begin? | **Да — conditional GO** (как в audit) |
| Updates required? | **Да — 5 items; none BLOCK** |
| Affected docs edited in this pass? | **Нет** — gaps зафиксированы; правки отложены как targeted follow-up |

**ATLAS остаётся canonical owner:** Organization, Person, Website, Domain, ATLAS Project, Relationship, client reality (Organization + relationship edge).

**Factory остаётся owner:** Factory Project, lifecycle state, gates, handoffs, tracking, production artefact refs, Legal Entity Card (production scope only).

**Highest residual risk:** Legal Entity Card vs Counterparty Card (RC-02) — параллельный capture org-фактов без crosswalk.

---

## RC-01 Review

**Audit requirement:** Normative **ATLAS reference binding convention** для charter / MOC-12 / POC-09 — field names, optional vs mandatory when ids known, SAFE UNKNOWN handling.

### Current state

| Location | ATLAS-specific discipline | Status |
|----------|---------------------------|--------|
| Integration Audit | Recommends `atlas_project_ref`, `atlas_website_ref`, `atlas_client_org_ref`, `atlas_domain_ref` | **Illustrative only — not normative in Factory canon** |
| Manifest Charter Category 7 | External refs topology — no ATLAS naming | **Implicit via external-ref pattern** |
| RT-G10 Physical Spec MOC-12 | Topology target locators; POC-09 discipline | **Aligned structurally; ATLAS not named** |
| Enrollment Workflow | No ATLAS ref fields at bind | **Gap** |
| Operational Model | No ATLAS ref convention | **Gap** |

### Evaluation

| Criterion | Satisfied? |
|-----------|------------|
| Physical specs support external refs (MOC-12, POC-09) | **Yes** |
| Normative field names for ATLAS ids | **No** |
| Mandatory vs optional when active canonical exists | **No** |
| SAFE UNKNOWN when ownership uncertain (IGV 9.3) | **No — not in Factory playbooks** |

### Proposed convention (for adoption — not yet in canon)

```text
Charter / MOC-12 / POC-09 ATLAS reference fields (when binding):

  atlas_client_org_ref     → ORG-*   (commissioning / client organization)
  atlas_website_ref        → WEB-*   (structural website identity)
  atlas_project_ref        → PRJ-*   (structural ATLAS project — NOT Factory Project id)
  atlas_domain_ref         → DOM-*   (when domain identity relevant)

Disposition:
  • When active attested canonical exists → field SHOULD be populated (ref only)
  • When unknown or disputed → explicit SAFE UNKNOWN; MUST NOT invent OWNER/ORG
  • When no ATLAS population yet → field absent or marked proposed; MUST NOT fork parallel registry
  • Factory Project identity (MOC-02) MUST remain distinct from atlas_project_ref
```

**RC-01 status:** **NOT SATISFIED** — convention documented in this pass; **requires propagation** to Manifest Charter Category 7, RT-G10 MOC-12 obligations, Playbook 01 bind checklist.

---

## RC-02 Review

**Audit requirement:** Document **Legal Entity Card ↔ ATLAS Counterparty Card crosswalk** — evidence flow CC → ATLAS proposal; LEC → legal production; LEC should cite `ORG-*` + `evidence_ref` when attested.

### Current state

| Artifact | Authority claim | ATLAS link |
|----------|-----------------|------------|
| Legal Entity Card (`legal-entity/LEGAL-ENTITY-CARD-v1.md`) | «Primary source of truth» for **legal production workflow** | **No `ORG-*`, no Counterparty Card crosswalk** |
| ATLAS Counterparty Card (`ATLAS-COUNTERPARTY-CARD-MODEL-v1.md`) | Evidence artifact — **not canonical record** | Canonical org = `ORG-*` after attestation |
| Integration Audit | Identifies D-03 HIGH drift risk | Crosswalk recommended |

### Evaluation

| Criterion | Satisfied? |
|-----------|------------|
| LEC scoped to production (not business registry) | **Yes — in card purpose and audit** |
| Explicit crosswalk LEC ↔ CC ↔ ORG-* | **No** |
| LEC cites `ORG-*` when attested | **No field in schema** |
| Evidence tier / `evidence_ref` to Counterparty Card | **No** |

### Required crosswalk (proposed)

```text
Counterparty Card (ATLAS evidence)
       │ propose / attest
       ▼
ORG-* (ATLAS canonical) ◀──ref── Legal Entity Card (Factory production)
       │
       └── LEC holds production fields for templates; ORG-* wins on identity conflict
```

**RC-02 status:** **NOT SATISFIED** — highest drift risk; update target: `legal-entity/LEGAL-ENTITY-CARD-v1.md` (+ optional `LEGAL-ENTITY-DISCOVERY-RULES-v1.md` pointer). **Not in conditional-review list** — listed as Required Update, not edited in this pass.

---

## RC-03 Review

**Audit requirement:** Terminology guard in Factory onboarding: «Factory Project ≠ ATLAS Project»; «Factory Registry ≠ ATLAS Registry»; «Site Type Registry ≠ Business Reality Registry».

### Current state

| Guard | Where expressed | Status |
|-------|-----------------|--------|
| Site Type Registry ≠ Factory Project Registry | **RAP-11** across Registry charter, RT-G05, Operational Model §Excluded | **Satisfied** |
| Factory Project ≠ ATLAS Project | Integration Audit only; Object Model uses «Factory Project» without ATLAS homonym note | **Partial** |
| Factory Registry (ROC) ≠ ATLAS Business Reality Registry | Audit terminology table; RAP-11 covers Site Type only | **Partial** |
| Onboarding / Playbook 01 | MRDY-07 Manifest ≠ Passport ≠ Registry; **no ATLAS homonyms** | **Gap** |

### Evaluation

| Criterion | Satisfied? |
|-----------|------------|
| Site Type vs Factory Registry guard | **Yes (RAP-11)** |
| Factory Project vs ATLAS Project | **No in Factory onboarding canon** |
| Factory ROC vs ATLAS Registry | **No explicit guard in reviewed docs** |
| Consolidated terminology guard section | **No** |

**RC-03 status:** **PARTIALLY SATISFIED** — RAP-11 covers one of three homonyms; **requires** short terminology guard block in Operational Model and/or Playbook 01 (MRDY-07 extension or parallel attestation).

---

## RC-04 Review

**Audit requirement:** Create `ATLAS-ADOPTION-STATEMENT` for Website Factory per `ATLAS-CONSUMER-CERTIFICATION-v1.md` (C1→C2 checklist).

### Current state

| Criterion (C1) | Evidence in Factory canon |
|----------------|---------------------------|
| C0 — Aware, no parallel canonical list | Engine boundary EO-02; audit confirms no fork authorization |
| Adoption owner named | **Not named** |
| Semantic contract accepted | Implied by audit; **no explicit acceptance artifact** |
| Phase 4 consumer contracts acknowledged | Audit cites §8.3; **not in Factory charter** |
| No MAP-B01–B09 in design | **Not formally attested** |
| Business Scope ≠ identity partition | **Not stated** |

**Adoption level (audit):** **C1** (documented consumer) — target C1→C2.

### Evaluation

| Criterion | Satisfied? |
|-----------|------------|
| Semantic alignment by architecture | **Yes** |
| Dedicated ATLAS-ADOPTION-STATEMENT artifact | **No** |
| C1 checklist evidence bundle | **No** |
| C2 mapping table | **No** (expected later) |

**RC-04 status:** **NOT SATISFIED** — Factory operates at **implicit C1** via integration audit; **requires** `WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md` (or equivalent under Factory governance path) before C2 claims.

---

## RC-05 Review

**Audit requirement:** Playbook 01 enrollment checklist — verify ATLAS ids for client org / website / structural project **before** writing org-identifying fields into MOC-03 charter.

### Current state

| Playbook 01 step | ATLAS discipline |
|------------------|------------------|
| Factory-scoped recognition | No ATLAS lookup |
| MRDY-* evaluation | No ATLAS id verification |
| Manifest bind (RT-G10 MOC-03 scope) | Charter categories — **no ordering rule vs ATLAS refs** |
| IGV 9.3 / CC-02 operationalization | **Absent from enrollment workflow** |

### Evaluation

| Criterion | Satisfied? |
|-----------|------------|
| Enrollment precedes physical bind | **Yes (INT-M01, Playbook 01)** |
| ATLAS id lookup before org-identifying MOC-03 content | **No** |
| SAFE UNKNOWN on disputed ownership | **No explicit step** |
| Ref-first vs restate-as-authority | **No checklist item** |

### Proposed enrollment addendum (for adoption)

Before populating MOC-03 (or charter scope categories) with org-identifying facts (`legal_name`, `inn`, client org name as identity):

1. Check ATLAS population / steward for active `ORG-*`, `WEB-*`, `PRJ-*` for this case.  
2. If active canonical exists → bind refs in MOC-12 (RC-01 fields); MOC-03 carries **production scope**, not canonical identity.  
3. If unknown → **SAFE UNKNOWN**; do not invent OWNER or parallel org registry row.  
4. Legal Entity Card creation follows RC-02 crosswalk — production input, not registry entry.

**RC-05 status:** **NOT SATISFIED** — requires Playbook 01 update and alignment with RT-G10 bind checklist (R-M3 area).

---

## Required Updates

Priority follows audit severity (REC/DOC); **none block Creation Era**.

| ID | Update | Target document(s) | Severity | This pass |
|----|--------|-------------------|----------|-----------|
| **RC-01** | Add normative ATLAS ref field convention (see RC-01 Review) | Manifest Charter §Category 7; RT-G10 MOC-12 / OBL-M-12; optional `WEBSITE-FACTORY-ATLAS-REFERENCE-CONVENTION-v1.md` | REC | **Deferred** — convention defined here |
| **RC-02** | LEC ↔ Counterparty Card crosswalk; optional `atlas_org_ref`, `counterparty_evidence_ref` on LEC | `legal-entity/LEGAL-ENTITY-CARD-v1.md`, Discovery Rules | REC | **Deferred** |
| **RC-03** | Terminology guard block (three homonyms) | Operational Model §Operational Boundaries; Playbook 01 MRDY-07 or new **TG-ATLAS-*** principles | DOC | **Deferred** |
| **RC-04** | ATLAS Adoption Statement (C1 attestation + owner + semantic contract link) | `WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md` (new) | DOC | **Deferred** |
| **RC-05** | Pre-MOC-03 ATLAS id verification checklist | `FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md`; RT-G10 R-M3 bind checklist cross-ref | REC | **Deferred** |

### Reviewed documents — update decision

| Document | Update required? | Rationale |
|----------|------------------|-----------|
| FACTORY-OPERATIONAL-MODEL-v1.md | **Yes (RC-03, RC-04 pointer)** | No ATLAS boundary section; RAP-11 alone insufficient |
| FACTORY-PROJECT-MANIFEST-CHARTER-v1.md | **Yes (RC-01)** | Category 7 lacks ATLAS ref naming |
| FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md | **Yes (RC-05, RC-03)** | No ATLAS verification before scope/org categories |
| RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md | **Yes (RC-01, light)** | MOC-12 aligned implicitly; ATLAS field names absent |

**Why not edited in this pass:** Task scope = alignment **evaluation** + single deliverable; proposed text captured above and in RC sections for **targeted follow-up** without multi-file churn in one pass.

---

## Final Recommendation

### Alignment status

| Dimension | Status |
|-----------|--------|
| Architectural / semantic boundaries | **Aligned** |
| ATLAS canonical ownership explicit in Factory canon | **Partial** — implicit via Engine + audit |
| RC-01…RC-05 closed | **No — 0/5 fully satisfied; 1/5 partial (RC-03)** |
| Documentation adoption level | **Implicit C1** — formal C1 artifact pending (RC-04) |

### Decision

| Criterion | Result |
|-----------|--------|
| Factory fully aligned with ATLAS? | **No — conditional; gaps are document/operator discipline, not architecture** |
| Creation Era may begin? | **YES — conditional GO** |
| Blockers? | **None** |
| Sequencing | Creation Era authorized; RC-01/02/05 at **first physical bind**; RC-03/04 in **parallel documentation** |

### Conditional GO (unchanged from audit)

1. First physical records = Factory classes (POC/MOC/ROC/SOC) + **refs** to ATLAS ids — **not** canonical registry rows.  
2. When active ATLAS canonical exists → charter/MOC-12 **should reference** `ORG-*` / `WEB-*` / `PRJ-*` — not restate as authoritative identity.  
3. Legal Entity Card follows RC-02 crosswalk — production input, not business registry entry.  
4. Uncertain domain/org ownership → **SAFE UNKNOWN** (IGV 9.3) — no invented OWNER to unblock export.

### Recommended next actions (ordered)

1. Create `WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md` (RC-04).  
2. Add ATLAS reference convention to Manifest Charter + RT-G10 MOC-12 (RC-01).  
3. Add Playbook 01 pre-MOC-03 checklist (RC-05).  
4. Add LEC ↔ Counterparty Card crosswalk (RC-02).  
5. Add terminology guard TG-ATLAS-* to Operational Model + Playbook 01 (RC-03).

---

## Explicit Non-Claims

This alignment pass **does not** claim:

- Website Factory **runtime**, `website-factory-operations/`, or physical MOC/POC records **exist** on disk  
- ATLAS **runtime**, API, or live attestation service **exist** in-repo  
- RC-01…RC-05 have been **implemented** in Factory canon — evaluated and partially specified in this pass only  
- Triumph/manipulator wave records are **live attested canonical** on a service — population docs are documentation-level  
- Legal Entity Card and Counterparty Card **are synchronized** automatically  
- MVP **requires** mechanical ATLAS integration — explicitly deferred per topology decision  
- This pass **authorizes** physical creation under `website-factory-operations/` — separate authorization  
- Reviewed Factory documents were **modified** — evaluation only  
- Any **git commit or push** was performed  

**SAFE UNKNOWN:**

- Whether operators maintain ad-hoc manifest/registry files with org facts instead of ATLAS refs  
- Exact serialization of `atlas_*_ref` fields in MOC-12 — deferred to Creation Era operator choice under class separation  
- External Counterparty Card storage at `C:\AI MARS STORAGE\atlas\evidence\` — referenced by ATLAS, not verified in this pass  

---

*Website Factory ATLAS Adoption Alignment Pass v1 — evaluation and convention capture only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-ATLAS-ADOPTION-ALIGNMENT-PASS-v1.md`. Git: no commit, no push.*
