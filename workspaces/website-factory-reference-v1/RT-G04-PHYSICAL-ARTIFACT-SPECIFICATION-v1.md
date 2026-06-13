# REPORT — RT-G04 Physical Artifact Specification v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical Artifact Specification Era — **RT-G04 physical artifact specification only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE** (RT-G04, RT-G10, RT-G05, RT-G12); Physical MVP Artifact Definition **COMPLETE**; RT-G04 Physical Artifact Specification Review **COMPLETE**  
**Тип:** physical artifact specification only — **без** artifact creation, folder creation, file creation, serialization format, naming conventions, schemas, layout design, runtime, automation, workflow engine  
**Upstream:** [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md), [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md), [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-REVIEW-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-REVIEW-v1.md)  
**Also reviewed:** [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), Operational Playbooks 01–05  
**Связь:** [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md), [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md), [RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md](RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md)

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |

---

## Purpose

### Зачем существует RT-G04 Physical Artifact Specification

**RT-G04 Physical Artifact Specification v1** переводит принятые implementation и review артефакты в **полную нормативную модель физической реальности** persistence substrate — определяя **что физически существует**, **что авторитетно**, **как классы связаны**, **какие обязательства и гарантии** substrate несёт для downstream standards — **без** создания артефактов на диске и **без** выбора serialization format.

| Upstream отвечает | Эта specification отвечает |
|-------------------|---------------------------|
| Implementation Standard — **классы** и **implementation obligations** | **Физическая модель** классов как normative artifact reality |
| Physical MVP Definition Review — **Wave 1 inventory** (POC/MOC/ROC/SOC) | **RT-G04 scope only** — LOC-*, POC-* и их физические обязательства |
| Specification Review — **авторизация** концептуальной модели | **Завершённая specification** artifact class model, authority, relationships, guarantees |
| RT-G10/05/12 standards — serialization **внутри** facets | **Handoff assumptions** substrate → downstream **без** serialization design |

### Нормативная формулировка physical artifact responsibility

**RT-G04 Physical Artifacts (MVP specification)** — **авторизованный file-backed physical layer** в `workspaces/website-factory-operations/` (LOC-ZONE), содержащий **structured filesystem records** нормативных классов LOC-ZONE, LOC-HOME, POC-01…POC-10 и опциональных POC-D1, POC-O1, POC-O2, которые operator **читает и вручную обновляет** для поддержки Playbooks 01→05 и capability floor C2 — **без** shipped runtime, **без** automated index mutation и **без** определения формата сериализации (территория отдельных specification tracks или downstream standards).

### Specification purpose statement

Physical artifact specification **материализует** единую физическую модель (TR-01, C2), на которой:

1. **LOC-ZONE** и **LOC-HOME** определяют infrastructure loci для portfolio и project scope.
2. **POC-01…POC-10** определяют authoritative persistent record classes с явными lifecycle triggers.
3. **POC-02** hosts manifest и registry **facets** как separate binding carriers — content populated by RT-G10/05.
4. **POC-D1, POC-O1, POC-O2** определяют derived и operational classes с subordinate authority.
5. **Physical obligations и guarantees** формализуют минимум для valid Factory Project и downstream handoff.

Specification **не создаёт** physical artifacts — она **определяет физическую реальность**, которую authorized creation track должен реализовать.

---

## Foundation Dependencies

Specification **наследует** upstream артефакты **без их переопределения**.

### Tier 0 — Implementation standard and reviews

| Document | Specification использует |
|----------|-------------------------|
| [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md) | POC-01…POC-10 taxonomy; P1–P8; persistence categories; integrity; boundary protection; H-01…H-10 |
| [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-REVIEW-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-REVIEW-v1.md) | LOC-ZONE, LOC-HOME; REL-01…13; scope split; authority model; authorization verdict |
| [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md) | Wave 1 POC disposition; mandatory/optional/forbidden; creation sequence phases A–F |
| [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) | P1–P8 charter obligations; reality model; authorized zone doctrine |

### Tier 1 — MVP and topology context

| Document | Specification использует |
|----------|-------------------------|
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C2–C7 capability floor; S1–S9 success classes; MVP purpose |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-01/02/03/06; structured artifacts without format choice |
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; single operator; human-operated writes |

### Tier 2 — Operational playbooks (lifecycle triggers)

| Playbook | Specification использует |
|----------|-------------------------|
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — enrollment precedes physical bind |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — declared catalog enrollment |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — read-only session; SRDY assessment |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — DA-01 sole declarer; index writes |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — terminal metadata persistence |

### Tier 3 — Downstream standards (facet content owners)

| Standard | Constraint on RT-G04 specification |
|----------|-----------------------------------|
| RT-G10 Manifest Implementation Standard | MOC-* content **within** POC-02 manifest facet — not RT-G04 storage design |
| RT-G05 Registry Implementation Standard | ROC-* content **within** POC-02 registry facet at portfolio scope |
| RT-G12 Surface Read Binding Standard | SOC-* read composition — **references** POC-*; not RT-G04 storage |

**Authority precedence:** Foundation Freeze + Engine → Manifest/Registry/Surface charters → RT-G04 Charter → Implementation Standard → **эта specification** → physical creation (separate authorization) → RT-G10/05/12 physical specification tracks (separate deliverables).

**Scope boundary (SPEC-SCOPE-01):** Эта specification covers **RT-G04 classes only** — LOC-ZONE, LOC-HOME, POC-01…POC-10, POC-D1, POC-O1, POC-O2. MOC-*, ROC-*, SOC-* physical specification belongs to **separate standard-specific tracks** hosted within or reading from POC-02 facets.

---

## Artifact Class Model

Normative **classes** — не file names, не schemas, не folder trees, не serialization labels.

### Infrastructure loci

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **LOC-ZONE** | **Authorized zone** | Bounded Factory SoT filesystem root at `workspaces/website-factory-operations/` (DF-03) | Hosts **all** Factory SoT structured records; portfolio root; boundary against monorepo scatter | **Must exist** before any POC class materialization |
| **LOC-HOME** | **Per-project record home** | Exactly one discoverable physical locus per Factory Project identity (P1) | Container for project-scope POC-01…POC-10; stable identity binding; no competing homes | **Must exist** per manifest-bound project |

### Authoritative persistent classes (POC-01…POC-10)

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **POC-01** | **Identity** | Stable Factory Project identity shell bound to LOC-HOME | Anchors logical Factory Project to physical locus; survives across playbooks | **Must persist** |
| **POC-02** | **Binding** | Manifest and registry binding **carriers** — separate facets, same class ID | **Hosts** RT-G10 MOC-* (manifest facet) and RT-G05 ROC-* (registry facet); carrier existence ≠ content authority | **Must persist** (when bound) |
| **POC-03** | **State** | Active state instance + declared state history | Reflects last Playbook 04 declared state; not inferred automation | **Must persist** |
| **POC-04** | **Gate** | Gate outcome index — observed PASS/FAIL/BLOCKED outcomes | Records **outcomes**, not criteria definitions | **Must persist** |
| **POC-05** | **Handoff** | Handoff event index + package refs | Records **events/refs**, not payloads | **Must persist** |
| **POC-06** | **Declaration** | Append-only operator declaration records and reconciliation acts | Authoritative declaration truth trail; Playbook 04 only | **Must persist** |
| **POC-07** | **Ledger** | Progression ledger / audit trail linking declarations to index mutations | Append-only audit; links POC-06 acts to POC-03…05 mutations | **Must persist** |
| **POC-08** | **Closure** | Factory-terminal / partial / suspended outcome metadata | Terminal outcome binding to existing POC-01; Playbook 05 only | **Must persist** (when Playbook 05 executed) |
| **POC-09** | **Reference** | External workspace, layer body, handoff payload, Runtime doc pointers | Locator + role label only; never embeds external bodies | **Must persist** (refs only) |
| **POC-10** | **Audit** | Last declaration recency markers; session outcome refs for SRDY-07 | Recency honesty for Surface; not session notes authority | **Must persist** |

### Optional / subordinate classes

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **POC-D1** | **Derived cache** | Eligibility snapshots, SRDY pass/fail views, registry orientation summaries | Operator convenience; regeneratable from POC-03…07 | **Optional** — non-authoritative |
| **POC-O1** | **Operational note** | Pre-declaration Playbook 03 session notes | Session-local material; never substitutes POC-06 | **Optional** — non-authoritative |
| **POC-O2** | **Enrollment draft** | Pre-bind enrollment decision notes before RT-G10 physical bind | Supports OQ-ME05; not blocking for bind | **Optional** — non-authoritative |

### Class composition model (conceptual — not layout)

```text
  workspaces/website-factory-operations/          ← LOC-ZONE (portfolio root)
  │
  ├── portfolio scope
  │     └── POC-02 registry facet                 ← binding carrier; ROC-* = RT-G05 content
  │
  └── per-project record home (LOC-HOME)          ← one per Factory Project
        ├── POC-01 identity
        ├── POC-02 manifest facet                 ← binding carrier; MOC-* = RT-G10 content
        ├── POC-03 state instance + history
        ├── POC-04 gate outcome index
        ├── POC-05 handoff event index
        ├── POC-06 declaration records
        ├── POC-07 progression ledger
        ├── POC-08 closure metadata               ← on Playbook 05
        ├── POC-09 external ref index
        ├── POC-10 audit / recency markers
        ├── POC-D1 derived cache (optional)
        ├── POC-O1 session notes (optional)
        └── POC-O2 enrollment draft (optional)
```

### Class principles

| ID | Principle |
|----|-----------|
| **POC-RULE-01** | Каждый Factory Project с physical binding **must have exactly one** discoverable LOC-HOME (P1) |
| **POC-RULE-02** | POC-02 manifest facet and POC-03…POC-07 tracking indexes **remain separate record classes** — substrate **must not** collapse into undifferentiated mega-record (MT-01, MAP-01) |
| **POC-RULE-03** | POC-02 manifest facet (project scope) and POC-02 registry facet (portfolio scope) **remain separate facets** — same class ID, distinct loci and content owners |
| **RTG04-CLASS-01** | RT-G04 specification covers **POC-* and infrastructure loci only** — MOC/ROC/SOC physical shape deferred to downstream specification tracks |

### Charter obligation → physical class mapping

| Charter obligation | Physical classes |
|--------------------|------------------|
| P1 Per-project physical locus | LOC-HOME (container for POC-01…POC-10) |
| P2 Manifest binding carrier | POC-02 manifest facet + POC-01 |
| P3 Registry catalog carrier | POC-02 registry facet at portfolio scope |
| P4 Tracking instance records | POC-03, POC-04, POC-05, POC-09 (artefact refs), POC-10 |
| P5 Declaration writes | POC-06, POC-07; mutates POC-03…POC-05 |
| P6 Closure records | POC-08 |
| P7 Append-only honesty | POC-06, POC-07 — immutable event semantics |
| P8 External ref discipline | POC-09 — pointers only |

---

## Authority Model

### Four persistence categories (implementation terms)

| Category | RT-G04 classes | Authority rule |
|----------|----------------|----------------|
| **Persistent authoritative** | POC-01…POC-10 | Must survive between sessions; loss breaks Playbooks 03/04/05 or Surface questions without workspace archaeology |
| **Derived** | POC-D1 | Regeneratable from persistent records + Runtime vocabulary; subordinate to POC-03…07, POC-06 |
| **Reference-only bodies** | External loci pointed by POC-09 | Bodies live **outside** LOC-ZONE; POC-09 stores locator + role only |
| **Operational / transient** | POC-O1, POC-O2 | Pre-declaration / pre-bind; **must not** mutate POC-03…07 without Playbook 04 |

### Authority matrix by class

| Class | Authoritative for | Not authoritative for | Write authority |
|-------|-------------------|----------------------|-----------------|
| **LOC-ZONE** | Factory SoT boundary existence | Per-project tracking content | Operator authorization + RT-G04 creation act |
| **LOC-HOME** | Per-project locus discoverability | Manifest categories; tracking state | Playbook 01 bind + RT-G10 |
| **POC-01** | Factory Project identity binding to locus | Manifest categories; tracking state | Playbook 01 bind + RT-G10 |
| **POC-02 (manifest facet)** | Manifest binding **carrier existence** | MOC-* content authority → RT-G10 | RT-G10 bind act |
| **POC-02 (registry facet)** | Catalog binding **carrier existence** | ROC-* content authority → RT-G05 | RT-G05 bind act |
| **POC-03** | Active state + declared history | Gate criteria; manifest scope tier | Playbook 04 only (DA-01) |
| **POC-04** | Gate **outcomes** observed | Gate **criteria** definitions | Playbook 04 only |
| **POC-05** | Handoff **events/refs** | Handoff **payloads** | Playbook 04 only |
| **POC-06** | Declaration truth trail | — | Playbook 04 only |
| **POC-07** | Progression audit trail | — | Playbook 04 only |
| **POC-08** | Terminal closure outcome | Manifest enrollment revocation | Playbook 05 only |
| **POC-09** | External **locators** | External **bodies** | Operator maintains refs (all playbooks) |
| **POC-10** | Recency markers for SRDY-07 | Session notes authority | Playbooks 03–04 |
| **POC-D1** | — (derived views only) | Any declarer authority | Non-authoritative operator or tooling |
| **POC-O1, POC-O2** | — | Declaration or bind authority | Operator notes only |

### Authoritative vs derived vs operational vs reference — summary

| Disposition | Classes | Precedence when conflict |
|-------------|---------|-------------------------|
| **Authoritative** | POC-01…POC-10 | POC-06/POC-03 tail wins over all derived; last Playbook 04 wins for active POC-03…05 view |
| **Derived** | POC-D1 | Subordinate to POC-06, POC-03 (DR-02, INT-04) |
| **Operational** | POC-O1, POC-O2 | Never substitute POC-06 (LC-03, OR-02) |
| **Reference bodies** | External to zone | POC-09 identifies locus; broken refs visible; no silent copy (INT-05) |

### Authority precedence rules

| Rule ID | Precedence |
|---------|------------|
| **AUTH-01** | POC-06/POC-03 tail **wins over** POC-D1 (DR-02, INT-04, TV-02) |
| **AUTH-02** | POC-06/POC-07 **append-only** — corrections = new events, not silent delete (INT-01, P7) |
| **AUTH-03** | Last Playbook 04 act **wins** for POC-03…05 active view (INT-03) |
| **AUTH-04** | Manifest facet **must not** embed live gate index as second authoritative store (INT-06, MT-01) |
| **AUTH-05** | Registry facet **must not** embed full tracking depth (INT-07, RA-05) |
| **AUTH-06** | Only Factory operator (Playbook 04/05, OA-ACT-04) **authoritatively mutates** POC-03…07 |
| **AUTH-07** | RT-G12 **never writes** POC-03…07 — read-oriented only (OWN-03, TRK-REL-01) |
| **AUTH-08** | External systems **never mutate** indexes without operator act (SC-03) |

### Ownership summary

| Layer | Owns physical artifact reality | Does not own |
|-------|-------------------------------|--------------|
| **RT-G04 (this specification)** | LOC-ZONE, LOC-HOME; POC class taxonomy; zone discipline; P1–P8 hosting; integrity expectations | Serialization format; manifest MOC-* content; catalog ROC-* content; Surface SOC-* composition |
| **RT-G10** | MOC-* content within POC-02 manifest facet | Substrate zone topology; tracking indexes |
| **RT-G05** | ROC-* content within POC-02 registry facet | Per-project tracking depth |
| **RT-G12** | SOC-* read composition referencing POC-* | Any authoritative index write |

---

## Relationship Model

### Portfolio scope vs project scope

| Scope | Primary loci | RT-G04 artifacts | Content populated by |
|-------|--------------|-------------------|---------------------|
| **Portfolio** | LOC-ZONE root | POC-02 registry facet (binding carrier) | RT-G05 ROC-* within facet |
| **Project** | LOC-HOME within LOC-ZONE | POC-01, POC-02 manifest facet, POC-03…10, optional POC-D1/O1/O2 | RT-G10 MOC-* within manifest facet; operator Playbooks 04/05 for indexes |

### Portfolio-scope rules

| Rule ID | Rule |
|---------|------|
| **PS-01** | Exactly **one** canonical portfolio catalog binding locus at MVP — hosted in POC-02 registry facet |
| **PS-02** | Portfolio scope **does not** contain per-project tracking indexes (POC-03…POC-07) |
| **PS-03** | Portfolio scope **does not** answer eight Surface questions — portfolio select only |
| **PS-04** | LOC-ZONE **must not** expand to entire MARS monorepo (AZ-05) |
| **PS-05** | Registry facet **may exist without** any per-project homes — doctrinally valid; MVP Wave 1 demo track requires both |

### Project-scope rules

| Rule ID | Rule |
|---------|------|
| **PRJ-01** | Exactly **one** LOC-HOME per Factory Project identity — no competing homes |
| **PRJ-02** | All POC-01…POC-10 for a project **reside within** its LOC-HOME (co-location permitted at physical level) |
| **PRJ-03** | POC-02 manifest facet and POC-03…POC-07 **must remain distinct record classes** even when co-located |
| **PRJ-04** | Playbook 05 closure (POC-08) **binds to existing** LOC-HOME — no orphan records (LC-05) |
| **PRJ-05** | SOC-* read composition (RT-G12) **references** project-scope POC-* — SOC-* is **not** RT-G04 storage |

### Home composition

LOC-HOME **contains** for one Factory Project:

- POC-01 identity shell
- POC-02 manifest facet (hosts MOC-* — RT-G10)
- POC-03…POC-07 tracking indexes
- POC-08 closure (when Playbook 05 executed)
- POC-09 external ref index
- POC-10 audit/recency markers
- Optional POC-D1, POC-O1, POC-O2

LOC-HOME **does not contain**:

- POC-02 registry facet (portfolio scope only)
- Layer artefact bodies
- MOC-* or SOC-* as RT-G04-owned storage (MOC-* hosted **within** POC-02 manifest facet; SOC-* is read composition layer)

### Facet hosting

| Facet | Scope | Host class | Content owner | Separation rule |
|-------|-------|------------|---------------|-----------------|
| **Manifest facet** | Project (LOC-HOME) | POC-02 | RT-G10 MOC-* | Must not embed live POC-04/05 as authoritative second store |
| **Registry facet** | Portfolio (LOC-ZONE) | POC-02 | RT-G05 ROC-* | Must not embed full POC-03…07 tracking depth |

**Principle FACET-01:** POC-02 is one **class ID** with **two facets** — manifest (project) and registry (portfolio). Facets share class taxonomy but **must remain separate record classes** on disk (POC-RULE-02, POC-RULE-03).

### Cross-reference rules (REL-*)

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-01** | LOC-ZONE **contains** all POC-* classes | AZ-01 — no scattered Factory SoT |
| **REL-02** | LOC-HOME **contains** POC-01…POC-10 for one project | POC-RULE-01 — exactly one home per identity |
| **REL-03** | POC-02 manifest facet **hosts** MOC-* (RT-G10) | Substrate hosts carrier; RT-G10 serializes content |
| **REL-04** | POC-02 registry facet **hosts** ROC-* (RT-G05) | Portfolio scope; separate from manifest facet |
| **REL-05** | POC-02 facets **must remain separate record classes** | POC-RULE-02 — no mega-record |
| **REL-06** | POC-03…POC-05 **mutated by** Playbook 04 only | OWN-02, LC-04 |
| **REL-07** | POC-06/POC-07 **append-only**; POC-03…05 reflect last declaration | INT-01, INT-03 |
| **REL-08** | POC-09 **points to** external bodies — never embeds | RR-01…RR-04 |
| **REL-09** | POC-08 **references** POC-01 identity | INT-10 — no orphan closure |
| **REL-10** | POC-D1 **subordinate to** POC-03…POC-07 | INT-04, DR-02 |
| **REL-11** | RT-G12 **reads** POC-03…07, POC-10 — **never writes** | OWN-03, TRK-REL-01 |
| **REL-12** | ROC-05 (RT-G05) **points to** MOC-01 (RT-G10) via POC-02 facets | Cross-facet pointer; not RT-G04 content |
| **REL-13** | Class separation **mandatory** regardless of future co-location policy | COL-02…COL-04 — physical co-location permitted; class separation on disk mandatory |

### Lifecycle dependency graph

```text
  PRE-FACTORY (no zone)
       │
       ▼
  LOC-ZONE created ───────────────────────────── portfolio infrastructure
       │
       ▼
  Playbook 01 enrolled → RT-G10 bind
       │
       ├──▶ LOC-HOME + POC-01 + POC-02(m) + POC-09
       │
       ▼
  Playbook 02 enrolled → RT-G05 bind (optional doctrinal; mandatory MVP demo track)
       │
       └──▶ POC-02(r) at portfolio scope
       │
       ▼
  Playbook 04 declarations (repeat)
       │
       └──▶ POC-03…07, POC-06, POC-07, POC-10
       │
       ▼
  Playbook 05 closure
       │
       └──▶ POC-08
```

### Playbook → physical record interaction

| Playbook | Substrate interaction | Record classes touched |
|----------|----------------------|------------------------|
| **01** Manifest enrollment | Doctrinal enrollment precedes physical bind; RT-G10 creates POC-02 manifest + POC-01 on bind | POC-01, POC-02 (manifest), POC-09 — **on bind** |
| **02** Registry enrollment | Operator declares catalog entry; RT-G05 populates POC-02 registry facet | POC-02 (registry) — **requires** manifest anchor |
| **03** Surface session | **Reads** POC-03…07, POC-10; **may write** POC-O1 only; **must not** mutate indexes | Read POC-*; optional POC-O1 |
| **04** Project declaration | Operator **writes** POC-06, appends POC-07, **mutates** POC-03…05, updates POC-10 | POC-03…07, POC-10 |
| **05** Project closure | Operator **writes** POC-08; **does not revoke** manifest enrollment | POC-08 |

---

## Physical Obligations

### What must physically exist for a valid Factory Project

A **valid Factory Project with physical binding** requires satisfaction of obligations below. Obligations are **class-level** — not file counts or serialization shapes.

### Tier 0 — Zone infrastructure (C2)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-ZONE-01** | **LOC-ZONE** at `workspaces/website-factory-operations/` | Before any POC materialization |
| **OBL-HOME-01** | **LOC-HOME** — exactly one per Factory Project identity | Manifest bind (Playbook 01 + RT-G10) |

### Tier 1 — Identity and manifest binding (C3, S2)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-01** | **POC-01** identity shell bound to LOC-HOME | Manifest bind |
| **OBL-02** | **POC-02 manifest facet** as binding carrier | Manifest bind |
| **OBL-09** | **POC-09** topology refs pointing to index loci (even if empty) | Manifest bind |

**Doctrinal precondition (not a disk artifact):** Playbook 01 manifest-enrolled outcome **must precede** physical bind (LC-01, LC-06).

### Tier 2 — Registry catalog (C4, S3 — MVP demo track)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-02R** | **POC-02 registry facet** at portfolio scope | Registry bind (Playbook 02 + RT-G05) |

**Note:** Single-project Factory path without catalog remains doctrinally valid — OBL-02R is **mandatory for MVP Wave 1 demo track (C4/S3)**, not for all Factory work.

### Tier 3 — Tracking indexes (C6, S5)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-03** | **POC-03** state index | First Playbook 04 (empty shell permitted at NEW_PROJECT after scaffold) |
| **OBL-04** | **POC-04** gate outcome index | First Playbook 04 (may start empty) |
| **OBL-05** | **POC-05** handoff event index | First Playbook 04 (may start empty) |
| **OBL-06** | **POC-06** declaration records | First Playbook 04 act |
| **OBL-07** | **POC-07** progression ledger | First Playbook 04 act |
| **OBL-10** | **POC-10** audit/recency markers | First Playbook 04 or explicit recency marker |

### Tier 4 — Closure (C7, S6)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-08** | **POC-08** closure metadata | Playbook 05 execution |

### Persistent inventory by playbook milestone

| Must exist after | Persistent classes |
|------------------|-------------------|
| LOC-ZONE creation | LOC-ZONE |
| Playbook 01 + RT-G10 bind | LOC-HOME, POC-01, POC-02 (manifest), POC-09 |
| Playbook 02 (if enrolled / MVP demo) | POC-02 (registry) at portfolio scope |
| Playbook 04 (first declaration) | POC-03…POC-07, POC-10 |
| Playbook 05 | POC-08 |

### Minimum bootstrap before credible Playbook 03 session

| # | Physical element | Phase reference |
|---|------------------|-----------------|
| 1 | LOC-ZONE exists | Substrate creation |
| 2 | One LOC-HOME | Manifest bind |
| 3 | POC-01 + POC-02 manifest facet bound | RT-G10 bind |
| 4 | POC-09 refs to index loci | RT-G10 bind |
| 5 | POC-02 registry facet (MVP demo) | RT-G05 bind |
| 6 | POC-03…POC-05 loci (empty OK) | Index scaffold |
| 7 | At least one Playbook 04 declaration (recommended) | Declaration cycle |

### What is NOT a physical obligation of RT-G04

| Not required by RT-G04 | Owner |
|------------------------|-------|
| MOC-* content shape | RT-G10 physical specification track |
| ROC-* content shape | RT-G05 physical specification track |
| SOC-* read binding | RT-G12 physical specification track |
| Serialization format | Deferred — not in this specification |
| Layer artefact bodies in zone | Forbidden (RR-02) |

---

## Physical Guarantees

RT-G04 physical artifact specification **guarantees** the following to downstream standards **without defining serialization**.

### Guarantees to RT-G10 (Manifest)

| Guarantee ID | RT-G10 may rely on |
|--------------|-------------------|
| **G10-01** | Authorized zone at `workspaces/website-factory-operations/` **exists or will exist** before manifest physical bind (H-01) |
| **G10-02** | Each manifest-bound Factory Project receives **one** stable LOC-HOME (H-02, P1) |
| **G10-03** | Substrate **hosts** POC-02 manifest facet — RT-G10 **defines MOC-* content within** that carrier (H-03) |
| **G10-04** | Manifest binding **may exist without** registry catalog entry (H-04, MR-01) |
| **G10-05** | Doctrinal manifest-enrolled (Playbook 01) **precedes** physical bind; substrate **does not** auto-create on discovery (H-05) |
| **G10-06** | POC-09 topology pointers **may point to** POC-03…05 indexes on same substrate (H-06, MAP-05) |
| **G10-07** | Manifest facet **must not** be required to duplicate POC-03…05 as live authoritative gate index (H-07, MT-01) |
| **G10-08** | Playbook 04 continues to own POC-03…07 mutations — RT-G10 bind **does not** grant automation write path (H-08) |
| **G10-09** | POC-08 closure metadata **primary owner** remains Playbook 05 — RT-G10 **may reference**, not own (H-09) |
| **G10-10** | Append-only honesty (P7) applies to all records RT-G10 creates within substrate (H-10) |

### Guarantees to RT-G05 (Registry)

| Guarantee ID | RT-G05 may rely on |
|--------------|-------------------|
| **G05-01** | POC-02 registry facet **exists at portfolio scope** within LOC-ZONE when catalog bind occurs |
| **G05-02** | Registry facet **must not** embed full per-project tracking depth (INT-07, RA-05) |
| **G05-03** | Manifest anchor on substrate **must exist** before catalog pointer is valid (LC-02, REG-REL-01) |
| **G05-04** | ROC-05 → MOC-01 pointer chain crosses POC-02 facets — substrate **hosts both carriers** (REL-12) |
| **G05-05** | Portfolio catalog binding **may list zero or more** projects; manifest binding **may exist without** registry slot |
| **G05-06** | LOC-ZONE provides **one** discoverable portfolio catalog binding locus at MVP (PS-01) |
| **G05-07** | Enrollment by folder/git discovery **forbidden** — catalog records follow operator acts (LC-06, RAP-10) |

### Guarantees to RT-G12 (Tracking Surface)

| Guarantee ID | RT-G12 may rely on |
|--------------|-------------------|
| **G12-01** | POC-03…POC-07, POC-10 **exist as readable persistent indexes** at project LOC-HOME after Playbook 04 path |
| **G12-02** | RT-G12 **reads** POC-* — **never writes** POC-03…07 (OWN-03, TRK-REL-01) |
| **G12-03** | POC-D1 **may exist** as optional derived convenience — RT-G12 **may read or reconstruct** from POC-03…07 (DR-03, DR-04) |
| **G12-04** | Substrate **must not require** duplicate live gate index in manifest binding for Surface read (MAP-05) |
| **G12-05** | POC-10 provides recency markers for SRDY-07 — **must not** fabricate recency from POC-O1 alone (INT-09) |
| **G12-06** | Last Playbook 04 act reflected in POC-03…05 **is** the authoritative read source for active state view (INT-03) |
| **G12-07** | POC-09 external refs **identify** loci — broken refs visible to operator; no silent fallback to copied bodies (INT-05) |
| **G12-08** | SOC-* read composition **references** project-scope POC-* — SOC-* is **not** RT-G04 storage (PRJ-05) |

### Cross-standard guarantee principles

| Principle | Meaning |
|-----------|---------|
| **GUAR-01** | RT-G04 **hosts** all POC classes; RT-G10/05/12 **populate or read** their respective planes — **must not** create parallel SoT outside LOC-ZONE (OWN-01) |
| **GUAR-02** | Physical guarantees are **class-level and locus-level** — not format-specific |
| **GUAR-03** | Downstream standards **must not** require substrate redesign — open questions resolve within RT-G10/05/12 bounds (HAND-01) |

---

## Integrity Model

Minimum physical integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Physical artifact expectation |
|----|----------|------------------------------|
| **INT-01** | **Append-only declaration honesty** | POC-06 and POC-07 **append** new events; corrections = new declaration, not silent delete (P7) |
| **INT-02** | **Stable locus identity** | LOC-HOME **does not move** without explicit operator reconciliation act in POC-06/POC-07 |
| **INT-03** | **Last-declared wins** | POC-03 active state and POC-04/POC-05 tails **reflect** most recent Playbook 04 act |
| **INT-04** | **Derived subordination** | POC-D1 **must not** override POC-06/POC-03 when in conflict |
| **INT-05** | **Reference integrity (minimal)** | POC-09 pointers **identify** external locus; broken refs **visible** — no silent fallback to copied bodies |
| **INT-06** | **Plane separation on disk** | POC-02 manifest facet **must not** embed live gate index as authoritative second store (MT-01) |
| **INT-07** | **Catalog depth limit** | POC-02 registry facet **must not** embed full tracking depth (RA-05) |
| **INT-08** | **Human-only mutation path** | Only operator Playbook 04/05 acts **authoritatively change** persistent indexes (OA-ACT-04, SC-03) |
| **INT-09** | **Recency honesty** | POC-10 reflects last declaration or explicit «none yet» — **must not** fabricate from POC-O1 alone |
| **INT-10** | **Closure binding** | POC-08 **references** existing POC-01 identity; terminal outcome **does not** delete POC-06/POC-07 history |

### What integrity model explicitly excludes

| Excluded | Reason |
|----------|--------|
| Automated schema validation | RT-G11 post-MVP |
| Gate pass/fail evaluation | Human Playbook 04 only |
| CI/git-hook enforcement as declarer | SC-03 |
| Cross-record referential integrity engine | Single-operator MVP; operator resolves |
| Backup/DR product specification | May inherit git — not Factory subsystem |

### Integrity verification (human-operated)

MVP **accepts** operator manual review as sufficient integrity check: Playbook 03 Surface session and Playbook 04 declaration review **surface** inconsistencies. Formal validators **deferred**.

---

## Boundary Protection

RT-G04 physical artifacts **must never become** the following — inherited from implementation standard, reinforced at specification layer.

### Forbidden storage content in LOC-ZONE

| Must never persist in zone | Actual owner / location |
|----------------------------|-------------------------|
| Layer artefact bodies (Legal Pack, blueprints, HTML, src) | T1 Foundation / external workspaces |
| Gate/handoff criteria definitions | Runtime Architecture + Engine |
| Runtime vocabulary canon | Runtime Architecture v1 docs |
| Handoff package payloads | Generation Outputs / layer workstreams |
| Site Type Registry entries | Foundation `registry/` |
| Engine doctrine copies | `website-factory-reference-v1/` |
| Automated transition logs as authority | RT-G07 post-MVP |
| Queue rank / scheduler state | RT-G06, RT-G14 |
| Deploy/hosting state | Post-Factory |
| MIG / pipeline SoT | RT-G08 external |
| Agent chat, CI logs, tickets as SoT | External unless charter-bound ref |

### Forbidden system roles (no RT-G04 physical artifact class)

| RT-G04 must not become | Guard |
|------------------------|-------|
| Database / multi-tenant storage product | DF-02, TX-06 |
| Workflow engine / state machine executor | RT-G01 |
| Factory runtime product | RT-G09, SC-01 |
| Automation layer mutating indexes | RT-G03, SC-03, INT-08 |
| Application / SaaS / HomeGateway consumer | DF-06, TX-05 |
| Operator UI / dashboard | RT-G12 display ≠ storage |
| Validator / gate authority engine | RT-G11 |
| Manifest / Registry / Surface doctrine owner | Charters COMPLETE |
| Discovery crawler (auto-enrollment) | RAP-10, RD-04 |
| Unified Passport / second YAML SoT | BV-05, MA-03 |

### Forbidden anti-patterns (RT-G04 specific)

| Anti-pattern | Prevention |
|--------------|------------|
| Single mega-record swallowing manifest + full tracking | POC-RULE-02, MT-01 |
| POC-02 registry facet embedding full tracking depth | RA-05, INT-07 |
| Substrate docs inside `website-factory-reference-v1/` mixed with Engine | AZ-02 |
| Entire MARS repo as Factory zone | DF-03 bounded zone |
| Structured records inviting CI auto-write | INT-08, SC-03 |
| Physical bind before doctrinal enrollment | INT-M01, LC-06 |
| POC-O1/O2 treated as declaration authority | OR-02, LC-03 |
| RT-G04 artifact that **executes**, **mutates without Playbook 04**, **embeds bodies**, or **collapses plane separation** | PROH-01 |

**Principle BP-SPEC-01:** Structured filesystem persistence **≠** Factory runtime — physical artifact classes **support** human-operated path; they **do not execute** it.

---

## Readiness Model

### When RT-G04 Physical Artifact Specification is **complete**

This deliverable is **specification-complete** when:

| Criterion | Status |
|-----------|--------|
| Infrastructure loci defined (LOC-ZONE, LOC-HOME) | **Yes** |
| Physical record classes defined (POC-01…POC-10 + optional POC-D1/O1/O2) | **Yes** |
| Class responsibilities formalized | **Yes** |
| Authority model (authoritative / derived / operational / reference) with precedence | **Yes** |
| Relationship model (portfolio vs project, facet hosting, REL-*) | **Yes** |
| Physical obligations for valid Factory Project stated | **Yes** |
| Physical guarantees to RT-G10/05/12 without serialization | **Yes** |
| Minimum integrity expectations stated (no validators) | **Yes** |
| Boundary protection at specification layer | **Yes** |
| RT-G10 handoff assumptions explicit | **Yes** |
| No artifacts, folders, serialization, or layout created | **Yes** |

### What specification-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| Physical files **exist** in repo | Specification defines model; creation = separate authorized track |
| Serialization format **chosen** | Explicitly out of scope for this deliverable |
| Per-project home internal layout **designed** | Deferred to future specification or operator convention |
| RT-G04 gap in RUNTIME-GAPS marked IMPLEMENTED | Physical creation not started |
| MVP **demonstrated** on pilot | Success S1–S9 post-physical bind |
| LOC-ZONE path **exists on disk** | **SAFE UNKNOWN** until operator creates |

### Specification-complete vs physical creation

```text
  RT-G04 Implementation Standard v1 ── COMPLETE
           │
           ▼
  RT-G04 Physical Artifact Specification Review v1 ── COMPLETE
           │
           ▼
  RT-G04 Physical Artifact Specification v1 ── THIS (specification-complete)
           │
           ├──▶ RT-G10 Physical Artifact Specification (separate track)
           ├──▶ RT-G05 Physical Artifact Specification (separate track)
           └──▶ RT-G12 Physical Artifact Specification (separate track)
           │
           ▼
  Physical artefact creation (zone, sample records) ── ONLY when separately authorized
```

### MVP substrate readiness checklist (for operator, post-specification)

Before claiming C2 satisfied on pilot:

| # | Check |
|---|-------|
| R1 | LOC-ZONE exists and is discoverable |
| R2 | At least one LOC-HOME exists for pilot |
| R3 | POC-01 + POC-02 manifest facet bound via RT-G10 |
| R4 | POC-03…POC-07 writable via Playbook 04 path |
| R5 | POC-08 writable via Playbook 05 path |
| R6 | POC-09 refs present; no layer bodies in zone |
| R7 | Operator can answer Playbook 03 without workspace archaeology |

---

## RT-G10 Handoff Assumptions

RT-G10 Manifest Physical Artifact Specification (future track) and RT-G10 implementation **may assume** the following from this RT-G04 specification — **without** RT-G10 redefining substrate artifact model.

### Guaranteed substrate provisions (H-01…H-10 aligned)

| Assumption ID | RT-G10 may assume |
|---------------|-------------------|
| **H-01** | LOC-ZONE at `workspaces/website-factory-operations/` **exists or will exist** before manifest physical bind |
| **H-02** | Each manifest-bound Factory Project receives **one** stable LOC-HOME (P1) |
| **H-03** | Substrate **hosts** POC-02 manifest facet — RT-G10 **defines MOC-* within** that carrier |
| **H-04** | Manifest binding **may exist without** registry catalog entry |
| **H-05** | Doctrinal manifest-enrolled (Playbook 01) **precedes** physical bind |
| **H-06** | POC-09 topology pointers **may point to** POC-03…05 indexes on same substrate |
| **H-07** | Manifest facet **must not** duplicate POC-03…05 as live authoritative gate index |
| **H-08** | Playbook 04 continues to own POC-03…07 mutations — RT-G10 bind **does not** grant automation write path |
| **H-09** | POC-08 closure metadata **primary owner** remains Playbook 05 — RT-G10 **may reference**, not own |
| **H-10** | Append-only honesty (P7) applies to all records RT-G10 creates within substrate |

### Explicitly **not** provided to RT-G10 (RT-G10 must decide in its own tracks)

| Topic | Owner |
|-------|-------|
| Serialization format | RT-G10 physical specification / implementation |
| Manifest vs tracking co-location policy (OQ-M04, DF-04) | RT-G10 |
| Which Tracking zones serialize via manifest bind (OQ-M01) | RT-G10 |
| Physical bind moment vs doctrinal Enrolled (OQ-ME05) | RT-G10 |
| MRDY-* field binding and MOC-* content shape | RT-G10 |
| LOC-HOME internal layout | RT-G10 + RT-G05 coordination — **not** RT-G04 |

### Dependency edge

```text
  RT-G04 Physical Artifact Specification (this)
       │ guarantees: LOC-ZONE, LOC-HOME, POC classes, P1/P2 hosting
       ▼
  RT-G10 Manifest Physical Artifact Specification
       │ populates: POC-02 manifest facet (MOC-*)
       ▼
  RT-G05 Registry Physical Artifact Specification
       │ populates: POC-02 registry facet (ROC-*)
       ▼
  RT-G12 Surface Physical Artifact Specification
       │ reads: POC-03…07, POC-10, POC-D1 optional
```

**Principle HAND-SPEC-01:** RT-G10 **must not** require RT-G04 artifact model redesign — open questions resolve **within** RT-G10 bounds, not by expanding RT-G04 scope.

### RT-G05 and RT-G12 may also assume

| Standard | Key assumptions from this specification |
|----------|----------------------------------------|
| **RT-G05** | G05-01…G05-07; POC-02 registry facet at portfolio scope; manifest anchor prerequisite |
| **RT-G12** | G12-01…G12-08; read-only access to POC-*; no write path to indexes |

---

## Explicit Non-Claims

This document and the RT-G04 physical artifact model it defines:

- **are not** physical artefact creation, folder creation, file creation, or disk writes;
- **are not** serialization format specification (JSON/YAML/markdown/SQLite/other);
- **are not** naming conventions, folder trees, field lists, schemas, or database structures;
- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **storage product**, **database**, **ORM**, or **multi-tenant** persistence service;
- **are not** **application**, **standalone service**, **SaaS**, or **HomeGateway** integration;
- **are not** **automation layer**, **agent orchestration**, **queue**, or **validator engine**;
- **are not** **operator UI**, **dashboard**, or **CLI** (RT-G12);
- **are not** **MOC-* / ROC-* / SOC-* physical specification** — separate standard-specific tracks;
- **do not** modify RT-G04 Implementation Standard, RT-G04 Charter, Physical MVP Definition Review, Specification Review, Engine Stages 1–6, or Manifest/Registry/Surface charters;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound planes;
- **do not** claim LOC-ZONE path **exists on disk** today — **SAFE UNKNOWN** until separately created;
- **do not** claim Physical Artifact Specification **automatically** authorizes physical creation — **separate operator authorization** required.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01.

---

## Open Questions (deferred — not blockers for this specification)

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-M04 / DF-04** | Manifest vs tracking record co-location | RT-G10 physical specification track |
| **OQ-M01** | Which Tracking zones may serialize via RT-G10 | RT-G10 physical specification track |
| **OQ-ME05** | Physical bind moment vs doctrinal Enrolled | RT-G10 / operator convention |
| **OQ-R01 / DF-05** | Registry central catalog vs distributed pointers | RT-G05 physical specification track |
| **Serialization format** | JSON vs YAML vs markdown vs other | Future specification track — **not** this deliverable |
| **Internal layout** | Per-project home structure | Future specification track — **not** this deliverable |
| **DF-08** | Pilot workspace pointer policy | Per-case in POC-09 |
| **DF-09** | Network/hosting beyond local git | Low for MVP |
| **DF-10** | Git versioning policy for SoT records | Operator workshop |
| **OQ-OM06** | v0↔v1 routing discipline | Hygiene |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G04 Physical Artifact Specification v1** as **RT-G04 specification-complete** — first Physical Artifact Specification in authorized sequence.
2. **Authorize next tracks:** RT-G10, RT-G05, RT-G12 **Physical Artifact Specifications** — MOC/ROC/SOC content and read binding within substrate assumptions G10-*, G05-*, G12-*.
3. **Preserve sequencing:** Specification tracks complete **before** physical MVP artefact creation unless separately authorized.
4. **Do not create yet:** folder trees, sample records, schemas, runtime, UI, automation under `workspaces/website-factory-operations/`.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — specification records authorized zone; physical creation not part of this deliverable |
| Calendar for RT-G10/05/12 Physical Artifact Specifications | **not scheduled** |
| Triumph / client workspaces in substrate refs vs external-only | **UNKNOWN** — DF-08 per case |
| Serialization format choice timing | **deferred** — explicit non-scope of this specification |

---

*RT-G04 Physical Artifact Specification v1 — first Website Factory Physical Artifact Specification. Canonical location: `workspaces/website-factory-reference-v1/RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G04 Physical Artifact Specification v1

**Stage:** Physical Artifact Specification Era — RT-G04 Physical Artifact Specification (first Physical Artifact Specification)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md` (created)  
**Summary:** Первая Physical Artifact Specification Website Factory: полная физическая модель RT-G04 — infrastructure loci (LOC-ZONE, LOC-HOME), thirteen POC classes с responsibilities и MVP disposition, authority model (authoritative/derived/operational/reference) с precedence, relationship model (portfolio vs project, facet hosting, REL-01…13), physical obligations для valid Factory Project, physical guarantees G10/G05/G12 без serialization, integrity model, boundary protection, readiness model и RT-G10 handoff assumptions — без создания артефактов, folders, serialization format и layout.  
**Git:** no commit, no push (per task).
