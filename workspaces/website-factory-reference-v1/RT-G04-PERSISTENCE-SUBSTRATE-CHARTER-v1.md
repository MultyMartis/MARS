# REPORT — RT-G04 Persistence Substrate Charter v1

**Версия:** v1  
**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Planning — **RT-G04 charter only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Planning Review **COMPLETE**  
**Тип:** charter only — **без** storage design, file design, schema design, folder layout, implementation plan, runtime plan, UI plan  
**Upstream:** [RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md), [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md)  
**Связь:** [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) ES-04, [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) MAP-01, [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) RAP-01, [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) TS-01, [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G04

**Owner decisions (fixed):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |

---

## Purpose

### Зачем существует RT-G04 Persistence Substrate

**RT-G04 Persistence Substrate** — архитектурная **роль единого авторизованного физического носителя** Factory Project records внутри MARS monorepo. Substrate закрывает capability **C2** (MVP Definition Review) и устраняет **physical binding gap** между doctrine-complete human-operated Factory и operator path, который сегодня зависит от ad-hoc scatter и workspace archaeology.

| Проблема | Как Substrate решает |
|----------|---------------------|
| Нет **одного** authorized locus для Factory Project records (TR-01) | Substrate = единый physical layer, который operator читает и **вручную** обновляет |
| Manifest, Registry и Surface существуют **только** как doctrine | Substrate **принимает** bound records, **не** переопределяя charter roles |
| Playbook 04 declarations логически существуют, но **не переживают** сессию стабильно | Substrate **должен** принимать operator-controlled writes к Engine indexes |
| Playbook 05 closure не имеет stable bound target | Substrate **должен** принимать Factory-terminal metadata |
| Dual corpus и client workspaces создают SoT confusion | Substrate **отделяет** Factory SoT records от narrative docs и external pointers (bounded zone DF-03) |

Substrate — **implementation-plane prerequisite** для физической привязки Manifest (RT-G10 impl), Registry (RT-G05 impl) и read path Tracking Surface (RT-G12 impl) — **без** переопределения Engine ownership rules.

### Нормативная формулировка роли

**RT-G04 Persistence Substrate** — архитектурная **роль физического носителя** Factory-scoped project instance records и bound post-Engine plane artefacts, **вне** Engine documentation boundary (ES-04), **внутри** TOPOLOGY-B-v1 constraints (MARS monorepo, structured file-backed records, single operator, no HomeGateway dependency).

Substrate **сам по себе ничего не сериализует** — он **обеспечивает locus**, на котором RT-G10/05/12 implementation charters **могут** разместить authorized bindings.

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
| Layer artefact production, deploy, hosting | External / post-Factory |

**Substrate — charter (конституция роли носителя), не продукт хранения, не Factory runtime и не application.**

---

## Foundation Dependencies

Persistence Substrate Charter **наследует** завершённый Engine v1, post-Engine charters, Operational Design и MVP topology decision; **не изменяет** Foundation, Runtime или Engine Stages 1–6.

### Tier 0 — Decision and review chain

| Document | Substrate использует |
|----------|---------------------|
| [RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-PLANNING-REVIEW-v1.md) | Planning boundary, reality classification, P1–P8 obligations |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1, DF-01/02/03/06, SC-* guards |
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C2–C7 capability floor, MVP success S2–S7 |
| [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md) | RT-G04 first in dependency graph |

### Tier 1 — Operational doctrine

| Document | Substrate использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | Human-operated v1; single operator; OA-ACT-04 |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — manifest enrollment; file **не** блокирует ritual |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — catalog enrollment declared |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — eight questions session |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — DA-01 operator sole declarer |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — terminal outcomes persistable |

### Tier 2 — Post-Engine charters (ownership rules Substrate must not violate)

| Charter | Document | Constraint on Substrate |
|---------|----------|------------------------|
| Manifest (RT-G10 doctrine) | [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Manifest **≠** storage (MAP-01); Substrate **hosts**, Manifest **defines** |
| Registry (RT-G05 doctrine) | [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Registry **≠** database (RAP-01); catalog **≠** tracking depth (RA-05) |
| Tracking Surface (RT-G12 doctrine) | [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Surface **≠** UI **≠** storage (TS-01); read-only semantics |

### Tier 3 — Engine boundary (hard limits)

| Document | Constraint |
|----------|------------|
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04 — persistence **external** to Engine |
| Engine Stages 1–6 | Logical models authoritative; Substrate **persists**, не переопределяет |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking owns composition; «RT-G04 may persist» instance records |

**Authority precedence:** Foundation Freeze + Engine Readiness Audit → Engine Stages 1–6 → Manifest / Registry / Surface charters → **этот charter** для роли Persistence Substrate → **будущие** RT-G10/05/12 implementation charters **не могут** нарушить MAP-01, RAP-01, TS-01, ES-04, OA-ACT-04.

---

## Ownership Model

### Что RT-G04 **владеет**

Substrate владеет **физическим носителем** следующих **классов** Factory-scoped records — категории doctrine, **не** поля или форматы:

| Ownership class | Content (doctrine) | Playbook / anchor |
|-----------------|-------------------|-------------------|
| **Persistent bindings** | Stable per-project record home; manifest binding carrier; registry catalog binding | P1–P3; C2–C4 |
| **Persistent declarations** | Append-only declaration records; progression ledger events; reconciliation acts | Playbook 04 DA-01; TV-02 |
| **Persistent indexes** | Engine instance indexes: state active + history; gate outcome index; handoff event index; artefact ref index | Tracking Model; C5–C6 |
| **Persistent identity shell** | Factory Project logical identity binding to physical locus | Playbook 01; Object Model |
| **Persistent audit markers** | Last declaration recency (logical); session outcome refs feeding SRDY-07 | Playbook 03–04; Tier S-A |
| **Persistent closure metadata** | Factory-terminal / partial / suspended outcomes | Playbook 05; C7 |
| **Persistent charter-bound categories** | Scope tier, declared endpoint, applicability mask when declared | Manifest Categories 2–4 |
| **External ref discipline** | Pointers to external workspaces and layer bodies — **refs only** | ER-06, TV-01; P8 |

**Ownership rule PS-01:** если потеря записи **ломает** operator ability to answer Playbook 03/04/05 или eight Surface questions **without workspace archaeology** — класс **persistent** и входит в RT-G04 responsibility scope.

### Что RT-G04 **не владеет**

| Non-ownership | Actual owner |
|---------------|--------------|
| Manifest **doctrine**, MRDY-* rules | Manifest Charter |
| Registry **doctrine**, RRDY-* rules | Registry Charter |
| Surface **visibility contract**, SRDY-* rules | Tracking Surface Charter |
| Gate/handoff **criteria** and Runtime **vocabulary** | Runtime Architecture + Foundation |
| Layer artefact **bodies** | T1 Foundation layers |
| Per-project **serialization standard** | RT-G10 implementation charter |
| Portfolio **catalog index shape** | RT-G05 implementation charter |
| Operator **display** semantics | RT-G12 implementation charter |
| Site Type Registry entries | Foundation `registry/` — RAP-11 |

### Principle PS-02 — Substrate hosts, charters own roles

RT-G04 **хранит bindings** между logical Factory truth и physical locus. Charters **определяют ownership rules** для Manifest, Registry и Surface — Substrate **must not** merge planes или подменять charter authority.

### Principle PS-03 — Human-only write authority for declarations

Operator-controlled write path (Playbook 04, OA-ACT-04) — **единственный** authoritative mutator Engine indexes на substrate. External systems **never** mutating indexes without operator act (SC-03).

### Planning obligations (must survive — P1–P8)

Substrate charter **обязывает** обеспечить persistence следующих **classes** для at least one Core 5 pilot through full Playbooks 01→05:

| # | Obligation | MVP anchor |
|---|------------|------------|
| P1 | Per-project physical locus discoverable as canonical Factory record home | C2, TR-01 |
| P2 | Manifest binding carrier — entry anchor + MRDY-* when physically bound | C3 |
| P3 | Registry catalog carrier — portfolio listing with Manifest pointer + RRDY-* | C4 |
| P4 | Tracking instance records — state, gates, handoffs, artefact refs | C5, C6 |
| P5 | Declaration writes — Playbook 04 outcomes in persisted indexes | C6, S5 |
| P6 | Closure records — Playbook 05 terminal metadata | C7, S6 |
| P7 | Append-only honesty — no silent overwrite of declared history | TV-02, AT-* |
| P8 | External ref discipline — bodies remain external | ER-06 |

**May persist (optional at MVP):** pre-declaration session notes; derived eligibility caches; registry card template fields (OQ-R02); git policy variants (DF-10).

**Must never persist as Substrate responsibility:** layer bodies; gate criteria text; Runtime vocabulary canon; automated transition logs as authority; Site Type Registry; queue rank; deploy/hosting state.

---

## Reality Model

RT-G04 planning и charter **классифицируют** информацию по четырём reality classes. Термины — planning-level; **не** schema labels.

### Persistent reality (must survive)

Информация, которую Factory **обязана** сохранять между operator sessions:

| Class | Examples |
|-------|----------|
| Factory Project identity shell | Stable logical identity, Factory-scoped recognition |
| Manifest minimum understanding | MRDY-* categories when manifest-enrolled |
| Registry catalog binding | Portfolio entry, discoverability status, distinction summaries, Manifest pointer |
| Engine instance indexes | State, gates, handoffs, artefact refs |
| Operator declarations | Append-only records, progression ledger, reconciliation |
| Audit / recency markers | Last declaration recency; session outcome refs |
| Closure metadata | Factory-terminal outcomes per Playbook 05 |
| Charter-bound stable categories | Scope tier, declared endpoint, applicability mask |

### Derived reality (may be reconstructed)

Информация, которую substrate **может** хранить для convenience, но которую **можно восстановить** из persistent records + Runtime vocabulary **без** новой operator declaration:

| Class | Examples | Reconstruction source |
|-------|----------|----------------------|
| Eligibility snapshot | Open blocking set, forward eligibility | Gate index + active state |
| Blocking / completion / remaining pictures | Surface questions #3–#5, #8 | Indexes + Lifecycle derivation |
| Active lifecycle segment label | LC-* display | Active state + Runtime binding map |
| Composite gate rollup status | Generation Ready display | Constituent RG PASS refs |
| Registry orientation summary | High-level state label on catalog card | Tracking read — RA-05 limits depth |
| Surface-ready checks | SRDY-* pass/fail as derived views | Composition rules over persistent indexes |

**Planning rule DR-01:** RT-G04 **must not** treat derived caches as **authoritative** if they contradict last declared truth (TV-02). Derived material **must be** regeneratable from persistent declaration records.

### Reference reality (must not become persistence bodies)

Информация, на которую Factory **ссылается**, но которую RT-G04 **не владеет** и **не должен** поглощать:

| Class | Examples | Actual owner |
|-------|----------|--------------|
| Foundation layer bodies | Legal templates, blueprints, block defs | T1 Foundation |
| Runtime definitions | State codes, RG-*/HO-* definitions | Runtime Architecture v1 |
| Handoff package payloads | PAGE_BUILD_SPEC, FRONTEND_HANDOFF_PACKAGE | Generation Outputs |
| Layer artefact content | SEO packs, content signals | Layer workstreams |
| External workspaces | Client `workspaces/*`, pilot snapshots | External — ERA-W03 refs only |
| Global registers | NEXT-PRIORITIES, Site Type Registry | T5 / Foundation |
| Non-canonical ops | Agent chat, MIG transcripts, CI logs | External unless charter-bound ref |

**Planning rule RR-01:** RT-G04 **indexes and points** — **never** substitutes T1/T2 authority or becomes second Legal Pack / Runtime doc store.

### Operational reality (transient; not persistence core)

| Class | Examples | Disposition |
|-------|----------|-------------|
| Pre-declaration assessment | Playbook 03 session notes before Playbook 04 act | May persist optionally; **not** authoritative until declared |
| Evidence bundles | Reviewer notes, layer outputs pre-declaration | Support declaration; **not** gate index |
| Trigger signals | Client brief, incoming request | Pre-Factory until recognition |
| UI/session ephemera | Scroll position, filter state | Out of scope |
| In-flight edits | Uncommitted operator draft | Not declared truth |

**Planning rule OR-01:** operational reality **must not** mutate Engine indexes without Playbook 04 operator act (OA-ACT-04, SC-03).

### Classification diagram

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

## Manifest Relationship

RT-G04 **enables** RT-G10; RT-G10 **uses** RT-G04; Manifest Charter **neither is nor owns** storage (MAP-01).

### Substrate support obligations (capability, not format)

| Obligation | Doctrine anchor | RT-G04 role |
|------------|-----------------|-------------|
| Stable per-project record home for manifest binding | MR-01, MRDY-06, C3 | Substrate provides locus; RT-G10 defines serialization |
| Persistence of MRDY-* categories when MVP binds physically | Manifest Charter §Manifest-ready | Carrier for categories — **not** category definitions |
| Reference topology pointers (Category 7) | MRDY-05, MAP-05 | Store refs to tracking indexes and external sources |
| Separation from live gate index | MT-01, MAP-01 | Substrate **must not** encourage Manifest-as-second-tracking-store |
| Precedence: manifest before registry | MR-01, RA-04, Playbook 01→02 | Substrate **must allow** manifest binding **without** registry entry |
| Enrollment without blocking on file | Playbook 01 | Doctrinal manifest-enrolled **precedes** physical file |

### Substrate forbidden actions for Manifest

| Forbidden | Reason |
|-----------|--------|
| Define manifest **serialization standard** | RT-G10 implementation charter |
| Own Manifest **doctrine** or MRDY-* rules | Manifest Charter |
| Store **live** gate/handoff composition as Manifest content | MT-01 |
| Auto-create manifest on folder/git discovery | RAP-10, RD-04 |
| Merge Manifest with Passport / second SoT | MA-03, BV-03 |

### Principle MR-REL-01 — Substrate precedes serialization, follows enrollment

Logical manifest-enrolled Factory Project **precedes** physical bind. RT-G04 **follows** enrollment doctrine; RT-G10 **defines** how enrollment materializes on substrate.

---

## Registry Relationship

RT-G04 **supports** Registry catalog binding **without** becoming Registry or catalog doctrine.

### Substrate support obligations

| Obligation | Doctrine anchor | RT-G04 role |
|------------|-----------------|-------------|
| Portfolio catalog physical carrier | C4, RRDY-*, Playbook 02 | Substrate holds catalog binding — RT-G05 impl defines index shape |
| Pointer to Manifest entry per project | RA-04, MR-02, RAP-16 | Stable link manifest anchor ↔ registry slot |
| Distinction summaries at catalog level only | RRDY-04, RA-05 | Persist summary categories — **not** seven/eight tracking questions |
| Discoverability status categories | RRDY-05, RD-* | Registered / withdrawn / archived — catalog status, not Runtime state |
| Logical identity ≠ registry entry ID | ES-03, RA-03 | Substrate **must allow** both identifiers without conflation |
| Declared enrollment — no auto-scan | RAP-10, RD-04 | Writes are operator acts |

### Substrate forbidden actions for Registry

| Forbidden | Reason |
|-----------|--------|
| Substitute Tracking depth on catalog card | RA-05, SC-05 |
| Act as dashboard / Surface | RAP-05 → RT-G12 |
| Define Site Type Registry content | RAP-11 |
| Implement queue or prioritization | RT-G06 |
| Create Factory Project **logical identity** | RA-02 — identity precedes catalog slot |

### Dependency edge

```text
  RT-G04 substrate
       │
       ▶ per-project manifest anchor (RT-G10 on substrate)
       │
       ▶ portfolio catalog (RT-G05 on substrate; depends on manifest pointer)
```

**Principle REG-REL-01:** Registry implementation **must not** precede stable manifest anchor on shared substrate.

---

## Tracking Relationship

RT-G04 **supports persistence** of Engine tracking instance records and **read feeding** Surface — **without** owning Tracking composition rules or RT-G12 display.

### Substrate support obligations

| Obligation | Tracking / Surface anchor | RT-G04 role |
|------------|---------------------------|-------------|
| State instance + history persistence | «RT-G04 may persist» | Authoritative declared state records |
| Gate outcome index persistence | Tracking owns index | Store outcomes — **not** criteria |
| Handoff event index + package refs | Tracking owns events | Store events/refs — **not** payloads |
| Artefact ref index per project | AV-* / Tracking | Refs only |
| Progression ledger / audit trail | AT-*, Playbook 04 | Append-only declaration history |
| Playbook 04 write path | C6, DA-01 | Operator-controlled updates to indexes |
| Surface read feed | SRDY-*, eight questions | Substrate **supplies data**; RT-G12 **renders** |
| Recency class (SRDY-07) | Tier S-A last declaration marker | Persistent declaration tail or explicit «none yet» |

### Substrate forbidden actions for Tracking

| Forbidden | Reason |
|-----------|--------|
| Redefine tracking zones, tiers, composition | Stage 3 Engine doc |
| Become Tracking Surface or dashboard | TS-01; RT-G12 |
| Evaluate gates or authorize transitions | Engine + Playbook 04 human acts only |
| Store Tier C excluded material | Tracking Model Tier C |
| Auto-sync from CI/MIG/agents | OA-ACT-04, SC-03 |

### RT-G10 overlap (planning clarity)

Tracking Model states RT-G10 **may serialize** tracking zones (ES-04). Charter boundary:

- **RT-G04** = **where** instance records live physically.
- **RT-G10** = **which manifest-related serialization** applies to which categories/zones.
- **Conflict guard:** serialization choices **must not** violate MT-01 / MAP-05.

**Principle TRK-REL-01:** RT-G12 **never** writes authoritative indexes — read-oriented only (Surface charter).

---

## Boundary Protection

RT-G04 **must never become** следующие системы — ни по TOPOLOGY-B-v1, ни по MVP exclusions, ни по Engine boundary.

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

### Architectural anti-patterns Substrate must resist

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
| Backup/DR product | May inherit git discipline — not a Factory subsystem charter |
| Permission / RBAC model | Single-operator MVP; OR-* |
| Notification / webhook hub | RT-G13 |
| Rollback automation executor | RT-G15 |
| Legal template store | T1 Legal Pack |
| Execution log product | RT-G07 post-MVP |

### Principle BP-01 — Structured persistence ≠ Factory runtime

TOPOLOGY-B-v1 **creates** physical layer external to Engine. Substrate charter **must preserve** human-only write authority for declaration path (C6) and read-only Surface semantics (C5) — tooling helpers **may** exist later but **never** replace operator declarer.

---

## Authorized Zone

### Factory Records Zone (DF-03 — resolved)

**Authorized Factory Records Zone** в MARS monorepo:

```text
workspaces/website-factory-operations/
```

| Constraint | Statement |
|------------|-----------|
| **Placement** | Factory SoT records **live in** authorized zone — **not** scattered ad-hoc across monorepo |
| **Bounded scope** | Zone **не** поглощает весь MARS repo; `registry/`, Lane A `src/`, unrelated programs остаются **outside** Factory SoT |
| **Doctrine vs records** | `workspaces/website-factory-reference-v1/` остаётся **canonical doctrine + Engine**; operational pack `projects/mars-website-factory/` **не** supersede v1 canon without explicit routing |
| **External workspaces** | Client pilots (`workspaces/triumph-*` и др.) — **external pointers** (ER-06), not Factory SoT by default |
| **Structure inside zone** | **NOT DEFINED** in this charter — no folder tree, no file naming, no layout |

### Zone discipline principles

| ID | Principle |
|----|-----------|
| **AZ-01** | Substrate locus **must** be discoverable by operator as canonical Factory record home (P1, TR-01) |
| **AZ-02** | Zone separation **must** prevent conflation of Factory SoT with narrative doctrine docs |
| **AZ-03** | Zone **must not** require HomeGateway, database, or standalone application (DF-06, TOPOLOGY-B-v1) |
| **AZ-04** | Physical zone existence **does not** imply implementation started — charter authorizes **role**, not artefacts |

---

## Readiness Model

### When RT-G04 charter is **complete**

RT-G04 Persistence Substrate Charter v1 считается **charter-complete** когда:

| Criterion | Status in this deliverable |
|-----------|---------------------------|
| Purpose defined — physical binding gap / C2 / TR-01 | **Yes** |
| Ownership model — persistent bindings, declarations, indexes | **Yes** |
| Reality model — persistent / derived / reference / operational | **Yes** |
| Manifest / Registry / Tracking relationships separated from RT-G10/05/12 | **Yes** |
| Boundary protection — forbidden roles explicit | **Yes** |
| Authorized zone recorded (DF-03) | **Yes** — `workspaces/website-factory-operations/` |
| Explicit non-claims — no format, folders, runtime | **Yes** |
| Owner constraints integrated — DF-01, DF-02, DF-06 | **Yes** |

### What charter-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| RT-G04 **implementation** started or complete | Implementation — separate authorized track |
| Physical files or folders **created** | Explicitly forbidden in charter scope |
| Serialization format **selected** | RT-G10/05/12 implementation planning charters |
| DF-04…DF-10 **fully resolved** | Remain workshop inputs for implementation planning |
| MVP **demonstrated** on pilot case | Success criteria S1–S9 — post-implementation |

### Charter-complete vs implementation-ready

```text
  RT-G04 Planning Review v1 ── COMPLETE
           │
           ▼
  RT-G04 Persistence Substrate Charter v1 ── THIS (charter-complete)
           │
           ▼
  RT-G10 Manifest Implementation Planning Charter ── NEXT authorized track
           │
           ├──▶ RT-G05 Registry Implementation Planning Charter
           │
           └──▶ RT-G12 Surface Read Binding Implementation Planning Charter
```

**Principle RDY-01:** Loss of RT-G04 charter clarity **must not** block Engine docs — Engine already COMPLETE without storage.

---

## Future Relationship Model

### How RT-G10, RT-G05 and RT-G12 **consume** RT-G04

Без implementation design — **roles and dependency edges only**:

| Gap | Role | Depends on RT-G04 | RT-G04 depends on |
|-----|------|-------------------|-------------------|
| **RT-G04** | Physical substrate — authorized locus for Factory Project records | — | TOPOLOGY-B-v1; Engine external placement; DF-03 zone |
| **RT-G10 impl** | Per-project **serialization standard** for Manifest binding (+ optional tracking zones) | **Yes** — needs substrate locus | Engine + Manifest Charter |
| **RT-G05 impl** | Portfolio **catalog implementation** | **Yes** — catalog on substrate | RT-G10 anchor + Registry Charter |
| **RT-G12 impl** | Operator **read surface** for eight visibility questions | **Yes** — reads substrate-backed data | RT-G10 (+ optional RT-G05 portfolio drill-down) + Tracking/Surface doctrine |

### Layer diagram (doctrine)

```text
                    ┌─────────────────────────┐
                    │   ENGINE (logical)      │
                    │   Stages 1–6 docs       │
                    └───────────┬─────────────┘
                                │ declares ownership;
                                │ does not store
                                ▼
                    ┌─────────────────────────┐
                    │   RT-G04 SUBSTRATE      │  ◀── THIS CHARTER
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

### Separation principles (future consumers)

| ID | Principle |
|----|-----------|
| **B-01** | RT-G04 **precedes** RT-G10/05/12 impl planning authorization in MVP sequence — substrate first |
| **B-02** | RT-G04 **does not** define what RT-G10 serializes — only **hosts** authorized bindings |
| **B-03** | RT-G05 **never** stores per-project tracking depth — catalog only (RA-05) |
| **B-04** | RT-G12 **never** writes authoritative indexes — read-oriented (Surface charter) |
| **B-05** | Charters (RT-G10/05/12 doctrine) **remain** authoritative for roles; substrate **must not** merge planes |
| **B-06** | RT-G07 execution logs **may use** same substrate post-MVP — separate charter |

### Playbook consumption path

Future implementation **must preserve** operator path Playbooks 01→02→03↔04→05:

```text
  Playbook 01  Manifest enrollment     ──▶  substrate accepts manifest binding (RT-G10)
  Playbook 02  Registry enrollment     ──▶  substrate accepts catalog binding (RT-G05)
  Playbook 03  Surface session         ──▶  substrate supplies read feed (RT-G12 reads)
  Playbook 04  Project declaration     ──▶  substrate accepts operator index writes
  Playbook 05  Project closure         ──▶  substrate accepts closure metadata
```

---

## Explicit Non-Claims

This document and the RT-G04 Persistence Substrate role it defines:

- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **storage product**, **database**, **ORM**, or **multi-tenant** persistence service;
- **are not** **application**, **standalone service**, **SaaS**, or **HomeGateway** integration;
- **are not** **automation layer**, **agent orchestration**, **queue**, or **validator engine**;
- **are not** **operator UI**, **dashboard**, or **CLI** (RT-G12);
- **are not** **Manifest** (RT-G10 doctrine), **Registry** (RT-G05 doctrine), or **Tracking Surface** (RT-G12 doctrine);
- **are not** **serialization standard** for manifest, registry, or tracking records;
- **are not** **implementation**, **physical MVP folders**, or **sample artefacts**;
- **do not** define JSON/YAML/SQLite schemas, field lists, folder structures, database tables, or file paths **inside** authorized zone;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** modify Manifest, Registry, or Tracking Surface charters;
- **do not** claim physical substrate artefacts **exist** in repo — **charter only**;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound planes.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01.

---

## Open Questions

Charter **bounds** questions for **future** implementation planning — **does not answer** storage, format, or layout.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-M04 / DF-04** | Manifest vs tracking record **co-location** policy | **OPEN** — RT-G10 implementation planning |
| **OQ-M01** | Which Tracking zones **may** serialize via RT-G10 on same substrate | **OPEN** — RT-G10 implementation planning |
| **OQ-ME05** | Physical bind moment vs doctrinal Enrolled | **OPEN** — RT-G10 implementation planning |
| **OQ-R01 / DF-05** | Registry central catalog artefact vs distributed pointers + aggregator | **OPEN** — RT-G05 implementation planning |
| **OQ-R02** | Registry card field template | **OPEN** — near-MVP; not doctrine blocker |
| **OQ-PD05 / DF-** | Declaration/session record binding for SRDY-07 | **OPEN** — RT-G10/12 implementation planning |
| **DF-07** | RT-G12 read surface form factor | **OPEN** — must respect TX-07 (no dashboard product) |
| **DF-08** | Pilot workspace pointer policy | **OPEN** — operational |
| **DF-09** | Network/hosting beyond local git | **OPEN** — low for MVP |
| **DF-10** | Git versioning policy for SoT records | **OPEN** — audit vs privacy tradeoff |
| **OQ-OM06** | v0↔v1 routing discipline for dual corpus | **OPEN** — hygiene |

**Resolved by owner decision (not open in charter scope):** DF-01 (MARS monorepo), DF-02 (structured artifacts), DF-03 (`workspaces/website-factory-operations/`), DF-06 (no HomeGateway).

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G04 Persistence Substrate Charter v1** as **RT-G04 role definition complete** — gap RT-G04 in RUNTIME-GAPS remains **NOT STARTED** for **implementation**, not for doctrine.
2. **Authorize next track:** **RT-G10 Manifest Implementation Planning Charter** — serialization standard and bind rules on substrate; **still not** physical files or schemas in planning charter unless separately authorized.
3. **Preserve sequencing:** RT-G10 → RT-G05 → RT-G12 implementation planning charters — **after** RT-G04 charter, **before** any physical MVP artefact creation.
4. **Do not create yet:** folder trees under `workspaces/website-factory-operations/`, JSON/YAML samples, manifest/registry/tracking physical files, database design, runtime, UI, automation.
5. **Optional P3:** Update RUNTIME-GAPS RT-G04 line to «CHARTERED (doctrine)» — **operator action**, outside this deliverable.

**Engine Architecture v1 requires no further architecture stages.** Persistence Substrate charter is **post-Engine, post-MVP-topology, post-planning-review** documentation.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` path **exists** on disk today | **UNKNOWN** — charter records authorized zone; physical creation not part of this deliverable |
| Calendar for RT-G10/05/12 implementation planning charters | **not scheduled** |
| Triumph / client workspaces in substrate refs vs external-only | **UNKNOWN** — charter per case (DF-08) |
| Operators updated NEXT-PRIORITIES to RT-G04 charter-complete era | **UNKNOWN** |

---

*RT-G04 Persistence Substrate Charter v1 — RT-G04 doctrine complete. Architecture charter only. Canonical location: `workspaces/website-factory-reference-v1/RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G04 Persistence Substrate Charter v1

**Stage:** RT-G04 — Persistence Substrate Charter (post–MVP Topology Decision, post–Planning Review)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md` (created)  
**Summary:** Определена доктрина RT-G04 Persistence Substrate как единого авторизованного физического носителя Factory Project records в MARS monorepo: purpose (physical binding gap / C2), ownership (persistent bindings, declarations, indexes), reality model (persistent / derived / reference / operational), relationships to RT-G10/05/12 без serialization design, boundary protection, authorized zone `workspaces/website-factory-operations/` (DF-03), readiness and future consumption model — без storage, schemas, folders, runtime, UI, implementation.  
**Git:** no commit, no push (per task).
