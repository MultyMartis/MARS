# REPORT — RT-G04 Persistence Substrate Implementation Standard v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Standards — **RT-G04 implementation standard only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Persistence Substrate Charter **COMPLETE**; Implementation Planning Consolidation Review **COMPLETE**  
**Тип:** implementation standard only — **без** runtime, database, automation, queue, workflow engine, UI, application, schemas, folder layout, physical artefact creation, code  
**Upstream:** [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), Operational Playbooks 01–05  
**Связь:** [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G04

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |

---

## Purpose

### Зачем существует RT-G04 Implementation Standard

**RT-G04 Persistence Substrate Implementation Standard v1** переводит [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) из **роли носителя** (charter) в **конкретную MVP-модель физического существования** persistence substrate — оставаясь **filesystem-backed**, **documentation-first** и **human-operated**, без runtime-концепций.

| Charter отвечает | Implementation Standard отвечает |
|------------------|----------------------------------|
| Какова **роль** substrate | Как substrate **существует физически** в MVP |
| Какие **классы** substrate владеет (doctrine-level) | Какие **физические record classes** должны существовать |
| Где **authorized zone** (DF-03) | Какие **виды записей** принадлежат zone |
| P1–P8 как planning obligations | P1–P8 как **implementation obligations** для physical records |
| Что substrate **не становится** | Что substrate **не хранит** на диске |

### Нормативная формулировка implementation responsibility

**RT-G04 Persistence Substrate (MVP implementation)** — **авторизованный file-backed physical layer** в `workspaces/website-factory-operations/` внутри MARS monorepo, содержащий **structured filesystem records** классов, определённых этим standard, которые operator **читает и вручную обновляет** для поддержки Playbooks 01→05 и capability floor C2–C7 — **без** shipped runtime, **без** automated index mutation и **без** выбора serialization format (территория RT-G10/05/12 standards).

### Implementation purpose statement

Substrate implementation **материализует** единый physical locus (TR-01, C2), на котором:

1. **Per-project record homes** принимают manifest binding (RT-G10), tracking indexes и closure metadata.
2. **Portfolio-level catalog binding** принимает registry records (RT-G05).
3. **Operator declaration writes** (Playbook 04) отражаются в persisted Engine instance indexes.
4. **External refs** указывают на layer bodies и client workspaces **без** их поглощения.

Substrate implementation **не сериализует** manifest/registry/surface — он **обеспечивает physical homes** для authorized bindings, которые RT-G10/05/12 standards определяют отдельно.

---

## Foundation Dependencies

Implementation Standard **наследует** charter и planning review **без их переопределения**.

### Tier 0 — Charter and decision chain

| Document | Standard использует |
|----------|---------------------|
| [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) | P1–P8, reality model, ownership, authorized zone, boundary protection |
| [RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md) | Persistence responsibilities, playbook touchpoints, classification rules |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-01/02/03/06; SC-* guards |
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C2–C7 capability floor; S2–S7 success classes |
| [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-CONSOLIDATION-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-CONSOLIDATION-REVIEW-v1.md) | Sequencing: RT-G04 standard first; RT-G10/05/12 follow |

### Tier 1 — Operational doctrine

| Document | Standard использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; single operator; human-operated writes |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — enrollment precedes physical bind |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — declared catalog enrollment |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — read-only session; SRDY assessment |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — DA-01 sole declarer; index writes |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — terminal metadata persistence |

### Tier 2 — Post-Engine charters (ownership Substrate must not violate)

| Charter | Constraint on implementation |
|---------|------------------------------|
| Manifest (RT-G10 doctrine) | MAP-01 — Manifest ≠ storage; substrate **hosts** binding carrier |
| Registry (RT-G05 doctrine) | RAP-01 — Registry ≠ database; catalog **≠** tracking depth |
| Tracking Surface (RT-G12 doctrine) | TS-01 — Surface **reads** substrate; **never** writes indexes |

### Tier 3 — Engine boundary

| Document | Constraint |
|----------|------------|
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04 — persistence **external** to Engine docs |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking owns composition; substrate **persists** instance records |

**Authority precedence:** Foundation Freeze + Engine → Manifest/Registry/Surface charters → RT-G04 Charter → **этот standard** → RT-G10/05/12 implementation standards **не могут** нарушить MAP-01, RAP-01, TS-01, ES-04, OA-ACT-04.

---

## Persistence Object Classes

Implementation standard определяет **десять physical record classes** — нормативные категории structured filesystem records, **не** schema labels, field names или file names.

### Class taxonomy

| Class ID | Class name | Physical meaning | MVP disposition |
|----------|------------|------------------|-----------------|
| **POC-01** | **Identity** | Stable Factory Project identity shell bound to per-project physical locus | **Must persist** |
| **POC-02** | **Binding** | Manifest and registry binding carriers at project or portfolio level | **Must persist** (when bound) |
| **POC-03** | **State** | Active state instance + declared state history | **Must persist** |
| **POC-04** | **Gate** | Gate outcome index — observed PASS/FAIL/BLOCKED outcomes, not criteria | **Must persist** |
| **POC-05** | **Handoff** | Handoff event index + package refs — events/refs, not payloads | **Must persist** |
| **POC-06** | **Declaration** | Append-only operator declaration records and reconciliation acts | **Must persist** |
| **POC-07** | **Ledger** | Progression ledger / audit trail linking declarations to index mutations | **Must persist** |
| **POC-08** | **Closure** | Factory-terminal / partial / suspended outcome metadata | **Must persist** (when Playbook 05 executed) |
| **POC-09** | **Reference** | External workspace, layer body, handoff payload, Runtime doc pointers | **Must persist** (refs only) |
| **POC-10** | **Audit** | Last declaration recency markers; session outcome refs for SRDY-07 | **Must persist** |

### Optional physical classes (may persist at MVP)

| Class | Content | Notes |
|-------|---------|-------|
| **POC-D1** | **Derived cache** | Eligibility snapshots, SRDY pass/fail views, registry orientation summaries | Regeneratable; **not authoritative** |
| **POC-O1** | **Operational note** | Pre-declaration Playbook 03 session notes | **Not authoritative** until Playbook 04 act |
| **POC-O2** | **Enrollment draft** | Pre-bind enrollment decision notes before RT-G10 physical bind | Supports OQ-ME05; not blocking |

### Class composition model (implementation-level, not folder design)

```text
  workspaces/website-factory-operations/          ← authorized zone (DF-03)
  │
  ├── portfolio scope
  │     └── POC-02 (registry catalog binding)     ← P3; Playbook 02
  │
  └── per-project record home                     ← P1; discoverable locus
        ├── POC-01 identity
        ├── POC-02 manifest binding carrier         ← P2; RT-G10 serializes content
        ├── POC-03 state instance + history       ← P4
        ├── POC-04 gate outcome index             ← P4
        ├── POC-05 handoff event index            ← P4
        ├── POC-09 artefact ref index             ← P4, P8
        ├── POC-06 declaration records            ← P5
        ├── POC-07 progression ledger             ← P5, P7
        ├── POC-10 audit / recency markers        ← P4/P5; SRDY-07
        ├── POC-08 closure metadata               ← P6; Playbook 05
        ├── POC-09 external ref discipline        ← P8
        └── POC-D1 derived cache (optional)       ← may persist; subordinate
```

**Principle POC-RULE-01:** каждый Factory Project с physical binding **must have exactly one** discoverable per-project record home (P1). Portfolio catalog binding **may list zero or more** projects; manifest binding **may exist without** registry slot.

**Principle POC-RULE-02:** POC-02 manifest binding and POC-03…POC-07 tracking indexes **remain separate record classes** on disk — substrate **must not** collapse them into a single undifferentiated «project file» that violates MT-01 / MAP-01, even if RT-G10 later chooses co-location policy (OQ-M04).

### Mapping: charter obligations → physical classes

| Charter obligation | Physical classes |
|--------------------|------------------|
| P1 Per-project physical locus | Per-project record home (container for POC-01…POC-10) |
| P2 Manifest binding carrier | POC-02 (manifest facet) + POC-01 |
| P3 Registry catalog carrier | POC-02 (registry facet) at portfolio scope |
| P4 Tracking instance records | POC-03, POC-04, POC-05, POC-09 (artefact refs), POC-10 |
| P5 Declaration writes | POC-06, POC-07; mutates POC-03…POC-05 |
| P6 Closure records | POC-08 |
| P7 Append-only honesty | POC-06, POC-07 — immutable event semantics |
| P8 External ref discipline | POC-09 — pointers only |

---

## Persistence Categories

Implementation standard формализует четыре reality categories из charter в **implementation terms** — правила физического размещения и authority.

### Persistent reality (must survive between sessions)

**Definition:** structured filesystem records, потеря которых **ломает** Playbooks 03/04/05 или eight Surface questions **without workspace archaeology**.

| Implementation rule | Physical manifestation |
|---------------------|------------------------|
| **PR-01** | POC-01…POC-10 **must exist** as durable structured records within authorized zone when corresponding playbook act has occurred |
| **PR-02** | Persistent records **must remain** readable after operator session ends — filesystem durability + optional git versioning (DF-10) |
| **PR-03** | Charter-bound stable categories (scope tier, declared endpoint, applicability mask) **must persist** when declared — typically within POC-02 manifest binding carrier (RT-G10) or POC-06 declaration trail |
| **PR-04** | Engine instance indexes (POC-03…POC-05) **must reflect last declared truth** — not last inferred or automated state |

**Persistent inventory (MVP minimum for one Core 5 pilot through Playbooks 01→05):**

| Must exist after | Persistent classes |
|------------------|-------------------|
| Playbook 01 + RT-G10 bind | POC-01, POC-02 (manifest), POC-09 (topology refs) |
| Playbook 02 (if enrolled) | POC-02 (registry catalog entry + manifest pointer) |
| Playbook 04 (first declaration) | POC-03…POC-07, POC-10 |
| Playbook 05 | POC-08 |

### Derived reality (may be reconstructed)

**Definition:** structured records **permitted** on substrate for operator convenience; **must be regeneratable** from persistent records + Runtime vocabulary.

| Implementation rule | Physical manifestation |
|---------------------|------------------------|
| **DR-01** | POC-D1 caches **must be labeled** (by convention or separate record class) as derived — not declarer authority |
| **DR-02** | If derived cache contradicts POC-06/POC-03 tail, **persistent wins** (TV-02) |
| **DR-03** | RT-G12 **may read** POC-D1 or **reconstruct** from POC-03…POC-07 — substrate **must not require** duplicate live index in manifest binding (MAP-05) |
| **DR-04** | Derived material **may be omitted** at MVP; Playbook 03 remains operable via direct index read |

**Examples:** eligibility snapshot, blocking/completion picture, active lifecycle segment label, composite gate rollup, SRDY-* derived views.

### Reference reality (must not become persistence bodies)

**Definition:** information **indexed by pointer** from substrate; **bodies live elsewhere**.

| Implementation rule | Physical manifestation |
|---------------------|------------------------|
| **RR-01** | POC-09 stores **locator + role label** — not T1 layer content |
| **RR-02** | Substrate **must not** copy Legal Pack, blueprints, handoff payloads, Runtime definitions into Factory SoT zone |
| **RR-03** | Client workspaces (`workspaces/triumph-*`, Lane A `src/`, pilot snapshots) appear as **external refs only** (ER-06) |
| **RR-04** | Site Type Registry (`registry/`) **never** migrates into Factory zone (RAP-11) |

### Operational reality (transient; not persistence core)

**Definition:** session-local or pre-declaration material; **must not mutate** POC-03…POC-07 without Playbook 04.

| Implementation rule | Physical manifestation |
|---------------------|------------------------|
| **OR-01** | POC-O1 session notes **may persist** optionally; **do not** substitute for POC-06 |
| **OR-02** | In-flight operator drafts **must not** be treated as Factory SoT until declared |
| **OR-03** | Evidence bundles pre-declaration **may** live outside zone or as non-authoritative refs |
| **OR-04** | Trigger signals (client brief, incoming request) **remain pre-Factory** until Playbook 01 recognition |

### Category interaction diagram

```text
  REFERENCE (outside zone)          OPERATIONAL (transient)
         │                                    │
         │ POC-09 pointers only               │ POC-O1 optional
         ▼                                    ▼
  ┌─────────────────────────────────────────────────────────┐
  │  AUTHORIZED ZONE — PERSISTENT + optional DERIVED         │
  │  POC-01…POC-10 (authoritative)  │  POC-D1 (subordinate)  │
  └─────────────────────────────────────────────────────────┘
         ▲
         │ read-only composition
  ┌──────┴──────┐
  │ RT-G12 impl │  (future standard — not substrate)
  └─────────────┘
```

---

## Authorized Zone Usage

### Factory Records Zone (DF-03 — implementation binding)

**Normative path:** `workspaces/website-factory-operations/` within `C:\AI MARS`.

| Rule ID | Implementation rule |
|---------|---------------------|
| **AZ-01** | **All** Factory SoT structured records (POC-01…POC-10, optional POC-D1) **must live inside** authorized zone — not scattered across monorepo |
| **AZ-02** | Zone **hosts** Factory Project persistence only — **not** Engine doctrine, **not** layer bodies, **not** client site source |
| **AZ-03** | `workspaces/website-factory-reference-v1/` **remains** canonical doctrine + Engine — **outside** Factory SoT |
| **AZ-04** | `projects/mars-website-factory/` operational pack v0 **does not supersede** v1 canon without explicit routing (OQ-OM06) |
| **AZ-05** | `registry/`, Lane A `src/`, unrelated MARS programs **remain outside** zone |
| **AZ-06** | Portfolio-level registry catalog binding (POC-02 registry facet) **may reside** at zone root scope; per-project homes **must be** discoverable from catalog pointer or direct operator knowledge |
| **AZ-07** | Zone **requires no** HomeGateway, database, or standalone application (DF-06, TOPOLOGY-B-v1) |

### What belongs in the zone (by record kind)

| Belongs in zone | Does not belong in zone |
|-----------------|-------------------------|
| Per-project record homes (P1) | Legal templates, blueprints, block definitions |
| Manifest binding carriers (P2) | Runtime Architecture vocabulary canon |
| Registry catalog binding (P3) | Site Type Registry entries |
| State / gate / handoff / artefact indexes (P4) | Handoff package payloads |
| Declaration records + progression ledger (P5, P7) | Gate/handoff **criteria** text |
| Closure metadata (P6) | CI logs, agent chat, MIG transcripts as SoT |
| External ref pointers (P8) | Layer artefact bodies |
| Optional derived caches (POC-D1) | Operator UI session state |
| Optional pre-declaration notes (POC-O1) | Automated transition logs as authority |

### Zone discoverability standard (without path design)

| Requirement | Implementation expectation |
|-------------|---------------------------|
| Operator finds canonical project home | **One** stable per-project locus per Factory Project identity — no competing homes |
| Operator finds portfolio catalog | **One** portfolio catalog binding location at MVP — shape deferred to RT-G05 (OQ-R01) |
| Operator distinguishes SoT from doctrine | Zone path **distinct** from `website-factory-reference-v1/` |
| Git audit | Zone records **may** inherit monorepo git discipline; policy = DF-10 (open) |

**Principle AZ-IMPL-01:** creation of zone directory tree and sample files is **out of scope** for this standard — standard **authorizes what may exist**, not **creates** artefacts.

---

## Record Ownership

### Ownership matrix: who owns physical records vs who references

| Record class | Primary owner (writes) | Reference-only consumers |
|--------------|------------------------|--------------------------|
| POC-01 Identity | Substrate + Playbook 01 enrollment act; stabilized at RT-G10 bind | RT-G05 catalog, RT-G12 Surface |
| POC-02 Manifest binding | RT-G10 implementation (serialization); operator Playbook 01 | RT-G05 (pointer), RT-G12 (entry E4) |
| POC-02 Registry catalog | RT-G05 implementation; operator Playbook 02 | RT-G12 (portfolio select) |
| POC-03 State | Operator Playbook 04 (DA-01) | RT-G12 read; Engine logical model |
| POC-04 Gate | Operator Playbook 04 | RT-G12 read |
| POC-05 Handoff | Operator Playbook 04 | RT-G12 read |
| POC-06 Declaration | Operator Playbook 04 **only** | RT-G12 read (recency) |
| POC-07 Ledger | Operator Playbook 04 **only** | Audit; RT-G12 SRDY-07 |
| POC-08 Closure | Operator Playbook 05 | RT-G12 read; manifest orientation (ref only) |
| POC-09 Reference | Operator all playbooks (maintain refs) | All planes |
| POC-10 Audit | Operator Playbooks 03–04 | RT-G12 Tier S-A |
| POC-D1 Derived | Operator or tooling **non-authoritative** | RT-G12 convenience |

### Substrate vs downstream implementation ownership

| Layer | Owns | Does not own |
|-------|------|--------------|
| **RT-G04 substrate (this standard)** | Physical homes; POC class taxonomy; zone discipline; P1–P8 hosting; integrity rules | Serialization format; manifest MRDY field binding; catalog card template; Surface display |
| **RT-G10 standard** | Manifest binding **content** and serialization within POC-02 manifest facet | Substrate zone; tracking indexes; registry catalog |
| **RT-G05 standard** | Registry catalog **content** and index shape within POC-02 registry facet | Per-project tracking depth; manifest doctrine |
| **RT-G12 standard** | Read composition for eight questions | Any authoritative index write |

### Ownership principles

| ID | Principle |
|----|-----------|
| **OWN-01** | RT-G04 **hosts** all POC classes; RT-G10/05/12 **populate** their respective binding facets — **must not** create parallel SoT outside zone |
| **OWN-02** | Only **Factory operator** (Playbook 04, OA-ACT-04) **authoritatively mutates** POC-03…POC-07 |
| **OWN-03** | RT-G12 **never writes** POC-03…POC-07 — read-oriented only (TRK-REL-01) |
| **OWN-04** | External systems **never mutate** indexes without operator act (SC-03) |
| **OWN-05** | Logical Factory Project identity **precedes** physical records (Playbook 01); registry slot **follows** manifest anchor (REG-REL-01) |

---

## Lifecycle Relationship

Implementation standard defines **how Playbooks 01–05 interact with persisted records** — **without** workflow design, state machine execution, or automation.

### Playbook → physical record interaction

| Playbook | Phase | Substrate interaction | Record classes touched |
|----------|-------|----------------------|------------------------|
| **01** Manifest enrollment | Recognition → manifest-enrolled (doctrinal) | Doctrinal enrollment **precedes** physical bind; RT-G10 creates POC-02 manifest + POC-01 when operator binds | POC-01, POC-02 (manifest), POC-09 (refs) — **on bind** |
| **02** Registry enrollment | Optional catalog declare | Operator declares catalog entry; RT-G05 populates POC-02 registry facet with manifest pointer | POC-02 (registry) — **requires** manifest anchor |
| **03** Surface session | Read-only supervision | **Reads** POC-03…POC-07, POC-10; **may write** POC-O1 notes only; **must not** mutate indexes | Read POC-*; optional POC-O1 |
| **04** Project declaration | Authoritative truth update | Operator **writes** POC-06, appends POC-07, **mutates** POC-03…POC-05, updates POC-10 | POC-03…POC-07, POC-10 |
| **05** Project closure | Terminal outcome | Operator **writes** POC-08; **does not revoke** manifest enrollment | POC-08 |

### Lifecycle sequence (physical binding path)

```text
  PRE-FACTORY (no zone records)
       │
       ▼
  [01] Doctrinal manifest-enrolled
       │     └── optional: RT-G10 physical bind → POC-01, POC-02(m), POC-09
       ▼
  [02] Optional registry declare → POC-02(r) at portfolio scope
       │
       ▼
  [03] Surface session ──read──▶ POC-03…07, POC-10
       │         (repeat)
       ├── [04] Declaration ──write──▶ POC-06, POC-07, POC-03…05, POC-10
       │         (repeat)
       ▼
  [05] Closure ──write──▶ POC-08
```

### Lifecycle rules (implementation)

| ID | Rule |
|----|------|
| **LC-01** | Playbook 01 **complete** doctrinally **without** zone records; MVP success (S2) **requires** subsequent physical bind |
| **LC-02** | Playbook 02 **requires** manifest-enrolled + manifest anchor on substrate before catalog pointer is valid |
| **LC-03** | Playbook 03 **never** substitutes session notes (POC-O1) for declaration records (POC-06) in SRDY-07 authority |
| **LC-04** | Playbook 04 **only** path that mutates POC-03…POC-05; mid-track movement = repeated 03↔04 cycle |
| **LC-05** | Playbook 05 **binds** closure to **existing** per-project home — no orphan closure records |
| **LC-06** | Enrollment by folder/git discovery **forbidden** — all zone records follow operator acts (RD-04, RAP-10) |

---

## Integrity Model

Minimum persistence integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Implementation expectation |
|----|----------|---------------------------|
| **INT-01** | **Append-only declaration honesty** | POC-06 and POC-07 **append** new events; corrections = new declaration, not silent delete of prior declared truth (P7, TV-02, AT-*) |
| **INT-02** | **Stable locus identity** | Per-project record home **does not move** without explicit operator reconciliation act recorded in POC-06/POC-07 |
| **INT-03** | **Last-declared wins** | POC-03 active state and POC-04/POC-05 tails **reflect** most recent Playbook 04 act — not inferred automation |
| **INT-04** | **Derived subordination** | POC-D1 **must not** override POC-06/POC-03 when in conflict |
| **INT-05** | **Reference integrity (minimal)** | POC-09 pointers **identify** external locus; broken refs are **visible** to operator — no silent fallback to copied bodies |
| **INT-06** | **Plane separation on disk** | Manifest binding carrier **must not** embed live gate index as authoritative second store (MT-01, MAP-01) |
| **INT-07** | **Catalog depth limit** | Registry catalog records **must not** embed full tracking depth (RA-05) |
| **INT-08** | **Human-only mutation path** | Only operator Playbook 04/05 acts **authoritatively change** persistent indexes (OA-ACT-04, SC-03) |
| **INT-09** | **Recency honesty** | POC-10 reflects last declaration or explicit «none yet» — **must not** fabricate recency from session notes alone |
| **INT-10** | **Closure binding** | POC-08 **references** existing POC-01 identity; terminal outcome **does not** delete historical POC-06/POC-07 |

### What integrity model explicitly excludes

| Excluded | Reason |
|----------|--------|
| Automated schema validation | RT-G11 post-MVP |
| Gate pass/fail evaluation | Human Playbook 04 only |
| CI/git-hook enforcement | SC-03 — automation forbidden as declarer |
| Cross-record referential integrity engine | Single-operator MVP; operator resolves |
| Backup/DR product | May inherit git — not Factory subsystem |

### Integrity verification (human-operated)

MVP **accepts** operator manual review as sufficient integrity check: Playbook 03 Surface session and Playbook 04 declaration review **surface** inconsistencies. Formal validators **deferred**.

---

## Boundary Protection

RT-G04 implementation **must never store or become** the following — inherited from charter, reinforced at implementation layer.

### Forbidden storage content

| Must never persist in zone | Actual owner / location |
|----------------------------|-------------------------|
| Layer artefact bodies | T1 Foundation / external workspaces |
| Gate/handoff criteria definitions | Runtime Architecture + Engine |
| Runtime vocabulary canon | Runtime Architecture v1 docs |
| Handoff package payloads | Generation Outputs / layer workstreams |
| Site Type Registry | Foundation `registry/` |
| Automated transition logs as authority | RT-G07 post-MVP |
| Queue rank / scheduler state | RT-G06, RT-G14 |
| Deploy/hosting state | Post-Factory |
| MIG / pipeline SoT | RT-G08 external |
| Agent chat, CI logs, tickets | External unless charter-bound ref |

### Forbidden system roles

| RT-G04 implementation must not become | Guard |
|---------------------------------------|-------|
| Database / multi-tenant storage product | DF-02, TX-06 |
| Workflow engine / state machine executor | RT-G01; transitions declared not executed |
| Factory runtime product | RT-G09; SC-01 |
| Automation layer mutating indexes | RT-G03; SC-03 |
| Application / SaaS / HomeGateway consumer | DF-06, TX-05 |
| Operator UI / dashboard | RT-G12 display ≠ storage |
| Validator / gate authority engine | RT-G11 |
| Manifest / Registry / Surface doctrine owner | Charters COMPLETE |
| Discovery crawler (auto-enrollment) | RAP-10, RD-04 |
| Unified Passport / second YAML SoT | BV-05, MA-03 |

### Implementation anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| Single «project.yaml» swallowing manifest + full tracking | POC-RULE-02; MT-01 |
| Registry card with seven Surface answers | RA-05; POC-02 registry facet limits |
| Substrate docs inside `website-factory-reference-v1/` mixed with Engine | AZ-02 |
| Entire MARS repo as Factory zone | DF-03 bounded zone |
| Structured files inviting CI auto-write | INT-08; SC-03 |

**Principle BP-IMPL-01:** Structured filesystem persistence **≠** Factory runtime — physical records **support** human-operated path; they **do not execute** it.

---

## Readiness Model

### When RT-G04 Implementation Standard is **complete**

This deliverable is **standard-complete** when:

| Criterion | Status |
|-----------|--------|
| Physical record classes defined (POC-01…POC-10) | **Yes** |
| Must / may / derived / reference / operational categories formalized | **Yes** |
| Authorized zone usage specified (DF-03) | **Yes** |
| Record ownership matrix defined | **Yes** |
| Playbook 01–05 lifecycle interaction specified (no workflow design) | **Yes** |
| Minimum integrity expectations stated (no validators) | **Yes** |
| Boundary protection at implementation layer | **Yes** |
| RT-G10 handoff assumptions explicit | **Yes** |
| No schemas, folders, code, or physical artefacts created | **Yes** |

### What standard-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| Physical files **exist** in repo | Standard authorizes; creation = separate authorized track |
| RT-G04 gap in RUNTIME-GAPS marked IMPLEMENTED | Implementation execution not started |
| DF-04…DF-10 **resolved** | Deferred to RT-G10/05/12 standards |
| MVP **demonstrated** on pilot | Success S1–S9 post-physical bind |
| Zone path **exists on disk** | **SAFE UNKNOWN** until operator creates |

### Standard-complete vs implementation-executed

```text
  RT-G04 Charter v1 ── COMPLETE
           │
           ▼
  RT-G04 Implementation Standard v1 ── THIS (standard-complete)
           │
           ▼
  RT-G10 Manifest Implementation Standard ── NEXT authorized standard
           │
           ├──▶ RT-G05 Registry Implementation Standard
           │
           └──▶ RT-G12 Surface Implementation Standard
           │
           ▼
  Physical artefact creation (zone, sample records) ── ONLY when separately authorized
```

### MVP substrate readiness checklist (for operator, post-standards)

Before claiming C2 satisfied on pilot:

| # | Check |
|---|-------|
| R1 | Authorized zone exists and is discoverable |
| R2 | At least one per-project record home exists for pilot |
| R3 | POC-01…POC-02 (manifest) bound via RT-G10 standard |
| R4 | POC-03…POC-07 writable via Playbook 04 path |
| R5 | POC-08 writable via Playbook 05 path |
| R6 | POC-09 refs present; no layer bodies in zone |
| R7 | Operator can answer Playbook 03 without workspace archaeology |

---

## RT-G10 Handoff Assumptions

RT-G10 Manifest Implementation Standard **may assume** the following from RT-G04 — **without** RT-G10 redefining substrate.

### Guaranteed substrate provisions

| Assumption ID | RT-G10 may assume |
|---------------|-------------------|
| **H-01** | Authorized zone at `workspaces/website-factory-operations/` **exists or will exist** before manifest physical bind |
| **H-02** | Each manifest-bound Factory Project receives **one** stable per-project record home (P1) |
| **H-03** | Substrate **hosts** POC-02 manifest binding carrier — RT-G10 **defines serialization within** that carrier |
| **H-04** | Manifest binding **may exist without** registry catalog entry (MR-01, Playbook 01→02 precedence) |
| **H-05** | Doctrinal manifest-enrolled (Playbook 01) **precedes** physical bind; substrate **does not** auto-create on discovery |
| **H-06** | POC-09 reference topology pointers **may point to** POC-03…POC-05 indexes on same substrate (MAP-05) |
| **H-07** | Manifest binding **must not** be required to duplicate POC-03…POC-05 as live authoritative gate index (MT-01) |
| **H-08** | Playbook 04 continues to own POC-03…POC-07 mutations — RT-G10 bind **does not** grant automation write path |
| **H-09** | POC-08 closure metadata **primary owner** remains Playbook 05 + substrate P6 — RT-G10 **may reference**, not own |
| **H-10** | Append-only honesty (P7) applies to all records RT-G10 creates within substrate |

### Explicitly **not** provided to RT-G10 (RT-G10 must decide)

| Topic | Owner |
|-------|-------|
| Serialization format (JSON/YAML/markdown structured / other) | RT-G10 standard |
| Manifest vs tracking co-location (OQ-M04, DF-04) | RT-G10 standard |
| Which Tracking zones serialize via manifest bind (OQ-M01) | RT-G10 standard |
| Physical bind moment vs doctrinal Enrolled (OQ-ME05) | RT-G10 standard |
| MRDY-* field binding and entry anchor shape | RT-G10 standard |
| Per-project home internal layout | RT-G10 + RT-G05 coordination — **not** RT-G04 |

### Dependency edge (implementation sequence)

```text
  RT-G04 Implementation Standard (this)
       │ guarantees: zone + POC classes + P1/P2 hosting
       ▼
  RT-G10 Manifest Implementation Standard
       │ populates: POC-02 manifest facet, POC-01, POC-09 topology refs
       ▼
  RT-G05 Registry Implementation Standard
       │ populates: POC-02 registry facet (portfolio)
       ▼
  RT-G12 Surface Implementation Standard
       │ reads: POC-03…07, POC-10, POC-D1 optional
```

**Principle HAND-01:** RT-G10 **must not** require substrate redesign — open questions OQ-M04, OQ-M01, OQ-ME05 resolve **within** RT-G10 standard bounds, not by expanding RT-G04 scope.

---

## Explicit Non-Claims

This document and the RT-G04 Persistence Substrate implementation standard it defines:

- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **storage product**, **database**, **ORM**, or **multi-tenant** persistence service;
- **are not** **application**, **standalone service**, **SaaS**, or **HomeGateway** integration;
- **are not** **automation layer**, **agent orchestration**, **queue**, or **validator engine**;
- **are not** **operator UI**, **dashboard**, or **CLI** (RT-G12);
- **are not** **Manifest serialization standard** (RT-G10), **Registry catalog standard** (RT-G05), or **Surface read standard** (RT-G12);
- **do not** define JSON/YAML/SQLite schemas, field lists, folder trees, file naming, or database tables;
- **do not** create physical artefacts under `workspaces/website-factory-operations/`;
- **do not** modify RT-G04 Charter, Engine Stages 1–6, or Manifest/Registry/Surface charters;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound planes;
- **do not** claim zone path **exists on disk** today — **SAFE UNKNOWN** until separately created.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01.

---

## Open Questions (deferred — not blockers for this standard)

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-M04 / DF-04** | Manifest vs tracking record co-location | RT-G10 Implementation Standard |
| **OQ-M01** | Which Tracking zones may serialize via RT-G10 | RT-G10 Implementation Standard |
| **OQ-ME05** | Physical bind moment vs doctrinal Enrolled | RT-G10 Implementation Standard |
| **OQ-R01 / DF-05** | Registry central catalog vs distributed pointers | RT-G05 Implementation Standard |
| **OQ-R02** | Registry card field template | RT-G05 Implementation Standard |
| **OQ-PD05** | Declaration/session record binding for SRDY-07 | RT-G10/12 standards |
| **DF-07** | RT-G12 read surface form factor | RT-G12 Implementation Standard |
| **DF-08** | Pilot workspace pointer policy | Operational |
| **DF-09** | Network/hosting beyond local git | Low for MVP |
| **DF-10** | Git versioning policy for SoT records | Operator workshop |
| **OQ-OM06** | v0↔v1 routing discipline | Hygiene |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G04 Persistence Substrate Implementation Standard v1** as **RT-G04 standard-complete** — first Implementation Standard in authorized sequence.
2. **Authorize next standard:** **RT-G10 Manifest Implementation Standard** — serialization and bind rules **within** substrate assumptions H-01…H-10.
3. **Preserve sequencing:** RT-G10 → RT-G05 → RT-G12 implementation standards — **before** physical MVP artefact creation unless separately authorized.
4. **Do not create yet:** folder trees, sample records, schemas, runtime, UI, automation under `workspaces/website-factory-operations/`.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — standard records authorized zone; physical creation not part of this deliverable |
| Calendar for RT-G10 Implementation Standard | **not scheduled** |
| Triumph / client workspaces in substrate refs vs external-only | **UNKNOWN** — DF-08 per case |
| Operators updated NEXT-PRIORITIES to Implementation Standards era | **UNKNOWN** |

---

*RT-G04 Persistence Substrate Implementation Standard v1 — first Website Factory Implementation Standard. Canonical location: `workspaces/website-factory-reference-v1/RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G04 Persistence Substrate Implementation Standard v1

**Stage:** RT-G04 — Persistence Substrate Implementation Standard (post–Charter, first Implementation Standard)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md` (created)  
**Summary:** Первый Implementation Standard Website Factory: перевод RT-G04 charter в конкретную MVP-модель физического существования persistence substrate — десять record classes (POC-01…POC-10), четыре persistence categories в implementation terms, authorized zone usage (`workspaces/website-factory-operations/`), ownership matrix, lifecycle связь Playbooks 01–05, minimum integrity model, boundary protection, readiness model и RT-G10 handoff assumptions H-01…H-10 — без runtime, schemas, folders, code и physical artefacts.  
**Git:** no commit, no push (per task; document does not recommend commit).
