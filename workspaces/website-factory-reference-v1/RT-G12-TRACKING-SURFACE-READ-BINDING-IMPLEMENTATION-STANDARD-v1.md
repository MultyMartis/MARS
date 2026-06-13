# REPORT — RT-G12 Tracking Surface Read Binding Implementation Standard v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Standards — **RT-G12 implementation standard only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Persistence Substrate Implementation Standard **COMPLETE**; RT-G10 Manifest Implementation Standard **COMPLETE**; RT-G05 Registry Implementation Standard **COMPLETE**; RT-G12 Tracking Surface Implementation Planning Charter **COMPLETE**  
**Тип:** implementation standard only — **без** runtime, database, automation, queue, workflow engine, UI design, screen design, dashboard design, schemas, folder layout, physical artefact creation, code  
**Upstream:** [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), [RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md), [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md), Operational Playbooks 01–05  
**Связь:** [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G12, [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md)

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |
| **TX-07** | No dashboard product / operator SaaS in MVP |

---

## Purpose

### Зачем существует RT-G12 Implementation Standard

**RT-G12 Tracking Surface Read Binding Implementation Standard v1** переводит [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) и [RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md) из **роли read visibility doctrine** (charter + planning) в **конкретную MVP-модель физического существования** per-project Surface read binding — оставаясь **filesystem-backed**, **documentation-first**, **human-operated** и **read-only**, без runtime-концепций.

| Charter / Planning отвечает | Implementation Standard отвечает |
|-----------------------------|------------------------------------|
| Какова **роль** Surface — eight questions, Tier S-A/B/C, SRDY-* | Как Surface read binding **существует физически** в MVP |
| Какие **классы информации** оператор **должен видеть** | Какие **implementation object classes** compose eight-question read path |
| TS-*, VP-*, PO-*, STV-*, GV-*, LV-*, EV-*, OA-* doctrine | Что Surface implementation **must never become** on disk or in tooling |
| IS-* planning obligations | IS-* как **implementation obligations** для read composition |
| C5 capability gap at planning level | C5/S4 **minimum read binding** at implementation class level |

### Нормативная формулировка implementation responsibility

**RT-G12 Tracking Surface Read Binding (MVP implementation)** — **авторизованная per-project physical read composition** Surface doctrine (eight operator questions, Tier S-A/B/C visibility classes, SRDY-* completeness expectations) **поверх** RT-G04 substrate records, **начиная от** RT-G10 manifest entry anchor, с **опциональным** portfolio select через RT-G05 registry catalog — которую operator **читает** для Playbook 03 supervision **без** authoritative index mutation — **без** shipped runtime, **без** automated read-side writes и **без** выбора display product или serialization format в этом standard (implementation classes only).

Surface read binding **материализует operator visibility path (C5, S4)** — **не** dashboard, **не** Tracking composition engine, **не** persistence substrate, **не** Manifest or Registry substitute.

### Implementation purpose statement

Surface read binding implementation **материализует** для **одного** Factory Project:

1. **One discoverable per-project read convergence point** — operator answers eight Surface visibility questions **from one authorized read path** without full-repo search when indexes exist.
2. **Faithful read composition** of Tier S-A + available Tier S-B classes from persisted substrate indexes and manifest pointers — **not** re-definition of visibility doctrine.
3. **Read-only semantics** — Playbook 04 remains sole authoritative write plane for POC-03…POC-07 (TRK-REL-01, OA-ACT-04).
4. **SRDY-* enablement** — physical bind **exposes or explicitly signals** each S-A class and SRDY criterion — **not** automated SRDY pass/fail authority.
5. **Optional portfolio entry assist** — ROC-01 select → MOC-01 → per-project read path — **never** eight questions at portfolio level (RE-01).

Surface read binding **не сериализует** tracking indexes, manifest categories, registry catalog, gate criteria, layer bodies, or declaration authority — it **composes read views** from substrate records RT-G04 hosts and bindings RT-G10/RT-G05 populate.

---

## Foundation Dependencies

Implementation Standard **наследует** Surface Charter, RT-G12 planning charter, RT-G04/RT-G10/RT-G05 standards и operational doctrine **без их переопределения**.

### Tier 0 — Charter, standard, and decision chain

| Document | Standard использует |
|----------|---------------------|
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Eight questions, Tier S-A/B/C, SRDY-*, VP-*, PO-*, STV-*, GV-*, LV-*, EV-*, OA-* — **sole doctrine source** |
| [RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | IS-*, SRB-*, G04-REL-*, M10-REL-*, G05-REL-*, AUTH-*, BP-* |
| [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md) | POC-01…POC-10, POC-D1, DR-*, TRK-REL-01, OWN-03 |
| [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md) | MOC-01…MOC-12, M-H01…M-H10, TRK-IMPL-01 |
| [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md) | ROC-01…ROC-11, R-H01…R-H10, RE-01, VIEW-* |
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C5 Tracking visibility; S4 success; C2→C3→C4→C5 chain |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-01/02/03/06; TX-07 |

### Tier 1 — Tracking and operational doctrine

| Document | Standard использует |
|----------|---------------------|
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking zones, Tier A/B/C, seven questions, TC-* — **composition source** Surface **reads** |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — eight questions session; SE-03 read-only; SRDY assessment ritual |
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-04; operator path Registry→Manifest→Tracking→Surface |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — declarations update indexes Surface **reads** |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Gate visibility boundaries — instance observation only |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | Lifecycle visibility classes — Surface **exposes**, **does not execute** |

### Tier 2 — Engine boundary

| Document | Constraint on implementation |
|----------|------------------------------|
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04; Surface read binding **external** to Engine docs |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | SV-*, SHV-* — Surface **shows**, **does not redefine** |

**Authority precedence:** Foundation Freeze + Engine → Surface Charter (doctrine) → Tracking Model → RT-G04 Standard → RT-G10 Standard → RT-G05 Standard → RT-G12 Planning Charter → **этот standard** → physical artefact creation **не может** нарушить TS-01, VP-01, MAP-05, TRK-REL-01, OA-ACT-04, RE-01, SRDY-09.

---

## Surface Object Model

Implementation standard определяет **одиннадцать implementation object classes** plus optional extensions — нормативные категории read composition for one Factory Project, **не** schema labels, field names, screen regions, or file names.

### Class taxonomy

| Class ID | Class name | Physical meaning | MVP disposition |
|----------|------------|------------------|-----------------|
| **SOC-01** | **Read convergence point** | Per-project canonical locus where eight-question read composition **starts** — materialization of «one authorized read path» (IS-01, C5) | **Must exist** per bound project |
| **SOC-02** | **Orientation view** | Read composition for question #1 — identity, charter summary, scope tier, endpoint, mask, conditional classification (PO-*, Tier S-A/B) | **Must compose** |
| **SOC-03** | **State view** | Read composition for question #2 — active state (one), LC segment, halt/suspension, invalid flag (STV-01, SV-*) | **Must compose** |
| **SOC-04** | **Blocking view** | Read composition for question #3 — open blocker summary, gate/handoff/halt/legal block, eligibility snapshot (GV-*, GV-02) | **Must compose** |
| **SOC-05** | **Completion view** | Read composition for question #4 — completed states/segments, satisfied gates, cleared handoffs, stale markers visible (SHV-*, GV-03/05) | **Must compose** |
| **SOC-06** | **Remaining view** | Read composition for question #5 — remaining segments/gates/artefacts **to declared endpoint** (LPC-03, scope mask) | **Must compose** |
| **SOC-07** | **Recency view** | Read composition for question #6 — progression ledger tail, recent declarations, invalidations, explicit «no declarations yet» (EV-*, SRDY-07) | **Must compose** |
| **SOC-08** | **Forward view** | Read composition for question #7 — next segment eligibility or blocked-with-cause — **derived**, enables declare decision (OA-01) | **Must compose** |
| **SOC-09** | **Integrity warning surface** | Read-visible flags when indexes inconsistent — invalid active, ledger ≠ active, stale blocking, manifest/tracking drift (VP-04, MS-02) | **Must compose when detected** |
| **SOC-10** | **Portfolio select assist** | Optional read path from ROC-01 catalog to MOC-01 per selected project — portfolio **select only** (IS-12, RE-01) | **May exist** at portfolio scope |
| **SOC-11** | **Tier S-B conditional views** | Conditional read slices when substrate supplies data — classification, generation freeze, parallel legal, drill-down gate detail (Surface §Tier S-B) | **May compose** when data present |

### Optional extension classes (bounded — default exclude)

| Class | Content | Notes |
|-------|---------|-------|
| **SOC-D1** | **Derived read cache** | Regeneratable composed views from POC-D1 or local read-side cache — eligibility rollup, SRDY derived views | **Non-authoritative**; DR-01 analog |
| **SOC-O1** | **Session read notes** | Pre-declaration Playbook 03 session notes — POC-O1 analog at read plane | **Not authoritative** for SRDY-* or indexes |

### Class composition model (implementation-level, not display design)

```text
  [optional] portfolio scope
       │
       └── SOC-10 Portfolio select assist ──▶ ROC-01 → ROC-05 → MOC-01
                                                    │
  per-project record home (RT-G04 P1)               │
       │                                            │
       ├── MOC-01 Entry anchor ◀────────────────────┘
       │
       └── SOC-01 Read convergence point ◀── MVP hinge (C5, S4)
             │
             ├── SOC-02 Orientation view      ← MOC-02…06, POC-01, MOC-07 pointer
             ├── SOC-03 State view            ← POC-03, lifecycle bind
             ├── SOC-04 Blocking view         ← POC-03…05, POC-D1 optional
             ├── SOC-05 Completion view      ← POC-03…05 history + stale markers
             ├── SOC-06 Remaining view         ← derived from endpoint + mask + indexes
             ├── SOC-07 Recency view           ← POC-06, POC-07, POC-10
             ├── SOC-08 Forward view           ← derived eligibility
             ├── SOC-09 Integrity warnings     ← cross-index reconciliation
             ├── SOC-11 Tier S-B views        ← when indexes supply conditional classes
             └── SOC-D1 derived cache (optional, subordinate)
```

**Principle SOC-RULE-01:** SOC-01 **must** be **one** canonical read convergence point per Factory Project identity — no competing per-project Surface read SoT.

**Principle SOC-RULE-02:** SOC-02…SOC-08 **must compose from** substrate authoritative records (POC-03…POC-07, POC-10) and manifest pointers (MOC-*) — **must not** duplicate live gate/handoff index as second authoritative store (MAP-05, MT-01).

**Principle SOC-RULE-03:** SOC-10 **must remain** portfolio-scope **select assist only** — eight questions **never** primary at catalog level (RE-01, G05-REL-03).

**Principle SOC-RULE-04:** SOC-07 recency **must bind** to POC-06/POC-07/POC-10 — **must not** treat SOC-O1 or POC-O1 as SRDY-07 authority (LC-03 analog).

### Mapping: eight operator questions → implementation classes

| Surface question | Implementation class | Primary read sources |
|------------------|---------------------|----------------------|
| #1 — What is this project? | SOC-02 | MOC-02…06, POC-01, MOC-07 pointer, MOC-12 refs |
| #2 — Where is it now? | SOC-03 | POC-03 active + LC bind, suspension flags |
| #3 — What is blocked? | SOC-04 | POC-03…05, eligibility derived, LS-* halt |
| #4 — What is completed? | SOC-05 | POC-03 history, POC-04/05 with stale markers |
| #5 — What remains? | SOC-06 | MOC-04 endpoint, MOC-05 mask, open indexes |
| #6 — What happened recently? | SOC-07 | POC-06, POC-07 tail, POC-10 recency |
| #7 — What should happen next? | SOC-08 | Derived forward eligibility from SOC-04 + lifecycle |
| Cross-cutting integrity | SOC-09 | MOC-07 vs POC-03, ledger vs active, stale blocking |
| Portfolio entry (optional) | SOC-10 | ROC-01, ROC-05 → MOC-01 |

### Mapping: Surface Charter tiers → read composition obligation

| Charter tier | RT-G12 implementation rule |
|--------------|---------------------------|
| **Tier S-A — must always be visible** | SOC-02…SOC-08 **must** include all S-A classes or explicit empty-allowed signal — **core MVP read obligation** |
| **Tier S-B — conditionally visible** | SOC-11 **may** expose when POC-03…09 supply data — **must not** fake presence |
| **Tier S-C — must never belong** | Read composition **must not** surface Tier C material as Surface core — external link-out only if any |

### Read form factor (DF-07 — resolved at implementation standard)

| Rule ID | Implementation rule |
|---------|---------------------|
| **FF-01** | **Default MVP:** read binding **form-factor agnostic** — markdown index, CLI read path, static HTML index, or operator-maintained structured read map **all permitted** — **none mandated** |
| **FF-02** | **Forbidden:** dashboard product, widget system, SaaS operator console, multi-panel analytics UI (TX-07, SC-07) |
| **FF-03** | Whatever form factor chosen **must** expose SOC-01 discoverability and SOC-02…SOC-08 composition **without** requiring full monorepo search |
| **FF-04** | Form factor choice **does not** determine authority — read composition class separation **is normative** regardless of medium |
| **FF-05** | Separate Operator Display Charter (OQ-TS05) **may** refine render rules — **must** map to SOC-* and SRDY-*; **not** substitute for this standard |

---

## Surface Ownership

### What Surface read binding physically owns

Surface read binding **owns read composition artifacts and convergence discipline** — **not** tracking truth, **not** manifest categories, **not** registry catalog.

| Owned content | Implementation class | Owner write path |
|---------------|---------------------|------------------|
| Per-project read convergence point identity | SOC-01 | Operator read-bind act (post RT-G10 MOC-01 + substrate indexes) |
| Composed read view structure linking eight questions | SOC-02…SOC-08 | Operator read-bind create/update — **read-oriented only** |
| Integrity warning presentation rules | SOC-09 | Read-bind composition — flags **reflect** substrate, **do not author** truth |
| Optional portfolio select read assist | SOC-10 | Operator read-bind at portfolio scope — **optional** |
| Optional derived read cache | SOC-D1 | Operator or tooling **non-authoritative** refresh |
| Optional session read notes | SOC-O1 | Playbook 03 — **not** index substitute |

### What Surface read binding physically reads

Surface **consumes** substrate-backed records and manifest/registry pointers — **does not own** authoritative indexes.

| Read source | Typical locus | Read rule |
|-------------|---------------|-----------|
| Manifest entry anchor | MOC-01 | SOC-01 **starts from** discoverable MOC-01 — Playbook 03 E4 |
| Minimum understanding categories (operational slice) | MOC-02…06 | SOC-02 **operational depth** — PO-01; **not** Manifest essay |
| Reference topology pointers | MOC-08, MOC-12 | SOC-02 **follows refs** to POC-03…09 loci — TS-03 |
| Active state instance + history | POC-03 | SOC-03, SOC-05, SOC-06 |
| Gate outcome index | POC-04 | SOC-04, SOC-05, SOC-08 |
| Handoff event index | POC-05 | SOC-04, SOC-05, SOC-07 |
| Declaration records | POC-06 | SOC-07 recency |
| Progression ledger | POC-07 | SOC-07 narrative |
| Audit / recency markers | POC-10 | SOC-07 Tier S-A marker |
| Artefact ref index | POC-09 | SOC-05, SOC-06 |
| Closure terminal metadata | POC-08 | SOC-05, SOC-11 context only |
| Optional derived substrate cache | POC-D1 | SOC-D1 — **subordinate** to POC-03…07 |
| Portfolio catalog listing | ROC-01, ROC-02 | SOC-10 select only |
| Manifest pointer per catalog entry | ROC-05 | SOC-10 → MOC-01 chain |
| Distinction summaries (select context) | ROC-06 | SOC-10 — **non-authoritative** for blockers (RS-03) |
| Orientation snapshot on card | ROC-08 | SOC-10 — **reconcile** before trusting (R-H06) |
| Runtime vocabulary definitions | External canon docs | **Link only** — never Surface core |
| Foundation layer bodies | External workspaces | **Link only** — Tier S-C |

### What Surface read binding must never own

| Forbidden ownership | Actual owner | Guard |
|---------------------|--------------|-------|
| Live gate/handoff/state indexes | POC-03…POC-05; Playbook 04 | TRK-REL-01, MAP-05 |
| Declaration records & progression ledger | POC-06, POC-07; Playbook 04 | SE-03, DA-01 |
| Manifest minimum understanding serialization | MOC-*; RT-G10 | MAP-05, MT-01 |
| Portfolio catalog membership & lifecycle | ROC-*; RT-G05 | RE-01, RA-05 |
| Gate/handoff **criteria** | Runtime + Foundation | GV-01, Tier S-C |
| Layer artefact **bodies** | T1 layers / external | PO-02, RR-02 |
| Handoff package payloads | Generation Outputs | Tier S-C |
| Closure outcome **primary** persistence | POC-08; Playbook 05 | Playbook 05 scope |
| Tracking composition rules & zone ownership | Tracking Model Stage 3 | TS-01 |
| Automated transition / execution state | **Nobody in MVP** | OA-ACT-04 |
| SRDY-* pass/fail **authority** | Playbook 03 human assessment | SRB-01 |
| Site Type Registry entries | Foundation `registry/` | Tier S-C |

### Ownership principles

| ID | Principle |
|----|-----------|
| **SOWN-01** | RT-G12 **composes** read views; RT-G04 **hosts** POC records; RT-G10/05 **populate** binding facets — **must not** create parallel tracking SoT in read layer |
| **SOWN-02** | Only **Factory operator** **authoritatively mutates** POC-03…POC-07 via Playbook 04 — Surface read path **never writes** indexes (TRK-REL-01) |
| **SOWN-03** | Surface read-bind create/update **must not** grant declaration write path — read binding **≠** Playbook 04 channel |
| **SOWN-04** | RT-G10/05 implementations **never receive** authoritative writes from Surface read consumer |
| **SOWN-05** | Logical Factory Project **precedes** read bind; MOC-01 **precedes** meaningful SOC-02…08 depth (TS-02, G04-REL-02) |
| **SOWN-06** | SOC-D1 derived cache **must not** override POC-06/POC-03 when in conflict — DR-02 |

### Substrate vs manifest vs registry vs surface ownership

| Layer | Owns | Does not own |
|-------|------|--------------|
| **RT-G04 substrate** | Physical homes; POC class taxonomy; zone discipline | Read composition; Surface display |
| **RT-G10 manifest** | MOC-* within POC-02 manifest facet | Eight-question answers; live indexes |
| **RT-G05 registry** | ROC-* within POC-02 registry facet | Per-project Surface depth |
| **Playbook 04 / Tracking** | POC-03…POC-07 authoritative indexes | Read view structure |
| **RT-G12 Surface (this standard)** | SOC-* read composition; SOC-01 convergence | Any authoritative index write; tracking zones |

---

## Surface Readiness Model

SRDY-* governs **doctrinal observability completeness**; RT-G12 standard defines **implementation expectations** when physical read bind exists — **without** schemas, field lists, display labels, or storage layouts.

### SRDY → implementation standard mapping

| ID | Doctrinal criterion (Surface Charter) | RT-G12 implementation expectation |
|----|----------------------------------------|-----------------------------------|
| **SRDY-01** | Tier S-A classes present or explicitly empty-allowed | SOC-02…SOC-08 **must** surface each S-A class or explicit empty-allowed signal — **not** silent gap |
| **SRDY-02** | Valid active state (or invalid flagged) | SOC-03 **must** show active code or SOC-09 integrity warning — **no** silent normalization (VP-04) |
| **SRDY-03** | Declared endpoint explicit | SOC-02/SOC-06 **must** expose endpoint from MOC-04 / lifecycle bind |
| **SRDY-04** | Blocking summary derivable | SOC-04 **must** compose eligibility + open gate/handoff/halt — may be «none» if eligible |
| **SRDY-05** | Completion picture derivable for reached prefix | SOC-05 **must** expose completed states/gates/handoffs with stale markers visible |
| **SRDY-06** | Remaining picture derivable to endpoint | SOC-06 **must** derive remaining segments/gates/artefacts — **not** invent micro-states (ERA-W07) |
| **SRDY-07** | Recent event window non-empty or «no declarations yet» explicit | SOC-07 **must** show declaration recency tail from POC-06/07/10 or explicit none |
| **SRDY-08** | Forward picture derivable | SOC-08 **must** expose next eligibility or blocked-with-cause |
| **SRDY-09** | No Surface/Manifest/Tracking duplication violation | Read composition **must not** present second live gate/handoff SoT (MAP-05) |

### Readiness relationships (implementation terms)

| Concept | Implementation rule |
|---------|---------------------|
| **Surface-ready** | Operator can answer eight questions from SOC-* composition — **target** for read bind fidelity |
| **Surface-ready ⊇ manifest-ready** | MOC-01 reachable **precedes** meaningful SOC depth — TS-02 |
| **Surface-ready ⊄ gate-complete** | Blocked project may be surface-ready (OA-03) — SOC-04 **shows** blockers |
| **Surface-ready ≈ fully trackable** | Typical co-occurrence (TC-* + SRDY-*) — RT-G12 **reads** indexes, **does not** define TC-* |
| **Physical read bind ⊄ surface-ready retroactively** | Indexes may exist before SOC-01 — bind **enables** archaeology-free consumption |
| **Read bind ⊄ SRDY authority** | Playbook 03 **owns** human SRDY assessment — SOC-* **enable**, **do not replace** |

### Recency binding (OQ-PD05 — resolved at implementation standard)

| Rule ID | Implementation rule |
|---------|---------------------|
| **REC-01** | SOC-07 **must** read recency from POC-06 declaration tail, POC-07 progression events, and/or POC-10 audit marker — **authoritative chain** |
| **REC-02** | SOC-O1 and POC-O1 session notes **must not** satisfy SRDY-07 alone — explicit «no declarations yet» **required** when POC-06/07 empty |
| **REC-03** | Recent event window **depth** (OQ-TS01) — **bounded default:** logical tail sufficient for Playbook 03 reality phase; exact N **operator convention** — **not** schema |
| **REC-04** | «Since last session» semantics (OQ-TSW02) — **non-authoritative** filter only; authoritative recency = declaration chain (VP-03) |

### Tier binding (S-A / S-B / S-C)

| Tier | Surface Charter | RT-G12 implementation rule |
|------|-----------------|---------------------------|
| **S-A** | Must always be visible | SOC-02…SOC-08 core obligation — empty-allowed where charter permits early intake |
| **S-B** | Conditionally visible | SOC-11 — expose when indexes supply; **omit** when absent |
| **S-C** | Must never belong on Surface | **Exclude** from SOC core — external ref link only |

### Principle SRDY-IMPL-01 — Readiness ritual vs read representation

Playbook 03 **owns** session assessment using SRDY-* as observability lens. RT-G12 **owns** faithful SOC-* read access to persisted classes — **not** session workflow redesign, **not** automated SRDY pass evaluation as authority (SRB-01).

### Principle SRDY-IMPL-02 — SRDY-07 is the recency hinge

Standard is **incomplete** if SOC-07 recency class read obligation from persisted audit markers is ambiguous (REC-01…REC-04).

### MVP Surface read bind readiness checklist (operator, post-standard)

Before claiming C5/S4 satisfied on pilot:

| # | Check |
|---|-------|
| R-S1 | SOC-01 read convergence point discoverable per pilot project |
| R-S2 | MOC-01 reachable as read entry without repo-wide search |
| R-S3 | SOC-02…SOC-08 compose eight questions from POC-03…07 when indexes exist |
| R-S4 | SOC-07 shows recency or explicit «no declarations yet» |
| R-S5 | SOC-09 surfaces MOC-07/POC-03 mismatch when present |
| R-S6 | No second live gate/handoff index in read layer (SRDY-09) |
| R-S7 | Operator completes Playbook 03 session from read path — not full-repo archaeology |

---

## RT-G04 Relationship

RT-G04 **hosts** records Surface reads; RT-G12 **composes** SOC-* views **from** substrate — **without** storage redesign or write path.

### Consumption of RT-G04 provisions

| RT-G04 provision | RT-G12 implementation binding |
|------------------|-------------------------------|
| **DF-03** authorized zone | SOC-01 **resides in or references** per-project home within `workspaces/website-factory-operations/` |
| **P1** per-project record home | SOC-01 **converges on** one stable P1 locus per Factory Project |
| **P4** tracking instance records | SOC-03…SOC-06, SOC-08 **primary read source** for questions #2–#8 |
| **P5** declaration writes | SOC-07 **read-only** feed from POC-06, POC-07 |
| **POC-03…POC-07** | **Hard dependency** — meaningful C5 demo requires persisted indexes |
| **POC-10** audit/recency | SOC-07 Tier S-A last declaration marker |
| **POC-D1** derived cache | SOC-D1 **may consume** — **must not** treat as sole SoT if indexes diverge (DR-02) |
| **POC-O1** session notes | SOC-O1 analog — **not** SRDY-07 authority |
| **TRK-REL-01** read-only Surface | RT-G12 **excluded** from POC-03…07 write path — **hard** |
| **OWN-03** | Surface **never writes** POC-03…POC-07 |
| **INT-01…INT-10** | SOC-09 **reflects** integrity expectations — **does not enforce** automatically |

### Read feed model (implementation)

```text
  RT-G04 SUBSTRATE (POC-*)              RT-G12 SURFACE READ BINDING
  authorized zone                              │
       │                                       │
       ├── POC-01 identity ──────────────────▶ SOC-02
       ├── POC-02 manifest facet (read) ─────▶ SOC-02 (via MOC-*)
       ├── POC-03 state ─────────────────────▶ SOC-03, SOC-05, SOC-06, SOC-09
       ├── POC-04 gates ─────────────────────▶ SOC-04, SOC-05, SOC-08
       ├── POC-05 handoffs ──────────────────▶ SOC-04, SOC-05, SOC-07
       ├── POC-06 declarations ──────────────▶ SOC-07
       ├── POC-07 ledger ────────────────────▶ SOC-07
       ├── POC-08 closure ───────────────────▶ SOC-05, SOC-11 (context)
       ├── POC-09 artefact refs ─────────────▶ SOC-05, SOC-06
       ├── POC-10 audit ─────────────────────▶ SOC-07
       └── POC-D1 derived (optional) ────────▶ SOC-D1 (subordinate)
```

### RT-G04 forbidden overlap (RT-G12 must respect)

| Forbidden | Reason |
|-----------|--------|
| RT-G12 defining substrate zone structure or POC taxonomy | RT-G04 standard — DF-03 only |
| RT-G12 owning POC-03…POC-07 **writes** | Playbook 04 only — DA-01 |
| RT-G12 choosing persistence product or serialization | RT-G04 + RT-G10/05 standards |
| Read binding auto-mutating indexes on read | SC-03, TRK-REL-01, OA-ACT-04 |
| RT-G12 preceding substrate + manifest anchor stability | SC-02, G04-REL-02 |

**Principle G04-IMPL-01:** RT-G04 answers **where** Factory records live; RT-G12 answers **how operator reads** eight Surface question classes from that locus — **orthogonal** planes.

**Principle G04-IMPL-02:** RT-G12 read bind **must not** require substrate redesign — all SOC-* obligations resolve **within** read composition bounds.

---

## RT-G10 Relationship

Manifest implementation **precedes** Surface read depth; RT-G10 **enables** entry anchor; RT-G12 **must never duplicate** Manifest minimum understanding.

### Consumption of M-H01…M-H10 and MOC-* (guaranteed manifest provisions)

| Assumption / class | RT-G12 implementation binding |
|--------------------|--------------------------------|
| **M-H01** / **MOC-01** | SOC-01 **must start from** discoverable MOC-01 — Playbook 03 E4 |
| **M-H02** / **MOC-02** | SOC-02 **uses** logical identity — **does not** replace with registry entry ID |
| **M-H05** / **MOC-03…05** | SOC-02 **operational slice** of charter/scope/endpoint — PO-01; **not** full Manifest restatement |
| **M-H06** / **MOC-08, MOC-12** | SOC-02 **follows topology pointers** to POC-03…09 loci — **not** full map essay on Surface |
| **M-H07** | MOC-08 topology **not required** duplicated on SOC-01 — pointer traversal sufficient |
| **M-H09** | Operator path to MOC-01 **must work** without archaeology — SOC-01 entry |
| **M-H10** | On conflict, **manifest facet wins** for stable categories — SOC-02 **follows** MOC-11 amendment trail |
| **MOC-07** | SOC-03 **may reconcile** MOC-07 pointer vs POC-03 — SOC-09 when divergent |
| **MT-01, TRK-IMPL-01** | SOC-04/05 **read** POC-04/05 — **never** manifest facet as gate SoT |

### What RT-G12 must never duplicate from Manifest

| Manifest scope | RT-G12 exclusion |
|----------------|------------------|
| Minimum understanding contract restatement (Categories 1–5 depth) | SOC-02 operational slice only — PO-01 |
| Manifest entry anchor identification ritual | MRDY-06 — enrollment-time only |
| Authoritative reference topology **full map** | One-line pointer repeat **allowed**; essay **forbidden** |
| Stable category amendment narrative bodies | MOC-11 — Surface **reads outcome** |
| Per-project «start here» enrollment contract | RT-G10 scope — Surface **assumes** entry completed |
| MOC-X1 optional zone snapshot | Default absent — live indexes POC-03…07 only (TZ-01) |

### What Surface read binding provides that Manifest does not

| Surface read scope | Manifest exclusion |
|--------------------|-------------------|
| Eight operator questions from **live** index composition | Manifest = entry + minimum understanding |
| Tier S-A operational visibility (active state, blockers, recency) | MOC-07 pointer only — SOC-03/04/07 **materialize** |
| Actionability classes (OA-*) for Playbook 03 | Manifest **does not** enable daily supervision session |
| Integrity warnings when indexes inconsistent | Manifest **does not** own declaration truth (MA-02) |
| Blocking, completion, remaining, forward pictures | Manifest Category 6 **pointer** — not depth |

### Dependency edge

```text
  Playbook 01 ──▶ manifest-enrolled
       │
       ▼
  RT-G10 ──▶ MOC-01…MOC-12 on per-project home
       │
       ▼
  RT-G12 ──▶ SOC-01 convergence: MOC-01 → POC-03…07 → SOC-02…08
       │
       ▼
  Playbook 03 ──▶ eight questions via read path
```

**Principle M10-IMPL-01:** RT-G12 **must not** absorb manifest enrollment (Playbook 01) or MRDY-* evaluation — **entry consumption only** (M10-REL-01).

**Principle M10-IMPL-02:** Surface read **must not** treat manifest bind as substitute for Tracking gate/handoff index (MT-01, SRDY-09).

---

## RT-G05 Relationship

Registry implementation **optional** for Surface entry; RT-G05 **never** substitutes per-project Surface depth.

### Consumption of R-H01…R-H10 (guaranteed registry provisions)

| Assumption ID | RT-G12 implementation binding |
|---------------|-------------------------------|
| **R-H01** | SOC-10 **may exist** when operator uses portfolio path — **optional** for single-project MVP |
| **R-H02** | SOC-10 **must** follow ROC-05 → MOC-01 per selected ROC-02 entry |
| **R-H03** | ROC-06 distinction summaries **sufficient for select** — **not** for SOC-02…08 depth |
| **R-H04** | SOC-10 **may filter** by ROC-07 discoverability — VIEW-01 default |
| **R-H05** | SOC-04…08 **read** POC-03…07 after per-project select — **never** from registry facet |
| **R-H06** | ROC-08 **non-authoritative** — SOC-10 **must reconcile** before trusting blockers |
| **R-H07** | RT-G12 **never writes** ROC-* |
| **R-H08** | Playbook 03 **may start** from SOC-10 select — eight questions **only** after MOC-01 |
| **R-H09** | Withdrawn/archived entries — default hidden; extended view **operator/read-bind policy** |
| **R-H10** | RRDY attestation **outside** RT-G12 — Surface **does not** evaluate RRDY-* |

### What RT-G12 must never duplicate from Registry

| Registry scope | RT-G12 exclusion |
|----------------|------------------|
| Cross-project listing, discoverability lifecycle | SOC-10 select assist only — RE-01 |
| Distinction summaries at portfolio scale as Surface depth | SOC-10 context — SOC-02 **per-project** |
| Catalog membership / withdrawn / archived as primary orientation | ROC-07 context in SOC-10 only |
| RRDY-* enrollment attestation | Playbook 02 — **not** read bind scope |
| Portfolio orientation snapshot as blocker SoT | ROC-08 reconcile rule — R-H06 |

### What Surface read binding provides that Registry does not

| Surface read scope | Registry exclusion |
|--------------------|-------------------|
| Eight visibility questions for **one** selected project | Registry answers «which projects» — RE-01 |
| SOC-04…08 blocking/completion/remaining/forward/recency | RA-05 — **forbidden** on catalog |
| Per-project actionability assessment (Playbook 03) | Catalog **never** primary supervision surface |
| SRDY-07 declaration narrative | Registry **does not** own audit trail |

### Dependency edge

```text
  [optional] RT-G05 ──▶ SOC-10 portfolio select
       │
       ▼
  RT-G10 ──▶ MOC-01 entry anchor
       │
       ▼
  RT-G12 ──▶ SOC-01…08 per-project read binding
```

**Principle G05-IMPL-01:** Single-project Factory path **without** catalog remains **valid** — SOC-10 **not required** (G05-REL-02, R-H01).

**Principle G05-IMPL-02:** RT-G12 **must not** implement portfolio-scale Surface session — one Playbook 03 session = **one** Factory Project after select (G05-REL-03).

**Principle G05-IMPL-03:** RT-G12 **must not** absorb registry enrollment (Playbook 02) — **optional portfolio consumer only**.

---

## Tracking Relationship

Tracking **owns** composition semantics and instance indexes on substrate; Surface read binding **consumes** Tracking zones for visibility — **does not own** composition rules (Stage 3).

### What Surface read binding reads from Tracking composition

| Tracking zone (Tracking Model) | Surface read class | Operator question |
|--------------------------------|-------------------|-------------------|
| Identity references | SOC-02 | #1 |
| Charter & scope declaration refs | SOC-02, SOC-06 | #1, #5 |
| Current state reference | SOC-03 | #2 |
| State history reference | SOC-05, SOC-07 | #4, #6 |
| Eligibility snapshot (derived) | SOC-04, SOC-08 | #3, #7 |
| Scope state mask | SOC-02, SOC-06 | #1, #5 |
| Gate outcome records | SOC-04, SOC-05 | #3, #4 |
| Handoff event records | SOC-04, SOC-05, SOC-07 | #3, #4, #6 |
| Handoff package references | SOC-05, SOC-06 | #4, #5 |
| Layer artefact references | SOC-05, SOC-06 | #4, #5 |
| Audit trail (tracking-scoped) | SOC-07 | #6 |
| Invalidation / supersession markers | SOC-05, SOC-07, SOC-09 | #4, #6 |

### What remains in Tracking (not Surface-owned)

| Tracking responsibility | Surface exclusion |
|-------------------------|-------------------|
| Composition rules — how zones combine | Tracking Model Stage 3 — RT-G12 **reads result** |
| TC-* trackability evaluation semantics | Tracking Model — Playbook 03 **uses**, RT-G12 **does not redefine** |
| Zone ownership and index structure | POC-03…POC-07 on substrate — Playbook 04 writes |
| Authoritative declaration of transitions | Playbook 04 — Surface **shows** declared ledger (STV-03) |
| Gate/handoff **definitions** | Runtime + Foundation — Tier S-C |
| Seven tracking questions **doctrine** | Tracking Model — Surface adds **eighth recency** question per charter |

### Tracking visibility tier crosswalk

| Tracking Model tier | Surface Charter tier | RT-G12 rule |
|---------------------|------------------------|-------------|
| Tier A — minimal trackable | Tier S-A (+ S-B overlap) | SOC-02…08 **must** cover trackable minimum when indexes exist |
| Tier B — optional/deferred | Tier S-B | SOC-11 when data present |
| Tier C — excluded | Tier S-C | **Exclude** from SOC core |

### Playbook write plane separation

| Playbook | Surface read binding interaction |
|----------|----------------------------------|
| **01** | Manifest-enrolled precondition — RT-G12 **does not** participate |
| **02** | Optional SOC-10 portfolio select — RT-G12 **does not** evaluate RRDY |
| **03** | **Reads** SOC-01…08; SRDY assessment **human**; **must not** mutate POC-03…07 (SE-03) |
| **04** | **Mutates** POC-03…07 — Surface read **reflects** on next read — **no** auto-sync as authority (OQ-TS07 bounded) |
| **05** | POC-08 visible in SOC-05/11 — closure **not** Surface-owned |

**Principle TRK-IMPL-01:** Surface-ready ⊇ manifest-ready; indexes on substrate **precede** read bind; RT-G12 **enables consumption**, **does not create** tracking zones.

**Principle TRK-IMPL-02:** Operator path for seven/eight questions: **Manifest (MOC-01) → Tracking indexes (POC-03…07) → Surface read (SOC-*)** — Registry **optional prefix** only (RE-01).

**Principle TRK-IMPL-03:** Playbook 04 declaration **must not** silently duplicate gate rows into SOC-* or read-bind artefact as second SoT — INT-S05.

---

## Integrity Model

Minimum Surface read binding integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Implementation expectation |
|----|----------|---------------------------|
| **INT-S01** | **Read-only honesty** | SOC-* composition **must not** mutate POC-03…POC-07 on read — TRK-REL-01 |
| **INT-S02** | **Single read SoT** | Exactly **one** SOC-01 per Factory Project — no competing read convergence points |
| **INT-S03** | **Last-declared reflection** | SOC-03…08 **reflect** most recent Playbook 04 truth — freshness = declaration chain, not filesystem mtime (VP-03, AUTH-02) |
| **INT-S04** | **Invalid active visibility** | SOC-03 or SOC-09 **must flag** invalid active state — **no** silent normalization (VP-04, SV-05) |
| **INT-S05** | **Plane separation** | Read layer **must not** embed POC-04/POC-05 live tails as co-authoritative duplicate (MAP-05, SRDY-09) |
| **INT-S06** | **Manifest pointer honesty** | SOC-02 **follows** MOC-08/MOC-12 locators — broken refs **visible**; no silent body copy |
| **INT-S07** | **Registry glance honesty** | SOC-10 **must not** treat ROC-08 as blocker SoT — reconcile with POC-03 (R-H06, RS-03) |
| **INT-S08** | **Derived subordination** | SOC-D1 **must not** override POC-06/POC-03 when in conflict — DR-02 |
| **INT-S09** | **Recency honesty** | SOC-07 **must not** fabricate recency from SOC-O1 alone — REC-02 |
| **INT-S10** | **Stale visibility** | Stale/superseded markers **remain visible** in SOC-05/07 — **not** erased (VP-02, GV-05) |
| **INT-S11** | **Human-only read-bind mutation** | Only operator read-bind acts **change** SOC-* structure — no CI/agent auto-update of read composition as authority (OA-ACT-04) |

### What integrity model explicitly excludes

| Excluded | Reason |
|----------|--------|
| Automated schema validation of read composition | RT-G11 post-MVP |
| SRDY pass/fail automated engine | Playbook 03 owns assessment |
| Auto-sync read view from Tracking as **authoritative** | OQ-TS07 bounded — display-only sync **non-authoritative** if any |
| Cross-record referential integrity engine | Single-operator MVP; operator resolves |
| Gate pass/fail evaluation on read | GV-02 — human Playbook 04 |

### Integrity verification (human-operated)

MVP **accepts** operator manual review: Playbook 03 session surfaces SOC-09 conditions; Playbook 04 declaration review confirms read path reflects writes. Formal validators **deferred**.

---

## Boundary Protection

RT-G12 Surface read binding implementation **must never become** the following — inherited from Surface Charter, planning charter, RT-G04/RT-G10/RT-G05 separation, MVP exclusions.

### Forbidden system roles

| Forbidden system | Why | Guard anchor |
|------------------|-----|--------------|
| **Dashboard platform / operator SaaS / widget product** | TX-07, SC-07; Surface ≠ UI product | FF-02; MVP = minimum read binding |
| **Tracking composition engine / tracking storage** | TS-01; Stage 3 owns composition | RT-G12 **reads** indexes — **does not own** zones |
| **Persistence substrate product** | RT-G04 owns locus | Substrate design — **not RT-G12** |
| **Manifest / Passport / minimum understanding store** | MT-01, MAP-06; RT-G10 separate | Entry depth duplication **forbidden** |
| **Registry / portfolio catalog product** | RE-01, RA-05; RT-G05 separate | SOC-10 select only |
| **Database / query engine / analytics platform** | Scope creep; cross-project KPI rollups | No portfolio analytics on Surface |
| **Workflow engine / state machine executor** | MAP-04; RT-G01 | SOC-08 **enables** declare — **does not** transition |
| **Factory runtime product** | SC-01; RT-G09 | «Surface drives execution» — **rejected** |
| **Gate Results System / gate evaluator** | GV-02, MAP-10 | Surface **shows** outcomes — **does not evaluate** |
| **Project management system** | Scope creep | Tasks, sprints, assignments — **out of scope** |
| **Session workflow engine / automated supervision** | Playbook 03 human ritual | No CI/agent session open/close |
| **Declaration write path** | Playbook 04, DA-01 | Read binding **≠** declaration channel |
| **Automation / agent index mutation on read** | OA-ACT-04, SC-03 | Sync as authoritative — **forbidden** |
| **Notification / webhook hub** | RT-G13 | External approval — **post-MVP** |
| **Closure registry / terminal workflow engine** | Playbook 05 | POC-08 primary owner |
| **Control plane / orchestrator** | RT-G09, RT-G03 | Read binding **observes** — **does not command** |
| **Operator Display Charter as substitute** | OQ-TS05 | Separate future artifact — **must** map SOC-*, SRDY-* |

### Forbidden content in Surface read core

| Must never persist as Surface-owned authoritative content | Actual owner |
|-------------------------------------------------------------|--------------|
| Live gate outcome rows (duplicate) | POC-04 |
| Live handoff event sequence (duplicate) | POC-05 |
| Full state history authoritative copy | POC-03 |
| Declaration event bodies | POC-06 |
| Progression ledger authoritative copy | POC-07 |
| MOC-* minimum understanding bodies as substitute | POC-02 manifest facet |
| ROC-* catalog content as per-project depth | POC-02 registry facet |
| Layer artefact bodies | External workspaces |
| Gate/handoff criteria text | Runtime Architecture |
| Queue rank among projects | RT-G06 |

### Implementation anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| RT-G12 conflated with «shipped Factory runtime» or «dashboard MVP» | C5 ≠ RT-G09; TX-07; FF-02 |
| UI layout/wireframe design smuggled into **this** standard | Task forbidden list; FF-01 agnostic |
| Surface read duplicates live Manifest gate index | MT-01, SRDY-09, INT-S05 |
| Registry card answers eight questions | RE-01, RA-05, SOC-10 limits |
| Read binding **before** substrate indexes + MOC-01 stable | SC-02, SOWN-05 |
| Surface read replaces Playbook 04 declaration path | DA-01, TRK-REL-01 |
| `COMPLETE` / deploy conflated with Surface «completion» | LV-03, MAP-13 |
| RUNTIME-GAPS «dashboard» line interpreted as UX program mandate | OQ-TS09 — impl = read binding |
| Single read artefact swallowing manifest + tracking + surface | SOC-RULE-02; POC-RULE-02 |
| Auto-sync read composition mutating POC-* on refresh | INT-S01, OQ-TS07 bounded |

**Principle BP-IMPL-01:** RT-G12 is **per-project Surface read binding** — **one plane**, **one project**, **eight questions**, **read-only** — not a platform.

**Principle BP-IMPL-02:** Physical read binding **extends operability** of observability doctrine — **does not transfer** declaration authority to read channel or display layer (AUTH-01).

---

## Completion Model

### When RT-G12 Implementation Standard is **complete**

This deliverable is **standard-complete** when:

| Criterion | Status |
|-----------|--------|
| Surface object classes defined (SOC-01…SOC-11, SOC-D1, SOC-O1) | **Yes** |
| Eight-question mapping to SOC-* explicit | **Yes** |
| Surface ownership matrix (owns / reads / never owns) | **Yes** |
| SRDY-* implementation expectations without schemas | **Yes** |
| RT-G04 consumption model — read feed vs writes | **Yes** — G04-IMPL-* |
| RT-G10 dependency — entry anchor, non-duplication | **Yes** — M10-IMPL-* |
| RT-G05 dependency — optional portfolio, RE-01 | **Yes** — G05-IMPL-* |
| Tracking relationship — composition read vs ownership | **Yes** — TRK-IMPL-* |
| Minimum integrity expectations stated (no validators) | **Yes** — INT-S* |
| Boundary protection at implementation layer | **Yes** — BP-IMPL-* |
| DF-07 form factor bounded (FF-*) | **Yes** |
| OQ-PD05 recency binding (REC-*) | **Yes** |
| No UI, schemas, folders, code, or physical artefacts created | **Yes** |

### What standard-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| Physical SOC-* read artefacts **exist** in repo | Standard authorizes; creation = separate authorized track |
| RT-G12 gap in RUNTIME-GAPS marked IMPLEMENTED | Implementation execution not started |
| MVP **demonstrated** on pilot (S4) | Post-physical read bind + Playbook 03 |
| Operator dashboard **authorized** | Explicitly excluded — FF-02 |
| OQ-TS01 exact window N, OQ-TS03 PHASE_SLICE **resolved** | Deferred — not blockers |
| Zone path **exists on disk** | **SAFE UNKNOWN** until operator creates |

### Standard-complete vs implementation-executed

```text
  Surface Charter v1 (doctrine) ── COMPLETE
           │
           ▼
  RT-G04 Implementation Standard v1 ── COMPLETE
           │
           ▼
  RT-G10 Manifest Implementation Standard v1 ── COMPLETE
           │
           ▼
  RT-G05 Registry Implementation Standard v1 ── COMPLETE
           │
           ▼
  RT-G12 Surface Read Binding Implementation Standard v1 ── THIS (standard-complete)
           │
           ▼
  Physical read-bind artefact creation (SOC-01…08) ── ONLY when separately authorized
```

### Implementation Standards Era sequencing (complete)

```text
  RT-G04 ──▶ RT-G10 ──▶ RT-G05 ──▶ RT-G12
  substrate   manifest   registry   surface read
     │           │           │            │
     └───────────┴───────────┴────────────┘
              MVP capability floor C2→C3→C4→C5
```

### MVP operator path after RT-G12 standard (reference)

```text
  Playbook 01 ──▶ manifest-enrolled
       │
       ▼
  RT-G10 ──▶ MOC-01 physical anchor (C3)
       │
       ├──▶ [optional] Playbook 02 / RT-G05 ──▶ SOC-10 portfolio select
       │
       ▼
  RT-G12 ──▶ SOC-01…08 read binding (C5, S4)
       │
       ▼
  Playbook 03 ──▶ Surface session via read path
       │
       ▼
  Playbook 04 ──▶ declaration writes ──▶ Surface read reflects
       │
       ▼
  Playbook 05 ──▶ closure visible on read path
```

**Principle COMP-01:** Loss of RT-G12 standard clarity **must not** block Surface doctrine or Playbook 03 — doctrine **already operable** via manual composition (RDY-01).

**Principle COMP-02:** MVP S4 success **requires** physical read bind **after** RT-G04 substrate + RT-G10 MOC-01 + Playbook 04 indexes — not standard alone (RDY-02).

**Principle COMP-03:** RT-G12 standard-complete **does not** authorize physical MVP artefact creation, UI mockups, or dashboard prototypes — separate operator authorization required.

---

## Explicit Non-Claims

This document and the RT-G12 Tracking Surface Read Binding Implementation Standard it defines:

- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **UI design**, **dashboard design**, **screen layout**, **wireframe**, **widget system**, **navigation design**, or **operator product**;
- **are not** **storage design**, **database design**, **file format**, **JSON/YAML schema**, **folder structure**, or **physical MVP artefacts**;
- **are not** **tracking engine**, **tracking storage**, **state store**, or **recorder product**;
- **are not** **Manifest** (RT-G10) or **Registry** (RT-G05) redesign;
- **are not** **Persistence Substrate** (RT-G04) redesign — only **consumption** relationship;
- **are not** **Tracking Surface Charter** or **Tracking Model** rewrite — doctrine taken as authoritative input;
- **are not** Playbooks 01–05 rewrite;
- **are not** **implementation code**, **agents**, **validators**, or **CI binding**;
- **do not** define screens, panels, CLI commands, markdown templates, database tables, or read file paths;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** claim physical Surface read artefacts or operator dashboard **exist** in-repo — **standard only**;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound Surface read path;
- **do not** claim RT-G12 **implementation execution** is complete by existence of this document alone.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01. Surface read binding remains **read-oriented only** per TRK-REL-01.

Tracking Surface remains **Read Visibility Layer** — **not** Dashboard, Analytics Platform, Workflow Engine, Project Manager, or Control Center.

### Resolved in this standard (were OPEN in planning)

| ID | Resolution |
|----|------------|
| **DF-07** | FF-01…FF-05 — form-factor agnostic minimum read binding; dashboard product forbidden |
| **OQ-PD05** | REC-01…REC-04 — SOC-07 binds to POC-06/07/10; session notes non-authoritative |
| **OQ-TS07** | INT-S08, anti-pattern table — authoritative auto-sync **forbidden**; display-only non-authoritative bounded |
| **OQ-TS09** | BP section — impl = minimum read binding, not UX program |
| **OQ-R03** | G05-IMPL-02, R-H09 — default discoverable; extended view read-bind policy |

### Deferred (not blockers for this standard)

| ID | Disposition |
|----|-------------|
| **OQ-TS01** | Exact recent event window N — operator convention + Playbook 03; REC-03 bounded |
| **OQ-TS02** | Whether MOC-X1 holds Surface S-A subset — default read from POC-* per TZ-01 |
| **OQ-TS03** | PHASE_SLICE — one SOC-01 per shell vs slice — Engine v2 or case policy |
| **OQ-TS05** | Separate Operator Display Charter — future; must map SOC-*, SRDY-* |
| **OQ-TS06** | `PASS_WITH_WARNINGS` actionable class on read binding — gate composition |
| **OQ-TS08** | MIG correlation as Surface event class — RT-G08 |
| **OQ-TSW02** | «Since last session» filter semantics — REC-04 non-authoritative |
| **DF-08…DF-10** | Pilot pointer policy, git policy — operational cross-charter |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G12 Tracking Surface Read Binding Implementation Standard v1** as **RT-G12 standard-complete** — fourth and final Implementation Standard in authorized MVP sequence (RT-G04 → RT-G10 → RT-G05 → RT-G12).
2. **Preserve sequencing for execution:** Physical substrate zone + manifest bind + registry catalog (optional) + Playbook 04 indexes **before** meaningful C5/S4 demonstration via SOC-* read bind.
3. **Do not create yet:** dashboard mockups, FACTORY-DASHBOARD-v1.md, FACTORY-UI-SPEC-v1.md, FACTORY-TRACKING-SURFACE-STANDARD-v1.md, tracking storage schemas, Surface-as-write-channel prototypes, registry-as-Surface-depth prototypes, physical files under `workspaces/website-factory-operations/` — **unless separately authorized**.
4. **Optional P3:** Update RUNTIME-GAPS RT-G12 line to «STANDARD COMPLETE (read binding)» — **operator action**, outside this deliverable.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — RT-G04 standard records authorized zone |
| Whether any SOC-* read binding artefacts **exist** in-repo | **UNKNOWN** — standard authorizes; creation not part of deliverable |
| Which DF-07 form factor operator will choose for pilot | **not decided** — FF-01 permits multiple |
| Triumph / pilot workspaces as read-bind targets vs external-only refs | **UNKNOWN** — DF-08 per case |
| Whether any tool already renders Engine composition for supervision | **UNKNOWN** — no canonical read bind chartered pre-standard |
| Operators updated NEXT-PRIORITIES to Implementation Standards era (RT-G12 complete) | **UNKNOWN** |

---

*RT-G12 Tracking Surface Read Binding Implementation Standard v1 — fourth Website Factory Implementation Standard. Canonical location: `workspaces/website-factory-reference-v1/RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G12 Tracking Surface Read Binding Implementation Standard v1

**Stage:** RT-G12 — Tracking Surface Read Binding Implementation Standard (post–Planning Charter, fourth Implementation Standard)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md` (created)  
**Summary:** Четвёртый Implementation Standard Website Factory: перевод Tracking Surface Charter и RT-G12 planning charter в конкретную MVP-модель физического существования per-project Surface read binding — одиннадцать implementation object classes (SOC-01…SOC-11) plus SOC-D1/SOC-O1, ownership matrix (owns read composition / reads POC-* and MOC-* / never owns indexes), SRDY-* implementation expectations, relationships к RT-G04 (read feed), RT-G10 (MOC-01 entry, non-duplication), RT-G05 (optional SOC-10 portfolio select), Tracking Model (composition read vs zone ownership), minimum integrity model (INT-S*), boundary protection (Read Visibility Layer ≠ dashboard/tracker/workflow/PM/analytics/control plane), completion model; resolved DF-07 (FF-* form-factor agnostic), OQ-PD05 (REC-* recency binding), OQ-TS07/OQ-TS09/OQ-R03 — без UI, runtime, schemas, folders, code и physical artefacts.  
**Git:** no commit, no push (per task; document does not recommend commit).
