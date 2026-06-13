# REPORT — Factory Engine System Boundary v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Factory Engine Architecture v1 — **Stage 6 only**  
**Контекст:** Website Factory Foundation Era **COMPLETE**; Stages 1–5 **ACCEPTED**; Engine Readiness Audit v1 — **PASS WITH WARNINGS**  
**Тип:** architecture only — **без** implementation, runtime product, agents, code, workflows, databases, automation, storage format, manifests, passports  
**Связь:** [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md), [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md), [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md), [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md), [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G09

---

## Purpose

Stages 1–5 ответили на вопросы **внутри** одного Factory Project:

| Stage | Вопрос |
|-------|--------|
| 1 — Object | Что движется? |
| 2 — State | Как это движется? |
| 3 — Tracking | Как это наблюдается? |
| 4 — Gate Composition | Что авторизует движение? |
| 5 — Lifecycle Composition | Как полный lifecycle складывается в один нарратив? |

Stage 6 отвечает: **«Где начинается и где заканчивается Factory Engine?»**

### Зачем существует Engine

**Factory Engine** — documentation-first, methodology-first, human-supervised **координационный слой архитектуры** для **одного** Factory Project. Engine даёт оператору **единую логическую модель** и **правила владения**, по которым можно ответить на семь базовых вопросов — **без** чтения всего workspace и **без** исполнительной инфраструктуры.

| Координационная проблема | Как Engine решает |
|--------------------------|-------------------|
| Истина распределена по Foundation layers, Runtime и layer workstreams | **Composition rules** — Object, State, Tracking, Gates, Lifecycle **собираются** в согласованный operator narrative |
| Оператор не должен археологически искать прогресс по workspace | **Tracking composition** — единая observability surface для **этого** production case |
| State, gates, handoffs и artefacts имеют разных владельцев | **Ownership principles** — кто владеет instance, кто владеет definition, что только ссылается |
| Human-operated v1 — нет автоматического recorder | Engine фиксирует **что оператор объявил видимым** — не подменяет enforcement |
| Риск semantic drift между Runtime и project tracking | Engine **потребляет** Runtime vocabulary read-only — не переопределяет states, `RG-*`, `HO-*` |

### Что Engine **не** решает

| Out of scope | Куда относится |
|--------------|----------------|
| Автоматическая смена state, gate evaluation, handoff delivery | Runtime rules + **FUTURE** automation (RT-G01, RT-G03, RT-G11) |
| Производство layer artefacts (contracts, specs, validation runs) | Foundation layer workstreams |
| Frontend HTML/CSS/JS, deploy, hosting, CI для client site | Post-Factory / external |
| Центральный реестр проектов, очередь, приоритизация | **FUTURE** RT-G05, RT-G06 |
| Persistence, manifest file, dashboard, CLI | **FUTURE** RT-G04, RT-G10, RT-G12 |
| MIG runs, n8n workflows, MetaBOT, ORCA, WPilot execution | External orchestration — **не** Engine |
| Переопределение Foundation contracts, Legal Pack, Registry, `block_id` | Protected documents — **reference only** |

**Engine boundary:** Engine **начинается** там, где Factory Project признан Factory-scoped и требуется **координированное отслеживание** одного production case. Engine **заканчивается** на границе **декларации и наблюдаемости** — до любого runtime, storage, automation или application layer.

```text
                    ┌─────────────────────────────────────────┐
                    │           FACTORY ENGINE (v1)            │
                    │  documentation + methodology + human     │
                    │  coordination for ONE Factory Project    │
                    ├─────────────────────────────────────────┤
                    │  Stage 1  Object                         │
                    │  Stage 2  State                          │
                    │  Stage 3  Tracking                       │
                    │  Stage 4  Gate Composition               │
                    │  Stage 5  Lifecycle Composition          │
                    │  Stage 6  System Boundary (this doc)     │
                    └─────────────────────────────────────────┘
              owns instance / indexes          references only
                     │                                  │
         ┌───────────┴───────────┐          ┌───────────┴───────────┐
         │  PROJECT INSTANCE     │          │  FOUNDATION (T1)      │
         │  data planes          │          │  layer contracts +    │
         │                       │          │  artefact bodies      │
         └───────────┬───────────┘          └───────────────────────┘
                     │ references
         ┌───────────┴───────────┐          ┌───────────────────────┐
         │  RUNTIME (T2)         │          │  EXTERNAL SYSTEMS     │
         │  movement vocabulary  │          │  storage, UI, agents,   │
         │  — no instance store  │          │  queue, MIG, ORCA…    │
         └───────────────────────┘          └───────────────────────┘
```

---

## Foundation Dependencies

Engine **существует только** как composition layer над принятой Foundation + Runtime. Engine **не** заменяет и **не** изменяет frozen/accepted layer contracts.

### Tier 1 — Engine charter inputs (Stages 1–5)

| Document | Engine role |
|----------|-------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Канонический объект; authority tiers T1–T5; mandatory components |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Instance state; progression; rollback; terminal `COMPLETE` |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Observability composition; visibility tiers |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Authorization plane; namespace mapping; sufficiency semantics |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | Full lifecycle narrative; rollback cascade; partial completion |

### Tier 2 — Runtime + production chain (reference only)

| Document | Engine consumes |
|----------|-----------------|
| [runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) | Movement discipline; human-operated v1 model |
| [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) | 14 canonical states — **не** переопределяются |
| [runtime-architecture/STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md) | TR/FT/DR/RB/LR/ER — read-only |
| [runtime-architecture/RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) | `RG-*` definitions |
| [runtime-architecture/RUNTIME-HANDOFFS-v1.md](runtime-architecture/RUNTIME-HANDOFFS-v1.md) | `HO-*` contracts |
| [runtime-architecture/PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) | LC-00…LC-13, LS-*, AP-* |
| [generation-contracts/](generation-contracts/) | Generation scope, outputs, gates |
| [production-qa/](production-qa/) | Production QA gates, Frontend readiness |
| [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md) | Engine ↔ Runtime boundary; ERA-W01…W10 |

### Tier 3 — Remaining Foundation layers (reference only)

Registry → Blueprints → Page Architecture → Block Registry → Page Block Validation → SEO → Design → Content → Content Validation → Legal Pack (+ Legal Entity Discovery when required).

**Authority precedence:** Foundation Freeze + Finalization Pass + Engine Readiness Audit → [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) for global layer status → Engine Stages 1–6 for per-project coordination semantics.

---

## Engine Ownership Principles

Engine **владеет** per-project **instance semantics** и **indexes** — не class-level Foundation authority.

### What Engine owns (one Factory Project)

| Domain | Engine ownership | Source stage |
|--------|------------------|--------------|
| **Project Object** | Identity shell; charter & scope refs; logical composition of mandatory components | Stage 1 |
| **State instance** | Active `runtime_state_code`; state history; progression ledger; eligibility snapshot; scope state mask | Stage 2 |
| **Tracking composition** | Operator single-view rules; visibility tiers; audit trail for Factory declarations | Stage 3 |
| **Gate instance composition** | Gate outcome index; validity (ACTIVE/STALE/INVALID); active gate set derivation; composite rollup refs | Stage 4 |
| **Lifecycle composition** | Active segment narrative; continuity rules; rollback cascade **status** on indexes; partial endpoint metadata | Stage 5 |
| **Handoff events** | HO event records; clearance declarations; package **refs**; ack records; supersession status | Stages 1, 5, 6 |
| **Artefact references** | Pointers to layer outputs per project — **not** bodies | Stage 1, 3 |
| **Scope freeze marker** | `generation_id` boundary visibility from Generation Ready onward | Stage 1 |
| **Parallel legal status refs** | RG-LEGAL / RG-ENTITY visibility refs | Stage 1, 3 |
| **Invalidation markers** | Post-rollback STALE/SUPERSEDED/INVALIDATED **status** on project indexes | Stages 2, 4, 5 |
| **Logical metadata flags** | `FACTORY_TRACK_SUSPENDED`, `FACTORY_TRACK_CLOSED_PARTIAL` — **not** Runtime states | Stage 5 |

### Ownership principles (normative)

| ID | Principle |
|----|-----------|
| **EO-01** | Engine owns **instance**, never **definition** — states, gates, handoffs, layer contracts stay in Runtime / Foundation. |
| **EO-02** | Engine owns **refs and records**, never **artefact bodies** — PAGE-CONTRACT, specs, validation logs, handoff package payloads remain in layer workstreams. |
| **EO-03** | Engine owns **declaration truth** for this project — last operator-declared state, gate PASS, handoff clearance — not automated inference. |
| **EO-04** | Engine owns **composition rules** across five stage models — how planes align at segment boundaries — not an executor. |
| **EO-05** | Engine owns **one project per model** — multi-project registry, queue rank, concurrency are **explicitly external** (RT-G05, RT-G06). |
| **EO-06** | Rollback cascade affects **project indexes only** — Foundation documents and layer artefact bodies are **never** mutated by Engine semantics. |
| **EO-07** | Charter & scope declaration content is **operator-authored**; Engine **indexes** and applies LR-07 mask — does not invent scope. |

### What Engine does **not** own (even though Stages 1–5 describe it)

| Concern | Actual owner |
|---------|--------------|
| Canonical state vocabulary (14 codes) | Runtime Architecture v1 |
| Transition rules TR/FT/DR/RB/LR/ER | Runtime Architecture v1 |
| `RG-*`, `HO-*` definitions and blocked conditions | Runtime Architecture v1 |
| Layer `GATE_*`, validation PASS/FAIL criteria | Respective Foundation layers |
| Gate pass/fail **criteria text**, failure libraries | RUNTIME-GATES + layer docs |
| Handoff **package data** (spec bodies, FRONTEND_HANDOFF_PACKAGE assembly) | Generation Outputs / layer workstreams |
| Frontend implementation state | Frontend workstream — post-Factory |
| Physical persistence format | **NOT DEFINED** — RT-G04, RT-G10 FUTURE |

---

## Engine Reference Principles

Engine **ссылается** на authoritative sources — **не** копирует и **не** сливает authority.

### Reference tiers (inherited from Stage 1)

| Tier | Role | Engine relationship |
|------|------|---------------------|
| **T1 — Layer contracts** | What must be true (semantics, matrices, PASS/FAIL rules) | **Reference only** — link to defining doc |
| **T2 — Runtime movement** | State names, TR rules, `RG-*`, `HO-*` | **Read-only vocabulary** — instance values in Engine indexes |
| **T3 — Layer gate namespaces** | Domain `GATE_*`, validation contracts | **Reference** — mapped to `RG-*` per Stage 4 table |
| **T4 — Project tracking (Engine)** | This project's state, gates, handoffs, refs | **Engine scope** — Stages 1–5 |
| **T5 — Operational status register** | Global ACCEPTED/FROZEN | **Optional context link** — not per-project progress |

### Reference principles (normative)

| ID | Principle |
|----|-----------|
| **ER-01** | **«What must a LANDING blueprint contain?»** → Blueprint layer (T1), not Engine. |
| **ER-02** | **«May any project advance to SEO_READY?»** → Runtime transitions (T2) + gate rules — Engine evaluates **this** instance only. |
| **ER-03** | **«What is this project's current state?»** → Engine T4 using Runtime vocabulary (T2). |
| **ER-04** | **«Is SEO Architecture v2 accepted globally?»** → NEXT-PRIORITIES (T5), not Project. |
| **ER-05** | Tracking single view **points to** sources — **does not become** Legal Pack, Registry, or Runtime doc. |
| **ER-06** | External workspace pointers (`projects/mars-website-factory/` — ERA-W03) — **charter-declared refs only**; not canonical replacements for layer authority. |
| **ER-07** | MIG, ORCA, MetaBOT, WPilot artefacts may appear as **external refs** if charter binds — Engine **does not** own their execution semantics. |

### Domains Engine references but never owns

| Domain | Engine holds | Authoritative owner |
|--------|--------------|---------------------|
| **Runtime Architecture** | State/gate/handoff **vocabulary** consumption | Runtime docs |
| **Foundation layers** | Artefact refs + layer doc links | Each `*-SYSTEM-v1.md` |
| **Legal** | Route mapping refs, Input Sheet status, parallel track visibility | Legal Pack workflow |
| **Blueprints** | `blueprint_ref` binding | Blueprint System |
| **Page Architecture** | PAGE-CONTRACT refs per route | Page Architecture layer |
| **Blocks** | Resolved stack refs | Block Registry |
| **SEO** | Strategy + PAGE-SEO-CONTRACT refs | SEO Architecture v2 |
| **Design** | `VF_*` binding refs | Design System Mapping |
| **Content** | Signal binding refs | Content Contracts |
| **Generation** | `generation_id`, scope freeze ref, output refs | Generation Contracts / Outputs |
| **QA** | Production QA run ref, checklist consumption ref | Production QA layer |
| **Validation** | PASS/FAIL run refs | Page Block + Content Validation |

---

## External System Principles

Следующие системы **остаются вне** Factory Engine Architecture v1. Engine **не** invent integrations с ними.

### Explicitly external

| System class | Examples | Relationship to Engine |
|--------------|----------|------------------------|
| **Runtime product** | Workflow engine, state machine executor, BPMN | **FUTURE** RT-G01 — Engine is **not** this |
| **Storage** | Database, file-backed state store, git-as-SoT for tracking | **FUTURE** RT-G04 — Engine defines **no** format |
| **Project registry** | Central index of all Factory projects | **FUTURE** RT-G05 — Engine scope = **one** project |
| **Queue / scheduler** | Work prioritization, job queues | **FUTURE** RT-G06 |
| **Manifest / passport serialization** | Canonical JSON/YAML project file | **FUTURE** RT-G10 — separate charter |
| **Operator UI / dashboard / CLI** | Visual tracking surface | **FUTURE** RT-G12 — may **display** Engine composition |
| **Automation** | n8n, CI state mutation, webhooks | **FUTURE** RT-G01, RT-G03, RT-G13 |
| **Validator CLI binding** | Automated gate evaluation | **FUTURE** RT-G11 |
| **Agent systems** | MIG orchestration, Cursor agents, MetaBOT workflows | External — Engine **does not** execute agents |
| **ORCA** | Content pack coordination, route-family workflows | External production workstream — refs only if charter binds |
| **WPilot** | **SAFE UNKNOWN** — no integration defined in Engine scope | External until chartered |
| **Frontend layer** | HTML/partials/SCSS/JS, gulp build, client deploy | Post-Factory consumer of handoff package |
| **Hosting / CI / deploy** | Production go-live, Triumph workspace build | External to Factory closure |
| **Enterprise tooling** | Tickets, chat, git history | May link from audit trail — **not** canonical Engine data |

### External system principles (normative)

| ID | Principle |
|----|-----------|
| **ES-01** | External systems **may persist or display** Engine-defined logical entities **only** under separate implementation charter — Engine v1 **does not** specify how. |
| **ES-02** | No external system **redefines** Runtime states, `RG-*`, or layer gate semantics without supersession banner (ERA-W07). |
| **ES-03** | RT-G05 registry entry ≠ Factory Project identity — logical project exists in Engine model; registry is **FUTURE** optional index. |
| **ES-04** | RT-G10 manifest **may serialize** tracking zones (Stage 3) — manifest standard is **not** part of Engine architecture closure. |
| **ES-05** | Deploy authorization, client go-live, Triumph production — **SAFE UNKNOWN** — never conflated with `COMPLETE`. |

```text
  ┌────────────── ENGINE (documentation boundary) ──────────────┐
  │  logical model · ownership · composition · human declaration │
  └──────────────────────────┬──────────────────────────────────┘
                             │ future binding only (charter)
     ┌───────────────────────┼───────────────────────┐
     ▼                       ▼                       ▼
 RT-G04 Storage        RT-G10 Manifest         RT-G12 UI
 RT-G05 Registry       RT-G11 Validators       RT-G01 Workflow
 RT-G06 Queue           Agents / MIG / ORCA     Frontend / Deploy
```

---

## Handoff Binding Principles

**Closes OQ-S6-01** — minimum handoff binding semantics within Engine boundary **without** FACTORY-HANDOFF-PACKAGE document or package system.

### Relationship between Engine and handoffs

Handoffs exist in **two planes** — Engine owns one, references the other:

| Plane | Classification | Engine relationship |
|-------|----------------|---------------------|
| **Handoff contracts** | `HO-01`…`HO-13`, `HO-L1`, `HO-L2` definitions; required artefact lists; blocked conditions | **Reference only** — RUNTIME-HANDOFFS-v1 |
| **Handoff events** | Producer → consumer declared; boundary crossed; clearance status | **Engine owns** — project data |
| **Handoff package data** | PAGE_BUILD_SPEC, BLOCK_STACK_SPEC, FRONTEND_HANDOFF_PACKAGE **contents** | **Engine indexes ref only** — Generation Outputs / layers |
| **Frontend acknowledgement** | Ack required for `FRONTEND_READY` → `COMPLETE` | **Engine owns** ack **record** |

### Handoff binding principles (normative)

| ID | Principle |
|----|-----------|
| **HB-01** | Each forward TR transition across layer boundary **aligns** with one `HO-*` — Engine records **event**, Runtime defines **contract**. |
| **HB-02** | Handoff **clearance** and exit **gate PASS** are **both** required for segment exit (GC-05, LCP-02) — neither substitutes the other. |
| **HB-03** | Gate PASS **without** HO clearance → lifecycle **frozen** at segment; HO cleared **without** gate PASS → forward **still blocked**. |
| **HB-04** | `HO-12` blocked until Production QA PASS reflected in gate index (FT-07, HV-02). |
| **HB-05** | Rollback across handoff boundary → downstream HO events **SUPERSEDED** in Engine index (HV-03, LRC-07) — package files may exist physically; operator manages cleanup **externally**. |
| **HB-06** | Progression ledger `handoff_ref` **must align** with declared HO event (TC-05, LCC-04). |
| **HB-07** | Re-entry after rollback → **new** HO event records at re-crossed boundaries; prior events remain SUPERSEDED in history. |
| **HB-08** | Partial charter excluding LC-12 → HO-12 / HO-13 may be **N_A** — not treated as open blockers (LCS-02, GC-06). |

### Minimum handoff event content (logical — not schema)

Engine defines **minimum semantic content** of a handoff **event record** — **not** file format, **not** FACTORY-HANDOFF-PACKAGE:

| Logical element | Purpose |
|-----------------|---------|
| `handoff_id` | `HO-*` from Runtime catalogue |
| `boundary_from_state` / `boundary_to_state` | Runtime state pair at crossing |
| `clearance_status` | CLEARED \| BLOCKED \| SUPERSEDED |
| `producer` / `consumer` | Logical roles per RUNTIME-HANDOFFS |
| `gate_refs_at_boundary` | `RG-*` PASS refs relied upon — pointers only |
| `package_ref` | When applicable — link to handoff package data, **not** payload |
| `blocked_conditions_status` | Per HO blocked conditions — cleared or open |
| `operator_declaration` | Who declared clearance, when (logical) |
| `ack_ref` | For HO-12 / HO-13 — Frontend ack when required |
| `supersedes_event_ref` | On re-entry or rollback reconciliation |

**Engine never owns:** spec bodies, FRONTEND_HANDOFF_PACKAGE assembly rules (GENERATION-OUTPUTS), implementation code, physical file paths.

---

## Engine Responsibility Map

### Engine **is responsible for**

| Responsibility | Delivered by |
|----------------|--------------|
| Defining canonical **Factory Project** as logical tracking unit | Stage 1 |
| Binding project to **Runtime state instance** without new state codes | Stage 2 |
| **Observability composition** — seven operator questions from tracking model | Stage 3 |
| **Gate authorization composition** — satisfied/stale/invalid semantics | Stage 4 |
| **Lifecycle narrative** — segments, continuity, rollback cascade, partial completion | Stage 5 |
| **System boundary** — ownership, references, externals, allowed/forbidden future work | Stage 6 (this doc) |
| **Handoff event binding** minimum semantics | Stage 6 §Handoff Binding |
| Preserving **human-operated declaration** as v1 execution model | All stages |
| **Explicit non-claims** — no runtime, storage, automation mythology | All stages |

### Engine **is explicitly not responsible for**

| Non-responsibility | Owner / status |
|--------------------|----------------|
| Executing state transitions | Nobody in v1 — operator declares |
| Evaluating gate pass/fail automatically | **FUTURE** RT-G11 |
| Delivering or assembling handoff packages | Layer workstreams + Generation Outputs |
| Producing layer artefacts | Foundation layer workstreams |
| Frontend implementation, build, deploy | Frontend / external |
| Storing project instance data | **FUTURE** RT-G04 |
| Multi-project scheduling or registry | **FUTURE** RT-G05, RT-G06 |
| Operator dashboard, CLI, notifications | **FUTURE** RT-G12, RT-G13 |
| Agent orchestration (MIG, MetaBOT, etc.) | External systems |
| Legal template text, Registry matrices, block definitions | Frozen Foundation |
| Triumph / client production authorization | **SAFE UNKNOWN** — external |

### Operator answer map (full Engine v1)

| Question | Engine answer source |
|----------|---------------------|
| What is this project? | Object + Tracking identity zones |
| What state is it in? | State active instance + Lifecycle active segment |
| What states completed? | State history + Lifecycle segment history |
| What gates passed? | Gate outcome index + Gate Composition validity |
| What handoffs happened? | Handoff event index + Handoff Binding principles |
| What artefacts exist? | Artefact reference index |
| What remains unfinished? | Eligibility snapshot + Lifecycle «remains» derivation |
| What belongs to Engine vs external? | **This document** |

---

## Boundary Violation Patterns

Следующие паттерны **нарушают** Factory Engine Architecture v1 — **anti-patterns** для future work.

### Architectural violations

| ID | Anti-pattern | Why forbidden |
|----|--------------|---------------|
| **BV-01** | Redefining Runtime state codes or adding canonical states (e.g. `SEO_IN_PROGRESS`, `CANCELLED`) | ERA-W07; Engine consumes vocabulary only |
| **BV-02** | Adding or renaming `RG-*` / `HO-*` in Engine docs without Runtime supersession | Gate/handoff definitions belong to Runtime |
| **BV-03** | Merging T1 layer authority into single «project manifest» that replaces Foundation docs | Violates distributed authority (EO-01, ER-05) |
| **BV-04** | Claiming Engine **is** runtime, workflow engine, or orchestrator | Explicit non-claims; RT-G01 scope |
| **BV-05** | Defining JSON/YAML schemas, field lists, DB tables, folder layouts in Engine charter | Stage 1–6 explicit prohibition |
| **BV-06** | Creating FACTORY-GATE-RESULTS, FACTORY-STATE-STORE, FACTORY-ENGINE-SYSTEM as **implementation products** | Forbidden deliverables; Gate Results ≠ Stage 4 |
| **BV-07** | Automated state mutation or gate inference **without** operator declaration in v1 docs | Violates human-operated model |
| **BV-08** | Embedding handoff package payloads or artefact bodies in Engine tracking as authoritative | Violates ref-not-copy (AV-01, HB-08) |
| **BV-09** | Treating Frontend deploy / go-live as `COMPLETE` or Factory terminal | Stage 2 terminal rules; SAFE UNKNOWN external |
| **BV-10** | Inventing MIG/ORCA/MetaBOT/WPilot **integrations** in Engine architecture | ES-05; no integration proof in scope |
| **BV-11** | Modifying Legal Pack, Registry, 29 `block_id`, Core 5 blueprints via Engine work | Engine Protected Documents (ERA audit) |
| **BV-12** | Skip-forward progression without TR charter supersession | FT-09, LCP-07 |
| **BV-13** | Silent deletion of history on rollback — overwrite instead of SUPERSEDED | Append-only audit (AT-01, LCC-06) |
| **BV-14** | Queue position or multi-project priority as Engine canonical field | RT-G06 external |
| **BV-15** | «Passport» document duplicating Engine indexes as second SoT without charter | See Forbidden Future Documents |

### Documentation drift violations

| ID | Anti-pattern | Why forbidden |
|----|--------------|---------------|
| **BV-16** | Engine doc that rewrites accepted `*-SYSTEM-v1.md` layer contracts | Foundation protected |
| **BV-17** | Conflating global layer ACCEPTED status with per-project gate PASS | T5 vs T4 confusion |
| **BV-18** | Stale PASS treated as active after rollback without reconciliation | TC-04, GST-01 |
| **BV-19** | Lifecycle System / Gate Results System / Handoff Package System named as **existing** products | Explicit non-claims across Stages 4–5 |

---

## Allowed Future Documents

Классы документов, **легитимные** как next steps **вне** Engine architecture closure — **не создавать** в рамках Stage 6.

| Document class | Legitimacy | Conditions | Engine relationship |
|----------------|------------|------------|---------------------|
| **Project Manifest standard** | **ALLOWED** — RT-G10 charter | Separate operator charter; serialization of tracking zones | **May map to** Stage 3 zones — Engine **does not** define format |
| **Tracking Surface spec** | **ALLOWED** — RT-G12 charter | UI/CLI **display** of Engine composition | **References** Stages 1–5; does not redefine ownership |
| **Lifecycle Surface spec** | **ALLOWED** — RT-G12 / operational | Operator view of LC segments | **Derived from** Stage 5 visibility rules |
| **Gate Results display spec** | **ALLOWED** — RT-G12 only | Visual rendering of gate index | **Must not** become Gate Results **System** (Stage 4 non-claim) |
| **Operational playbook** | **ALLOWED** | Partial scope templates, suspension conventions, ERA-W03 pointer discipline | **Operational** — does not amend Engine semantics |
| **Charter templates** | **ALLOWED** | LR-07 partial scope, PHASE_SLICE, design-only | **Bind to** Engine scope mask rules |
| **Implementation charter** | **ALLOWED** | RT-G04 storage, RT-G05 registry, RT-G11 validators | **Separate** from Engine v1 — explicit non-claims preserved |
| **Integration charter** | **ALLOWED** | RT-G08 MIG; ORCA handoff refs if operator authorizes | **Must not** claim integration exists by default |
| **Supersession charter** | **ALLOWED** | If Runtime states/gates must change | ERA-W07 discipline — explicit banner |
| **Engine v2+ architecture** | **ALLOWED** | If scope expands with new operator charter | Must supersede v1 explicitly — not silent drift |

### RT-G09 documentation closure

Factory Engine Architecture v1 Stages 1–6 **satisfy** RT-G09 **documentation charter** scope from Engine Readiness Audit:

> project object model, state model, lifecycle model, gate model, handoff model, project tracking model

**RT-G09 gap status** in RUNTIME-GAPS remains **NOT STARTED** for **implementation** — documentation closure **does not** imply runtime product. Operator may update gap register separately — **outside** this Stage 6 deliverable.

---

## Forbidden Future Documents

Классы документов, которые **не должны** создаваться — или только под **explicitly different charter** with anti-pattern review.

| Document class | Verdict | Why forbidden / deferred |
|--------------|---------|--------------------------|
| **FACTORY-PROJECT-MANIFEST-v1.md** | **FORBIDDEN** in Engine Stages 1–6 | RT-G10 is separate charter; schemas explicitly excluded |
| **FACTORY-PROJECT-PASSPORT-v1.md** | **FORBIDDEN** | Duplicates Object + Tracking identity without distinct semantics; risks second SoT (BV-15) |
| **FACTORY-GATE-RESULTS-v1.md** | **FORBIDDEN** | Stage 4 defines composition **semantics** — Gate Results **System** is implementation (BV-06) |
| **FACTORY-HANDOFF-PACKAGE-v1.md** | **FORBIDDEN** | Package **data** owned by Generation Outputs; Engine owns **events + refs** only |
| **FACTORY-ENGINE-SYSTEM-v1.md** | **FORBIDDEN** as implementation product | Would imply shipped system; boundary doc replaces **system product** claim |
| **FACTORY-STATE-STORE-v1.md** | **FORBIDDEN** | RT-G04 storage — implementation territory |
| **FACTORY-ENGINE-LIFECYCLE-v1.md** | **FORBIDDEN** as Lifecycle System | Stage 5 is composition model — not executor (Stage 5 non-claims) |
| **Engine runtime / orchestrator spec** | **FORBIDDEN** under Engine charter | RT-G01, RT-G02 — separate high-risk charter |
| **Engine agent card / workflow JSON** | **FORBIDDEN** | Agent system — external to Engine |
| **Unified YAML project schema in Engine path** | **FORBIDDEN** | BV-05; belongs to RT-G10 if ever chartered |
| **FACTORY-HANDOFF-BINDING-v1.md** (standalone) | **DEFERRED / CLOSED** | Minimum semantics **closed in this doc** §Handoff Binding — separate doc **unnecessary** unless v2 expands |

---

## Boundary Completeness

### When Engine Architecture v1 is architecturally complete

Factory Engine Architecture v1 is **architecturally complete** when all conditions hold:

| # | Criterion | Status after Stage 6 |
|---|-----------|----------------------|
| 1 | Factory Project **object** defined with distributed authority | **DONE** — Stage 1 |
| 2 | **State instance** model bound to Runtime 14 states | **DONE** — Stage 2 |
| 3 | **Tracking** observability composition defined | **DONE** — Stage 3 |
| 4 | **Gate composition** with namespace mapping and sufficiency | **DONE** — Stage 4 |
| 5 | **Lifecycle composition** with rollback cascade and partial rules | **DONE** — Stage 5 |
| 6 | **System boundary** — ownership, externals, handoff binding, violations | **DONE** — Stage 6 |
| 7 | Operator can answer ownership questions **without** full workspace read | **DONE** — this document |
| 8 | Explicit non-claims preserved across all stages | **DONE** |
| 9 | No implementation, storage, manifest, runtime created | **DONE** — charter respected |

**Engine v1 completeness ≠ Factory production automation.** A project may be fully described by Engine models yet remain **human-operated** with **no** persistence layer.

### What remains future implementation territory

| Territory | Gap ID | Notes |
|-----------|--------|-------|
| Physical persistence of tracking records | RT-G04 | Storage charter |
| Canonical manifest / serialization | RT-G10 | **May** map to Stage 3 zones |
| Project registry, multi-project index | RT-G05 | One Engine model per project |
| Queue, prioritization | RT-G06 | External to per-project Engine |
| Operator UI / dashboard / CLI | RT-G12 | Display layer |
| Validator CLI, automated gates | RT-G11 | Does not change Engine semantics |
| Workflow engine, automation, webhooks | RT-G01, RT-G03, RT-G13 | Highest risk |
| MIG / external orchestration binding | RT-G08 | Integration charter |
| Rollback automation | RT-G15 | Cascade rules exist — execution deferred |
| Execution logs (machine-readable) | RT-G07 | Append-only audit exists logically |
| Triumph deploy, client go-live | — | **SAFE UNKNOWN** |

### Completeness diagram

```text
ENGINE ARCHITECTURE v1 (COMPLETE after Stage 6)
├── Documentation methodology  ✓
├── Per-project logical model    ✓
├── Ownership & reference rules  ✓
├── Human-operated declaration   ✓
└── Boundary & anti-patterns     ✓

IMPLEMENTATION PLANE (NOT STARTED — separate charters)
├── Storage · Manifest · Registry
├── UI · Validators · Automation
└── Agents · MIG · External integrations
```

---

## Explicit Non-Claims

This document and Factory Engine Architecture v1 (Stages 1–6) collectively:

- **are not** a Website Factory **runtime**, execution engine, or shipped product;
- **are not** a **workflow engine**, BPMN executor, or n8n replacement;
- **are not** a **queue**, job scheduler, or work prioritization system;
- **are not** an **orchestrator** or automation layer;
- **are not** an **application**, dashboard, operator UI (RT-G12), or CLI;
- **are not** **implementation** — no code, validators, CI binding, or agents;
- **are not** a **storage layer**, database, file format, or state store (RT-G04);
- **are not** an **autonomous factory** or unattended production pipeline;
- **are not** an **agent system**, MIG orchestration, MetaBOT runtime, or AI workflow;
- **do not** define JSON/YAML **schemas**, field lists, folder structures, manifest paths, or passport format;
- **do not** authorize Foundation redesign, Legal Pack expansion, or new `block_id`;
- **do not** claim existence of project registry (RT-G05), manifest standard (RT-G10), Gate Results System, Handoff Package System, Lifecycle System, or FACTORY-ENGINE-SYSTEM **product**;
- **do not** invent integrations with WPilot, ORCA, MetaBOT, or MIG — external until separately chartered.

**Human-operated declaration** remains the v1 model per [RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) §7.

---

## Open Questions After Stage 6

Stage 6 **closes** OQ-S6-01 (handoff binding minimum semantics) and OQ-S6-02 (Engine system boundary / RT-G09 documentation closure). Remaining items require **operational charter**, **implementation charter**, or **Engine v2** — not Engine v1 architecture gaps.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-S6-01** | Handoff binding minimum semantics | **CLOSED** — §Handoff Binding Principles |
| **OQ-S6-02** | Engine system boundary; RT-G09 doc closure | **CLOSED** — this document |
| **OQ-S6-03** | PHASE_SLICE / multi-`generation_id` — shell vs slice indexes | **OPEN** — implementation or Engine v2 charter |
| **OQ-S6-04** | Partial scope formal jump table for consecutive EXCLUDED states | **OPEN** — charter templates (allowed future doc) |
| **OQ-S6-05** | RT-G10 manifest — which tracking zones serialize | **OPEN** — RT-G10 charter; not Engine v1 |
| **OQ-S6-06** | Extended types ER-01 — lifecycle prerequisites | **OPEN** — Registry charter |
| **OQ-S6-07** | Chrome blocks without `block_id` (ERA-W01) — artefact ref conventions | **OPEN** — operational / Engine v2 |
| **OQ-S6-08** | `PASS_WITH_WARNINGS` validation — gate decision composition | **OPEN** — validation + AP-* operational binding |
| **OQ-S6-09** | `FACTORY_TRACK_CLOSED_PARTIAL` standardization | **OPEN** — operational playbook |
| **OQ-S6-10** | External workspace pointers (ERA-W03) discipline | **OPEN** — operational playbook |
| **OQ-S6-11** | Stages 1–5 alignment audit | **ADDRESSED** — boundary doc synthesizes; formal audit optional P3 |
| **OQ-12** (Stage 1) | RT-G05 registry vs logical project | **BOUNDED** — registry external (ES-03) |

---

## Recommended Next Step

**Engine Architecture v1 is documentation-complete.** No further Engine architecture stages are required for RT-G09 documentation charter scope.

Recommended **operator** next actions ( **separate charters** — not part of Engine v1):

1. **Optional P3 hygiene:** sync stale RUNTIME-ROADMAP acceptance checkbox (ERA-W05) — non-blocking.
2. **If persistence needed:** authorize **RT-G10 Project Manifest** charter — serialize Stage 3 tracking zones; **do not** conflate with Engine ownership rules.
3. **If multi-project operations needed:** authorize **RT-G05 Project Registry** charter — external index; one Engine logical model per entry.
4. **If operator UI needed:** authorize **RT-G12** charter — Tracking/Lifecycle Surface as **display** of Engine composition.
5. **If automation needed:** authorize **RT-G01 / RT-G11** implementation charter — explicit non-claims from Engine v1 **must** carry forward.

**Do not** proceed to FACTORY-PROJECT-MANIFEST, PASSPORT, GATE-RESULTS, HANDOFF-PACKAGE, ENGINE-SYSTEM, or STATE-STORE documents without explicit supersession of forbidden list above.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Physical location / format of tracking records | **NOT DEFINED** — RT-G04, RT-G10 FUTURE |
| Calendar for implementation charters | **not scheduled** |
| Triumph production deploy vs Factory `COMPLETE` | **UNKNOWN** — external |
| WPilot relationship to Factory Project | **UNKNOWN** — no repo evidence for integration |
| Whether operator updates RT-G09 gap register to DOCUMENTED | **requires operator action** — outside Stage 6 file scope |
| MARS v2 baseline path repo-wide | **not verified** in Engine scope |

---

*Factory Engine System Boundary v1 — Stage 6 complete. Architecture only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Engine System Boundary v1

**Stage:** Factory Engine Architecture v1 — Stage 6 (System Boundary)  
**Deliverable:** `FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md` (created)  
**Summary:** Определена финальная архитектурная граница Factory Engine для одного Factory Project: purpose, ownership vs reference vs external systems; закрыты OQ-S6-01 (handoff binding) и OQ-S6-02 (RT-G09 documentation closure); responsibility map; anti-patterns; классификация allowed/forbidden future documents; критерии architectural completeness Engine v1 — без runtime, storage, manifests, passports, schemas, implementation.  
**Git:** no commit, no push (per task charter).
