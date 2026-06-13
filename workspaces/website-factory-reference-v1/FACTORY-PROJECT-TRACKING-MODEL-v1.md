# REPORT — Factory Project Tracking Model v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Factory Engine Architecture v1 — **Stage 3 only**  
**Контекст:** Website Factory Foundation Era **COMPLETE**; [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) **ACCEPTED** (Stage 1); [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) **ACCEPTED** (Stage 2); Engine Readiness Audit v1 — **PASS WITH WARNINGS**  
**Тип:** architecture only — **без** implementation, runtime product, agents, code, workflows, databases, automation, storage format, manifests, passports, dashboards, UI, CLI  
**Связь:** [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md), [FOUNDATION-FINALIZATION-PASS-v1.md](FOUNDATION-FINALIZATION-PASS-v1.md), [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md)

---

## Purpose

Stage 1 ответил: **«Что движется?»** — канонический [Factory Project](FACTORY-PROJECT-OBJECT-MODEL-v1.md) как логическая единица с распределённой authority.

Stage 2 ответил: **«Как это движется?»** — [модель состояния](FACTORY-PROJECT-STATE-MODEL-v1.md): active state, progression, rollback, re-entry, terminal `COMPLETE`.

Stage 3 отвечает: **«Как оператор видит и отслеживает это?»** — **Project Tracking Model**: архитектура наблюдаемости одного Factory Project **без** определения хранилища, форматов, манифестов или инструментов.

### Зачем существует Project Tracking

| Проблема | Как tracking решает |
|----------|---------------------|
| Истина распределена по Foundation layers, Runtime и layer workstreams | **Агрегирующая проекция** — единая логическая observability surface для **этого** production case |
| Оператор не должен читать весь workspace | **Composed view** — ответы на семь operator questions из одной tracking-модели |
| State, gates, handoffs и artefacts имеют разных владельцев | Tracking **собирает ссылки и instance records**, не сливая authority |
| Human-operated v1 — нет автоматического recorder | Tracking фиксирует **что оператор объявил видимым**, не подменяя enforcement |

### Что tracking **не** решает

| Out of scope | Куда относится |
|--------------|----------------|
| Автоматическая смена state, gate evaluation, handoff delivery | Runtime rules + **FUTURE** automation (RT-G01, RT-G03, RT-G11) |
| Определение pass/fail criteria, gate IDs, transition legality | Runtime + Foundation layer contracts (T1–T3) |
| Хранение тел layer artefacts | Layer workstreams; tracking держит **refs only** |
| Приоритизация очереди проектов, scheduling | **FUTURE** registry/queue (RT-G05, RT-G06) |
| Frontend implementation progress, deploy, hosting | Post-Factory / external workstreams |
| Физический формат записи, путь к файлу, schema | **FUTURE** manifest standard (RT-G10), storage (RT-G04) — **явно не Stage 3** |

**Tracking — это модель наблюдения и composition**, не исполнение и не persistence.

---

## Foundation Dependencies

Project Tracking Model **наследует** Stage 1–2 и **компонует** только принятую Foundation + Runtime:

| Dependency | Role for tracking |
|------------|-------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Mandatory components, authority tiers T1–T5, gate/handoff/artefact ownership split |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Active state, history, progression ledger, eligibility snapshot, scope mask — **что показывать** оператору о движении |
| [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) | Vocabulary для state visibility — **не** instance storage |
| [runtime-architecture/RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) | `RG-*` definitions — tracking показывает **outcome records**, не criteria |
| [runtime-architecture/RUNTIME-HANDOFFS-v1.md](runtime-architecture/RUNTIME-HANDOFFS-v1.md) | `HO-*` contracts — tracking показывает **event records + package refs** |
| [runtime-architecture/PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) | LC-*, LS-*, AP-* — контекст halt/resume в visibility |
| [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md) | Engine ↔ Runtime boundary; ERA-W02 gate namespaces |
| [FOUNDATION-FINALIZATION-PASS-v1.md](FOUNDATION-FINALIZATION-PASS-v1.md) | 14-layer ACCEPTED stack — tracking **не** переопределяет layer status |

**Authority:** tracking **не** добавляет новых state codes, gate IDs или handoff contracts. При конфликте «что означает `SEO_READY`» → Runtime. При конфликте «где **этот** проект» → Factory Project tracking instance (Engine), **используя** Runtime vocabulary.

---

## Tracking Scope

Tracking scope — **логические зоны владения и индексации** для одного Factory Project. **Не** field lists, **не** schemas.

### Внутри tracking scope (owns or indexes for observation)

| Zone | Ownership | Tracking role |
|------|-----------|---------------|
| **Identity references** | Tracking **owns** stable project identity shell | Оператор узнаёт production case без workspace archaeology |
| **Charter & scope declaration refs** | Project (operator-authored); tracking **indexes** | Bounds Factory work; drives partial visibility |
| **Current state reference** | Tracking **owns** active instance value | «Where now?» — Runtime code, один ACTIVE |
| **State history reference** | Tracking **owns** occupancy + progression index | «What completed?» — ordered segments + ledger |
| **Eligibility snapshot** | Tracking **derives** for display | «What next / blocked?» — read-only evaluation surface |
| **Scope state mask** | Tracking **owns** charter-driven applicability | Partial scope: APPLICABLE / EXCLUDED / N_A per state |
| **Gate outcome records** | Tracking **owns** instance records | «What gates passed?» — PASS/FAIL/blocked/stale + sign-off refs |
| **Handoff event records** | Tracking **owns** instance records | «What handoffs happened?» — HO-ID, boundary, clearance |
| **Handoff package references** | Tracking **indexes**; package **data** — Generation Outputs | Link to FRONTEND_HANDOFF_PACKAGE etc. without owning spec bodies |
| **Layer artefact references** | Tracking **indexes**; artefacts — layers | «What artefacts exist?» — pointers per lifecycle phase |
| **Scope freeze marker** | Tracking **owns** from Generation Ready onward | Visibility of immutable generation boundary |
| **Parallel legal track status refs** | Tracking **indexes** legal workflow outputs | RG-LEGAL_COMPLETE / RG-ENTITY_VERIFIED visibility |
| **Audit trail (tracking-scoped)** | Tracking **owns** append-only operator declarations | Who declared what, when (logical), correction chain |
| **Invalidation / supersession markers** | Tracking **owns** post-rollback visibility | Stale gates, superseded segments — **status**, not deletion |

### Вне tracking scope (referenced, not owned)

| Zone | Owner | Tracking may show |
|------|-------|-------------------|
| Layer contract semantics | Foundation T1 | Layer doc refs only |
| Gate / handoff **definitions** | Runtime + layer gates T2–T3 | Gate ID + link to defining doc |
| Validation run **bodies** | Layer workstreams | Ref + PASS/FAIL summary for advance |
| Frontend code, deploy logs | Frontend / external | **Never** as Factory tracking core |
| Global layer ACCEPTED status | NEXT-PRIORITIES T5 | Optional context link — **not** per-project progress |
| MIG sessions, n8n runs, agent transcripts | External orchestration | **Not** Factory tracking unless charter binds ref |

### Operator questions → tracking zones

| Question | Primary tracking zones |
|----------|------------------------|
| What is this project? | Identity shell, charter, scope tier, classification ref (when present), generation slice ref (when applicable) |
| What state is it in? | Active state reference |
| What states already completed? | State history reference (COMPLETED segments) |
| What gates passed? | Gate outcome index (current + historical with stale markers) |
| What handoffs happened? | Handoff event index + package refs |
| What artefacts exist? | Layer artefact reference index (by phase / route / block) |
| What remains unfinished? | Derived: eligibility snapshot + open gates + active state + scope mask gaps |

---

## Tracking Boundaries

```text
┌──────────────────────────────────────────────────────────────────┐
│                    PROJECT TRACKING (Stage 3)                     │
│   observability composition — instance records + reference index   │
└──────────────────────────────────────────────────────────────────┘
         │ reads vocabulary              │ indexes outputs
         ▼                               ▼
┌─────────────────────┐         ┌─────────────────────┐
│  RUNTIME (T2)       │         │  FOUNDATION (T1)    │
│  states, TR/FT/RG,  │         │  layer contracts,   │
│  HO definitions     │         │  artefacts produced │
└─────────────────────┘         └─────────────────────┘
         │                               │
         └─────────── neither stores ────┘
                     project instances
                              │
                              ▼
              ┌───────────────────────────────┐
              │  FUTURE SYSTEMS (explicit)     │
              │  RT-G04 storage, RT-G05 registry│
              │  RT-G10 manifest, RT-G12 UI     │
              │  workflow engine, agents, queue   │
              └───────────────────────────────┘
```

| Boundary | Project Tracking | Runtime | Foundation layers | Future systems |
|----------|------------------|---------|-------------------|----------------|
| State **vocabulary** | References | **Owns** | — | — |
| State **instance** + history | **Owns** visibility | Rules only | — | RT-G04 may persist |
| Transition **legality** | Displays derived eligibility | **Owns** TR/FT/DR/RB | — | Auto-enforcement FUTURE |
| Gate **definitions** | References | **Owns** RG-* | **Owns** GATE_* / validation | — |
| Gate **outcome records** | **Owns** index | — | Inputs from layer runs | Recorder FUTURE |
| Handoff **contracts** | References | **Owns** HO-* | Required artefact lists | — |
| Handoff **events + package refs** | **Owns** events; **indexes** packages | — | Produces package data | RT-G10 may serialize |
| Artefact **content** | — | — | **Owns** | — |
| Artefact **refs per project** | **Owns** index | — | — | — |
| Operator **single view** | **Owns** composition model | — | — | UI FUTURE (RT-G12) |
| Multi-project **registry** | One project per tracking model | — | — | RT-G05 FUTURE |

**Foundation rule (repeated):** Project Object owns identity, state instance, gate outcomes, handoff records, artefact references. Runtime owns state/gate/handoff **vocabulary**. Tracking **implements observability** over that ownership split — **не** storage architecture.

---

## Tracking Visibility Principles

### Tier A — Must always be visible (minimal trackable surface)

Information без которой проект **не считается наблюдаемым** в Factory scope:

| Element | Visibility rule |
|---------|-----------------|
| Stable project identity | Always — even at `NEW_PROJECT` |
| Charter / scope tier | Always |
| Active `runtime_state_code` | Always — exactly one (CS-01) |
| Scope applicability mask (or default full chain) | Always |
| Index presence for gates, handoffs, artefacts | **Structure exists** — may be empty early |
| Last operator declaration timestamp (logical) | Always when any transition recorded |

### Tier B — May be optional or deferred visibility

| Element | When optional |
|---------|---------------|
| `site_type_code`, blueprint ref | Until `CLASSIFIED` / `BLUEPRINT_READY` |
| Per-route artefact refs | Until corresponding LC phase |
| `generation_id`, scope freeze | Until `GENERATION_READY` |
| Parallel legal status | Until scope requires legal track |
| Eligibility snapshot detail | May collapse to «blocked — see open gates» |
| Foundation version pins | Implicit default unless charter pins |
| External workspace pointers (ERA-W03) | Charter-declared only |
| `FACTORY_TRACK_SUSPENDED` flag | When charter suspends Factory track without new Runtime state |

### Tier C — Must never be considered part of tracking

| Element | Why excluded |
|---------|--------------|
| Full text of Legal Pack templates | T1 authority — class-level |
| Block registry definitions, site type matrices | T1 — not instance |
| Gate pass/fail **criteria** and failure libraries | Definitions — not project observation |
| Handoff package **payload bodies** (specs, HTML) | Handoff package data — indexed only |
| Frontend source code, CI logs, deploy status | Post-Factory / external |
| Agent prompts, chat, tickets | Non-canonical |
| Queue position, priority rank among projects | Not per-project tracking |
| Automated inference of state without operator declaration | Forbidden in v1 |

### Visibility composition principle (TV-01)

**Single logical view** = compose Tier A + available Tier B from indexes **without merging authority**. Tracking surface **points to** authoritative sources; it **does not become** the Legal Pack, Registry, or Runtime doc.

### Visibility freshness principle (TV-02)

Tracking reflects **last declared truth** by operator. Stale gate markers after rollback **must** remain visible (historical) with **stale** status — not hidden. Corrections = new declaration records (append-only).

---

## State Visibility

State visibility связывает [Factory Project State Model](FACTORY-PROJECT-STATE-MODEL-v1.md) с operator observation.

### Current state visibility

| Rule | ID | Statement |
|------|-----|-----------|
| Single active display | **SV-01** | Tracking **always** shows exactly one active Runtime state code |
| Phase context | **SV-02** | Active code maps to LC-* phase for operator «where in chain» |
| Halt is not hidden | **SV-03** | LS-* stop → active **unchanged**; tracking shows **halt at** current state, not synthetic sub-state |
| Terminal display | **SV-04** | `COMPLETE` → tracking shows closed Factory track; no outbound eligibility |
| Invalid active | **SV-05** | Active code outside Runtime catalogue → tracking surface **invalid** — must flag, not silently normalize |

**Operator «What state is it in?»** = active `runtime_state_code` + optional LC label + halt/blocked annotation from eligibility snapshot.

### State history visibility

| Rule | ID | Statement |
|------|-----|-----------|
| Completed occupancy | **SHV-01** | Tracking shows ordered list of states with `COMPLETED` occupancy |
| Progression ledger | **SHV-02** | Forward and rollback transitions visible as **events**, not silent overwrites |
| Supersession | **SHV-03** | Post-rollback segments marked `SUPERSEDED_BY_ROLLBACK` — remain in history |
| Re-entry | **SHV-04** | Re-occupation of same Runtime code creates **new** history segment linked to prior |
| Excluded states | **SHV-05** | LR-07 `EXCLUDED` / `N_A` visible in mask — not shown as completed unless charter jump documented |
| Intra-state work | **SHV-06** | Work inside active state **without** transition — **not** new history segment; visible via gates/artefacts |

### Current vs history — operator split

```text
CURRENT STATE          →  "Where is the project NOW?"
STATE HISTORY          →  "What states did it pass through?"
PROGRESSION LEDGER     →  "How did it move (forward/rollback)?"
ELIGIBILITY SNAPSHOT   →  "What remains / what blocks next step?"
```

**State visibility does not duplicate gate criteria** — only shows which gates progression records **claimed** at transition (`gate_refs_passed`).

---

## Gate Visibility

Gate visibility — **instance observation** across three complementary namespaces (ERA-W02). Tracking **не** владеет definitions.

### What tracking must know (show)

| Visibility need | Source of truth for display |
|-----------------|----------------------------|
| Which `RG-*` recorded PASS/FAIL/blocked for **this** project | Gate outcome index |
| Open vs closed gates **relative to active state** | Derived from index + Runtime transition map |
| Stale gates after rollback | Index status `STALE` — still visible |
| Operator sign-off refs (AP-01…AP-09) where applicable | Linked to outcome record |
| Composite readiness **status** (e.g. Generation Ready) | **Aggregated view** of constituent PASS refs — criteria stay Runtime/layer |
| Layer `GATE_*` and validation PASS/FAIL **as referenced by** RG advance | Outcome refs — mapping detail deferred to Stage 4 |

### What tracking must not own

| Excluded | Owner |
|----------|-------|
| Gate ID definitions, inputs, pass/fail criteria | RUNTIME-GATES, layer *-GATES-v1, validation contracts |
| Failure remediation playbooks | RUNTIME-FAILURE-LIBRARY, layer docs |
| Automated gate evaluation | **FUTURE** |
| Namespace mapping table RG ↔ GATE_* ↔ validation | **Stage 4** gate composition model |

### Gate visibility rules

| Rule | ID | Statement |
|------|-----|-----------|
| Outcome without criteria | **GV-01** | Tracking shows **that** `RG-VALIDATION_PASS` = PASS on date X; **not** validation rule text |
| Open gate blocks forward display | **GV-02** | Eligibility snapshot cites first open blocking gate |
| FAIL visible | **GV-03** | FAIL outcomes **remain visible** — drive LS halt narrative |
| Composite display | **GV-04** | Composite gates shown as **rollup status + expandable constituent refs** (logical) — not redefinition |
| No silent erase on rollback | **GV-05** | Prior PASS above rollback target → `STALE`, not deleted |

**Operator «What gates passed?»** = gate outcome index filtered by current validity + historical stale segment.

**Operator «What blocks movement?»** = open FAIL/blocking gates + parallel legal + handoff blocked conditions — **derived**, not stored as new state.

---

## Handoff Visibility

Handoff visibility separates **events** (project data) from **packages** (handoff package data) per Stage 1.

### What tracking must know (show)

| Visibility need | Classification |
|-----------------|----------------|
| Handoff ID (`HO-*`), state boundary crossed | Handoff **event** record |
| Producer → consumer declaration, operator clearance | Handoff **event** record |
| Blocked / cleared status per HO blocked conditions | Handoff **event** record |
| Reference to handoff package (e.g. FRONTEND_HANDOFF_PACKAGE) | **Package ref** in index |
| Frontend acknowledgement for HO-12 / closure | Handoff **event** / ack ref |
| Superseded handoffs after rollback | Event status `SUPERSEDED` — visible |

### What tracking must not own

| Excluded | Owner |
|----------|-------|
| HO-* contract definitions, required artefact lists | RUNTIME-HANDOFFS |
| PAGE_BUILD_SPEC, BLOCK_STACK_SPEC, spec **contents** | Generation Outputs / layer artefacts |
| Production QA checklist **bodies** | Production QA layer |
| Implementation code | Frontend workstream |

### Handoff visibility rules

| Rule | ID | Statement |
|------|-----|-----------|
| Event vs package split | **HV-01** | Tracking **always** distinguishes «handoff declared» from «package contents» |
| HO-12 gate | **HV-02** | Frontend handoff visibility **blocked** until Production QA PASS reflected in gate index |
| Rollback invalidation | **HV-03** | Downstream HO events beyond rollback target → superseded in visibility |
| Minimum event content | **HV-04** | Logical minimum: HO-ID, boundary states, clearance status, package ref when applicable — **format** Stage 5 |

**Operator «What handoffs happened?»** = handoff event index ordered by boundary + linkage to progression ledger `handoff_ref`.

---

## Artefact Visibility

Artefacts — **produced by Foundation layers**; tracking **references without owning or duplicating**.

### Reference model

```text
Layer workstream  ──produces──▶  artefact (authoritative body)
                                      │
                                      │ ref only
                                      ▼
                            Project artefact reference index
                                      │
                                      ▼
                            Tracking visibility surface
```

### What tracking shows

| Artefact class | Visibility |
|----------------|------------|
| Classification outputs | Ref when `CLASSIFIED` |
| Blueprint binding | Ref when `BLUEPRINT_READY` |
| PAGE-CONTRACT per route | Refs when `PAGE_READY` |
| Block stack resolution | Refs when `BLOCK_READY` |
| Validation run records | Ref + PASS/FAIL when `VALIDATED` / content validation |
| SEO, Design, Content bindings | Refs at respective READY states |
| Generation contract / outputs | Refs + `generation_id` when `GENERATION_READY` |
| Production QA run | Ref when `PRODUCTION_QA_READY` |
| Legal route mapping, Entity Card | Parallel track refs when in scope |

### Artefact visibility rules

| Rule | ID | Statement |
|------|-----|-----------|
| Ref not copy | **AV-01** | Tracking **never** embeds artefact body as authoritative |
| Lifecycle alignment | **AV-02** | Refs grouped by LC phase / Runtime state for operator scan |
| Invalidation on rollback | **AV-03** | Downstream refs beyond rollback target → `INVALIDATED` status visible |
| Missing ref | **AV-04** | Required ref absent for current state → tracking shows **gap** — drives unfinished work |
| Foundation docs | **AV-05** | Frozen layer **definitions** linked as class refs — not per-project copies |

**Operator «What artefacts exist?»** = artefact reference index with validity status — **not** file tree listing.

**Operator «What remains unfinished?»** = required refs for active state + open gates + eligibility gaps — **derived composition**.

---

## Audit Trail Principles

Audit trail в tracking — **append-only operator declaration history** scoped to Factory Project observation. **Не** полный enterprise audit log.

### Belongs in tracking audit trail

| Record class | Purpose |
|--------------|---------|
| State transition declarations | Forward + rollback + correction refs |
| Gate outcome sign-offs | Who passed/failed/blocked |
| Handoff clearance declarations | HO completed / blocked cleared |
| Scope mask / charter amendments affecting tracking | LR-07 changes |
| Invalidation events | Rollback-triggered stale/invalidated markers |
| Correction records | `corrects_declaration_id` — no silent delete |

### Belongs elsewhere (may link from tracking)

| Record class | Owner |
|--------------|-------|
| Validation run detailed logs | Layer validation workstreams |
| Legal generation audit | Legal Pack workflow |
| Git commit history, file diffs | Workspace tooling |
| Agent session transcripts | External |
| Global layer acceptance changes | NEXT-PRIORITIES — not per-project |

### Audit principles

| Rule | ID | Statement |
|------|-----|-----------|
| Append-only | **AT-01** | Declarations add; correction = new record |
| Human-declared v1 | **AT-02** | No automated writer implied |
| Separation from definitions | **AT-03** | Audit shows **that** operator declared PASS — not **why** criteria met (see layer artefact) |
| Proportionality | **AT-04** | Tracking audit = Factory movement + gate/handoff declarations — not full workspace telemetry |
| Immutability of history | **AT-05** | Superseded ≠ deleted — audit preserves narrative |

---

## Tracking Completeness

### Fully trackable project

A Factory Project is **fully trackable** when an operator can answer **all seven** primary questions (see Tracking Scope) **from the tracking composition alone**, with only **follow refs** to authoritative bodies — **without** workspace-wide search.

| Criterion | ID | Requirement |
|-----------|-----|-------------|
| Identity + charter | **TC-01** | Present |
| Valid active state | **TC-02** | Exactly one Runtime code |
| State history coherent | **TC-03** | Active consistent with latest progression ledger |
| Gate index current | **TC-04** | No undeclared stale PASS treated as active for eligibility |
| Handoff index aligned | **TC-05** | Progression ledger handoff_refs match declared HO events |
| Artefact refs for reached phases | **TC-06** | No silent gaps for mandatory bindings at completed states |
| Scope mask documented | **TC-07** | Full chain default or charter partial path explicit |

**Typical fully trackable moments:** any stable active state after operator hygiene; always at `COMPLETE` if closure criteria met (Stage 2 terminal rules).

### Partially trackable project

**Partially trackable** — tracking surface exists but **one or more** Tier A elements missing, invalid, or inconsistent.

| Condition | Partial trackable signal |
|-----------|--------------------------|
| Early intake | Empty gate/handoff/artefact indexes — **expected**; identity + active state suffice |
| Undeclared transition | Active state disagrees with ledger — **integrity warning** |
| Missing mandatory ref at completed state | Gap flagged — operator must declare or rollback |
| Post-rollback without invalidation hygiene | Stale gates appear active — **partial until reconciled** |
| `FACTORY_TRACK_SUSPENDED` | Factory questions may be frozen at last declared state |
| PHASE_SLICE / multi-`generation_id` | **OPEN** — shell trackable; slice binding may be partial (OQ-S4-01) |
| Extended types ER-01 | May remain partially trackable until charter completes prerequisites |

### Non-trackable (in Factory sense)

| Condition | Meaning |
|-----------|---------|
| No stable project identity | Not a Factory Project in tracking scope |
| Active state not in Runtime catalogue | Invalid — must not present as trackable |
| Workstream outside Factory charter with no identity shell | Outside model — e.g. raw Frontend repo with no Factory binding |

**Completeness is about observability quality**, not production readiness. A project at `BLOCK_READY` with validation FAIL is **fully trackable** yet **blocked** — tracking shows both.

---

## Explicit Non-Claims

This document and the Factory Project Tracking Model it defines:

- **are not** a Website Factory runtime, execution engine, or shipped product;
- **are not** an autonomous factory, agent system, MIG orchestration, or AI workflow;
- **are not** a queue, job scheduler, or work prioritization system;
- **are not** a workflow engine, BPMN executor, or n8n replacement;
- **are not** an orchestrator or automation layer;
- **are not** an application, dashboard, operator UI (RT-G12), or CLI;
- **are not** implementation — no code, validators, CI binding, or agents;
- **are not** a storage layer, database, file format, or state store (RT-G04);
- **are not** a project manifest standard or passport (RT-G10 — **FUTURE**, explicitly not defined here);
- **are not** FACTORY-GATE-RESULTS, FACTORY-HANDOFF-PACKAGE, FACTORY-STATE-STORE, FACTORY-ENGINE-LIFECYCLE, or FACTORY-ENGINE-SYSTEM documents;
- **do not** define JSON/YAML schemas, field lists, folder structures, or tracking files;
- **do not** modify Runtime Architecture, Stage 1 Object Model, or Stage 2 State Model semantics;
- **do not** claim automated persistence, project registry (RT-G05), or multi-project queue (RT-G06).

Human-operated declaration remains the v1 observation model per Runtime Architecture.

---

## Open Questions For Stage 4

Stage 4+ Engine documents must resolve (without answering here):

| ID | Question | Primary dependency |
|----|----------|-------------------|
| **OQ-S4-01** | Gate namespace **mapping table** — `RG-*` ↔ layer `GATE_*` ↔ validation gates (ERA-W02) | Gate composition model |
| **OQ-S4-02** | Composite gate **representation** in gate outcome index (OQ-04 Stage 1) | Gate composition model |
| **OQ-S4-03** | Minimum gate outcome record content (logical) — without schema | Gate composition model |
| **OQ-S4-04** | Cascade **invalidation table** — which ref types invalidate per RB-* target (OQ-S3-05) | Lifecycle binding + tracking |
| **OQ-S4-05** | Partial scope **effective path** / jump table when states `EXCLUDED` (OQ-S3-01) | Lifecycle model |
| **OQ-S4-06** | `FACTORY_TRACK_SUSPENDED` conventions vs active state display (OQ-S3-02) | Lifecycle model |
| **OQ-S4-07** | Partial closure without `COMPLETE` — deliverable boundary (OQ-S3-03) | Lifecycle model |
| **OQ-S4-08** | Multiple `generation_id` / PHASE_SLICE — tracking shell vs slice visibility (OQ-S3-04) | Lifecycle + Generation binding |
| **OQ-S4-09** | Handoff record minimum content (OQ-08 Stage 1) — format still deferred | Handoff binding Stage 5 |
| **OQ-S4-10** | Relationship to future RT-G05 registry entry vs logical project (OQ-12) | Engine system boundary |
| **OQ-S4-11** | RT-G10 manifest — which tracking zones **may** serialize when chartered (OQ-S3-06) | Manifest charter — **not** Stage 4 design |
| **OQ-S4-12** | Extended types ER-01 — tracking prerequisites before full production path | Registry charter |

---

## Recommended Next Step

**Stage 4 — Factory Project Gate Composition Model (Engine Architecture v1):** formalize gate namespace mapping, composite gate visibility rules, and outcome record semantics **as referenced by** this tracking model — **without** defining storage, FACTORY-GATE-RESULTS implementation, or renaming `RG-*`.

Subsequent Engine stages per Engine Readiness Audit: lifecycle binding (partial paths, invalidation tables) → handoff binding (Stage 5) → engine system boundary (RT-G09 documentation closure).

Optional P3 hygiene (non-blocking): sync stale RUNTIME-ROADMAP acceptance checkbox per ERA-W05.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Physical location / format of tracking records | **NOT DEFINED** — RT-G04, RT-G10 FUTURE |
| Dashboard or CLI presenting tracking composition | **NOT DEFINED** — RT-G12 FUTURE |
| Calendar for Engine Stages 4–6 | **not scheduled** |
| Triumph production deploy vs tracking closure | **UNKNOWN** — external |
| Whether tracking composition maps 1:1 to future manifest | **requires RT-G10 charter** |

---

*Factory Project Tracking Model v1 — Stage 3 complete. Architecture only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Project Tracking Model v1

**Stage:** Factory Engine Architecture v1 — Stage 3 (Project Tracking Model)  
**Deliverable:** `FACTORY-PROJECT-TRACKING-MODEL-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-TRACKING-MODEL-v1.md` (created)  
**Summary:** Определена архитектура наблюдаемости Factory Project: tracking scope и boundaries (vs Runtime, Foundation, future systems), visibility tiers, правила state/gate/handoff/artefact visibility, audit trail principles, критерии full vs partial trackability; закрыты OQ-02 Stage 1 и OQ-S3 tracking aspects из Stage 2 — без storage, schemas, manifests, passports, UI.  
**Git:** no commit, no push (per task charter).
