# REPORT — RT-G04 Persistence Substrate Planning Review v1

**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Тип:** planning review only — **без** storage design, file design, schema design, folder layout, implementation plan, runtime plan  
**Метод:** синтез принятых артефактов (MVP Definition Review, Implementation Planning Review, MVP Topology Decision, Manifest/Registry/Tracking Surface charters, Operational Model, Playbooks 01–05, Engine System Boundary, Tracking Model) в **границу планирования** RT-G04  
**Принятая реальность (контекст задачи):** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04/05/10/12 implementation **NOT STARTED**; shipped Factory runtime **отсутствует**

**Upstream chain:** [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) → **этот review** → RT-G04 charter authorization (future)

---

## Executive Summary

**Вердикт:** RT-G04 Persistence Substrate — **не** продукт хранения и **не** Factory runtime. RT-G04 — **единый авторизованный физический носитель** Factory Project records внутри MARS monorepo (TOPOLOGY-B-v1), который закрывает capability **C2** и делает возможной физическую привязку Manifest (RT-G10 impl), Registry (RT-G05 impl) и read path Tracking Surface (RT-G12 impl) — **без** переопределения Engine ownership rules.

**Проблема, которую RT-G04 решает:** Factory **уже работает** documentation-first; operator ведёт Playbooks 01–05 без канонического physical locus. RT-G04 устраняет **ad-hoc scatter** и **workspace archaeology** как единственный способ сохранить manifest enrollment, portfolio catalog, Engine indexes и closure metadata между сессиями.

**Проблемы, которые RT-G04 не решает:** исполнение переходов, оценка gates, orchestration, UI semantics, формат сериализации manifest, doctrine Manifest/Registry/Surface, производство layer bodies, deploy, automation.

**Planning boundary (кратко):**

| RT-G04 **есть** | RT-G04 **не есть** |
|-----------------|---------------------|
| Единый physical layer для Factory Project records (C2) | Serialization standard per-project manifest (RT-G10) |
| Носитель operator-declared persistence (Playbook 04 writes, Playbook 05 closure) | Portfolio catalog doctrine (RT-G05 charter) |
| Substrate для bound Manifest + Registry + Tracking indexes | Operator read surface (RT-G12 impl) |
| Pointer/ref discipline к external workspaces и layer bodies | Layer artefact bodies, gate criteria, Runtime definitions |
| Human/assisted write path; git-auditable locus in MARS | Workflow engine, automation, queue, multi-tenant DB |

**Readiness:** граница планирования RT-G04 **понятна**; charter authorization — **следующий** deliverable после разрешения **DF-03** (Factory records zone в MARS).

**Рекомендация:** авторизовать **RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1** (role, boundaries, non-goals) — **не** implementation design.

---

## RT-G04 Purpose

### Зачем существует Persistence Substrate

RT-G04 закрывает **physical binding gap** между:

- **Сегодня:** doctrine-complete human-operated Factory; logical Engine indexes и charter categories **исполнимы** без bytes on disk.
- **MVP:** operator **не зависит** от implicit discipline, разрозненных markdown notes и поиска по workspace для manifest entry, portfolio discoverability, declaration honesty и Surface visibility (C2–C7).

Persistence Substrate — **implementation-plane prerequisite** для всех physical bindings в MVP dependency graph:

```text
  RT-G04 (substrate)
       │
       ├──▶ RT-G10 impl (manifest serialize)
       │         │
       │         ├──▶ RT-G05 impl (registry catalog)
       │         │
       │         └──▶ RT-G12 impl (surface read)
       │
       └──▶ declaration/session + closure record binding (Playbooks 03–05)
```

### Какую проблему решает

| Проблема | Роль RT-G04 |
|----------|-------------|
| Нет **одного** authorized locus для Factory Project records (TR-01) | Substrate = единый physical layer operator читает и **вручную** обновляет |
| Manifest/Registry/Surface остаются **только** doctrine | Substrate **принимает** bound records, не переопределяя charter roles |
| Playbook 04 declarations существуют логически, но не **переживают** сессию стабильно | Substrate **должен** принимать operator-controlled writes к Engine indexes |
| Playbook 05 closure не имеет stable bound target | Substrate **должен** принимать Factory-terminal metadata |
| Dual corpus и client workspaces создают SoT confusion | Substrate **должен** отделять Factory SoT records от narrative docs и external pointers (bounded zone — DF-03) |

### Что RT-G04 **не** решает

| Не решает | Владелец / gap |
|-----------|----------------|
| «Что такое Manifest» doctrinally | Manifest Charter (RT-G10 doctrine) |
| «Как сериализовать» manifest binding | RT-G10 **implementation** charter |
| Portfolio catalog doctrine | Registry Charter (RT-G05 doctrine) |
| Eight visibility questions semantics | Tracking Surface Charter (RT-G12 doctrine) |
| Как operator **видит** bound data | RT-G12 **implementation** |
| State/gate/handoff **definitions** | Runtime Architecture + Foundation |
| Movement **execution** | Nobody in v1; RT-G01 FUTURE |
| Automated index mutation | RT-G03 forbidden in MVP |
| Gate pass/fail **evaluation** | RT-G11 FUTURE; human Playbook 04 only |

### Нормативная формулировка роли (planning-level)

**RT-G04 Persistence Substrate** — архитектурная **роль физического носителя** Factory-scoped project instance records и bound post-Engine plane artefacts, **вне** Engine documentation boundary (ES-04, Engine System Boundary §External System Principles), **внутри** TOPOLOGY-B-v1 constraints (MARS monorepo, structured file-backed records, single operator).

Substrate **serializes nothing by itself** — он **обеспечивает locus**, на котором RT-G10/05/12 implementation charters **могут** разместить authorized bindings.

---

## Reality Classification

Классификация — **только** по принятой doctrine (Engine, Tracking Model, charters, Operational Model, Playbooks). Термины planning-level; **не** schema labels.

### Persistent reality (must survive)

Информация, которую Factory **обязана** сохранять между operator sessions, чтобы human-operated path оставался честным и MVP success criteria (S2–S7) достижимы:

| Class | Content (doctrine) | Authority source |
|-------|-------------------|------------------|
| **Factory Project identity shell** | Stable logical identity, Factory-scoped recognition | Object Model; Playbook 01 |
| **Manifest minimum understanding** | MRDY-* categories when manifest-enrolled (entry anchor identification included) | Manifest Charter; Playbook 01 |
| **Registry catalog binding** | Portfolio entry, discoverability status, distinction summaries, pointer to Manifest entry | Registry Charter RRDY-*; Playbook 02 |
| **Engine instance indexes** | State active + history; gate outcome index; handoff event index; artefact ref index | Tracking Model §Tracking Boundaries — «RT-G04 may persist» |
| **Operator declarations** | Append-only declaration records, progression ledger events, reconciliation acts | Playbook 04 DA-01; Tracking TV-02 |
| **Audit / recency markers** | Last declaration recency (logical); session outcome refs feeding SRDY-07 | Playbook 03–04; Surface Charter Tier S-A |
| **Closure metadata** | Factory-terminal / partial / suspended outcomes per Playbook 05 | Lifecycle Composition; Playbook 05 |
| **Charter-bound stable categories** | Scope tier, declared endpoint, applicability mask when declared | Manifest Categories 2–4; Engine |

**Planning rule:** если потеря записи **ломает** operator ability to answer Playbook 03/04/05 или eight Surface questions **without workspace archaeology** — класс **persistent** и входит в RT-G04 responsibility scope.

### Derived reality (may be reconstructed)

Информация, которую substrate **может** хранить для convenience, но которую **можно восстановить** из persistent records + Runtime vocabulary **без** новой operator declaration:

| Class | Examples | Reconstruction source |
|-------|----------|----------------------|
| **Eligibility snapshot** | Open blocking set, forward eligibility summary | Gate index + active state + TR map |
| **Blocking / completion / remaining pictures** | Surface questions #3–#5, #8 | Indexes + Lifecycle derivation rules |
| **Active lifecycle segment label** | LC-* display | Active state + Runtime binding map |
| **Composite gate rollup status** | Generation Ready display | Constituent RG PASS refs |
| **Registry orientation summary** | High-level state label on catalog card (category only) | Tracking read — RA-05 limits depth |
| **Surface-ready checks** | SRDY-* pass/fail as **derived views** | Composition rules over persistent indexes |

**Planning rule:** RT-G04 **must not** treat derived caches as **authoritative** if they contradict last declared truth (TV-02). Derived material **must be** regeneratable from persistent declaration records.

### Reference reality (must not become persistence bodies)

Информация, на которую Factory **ссылается**, но которую RT-G04 **не владеет** и **не должен** поглощать:

| Class | Examples | Actual owner |
|-------|----------|--------------|
| **Foundation layer bodies** | Legal templates, blueprints, block defs, site type matrices | T1 Foundation layers |
| **Runtime definitions** | State codes, RG-*/HO-* definitions, TR/FT rules | Runtime Architecture v1 |
| **Handoff package payloads** | PAGE_BUILD_SPEC, FRONTEND_HANDOFF_PACKAGE contents | Generation Outputs / layers |
| **Layer artefact content** | SEO packs, content signals, design mappings | Layer workstreams |
| **External workspaces** | Client `workspaces/*`, pilot snapshots, Lane A `src/` | External — ERA-W03 refs only |
| **Global registers** | NEXT-PRIORITIES ACCEPTED/FROZEN, Site Type Registry | T5 / Foundation `registry/` |
| **Non-canonical ops** | Agent chat, MIG transcripts, CI logs, tickets | External unless charter-bound ref |

**Planning rule:** RT-G04 **indexes and points** — **never** substitutes T1/T2 authority or becomes second Legal Pack / Runtime doc store.

### Operational reality (transient; not persistence core)

Информация **операционного момента**, не обязанная становиться Factory SoT:

| Class | Examples | Disposition |
|-------|----------|-------------|
| **Pre-declaration assessment** | Playbook 03 session notes before Playbook 04 act | May persist optionally (near-MVP); **not** authoritative until declared |
| **Evidence bundles** | Reviewer notes, layer run outputs pre-declaration | Support declaration; **not** gate index |
| **Trigger signals** | Client brief, incoming request | Pre-Factory until recognition |
| **UI/session ephemera** | Scroll position, filter state | Out of scope |
| **In-flight edits** | Uncommitted operator draft | Not declared truth |

**Planning rule:** operational reality **must not** mutate Engine indexes without Playbook 04 operator act (OA-ACT-04, SC-03).

### Classification summary

```text
  REFERENCE (T1/T2/external)     OPERATIONAL (transient)
         │                              │
         │ pointers only                │ pre-declaration
         ▼                              ▼
  ┌──────────────────────────────────────────────────┐
  │           RT-G04 PERSISTENCE SUBSTRATE            │
  │   PERSISTENT: declarations · indexes · bindings   │
  │   DERIVED (optional cache): eligibility · SRDY views │
  └──────────────────────────────────────────────────┘
         ▲
         │ reads for display — does not define storage
  ┌──────┴──────┐
  │ RT-G12 impl │
  └─────────────┘
```

---

## Persistence Responsibilities

### Must survive (RT-G04 planning obligation)

Substrate planning **must** ensure the following **classes** can persist for at least one Core 5 pilot through full Playbooks 01→05:

| # | Responsibility class | MVP anchor | Playbook |
|---|---------------------|------------|----------|
| P1 | **Per-project physical locus** exists and is discoverable by operator as canonical Factory record home | C2, TR-01 | 01+ |
| P2 | **Manifest binding carrier** — entry anchor + MRDY-* categories when physically bound | C3 | 01 |
| P3 | **Registry catalog carrier** — portfolio listing with Manifest pointer + RRDY-* distinction categories | C4 | 02 |
| P4 | **Tracking instance records** — state, gates, handoffs, artefact refs per Tracking Model ownership table | C5, C6 | 03–04 |
| P5 | **Declaration writes** — operator Playbook 04 outcomes reflected in persisted indexes | C6, S5 | 04 |
| P6 | **Closure records** — Playbook 05 terminal metadata bound to existing project records | C7, S6 | 05 |
| P7 | **Append-only honesty** — stale markers, superseded events remain visible; no silent overwrite of declared history | TV-02, AT-* | 04 |
| P8 | **External ref discipline** — workspace/layer pointers stored; bodies remain external | ER-06, TV-01 | all |

### May persist (optional at MVP; not blocking planning boundary)

| Class | Notes |
|-------|-------|
| Declaration/session record **before** formal RT-G10 bind | Supports SRDY-07; operable manually pre-impl |
| Derived eligibility/cache material | Performance convenience only |
| Registry card template fields (OQ-R02) | Reduces ambiguity; not doctrine blocker |
| Git policy variants (DF-10) | Audit vs local-only — owner workshop |

### Must never persist as RT-G04 responsibility

| Class | Why excluded |
|-------|--------------|
| Layer artefact **bodies** | T1 authority |
| Gate/handoff **criteria** text | Definitions ≠ observation |
| Runtime **vocabulary** canon | Already in Runtime Architecture docs |
| Automated transition logs as **authority** | RT-G07 post-MVP; must not replace declarations |
| Site Type Registry entries | RAP-11 — different Registry |
| Multi-project **queue rank** | RT-G06 |
| Deploy/hosting state | Post-Factory |

### Reconstruction allowance

Substrate planning **should** assume RT-G12 read path **may** reconstruct Tier S-A/B Surface classes from persistent indexes **without** requiring duplicate live gate/handoff index (MAP-05, MT-01, SRDY-09).

---

## Manifest Implications

RT-G04 planning **must** support Manifest **physical binding** without becoming Manifest or RT-G10.

### What RT-G04 must support (capability, not format)

| Support obligation | Doctrine anchor | RT-G04 role |
|--------------------|-----------------|-------------|
| **Stable per-project record home** for manifest binding | MR-01, MRDY-06, C3 | Substrate provides locus; RT-G10 defines serialization |
| **Persistence of MRDY-* categories** when MVP binds physically | Manifest Charter §Manifest-ready | Carrier for categories — **not** category definitions |
| **Reference topology pointers** (Category 7) — where truths live | MRDY-05, MAP-05 | Store refs to tracking indexes and external sources — **not** duplicate indexes |
| **Separation from live gate index** | MT-01, MAP-01 | Substrate **must not** encourage Manifest-as-second-tracking-store |
| **Precedence: manifest before registry** | MR-01, RA-04, Playbook 01→02 | Substrate **must allow** manifest binding **without** registry entry |
| **Enrollment without blocking on file** | Playbook 01 | Doctrinal manifest-enrolled **precedes** physical file; substrate **follows** enrollment |

### What RT-G04 must not do for Manifest

| Forbidden | Reason |
|-----------|--------|
| Define manifest **serialization standard** | RT-G10 implementation charter |
| Own Manifest **doctrine** or MRDY-* rules | Manifest Charter |
| Store **live** gate/handoff composition as Manifest content | MT-01 |
| Auto-create manifest on folder/git discovery | RAP-10, RD-04 |
| Merge Manifest with Passport / second SoT | MA-03, BV-03 |

### Open planning questions (for charter workshop — not answered here)

| ID | Question |
|----|----------|
| OQ-M04 / DF-04 | Manifest vs tracking record **co-location** policy |
| OQ-M01 | Which Tracking zones **may** serialize via RT-G10 on same substrate |
| OQ-ME05 | Physical bind moment vs doctrinal Enrolled |

**Boundary statement:** RT-G04 **enables** RT-G10; RT-G10 **uses** RT-G04; Manifest Charter **neither is nor owns** storage (MAP-01).

---

## Registry Implications

RT-G04 planning **must** support Registry **catalog binding** without becoming Registry or catalog doctrine.

### What RT-G04 must support

| Support obligation | Doctrine anchor | RT-G04 role |
|--------------------|-----------------|-------------|
| **Portfolio catalog physical carrier** | C4, RRDY-*, Playbook 02 | Substrate holds catalog binding — RT-G05 impl defines index shape |
| **Pointer to Manifest entry** per project | RA-04, MR-02, RAP-16 | Stable link manifest anchor ↔ registry slot |
| **Distinction summaries** at catalog level only | RRDY-04, RA-05 | Persist summary categories — **not** seven/eight tracking questions |
| **Discoverability status** categories | RRDY-05, RD-* | Registered / withdrawn / archived — catalog status, not Runtime state |
| **Logical identity ≠ registry entry ID** | ES-03, RA-03 | Substrate **must allow** both identifiers without conflation |
| **Declared enrollment** — no auto-scan | RAP-10, RD-04 | Writes are operator acts — **not** filesystem discovery |

### What RT-G04 must not do for Registry

| Forbidden | Reason |
|-----------|--------|
| Substitute Tracking depth on catalog card | RA-05, SC-05 |
| Act as dashboard / Surface | RAP-05 → RT-G12 |
| Define Site Type Registry content | RAP-11 |
| Implement queue or prioritization | RT-G06 |
| Create Factory Project **logical identity** | RA-02 — identity precedes catalog slot |

### Dependency edge (planning)

```text
  RT-G04 substrate
       │
       ▶ per-project manifest anchor (RT-G10 on substrate)
       │
       ▶ portfolio catalog (RT-G05 on substrate; depends on manifest pointer)
```

Registry implementation **must not** precede stable manifest anchor on shared substrate (Implementation Planning Review order).

---

## Tracking Implications

RT-G04 planning **must** support **persistence of Engine tracking instance records** and **read feeding** Surface — without owning Tracking composition rules or RT-G12 display.

### What RT-G04 must support

| Support obligation | Tracking Model / Surface anchor | RT-G04 role |
|--------------------|--------------------------------|-------------|
| **State instance + history** persistence | «RT-G04 may persist» | Authoritative declared state records |
| **Gate outcome index** persistence | Tracking owns index | Store outcomes — **not** criteria |
| **Handoff event index + package refs** | Tracking owns events | Store events/refs — **not** payloads |
| **Artefact ref index** per project | AV-* / Tracking | Refs only |
| **Progression ledger / audit trail** | AT-*, Playbook 04 | Append-only declaration history |
| **Playbook 04 write path** | C6, DA-01 | Operator-controlled updates to indexes |
| **Surface read feed** | SRDY-*, eight questions | Substrate **supplies data**; RT-G12 **renders** |
| **Recency class (SRDY-07)** | Tier S-A last declaration marker | Persistent declaration tail or explicit «none yet» |

### What RT-G04 must not do for Tracking

| Forbidden | Reason |
|-----------|--------|
| Redefine tracking zones, tiers, composition | Stage 3 Engine doc |
| Become Tracking Surface or dashboard | TS-01; RT-G12 |
| Evaluate gates or authorize transitions | Engine + Playbook 04 human acts only |
| Store Tier C excluded material | Tracking Model Tier C |
| Auto-sync from CI/MIG/agents | OA-ACT-04, SC-03 |

### RT-G10 overlap (planning clarity)

Tracking Model states RT-G10 **may serialize** tracking zones (ES-04, OQ-S4-11). Planning boundary:

- **RT-G04** = **where** instance records live physically.
- **RT-G10** = **which manifest-related serialization** applies to which categories/zones.
- **Conflict guard:** serialization choices **must not** violate MT-01 / MAP-05.

---

## Non-Responsibilities

RT-G04 **must never become** the following — ни по TOPOLOGY-B-v1, ни по MVP exclusions, ни по Engine boundary:

### Core forbidden roles

| Forbidden system | Why |
|------------------|-----|
| **Database / multi-tenant storage product** | MVP sufficient with file-backed single-operator model (TX-06, DF-02) |
| **Workflow engine / state machine executor** | RT-G01; transitions declared not executed |
| **Factory runtime product** | RT-G09 impl; SC-01 |
| **Automation layer** (CI/n8n/index mutation) | RT-G03; SC-03 |
| **Application / standalone service / SaaS** | Topology E rejected; TX-05 |
| **Operator UI / dashboard product** | RT-G12; Surface charter ≠ UI |
| **Agent orchestration platform** | RT-G02 |
| **Queue / scheduler** | RT-G06, RT-G14 |
| **Validator / gate authority engine** | RT-G11 |
| **Manifest / Registry / Surface doctrine owner** | Charters already COMPLETE |
| **Project serialization standard** | RT-G10 impl — separate charter |
| **Layer generation or frontend build system** | GG-*, Lane A external |
| **HomeGateway host or consumer** | DF-06 none |
| **MIG / external pipeline SoT** | RT-G08 |
| **Site Type Registry** | Foundation T1 — RAP-11 |
| **Discovery crawler** (git folder scan enrollment) | RAP-10, RD-04 |

### Architectural anti-patterns RT-G04 must resist

| Anti-pattern | Guard |
|--------------|-------|
| Substrate conflated with «shipped Factory runtime» | SC-01, explicit non-claims |
| Storage design smuggled into doctrine rewrite | SC-06 |
| Manifest owns live gate index on disk | MT-01, MAP-01 |
| Registry card duplicates Tracking | RA-05 |
| Structured persistence invites automated writes | SC-03, C6 human path |
| Entire MARS repo treated as Factory zone | Topology C rejected; DF-03 bounded zone |
| Passport / unified YAML project schema in Engine path | BV-05, forbidden docs list |

### Additional justified non-responsibilities

| Role | Rationale |
|------|-----------|
| **Backup/DR product** | May inherit git discipline — not a Factory subsystem charter |
| **Permission / RBAC model** | Single-operator MVP; OR-* |
| **Notification / webhook hub** | RT-G13 |
| **Rollback automation executor** | RT-G15 |
| **Legal template store** | T1 Legal Pack |
| **Execution log product** | RT-G07 post-MVP |

---

## Boundary Review

Planning relationships among RT-G04, RT-G10, RT-G05, RT-G12 — **roles only**, no design.

### Relationship matrix

| Gap | Role (planning) | Depends on RT-G04 | RT-G04 depends on |
|-----|-----------------|-------------------|-------------------|
| **RT-G04** | Physical substrate — **authorized locus** for Factory Project records | — | TOPOLOGY-B-v1; Engine external placement |
| **RT-G10 impl** | Per-project **serialization standard** for Manifest binding (+ optional tracking zones) | **Yes** — needs substrate locus | Engine + Manifest Charter |
| **RT-G05 impl** | Portfolio **catalog implementation** | **Yes** — catalog on substrate | RT-G10 anchor + Registry Charter |
| **RT-G12 impl** | Operator **read surface** for eight visibility questions | **Yes** — reads substrate-backed data | RT-G10 (+ optional RT-G05 portfolio drill-down) + Tracking/Surface doctrine |

### Layer diagram (planning)

```text
                    ┌─────────────────────────┐
                    │   ENGINE (logical)      │
                    │   Stages 1–6 docs       │
                    └───────────┬─────────────┘
                                │ declares ownership;
                                │ does not store
                                ▼
                    ┌─────────────────────────┐
                    │   RT-G04 SUBSTRATE      │  ◀── THIS PLANNING REVIEW
                    │   persistence locus     │
                    └───────────┬─────────────┘
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │ RT-G10 impl │      │ RT-G05 impl │      │ (indexes for│
   │ manifest    │      │ registry    │      │  declarations│
   │ serialize   │      │ catalog     │      │  + closure)  │
   └──────┬──────┘      └──────┬──────┘      └──────┬──────┘
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │ read-only consumer
                                ▼
                    ┌─────────────────────────┐
                    │   RT-G12 impl           │
                    │   operator read surface │
                    └─────────────────────────┘
```

### Separation principles

| ID | Principle |
|----|-----------|
| **B-01** | RT-G04 **precedes** RT-G10/05/12 impl planning authorization in MVP sequence — substrate first |
| **B-02** | RT-G04 **does not** define what RT-G10 serializes — only **hosts** authorized bindings |
| **B-03** | RT-G05 **never** stores per-project tracking depth — catalog only (RA-05) |
| **B-04** | RT-G12 **never** writes authoritative indexes — read-oriented (Surface charter) |
| **B-05** | Charters (RT-G10/05/12 doctrine) **remain** authoritative for roles; substrate **must not** merge planes |
| **B-06** | Loss of RT-G04 charter clarity **must not** block Engine docs — Engine already COMPLETE without storage |

### Versus adjacent gaps (context)

| Gap | Relation to RT-G04 |
|-----|-------------------|
| RT-G07 Execution logs | Post-MVP; may **use** same substrate — separate charter |
| RT-G11 Validators | Post-MVP; **must not** write indexes as declarer |
| RT-G01/03 | Forbidden before substrate stable — automation debt risk |

---

## Readiness Review

| Question | Assessment |
|----------|------------|
| Is RT-G04 **purpose** defined at planning level? | **Yes** — physical binding gap / C2 / TR-01 |
| Is **reality classification** bounded? | **Yes** — persistent / derived / reference / operational |
| Are **persistence responsibilities** enumerated without design? | **Yes** — P1–P8 must; optional/must-never listed |
| Are Manifest / Registry / Tracking **implications** separated from RT-G10/05/12? | **Yes** |
| Are **non-responsibilities** explicit? | **Yes** |
| Are **boundaries** vs RT-G10/05/12 clear? | **Yes** |
| Topology owner constraints integrated? | **Yes** — TOPOLOGY-B-v1, DF-01/02/06 resolved |
| RT-G04 implementation started? | **No** — correctly NOT STARTED |
| RT-G04 **planning boundary** understood? | **Yes** |
| RT-G04 **charter authorization** ready immediately? | **Partial** — requires **DF-03** placement resolution minimum |
| Physical artefacts required for this review? | **No** — none created |

### Readiness verdict

**RT-G04 Persistence Substrate planning boundary — UNDERSTOOD.**

Planning workshop **may close** with:

1. Confirmed role/boundaries/non-goals (this review).
2. DF-03 recommendation for Factory records zone in MARS (still **not** folder design in this doc).
3. Handoff to **RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1** draft for owner authorization.

**Not ready without separate charter:** any serialization format, schema, sample files, MVP folders, RT-G10/05/12 implementation specs.

---

## Final Recommendation

### Primary recommendation

**Authorize next deliverable:** **`RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md`** — implementation **charter** at role/boundaries/non-goals level only, constrained by:

- This planning review
- TOPOLOGY-B-v1 (filesystem + structured artifacts, `C:\AI MARS`, no HG/DB/app)
- MVP Definition C2–C7 and exclusions
- SC-01 / SC-03 / SC-06 checklist from Topology Decision

### Charter must contain (planning expectation — not text here)

| Section | Content type |
|---------|--------------|
| Purpose | Substrate role as in §RT-G04 Purpose |
| Scope | Persistent classes P1–P8; reference pointer discipline |
| Non-goals | §Non-Responsibilities |
| Plane boundaries | Manifest / Registry / Tracking support vs RT-G10/05/12 |
| Owner constraints | DF-01, DF-02, DF-06; DF-03 resolution gate |
| MVP success linkage | S2–S7 evidence classes substrate enables |
| Explicit non-claims | No format, no folders, no runtime |

### Sequencing after charter authorization

```text
  RT-G04 Planning Review v1 (this doc) ── COMPLETE
           │
           ▼
  RT-G04 Persistence Substrate Charter v1 ── NEXT
           │ (requires DF-03 confirm)
           ▼
  RT-G10 Manifest Implementation Planning Charter
           │
           ├──▶ RT-G05 Registry Implementation Planning Charter
           │
           └──▶ RT-G12 Surface Read Binding Implementation Planning Charter
```

### Do not authorize yet

- Physical MVP folder creation
- JSON/YAML/SQLite or field list selection
- RT-G10/05/12 **implementation** (only planning charters after RT-G04 charter)
- RT-G01, RT-G03, RT-G09 impl, automation, queue

### Secondary hygiene (non-blocking)

- Sync NEXT-PRIORITIES: RT-G04 planning era **ACTIVE**
- Resolve OQ-OM06 v0↔v1 routing before agent-assisted binding work

---

## Explicit Non-Claims

This review **does not** claim:

- Any **storage model**, file format, folder layout, schema, YAML, JSON, database design, or sample artefacts **were created**.
- RT-G04 **implementation** is complete, started, or charter-authorized.
- **DF-03** Factory records zone **was selected** — only that it **gates** charter authorization.
- **DF-04…DF-10** **were resolved** — listed as charter workshop inputs.
- A shipped Website Factory **runtime**, workflow engine, persistence **product**, operator UI, or HomeGateway integration **exists** or **was designed**.
- MVP **has been built** or pilot-demonstrated with bound planes.
- Registry enrollment is optional **in MVP mission sense** — Implementation Planning included catalog in MVP scope.
- Triumph/pilot workspaces are deploy-authorized (**SAFE UNKNOWN**).
- Operators updated NEXT-PRIORITIES post-2026-06-05 (**UNKNOWN**).
- Any accepted artefact was modified — **planning deliverable only**.

This review **does** claim (evidence-based):

- RT-G04 is the **persistence substrate role** — unified physical layer for Factory Project records — **not** Manifest, Registry, Surface, or runtime product.
- RT-G04 **must** support persistent operator-declared Engine indexes, manifest/registry bindings, declaration writes, and closure metadata — **without** owning layer bodies or definitions.
- **Derived** Surface views **may** be reconstructed; **reference** and **operational** classes **must not** become substrate authority.
- RT-G04 **precedes** RT-G10 → RT-G05 → RT-G12 in MVP planning sequence; RT-G12 **reads**, RT-G10/05 **serialize/bind**, RT-G04 **hosts**.
- Planning boundary is **understood**; next artifact should be **RT-G04 Persistence Substrate Charter v1** — still **not** implementation design.

---

*RT-G04 Persistence Substrate Planning Review v1 — planning boundary only. Canonical location: `workspaces/website-factory-reference-v1/RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G04 Persistence Substrate Planning Review v1
