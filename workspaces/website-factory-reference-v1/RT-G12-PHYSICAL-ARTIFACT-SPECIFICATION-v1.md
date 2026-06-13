# REPORT — RT-G12 Physical Artifact Specification v1

**Версия:** v1  
**Дата:** 2026-06-07  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical Artifact Specification Era — **RT-G12 physical artifact specification only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE**; Physical MVP Artifact Definition **COMPLETE**; RT-G04 Physical Artifact Specification **COMPLETE**; RT-G10 Physical Artifact Specification **COMPLETE**; RT-G05 Physical Artifact Specification **COMPLETE**  
**Тип:** physical artifact specification only — **без** artifact creation, folder creation, file creation, serialization format, naming conventions, schemas, layout design, runtime, automation, workflow engine, UI design  
**Upstream:** [RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md](RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md), [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md)  
**Also reviewed:** [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), Operational Playbooks 01–05  
**Связь:** [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md), [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md)

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |
| **DF-07** | Form-factor agnostic minimum read binding (FF-01…FF-05) |
| **TX-07** | No dashboard product / operator SaaS in MVP |

---

## Purpose

### Зачем существует RT-G12 Physical Artifact Specification

**RT-G12 Physical Artifact Specification v1** переводит принятые implementation и review артефакты в **полную нормативную модель физической реальности** Tracking Surface read binding — определяя **какие физические Surface artifacts существуют**, **что авторитетно**, **как классы связаны** с RT-G04 substrate, Manifest, Registry и Tracking, **какие обязательства и гарантии** Surface несёт для operator visibility — **без** создания артефактов на диске и **без** выбора serialization format.

| Upstream отвечает | Эта specification отвечает |
|-------------------|---------------------------|
| Surface Charter — **doctrinal role** eight operator questions, Tier S-A/B/C, SRDY-* | **Физическая модель** Surface read binding как normative artifact reality |
| RT-G12 Implementation Standard — **SOC classes** и implementation obligations | **Завершённая specification** artifact class model, authority, relationships, guarantees |
| RT-G04 Physical Artifact Specification — **POC-* indexes** Surface reads | **SOC-* read composition reality** — без substrate redesign |
| RT-G10 Physical Artifact Specification — **MOC-01 entry anchor** | **SOC-01 convergence** from MOC-01 — non-duplication of manifest depth |
| RT-G05 Physical Artifact Specification — **ROC-01 portfolio select** | **SOC-10 optional assist** — portfolio select only |
| Physical MVP Definition Review — **Wave 1 SOC inventory** | **RT-G12 scope only** — SOC-01…SOC-11, SOC-D1, SOC-O1 и их физические обязательства |

### Нормативная формулировка physical artifact responsibility

**RT-G12 Physical Surface Artifacts (MVP specification)** — **авторизованные structured filesystem records** классов SOC-01…SOC-11 (и опциональных SOC-D1, SOC-O1), **материализованные как per-project read composition** в пределах или с привязкой к per-project record home на RT-G04 substrate, которые operator **читает** для Playbook 03 supervision и **вручную создаёт/обновляет** через operator read-bind act **после** RT-G10 MOC-01 stability и наличия substrate indexes — **без** shipped runtime, **без** automated read-side writes к POC-03…POC-07 и **без** определения формата сериализации или display product.

Surface physical artifacts **материализуют** operator visibility path (C5, S4) и eight-question read composition — **не** dashboard, **не** Tracking storage, **не** Manifest substitute, **не** Registry substitute, **не** declaration write channel.

### Specification purpose statement

Physical artifact specification **материализует** единую физическую модель Surface read binding, на которой:

1. **SOC-01** определяет canonical per-project read convergence point — MVP hinge (C5, S4, IS-01).
2. **SOC-02…SOC-08** определяют authoritative read composition slices для eight operator questions.
3. **SOC-09** определяет integrity warning presentation when cross-index reconciliation detects drift.
4. **SOC-10** определяет optional portfolio select assist — never eight questions at portfolio level.
5. **Authority, reference, optional, and prohibited** components формализованы с явным precedence.
6. **Physical obligations и guarantees** определяют минимум для valid Surface-capable Factory Project и Playbook 03 path without workspace archaeology.

Specification **не создаёт** physical artifacts — она **определяет физическую реальность Surface**, которую authorized creation track должен реализовать.

---

## Foundation Dependencies

Specification **наследует** upstream артефакты **без их переопределения**.

### Tier 0 — Implementation standard, substrate/manifest/registry specifications, reviews

| Document | Specification использует |
|----------|-------------------------|
| [RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md](RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md) | SOC-01…SOC-11 taxonomy; SOWN-*; SRDY-IMPL-*; INT-S01…S11; FF-*; REC-*; G04/M10/G05/TRK-IMPL-* |
| [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md) | LOC-ZONE, LOC-HOME; POC-01…POC-10; G12-01…G12-08; REL-11; PRJ-05 |
| [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md) | MOC-01…MOC-12; M-G12-01…M-G12-10; REL-M13…REL-M17 |
| [RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md) | ROC-01…ROC-11; R-G12-01…R-G12-10; R-H01…R-H10; HAND-R-SPEC-* |
| [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md) | Wave 1 SOC disposition; mandatory/optional/forbidden; Phase E creation sequence |
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Eight questions, Tier S-A/B/C, SRDY-*, VP-*, PO-*, STV-*, GV-*, LV-*, EV-*, OA-* — **sole doctrine source** |

### Tier 1 — Tracking and operational doctrine

| Document | Specification использует |
|----------|-------------------------|
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking zones, Tier A/B/C, seven questions, TC-* — **composition source** Surface reads |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — eight questions session; SE-03 read-only; SRDY assessment ritual |
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-04; operator path Registry→Manifest→Tracking→Surface |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — declarations update indexes Surface **reads** |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — POC-08 visible on read path; closure not Surface-owned |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — manifest-enrolled precondition |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — optional portfolio select precondition |

### Tier 2 — Engine boundary

| Document | Constraint on RT-G12 specification |
|----------|--------------------------------------|
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04; Surface read binding **external** to Engine docs |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | SV-*, SHV-* — Surface **shows**, **does not redefine** |

**Authority precedence:** Foundation Freeze + Engine → Surface Charter (doctrine) → Tracking Model → RT-G04 Physical Artifact Specification → RT-G10 Physical Artifact Specification → RT-G05 Physical Artifact Specification → RT-G12 Implementation Standard → **эта specification** → physical creation (separate authorization).

**Scope boundary (SPEC-SCOPE-04):** Эта specification covers **RT-G12 SOC classes only** — read composition artifacts. POC substrate classes, MOC manifest classes, ROC registry classes belong to **separate standard-specific tracks** — RT-G04, RT-G10, RT-G05 respectively. SOC-* **references** POC-*/MOC-*/ROC-* — **does not host** authoritative indexes.

---

## Surface Artifact Class Model

Normative **classes** — не file names, не schemas, не folder trees, не serialization labels, не screen regions.

### Authoritative surface read classes (SOC-01…SOC-11)

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **SOC-01** | **Read convergence point** | Per-project canonical locus where eight-question read composition **starts** | Operator discovers **one authorized read path** per Factory Project without full-repo search; materialization of IS-01, C5 | **Must persist** per bound project |
| **SOC-02** | **Orientation view** | Read composition for question #1 — identity, charter summary, scope tier, endpoint, mask, conditional classification | Operational slice from MOC-02…06 + POC-01 — **not** Manifest essay (PO-01) | **Must compose** |
| **SOC-03** | **State view** | Read composition for question #2 — active state, LC segment, halt/suspension, invalid flag | Reflects POC-03 active + lifecycle bind (STV-01, SV-*) | **Must compose** |
| **SOC-04** | **Blocking view** | Read composition for question #3 — open blocker summary, gate/handoff/halt, eligibility snapshot | Derived from POC-03…05 + eligibility (GV-*, GV-02) | **Must compose** |
| **SOC-05** | **Completion view** | Read composition for question #4 — completed states/segments, satisfied gates, cleared handoffs, stale markers | POC-03 history + POC-04/05 with stale visibility (SHV-*, GV-03/05) | **Must compose** |
| **SOC-06** | **Remaining view** | Read composition for question #5 — remaining segments/gates/artefacts to declared endpoint | Derived from MOC-04 endpoint, MOC-05 mask, open indexes (LPC-03) | **Must compose** |
| **SOC-07** | **Recency view** | Read composition for question #6 — progression ledger tail, recent declarations, invalidations, explicit «no declarations yet» | Binds to POC-06, POC-07, POC-10 — **not** SOC-O1 alone (REC-01…04, SRDY-07) | **Must compose** |
| **SOC-08** | **Forward view** | Read composition for question #7 — next segment eligibility or blocked-with-cause | **Derived** from SOC-04 + lifecycle — enables declare decision (OA-01); **does not execute** | **Must compose** |
| **SOC-09** | **Integrity warning surface** | Read-visible flags when indexes inconsistent — invalid active, ledger ≠ active, stale blocking, manifest/tracking drift | Reflects VP-04, MS-02, INT-S04…S10 conditions — **does not author** truth | **Must compose when detected** |
| **SOC-10** | **Portfolio select assist** | Optional read path from ROC-01 catalog to MOC-01 per selected project | Portfolio **select only** — eight questions **never** primary at catalog level (IS-12, RE-01) | **May persist** at portfolio scope |
| **SOC-11** | **Tier S-B conditional views** | Conditional read slices when substrate supplies data — classification, generation freeze, parallel legal, drill-down gate detail | Expose when POC-03…09 supply data — **must not** fake presence | **May compose** when data present |

### Optional / subordinate surface classes

| Class ID | Class name | Physical meaning | Class responsibility | MVP disposition |
|----------|------------|------------------|---------------------|-----------------|
| **SOC-D1** | **Derived read cache** | Regeneratable composed views from POC-D1 or local read-side cache | Eligibility rollup, SRDY derived views — **non-authoritative** (DR-01 analog) | **Optional** — subordinate to POC-03…07 |
| **SOC-O1** | **Session read notes** | Pre-declaration Playbook 03 session notes at read plane | POC-O1 analog — **not authoritative** for SRDY-* or indexes (LC-03 analog) | **Optional** — non-authoritative |

### Class composition model (conceptual — not layout)

```text
  [optional] portfolio scope
       │
       └── SOC-10 Portfolio select assist ──▶ ROC-01 → ROC-05 → MOC-01
                                                    │
  per-project record home (RT-G04 LOC-HOME)           │
       │                                            │
       ├── MOC-01 Entry anchor ◀────────────────────┘
       │
       └── SOC-01 Read convergence point ◀── MVP hinge (C5, S4)
             │
             ├── SOC-02 Orientation view      ← MOC-02…06, POC-01, MOC-07 pointer
             ├── SOC-03 State view            ← POC-03, lifecycle bind
             ├── SOC-04 Blocking view         ← POC-03…05, POC-D1 optional
             ├── SOC-05 Completion view       ← POC-03…05 history + stale markers
             ├── SOC-06 Remaining view        ← MOC-04/05 + open indexes
             ├── SOC-07 Recency view          ← POC-06, POC-07, POC-10
             ├── SOC-08 Forward view          ← derived eligibility
             ├── SOC-09 Integrity warnings    ← cross-index reconciliation
             ├── SOC-11 Tier S-B views        ← when indexes supply conditional classes
             └── SOC-D1 derived cache (optional, subordinate)
```

### Class principles

| ID | Principle |
|----|-----------|
| **SOC-RULE-01** | Exactly **one** canonical SOC-01 read convergence point per Factory Project identity — no competing per-project Surface read SoT |
| **SOC-RULE-02** | SOC-02…SOC-08 **must compose from** substrate authoritative records (POC-03…POC-07, POC-10) and manifest pointers (MOC-*) — **must not** duplicate live gate/handoff index as second authoritative store (MAP-05, MT-01) |
| **SOC-RULE-03** | SOC-10 **must remain** portfolio-scope **select assist only** — eight questions **never** primary at catalog level (RE-01, G05-REL-03) |
| **SOC-RULE-04** | SOC-07 recency **must bind** to POC-06/POC-07/POC-10 — **must not** treat SOC-O1 or POC-O1 as SRDY-07 authority |
| **RTG12-CLASS-01** | RT-G12 specification covers **SOC-* classes only** — POC/MOC/ROC physical shape is RT-G04/RT-G10/RT-G05 scope |

### Eight operator questions → physical class mapping

| Surface question | Physical class | Primary read sources |
|------------------|----------------|----------------------|
| #1 — What is this project? | SOC-02 | MOC-02…06, POC-01, MOC-07 pointer, MOC-12 refs |
| #2 — Where is it now? | SOC-03 | POC-03 active + LC bind, suspension flags |
| #3 — What is blocked? | SOC-04 | POC-03…05, eligibility derived, LS-* halt |
| #4 — What is completed? | SOC-05 | POC-03 history, POC-04/05 with stale markers |
| #5 — What remains? | SOC-06 | MOC-04 endpoint, MOC-05 mask, open indexes |
| #6 — What happened recently? | SOC-07 | POC-06, POC-07 tail, POC-10 recency |
| #7 — What should happen next? | SOC-08 | Derived forward eligibility from SOC-04 + lifecycle |
| Cross-cutting integrity | SOC-09 | MOC-07 vs POC-03, ledger vs active, stale blocking |
| Portfolio entry (optional) | SOC-10 | ROC-01, ROC-05 → MOC-01 |

### Surface Charter tier → physical class obligation

| Charter tier | RT-G12 physical specification rule |
|--------------|-----------------------------------|
| **Tier S-A — must always be visible** | SOC-02…SOC-08 **must** include all S-A classes or explicit empty-allowed signal — **core MVP read obligation** |
| **Tier S-B — conditionally visible** | SOC-11 **may** expose when POC-03…09 supply data — **must not** fake presence |
| **Tier S-C — must never belong** | Read composition **must not** surface Tier C material as Surface core — external link-out only if any |

### Read form factor (DF-07 — inherited, not reopened)

| Rule ID | Physical specification rule |
|---------|----------------------------|
| **FF-01** | **Default MVP:** read binding **form-factor agnostic** — markdown index, CLI read path, static HTML index, or operator-maintained structured read map **all permitted** — **none mandated** |
| **FF-02** | **Forbidden:** dashboard product, widget system, SaaS operator console, multi-panel analytics UI (TX-07, SC-07) |
| **FF-03** | Whatever form factor chosen **must** expose SOC-01 discoverability and SOC-02…SOC-08 composition **without** requiring full monorepo search |
| **FF-04** | Form factor choice **does not** determine authority — read composition class separation **is normative** regardless of medium |
| **FF-05** | Separate Operator Display Charter (OQ-TS05) **may** refine render rules — **must** map to SOC-* and SRDY-*; **not** substitute for this specification |

---

## Authority Model

### Four surface content categories

| Category | SOC classes | Authority rule |
|----------|-------------|----------------|
| **Authoritative read composition** | SOC-01…SOC-08, SOC-09 (when conditions detected) | Must survive between sessions for archaeology-free Playbook 03; loss breaks C5/S4 without full-repo search |
| **Optional read assist** | SOC-10, SOC-11 | SOC-10 portfolio select **optional** for single-project path; SOC-11 when substrate supplies S-B data |
| **Derived / subordinate** | SOC-D1 | Regeneratable from POC-03…07 + POC-D1 — **must not** override authoritative indexes (DR-02) |
| **Operational / session-local** | SOC-O1 | Pre-declaration Playbook 03 notes — **must not** substitute POC-06/POC-07 for SRDY-07 |

### Authority matrix by class

| Class | Authoritative for | Not authoritative for | Write authority |
|-------|-------------------|----------------------|-----------------|
| **SOC-01** | Read convergence point identity; «start read here» discoverability | Tracking truth; manifest categories; registry catalog | Operator read-bind create/update act (post MOC-01 + substrate indexes) |
| **SOC-02** | Composed orientation **read view** linking question #1 | Manifest minimum understanding bodies; charter essay depth | Operator read-bind composition update — **read-oriented only** |
| **SOC-03** | Composed state **read view** for question #2 | Active state truth — POC-03 owns | Operator read-bind composition — **reflects** POC-03 |
| **SOC-04** | Composed blocking **read view** for question #3 | Gate criteria; gate pass/fail authority | Operator read-bind composition — **reflects** POC-03…05 |
| **SOC-05** | Composed completion **read view** for question #4 | State/gate/handoff authoritative indexes | Operator read-bind composition — **reflects** POC-03…05 |
| **SOC-06** | Composed remaining **read view** for question #5 | Declared endpoint category — MOC-04 owns | Operator read-bind composition — **derives** from indexes + MOC-04/05 |
| **SOC-07** | Composed recency **read view** for question #6 | Declaration truth trail — POC-06/07 own | Operator read-bind composition — **binds** to POC-06/07/10 |
| **SOC-08** | Composed forward **read view** for question #7 | Transition execution; declare authority | Operator read-bind composition — **derived only** |
| **SOC-09** | Integrity warning **presentation rules** | Underlying index truth | Operator read-bind composition — **flags reflect** substrate |
| **SOC-10** | Portfolio select **read path structure** | Per-project eight-question depth | Operator read-bind at portfolio scope — **optional** |
| **SOC-11** | Conditional S-B **read slices** when data present | Tier A minimum — SOC-02…08 own | Operator read-bind composition when indexes supply |
| **SOC-D1** | — (derived cache only) | Any declarer or index authority | Operator or tooling **non-authoritative** refresh |
| **SOC-O1** | — | SRDY-* or index authority | Playbook 03 session notes only |

### Authoritative vs referenced vs optional vs prohibited — summary

| Disposition | Components | Precedence when conflict |
|-------------|------------|-------------------------|
| **Authoritative (Surface-owned read composition)** | SOC-01…SOC-08 structure; SOC-09 presentation when triggered | Read composition **must not** present second live gate/handoff SoT — POC-04/05 **win** (SRDY-09, INT-S05) |
| **Referenced (Surface reads, does not own)** | POC-03…POC-07, POC-10; MOC-01…MOC-12; ROC-01/05/06/07/08 for SOC-10; POC-D1 for SOC-D1 | POC-06/POC-03 tail **wins** over SOC-D1; MOC-02…05 **win** over ROC-06 for stable categories; POC-03 **wins** over MOC-07 and ROC-08 |
| **Optional** | SOC-10, SOC-11, SOC-D1, SOC-O1 | Absence **valid** for single-project Factory path (G05-REL-02); S-A classes sufficient without SOC-11 |
| **Prohibited inside Surface read core** | Live gate/handoff rows duplicate; declaration bodies; MOC-* minimum understanding substitute; ROC-* catalog as per-project depth; layer bodies; gate criteria; eight answers at portfolio level | Actual owners per Boundary Protection section |

### Authority precedence rules

| Rule ID | Precedence |
|---------|------------|
| **AUTH-S01** | POC-06/POC-03 tail **wins over** SOC-D1 and POC-D1 when in conflict — DR-02, INT-S08 |
| **AUTH-S02** | Last Playbook 04 act **wins** for POC-03…05 active view — SOC-03…08 **reflect** on next read (INT-S03, VP-03) |
| **AUTH-S03** | MOC-02…MOC-05 stable categories **win over** ROC-06 distinction summaries on conflict — M-H10; SOC-02 **follows** manifest facet |
| **AUTH-S04** | POC-03 active state **wins over** MOC-07 position summary and ROC-08 orientation — SOC-09 **may surface** mismatch |
| **AUTH-S05** | Playbook 04 **must not** silently duplicate gate rows into SOC-* as second SoT — INT-S05, TRK-IMPL-03 |
| **AUTH-S06** | Only Factory operator **authoritatively mutates** SOC-* read composition structure — no CI/agent auto-update as authority (INT-S11, OA-ACT-04) |
| **AUTH-S07** | RT-G12 Surface **never writes** POC-03…POC-07, MOC-*, or ROC-* — read-oriented only (OWN-03, TRK-REL-01, R-H07) |
| **AUTH-S08** | Playbook 03 **owns** human SRDY assessment — SOC-* **enable**, **do not replace** (SRB-01) |

### Ownership summary

| Layer | Owns surface physical artifact reality | Does not own |
|-------|----------------------------------------|--------------|
| **RT-G04 substrate** | LOC-HOME; POC-* authoritative indexes; zone discipline | Read composition structure; Surface display |
| **RT-G10 manifest** | MOC-* within POC-02 manifest facet | Eight-question answers; live indexes |
| **RT-G05 registry** | ROC-* within POC-02 registry facet | Per-project Surface depth |
| **Playbook 04 / Tracking** | POC-03…POC-07 authoritative indexes | Read view structure |
| **RT-G12 (this specification)** | SOC-* read composition; SOC-01 convergence discipline | Any authoritative index write; tracking zones; declaration channel |

---

## Relationship Model

### Surface within substrate (RT-G04)

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-S01** | SOC-01 **resides in or references** per-project home within `workspaces/website-factory-operations/` | DF-03, G12-01; SOC-01 **converges on** one stable LOC-HOME per Factory Project |
| **REL-S02** | SOC-02…SOC-08 **read** POC-03…POC-07, POC-10 at project LOC-HOME | G12-01…G12-06; **hard dependency** for meaningful C5 demo |
| **REL-S03** | SOC-07 **read-only** feed from POC-06, POC-07, POC-10 | G12-05; REC-01…REC-04 |
| **REL-S04** | SOC-D1 **may consume** POC-D1 — **must not** treat as sole SoT if indexes diverge | DR-02, INT-S08 |
| **REL-S05** | RT-G12 **excluded** from POC-03…07 write path — **hard** (TRK-REL-01, OWN-03) | Playbook 04 sole declarer |
| **REL-S06** | SOC-09 **reflects** RT-G04 integrity expectations INT-01…INT-10 — **does not enforce** automatically | Human-operated reconciliation |
| **REL-S07** | SOC-* read composition **references** project-scope POC-* — SOC-* is **not** RT-G04 storage class (PRJ-05) | Plane separation |

### Surface ↔ Manifest (RT-G10)

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-S08** | SOC-01 **must start from** discoverable MOC-01 — Playbook 03 E4 | M-G12-01, M-H01 |
| **REL-S09** | SOC-02 **uses** MOC-02…MOC-06 operational slice — **not** full Manifest restatement (PO-01) | M-G12-02, M-G12-07 |
| **REL-S10** | SOC-02 **follows** MOC-08/MOC-12 topology pointers to POC-03…09 loci | M-G12-03, TS-03 |
| **REL-S11** | SOC-03 **may reconcile** MOC-07 pointer vs POC-03 — SOC-09 when divergent | M-G12-04, MS-02 |
| **REL-S12** | SOC-04/05 **read** POC-04/05 — **never** manifest facet as gate SoT | M-G12-05, MT-01, TRK-IMPL-01 |
| **REL-S13** | SOC-06 **uses** MOC-04 endpoint and MOC-05 applicability for remaining view | M-G12-06 |
| **REL-S14** | MOC-01 **precedes** meaningful SOC-02…08 depth — TS-02, SOWN-05 | Manifest-ready ⊂ surface-ready prerequisite |
| **REL-S15** | RT-G12 **must not** absorb manifest enrollment (Playbook 01) or MRDY-* evaluation | M10-IMPL-01 — entry consumption only |

### Surface ↔ Registry (RT-G05)

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-S16** | SOC-10 **may exist** when operator uses portfolio path — **optional** for single-project MVP | R-H01, G05-IMPL-01 |
| **REL-S17** | SOC-10 **must follow** ROC-05 → MOC-01 per selected ROC-02 entry | R-H02, REL-R03 |
| **REL-S18** | ROC-06 distinction summaries **sufficient for select** — **not** for SOC-02…08 depth | R-H03, HAND-R-SPEC-03 |
| **REL-S19** | SOC-10 **must not** treat ROC-08 as blocker SoT — reconcile with POC-03 | R-H06, INT-S07, RS-03 |
| **REL-S20** | RT-G12 **never writes** ROC-* | R-H07 |
| **REL-S21** | Playbook 03 **may start** from SOC-10 select — eight questions **only** after MOC-01 | R-H08, G05-REL-03 |
| **REL-S22** | RT-G12 **must not** absorb registry enrollment (Playbook 02) — optional portfolio consumer only | G05-IMPL-03 |

### Surface ↔ Tracking

| Rule ID | Relationship | Normative constraint |
|---------|--------------|---------------------|
| **REL-S23** | Tracking **owns** composition semantics and instance indexes on substrate; Surface **consumes** zones for visibility | TS-01; Stage 3 owns rules |
| **REL-S24** | SOC-03…SOC-06, SOC-08 **primary read source** for questions #2–#8 from POC-03…07 | TRK-IMPL-01 |
| **REL-S25** | Playbook 04 **mutates** POC-03…07 — Surface read **reflects** on next read — **no** auto-sync as authority | TRK-IMPL-03, OQ-TS07 bounded |
| **REL-S26** | Surface-ready ⊇ manifest-ready; indexes on substrate **precede** read bind | TRK-IMPL-01, TRK-IMPL-02 |
| **REL-S27** | Operator path: **Manifest (MOC-01) → Tracking indexes (POC-03…07) → Surface read (SOC-*)** — Registry **optional prefix** | RE-01, TRK-IMPL-02 |
| **REL-S28** | Tracking Model seven questions + Surface eighth recency — Surface **does not redefine** TC-* | Tracking Model doctrine |

### Surface ↔ Playbooks

| Playbook | Surface physical artifact interaction | Record classes |
|----------|--------------------------------------|----------------|
| **01** Manifest enrollment | Manifest-enrolled precondition — RT-G12 **does not** participate | **None** in SOC-* until read bind |
| **02** Registry enrollment | Optional SOC-10 portfolio select — RT-G12 **does not** evaluate RRDY | Read ROC-* only when SOC-10 exists |
| **03** Surface session | **Reads** SOC-01…08; SRDY assessment **human**; **must not** mutate POC-03…07 (SE-03) | Read SOC-*; optional SOC-O1 |
| **04** Project declaration | **Mutates** POC-03…07 — Surface read **reflects** on next read | **No** SOC-* authoritative write to indexes |
| **05** Project closure | POC-08 visible in SOC-05/11 — closure **not** Surface-owned | Read-only visibility |

### Lifecycle dependency graph

```text
  PRE-FACTORY (no surface records)
       │
       ▼
  Playbook 01 + RT-G10 ──▶ MOC-01…MOC-12 on per-project LOC-HOME
       │
       ├──▶ [optional] Playbook 02 + RT-G05 ──▶ ROC-01…ROC-10
       │
       ▼
  Playbook 04 (first declaration) ──▶ POC-03…07, POC-10
       │
       ▼
  Operator read-bind act ──▶ SOC-01 + SOC-02…SOC-08 composition
       │
       ├──▶ [optional] SOC-10 portfolio select assist
       │
       ▼
  Playbook 03 ──▶ eight questions via SOC-* read path (repeat)
       │
       ▼
  Playbook 04 ──▶ declaration writes ──▶ Surface read reflects
       │
       ▼
  Playbook 05 ──▶ closure visible on read path
```

### Tracking visibility tier crosswalk

| Tracking Model tier | Surface Charter tier | RT-G12 physical rule |
|---------------------|------------------------|----------------------|
| Tier A — minimal trackable | Tier S-A (+ S-B overlap) | SOC-02…08 **must** cover trackable minimum when indexes exist |
| Tier B — optional/deferred | Tier S-B | SOC-11 when data present |
| Tier C — excluded | Tier S-C | **Exclude** from SOC core |

---

## Physical Obligations

### What must physically exist for a valid Surface-capable Factory Project

A **valid Factory Project with physical Surface read binding** requires satisfaction of obligations below. Obligations are **class-level** — not file counts or serialization shapes.

**Doctrinal precondition (not a disk artifact):** Playbook 01 manifest-enrolled and RT-G10 MOC-01 physical bind **must precede** meaningful SOC-02…08 depth (TS-02, SOWN-05).

**Substrate precondition:** POC-03…POC-07 indexes **should exist** for credible Playbook 03 demonstration — empty shells permitted at `NEW_PROJECT`; **meaningful C5/S4** typically requires at least one Playbook 04 declaration cycle (COMP-02).

### Tier 0 — Substrate and manifest prerequisites (RT-G04, RT-G10)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-S-SUB-01** | **LOC-ZONE** at authorized path | Before any SOC materialization |
| **OBL-S-SUB-02** | **LOC-HOME** — exactly one per Factory Project identity | Before read bind |
| **OBL-S-SUB-03** | **MOC-01** entry anchor discoverable | Manifest bind — **precedes** SOC-01 depth |
| **OBL-S-SUB-04** | **POC-03…POC-05** index loci (empty OK at scaffold) | Index scaffold before credible session |
| **OBL-S-SUB-05** | **POC-06, POC-07, POC-10** when declarations exist | First Playbook 04 act for recency depth |

### Tier 1 — Core surface read binding (C5, S4)

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-S-01** | **SOC-01** read convergence point | Operator read-bind act — **core MVP obligation** |
| **OBL-S-02** | **SOC-02** orientation view composition | Read-bind act |
| **OBL-S-03** | **SOC-03** state view composition | Read-bind act |
| **OBL-S-04** | **SOC-04** blocking view composition | Read-bind act |
| **OBL-S-05** | **SOC-05** completion view composition | Read-bind act |
| **OBL-S-06** | **SOC-06** remaining view composition | Read-bind act |
| **OBL-S-07** | **SOC-07** recency view composition | Read-bind act |
| **OBL-S-08** | **SOC-08** forward view composition | Read-bind act |

### Tier 2 — Conditional / lifecycle-triggered

| Obligation ID | Must physically exist | Trigger |
|---------------|----------------------|---------|
| **OBL-S-09** | **SOC-09** integrity warning presentation | When MOC-07/POC-03 mismatch, stale blocking, or ledger drift detected |
| **OBL-S-10** | **SOC-10** portfolio select assist | **Optional** — when operator uses portfolio path for Playbook 03 (recommended for S3 demo) |
| **OBL-S-11** | **SOC-11** Tier S-B conditional views | **Optional** — when substrate supplies conditional data |
| **OBL-S-D1** | **SOC-D1** derived read cache | **Optional** — non-authoritative convenience |
| **OBL-S-O1** | **SOC-O1** session read notes | **Optional** — Playbook 03 pre-declaration notes |

### Persistent surface inventory by milestone

| Must exist after | Surface physical classes |
|------------------|-------------------------|
| Manifest bind only | **None** — MOC-01 exists; SOC-* not yet obligated |
| Operator read-bind act | SOC-01, SOC-02…SOC-08 |
| Integrity condition detected | SOC-09 presentation active |
| Portfolio path demo (optional) | SOC-10 at portfolio scope |
| Playbook 03 session (optional) | SOC-O1 may accumulate — **not** authoritative |

### Minimum bootstrap before credible Playbook 03 session via read path

| # | Physical element | Phase reference |
|---|------------------|-----------------|
| 1 | LOC-ZONE + LOC-HOME exist | RT-G04 substrate |
| 2 | MOC-01 discoverable as read entry | RT-G10 manifest bind |
| 3 | POC-03…POC-05 loci (empty OK) | Index scaffold |
| 4 | At least one Playbook 04 declaration (recommended) | Declaration cycle |
| 5 | SOC-01 read convergence point bound | RT-G12 read-bind |
| 6 | SOC-02…SOC-08 wired to POC-* + MOC-* read feeds | RT-G12 read-bind |
| 7 | SOC-07 shows recency or explicit «no declarations yet» | REC-02 |
| 8 | [Optional] ROC-01 → SOC-10 → MOC-01 chain for portfolio demo | RT-G05 + RT-G12 |

### What is NOT a physical obligation of RT-G12

| Not required by RT-G12 | Owner |
|------------------------|-------|
| POC-03…POC-07 index **content** creation | Playbook 04; RT-G04 |
| MOC-* manifest content | RT-G10 physical specification |
| ROC-* catalog content | RT-G05 physical specification |
| Serialization format | Deferred — not in this specification |
| Dashboard / UI product | Forbidden — FF-02, TX-07 |
| SRDY pass/fail authority | Playbook 03 human assessment |

---

## Physical Guarantees

RT-G12 physical artifact specification **guarantees** the following to the Factory operator **without defining serialization, UI, or dashboards**.

### Eight-question visibility guarantees (doctrine → physical)

| Guarantee ID | Operator may rely on (when SOC-* read bind exists) |
|--------------|---------------------------------------------------|
| **S-GUAR-01** | **Question #1:** SOC-02 exposes project orientation from MOC-02…06 + POC-01 — identity, charter summary, scope tier, endpoint, mask — or explicit empty-allowed where charter permits (SRDY-01) |
| **S-GUAR-02** | **Question #2:** SOC-03 shows valid active state code or SOC-09 integrity warning — **no** silent normalization of invalid active (SRDY-02, VP-04) |
| **S-GUAR-03** | **Question #3:** SOC-04 composes blocking summary — open gate/handoff/halt/eligibility — may be «none» if eligible (SRDY-04) |
| **S-GUAR-04** | **Question #4:** SOC-05 exposes completed states/gates/handoffs with stale/superseded markers **visible** (SRDY-05, VP-02) |
| **S-GUAR-05** | **Question #5:** SOC-06 derives remaining segments/gates/artefacts to declared endpoint — **not** invented micro-states (SRDY-06) |
| **S-GUAR-06** | **Question #6:** SOC-07 shows declaration recency tail from POC-06/07/10 or explicit «no declarations yet» — **not** fabricated from session notes alone (SRDY-07, REC-02) |
| **S-GUAR-07** | **Question #7:** SOC-08 exposes next eligibility or blocked-with-cause — **derived**, enables declare decision without executing transition (SRDY-08, OA-01) |
| **S-GUAR-08** | **Cross-cutting:** Read composition presents **no** second live gate/handoff authoritative store — POC-04/05 remain sole live index (SRDY-09, INT-S05) |

### Guarantees to operator path (Playbook 03)

| Guarantee ID | Operator may rely on |
|--------------|---------------------|
| **S-GUAR-09** | One discoverable SOC-01 per Factory Project — archaeology-free entry to eight-question session (IS-01, C5) |
| **S-GUAR-10** | Playbook 03 session is **read-only** with respect to POC-03…07 — Surface **never** grants declaration write path (SE-03, TRK-REL-01) |
| **S-GUAR-11** | SRDY-* assessment remains **human** ritual — SOC-* **enable** observability, **do not replace** Playbook 03 authority (SRB-01) |
| **S-GUAR-12** | Blocked project may be surface-ready — SOC-04 **shows** blockers without requiring gate-complete (OA-03) |
| **S-GUAR-13** | Form factor agnostic — any permitted FF-01 medium exposes SOC-01…08 without full monorepo search |

### Guarantees from upstream (Surface may assume — not re-guarantee)

| Upstream | Surface consumes |
|----------|------------------|
| **RT-G04 G12-01…G12-08** | POC-03…07, POC-10 readable; no write path; POC-D1 optional |
| **RT-G10 M-G12-01…M-G12-10** | MOC-01 entry; MOC-02…08 operational slice; no live gate index in manifest |
| **RT-G05 R-G12-01…R-G12-10** | Optional ROC-01 select; ROC-08 non-authoritative; portfolio depth forbidden |

### Cross-standard guarantee principles

| Principle | Meaning |
|-----------|---------|
| **GUAR-S01** | RT-G12 **composes** read views; RT-G04 **hosts** POC records; RT-G10/05 **populate** binding facets — **must not** create parallel tracking SoT in read layer (SOWN-01) |
| **GUAR-S02** | Physical guarantees are **class-level and composition-level** — not format-specific or UI-specific |
| **GUAR-S03** | Surface guarantees **observability access** — **not** execution, **not** automated transition, **not** gate evaluation |

---

## Integrity Model

Minimum Surface read binding integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Physical artifact expectation |
|----|----------|------------------------------|
| **INT-S01** | **Read-only honesty** | SOC-* composition **must not** mutate POC-03…POC-07 on read — TRK-REL-01 |
| **INT-S02** | **Single read SoT** | Exactly **one** SOC-01 per Factory Project — no competing read convergence points |
| **INT-S03** | **Last-declared reflection** | SOC-03…08 **reflect** most recent Playbook 04 truth — freshness = declaration chain, not filesystem mtime (VP-03, AUTH-S02) |
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

RT-G12 physical Surface artifacts **must never become** the following — inherited from Surface Charter, implementation standard, RT-G04/RT-G10/RT-G05 separation, MVP exclusions.

### Forbidden system roles (no surface physical artifact class)

| Surface must not become | Guard |
|-------------------------|-------|
| **Dashboard platform / operator SaaS / widget product** | TX-07, SC-07, FF-02 |
| **Tracking composition engine / tracking storage** | TS-01; Stage 3 owns composition — RT-G12 **reads** indexes |
| **Persistence substrate product** | RT-G04 owns locus — substrate design **not RT-G12** |
| **Manifest / Passport / minimum understanding store** | MT-01, MAP-06; RT-G10 separate |
| **Registry / portfolio catalog product** | RE-01, RA-05; RT-G05 separate — SOC-10 select only |
| **Database / query engine / analytics platform** | No portfolio KPI rollups, cross-project analytics |
| **Workflow engine / state machine executor** | MAP-04; RT-G01 — SOC-08 **enables** declare, **does not** transition |
| **Factory runtime product** | SC-01; RT-G09 — «Surface drives execution» **rejected** |
| **Gate Results System / gate evaluator** | GV-02, MAP-10 — Surface **shows** outcomes, **does not evaluate** |
| **Project management system** | Tasks, sprints, assignments — **out of scope** |
| **Session workflow engine / automated supervision** | Playbook 03 human ritual — no CI/agent session open/close |
| **Declaration write path** | Playbook 04, DA-01 — read binding **≠** declaration channel |
| **Automation / agent index mutation on read** | OA-ACT-04, SC-03 |
| **Notification / webhook hub** | RT-G13 — post-MVP |
| **Closure registry / terminal workflow engine** | Playbook 05 — POC-08 primary owner |
| **Control plane / orchestrator** | RT-G09, RT-G03 — read binding **observes**, **does not command** |
| **Operator Display Charter substitute** | OQ-TS05 — future artifact must map SOC-*, SRDY-* |
| **CRM / client relationship system** | No contact/deal pipeline on Surface |
| **Runtime object / execution state** | MAP-12 analog — no automated transitions |

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
| Site Type Registry entries | Foundation `registry/` |

### Forbidden physical anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| RT-G12 conflated with «shipped Factory runtime» or «dashboard MVP» | C5 ≠ RT-G09; TX-07; FF-02 |
| UI layout/wireframe design smuggled into **this** specification | Task forbidden list; FF-01 agnostic |
| Surface read duplicates live Manifest gate index | MT-01, SRDY-09, INT-S05 |
| Registry card answers eight questions | RE-01, RA-05, SOC-RULE-03 |
| Read binding **before** substrate indexes + MOC-01 stable | SC-02, SOWN-05 |
| Surface read replaces Playbook 04 declaration path | DA-01, TRK-REL-01 |
| `COMPLETE` / deploy conflated with Surface «completion» | LV-03, MAP-13 |
| RUNTIME-GAPS «dashboard» line interpreted as UX program mandate | OQ-TS09 — impl = read binding |
| Single read artefact swallowing manifest + tracking + surface | SOC-RULE-02; POC-RULE-02 |
| Auto-sync read composition mutating POC-* on refresh | INT-S01, OQ-TS07 bounded |
| SOC-O1 / POC-O1 treated as SRDY-07 authority | SOC-RULE-04, REC-02 |

**Principle BP-S-SPEC-01:** RT-G12 is **per-project Surface read binding** — **one plane**, **one project**, **eight questions**, **read-only** — not a platform.

**Principle BP-S-SPEC-02:** Physical read binding **extends operability** of observability doctrine — **does not transfer** declaration authority to read channel or display layer (AUTH-01).

---

## Readiness Model

### SRDY doctrinal readiness vs physical read bind completeness

| Concept | Physical specification rule |
|---------|----------------------------|
| **Surface-ready** | Operator can answer eight questions from SOC-* composition — **target** for read bind fidelity |
| **Surface-ready ⊇ manifest-ready** | MOC-01 reachable **precedes** meaningful SOC depth — TS-02 |
| **Surface-ready ⊄ gate-complete** | Blocked project may be surface-ready (OA-03) — SOC-04 **shows** blockers |
| **Surface-ready ≈ fully trackable** | Typical co-occurrence (TC-* + SRDY-*) — RT-G12 **reads** indexes, **does not** define TC-* |
| **Physical read bind ⊄ surface-ready retroactively** | Indexes may exist before SOC-01 — bind **enables** archaeology-free consumption |
| **Read bind ⊄ SRDY authority** | Playbook 03 **owns** human SRDY assessment — SOC-* **enable**, **do not replace** |

### SRDY → physical class mapping

| ID | Doctrinal criterion (Surface Charter) | Physical class obligation |
|----|----------------------------------------|---------------------------|
| **SRDY-01** | Tier S-A classes present or explicitly empty-allowed | SOC-02…SOC-08 **must** surface each S-A class or explicit empty-allowed signal |
| **SRDY-02** | Valid active state (or invalid flagged) | SOC-03 **must** show active code or SOC-09 integrity warning |
| **SRDY-03** | Declared endpoint explicit | SOC-02/SOC-06 **must** expose endpoint from MOC-04 / lifecycle bind |
| **SRDY-04** | Blocking summary derivable | SOC-04 **must** compose eligibility + open gate/handoff/halt |
| **SRDY-05** | Completion picture derivable for reached prefix | SOC-05 **must** expose completed states/gates/handoffs with stale markers |
| **SRDY-06** | Remaining picture derivable to endpoint | SOC-06 **must** derive remaining — **not** invent micro-states |
| **SRDY-07** | Recent event window non-empty or «no declarations yet» explicit | SOC-07 **must** show tail from POC-06/07/10 or explicit none |
| **SRDY-08** | Forward picture derivable | SOC-08 **must** expose next eligibility or blocked-with-cause |
| **SRDY-09** | No Surface/Manifest/Tracking duplication violation | Read composition **must not** present second live gate/handoff SoT |

### Recency binding (OQ-PD05 — inherited)

| Rule ID | Physical specification rule |
|---------|----------------------------|
| **REC-01** | SOC-07 **must** read recency from POC-06 declaration tail, POC-07 progression events, and/or POC-10 audit marker |
| **REC-02** | SOC-O1 and POC-O1 session notes **must not** satisfy SRDY-07 alone |
| **REC-03** | Recent event window depth — **bounded default:** logical tail sufficient for Playbook 03; exact N **operator convention** |
| **REC-04** | «Since last session» filter — **non-authoritative** only; authoritative recency = declaration chain |

### When RT-G12 Physical Artifact Specification is **complete**

This deliverable is **specification-complete** when:

| Criterion | Status |
|-----------|--------|
| Surface artifact classes defined (SOC-01…SOC-11, SOC-D1, SOC-O1) | **Yes** |
| Class responsibilities formalized | **Yes** |
| Authority model (authoritative / referenced / optional / prohibited) with precedence | **Yes** |
| Relationship model (RT-G04, Manifest, Registry, Tracking, Playbooks; REL-S*) | **Yes** |
| Physical obligations for valid Surface-capable Factory Project stated | **Yes** |
| Physical guarantees (eight-question doctrine) without UI/serialization | **Yes** |
| Minimum integrity expectations stated (no validators) | **Yes** |
| Boundary protection at specification layer | **Yes** |
| No artifacts, folders, serialization, or layout created | **Yes** |

### What specification-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| Physical SOC-* records **exist** in repo | Specification defines model; creation = separate authorized track |
| Serialization format **chosen** | Explicitly out of scope |
| Read binding form factor **decided** | FF-01 permits multiple — operator choice |
| MVP **demonstrated** on pilot (S4) | Post-physical read bind + Playbook 03 |
| `workspaces/website-factory-operations/` **exists on disk** | **SAFE UNKNOWN** until operator creates |

### Specification-complete vs physical creation

```text
  RT-G12 Surface Read Binding Implementation Standard v1 ── COMPLETE
           │
           ▼
  RT-G04 Physical Artifact Specification v1 ── COMPLETE
           │
           ▼
  RT-G10 Physical Artifact Specification v1 ── COMPLETE
           │
           ▼
  RT-G05 Physical Artifact Specification v1 ── COMPLETE
           │
           ▼
  RT-G12 Physical Artifact Specification v1 ── THIS (specification-complete)
           │
           ▼
  Physical artefact creation (SOC-01…08 read bind on pilot) ── ONLY when separately authorized
```

### MVP surface read bind readiness checklist (operator, post-specification)

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

## Era Closure Assessment

### Physical Artifact Specification Era status

| Track | Specification | Status |
|-------|---------------|--------|
| **RT-G04** Persistence Substrate | RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md | **COMPLETE** |
| **RT-G10** Manifest Binding | RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md | **COMPLETE** |
| **RT-G05** Registry Catalog | RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md | **COMPLETE** |
| **RT-G12** Tracking Surface | RT-G12-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md | **COMPLETE** (this deliverable) |

**Verdict:** Completion of **RT-G12 Physical Artifact Specification v1** **closes** the **Physical Artifact Specification Era** for Website Factory MVP Wave 1. All four authorized physical artifact specification tracks (RT-G04 → RT-G10 → RT-G05 → RT-G12) now have **specification-complete** deliverables defining normative class reality for POC, MOC, ROC, and SOC planes **without** serialization format, folder layout, or disk creation.

### What era closure **does** mean

| Implication | Meaning |
|-------------|---------|
| **Normative physical model complete** | Operator knows **what** physical artifact classes exist, **what** is authoritative/referenced/optional/prohibited, and **how** planes relate — for all four MVP implementation standards |
| **Wave 1 class inventory fully specified** | Physical MVP Definition Review inventory (POC/MOC/ROC/SOC) now has **per-standard physical specifications** — not only implementation standards |
| **Authorized next era** | **Physical MVP Artifact Creation** (or serialization/layout specification if separately authorized) — **not** automatic on era closure |
| **Sequencing preserved** | Substrate → manifest → registry → surface read bind creation order from Physical MVP Definition Review **remains binding** |

### What era closure **does not** mean

| Not implied | Reason |
|-------------|--------|
| Physical files **exist** on disk | Era defines specification; creation = separate authorization |
| Serialization format **chosen** | Explicitly deferred across all four specifications |
| Folder trees / naming conventions **designed** | Out of scope for Physical Artifact Specification Era |
| MVP **demonstrated** on pilot | Success S1–S9 post-physical creation |
| Implementation Standards Era **reopened** | RT-G04/10/05/12 implementation standards remain COMPLETE and authoritative |
| Operator Display Charter **exists** | OQ-TS05 deferred — future track; must map SOC-*, SRDY-* |

### Remaining mandatory specification gaps (post-era)

| Gap | Disposition | Blocks physical creation? |
|-----|-------------|---------------------------|
| **Serialization format** (JSON/YAML/markdown/other) | Future specification track or operator convention — **not** part of Physical Artifact Specification Era | **No** — operator may choose under FF-01 for read bind; substrate serialization similarly deferred |
| **Internal layout** (per-project home structure, portfolio facet structure) | Future specification track or operator convention | **No** — class separation normative; co-location permitted |
| **Operator Display Charter** (OQ-TS05) | Future charter — render rules map to SOC-*, SRDY-* | **No** — FF-01 form-factor agnostic sufficient for MVP |
| **DF-08…DF-10** (pilot pointer policy, git policy) | Operational cross-charter | **No** |
| **OQ-TS01, OQ-TS03, OQ-TS06, OQ-TS08** | Deferred in RT-G12 implementation standard | **No** — bounded defaults suffice |

**Principle ERA-SPEC-01:** Physical Artifact Specification Era **authorized four specifications** — RT-G04, RT-G10, RT-G05, RT-G12. **No fifth MVP-plane physical specification** is required for Wave 1 closure.

**Principle ERA-SPEC-02:** Era closure **enables** operator acknowledgment of complete physical class model — **does not authorize** immediate disk writes under `workspaces/website-factory-operations/` without separate creation authorization.

### Era transition diagram

```text
  Implementation Standards Era ── COMPLETE (RT-G04 → RT-G10 → RT-G05 → RT-G12)
           │
           ▼
  Physical MVP Artifact Definition Review ── COMPLETE
           │
           ▼
  Physical Artifact Specification Era ── COMPLETE (this deliverable closes era)
     RT-G04 spec ── RT-G10 spec ── RT-G05 spec ── RT-G12 spec
           │
           ▼
  [Next authorized era] Physical MVP Artifact Creation
     OR Serialization/Layout Specification (if separately chartered)
           │
           ▼
  Pilot demonstration (S1–S9) on Core 5 case
```

---

## Explicit Non-Claims

This document and the RT-G12 physical Surface artifact model it defines:

- **are not** physical artefact creation, folder creation, file creation, or disk writes;
- **are not** serialization format specification (JSON/YAML/markdown/SQLite/other);
- **are not** naming conventions, folder trees, field lists, schemas, or database structures;
- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **UI design**, **dashboard design**, **screen layout**, **wireframe**, **widget system**, **navigation design**, or **operator product**;
- **are not** **tracking engine**, **tracking storage**, **state store**, or **recorder product**;
- **are not** **Manifest** (RT-G10) or **Registry** (RT-G05) redesign;
- **are not** **Persistence Substrate** (RT-G04) redesign — only **consumption** relationship;
- **are not** **Tracking Surface Charter** or **Tracking Model** rewrite — doctrine taken as authoritative input;
- **are not** Playbooks 01–05 rewrite;
- **are not** **implementation code**, **agents**, **validators**, or **CI binding**;
- **do not** define screens, panels, CLI commands, markdown templates, database tables, or read file paths;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** claim physical Surface read artefacts or operator dashboard **exist** in-repo — **specification only**;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound Surface read path;
- **do not** claim Physical Artifact Specification **automatically** authorizes physical creation — **separate operator authorization** required;
- **do not** claim era closure **automatically** starts physical creation on disk.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01. Surface read binding remains **read-oriented only** per TRK-REL-01.

Tracking Surface remains **Read Visibility Layer** — **not** Dashboard, Analytics Platform, Workflow Engine, Project Manager, Control Center, or Runtime Object.

### Resolved in upstream standards (inherited, not reopened)

| ID | Resolution |
|----|------------|
| **DF-07** | FF-01…FF-05 — form-factor agnostic minimum read binding; dashboard product forbidden |
| **OQ-PD05** | REC-01…REC-04 — SOC-07 binds to POC-06/07/10; session notes non-authoritative |
| **OQ-TS07** | INT-S08, anti-pattern table — authoritative auto-sync **forbidden** |
| **OQ-TS09** | BP section — impl = minimum read binding, not UX program |
| **OQ-R03** | VIEW-01…VIEW-02 — default discoverable; extended view read-bind policy |

### Deferred (not blockers for this specification or era closure)

| ID | Disposition |
|----|-------------|
| **OQ-TS01** | Exact recent event window N — operator convention + Playbook 03 |
| **OQ-TS02** | Whether MOC-X1 holds Surface S-A subset — default read from POC-* per TZ-01 |
| **OQ-TS03** | PHASE_SLICE — one SOC-01 per shell vs slice — Engine v2 or case policy |
| **OQ-TS05** | Separate Operator Display Charter — future; must map SOC-*, SRDY-* |
| **OQ-TS06** | `PASS_WITH_WARNINGS` actionable class on read binding — gate composition |
| **OQ-TS08** | MIG correlation as Surface event class — RT-G08 |
| **OQ-TSW02** | «Since last session» filter semantics — REC-04 non-authoritative |
| **Serialization format** | Future specification track — **not** Physical Artifact Specification Era |
| **DF-08…DF-10** | Pilot pointer policy, git policy — operational cross-charter |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G12 Physical Artifact Specification v1** as **RT-G12 specification-complete** — fourth and **final** Physical Artifact Specification in authorized MVP sequence; **Physical Artifact Specification Era CLOSED**.
2. **Preserve sequencing for creation:** RT-G04 zone + manifest bind + registry catalog (optional) + Playbook 04 indexes **before** meaningful C5/S4 demonstration via SOC-* read bind.
3. **Authorize next era explicitly:** Physical MVP Artifact Creation on pilot — **or** Serialization/Layout Specification if operator prefers format-first — **separate authorization**; era closure **does not** auto-start creation.
4. **Do not create yet:** dashboard mockups, FACTORY-DASHBOARD-v1.md, FACTORY-UI-SPEC-v1.md, tracking storage schemas, Surface-as-write-channel prototypes, registry-as-Surface-depth prototypes, physical files under `workspaces/website-factory-operations/` — **unless separately authorized**.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — RT-G04 specification records authorized zone; Physical MVP Definition Review verified **not present** at definition time |
| Whether any SOC-* read binding artefacts **exist** in-repo | **UNKNOWN** — specification authorizes; creation not part of deliverable |
| Which DF-07 form factor operator will choose for pilot | **not decided** — FF-01 permits multiple |
| Triumph / pilot workspaces as read-bind targets vs external-only refs | **UNKNOWN** — DF-08 per case |
| Calendar for Physical MVP Artifact Creation era | **not scheduled** — awaits operator authorization post-era-closure |
| Operators updated NEXT-PRIORITIES to post–Physical Artifact Specification Era | **UNKNOWN** |

---

*RT-G12 Physical Artifact Specification v1 — fourth and final Website Factory Physical Artifact Specification. Canonical location: `workspaces/website-factory-reference-v1/RT-G12-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G12 Physical Artifact Specification v1

**Stage:** Physical Artifact Specification Era — RT-G12 Physical Artifact Specification (fourth and final Physical Artifact Specification; **era closure**)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G12-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G12-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md` (created)  
**Summary:** Четвёртая и завершающая Physical Artifact Specification Website Factory: полная физическая модель Tracking Surface read binding — одиннадцать authoritative SOC classes (SOC-01…SOC-11) плюс SOC-D1/SOC-O1, authority model (authoritative/referenced/optional/prohibited) с precedence AUTH-S01…S08, relationship model (REL-S01…REL-S28) к RT-G04/Manifest/Registry/Tracking/Playbooks, physical obligations для valid Surface-capable Factory Project (C5/S4), physical guarantees S-GUAR-01…13 по eight-question doctrine без UI/serialization, integrity model INT-S01…S11, boundary protection (Read Visibility Layer ≠ dashboard/tracker/workflow/PM/analytics/control plane/runtime), readiness model (SRDY-* → physical classes), Era Closure Assessment — **Physical Artifact Specification Era COMPLETE** — без создания артефактов, folders, serialization format и layout.  
**Git:** no commit, no push (per task).
