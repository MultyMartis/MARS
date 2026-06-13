# REPORT — RT-G10 Physical Artifact Specification v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical Artifact Specification Era — **RT-G10 physical artifact specification only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE**; Physical MVP Artifact Definition **COMPLETE**; RT-G04 Physical Artifact Specification **COMPLETE**  
**Тип:** physical artifact specification only — **без** artifact creation, folder creation, file creation, serialization format, naming conventions, schemas, layout design, runtime, automation, workflow engine  
**Upstream:** [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md), [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md)  
**Also reviewed:** [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md), [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md), [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md), Operational Playbooks 01–05  
**Связь:** [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md), [RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md](RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md)

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |

---

## Purpose

### Зачем существует RT-G10 Physical Artifact Specification

**RT-G10 Physical Artifact Specification v1** переводит принятые implementation и review артефакты в **полную нормативную модель физической реальности** Manifest binding — определяя **какие физические Manifest artifacts существуют**, **что авторитетно**, **как классы связаны** с RT-G04 substrate, Registry и Tracking, **какие обязательства и гарантии** Manifest несёт для downstream standards — **без** создания артефактов на диске и **без** выбора serialization format.

| Upstream отвечает | Эта specification отвечает |
|-------------------|---------------------------|
| Manifest Charter — **doctrinal role** entry anchor | **Физическая модель** Manifest binding как normative artifact reality |
| RT-G10 Implementation Standard — **MOC classes** и implementation obligations | **Завершённая specification** artifact class model, authority, relationships, guarantees |
| RT-G04 Physical Artifact Specification — **POC-02 manifest facet carrier** | **MOC-* content reality** within that carrier — без substrate redesign |
| Physical MVP Definition Review — **Wave 1 MOC inventory** | **RT-G10 scope only** — MOC-01…MOC-12, MOC-X1, MOC-O1 и их физические обязательства |
| RT-G05/RT-G12 standards — consumption of manifest provisions | **Handoff assumptions** manifest → Registry/Surface **без** serialization design |

### Нормативная формулировка physical artifact responsibility

**RT-G10 Physical Manifest Artifacts (MVP specification)** — **авторизованные structured filesystem records** классов MOC-01…MOC-12 (и опциональных MOC-X1, MOC-O1), **материализованные внутри** POC-02 manifest facet per-project record home на RT-G04 substrate, которые operator **читает и вручную создаёт/обновляет** после Playbook 01 manifest-enrolled и operator manifest bind act — **без** shipped runtime, **без** automated bind on discovery и **без** определения формата сериализации.

### Specification purpose statement

Physical artifact specification **материализует** единую физическую модель Manifest binding, на которой:

1. **MOC-01** определяет canonical per-project entry anchor — MVP hinge (S2, C3, MRDY-06).
2. **MOC-02…MOC-12** определяют authoritative minimum understanding categories и reference topology.
3. **MOC-10** связывает physical bind с prior Playbook 01 doctrinal enrollment act.
4. **Authority, reference, optional, and prohibited** components формализованы с явным precedence.
5. **Physical obligations и guarantees** определяют минимум для valid Manifest-bound Factory Project и downstream handoff к RT-G05 и RT-G12.

Specification **не создаёт** physical artifacts — она **определяет физическую реальность Manifest**, которую authorized creation track должен реализовать.

---

## Foundation Dependencies

Specification **наследует** upstream артефакты **без их переопределения**.

### Tier 0 — Implementation standard, substrate specification, and reviews

| Document | Specification использует |
|----------|-------------------------|
| [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md) | MOC-01…MOC-12 taxonomy; MOWN-*; MRDY-IMPL-*; INT-M01…M10; COL-*, TZ-*; M-H01…M-H10 |
| [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md) | LOC-ZONE, LOC-HOME; POC-01, POC-02 manifest facet; POC-09; G10-01…G10-10; REL-03, REL-05 |
| [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md) | Wave 1 MOC disposition; mandatory/optional/forbidden; Phase B creation sequence |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Categories 1–8, MRDY-*, MA-*, MT-*, MAP-*, ST-* — **sole doctrine source** |

### Tier 1 — Operational doctrine and playbooks

| Document | Specification использует |
|----------|-------------------------|
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — manifest-enrolled precedes physical bind; MRDY attestation |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — manifest anchor precondition; RD-02, RET-03 |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — E4 manifest entry anchor reachable; read-only session |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — separate write plane; DA-01; no manifest facet mutation as side effect |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — manifest enrollment never revoked; MOC-* persists |
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; operator path Registry→Manifest→Tracking→Surface |

### Tier 2 — Downstream standards (consumers of manifest physical reality)

| Standard | Constraint on RT-G10 specification |
|----------|--------------------------------------|
| RT-G05 Registry Implementation Standard | ROC-05 → MOC-01 pointer; consumes M-H01…M-H10 |
| RT-G12 Surface Read Binding Standard | SOC-01 starts from MOC-01; reads MOC-02…08, MOC-12 |

**Authority precedence:** Foundation Freeze + Engine → Manifest Charter (doctrine) → RT-G04 Physical Artifact Specification → RT-G10 Implementation Standard → **эта specification** → physical creation (separate authorization) → RT-G05/RT-G12 physical specification tracks (separate deliverables).

**Scope boundary (SPEC-SCOPE-02):** Эта specification covers **RT-G10 MOC classes only** — content within POC-02 manifest facet. POC substrate classes, ROC catalog classes, SOC read composition belong to **separate standard-specific tracks** — RT-G04, RT-G05, RT-G12 respectively.

---

## Manifest Artifact Class Model

Normative **classes** — не file names, не schemas, не folder trees, не serialization labels.

### Authoritative manifest classes (MOC-01…MOC-12)

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **MOC-01** | **Entry anchor** | Canonical per-project «start here» locus — materialization of MRDY-06 | Operator discovers Manifest binding **without** workspace archaeology; one anchor per Factory Project identity | **Must persist** on bind |
| **MOC-02** | **Identity** | Stable logical Factory Project identity reference (Category 1) | Binds physical manifest to Engine identity shell; **distinct** from registry entry ID (ES-03) | **Must persist** |
| **MOC-03** | **Scope** | Charter & scope tier categories (Category 2) | Intent, exclusions, operator assignment as **categories** — minimal intake valid | **Must persist** |
| **MOC-04** | **Endpoint** | Declared lifecycle endpoint category (Category 3) | Full chain default or partial with acknowledged boundary | **Must persist** |
| **MOC-05** | **Applicability** | Scope applicability doctrine (Category 4) | Full vs partial applicability **explicit** — aligns with scope mask category | **Must persist** |
| **MOC-06** | **Classification anchors** | Lifecycle-dependent binding refs (Category 5) | `site_type_code`, blueprint, generation slice refs when applicable — **not** artefact bodies | **Conditional mandatory** — may defer at bind; **must persist** when charter mandates |
| **MOC-07** | **Position summary** | Non-authoritative «where now» orientation pointer (Category 6) | **Pointer or absent** — reconcilable with POC-03; **must not** duplicate live state ledger | **Optional** — pointer-only when present |
| **MOC-08** | **Topology** | Authoritative reference topology — map of maps (Category 7) | Declares **where** state, gate, handoff, artefact truths live — **never** embeds bodies | **Must persist** |
| **MOC-09** | **Foundation pins** | Logical dependency pins when explicitly declared (Category 8) | Foundation version pins as categories — **not** layer bodies | **Optional** |
| **MOC-10** | **Enrollment** | Physical bind metadata linking to Playbook 01 manifest-enrolled act | Enrollment-before-bind honesty; bind **follows** doctrinal enrolled | **Must persist** on bind |
| **MOC-11** | **Amendment** | Stable-category amendment narrative (ST-01) | Append-oriented corrections to MOC-02…MOC-05, MOC-09 — silent overwrite **forbidden** | **Must persist** when amendments occur |
| **MOC-12** | **External refs** | Topology target locators and optional workspace pointers | Category 7 target locators; ATLAS `atlas_*_ref` convention when binding; POC-09 discipline; closure ref **optional** | **Must persist** for Category 7 targets |

### Optional / subordinate manifest classes

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **MOC-X1** | **Tracking zone snapshot** | Selected non-authoritative snapshot of tracking zones | OQ-M01 — **default absent**; **never** live gate/handoff index | **Forbidden default** — only if explicitly authorized later |
| **MOC-O1** | **Pre-bind enrollment draft** | Pre-bind enrollment decision notes before physical bind | Supports OQ-ME05; **not authoritative** until bind act | **Optional** — non-authoritative |

### Class composition model (conceptual — not layout)

```text
  per-project record home (RT-G04 LOC-HOME)
  │
  ├── POC-01 identity shell ──────────────────── MOC-02 binding context
  │
  └── POC-02 manifest facet (binding carrier)
        ├── MOC-01 Entry anchor ◀── MVP hinge (MRDY-06, S2, C3)
        ├── MOC-02 Identity
        ├── MOC-03 Scope
        ├── MOC-04 Endpoint
        ├── MOC-05 Applicability
        ├── MOC-06 Classification anchors (when applicable)
        ├── MOC-07 Position summary (pointer only — optional)
        ├── MOC-08 Topology ──▶ MOC-12 external refs
        ├── MOC-09 Foundation pins (optional)
        ├── MOC-10 Enrollment bind metadata
        ├── MOC-11 Amendment narrative (when needed)
        ├── MOC-X1 optional zone snapshot (default: absent)
        └── MOC-O1 pre-bind draft (optional — outside authoritative facet until bind)
```

### Class principles

| ID | Principle |
|----|-----------|
| **MOC-RULE-01** | Exactly **one** canonical MOC-01 entry anchor per Factory Project identity — no competing manifest binding carriers |
| **MOC-RULE-02** | POC-02 manifest facet **must remain** a **distinct record class** from POC-03…POC-07 tracking indexes — co-location within same LOC-HOME **permitted**; collapse into undifferentiated mega-record **forbidden** |
| **MOC-RULE-03** | MOC-08 topology **must** point to authoritative loci — typically POC-03, POC-04, POC-05, POC-09 on same substrate, plus external layer/Runtime refs — **never** embed bodies |
| **MOC-RULE-04** | MOC-07 **must not** become parallel active state ledger — **pointer, omitted, or marked invalid** only |
| **RTG10-CLASS-01** | RT-G10 specification covers **MOC-* classes only** — POC carrier existence is RT-G04; ROC/SOC physical shape deferred to downstream tracks |

### Charter category → physical class mapping

| Manifest Charter category | Physical classes |
|---------------------------|------------------|
| Category 1 — Stable project identity | MOC-02 (+ POC-01 shell) |
| Category 2 — Charter & production intent | MOC-03 |
| Category 3 — Declared lifecycle endpoint | MOC-04 |
| Category 4 — Scope applicability doctrine | MOC-05 |
| Category 5 — Classification & binding anchors | MOC-06 |
| Category 6 — Current position summary | MOC-07 (pointer only) |
| Category 7 — Authoritative reference topology | MOC-08, MOC-12 |
| Category 8 — Foundation version pins | MOC-09 |
| MRDY-06 entry anchor | MOC-01 |
| Playbook 01 enrollment act | MOC-10 |
| ST-01 stable amendments | MOC-11 |

---

## Authority Model

### Four manifest content categories

| Category | MOC classes | Authority rule |
|----------|-------------|----------------|
| **Authoritative manifest content** | MOC-01…MOC-06, MOC-08, MOC-10, MOC-11, MOC-12 | Must survive between sessions; loss breaks orientability (MRDY-*) and operator entry path without workspace archaeology |
| **Optional authoritative slice** | MOC-07, MOC-09 | May be absent; when present MOC-07 is **pointer-only**; MOC-09 only when pins declared |
| **Subordinate / forbidden default** | MOC-X1 | Default absent; if present **must be labeled** derived/subordinate — never co-authoritative with POC-04/05 |
| **Operational / pre-bind** | MOC-O1 | Pre-bind notes; **must not** substitute MOC-10 enrollment metadata or MOC-01…05 authoritative content |

### Authority matrix by class

| Class | Authoritative for | Not authoritative for | Write authority |
|-------|-------------------|----------------------|-----------------|
| **MOC-01** | Entry anchor locus identity; «start here» discoverability | Tracking depth; registry catalog; Surface answers | Operator manifest bind/amend act (post Playbook 01) |
| **MOC-02** | Logical Factory Project identity reference binding | Registry entry ID; live state | Operator bind + MOC-11 amendment |
| **MOC-03** | Charter & scope **tier categories** | Full charter bodies in external workspaces | Operator bind + explicit amendment |
| **MOC-04** | Declared endpoint **category** | Lifecycle progression; Runtime state codes | Operator bind + charter amendment |
| **MOC-05** | Scope applicability **doctrine category** | Effective path jump table | Operator bind + scope amendment |
| **MOC-06** | Classification **binding refs** when present | Layer artefact bodies; Site Type Registry definitions | Operator bind/update when lifecycle demands |
| **MOC-07** | — (orientation pointer only) | Active state truth — POC-03 owns | Operator optional pointer refresh — **not** Playbook 04 side effect |
| **MOC-08** | Topology structure & role labels | Index bodies; gate/handoff criteria | Operator bind; target list grows with refs |
| **MOC-09** | Foundation pin **categories** when declared | Foundation layer bodies | Operator bind/amendment |
| **MOC-10** | Enrollment-to-bind linkage | Doctrinal enrollment itself (Playbook 01 outcome) | Operator bind act |
| **MOC-11** | Stable category amendment narrative | Live tracking indexes | Operator explicit amendment — append-oriented |
| **MOC-12** | Topology pointer locators | External bodies; closure primary persistence | Operator maintains refs |
| **MOC-X1** | — (derived snapshot only) | Live gate/handoff index | Only if explicitly authorized — operator-labeled derived |
| **MOC-O1** | — | Any bind authority | Operator notes only |

### Authoritative vs referenced vs optional vs prohibited — summary

| Disposition | Components | Precedence when conflict |
|-------------|------------|-------------------------|
| **Authoritative (manifest-owned)** | MOC-01…MOC-06, MOC-08, MOC-10, MOC-11, MOC-12 | Manifest facet **wins** for stable categories over registry card summaries (M-H10); MOC-11 amendment trail **wins** over stale ROC-06 echo |
| **Referenced (manifest-indexed, not owned)** | POC-03…POC-05 live indexes; POC-08 closure; external layer bodies; Runtime docs | POC-03 tail **wins** over MOC-07 pointer; POC-04/05 **win** over any MOC-X1 snapshot |
| **Optional** | MOC-07, MOC-09, MOC-O1 | Absence **valid**; SOC-03 reads POC-03 directly when MOC-07 absent |
| **Prohibited inside manifest facet** | Live gate/handoff rows; declaration bodies; registry catalog entries; layer bodies; gate criteria; eight Surface answers | Actual owners per Boundary Protection section |

### Authority precedence rules

| Rule ID | Precedence |
|---------|------------|
| **AUTH-M01** | MOC-02…MOC-05 stable categories **win over** registry distinction summaries (ROC-06) on conflict — M-H10 |
| **AUTH-M02** | MOC-11 amendment narrative **append-only** — corrections = new amendment events, not silent overwrite (ST-01, INT-M03) |
| **AUTH-M03** | POC-03 active state **wins over** MOC-07 position summary when both present — MS-02 reconciliation surfaces mismatch |
| **AUTH-M04** | POC-04/POC-05 live indexes **win over** any MOC-X1 or frozen MOC-07 copy labeled «stable» (MT-01, MAP-05) |
| **AUTH-M05** | Playbook 04 **must not** silently mutate MOC-* as automatic side effect — manifest amend **separate operator act** (INT-M06) |
| **AUTH-M06** | Only Factory operator **authoritatively creates/updates** MOC-* — enrollment attestation (Playbook 01) **precedes** bind (INT-M09) |
| **AUTH-M07** | RT-G12 Surface **reads** MOC-* — **never writes** authoritative manifest content (MOWN-04) |
| **AUTH-M08** | RT-G05 Registry **references** MOC-01/MOC-02 — **never authors** manifest minimum understanding depth (REG-IMPL-01) |

### Ownership summary

| Layer | Owns manifest physical artifact reality | Does not own |
|-------|----------------------------------------|--------------|
| **RT-G04 substrate** | LOC-HOME; POC-02 manifest facet **carrier**; POC-09 ref index hosting | MOC-* content; MRDY field binding |
| **RT-G10 (this specification)** | MOC-* content within POC-02 manifest facet; entry anchor; topology pointers; enrollment bind metadata | Tracking indexes; registry catalog; Surface display; substrate zone topology |
| **RT-G05 registry** | ROC-* within POC-02 registry facet | Per-project manifest depth; MOC-* authoritative content |
| **Playbook 04 / Tracking** | POC-03…POC-07 authoritative indexes | Manifest minimum understanding categories |
| **RT-G12 Surface** | SOC-* read composition | Any authoritative MOC-* write |

---

## Relationship Model

### Manifest within substrate (RT-G04)

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-M01** | MOC-* **reside within** POC-02 manifest facet at project LOC-HOME | REL-03; H-03 — substrate hosts carrier; RT-G10 defines content |
| **REL-M02** | MOC-02 **binds to** POC-01 identity shell in same LOC-HOME | One identity binding per Factory Project |
| **REL-M03** | MOC-12 **may reference** POC-09 external ref index entries | Shared ref discipline — locators, not bodies |
| **REL-M04** | MOC-08 topology **points to** POC-03, POC-04, POC-05, POC-09 loci on same substrate | H-06, MAP-05 pointer pattern — even when indexes empty |
| **REL-M05** | MOC-08 **may reference** POC-08 closure metadata — **must not** own closure plane | H-09; Playbook 05 primary write |
| **REL-M06** | POC-02 manifest facet and POC-03…POC-07 **must remain separate record classes** | COL-01…COL-04; MOC-RULE-02 — co-location permitted; class separation mandatory |
| **REL-M07** | MOC-10 **must reference** prior Playbook 01 doctrinal enrollment — bind **follows** enrolled | H-05; INT-M01; discovery bind **forbidden** |

### Manifest ↔ Registry

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-M08** | MOC-01 **precedes** ROC-05 catalog pointer per enrolled project | MR-01, REG-REL-01; registry bind **must not** precede stable MOC-01 |
| **REL-M09** | MOC-02 logical identity **precedes** ROC-03 registry entry ID | ES-03, RA-03 — distinct identifiers |
| **REL-M10** | MOC-03…MOC-05 **supply source categories** for ROC-06 distinction summaries — registry **derives**, manifest **does not require** catalog slot | M-H05; MR-01 |
| **REL-M11** | Manifest facet **persists** when catalog withdrawn — registry status **orthogonal** | Playbook 05 CL-03 analog; M-H06 |
| **REL-M12** | Manifest facet **must not embed** registry catalog content | MAP-07, MR-02; REG-IMPL-01 |

### Manifest ↔ Tracking

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-M13** | MOC-01 **precedes** deep Tracking read — entry before composition | Playbook 03 E4; TS-02 |
| **REL-M14** | MOC-08 topology **orients** to POC-03…POC-07 — Tracking **owns** index bodies | MT-01; TRK-IMPL-01 |
| **REL-M15** | Playbook 04 **mutates** POC-03…POC-07 only — **may** require MOC-07 pointer refresh via **separate** operator manifest amend | INT-M06 |
| **REL-M16** | Playbook 05 **does not revoke** manifest enrollment — MOC-* **persist**; MOC-12 **may add** closure ref | Playbook 05 scope |
| **REL-M17** | Surface-ready ⊇ manifest-ready ⊄ manifest bind complete — SRDY-* remains substrate P4 + RT-G12 | TRK-IMPL-01 |

### Manifest ↔ Playbooks

| Playbook | Manifest facet interaction | Physical record classes |
|----------|---------------------------|-------------------------|
| **01** Manifest enrollment | Doctrinal enrolled → **triggers** bind obligation; **does not** write authoritative MOC-* without bind act | Doctrinal outcome only; MOC-10 links on bind |
| **02** Registry enrollment | **Requires** stable MOC-01; **does not** write manifest facet | Read MOC-01 for ROC-05 pointer |
| **03** Surface session | **Read** MOC-01…MOC-08; depth in POC-03…POC-07 | Read MOC-*; optional MOC-O1 notes only |
| **04** Project declaration | **Mutates** POC-03…POC-07 only — manifest amend **separate** if MOC-07 refresh needed | No automatic MOC-* mutation |
| **05** Project closure | Manifest enrollment **never revoked**; MOC-12 **may reference** POC-08 | MOC-* persist |

### Lifecycle dependency graph

```text
  PRE-FACTORY (no manifest records)
       │
       ▼
  Playbook 01 ──▶ manifest-enrolled (doctrinal)
       │
       ▼
  Operator manifest bind act ──▶ POC-02(m) populated:
       │                         MOC-01…MOC-12 per rules + POC-09 refs
       ▼
  Playbook 02 / RT-G05 (optional) ──▶ ROC-05 points TO MOC-01
       │
       ▼
  Playbook 03 ──read──▶ MOC-01 entry + POC-03…07 indexes
       │
       ▼
  Playbook 04 ──write──▶ POC-03…07 (separate plane)
       │
       ▼
  Playbook 05 ──write──▶ POC-08; MOC-* persist; MOC-12 optional closure ref
```

### Co-location policy (resolved — inherited from implementation standard)

| Rule ID | Implementation rule |
|---------|---------------------|
| **COL-01** | Manifest facet (POC-02 manifest) and tracking indexes (POC-03…POC-07) **may share** same LOC-HOME container |
| **COL-02** | **Must remain** separate **record classes** — MOC-RULE-02, POC-RULE-02 |
| **COL-03** | **Forbidden:** single undifferentiated record merging MOC-08 topology with live POC-04 gate tail as co-authoritative |
| **COL-04** | Serialization format choice **does not** determine co-location — class separation **is normative** |

### Tracking zone serialization (resolved — inherited)

| Rule ID | Rule |
|---------|------|
| **TZ-01** | **Default MVP:** MOC-X1 **absent** — all live indexes remain POC-03…POC-07 only |
| **TZ-02** | **If authorized later:** MOC-X1 **may** hold **non-authoritative** snapshot of **selected** zones — **never** gate/handoff live index |
| **TZ-03** | Any MOC-X1 **must be labeled** derived/subordinate |

---

## Physical Obligations

### What must physically exist for a valid Manifest-bound Factory Project

A **valid Factory Project with physical Manifest binding** requires satisfaction of obligations below. Obligations are **class-level** — not file counts or serialization shapes.

**Doctrinal precondition (not a disk artifact):** Playbook 01 manifest-enrolled outcome **must precede** physical bind (INT-M01, LC-01).

### Tier 0 — Substrate prerequisite (RT-G04)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-M-SUB-01** | **LOC-ZONE** at authorized path | Before any MOC materialization |
| **OBL-M-SUB-02** | **LOC-HOME** — exactly one per Factory Project identity | Before manifest bind |
| **OBL-M-SUB-03** | **POC-01** identity shell + **POC-02 manifest facet** as binding carrier | Manifest bind act |
| **OBL-M-SUB-04** | **POC-09** topology refs pointing to index loci (even if empty) | Manifest bind act |

### Tier 1 — Core manifest binding (C3, S2)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-M-01** | **MOC-01** entry anchor | Manifest bind — **core MVP obligation** |
| **OBL-M-02** | **MOC-02** identity reference | Manifest bind |
| **OBL-M-03** | **MOC-03** scope categories | Manifest bind — minimal intake valid |
| **OBL-M-04** | **MOC-04** endpoint category | Manifest bind |
| **OBL-M-05** | **MOC-05** applicability doctrine | Manifest bind |
| **OBL-M-08** | **MOC-08** topology structure | Manifest bind |
| **OBL-M-10** | **MOC-10** enrollment bind metadata | Manifest bind |
| **OBL-M-12** | **MOC-12** topology target locators; ATLAS refs per adoption statement when known | Manifest bind |

**ATLAS reference fields (MOC-12 — convention only, no serialization):** When active attested ATLAS canonical exists, operator **SHOULD** populate normative ref fields per [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md): `atlas_client_org_ref`, `atlas_person_ref`, `atlas_website_ref`, `atlas_project_ref`, `atlas_relationship_ref`, `atlas_domain_ref`. When unknown → **SAFE UNKNOWN**; **MUST NOT** invent canonical ids. Factory Project identity (MOC-02) **MUST remain distinct** from `atlas_project_ref`.

### Tier 2 — Conditional / lifecycle-triggered

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-M-06** | **MOC-06** classification anchors | When charter/lifecycle mandates classification binding — Core 5 pilot typically requires |
| **OBL-M-11** | **MOC-11** amendment narrative | When stable categories amended (ST-01) |
| **OBL-M-07** | **MOC-07** position summary | **Optional** — if present, pointer-only |
| **OBL-M-09** | **MOC-09** foundation pins | **Optional** — when pins explicitly declared |

### Persistent manifest inventory by milestone

| Must exist after | Manifest physical classes |
|------------------|--------------------------|
| Playbook 01 (doctrinal only) | **None** — doctrinal enrolled, not disk obligation |
| Operator manifest bind | MOC-01, MOC-02…05, MOC-08, MOC-10, MOC-12; MOC-06 per lifecycle; POC-09 refs |
| First stable category amendment | MOC-11 append entry |
| Playbook 05 closure | MOC-* **persist**; MOC-12 **may add** POC-08 ref — enrollment **not** revoked |

### Minimum bootstrap before Registry bind or credible Playbook 03

| # | Physical manifest element | Phase reference |
|---|---------------------------|-----------------|
| 1 | Playbook 01 manifest-enrolled recorded (doctrinal) | Pre-bind |
| 2 | MOC-01 discoverable within authorized zone | Manifest bind |
| 3 | MOC-02…MOC-05 consistent with enrollment attestation | Manifest bind |
| 4 | MOC-08 topology points to POC-03…05/POC-09 loci (even if empty) | Manifest bind |
| 5 | MOC-07 absent or pointer-only — no live gate index in manifest facet | Manifest bind |
| 6 | No Passport / registry-card / tracking-index duplication in POC-02 manifest facet | Manifest bind |
| 7 | Operator reaches MOC-01 from Registry pointer or direct knowledge | Post-bind verification |

### What is NOT a physical obligation of RT-G10

| Not required by RT-G10 | Owner |
|------------------------|-------|
| POC-03…POC-07 tracking index content | Playbook 04; RT-G04 |
| ROC-* catalog content | RT-G05 physical specification track |
| SOC-* read composition | RT-G12 physical specification track |
| Serialization format | Deferred — not in this specification |
| Registry catalog entry existence | Optional doctrinally (MR-01); MVP demo track mandates via Playbook 02 |

---

## Physical Guarantees

RT-G10 physical artifact specification **guarantees** the following to downstream standards **without defining serialization**.

### Guarantees to RT-G05 (Registry)

| Guarantee ID | RT-G05 may rely on |
|--------------|-------------------|
| **M-G05-01** | Each manifest-bound Factory Project exposes **one** stable MOC-01 entry anchor discoverable within authorized zone (M-H01) |
| **M-G05-02** | MOC-02 logical identity reference **stable** for catalog slot linkage — distinct from registry entry ID (M-H02) |
| **M-G05-03** | Manifest bind **may exist** before any POC-02 registry facet entry — catalog enrollment **optional** (M-H03) |
| **M-G05-04** | MOC-10 enrollment metadata confirms Playbook 01 preceded bind — registry **must not** treat discovery as enrollment (M-H04) |
| **M-G05-05** | MOC-03 scope tier and MOC-04 endpoint **available** as **source categories** for distinction summaries — RT-G05 **does not** duplicate full charter in catalog (M-H05) |
| **M-G05-06** | MOC-01 locus **stable** across registry withdraw/re-enroll — catalog status **orthogonal** to manifest persistence (M-H06) |
| **M-G05-07** | MOC-08 topology **not required** in registry card — catalog holds **pointer to manifest entry**, not full map-of-maps (M-H07) |
| **M-G05-08** | Manifest facet **does not embed** registry catalog — registry facet at portfolio scope **separate** (M-H08) |
| **M-G05-09** | Operator path Registry→Manifest **works** — MOC-01 reachable from ROC-05 without archaeology (M-H09) |
| **M-G05-10** | Append-only amendment honesty (MOC-11) applies — registry card **may show stale summary** until operator refresh; **manifest facet wins** on conflict (M-H10) |

### Guarantees to RT-G12 (Tracking Surface)

| Guarantee ID | RT-G12 may rely on |
|--------------|-------------------|
| **M-G12-01** | MOC-01 **discoverable** as per-project read entry — Playbook 03 E4; SOC-01 convergence starts here |
| **M-G12-02** | MOC-02…MOC-05 reflect Playbook 01 attestation — SOC-02 **operational slice** available without re-attestation |
| **M-G12-03** | MOC-08 + MOC-12 declare topology targets — SOC-02 **follows refs** to POC-03…09 loci |
| **M-G12-04** | MOC-07 **pointer-only or absent** — reconcilable with POC-03; SOC-09 **may surface** mismatch (MS-02) |
| **M-G12-05** | Manifest facet **does not hold** live gate/handoff index — POC-04/05 sole live index; MOC-X1 default absent |
| **M-G12-06** | MOC-04 endpoint and MOC-05 applicability **available** for SOC-06 remaining view |
| **M-G12-07** | MOC-06 classification refs **available** when lifecycle mandates — SOC-02 orientation depth |
| **M-G12-08** | On stable category conflict, **manifest facet wins** — SOC-02 follows MOC-11 amendment trail |
| **M-G12-09** | Manifest bind **does not imply** SRDY-* completeness — POC-03…07 separate obligation |
| **M-G12-10** | Playbook 04 **does not** silently corrupt manifest facet — read composition integrity preserved |

### Cross-standard guarantee principles

| Principle | Meaning |
|-----------|---------|
| **GUAR-M01** | RT-G10 **populates** POC-02 manifest facet; RT-G04 **hosts** carrier — **must not** create parallel manifest SoT outside authorized zone |
| **GUAR-M02** | Physical guarantees are **class-level and locus-level** — not format-specific |
| **GUAR-M03** | Downstream standards **must not** require manifest facet redesign — open questions resolve within RT-G05/RT-G12 bounds |

---

## Integrity Model

Minimum manifest binding integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Physical artifact expectation |
|----|----------|------------------------------|
| **INT-M01** | **Enrollment-before-bind honesty** | MOC-10 **must** reference Playbook 01 enrollment act — bind **without** prior enrolled **forbidden** |
| **INT-M02** | **Single entry anchor** | Exactly **one** MOC-01 per Factory Project identity — no competing anchors |
| **INT-M03** | **Stable category amendment narrative** | MOC-11 append-oriented — corrections to MOC-02…MOC-05 **via** amendment, not silent overwrite (ST-01) |
| **INT-M04** | **Topology pointer validity (minimal)** | MOC-12 locators **identify** target loci — broken refs **visible** to operator; no silent copy of external bodies |
| **INT-M05** | **Plane separation** | POC-02 manifest facet **must not** embed POC-04/POC-05 live tails as co-authoritative (MT-01, MAP-05) |
| **INT-M06** | **Declaration plane isolation** | Playbook 04 acts **must not** mutate MOC-* as automatic side effect — manifest amend **separate operator act** |
| **INT-M07** | **Position summary honesty** | MOC-07 **matches** POC-03 active state **or** marked invalid/unset — MS-02 |
| **INT-M08** | **Identity distinctness** | MOC-02 logical identity **≠** registry entry ID when catalog exists — ES-03 |
| **INT-M09** | **Human-only bind path** | Only operator manifest bind/amend acts **authoritatively change** MOC-* — SC-03, OA-ACT-04 |
| **INT-M10** | **Closure persistence non-ownership** | POC-08 **referenced** by MOC-12 **optional** — manifest **does not** replace Playbook 05 primary write |

### What integrity model explicitly excludes

| Excluded | Reason |
|----------|--------|
| Automated schema validation of manifest facet | RT-G11 post-MVP |
| MRDY pass/fail re-evaluation engine | Playbook 01 owns attestation |
| CI/git-hook auto-bind | INT-M09 |
| Cross-record referential integrity engine | Single-operator MVP; operator resolves |
| Automated sync manifest ↔ tracking indexes | INT-M06 |

### Integrity verification (human-operated)

MVP **accepts** operator manual review: Playbook 03 session surfaces MOC-07/POC-03 mismatches via SOC-09; Playbook 01 checklist covers MRDY-07 role distinction. Formal validators **deferred**.

---

## Boundary Protection

RT-G10 physical manifest artifacts **must never become** the following — inherited from Manifest Charter, implementation standard, RT-G04 separation, MVP exclusions.

### Forbidden system roles (no manifest physical artifact class)

| Manifest must not become | Guard |
|--------------------------|-------|
| **Passport** — parallel mega-document SoT | MA-03, MAP-06, BV-15 |
| **Registry / portfolio catalog** | MAP-07, MR-02; RT-G05 owns ROC-* |
| **Tracking composition / live observability index** | MT-01, MAP-05; POC-03…07 |
| **Tracking Surface / operator dashboard** | MAP-09, TS-01; RT-G12 SOC-* |
| **Persistence substrate product** | MAP-01; RT-G04 owns zone |
| **Database / query engine / multi-tenant store** | MAP-02; DF-02 |
| **Workflow engine / state machine executor** | MAP-04, MAP-12; RT-G01 |
| **Factory runtime product** | SC-01; RT-G09 |
| **Gate Results System** | MAP-10; POC-04 |
| **Project management system** | Tasks, sprints beyond charter category |
| **Automation / discovery enrollment** | Playbook 01 forbidden automation; RD-04 |
| **Foundation authority merge** | MAP-08; Legal Pack, Site Type matrices embedded |
| **Handoff package / artefact body store** | MAP-11; RR-02 |
| **Closure registry / terminal workflow engine** | Playbook 05 + POC-08 primary |
| **Validator / gate authority engine** | RT-G11 |
| **Declaration / progression ledger owner** | POC-06/07; Playbook 04 |
| **Runtime object / execution state** | MAP-12; no automated transitions |

### Forbidden content inside manifest facet

| Must never persist as manifest-owned authoritative content | Actual owner |
|-------------------------------------------------------------|--------------|
| Live gate outcome rows | POC-04 |
| Live handoff event sequence | POC-05 |
| Full state history | POC-03 |
| Declaration event bodies | POC-06 |
| Progression ledger | POC-07 |
| Registry catalog entries | POC-02 registry facet; ROC-* |
| Layer artefact bodies | External workspaces |
| Gate/handoff criteria text | Runtime Architecture |
| Site Type Registry definitions | Foundation `registry/` |
| Eight Surface question **answers** | RT-G12 SOC-* read composition |
| Portfolio distinction summaries as sole project truth | ROC-06 echoes MOC-03…05 — not replacement |

### Forbidden physical anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| Single record swallowing manifest + full tracking + surface | MOC-RULE-02; POC-RULE-02 |
| Manifest facet containing seven/eight Surface answers | RA-05; RT-G12 scope |
| Physical bind **before** Playbook 01 enrolled | INT-M01; REL-M07 |
| Registry impl creating manifest content as side effect | REG-IMPL-01; REL-M12 |
| MOC-07 frozen copy of gate index labeled «stable» | ST-02, MAP-05; AUTH-M04 |
| Manifest bind triggering automated POC-03 mutation | INT-M06; H-08 |
| `COMPLETE` / deploy conflated with manifest «completion» | MAP-13, MS-04 |
| MOC-X1 holding live POC-04/05 tail as co-authoritative | TZ-01…03; MT-01 |
| Filesystem/git discovery creating MOC-10 without Playbook 01 | INT-M01; RD-04 |

**Principle BP-M-SPEC-01:** Physical manifest binding **extends operability** of entry anchor doctrine — **does not execute** Factory movement or replace Engine declaration authority.

---

## Readiness Model

### MRDY doctrinal readiness vs physical bind completeness

| Concept | Physical specification rule |
|---------|----------------------------|
| **Manifest-ready** | Playbook 01 MRDY-* attestation — **prerequisite** for physical bind, **not replaced** by bind |
| **Physical bind complete** | MOC-01…MOC-05, MOC-08, MOC-10, MOC-12 **present**; MOC-06/07/09 per lifecycle rules |
| **Manifest-ready ⊄ fully trackable** | Valid bind at `NEW_PROJECT` with **empty** POC-04/POC-05 — MOC-08 still points to index loci |
| **Manifest-ready ⊄ surface-ready** | Physical bind **does not imply** SRDY-* — POC-03…07 separate |
| **Physical bind ⊄ retroactive enrollment** | MOC-10 **must** reference prior Playbook 01 act — same-session bind **permitted**; discovery bind **forbidden** |

### MRDY → physical class mapping at bind

| ID | Doctrinal criterion | Physical class obligation at bind |
|----|---------------------|-----------------------------------|
| **MRDY-01** | Stable project identity explicit | MOC-02 **must** carry stable logical identity reference |
| **MRDY-02** | Charter & scope tier explicit | MOC-03 **must** persist charter/scope **categories** |
| **MRDY-03** | Declared lifecycle endpoint explicit | MOC-04 **must** record endpoint category |
| **MRDY-04** | Scope applicability doctrine explicit | MOC-05 **must** make full vs partial **explicit** |
| **MRDY-05** | Reference topology declared | MOC-08 + MOC-12 **must** declare topology targets |
| **MRDY-06** | Manifest entry anchor identified | MOC-01 **must** materialize discoverable entry anchor |
| **MRDY-07** | Operator understands Manifest ≠ Passport ≠ Registry | **Not serialized** — Playbook 01 attestation; implementation **must not** create substitute artefact |

### Stability expectations at physical layer

| Stability class | Physical classes | Rule |
|-----------------|------------------|------|
| **Expected stable** | MOC-02…MOC-05, MOC-09, MOC-11 | Amendment **via** MOC-11; silent overwrite **forbidden** |
| **Expected evolving** | MOC-06, MOC-07, MOC-12 | **May update**; **must not** freeze live gate index into stable manifest facet |

### When RT-G10 Physical Artifact Specification is **complete**

This deliverable is **specification-complete** when:

| Criterion | Status |
|-----------|--------|
| Manifest artifact classes defined (MOC-01…MOC-12 + MOC-X1, MOC-O1) | **Yes** |
| Class responsibilities formalized | **Yes** |
| Authority model (authoritative / referenced / optional / prohibited) with precedence | **Yes** |
| Relationship model (RT-G04, Registry, Tracking, Playbooks; REL-M*) | **Yes** |
| Physical obligations for valid Manifest-bound Factory Project stated | **Yes** |
| Physical guarantees to RT-G05 and RT-G12 without serialization | **Yes** |
| Minimum integrity expectations stated (no validators) | **Yes** |
| Boundary protection at specification layer | **Yes** |
| RT-G05 handoff assumptions explicit | **Yes** |
| No artifacts, folders, serialization, or layout created | **Yes** |

### What specification-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| Physical MOC-* records **exist** in repo | Specification defines model; creation = separate authorized track |
| Serialization format **chosen** | Explicitly out of scope |
| LOC-HOME internal layout **designed** | Deferred to future track or operator convention |
| MVP **demonstrated** on pilot | Success S1–S9 post-physical bind |
| `workspaces/website-factory-operations/` **exists on disk** | **SAFE UNKNOWN** until operator creates |

### Specification-complete vs physical creation

```text
  RT-G10 Manifest Implementation Standard v1 ── COMPLETE
           │
           ▼
  RT-G04 Physical Artifact Specification v1 ── COMPLETE (substrate + POC carrier)
           │
           ▼
  RT-G10 Physical Artifact Specification v1 ── THIS (specification-complete)
           │
           ├──▶ RT-G05 Physical Artifact Specification (separate track)
           └──▶ RT-G12 Physical Artifact Specification (separate track)
           │
           ▼
  Physical artefact creation (manifest bind on pilot) ── ONLY when separately authorized
```

### MVP manifest bind readiness checklist (operator, post-specification)

Before claiming C3 satisfied on pilot:

| # | Check |
|---|-------|
| R-M1 | Playbook 01 manifest-enrolled outcome recorded (doctrinal) |
| R-M2 | MOC-01 entry anchor discoverable within authorized zone |
| R-M3 | MOC-02…MOC-05 present and consistent with enrollment attestation |
| R-M3a | ATLAS-first enrollment completed per Playbook 01 — refs bound in MOC-12 when active canonical known; SAFE UNKNOWN when not |
| R-M4 | MOC-08 topology points to POC-03…POC-05/POC-09 loci (even if indexes empty) |
| R-M5 | MOC-07 absent or pointer-only — no live gate index in manifest facet |
| R-M6 | No Passport / registry-card / tracking-index duplication in POC-02 manifest facet |
| R-M7 | Operator reaches manifest entry from Registry pointer or direct knowledge without archaeology |

---

## RT-G05 Handoff Assumptions

RT-G05 Registry Physical Artifact Specification (future track) and RT-G05 implementation **may assume** the following from this RT-G10 Physical Artifact Specification — **without** RT-G05 redefining manifest doctrine or substrate.

### Guaranteed manifest provisions (M-H01…M-H10 aligned)

| Assumption ID | RT-G05 may assume |
|---------------|-------------------|
| **M-H01** | Each manifest-bound Factory Project exposes **one** stable MOC-01 entry anchor discoverable within authorized zone |
| **M-H02** | MOC-02 logical identity reference **stable** for catalog slot linkage — distinct from registry entry ID (ROC-03) |
| **M-H03** | Manifest bind **may exist** before any POC-02 registry facet entry — catalog enrollment **optional** |
| **M-H04** | MOC-10 enrollment metadata confirms Playbook 01 preceded bind — registry **must not** treat discovery as enrollment |
| **M-H05** | MOC-03 scope tier and MOC-04 endpoint **available** as **source categories** for ROC-06 distinction summaries |
| **M-H06** | MOC-01 locus **stable** across registry withdraw/re-enroll — ROC-07 status **orthogonal** to manifest persistence |
| **M-H07** | MOC-08 topology **not required** in registry card — ROC-05 holds **pointer to MOC-01**, not full map-of-maps |
| **M-H08** | Manifest facet **does not embed** registry catalog — ROC-01 aggregate at portfolio scope **separate** |
| **M-H09** | Operator path ROC-05 → MOC-01 **works** without workspace archaeology |
| **M-H10** | MOC-11 append-only amendment honesty applies — ROC-06 **may be stale** until operator refresh; **manifest facet wins** on conflict |

### Explicitly **not** provided to RT-G05 (RT-G05 must decide in its own tracks)

| Topic | Owner |
|-------|-------|
| Registry catalog serialization format | RT-G05 physical specification |
| Catalog card field template (OQ-R02) | RT-G05 physical specification |
| Portfolio catalog physical shape (OQ-R01 / DF-05) | RT-G05 physical specification |
| Derived orientation snapshot refresh policy (ROC-08) | RT-G05 + RS-03 |
| Registry enrollment ritual steps | Playbook 02 — unchanged |
| LOC-HOME internal layout | Operator convention — not manifest scope |

### Dependency edge (implementation sequence)

```text
  RT-G04 Physical Artifact Specification
       │ hosts LOC-HOME, POC-02 manifest facet carrier
       ▼
  RT-G10 Physical Artifact Specification (this)
       │ populates MOC-* ; M-H01…M-H10
       ▼
  RT-G05 Registry Physical Artifact Specification
       │ populates ROC-* ; ROC-05 → MOC-01
       ▼
  RT-G12 Surface Physical Artifact Specification
       │ reads MOC-01 + POC-03…07 via SOC-*
```

**Principle HAND-M-SPEC-01:** RT-G05 **must not** require manifest facet redesign — OQ-M05 (card fields from Manifest categories) resolves **within** RT-G05 bounds using M-H05 source categories, not by expanding manifest scope.

**Principle HAND-M-SPEC-02:** RT-G05 catalog bind **must not precede** stable MOC-01 on substrate for each catalog entry (REG-IMPL-02, REL-M08).

---

## Explicit Non-Claims

This document and the RT-G10 physical manifest artifact model it defines:

- **are not** physical artefact creation, folder creation, file creation, or disk writes;
- **are not** serialization format specification (JSON/YAML/markdown/SQLite/other);
- **are not** naming conventions, folder trees, field lists, schemas, or database structures;
- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **storage product**, **database**, **ORM**, or **multi-tenant** persistence service;
- **are not** **application**, **standalone service**, **SaaS**, or **HomeGateway** integration;
- **are not** **automation layer**, **agent orchestration**, **queue**, or **validator engine**;
- **are not** **operator UI**, **dashboard**, or **CLI** (RT-G12);
- **are not** **Registry catalog standard** (RT-G05) or **Surface read standard** (RT-G12);
- **are not** **Persistence Substrate specification** (RT-G04) — only **consumption** of POC-02 manifest facet carrier and G10-01…G10-10;
- **do not** modify Manifest Charter, RT-G10 Implementation Standard, RT-G04 Physical Artifact Specification, Engine Stages 1–6, or Playbooks 01–05;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound manifest facet;
- **do not** claim manifest binding records **exist on disk** today — **SAFE UNKNOWN** until separately created;
- **do not** claim Physical Artifact Specification **automatically** authorizes physical creation — **separate operator authorization** required.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01.

Manifest remains **Entry Anchor** — **not** Passport, Tracker, Registry, Dashboard, Project Manager, or Runtime Object.

---

## Open Questions (deferred — not blockers for this specification)

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-M02** | Partial closure metadata — Manifest category vs Tracking flag only | Playbook 05 + RT-G12; MOC-12 ref **optional** |
| **OQ-M03** | PHASE_SLICE / multi-`generation_id` — one bind per shell vs per slice | Engine v2 or operational case policy |
| **OQ-M06** | External workspace pointer — Manifest MOC-12 vs tracking-only | Operational + RT-G12 |
| **OQ-M07** | `PASS_WITH_WARNINGS` — Manifest orientation category | MOC-07 pointer semantics |
| **OQ-M08** | Chrome blocks without `block_id` — Manifest binding category | MOC-06 when applicable |
| **OQ-ME05** | Physical bind moment vs doctrinal Enrolled timing | Same session permitted; discovery bind forbidden — exact ritual **operator convention** |
| **DF-04** | Co-location layout within per-project home | COL-* resolved — internal layout **operator/tooling** |
| **DF-07…DF-10** | Git policy, pilot pointer policy, read surface form | Cross-charter; not manifest scope |
| **Serialization format** | JSON vs YAML vs markdown vs other | Future specification track — **not** this deliverable |

**Resolved in upstream standards (inherited, not reopened):**

| ID | Resolution |
|----|------------|
| **OQ-M04** | COL-01…COL-04 — separate record classes; co-location within home permitted |
| **OQ-M01** | TZ-01…TZ-03 — default exclude live indexes; MOC-X1 optional bounded extension |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G10 Physical Artifact Specification v1** as **RT-G10 specification-complete** — second Physical Artifact Specification in authorized sequence.
2. **Authorize next track:** **RT-G05 Physical Artifact Specification** — ROC-* content reality within substrate and M-H01…M-H10 assumptions.
3. **Preserve sequencing:** RT-G05 → RT-G12 physical artifact specifications complete **before** physical MVP artefact creation unless separately authorized.
4. **Do not create yet:** manifest samples, folder trees, schemas, passport documents, manifest-as-gate-index prototypes, registry-in-manifest merges under `workspaces/website-factory-operations/`.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — RT-G04 specification records authorized zone |
| Whether any MOC-* binding records **exist** in-repo | **UNKNOWN** — specification authorizes; creation not part of deliverable |
| Calendar for RT-G05 Physical Artifact Specification | **not scheduled** |
| Triumph / client workspaces as MOC-12 targets vs external-only | **UNKNOWN** — DF-08 per case |
| Serialization format choice timing | **deferred** — explicit non-scope of this specification |

---

*RT-G10 Physical Artifact Specification v1 — second Website Factory Physical Artifact Specification. Canonical location: `workspaces/website-factory-reference-v1/RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G10 Physical Artifact Specification v1

**Stage:** Physical Artifact Specification Era — RT-G10 Physical Artifact Specification (second Physical Artifact Specification)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md` (created)  
**Summary:** Вторая Physical Artifact Specification Website Factory: полная физическая модель Manifest binding — двенадцать authoritative MOC classes (MOC-01…MOC-12) плюс MOC-X1/MOC-O1, authority model (authoritative/referenced/optional/prohibited) с precedence, relationship model (REL-M01…REL-M17) к RT-G04/Registry/Tracking/Playbooks, physical obligations для valid Manifest-bound Factory Project, physical guarantees M-G05/M-G12 к RT-G05 и RT-G12 без serialization, integrity model, boundary protection (Entry Anchor ≠ Passport/Tracker/Registry/Dashboard/Runtime), readiness model и RT-G05 handoff assumptions M-H01…M-H10 — без создания артефактов, folders, serialization format и layout.  
**Git:** no commit, no push (per task).
