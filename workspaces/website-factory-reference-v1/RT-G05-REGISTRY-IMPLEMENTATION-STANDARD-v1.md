# REPORT — RT-G05 Registry Implementation Standard v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `X:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Standards — **RT-G05 implementation standard only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Persistence Substrate Implementation Standard **COMPLETE**; RT-G10 Manifest Implementation Standard **COMPLETE**; RT-G05 Registry Implementation Planning Charter **COMPLETE**  
**Тип:** implementation standard only — **без** runtime, database, automation, queue, workflow engine, UI, application, schemas, folder layout, physical artefact creation, code  
**Upstream:** [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md), [RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md), [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), Operational Playbooks 01–05  
**Связь:** [RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G05

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`X:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |

---

## Purpose

### Зачем существует RT-G05 Implementation Standard

**RT-G05 Registry Implementation Standard v1** переводит [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) и [RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md) из **роли portfolio discoverability layer** (doctrine + planning) в **конкретную MVP-модель физического существования** Registry catalog binding — оставаясь **filesystem-backed**, **documentation-first** и **human-operated**, без runtime-концепций.

| Charter / Planning отвечает | Implementation Standard отвечает |
|-----------------------------|----------------------------------|
| Какова **роль** Registry (catalog, discoverability, distinction) | Как Registry catalog binding **существует физически** в MVP |
| Какие **категории** Registry владеет doctrinally (Scope Categories 1–7) | Какие **implementation object classes** должны быть сериализованы |
| RRDY-* как catalog integrity threshold | RRDY-* как **implementation expectations** при physical bind |
| RA-*, RM-*, RD-*, RAP-* anti-patterns | Что Registry implementation **must never become** on disk |
| IR-* planning obligations | IR-* как **implementation obligations** для POC-02 registry facet |

### Нормативная формулировка implementation responsibility

**RT-G05 Registry Implementation (MVP implementation)** — **авторизованная portfolio-level physical binding** Registry doctrine в POC-02 registry facet внутри authorized zone на RT-G04 substrate, которую operator **читает и вручную создаёт/обновляет** после Playbook 02 enrollment — **без** shipped runtime, **без** automated catalog enrollment on discovery и **без** выбора serialization format в этом standard (implementation classes only).

Registry implementation **материализует portfolio listing (C4, S3)** и **RRDY-* categories** — **не** Manifest, **не** Tracking composition, **не** Surface display, **не** CRM, **не** project manager.

### Implementation purpose statement

Registry implementation **материализует** для Factory portfolio scope:

1. **One canonical persisted portfolio catalog binding** (S3, C4) — operator перечисляет enrolled Factory Projects **без** workspace archaeology per case.
2. **Faithful physical representation** of RRDY-* categories attested at Playbook 02 — **not** re-evaluation ritual.
3. **Stable Manifest entry pointer** per catalog slot (RM-01) — portfolio select → per-project depth.
4. **Distinction summaries** sufficient for cross-project differentiation — **not** seven/eight tracking questions.
5. **Discoverability lifecycle** categories (discoverable / withdrawn / archived) — catalog visibility, not Runtime state.

Registry implementation **не сериализует** per-project manifest depth, live gate/handoff indexes, declaration authority, Surface answers, or layer bodies — it **populates POC-02 registry facet** at portfolio scope within substrate homes RT-G04 already defined.

---

## Foundation Dependencies

Implementation Standard **наследует** Registry Charter, RT-G05 planning charter, RT-G04 standard, RT-G10 standard и operational doctrine **без их переопределения**.

### Tier 0 — Charter, standard, and decision chain

| Document | Standard использует |
|----------|---------------------|
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Scope Categories 1–7, RRDY-*, RD-*, RA-*, RM-*, RE-*, RS-*, RAP-* — **sole doctrine source** |
| [RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | IR-*, RRB-*, G04-REL-*, M10-REL-*, TRK-REL-*, AUTH-*, BP-* |
| [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md) | POC-02 (registry facet), P3, AZ-06, INT-07, OWN-01 |
| [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md) | MOC-01…MOC-12, M-H01…M-H10, REG-IMPL-01/02 |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-01/02/03/06 |
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C4 registry visibility; S3 success; C2→C3→C4→C5 dependency |

### Tier 1 — Operational doctrine

| Document | Standard использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; operator path Registry→Manifest→Tracking→Surface; Decision class **I** |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — manifest-enrolled precondition |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — catalog-discoverable outcome; RRDY evaluation; enrollment/withdrawal acts |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — portfolio select; RE-01 |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — separate write plane; catalog **does not** receive gate outcomes |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — archived catalog category; withdrawal orthogonal to Factory-track closure |

### Tier 2 — Engine and neighbor charters

| Document | Constraint on implementation |
|----------|------------------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Identity shell; ES-03 — logical project vs registry entry |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | MR-01, MR-02, RA-04 — registry follows manifest anchor |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | RA-05 — registry **не** seven questions |
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | RE-01, VP-05, TS-01 — Surface **per-project**; Registry **portfolio only** |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-03 external registry; EO-05 one Engine per project |

**Authority precedence:** Foundation Freeze + Engine → Registry Charter (doctrine) → Manifest Charter (doctrine) → RT-G04 Standard → RT-G10 Standard → RT-G05 Planning Charter → **этот standard** → RT-G12 standard **не может** нарушить RA-*, RM-*, RD-*, RAP-*, OA-ACT-04, ES-03, M-H01…M-H10, POC-RULE-02.

---

## Registry Object Model

Implementation standard определяет **одиннадцать implementation object classes** — нормативные категории structured content within POC-02 registry facet at portfolio scope, **не** schema labels, field names, or file names.

### Class taxonomy

| Class ID | Class name | Physical meaning | MVP disposition |
|----------|------------|------------------|-----------------|
| **ROC-01** | **Catalog aggregate** | Portfolio-scope canonical listing container — materialization of «which Factory projects exist» | **Must persist** when any catalog entry bound |
| **ROC-02** | **Catalog entry** | One discoverability slot per logical Factory Project in portfolio view | **Must persist** per enrolled project |
| **ROC-03** | **Registry entry identity** | Index slot identifier — **distinct** from logical Factory Project identity (RA-03, ES-03) | **Must persist** per ROC-02 |
| **ROC-04** | **Logical identity reference** | Stable pointer to Engine identity shell (Category 2) | **Must persist** per ROC-02 |
| **ROC-05** | **Manifest pointer** | Stable reference to per-project MOC-01 entry anchor (Category 3, RM-01) | **Must persist** per discoverable ROC-02 |
| **ROC-06** | **Distinction summary** | Portfolio-safe charter label, scope tier, endpoint summary categories (Category 4) | **Must persist** per ROC-02 |
| **ROC-07** | **Discoverability status** | Catalog lifecycle category: discoverable / withdrawn / archived (Category 6) | **Must persist** per ROC-02 |
| **ROC-08** | **Orientation snapshot** | Non-authoritative portfolio glance — active state, track flags (Category 5) | **May persist**; **must not** duplicate live gate index |
| **ROC-09** | **Enrollment bind metadata** | Physical bind linkage to Playbook 02 Enrolled act | **Must persist** on catalog entry bind |
| **ROC-10** | **Catalog amendment narrative** | Enrollment, withdrawal, re-enrollment, distinction update — append-oriented (RS-01, RAP-17) | **Must persist** when catalog lifecycle events occur |
| **ROC-11** | **External workspace pointer** | Optional charter-declared external ref category on catalog card (Category 7) | **May persist** — refs only |

### Optional extension classes (bounded — default exclude)

| Class | Content | Notes |
|-------|---------|-------|
| **ROC-X1** | **Derived orientation cache** | Regeneratable portfolio glance from Tracking read — POC-D1 analog at catalog level | **Non-authoritative**; OQ-R08 bounded |
| **ROC-O1** | **Pre-bind enrollment draft** | Pre-physical-bind notes before Playbook 02 Enrolled — supports OQ-RE05 | **Not authoritative** until bind act |

### Class composition model (implementation-level, not folder design)

```text
  authorized zone (RT-G04 DF-03)
  │
  ├── portfolio scope
  │     └── POC-02 registry facet
  │           ├── ROC-01 Catalog aggregate ◀── MVP hinge (S3, C4)
  │           └── ROC-02 Catalog entry (0..n)
  │                 ├── ROC-03 Registry entry identity
  │                 ├── ROC-04 Logical identity reference
  │                 ├── ROC-05 Manifest pointer ──▶ MOC-01 (per-project home)
  │                 ├── ROC-06 Distinction summary
  │                 ├── ROC-07 Discoverability status
  │                 ├── ROC-08 Orientation snapshot (optional)
  │                 ├── ROC-09 Enrollment bind metadata
  │                 ├── ROC-10 Amendment narrative (when needed)
  │                 ├── ROC-11 External workspace pointer (optional)
  │                 └── ROC-X1 derived cache (default: absent)
  │
  └── per-project record home(s)  ◀── referenced by ROC-05, not owned by registry facet
        └── POC-02 manifest facet (RT-G10) + POC-03…07 (Tracking)
```

**Principle ROC-RULE-01:** ROC-01 **must** be **one** canonical portfolio catalog aggregate at MVP — no competing portfolio listings (TOP-01).

**Principle ROC-RULE-02:** Exactly **one** ROC-02 catalog entry **per** logical Factory Project identity in default portfolio doctrine — duplicate slots **forbidden** (RA-03).

**Principle ROC-RULE-03:** POC-02 registry facet **must remain** a **distinct record class** from POC-02 manifest facet and POC-03…POC-07 tracking indexes (POC-RULE-02, RA-05) — co-location within authorized zone **permitted**; **collapse into undifferentiated mega-record forbidden**.

**Principle ROC-RULE-04:** ROC-05 **must** resolve to** exactly one stable MOC-01 per catalog entry — registry **points**, manifest **orients**.

### Mapping: Registry Charter scope categories → implementation classes

| Charter scope category | Implementation classes |
|------------------------|------------------------|
| Category 1 — Catalog membership | ROC-01, ROC-02, ROC-07 |
| Category 2 — Stable logical identity reference | ROC-04 |
| Category 3 — Manifest entry pointer | ROC-05 |
| Category 4 — Distinction summaries (portfolio-safe) | ROC-06 |
| Category 5 — Orientation snapshot (non-authoritative) | ROC-08, ROC-X1 (optional) |
| Category 6 — Discoverability status | ROC-07 |
| Category 7 — External workspace pointer (optional) | ROC-11 |
| Registry entry ≠ logical identity (RA-03) | ROC-03 vs ROC-04 |
| Playbook 02 enrollment act | ROC-09, ROC-10 |
| Catalog lifecycle amendments | ROC-10 |

### Portfolio catalog topology (OQ-R01 — resolved in this standard)

| Rule ID | Implementation rule |
|---------|---------------------|
| **TOP-01** | **Default MVP:** one **central** ROC-01 catalog aggregate at portfolio scope within authorized zone — operator locates portfolio listing **without** repo-wide search |
| **TOP-02** | Each ROC-02 entry **holds pointers** to per-project record home and MOC-01 — **not** a distributed-only model without aggregate |
| **TOP-03** | Pure «filesystem discovery» of per-project homes **does not** substitute ROC-01 — catalog aggregate **required** for C4/S3 |
| **TOP-04** | Serialization format choice **does not** determine topology — ROC class separation **is normative** |

### Index card template (OQ-R02 — resolved as object classes, not fields)

**OQ-R02 resolution:** «Index card template» = **ROC-02 composition** of ROC-03…ROC-11 mandatory/optional classes per rules above — **not** a field list, **not** a schema. Distinction content **sources** from MOC-03…MOC-05 (M-H05) and operator charter — registry **echoes summaries**, **does not** author charter bodies.

---

## Registry Ownership

### What Registry physically owns

Registry catalog binding **owns serialized representation** of portfolio discoverability categories within POC-02 registry facet — **listing and distinction content**, not observability depth.

| Owned content | Implementation class | Owner write path |
|---------------|---------------------|------------------|
| Portfolio catalog aggregate identity | ROC-01 | Operator catalog bind act (post Playbook 02) |
| Catalog entry slot per logical project | ROC-02 | Operator Playbook 02 Enrolled + bind act |
| Registry entry index slot identity | ROC-03 | Operator bind act — **distinct** from ROC-04 |
| Catalog membership and discoverability lifecycle | ROC-07 | Operator enrollment / withdrawal / archive declaration |
| Distinction summary categories on card | ROC-06 | Operator bind + amendment following charter/Manifest source |
| Enrollment-to-bind linkage metadata | ROC-09 | Operator bind act after Playbook 02 Enrolled |
| Catalog amendment / withdrawal narrative | ROC-10 | Operator explicit catalog lifecycle acts — append-oriented |
| Optional external workspace ref on card | ROC-11 | Operator bind/amendment when declared |
| Optional non-authoritative orientation glance | ROC-08, ROC-X1 | Operator optional update — RS-03 discipline |

### What Registry physically references

Registry catalog binding **indexes and points** — **does not own** authoritative truth bodies, manifest depth, or live tracking indexes.

| Referenced content | Typical locus | Reference rule |
|--------------------|---------------|----------------|
| Logical Factory Project identity | MOC-02 / POC-01 on substrate | ROC-04 **references** — Engine owns semantics |
| Manifest entry anchor | MOC-01 in per-project POC-02 manifest facet | ROC-05 **hard pointer** — RM-01 |
| Per-project record home | RT-G04 P1 locus | ROC-05 **may include** home locator for operator convenience |
| Charter label, scope tier, endpoint **source** | MOC-03…MOC-05 manifest facet | ROC-06 **echoes summary** — RM-02, M-H05 |
| Active state / track flags for glance | POC-03, logical metadata | ROC-08 **non-authoritative** — RS-03 |
| Classification summary label | MOC-06 when present | ROC-06 **may echo** — not Site Type Registry authority |
| Client / external workspaces | External paths | ROC-11 **pointer only** — RR-03 |
| Closure / terminal outcome | POC-08 on substrate | ROC-07 archived category **may follow** Playbook 05 — **not** primary closure owner |

### What Registry must never own

| Forbidden ownership | Actual owner | Guard |
|---------------------|--------------|-------|
| Factory Project logical identity **definition** | Engine Object Model — identity shell | RA-02, RA-03 |
| Per-project minimum understanding categories | MOC-* manifest facet; RT-G10 | RAP-07, RM-02 |
| Live gate/handoff/state indexes | POC-03…POC-05; Playbook 04 | RA-05, RAP-06 |
| Declaration records & progression ledger | POC-06, POC-07; Playbook 04 | TRK-REL-02 |
| Gate/handoff **criteria** | Runtime + Foundation | RAP-13 |
| Layer artefact **bodies** | T1 layers / external workspaces | RAP-12 |
| Eight Surface question **answers** | RT-G12 read composition | RE-01, RA-05 |
| Closure outcome **primary** persistence | POC-08; Playbook 05 | Playbook 05 scope |
| Site Type Registry entries / matrix authority | Foundation `registry/` | RAP-11 |
| Queue rank, priority, scheduling | RT-G06 | RAP-04 |
| Portfolio analytics rollups, KPI aggregates | **Nobody in MVP** | RA-05 extension |
| Automated transition / execution state | **Nobody in MVP** | RAP-03 |
| MIG sessions, agent transcripts as SoT | External | RAP-18 |

### Ownership principles

| ID | Principle |
|----|-----------|
| **ROWN-01** | RT-G05 **populates** POC-02 registry facet at portfolio scope; RT-G04 **hosts** physical zone — **must not** create parallel catalog SoT outside authorized zone |
| **ROWN-02** | Only **Factory operator** **authoritatively creates/updates** catalog binding — Playbook 02 attestation **precedes** bind; withdrawal/amendment **separate** operator acts |
| **ROWN-03** | Playbook 04 **owns** POC-03…POC-07 mutations — catalog bind **does not grant** declaration write path |
| **ROWN-04** | RT-G12 Surface **reads** catalog for optional portfolio select — **never writes** ROC-* authoritative content |
| **ROWN-05** | Logical Factory Project **precedes** catalog entry; manifest anchor **precedes** registry bind per entry (MR-01, REG-REL-01, M-H03) |
| **ROWN-06** | ROC-08 orientation snapshot **must not** become parallel gate/handoff catalog — **glance or omitted**, not second Tracking SoT (RS-02, RAP-06) |

### Substrate vs registry vs downstream ownership

| Layer | Owns | Does not own |
|-------|------|--------------|
| **RT-G04 substrate** | Physical homes; POC class taxonomy; zone discipline | Registry category content; catalog card serialization format |
| **RT-G10 manifest** | MOC-* within per-project POC-02 manifest facet | Portfolio catalog; registry lifecycle |
| **RT-G05 registry (this standard)** | ROC-* within POC-02 registry facet; portfolio listing | Per-project manifest depth; tracking indexes; Surface display |
| **Playbook 04 / Tracking** | POC-03…POC-07 authoritative indexes | Catalog membership; distinction summaries authority |
| **RT-G12 Surface** | Read composition for eight questions per project | Any authoritative write; portfolio depth answers |

---

## Registry Readiness Model

RRDY-* governs **doctrinal catalog integrity** at Playbook 02; RT-G05 standard defines **implementation expectations** when physical bind occurs — **without** schemas, field lists, or storage labels.

### RRDY → implementation standard mapping

| ID | Doctrinal criterion | Implementation expectation at physical bind |
|----|---------------------|---------------------------------------------|
| **RRDY-01** | Logical Factory Project identity explicit and Factory-scoped | ROC-04 **must** carry stable logical identity reference — **distinct** from ROC-03 registry entry ID |
| **RRDY-02** | Manifest entry anchor identified (manifest-ready) | ROC-05 **must** reference stable MOC-01 — **hard** per RM-01 |
| **RRDY-03** | Registry entry distinct from logical identity understood | ROC-03 and ROC-04 **must** coexist as **two-identifier** discipline |
| **RRDY-04** | Distinction summaries sufficient for portfolio | ROC-06 **must** persist charter label, scope tier, endpoint **summary categories** — not full Manifest bodies |
| **RRDY-05** | Discoverability status category explicit | ROC-07 **must** record catalog lifecycle category at bind |
| **RRDY-06** | Operator understands Registry ≠ Tracking ≠ Manifest | **Not serialized** — Playbook 02 attestation **precedes** bind; implementation **must not** create tracking/manifest-substitute on catalog card |

### Readiness relationships (implementation terms)

| Concept | Implementation rule |
|---------|---------------------|
| **Registry-ready** | Playbook 02 threshold — **prerequisite** for physical bind, **not replaced** by bind |
| **Physical bind complete** | ROC-01 present; ROC-02…ROC-07, ROC-09 **present** per enrolled project; ROC-05 resolves to MOC-01 |
| **Registry-ready ⊄ gate-complete** | Valid catalog entry at `NEW_PROJECT` with **empty** POC-04/POC-05 |
| **Registry-ready ⊄ fully trackable** | Valid discoverable entry with empty indexes — RD discoverable analog |
| **Registry-ready ⊄ surface-ready** | Physical registry bind **does not imply** SRDY-* — per-project indexes separate |
| **Physical bind ⊄ retroactive enrollment** | ROC-09 **must** reference prior Playbook 02 Enrolled act — bind **follows** doctrinal enrolled (BIND-01…03) |
| **Manifest-ready ⊄ registry-ready** | Manifest-enrolled **required** before registry enrollment — RRDY-02 |

### Stability expectations at implementation layer

| Stability class | Charter | Implementation rule |
|-----------------|---------|---------------------|
| **Expected stable** (identity ↔ entry binding, manifest pointer, charter label summary, scope tier, endpoint, enrollment declaration) | RS-01; Stability §Expected stable | ROC-04↔ROC-02 binding, ROC-05, ROC-06 stable facets, ROC-09, ROC-10 — silent identity remap **forbidden** |
| **Expected evolving** (orientation snapshot, classification summary, discoverability status, track flags) | RS-02, RS-03 | ROC-07, ROC-08, ROC-06 classification echo — **may update**; **must not** freeze live gate index into ROC-08 (RA-05) |

### Physical bind moment (OQ-RE05 — resolved at implementation standard)

| Rule ID | Implementation rule |
|---------|---------------------|
| **BIND-01** | Playbook 02 outcome **Enrolled** **precedes** physical catalog entry bind — doctrinal catalog-discoverable **before** ROC-* persistence |
| **BIND-02** | Bind in **same operator session** as Enrolled outcome **permitted** |
| **BIND-03** | Bind triggered by folder/git/workspace discovery **forbidden** — RD-04, RAP-10 |
| **BIND-04** | ROC-O1 pre-bind drafts **not authoritative** until BIND-01 satisfied |

### Principle RRDY-IMPL-01 — Readiness ritual vs physical representation

Playbook 02 **owns** RRDY attestation. RT-G05 **owns** faithful ROC-* representation of attested categories — **not** re-evaluation gates, **not** automated RRDY pass/fail engine.

### Principle RRDY-IMPL-02 — RRDY-02 is the registry hinge

MVP success S3 maps **directly** to ROC-01 aggregate with ROC-05 manifest pointer per enrolled entry. Standard is **incomplete** if portfolio listing discoverability or RM-01 pointer binding is ambiguous.

### MVP registry bind readiness checklist (operator, post-standard)

Before claiming C4 satisfied on pilot:

| # | Check |
|---|-------|
| R-R1 | Playbook 02 Enrolled outcome recorded (doctrinal) |
| R-R2 | ROC-01 catalog aggregate discoverable within authorized zone |
| R-R3 | ROC-02 entry present per enrolled project with ROC-03≠ROC-04 |
| R-R4 | ROC-05 resolves to MOC-01 without workspace archaeology |
| R-R5 | ROC-06 distinction summaries present — not full Manifest bodies |
| R-R6 | ROC-07 discoverability status explicit |
| R-R7 | ROC-08 absent or non-authoritative — no live gate index on card |
| R-R8 | Operator selects project from catalog → reaches MOC-01 → Tracking depth |

---

## RT-G04 Relationship

RT-G04 **hosts** registry catalog binding; RT-G05 **populates** POC-02 registry facet **within** substrate assumptions — **without** storage redesign.

### Consumption of RT-G04 provisions

| RT-G04 provision | RT-G05 implementation binding |
|------------------|-------------------------------|
| **DF-03** authorized zone | ROC-* content **resides within** `workspaces/website-factory-operations/` |
| **P3** registry catalog carrier | All ROC-* serialization **within** POC-02 registry facet at portfolio scope |
| **P2** manifest binding carrier | ROC-05 **links to** per-project POC-02 manifest facet — **does not replace** |
| **P1** per-project record home | ROC-05 **references** stable home — catalog **does not host** tracking indexes |
| **AZ-06** | ROC-01 at portfolio scope; per-project homes discoverable from ROC-05 |
| **POC-RULE-02** | Registry facet **separate** from manifest facet and POC-03…07 |
| **INT-07** | Catalog records **must not** embed full tracking depth |
| **OWN-01** | RT-G05 populates registry facet; RT-G04 hosts — no parallel SoT |
| **OWN-05** | Registry slot **follows** manifest anchor on substrate per entry |

### Bind sequence on substrate (implementation, not workflow)

```text
  PRE-FACTORY (no zone catalog records)
       │
       ▼
  Playbook 01 + RT-G10 ──▶ MOC-01…MOC-12 on per-project home
       │
       ▼
  Playbook 02 Enrolled (doctrinal)
       │
       ▼
  Operator catalog bind act ──▶ ROC-01 + ROC-02…ROC-10 at portfolio scope
       │
       ├──▶ Playbook 03 / RT-G12 ──▶ portfolio select via ROC-01
       │
       └──▶ per-project depth ──▶ MOC-01 → POC-03…07
```

### Co-location with manifest and tracking (inherited COL-*, applied to registry)

| Rule ID | Implementation rule |
|---------|---------------------|
| **COL-R01** | POC-02 registry facet (portfolio) and per-project POC-02 manifest facet **share** authorized zone — **different scope** |
| **COL-R02** | **Must remain** separate **record classes** — ROC-* **must not** merge into MOC-* or POC-03…07 |
| **COL-R03** | **Forbidden:** catalog entry embedding POC-04 gate tail as co-authoritative portfolio SoT |
| **COL-R04** | Internal layout within zone **deferred** to operator/tooling — class separation **normative** |

**Principle G04-IMPL-01:** RT-G05 **must not** require substrate redesign — TOP-*, COL-R*, BIND-* resolve **within** this standard, not by expanding RT-G04 scope.

**Principle G04-IMPL-02:** RT-G05 bind **must not precede** stable MOC-01 on substrate for each ROC-02 entry (REG-REL-01, M-H01).

---

## RT-G10 Relationship

Manifest implementation **precedes** Registry catalog binding per entry; RT-G10 **enables** stable pointer; RT-G05 **must never duplicate** Manifest depth.

### Consumption of M-H01…M-H10 (guaranteed manifest provisions)

| Assumption ID | RT-G05 implementation binding |
|---------------|-------------------------------|
| **M-H01** | ROC-05 **must** reference **one** stable MOC-01 per catalog entry |
| **M-H02** | ROC-04 **aligns with** MOC-02 logical identity — ROC-03 remains distinct index slot |
| **M-H03** | ROC-02 **may be created** only when MOC-01 exists — manifest bind **may exist without** catalog entry |
| **M-H04** | ROC-09 **must** honor Playbook 01→02 precedence — no discovery enrollment |
| **M-H05** | ROC-06 **sources** distinction summaries from MOC-03…MOC-05 categories — **echo only** |
| **M-H06** | ROC-07 withdrawn/re-enroll **orthogonal** to manifest persistence — MOC-* **persists** |
| **M-H07** | ROC-05 **pointer to MOC-01 sufficient** — MOC-08 topology **not required** on catalog card |
| **M-H08** | ROC-* **reside in** POC-02 registry facet — **separate** from POC-02 manifest facet |
| **M-H09** | Operator path ROC-05 → MOC-01 **must work** without archaeology (S3) |
| **M-H10** | On ROC-06 vs MOC-03…05 conflict, **manifest facet wins** — registry summary **follows** amendment |

### What Registry may assume from Manifest implementation

| Registry need | RT-G10 guarantee |
|---------------|------------------|
| Stable per-project entry pointer | MOC-01 materialized |
| Logical identity for catalog slot linkage | MOC-02 on same per-project home |
| Source categories for distinction summaries | MOC-03 scope, MOC-04 endpoint |
| Enrollment precedence evidence | MOC-10 predates ROC-09 |
| Manifest persistence independent of catalog visibility | Withdrawn ROC-07 does not revoke MOC-* |

### What Registry must never derive independently

| Forbidden independent derivation | Reason |
|----------------------------------|--------|
| Factory Project logical identity **without** manifest anchor | MR-01, REG-REL-01 |
| Charter intent, scope tier, endpoint **authoritatively** on card without Manifest/charter source | RM-02, RM-03 |
| Reference topology map **on catalog card** | Category 7 — MOC-08 depth |
| Manifest-enrolled status **from** filesystem scan | RD-04, RAP-10 |
| Live tracking depth **from** portfolio listing | RA-05, MT-01 |
| Minimum understanding **without** following MOC-* amendment trail | RM-03 |

### What Registry provides that Manifest does not

| Registry bind scope | Manifest exclusion |
|---------------------|-------------------|
| Coexistence of **multiple** Factory Projects in one listing | Manifest is **per-project** only (MR-02) |
| Catalog membership and discoverability lifecycle | Manifest has no «list all projects» role |
| Cross-project distinction in one view | Manifest does not compare cases |
| Withdrawn / archived **portfolio visibility** categories | Manifest enrollment **never revoked** by catalog withdrawal |

### Dependency edge

```text
  MOC-01 Entry anchor (RT-G10)
       │
       │ ROC-05 stable pointer
       ▼
  ROC-02 Catalog entry (RT-G05)
       │
       │ portfolio select
       ▼
  Playbook 03 / RT-G12 ──▶ MOC-01 → POC-03…07
```

**Principle M10-IMPL-01:** RT-G05 **must not** embed MOC-* content in registry facet — **pointer and summary echo only**.

**Principle M10-IMPL-02:** Manifest enrollment workflow (Playbook 01) and MRDY evaluation **remain outside** RT-G05 — **pointer consumption only**.

---

## Tracking Relationship

Tracking **owns** per-project instance indexes on substrate; Registry **never** substitutes Tracking at portfolio scale (RA-05, RE-01).

### What Tracking / Surface may assume from Registry implementation

| Assumption | Consumer | RT-G05 guarantee |
|------------|----------|------------------|
| Portfolio listing of **catalog-discoverable** Factory Projects exists | Playbook 03 ST-03; operator path OR-04 | ROC-01 aggregate **operator-locatable** (S3) |
| Each listed entry **points to** MOC-01 | Playbook 03 input chain | ROC-05 per ROC-02 |
| Registry card **does not** answer seven/eight tracking questions | RE-01; Surface Charter | Portfolio select only — depth in Manifest→Tracking→Surface |
| Orientation snapshot on card, if present, is **non-authoritative** | RS-03; Playbook 02 | ROC-08 reconcilable with POC-03 or flagged |
| Catalog membership **≠** gate-complete or surface-ready | Registry-ready ⊄ fully trackable | Playbook 03 may open on early discoverable entry |
| Single-project path **without** catalog remains valid | G05-REL-02 | M-H03 — RT-G12 **not required** to consume ROC-01 |

### What Tracking knows that Registry must never store in registry facet

| Tracking knowledge | Registry exclusion |
|--------------------|-------------------|
| Full gate outcome index with STALE/INVALID | POC-04 — not ROC-* duplicate |
| Complete handoff event sequence | POC-05 |
| Artefact ref index exhaustiveness | POC-09 |
| Eligibility snapshot, open gate set as catalog SoT | Derived — DR-01; RA-05 |
| Append-only audit trail detail | POC-06, POC-07 |
| Eight Surface question **answers** | RT-G12 read binding |
| State history, progression ledger bodies | POC-03 history zones |
| Recent declaration narrative (SRDY-07) | Registry **does not** own audit trail |

### Registry orientation snapshot (implementation-bound)

| Rule ID | Implementation rule |
|---------|---------------------|
| **OS-01** | **Default MVP:** ROC-08 **absent** or **minimum** glance — ROC-06 distinction summaries **sufficient** for S3 |
| **OS-02** | ROC-08 **may** surface active state / track flag categories — **non-authoritative** per RS-03 |
| **OS-03** | ROC-X1 derived cache **permitted** — **must not** be sole SoT if POC-03 diverges (OQ-R08 bounded: authoritative sync **forbidden**) |
| **OS-04** | Auto-sync from Tracking as **authoritative** catalog update **forbidden** — RAP-06, OQ-R08 |

### Playbook write plane separation

| Playbook | Registry facet interaction |
|----------|---------------------------|
| **01** | Manifest-enrolled — **precondition** for catalog; RT-G05 **does not** participate |
| **02** | Enrolled → **triggers** ROC-* bind obligation (MVP C4) |
| **03** | **Read** ROC-01 for portfolio select → MOC-01 → POC-03…07 |
| **04** | **Mutates** POC-03…POC-07 only — catalog **does not** receive gate outcomes; ROC-08 **may** lag until operator refresh |
| **05** | **May update** ROC-07 archived category — **orthogonal** to POC-08 primary write |

**Principle TRK-IMPL-01:** Operator answering seven/eight Tracking questions **never** uses Registry as primary surface — only Manifest → Tracking → Surface path (RE-01).

**Principle TRK-IMPL-02:** Playbook 04 declaration **must not** silently append gate rows into POC-02 registry facet — INT-R06.

### Default vs extended portfolio view (OQ-R03 — bounded)

| Rule ID | Implementation rule |
|---------|---------------------|
| **VIEW-01** | **Default MVP:** ROC-01 listing exposes **discoverable** active entries per RD-03 |
| **VIEW-02** | ROC-07 **must persist** withdrawn/archived categories — extended view filtering **RT-G12 display policy**, not registry omission |

---

## Integrity Model

Minimum registry catalog integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Implementation expectation |
|----|----------|---------------------------|
| **INT-R01** | **Enrollment-before-bind honesty** | ROC-09 **must** reference Playbook 02 Enrolled act — bind **without** prior enrolled **forbidden** |
| **INT-R02** | **Single catalog aggregate** | Exactly **one** ROC-01 at MVP — no competing portfolio listings |
| **INT-R03** | **One entry per logical identity** | At most **one** ROC-02 per logical Factory Project — RA-03 |
| **INT-R04** | **Two-identifier discipline** | ROC-03 registry entry ID **≠** ROC-04 logical identity — ES-03 |
| **INT-R05** | **Manifest pointer validity (minimal)** | ROC-05 **must** resolve to existing MOC-01 — broken pointer **visible** to operator |
| **INT-R06** | **Plane separation** | POC-02 registry facet **must not** embed POC-04/POC-05 live tails as co-authoritative (RA-05) |
| **INT-R07** | **Declaration plane isolation** | Playbook 04 acts **must not** mutate ROC-* as automatic side effect — catalog amend **separate operator act** |
| **INT-R08** | **Orientation snapshot honesty** | ROC-08 **matches** POC-03 active state **or** marked stale/invalid/unset — RS-03 |
| **INT-R09** | **Catalog amendment narrative** | ROC-10 append-oriented — withdrawal/rebind **via** new events, not silent delete (RAP-17) |
| **INT-R10** | **Human-only bind path** | Only operator catalog enrollment/withdrawal/amend acts **authoritatively change** ROC-* — OA-ACT-04, SC-03 |
| **INT-R11** | **Summary follows source** | ROC-06 **follows** MOC-03…05/charter amendments — **does not lead** charter changes (RM-03) |

### What integrity model explicitly excludes

| Excluded | Reason |
|----------|--------|
| Automated schema validation of registry facet | RT-G11 post-MVP |
| RRDY pass/fail re-evaluation engine | Playbook 02 owns attestation |
| CI/git-hook auto-enrollment | INT-R10, RAP-10 |
| Cross-record referential integrity engine | Single-operator MVP; operator resolves |
| Duplicate detection automation across identities | OQ-R04 — operational + future tooling |
| Automated sync catalog ↔ tracking as authority | OQ-R08 bounded — forbidden |

### Integrity verification (human-operated)

MVP **accepts** operator manual review: Playbook 02 checklist, portfolio integrity review, Playbook 03 select path surfaces ROC-05/MOC-01 mismatches and ROC-08/POC-03 drift. Formal validators **deferred**.

---

## Boundary Protection

RT-G05 registry implementation **must never become** the following — inherited from Registry Charter, planning charter, RT-G04/RT-G10 separation, MVP exclusions.

### Forbidden system roles

| Registry implementation must not become | Guard |
|------------------------------------------|-------|
| **Manifest / per-project minimum understanding store** | RAP-07, MR-02; RT-G10 separate |
| **Tracking composition / live observability index** | RAP-06, RA-05; POC-03…07 |
| **Tracking Surface / operator dashboard** | RAP-05; RT-G12 separate |
| **Persistence substrate product** | RAP-01; RT-G04 owns zone |
| **Database / query engine / multi-tenant store** | RAP-01; DF-02 sufficient |
| **Workflow engine / state machine executor** | RAP-03; RT-G01 |
| **Factory runtime product** | SC-01; RT-G09 |
| **Queue / scheduler / prioritization** | RAP-04; RT-G06 |
| **Project management system** | Tasks, sprints beyond distinction summary — **out of scope** |
| **Portfolio analytics platform** | Cross-project gate rollups, KPI dashboards — RA-05 extension |
| **CRM / client relationship system** | No contact/deal pipeline ownership |
| **Passport / unified project mega-document** | RAP-08, BV-15 |
| **Site Type Registry** | RAP-11; Foundation T1 |
| **Discovery crawler / git folder scanner** | RAP-10, RD-04 |
| **Agent registry / MCP tool catalog** | RAP-18 |
| **Automation / agent enrollment** | Playbook 02 forbidden automation |
| **Closure registry / terminal workflow engine** | Playbook 05 + POC-08 primary |
| **Foundation authority merge** | RAP-12 |
| **Implementation spec documents** (FACTORY-PROJECT-INDEX, DISCOVERY, PASSPORT) | RAP-14 |
| **Engine Stage 7 / multi-project Engine** | RE-02 |

### Forbidden content inside registry facet

| Must never persist as registry-owned authoritative content | Actual owner |
|-------------------------------------------------------------|--------------|
| Live gate outcome rows | POC-04 |
| Live handoff event sequence | POC-05 |
| Full state history | POC-03 |
| Declaration event bodies | POC-06 |
| Progression ledger | POC-07 |
| MOC-* minimum understanding bodies | POC-02 manifest facet |
| MOC-08 full topology map | Manifest Category 7 |
| Layer artefact bodies | External workspaces |
| Gate/handoff criteria text | Runtime Architecture |
| Site Type Registry definitions | Foundation `registry/` |
| Eight Surface answers | RT-G12 read composition |
| Queue rank among projects | RT-G06 |

### Implementation anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| Single «registry.yaml» swallowing catalog + manifest + tracking | ROC-RULE-03; POC-RULE-02 |
| Catalog card containing seven Surface answers | RA-05; RE-01 |
| Physical bind **before** Playbook 02 Enrolled | INT-R01; BIND-01 |
| Registry impl **precedes** MOC-01 per entry | G04-IMPL-02; REG-IMPL-02 |
| Registry bind triggering automated POC-03 mutation | INT-R07; TRK-IMPL-02 |
| Deploy / go-live conflated with catalog «completion» | RAP-15 |
| Conflating Site Type Registry with Factory Project Registry | RAP-11 |
| Silent deletion of enrollment history | INT-R09; RAP-17 |
| Registry as **central** Engine for all projects | RE-02 |
| Manifest enrollment side-effect creating ROC-02 | Playbook 01 explicit block |
| Portfolio CRM fields (contacts, revenue, pipeline stage) | Scope creep — **not** Registry v1 |

**Principle BP-IMPL-01:** Physical registry catalog binding **extends operability** of portfolio discoverability doctrine — **does not execute** Factory movement, **does not replace** Engine declaration authority, **does not manage** projects.

**Principle BP-IMPL-02:** Registry remains **Portfolio Discoverability Layer** — **many projects listed**, **one Engine depth per project**, **not** a platform.

---

## RT-G12 Handoff Assumptions

RT-G12 Surface Implementation Standard **may assume** the following from RT-G05 Registry Implementation Standard — **without** RT-G12 redefining registry doctrine or catalog enrollment.

### Guaranteed registry provisions for Surface

| Assumption ID | RT-G12 may assume |
|---------------|-------------------|
| **R-H01** | ROC-01 portfolio catalog aggregate **exists or will exist** when operator uses portfolio path — **optional** for single-project Factory work |
| **R-H02** | Each ROC-02 discoverable entry exposes ROC-05 pointer to **one** stable MOC-01 |
| **R-H03** | ROC-06 distinction summaries sufficient for **portfolio select** — **not** for eight Surface questions |
| **R-H04** | ROC-07 discoverability status enables default portfolio filtering (VIEW-01) |
| **R-H05** | Registry facet **does not embed** POC-03…POC-07 live indexes — Surface depth **reads** per-project substrate after select |
| **R-H06** | ROC-08 orientation snapshot, if present, is **non-authoritative** — Surface **must not** treat as SRDY-* SoT |
| **R-H07** | RT-G12 **never writes** ROC-* — read-oriented portfolio consumer only (G05-REL-01) |
| **R-H08** | Playbook 03 portfolio session **may** start from ROC-01 select — **must not** answer eight questions at portfolio level (G05-REL-03) |
| **R-H09** | Withdrawn/archived ROC-07 entries **may be hidden** in default view — extended view policy **RT-G12** (VIEW-02, OQ-R03) |
| **R-H10** | Catalog enrollment (Playbook 02) and RRDY attestation **remain outside** RT-G12 — Surface **does not** evaluate RRDY-* |

### Explicitly **not** provided to RT-G12 (RT-G12 must decide)

| Topic | Owner |
|-------|-------|
| Surface read binding serialization / form factor (DF-07) | RT-G12 standard |
| SRDY-* read composition rules per question | RT-G12 standard |
| How eight questions aggregate from POC-03…07 + MOC-* | RT-G12 standard |
| Whether portfolio select UI is markdown index, CLI, or static HTML | RT-G12 standard (TX-07: not dashboard product) |
| Integrity warning display when MOC-07/POC-03 diverge | RT-G12 standard |
| SRDY-07 recency binding from POC-06/07 (OQ-PD05) | RT-G12 + RT-G04 coordination |

### Dependency edge (implementation sequence)

```text
  RT-G04 Implementation Standard
       │ hosts POC-02 registry facet locus
       ▼
  RT-G10 Manifest Implementation Standard
       │ MOC-01…M-H10
       ▼
  RT-G05 Registry Implementation Standard (this)
       │ populates ROC-* ; R-H01…R-H10
       ▼
  RT-G12 Surface Implementation Standard
       │ optional ROC-01 select → MOC-01 + POC-03…07 read
```

**Principle HAND-R01:** RT-G12 **must not** require registry facet redesign — DF-07, SRDY-*, OQ-PD05 resolve **within** RT-G12 bounds using R-H01…R-H10, not by expanding registry scope.

**Principle HAND-R02:** RT-G12 **must not** implement portfolio-scale Surface session — one Playbook 03 session = **one** Factory Project after select (G05-REL-03).

---

## Explicit Non-Claims

This document and the RT-G05 Registry Implementation Standard it defines:

- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **storage product**, **database**, **ORM**, or **multi-tenant** persistence service;
- **are not** **application**, **standalone service**, **SaaS**, or **HomeGateway** integration;
- **are not** **automation layer**, **agent orchestration**, **queue**, or **validator engine**;
- **are not** **operator UI**, **dashboard**, **portfolio analytics platform**, or **CLI** (RT-G12);
- **are not** **Manifest serialization standard** (RT-G10) or **Surface read standard** (RT-G12);
- **are not** **Persistence Substrate standard** (RT-G04) — only **consumption** of P3, POC-02, zone discipline;
- **are not** **Registry Charter** rewrite — doctrine taken as authoritative input;
- **are not** Playbooks 01–05 rewrite;
- **do not** define JSON/YAML/markdown schemas, field lists, folder trees, file naming, or database tables;
- **do not** create physical artefacts under `workspaces/website-factory-operations/`;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound registry catalog;
- **do not** claim registry catalog records **exist on disk** today — **SAFE UNKNOWN** until separately created.

Human-operated catalog enrollment path remains the v1 model per Operational Model OA-ACT-04 and Playbook 02.

Registry remains **Portfolio Discoverability Layer** — **not** Manifest, Tracker, CRM, Analytics System, Workflow Engine, Project Manager, or Dashboard.

### Resolved in this standard (were OPEN in planning)

| ID | Resolution |
|----|------------|
| **OQ-R01** | TOP-01…TOP-04 — central ROC-01 aggregate with per-entry pointers; not distributed-only |
| **OQ-R02** | ROC-02 composition of ROC-03…ROC-11 — object classes as card template; no field list |
| **OQ-RE05** | BIND-01…BIND-04 — enrolled precedes bind; same session permitted; discovery forbidden |
| **OQ-R03** | VIEW-01…VIEW-02 — default discoverable; extended view RT-G12; ROC-07 persists all statuses |
| **OQ-R08** | OS-03, OS-04 — authoritative auto-sync **forbidden**; derived cache optional non-authoritative |

### Deferred (not blockers for this standard)

| ID | Disposition |
|----|-------------|
| **OQ-R04** | Duplicate detection across logical identities — operational + future tooling |
| **OQ-R05** | PHASE_SLICE — one catalog entry per shell vs per slice — Engine v2 or case policy |
| **OQ-R06** | ROC-11 external workspace pointer — optional; operational per case (DF-08) |
| **OQ-R07** | RT-G06 queue relationship to catalog entry — queue charter |
| **OQ-R09** | MIG / incoming request correlation — RT-G08 integration charter |
| **DF-04…DF-10** | Internal zone layout, git policy, pilot pointer policy — cross-charter operational |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — RT-G04 standard records authorized zone |
| Whether any registry catalog binding records **exist** in-repo | **UNKNOWN** — standard authorizes; creation not part of deliverable |
| Calendar for RT-G12 Implementation Standard | **not scheduled** |
| Triumph / pilot workspaces in ROC-11 vs external-only | **UNKNOWN** — DF-08 per case |
| Operators updated NEXT-PRIORITIES to Implementation Standards era (RT-G05 complete) | **UNKNOWN** |

---

*RT-G05 Registry Implementation Standard v1 — third Website Factory Implementation Standard. Canonical location: `workspaces/website-factory-reference-v1/RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G05 Registry Implementation Standard v1

**Stage:** RT-G05 — Registry Implementation Standard (post–Planning Charter, third Implementation Standard)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md` (created)  
**Summary:** Третий Implementation Standard Website Factory: перевод Registry Charter и RT-G05 planning charter в конкретную MVP-модель физического существования Registry catalog binding — одиннадцать implementation object classes (ROC-01…ROC-11), ownership matrix (owns / references / never owns), RRDY-* implementation expectations, RT-G04 binding через P3/POC-02, relationships к RT-G10 (M-H01…M-H10 consumption) и Tracking (RE-01, RA-05), minimum integrity model, boundary protection (Portfolio Discoverability Layer ≠ Manifest/Tracker/CRM/Analytics/Dashboard), RT-G12 handoff assumptions R-H01…R-H10; resolved OQ-R01 (TOP-* central aggregate), OQ-R02 (ROC composition as card template), OQ-RE05 (BIND-*), OQ-R03 (VIEW-*), OQ-R08 (bounded) — без runtime, schemas, folders, code и physical artefacts.  
**Git:** no commit, no push (per task; document does not recommend commit).
