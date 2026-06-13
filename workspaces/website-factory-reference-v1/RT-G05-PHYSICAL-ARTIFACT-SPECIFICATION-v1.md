# REPORT — RT-G05 Physical Artifact Specification v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical Artifact Specification Era — **RT-G05 physical artifact specification only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE**; Physical MVP Artifact Definition **COMPLETE**; RT-G04 Physical Artifact Specification **COMPLETE**; RT-G10 Physical Artifact Specification **COMPLETE**  
**Тип:** physical artifact specification only — **без** artifact creation, folder creation, file creation, serialization format, naming conventions, schemas, layout design, runtime, automation, workflow engine  
**Upstream:** [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md), [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md)  
**Also reviewed:** [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md), [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), Operational Playbooks 01–05  
**Связь:** [RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md](RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md)

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-05** | Central registry aggregate ROC-01 at portfolio scope (TOP-01) |
| **DF-06** | No HomeGateway dependency |

---

## Purpose

### Зачем существует RT-G05 Physical Artifact Specification

**RT-G05 Physical Artifact Specification v1** переводит принятые implementation и review артефакты в **полную нормативную модель физической реальности** Registry catalog binding — определяя **какие физические Registry artifacts существуют**, **что авторитетно**, **как классы связаны** с RT-G04 substrate, Manifest и Tracking, **какие обязательства и гарантии** Registry несёт для downstream standards — **без** создания артефактов на диске и **без** выбора serialization format.

| Upstream отвечает | Эта specification отвечает |
|-------------------|---------------------------|
| Registry Charter — **doctrinal role** portfolio discoverability layer | **Физическая модель** Registry catalog binding как normative artifact reality |
| RT-G05 Implementation Standard — **ROC classes** и implementation obligations | **Завершённая specification** artifact class model, authority, relationships, guarantees |
| RT-G04 Physical Artifact Specification — **POC-02 registry facet carrier** | **ROC-* content reality** within that carrier — без substrate redesign |
| RT-G10 Physical Artifact Specification — **MOC-01 anchor** per project | **ROC-05 pointer chain** и distinction echo discipline |
| Physical MVP Definition Review — **Wave 1 ROC inventory** | **RT-G05 scope only** — ROC-01…ROC-11, ROC-X1, ROC-O1 и их физические обязательства |
| RT-G12 standard — consumption of registry provisions | **Handoff assumptions** registry → Surface **без** serialization design |

### Нормативная формулировка physical artifact responsibility

**RT-G05 Physical Registry Artifacts (MVP specification)** — **авторизованные structured filesystem records** классов ROC-01…ROC-11 (и опциональных ROC-X1, ROC-O1), **материализованные внутри** POC-02 registry facet at portfolio scope на RT-G04 substrate, которые operator **читает и вручную создаёт/обновляет** после Playbook 02 registry-enrolled и operator catalog bind act — **без** shipped runtime, **без** automated catalog enrollment on discovery и **без** определения формата сериализации.

Registry physical artifacts **материализуют** portfolio listing (C4, S3) и RRDY-* categories — **не** Manifest, **не** Tracking composition, **не** Surface display, **не** CRM, **не** project manager.

### Specification purpose statement

Physical artifact specification **материализует** единую физическую модель Registry catalog binding, на которой:

1. **ROC-01** определяет canonical portfolio catalog aggregate — MVP hinge (S3, C4, TOP-01).
2. **ROC-02…ROC-11** определяют per-entry catalog slot composition — discoverability, distinction, manifest pointer.
3. **ROC-09** связывает physical bind с prior Playbook 02 doctrinal enrollment act.
4. **Authority, reference, optional, and prohibited** components формализованы с явным precedence.
5. **Physical obligations и guarantees** определяют минимум для valid Registry-bound Factory Project portfolio view и downstream handoff к RT-G12.

Specification **не создаёт** physical artifacts — она **определяет физическую реальность Registry**, которую authorized creation track должен реализовать.

---

## Foundation Dependencies

Specification **наследует** upstream артефакты **без их переопределения**.

### Tier 0 — Implementation standard, substrate and manifest specifications, reviews

| Document | Specification использует |
|----------|-------------------------|
| [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md) | ROC-01…ROC-11 taxonomy; ROWN-*; RRDY-IMPL-*; INT-R01…R11; TOP-*, BIND-*, OS-*, VIEW-*; R-H01…R-H10 |
| [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md) | LOC-ZONE; POC-02 registry facet; G05-01…G05-07; REL-04, REL-12; PS-01…PS-05 |
| [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md) | MOC-01…MOC-05; M-H01…M-H10; REL-M08…REL-M12; M-G05-01…M-G05-10 |
| [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md) | Wave 1 ROC disposition; mandatory/optional/forbidden; Phase C creation sequence |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Scope Categories 1–7, RRDY-*, RD-*, RA-*, RM-*, RE-*, RS-*, RAP-* — **sole doctrine source** |

### Tier 1 — Operational doctrine and playbooks

| Document | Specification использует |
|----------|-------------------------|
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — catalog-discoverable outcome; RRDY evaluation; enrollment/withdrawal acts |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — manifest-enrolled precondition for catalog bind |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — portfolio select; RE-01 |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — separate write plane; catalog **does not** receive gate outcomes |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — archived catalog category; withdrawal orthogonal to Factory-track closure |
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; operator path Registry→Manifest→Tracking→Surface; Decision class **I** |

### Tier 2 — Downstream standards (consumers of registry physical reality)

| Standard | Constraint on RT-G05 specification |
|----------|-------------------------------------|
| RT-G12 Surface Read Binding Standard | SOC-10 optional portfolio select; reads ROC-01; **never writes** ROC-* |

**Authority precedence:** Foundation Freeze + Engine → Registry Charter (doctrine) → Manifest Charter (doctrine) → RT-G04 Physical Artifact Specification → RT-G10 Physical Artifact Specification → RT-G05 Implementation Standard → **эта specification** → physical creation (separate authorization) → RT-G12 physical specification track (separate deliverable).

**Scope boundary (SPEC-SCOPE-03):** Эта specification covers **RT-G05 ROC classes only** — content within POC-02 registry facet at portfolio scope. POC substrate classes, MOC manifest classes, SOC read composition belong to **separate standard-specific tracks** — RT-G04, RT-G10, RT-G12 respectively.

---

## Registry Artifact Class Model

Normative **classes** — не file names, не schemas, не folder trees, не serialization labels.

### Authoritative registry classes (ROC-01…ROC-11)

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **ROC-01** | **Catalog aggregate** | Portfolio-scope canonical listing container — materialization of «which Factory projects exist» | Operator locates portfolio listing **without** repo-wide search; one central aggregate at MVP | **Must persist** when any catalog entry bound |
| **ROC-02** | **Catalog entry** | One discoverability slot per logical Factory Project in portfolio view | Holds per-project catalog card composition; exactly one slot per logical identity | **Must persist** per enrolled project |
| **ROC-03** | **Registry entry identity** | Index slot identifier — **distinct** from logical Factory Project identity (RA-03, ES-03) | Two-identifier discipline; catalog slot ID ≠ Engine identity | **Must persist** per ROC-02 |
| **ROC-04** | **Logical identity reference** | Stable pointer to Engine identity shell (Category 2) | Links catalog slot to MOC-02 / POC-01 on substrate | **Must persist** per ROC-02 |
| **ROC-05** | **Manifest pointer** | Stable reference to per-project MOC-01 entry anchor (Category 3, RM-01) | Hard pointer — registry **points**, manifest **orients** | **Must persist** per discoverable ROC-02 |
| **ROC-06** | **Distinction summary** | Portfolio-safe charter label, scope tier, endpoint summary categories (Category 4) | Echoes MOC-03…MOC-05 — **not** full Manifest bodies | **Must persist** per ROC-02 |
| **ROC-07** | **Discoverability status** | Catalog lifecycle category: discoverable / withdrawn / archived (Category 6) | Catalog visibility — **not** Runtime state | **Must persist** per ROC-02 |
| **ROC-08** | **Orientation snapshot** | Non-authoritative portfolio glance — active state, track flags (Category 5) | **Glance or omitted** — **must not** duplicate live gate index | **Optional** — default absent (OS-01) |
| **ROC-09** | **Enrollment bind metadata** | Physical bind linkage to Playbook 02 Enrolled act | Enrollment-before-bind honesty | **Must persist** on catalog entry bind |
| **ROC-10** | **Catalog amendment narrative** | Enrollment, withdrawal, re-enrollment, distinction update — append-oriented (RS-01, RAP-17) | Catalog lifecycle audit trail | **Must persist** when catalog lifecycle events occur |
| **ROC-11** | **External workspace pointer** | Optional charter-declared external ref category on catalog card (Category 7) | Pointer only — refs external loci | **May persist** — refs only |

### Optional / subordinate registry classes

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **ROC-X1** | **Derived orientation cache** | Regeneratable portfolio glance from Tracking read — POC-D1 analog at catalog level | Non-authoritative convenience; **must not** be sole SoT if POC-03 diverges | **Optional** — default absent; OQ-R08 bounded |
| **ROC-O1** | **Pre-bind enrollment draft** | Pre-physical-bind notes before Playbook 02 Enrolled | Supports OQ-RE05; **not authoritative** until bind act | **Optional** — non-authoritative |

### Class composition model (conceptual — not layout)

```text
  workspaces/website-factory-operations/          ← RT-G04 LOC-ZONE
  │
  ├── portfolio scope
  │     └── POC-02 registry facet (binding carrier)
  │           ├── ROC-01 Catalog aggregate ◀── MVP hinge (S3, C4, TOP-01)
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

### Class principles

| ID | Principle |
|----|-----------|
| **ROC-RULE-01** | Exactly **one** canonical ROC-01 catalog aggregate at MVP — no competing portfolio listings (TOP-01) |
| **ROC-RULE-02** | Exactly **one** ROC-02 catalog entry **per** logical Factory Project identity — duplicate slots **forbidden** (RA-03) |
| **ROC-RULE-03** | POC-02 registry facet **must remain** a **distinct record class** from POC-02 manifest facet and POC-03…POC-07 tracking indexes — co-location within authorized zone **permitted**; collapse into undifferentiated mega-record **forbidden** |
| **ROC-RULE-04** | ROC-05 **must** resolve to exactly **one** stable MOC-01 per catalog entry — registry **points**, manifest **orients** |
| **RTG05-CLASS-01** | RT-G05 specification covers **ROC-* classes only** — POC carrier existence is RT-G04; MOC/SOC physical shape deferred to downstream tracks |

### Charter scope category → physical class mapping

| Charter scope category | Physical classes |
|------------------------|------------------|
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

### Portfolio catalog topology (resolved — inherited from implementation standard)

| Rule ID | Physical specification rule |
|---------|------------------------------|
| **TOP-01** | **Default MVP:** one **central** ROC-01 catalog aggregate at portfolio scope within authorized zone |
| **TOP-02** | Each ROC-02 entry **holds pointers** to per-project record home and MOC-01 — **not** a distributed-only model without aggregate |
| **TOP-03** | Pure «filesystem discovery» of per-project homes **does not** substitute ROC-01 — catalog aggregate **required** for C4/S3 |
| **TOP-04** | Serialization format choice **does not** determine topology — ROC class separation **is normative** |

### Index card template (resolved — object classes, not fields)

**OQ-R02 resolution (inherited):** «Index card template» = **ROC-02 composition** of ROC-03…ROC-11 mandatory/optional classes per rules above — **not** a field list, **not** a schema. Distinction content **sources** from MOC-03…MOC-05 (M-H05) and operator charter — registry **echoes summaries**, **does not** author charter bodies.

---

## Authority Model

### Four registry content categories

| Category | ROC classes | Authority rule |
|----------|-------------|----------------|
| **Authoritative registry content** | ROC-01…ROC-07, ROC-09, ROC-10 | Must survive between sessions; loss breaks portfolio discoverability (C4/S3) and operator select path without workspace archaeology |
| **Optional non-authoritative slice** | ROC-08, ROC-11 | May be absent; when present ROC-08 is **glance-only**; ROC-11 pointer-only |
| **Subordinate / derived** | ROC-X1 | Default absent; if present **must be labeled** derived/subordinate — never co-authoritative with POC-03…POC-05 |
| **Operational / pre-bind** | ROC-O1 | Pre-bind notes; **must not** substitute ROC-09 enrollment metadata or ROC-02…07 authoritative content |

### Authority matrix by class

| Class | Authoritative for | Not authoritative for | Write authority |
|-------|-------------------|----------------------|-----------------|
| **ROC-01** | Portfolio catalog aggregate identity; «which projects exist» listing | Per-project tracking depth; manifest categories; Surface answers | Operator catalog bind act (post Playbook 02) |
| **ROC-02** | Catalog entry slot existence per logical project | Manifest minimum understanding; live gate index | Operator Playbook 02 Enrolled + bind act |
| **ROC-03** | Registry entry index slot identity | Logical Factory Project identity definition | Operator bind act — **distinct** from ROC-04 |
| **ROC-04** | Logical identity **reference** on catalog card | Engine identity shell semantics — Engine owns | Operator bind act |
| **ROC-05** | Manifest entry **pointer** to MOC-01 | MOC-* content; per-project minimum understanding | Operator bind act |
| **ROC-06** | Distinction **summary categories** on card | Full charter bodies; Site Type Registry authority | Operator bind + amendment following MOC-03…05 source |
| **ROC-07** | Catalog discoverability lifecycle category | Runtime state; gate-complete status | Operator enrollment / withdrawal / archive declaration |
| **ROC-08** | — (orientation glance only) | Active state truth — POC-03 owns | Operator optional update — **not** Playbook 04 side effect |
| **ROC-09** | Enrollment-to-bind linkage | Doctrinal enrollment itself (Playbook 02 outcome) | Operator bind act |
| **ROC-10** | Catalog amendment / withdrawal narrative | Tracking indexes; declaration bodies | Operator explicit catalog lifecycle acts — append-oriented |
| **ROC-11** | External workspace **locator** on card | External bodies | Operator bind/amendment when declared |
| **ROC-X1** | — (derived cache only) | Live gate/handoff index | Operator-labeled derived refresh — auto-sync **forbidden** |
| **ROC-O1** | — | Any bind authority | Operator notes only |

### Authoritative vs referenced vs optional vs prohibited — summary

| Disposition | Components | Precedence when conflict |
|-------------|------------|-------------------------|
| **Authoritative (registry-owned)** | ROC-01…ROC-07, ROC-09, ROC-10 | Manifest facet **wins** for stable categories over ROC-06 echo on conflict (M-H10); POC-03 **wins** over ROC-08 orientation |
| **Referenced (registry-indexed, not owned)** | MOC-01…MOC-05 via ROC-05; MOC-02 via ROC-04; POC-01 identity shell; per-project LOC-HOME; POC-08 closure outcome | MOC-* **wins** over ROC-06 on amendment conflict; POC-03 **wins** over ROC-08 |
| **Optional** | ROC-08, ROC-11, ROC-X1, ROC-O1 | Absence **valid** for S3 — ROC-06 distinction sufficient (OS-01) |
| **Prohibited inside registry facet** | Live gate/handoff rows; declaration bodies; MOC-* minimum understanding bodies; eight Surface answers; layer bodies; queue rank | Actual owners per Boundary Protection section |

### Authority precedence rules

| Rule ID | Precedence |
|---------|------------|
| **AUTH-R01** | MOC-03…MOC-05 stable categories **win over** ROC-06 distinction summaries on conflict — M-H10 |
| **AUTH-R02** | ROC-10 amendment narrative **append-only** — withdrawal/rebind **via** new events, not silent delete (RAP-17) |
| **AUTH-R03** | POC-03 active state **wins over** ROC-08 orientation snapshot when both present — RS-03 |
| **AUTH-R04** | POC-04/POC-05 live indexes **win over** any ROC-X1 or frozen ROC-08 copy (RA-05, OS-04) |
| **AUTH-R05** | Playbook 04 **must not** silently mutate ROC-* as automatic side effect — catalog amend **separate operator act** (INT-R07) |
| **AUTH-R06** | Only Factory operator **authoritatively creates/updates** ROC-* — Playbook 02 attestation **precedes** bind (INT-R10) |
| **AUTH-R07** | RT-G12 Surface **reads** ROC-01 for optional portfolio select — **never writes** ROC-* authoritative content (R-H07) |
| **AUTH-R08** | Logical Factory Project **precedes** catalog entry; manifest anchor **precedes** registry bind per entry (MR-01, REG-REL-01) |

### Ownership summary

| Layer | Owns registry physical artifact reality | Does not own |
|-------|----------------------------------------|--------------|
| **RT-G04 substrate** | LOC-ZONE; POC-02 registry facet **carrier** at portfolio scope | ROC-* content; catalog card serialization format |
| **RT-G10 manifest** | MOC-* within per-project POC-02 manifest facet | Portfolio catalog; registry lifecycle |
| **RT-G05 (this specification)** | ROC-* content within POC-02 registry facet; portfolio listing | Per-project manifest depth; tracking indexes; Surface display |
| **Playbook 04 / Tracking** | POC-03…POC-07 authoritative indexes | Catalog membership; distinction summaries authority |
| **RT-G12 Surface** | SOC-* read composition; optional SOC-10 portfolio select assist | Any authoritative ROC-* write |

---

## Relationship Model

### Registry within substrate (RT-G04)

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-R01** | ROC-* **reside within** POC-02 registry facet at portfolio scope in LOC-ZONE | G05-01; REL-04 — substrate hosts carrier; RT-G05 defines content |
| **REL-R02** | ROC-01 **exists at** portfolio scope — **not** inside per-project LOC-HOME | PS-01, PS-02 — portfolio vs project scope separation |
| **REL-R03** | ROC-05 **points across** POC-02 facets to MOC-01 in per-project manifest facet | REL-12; G05-04 — cross-facet pointer chain |
| **REL-R04** | ROC-04 **aligns with** MOC-02 / POC-01 on referenced per-project home | ROC-03 remains distinct index slot — ES-03 |
| **REL-R05** | POC-02 registry facet and POC-02 manifest facet **must remain separate record classes** | ROC-RULE-03, COL-R02 — co-location within zone permitted; class separation mandatory |
| **REL-R06** | ROC-09 **must reference** prior Playbook 02 doctrinal enrollment — bind **follows** enrolled | BIND-01; INT-R01 — discovery bind **forbidden** |
| **REL-R07** | Registry facet **must not** embed POC-03…POC-07 tracking depth | INT-07, G05-02, RA-05 |

### Registry ↔ Manifest (RT-G10)

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-R08** | MOC-01 **precedes** ROC-05 catalog pointer per enrolled project | MR-01, REG-REL-01, REL-M08; registry bind **must not** precede stable MOC-01 |
| **REL-R09** | MOC-02 logical identity **precedes** ROC-03 registry entry ID | ES-03, RA-03 — distinct identifiers |
| **REL-R10** | MOC-03…MOC-05 **supply source categories** for ROC-06 — registry **echoes**, manifest **does not require** catalog slot | M-H05; RM-02 |
| **REL-R11** | Manifest facet **persists** when catalog withdrawn — ROC-07 status **orthogonal** | M-H06; Playbook 05 CL-03 analog |
| **REL-R12** | Registry facet **must not embed** MOC-* minimum understanding bodies | M10-IMPL-01; REG-IMPL-01 |
| **REL-R13** | MOC-08 topology **not required** on catalog card — ROC-05 pointer to MOC-01 **sufficient** | M-H07 |

### Registry ↔ Tracking

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-R14** | Registry **never** substitutes Tracking at portfolio scale — seven/eight questions answered per-project only | RA-05, RE-01, TRK-IMPL-01 |
| **REL-R15** | ROC-08 orientation snapshot, if present, **reconcilable with** POC-03 or flagged stale | RS-03; OS-02 |
| **REL-R16** | Playbook 04 **mutates** POC-03…POC-07 only — ROC-08 **may lag** until operator refresh | INT-R07; TRK-IMPL-02 |
| **REL-R17** | Catalog membership **≠** gate-complete or surface-ready | Registry-ready ⊄ fully trackable; Playbook 03 may open on early discoverable entry |
| **REL-R18** | Auto-sync from Tracking as **authoritative** catalog update **forbidden** | OS-04; RAP-06; OQ-R08 bounded |
| **REL-R19** | Single-project path **without** catalog remains valid — RT-G12 **not required** to consume ROC-01 | M-H03; G05-REL-02 |

### Registry ↔ Playbooks

| Playbook | Registry facet interaction | Physical record classes |
|----------|---------------------------|-------------------------|
| **01** Manifest enrollment | Manifest-enrolled — **precondition** for catalog; RT-G05 **does not** participate in bind | **None** in registry facet until Playbook 02 |
| **02** Registry enrollment | Enrolled → **triggers** ROC-* bind obligation (MVP C4) | ROC-01, ROC-02…ROC-10 per rules |
| **03** Surface session | **Read** ROC-01 for portfolio select → ROC-05 → MOC-01 → POC-03…07 | Read ROC-*; **must not** answer eight questions at portfolio level |
| **04** Project declaration | **Mutates** POC-03…POC-07 only — catalog **does not** receive gate outcomes | No automatic ROC-* mutation |
| **05** Project closure | **May update** ROC-07 archived category — **orthogonal** to POC-08 primary write | Optional ROC-07; ROC-10 amendment |

### Lifecycle dependency graph

```text
  PRE-FACTORY (no zone catalog records)
       │
       ▼
  Playbook 01 + RT-G10 ──▶ MOC-01…MOC-12 on per-project LOC-HOME
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

| Rule ID | Physical specification rule |
|---------|------------------------------|
| **COL-R01** | POC-02 registry facet (portfolio) and per-project POC-02 manifest facet **share** authorized zone — **different scope** |
| **COL-R02** | **Must remain** separate **record classes** — ROC-* **must not** merge into MOC-* or POC-03…07 |
| **COL-R03** | **Forbidden:** catalog entry embedding POC-04 gate tail as co-authoritative portfolio SoT |
| **COL-R04** | Internal layout within zone **deferred** — class separation **normative** regardless of co-location |

### Default vs extended portfolio view

| Rule ID | Physical specification rule |
|---------|------------------------------|
| **VIEW-01** | **Default MVP:** ROC-01 listing exposes **discoverable** active entries per RD-03 |
| **VIEW-02** | ROC-07 **must persist** withdrawn/archived categories — extended view filtering **RT-G12 display policy**, not registry omission |

---

## Physical Obligations

### What must physically exist for a valid Registry-bound Factory Project portfolio view

A **valid Registry catalog binding** requires satisfaction of obligations below. Obligations are **class-level** — not file counts or serialization shapes.

**Doctrinal precondition (not a disk artifact):** Playbook 02 registry-enrolled outcome **must precede** physical catalog bind (INT-R01, BIND-01).

**Note:** Single-project Factory path **without** catalog remains doctrinally valid (M-H03) — obligations below are **mandatory for MVP Wave 1 demo track (C4/S3)**, not for all Factory work.

### Tier 0 — Substrate prerequisite (RT-G04)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-R-SUB-01** | **LOC-ZONE** at authorized path | Before any ROC materialization |
| **OBL-R-SUB-02** | **POC-02 registry facet** as binding carrier at portfolio scope | Before catalog bind act |
| **OBL-R-SUB-03** | Per-project **MOC-01** stable on substrate for each ROC-02 entry | Manifest bind **precedes** registry bind |

### Tier 1 — Core catalog binding (C4, S3)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-R-01** | **ROC-01** catalog aggregate | Catalog bind — **core MVP obligation** |
| **OBL-R-02** | **ROC-02** catalog entry per enrolled logical project | Playbook 02 Enrolled + bind act |
| **OBL-R-03** | **ROC-03** registry entry identity **≠** ROC-04 | Catalog bind per entry |
| **OBL-R-04** | **ROC-04** logical identity reference | Catalog bind per entry |
| **OBL-R-05** | **ROC-05** manifest pointer resolving to MOC-01 | Catalog bind per discoverable entry |
| **OBL-R-06** | **ROC-06** distinction summary categories | Catalog bind per entry |
| **OBL-R-07** | **ROC-07** discoverability status category | Catalog bind per entry |
| **OBL-R-09** | **ROC-09** enrollment bind metadata | Catalog bind per entry |

### Tier 2 — Lifecycle-triggered

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-R-10** | **ROC-10** catalog amendment narrative | When enrollment, withdrawal, re-enrollment, or distinction update occurs |
| **OBL-R-08** | **ROC-08** orientation snapshot | **Optional** — if present, non-authoritative per OS-01 |
| **OBL-R-11** | **ROC-11** external workspace pointer | **Optional** — when declared per case (DF-08) |

### Persistent registry inventory by milestone

| Must exist after | Registry physical classes |
|------------------|--------------------------|
| Playbook 02 (doctrinal only) | **None** — doctrinal enrolled, not disk obligation |
| Operator catalog bind | ROC-01; ROC-02…ROC-07, ROC-09 per enrolled project; ROC-05 → MOC-01 |
| Catalog lifecycle event | ROC-10 append entry |
| Playbook 05 closure (optional) | ROC-07 **may** update to archived — **orthogonal** to POC-08 |

### Minimum bootstrap before credible Playbook 03 portfolio select

| # | Physical registry element | Phase reference |
|---|---------------------------|-----------------|
| 1 | Playbook 02 Enrolled outcome recorded (doctrinal) | Pre-bind |
| 2 | ROC-01 catalog aggregate discoverable within authorized zone | Catalog bind |
| 3 | ROC-02 entry per enrolled project with ROC-03≠ROC-04 | Catalog bind |
| 4 | ROC-05 resolves to MOC-01 without workspace archaeology | Catalog bind |
| 5 | ROC-06 distinction summaries present — not full Manifest bodies | Catalog bind |
| 6 | ROC-07 discoverability status explicit | Catalog bind |
| 7 | ROC-08 absent or non-authoritative — no live gate index on card | Catalog bind |
| 8 | Operator selects project from catalog → reaches MOC-01 → Tracking depth | Post-bind verification |

### What is NOT a physical obligation of RT-G05

| Not required by RT-G05 | Owner |
|------------------------|-------|
| MOC-* manifest content | RT-G10 physical specification |
| POC-03…POC-07 tracking index content | Playbook 04; RT-G04 |
| SOC-* read composition | RT-G12 physical specification track |
| Serialization format | Deferred — not in this specification |
| Manifest binding existence for portfolio-only work without enrolled projects | N/A — ROC-01 may list zero entries until enrollment |

---

## Physical Guarantees

RT-G05 physical artifact specification **guarantees** the following to downstream standards **without defining serialization**.

### Guarantees to RT-G12 (Tracking Surface)

| Guarantee ID | RT-G12 may rely on |
|--------------|-------------------|
| **R-G12-01** | ROC-01 portfolio catalog aggregate **exists or will exist** when operator uses portfolio path — **optional** for single-project Factory work (R-H01) |
| **R-G12-02** | Each ROC-02 discoverable entry exposes ROC-05 pointer to **one** stable MOC-01 (R-H02) |
| **R-G12-03** | ROC-06 distinction summaries sufficient for **portfolio select** — **not** for eight Surface questions (R-H03) |
| **R-G12-04** | ROC-07 discoverability status enables default portfolio filtering (VIEW-01, R-H04) |
| **R-G12-05** | Registry facet **does not embed** POC-03…POC-07 live indexes — Surface depth **reads** per-project substrate after select (R-H05) |
| **R-G12-06** | ROC-08 orientation snapshot, if present, is **non-authoritative** — Surface **must not** treat as SRDY-* SoT (R-H06) |
| **R-G12-07** | RT-G12 **never writes** ROC-* — read-oriented portfolio consumer only (R-H07) |
| **R-G12-08** | Playbook 03 portfolio session **may** start from ROC-01 select — **must not** answer eight questions at portfolio level (R-H08, G05-REL-03) |
| **R-G12-09** | Withdrawn/archived ROC-07 entries **may be hidden** in default view — extended view policy **RT-G12** (VIEW-02, R-H09) |
| **R-G12-10** | Catalog enrollment (Playbook 02) and RRDY attestation **remain outside** RT-G12 — Surface **does not** evaluate RRDY-* (R-H10) |

### Guarantees to RT-G10 (Manifest) — consumption symmetry

| Guarantee ID | Manifest may rely on (registry does not violate) |
|--------------|--------------------------------------------------|
| **R-G10-01** | Registry facet **does not embed** MOC-* minimum understanding bodies — pointer and summary echo only |
| **R-G10-02** | Manifest bind **may exist** without any ROC-02 catalog entry — catalog enrollment **optional** per project |
| **R-G10-03** | Withdrawn ROC-07 does **not** revoke MOC-* — manifest persistence **orthogonal** to catalog visibility |

### Guarantees to RT-G04 (Substrate) — hosting symmetry

| Guarantee ID | Substrate may rely on |
|--------------|----------------------|
| **R-G04-01** | RT-G05 **populates** POC-02 registry facet only — **does not** create parallel catalog SoT outside authorized zone (ROWN-01) |
| **R-G04-02** | Registry facet **must not** embed full per-project tracking depth (INT-07) |
| **R-G04-03** | ROC-* content **resides within** portfolio-scope POC-02 registry facet — per-project tracking indexes remain in LOC-HOME |

### Cross-standard guarantee principles

| Principle | Meaning |
|-----------|---------|
| **GUAR-R01** | RT-G05 **populates** POC-02 registry facet; RT-G04 **hosts** carrier — **must not** create parallel catalog SoT outside LOC-ZONE |
| **GUAR-R02** | Physical guarantees are **class-level and locus-level** — not format-specific |
| **GUAR-R03** | Downstream standards **must not** require registry facet redesign — open questions resolve within RT-G12 bounds using R-H01…R-H10 (HAND-R01) |

---

## Integrity Model

Minimum registry catalog integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Physical artifact expectation |
|----|----------|------------------------------|
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

RT-G05 physical registry artifacts **must never become** the following — inherited from Registry Charter, implementation standard, RT-G04/RT-G10 separation, MVP exclusions.

### Forbidden system roles (no registry physical artifact class)

| Registry must not become | Guard |
|--------------------------|-------|
| **Manifest / per-project minimum understanding store** | RAP-07, MR-02; RT-G10 separate |
| **Tracking composition / live observability index** | RAP-06, RA-05; POC-03…07 |
| **Tracking Surface / operator dashboard** | RAP-05; RT-G12 SOC-* separate |
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
| **Runtime object / execution state** | MAP-12 analog; no automated transitions |

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
| Eight Surface answers | RT-G12 SOC-* read composition |
| Queue rank among projects | RT-G06 |

### Forbidden physical anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| Single record swallowing catalog + manifest + tracking + surface | ROC-RULE-03; POC-RULE-02 |
| Catalog card containing seven/eight Surface answers | RA-05; RE-01 |
| Physical bind **before** Playbook 02 Enrolled | INT-R01; BIND-01 |
| Registry bind **precedes** MOC-01 per entry | REL-R08; G04-IMPL-02 |
| Registry bind triggering automated POC-03 mutation | INT-R07; TRK-IMPL-02 |
| Deploy / go-live conflated with catalog «completion» | RAP-15 |
| Conflating Site Type Registry with Factory Project Registry | RAP-11 |
| Silent deletion of enrollment history | INT-R09; RAP-17 |
| Registry as **central** Engine for all projects | RE-02 |
| Manifest enrollment side-effect creating ROC-02 | Playbook 01 explicit block |
| Portfolio CRM fields (contacts, revenue, pipeline stage) | Scope creep — **not** Registry v1 |
| Authoritative auto-sync from Tracking to catalog | OS-04; OQ-R08 |

**Principle BP-R-SPEC-01:** Physical registry catalog binding **extends operability** of portfolio discoverability doctrine — **does not execute** Factory movement, **does not replace** Engine declaration authority, **does not manage** projects.

**Principle BP-R-SPEC-02:** Registry remains **Portfolio Discoverability Layer** — **many projects listed**, **one Engine depth per project**, **not** a platform.

---

## Readiness Model

### RRDY doctrinal readiness vs physical bind completeness

| Concept | Physical specification rule |
|---------|----------------------------|
| **Registry-ready** | Playbook 02 RRDY-* attestation — **prerequisite** for physical bind, **not replaced** by bind |
| **Physical bind complete** | ROC-01 present; ROC-02…ROC-07, ROC-09 **present** per enrolled project; ROC-05 resolves to MOC-01 |
| **Registry-ready ⊄ gate-complete** | Valid catalog entry at `NEW_PROJECT` with **empty** POC-04/POC-05 |
| **Registry-ready ⊄ fully trackable** | Valid discoverable entry with empty indexes — RD discoverable analog |
| **Registry-ready ⊄ surface-ready** | Physical registry bind **does not imply** SRDY-* — per-project indexes separate |
| **Physical bind ⊄ retroactive enrollment** | ROC-09 **must** reference prior Playbook 02 Enrolled act — same-session bind **permitted**; discovery bind **forbidden** |
| **Manifest-ready ⊄ registry-ready** | Manifest-enrolled **required** before registry enrollment — RRDY-02 |

### RRDY → physical class mapping at bind

| ID | Doctrinal criterion | Physical class obligation at bind |
|----|---------------------|-----------------------------------|
| **RRDY-01** | Logical Factory Project identity explicit and Factory-scoped | ROC-04 **must** carry stable logical identity reference — **distinct** from ROC-03 |
| **RRDY-02** | Manifest entry anchor identified (manifest-ready) | ROC-05 **must** reference stable MOC-01 — **hard** per RM-01 |
| **RRDY-03** | Registry entry distinct from logical identity understood | ROC-03 and ROC-04 **must** coexist as **two-identifier** discipline |
| **RRDY-04** | Distinction summaries sufficient for portfolio | ROC-06 **must** persist charter label, scope tier, endpoint **summary categories** |
| **RRDY-05** | Discoverability status category explicit | ROC-07 **must** record catalog lifecycle category at bind |
| **RRDY-06** | Operator understands Registry ≠ Tracking ≠ Manifest | **Not serialized** — Playbook 02 attestation; implementation **must not** create tracking/manifest-substitute on catalog card |

### Stability expectations at physical layer

| Stability class | Physical classes | Rule |
|-----------------|------------------|------|
| **Expected stable** | ROC-04↔ROC-02 binding, ROC-05, ROC-06 stable facets, ROC-09, ROC-10 | Silent identity remap **forbidden** (RS-01) |
| **Expected evolving** | ROC-07, ROC-08, ROC-06 classification echo | **May update**; **must not** freeze live gate index into ROC-08 (RA-05) |

### Physical bind moment (resolved — inherited)

| Rule ID | Physical specification rule |
|---------|------------------------------|
| **BIND-01** | Playbook 02 outcome **Enrolled** **precedes** physical catalog entry bind |
| **BIND-02** | Bind in **same operator session** as Enrolled outcome **permitted** |
| **BIND-03** | Bind triggered by folder/git/workspace discovery **forbidden** — RD-04, RAP-10 |
| **BIND-04** | ROC-O1 pre-bind drafts **not authoritative** until BIND-01 satisfied |

### When RT-G05 Physical Artifact Specification is **complete**

This deliverable is **specification-complete** when:

| Criterion | Status |
|-----------|--------|
| Registry artifact classes defined (ROC-01…ROC-11 + ROC-X1, ROC-O1) | **Yes** |
| Class responsibilities formalized | **Yes** |
| Authority model (authoritative / referenced / optional / prohibited) with precedence | **Yes** |
| Relationship model (RT-G04, Manifest, Tracking, Playbooks; REL-R*) | **Yes** |
| Physical obligations for valid Registry-bound portfolio view stated | **Yes** |
| Physical guarantees to RT-G12 without serialization | **Yes** |
| Minimum integrity expectations stated (no validators) | **Yes** |
| Boundary protection at specification layer | **Yes** |
| RT-G12 handoff assumptions explicit | **Yes** |
| No artifacts, folders, serialization, or layout created | **Yes** |

### What specification-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| Physical ROC-* records **exist** in repo | Specification defines model; creation = separate authorized track |
| Serialization format **chosen** | Explicitly out of scope |
| Portfolio-scope internal layout **designed** | Deferred to future track or operator convention |
| MVP **demonstrated** on pilot | Success S1–S9 post-physical bind |
| `workspaces/website-factory-operations/` **exists on disk** | **SAFE UNKNOWN** until operator creates |

### Specification-complete vs physical creation

```text
  RT-G05 Registry Implementation Standard v1 ── COMPLETE
           │
           ▼
  RT-G04 Physical Artifact Specification v1 ── COMPLETE (substrate + POC carrier)
           │
           ▼
  RT-G10 Physical Artifact Specification v1 ── COMPLETE (MOC-* + M-H01…M-H10)
           │
           ▼
  RT-G05 Physical Artifact Specification v1 ── THIS (specification-complete)
           │
           ├──▶ RT-G12 Physical Artifact Specification (separate track)
           │
           ▼
  Physical artefact creation (catalog bind on pilot) ── ONLY when separately authorized
```

### MVP registry bind readiness checklist (operator, post-specification)

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

## RT-G12 Handoff Assumptions

RT-G12 Surface Physical Artifact Specification (future track) and RT-G12 implementation **may assume** the following from this RT-G05 Physical Artifact Specification — **without** RT-G12 redefining registry doctrine or catalog enrollment.

### Guaranteed registry provisions for Surface (R-H01…R-H10 aligned)

| Assumption ID | RT-G12 may assume |
|---------------|-------------------|
| **R-H01** | ROC-01 portfolio catalog aggregate **exists or will exist** when operator uses portfolio path — **optional** for single-project Factory work |
| **R-H02** | Each ROC-02 discoverable entry exposes ROC-05 pointer to **one** stable MOC-01 |
| **R-H03** | ROC-06 distinction summaries sufficient for **portfolio select** — **not** for eight Surface questions |
| **R-H04** | ROC-07 discoverability status enables default portfolio filtering (VIEW-01) |
| **R-H05** | Registry facet **does not embed** POC-03…POC-07 live indexes — Surface depth **reads** per-project substrate after select |
| **R-H06** | ROC-08 orientation snapshot, if present, is **non-authoritative** — Surface **must not** treat as SRDY-* SoT |
| **R-H07** | RT-G12 **never writes** ROC-* — read-oriented portfolio consumer only |
| **R-H08** | Playbook 03 portfolio session **may** start from ROC-01 select — **must not** answer eight questions at portfolio level (G05-REL-03) |
| **R-H09** | Withdrawn/archived ROC-07 entries **may be hidden** in default view — extended view policy **RT-G12** (VIEW-02) |
| **R-H10** | Catalog enrollment (Playbook 02) and RRDY attestation **remain outside** RT-G12 — Surface **does not** evaluate RRDY-* |

### Explicitly **not** provided to RT-G12 (RT-G12 must decide in its own tracks)

| Topic | Owner |
|-------|-------|
| Surface read binding serialization / form factor (DF-07) | RT-G12 standard / physical specification |
| SOC-* read composition rules per question | RT-G12 physical specification |
| How eight questions aggregate from POC-03…07 + MOC-* | RT-G12 physical specification |
| Whether portfolio select UI is markdown index, CLI, or static HTML | RT-G12 (TX-07: not dashboard product) |
| SOC-10 portfolio select assist implementation | RT-G12 — optional; consumes ROC-01 → ROC-05 → MOC-01 |
| Integrity warning display when MOC-07/POC-03 diverge | RT-G12 physical specification |
| SRDY-07 recency binding from POC-06/07 (OQ-PD05) | RT-G12 + RT-G04 coordination |
| Derived orientation cache refresh policy (ROC-X1) | RT-G05 + RS-03 — bounded; authoritative sync **forbidden** |

### Dependency edge (implementation sequence)

```text
  RT-G04 Physical Artifact Specification
       │ hosts POC-02 registry facet locus at portfolio scope
       ▼
  RT-G10 Physical Artifact Specification
       │ MOC-01…M-H10 per enrolled project
       ▼
  RT-G05 Physical Artifact Specification (this)
       │ populates ROC-* ; R-H01…R-H10
       ▼
  RT-G12 Surface Physical Artifact Specification
       │ optional ROC-01 select → MOC-01 + POC-03…07 read via SOC-*
```

**Principle HAND-R-SPEC-01:** RT-G12 **must not** require registry facet redesign — DF-07, SRDY-*, OQ-PD05 resolve **within** RT-G12 bounds using R-H01…R-H10, not by expanding registry scope.

**Principle HAND-R-SPEC-02:** RT-G12 **must not** implement portfolio-scale Surface session — one Playbook 03 session = **one** Factory Project after select (G05-REL-03).

**Principle HAND-R-SPEC-03:** RT-G12 **must not** treat ROC-06 distinction summaries as substitutes for SOC-02…SOC-08 per-project read composition — portfolio select **only** narrows project choice.

---

## Explicit Non-Claims

This document and the RT-G05 physical registry artifact model it defines:

- **are not** physical artefact creation, folder creation, file creation, or disk writes;
- **are not** serialization format specification (JSON/YAML/markdown/SQLite/other);
- **are not** naming conventions, folder trees, field lists, schemas, or database structures;
- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **storage product**, **database**, **ORM**, or **multi-tenant** persistence service;
- **are not** **application**, **standalone service**, **SaaS**, or **HomeGateway** integration;
- **are not** **automation layer**, **agent orchestration**, **queue**, or **validator engine**;
- **are not** **operator UI**, **dashboard**, **portfolio analytics platform**, or **CLI** (RT-G12);
- **are not** **Manifest physical specification** (RT-G10) or **Surface read specification** (RT-G12);
- **are not** **Persistence Substrate specification** (RT-G04) — only **consumption** of POC-02 registry facet carrier and G05-01…G05-07;
- **do not** modify Registry Charter, RT-G05 Implementation Standard, RT-G04/RT-G10 Physical Artifact Specifications, Engine Stages 1–6, or Playbooks 01–05;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound registry catalog;
- **do not** claim registry catalog records **exist on disk** today — **SAFE UNKNOWN** until separately created;
- **do not** claim Physical Artifact Specification **automatically** authorizes physical creation — **separate operator authorization** required.

Human-operated catalog enrollment path remains the v1 model per Operational Model OA-ACT-04 and Playbook 02.

Registry remains **Portfolio Discoverability Layer** — **not** Manifest, Tracker, CRM, Analytics System, Workflow Engine, Project Manager, Dashboard, or Runtime Object.

### Resolved in upstream standards (inherited, not reopened)

| ID | Resolution |
|----|------------|
| **OQ-R01** | TOP-01…TOP-04 — central ROC-01 aggregate with per-entry pointers |
| **OQ-R02** | ROC-02 composition of ROC-03…ROC-11 — object classes as card template |
| **OQ-RE05** | BIND-01…BIND-04 — enrolled precedes bind; same session permitted; discovery forbidden |
| **OQ-R03** | VIEW-01…VIEW-02 — default discoverable; extended view RT-G12 |
| **OQ-R08** | OS-03, OS-04 — authoritative auto-sync **forbidden**; derived cache optional non-authoritative |

### Deferred (not blockers for this specification)

| ID | Disposition |
|----|-------------|
| **OQ-R04** | Duplicate detection across logical identities — operational + future tooling |
| **OQ-R05** | PHASE_SLICE — one catalog entry per shell vs per slice — Engine v2 or case policy |
| **OQ-R06** | ROC-11 external workspace pointer — optional; operational per case (DF-08) |
| **OQ-R07** | RT-G06 queue relationship to catalog entry — queue charter |
| **OQ-R09** | MIG / incoming request correlation — RT-G08 integration charter |
| **Serialization format** | Future specification track — **not** this deliverable |
| **Internal layout** | Portfolio-scope registry facet structure — operator/tooling convention |

---

## Open Questions (deferred — not blockers for this specification)

| ID | Question | Disposition |
|----|----------|-------------|
| **DF-08** | Pilot workspace pointer policy — ROC-11 vs POC-09/MOC-12 only | Per-case operational |
| **DF-10** | Git versioning policy for SoT records | Operator workshop |
| **OQ-R04** | Automated duplicate identity detection | Post-MVP tooling |
| **OQ-R05** | Multi-slice catalog entry policy | Engine v2 or case policy |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G05 Physical Artifact Specification v1** as **RT-G05 specification-complete** — third Physical Artifact Specification in authorized sequence.
2. **Authorize next track:** **RT-G12 Physical Artifact Specification** — SOC-* content reality and read binding within substrate and R-H01…R-H10 assumptions.
3. **Preserve sequencing:** RT-G12 physical artifact specification completes **before** physical MVP artefact creation unless separately authorized.
4. **Do not create yet:** catalog samples, folder trees, schemas, registry-as-manifest merges, registry-as-tracking-index prototypes under `workspaces/website-factory-operations/`.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — RT-G04 specification records authorized zone |
| Whether any ROC-* catalog binding records **exist** in-repo | **UNKNOWN** — specification authorizes; creation not part of deliverable |
| Calendar for RT-G12 Physical Artifact Specification | **not scheduled** |
| Triumph / pilot workspaces in ROC-11 vs external-only | **UNKNOWN** — DF-08 per case |
| Serialization format choice timing | **deferred** — explicit non-scope of this specification |

---

*RT-G05 Physical Artifact Specification v1 — third Website Factory Physical Artifact Specification. Canonical location: `workspaces/website-factory-reference-v1/RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G05 Physical Artifact Specification v1

**Stage:** Physical Artifact Specification Era — RT-G05 Physical Artifact Specification (third Physical Artifact Specification)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md` (created)  
**Summary:** Третья Physical Artifact Specification Website Factory: полная физическая модель Registry catalog binding — одиннадцать authoritative ROC classes (ROC-01…ROC-11) плюс ROC-X1/ROC-O1, authority model (authoritative/referenced/optional/prohibited) с precedence AUTH-R01…R08, relationship model (REL-R01…REL-R19) к RT-G04/Manifest/Tracking/Playbooks, physical obligations для valid Registry-bound portfolio view (C4/S3), physical guarantees R-G12-01…R-G12-10 к RT-G12 без serialization, integrity model INT-R01…R11, boundary protection (Portfolio Discoverability Layer ≠ Manifest/Tracker/CRM/Analytics/Dashboard/Runtime), readiness model (RRDY-* → physical classes, BIND-*), RT-G12 handoff assumptions R-H01…R-H10 — без создания артефактов, folders, serialization format и layout.  
**Git:** no commit, no push (per task).
