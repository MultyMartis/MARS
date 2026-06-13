# REPORT — Factory Operational Model v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Operational Design — **Charter 01** (Factory Operational Model)  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 **COMPLETE**; Post-Engine Doctrine **COMPLETE** (Manifest, Registry, Tracking Surface charters); [WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md](WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md) **COMPLETE**  
**Тип:** operational design only — **без** runtime, automation, implementation, UI, storage, schemas  
**Не переопределяет:** Foundation, Engine Stages 1–6, Runtime vocabulary, Manifest/Registry/Tracking Surface charters  

---

## Purpose

### Операционное назначение Website Factory

**Website Factory** в операционном смысле — **производственная система документации и дисциплины** для выпуска коммерческих статических сайтов (Core 5 path и согласованные charter-исключения): от признания production case до Factory-terminal closure **через** принятую Foundation-цепочку и human-operated координацию Engine.

Factory **операционно** существует, чтобы:

| Производственная проблема | Как Factory решает (операционно) |
|---------------------------|----------------------------------|
| Разрозненные layer-контракты, Runtime-правила и workspace-артефакты без единой «нити» кейса | **Factory Project** + Engine composition + operator path (Manifest → Tracking → Surface) |
| Оператор не может быстро понять «где проект» и «что блокирует» | Декларативное движение по 14 Runtime states + gate/handoff indexes + observability doctrine |
| Риск подмены layer authority паспортом, дашбордом или папкой в git | Распределённая authority (T1–T5) + charters, запрещающие второй SoT |
| Необходимость воспроизводимого Core 5 production path без shipped orchestration | Methodology-first цепочка: classification → blueprints → … → `COMPLETE` с явными gates |

### Что Factory **не** решает операционно

| Вне scope | Почему |
|-----------|--------|
| Автоматическое исполнение переходов, валидаторов, handoff delivery | Human-operated v1; RT-G01, RT-G03, RT-G11 — **implementation NOT STARTED** |
| Хранение состояния в БД, manifest-файлы, центральный catalog на диске | RT-G04, RT-G10, RT-G05 **implementation** — doctrine only |
| Operator UI / dashboard / CLI как продукт Factory | RT-G12 display — **не** Tracking Surface charter |
| Frontend build, deploy, hosting, client go-live | Post-Factory / external; `COMPLETE` ≠ deploy |
| MIG, n8n, MetaBOT, ORCA, WPilot как **часть** Factory runtime | External orchestration — только charter-bound refs |
| Extended site types без blueprint parity | Architecture charter work — не блокер operational model для Core 5 pilot |
| Права доступа, RBAC, multi-tenant security model | **Не** в scope Charter 01 |

**Операционная граница (согласована с Engine):** Factory **начинается** при Factory-scoped recognition production case. Factory **заканчивается** на **декларации и наблюдаемости** Factory-track — до любого execution engine, persistence или application layer ([FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md)).

```text
  PRODUCTION INTENT (charter)
           │
           ▼
  ┌────────────────────┐
  │  WEBSITE FACTORY    │  coordination + observability + layer chain
  │  (operational)      │  human-operated declarations
  └─────────┬──────────┘
            │ produces refs + layer work
            ▼
  ┌────────────────────┐     ┌────────────────────┐
  │  FOUNDATION LAYERS  │     │  EXTERNAL WORK      │
  │  (artefact bodies)  │     │  workspace / deploy │
  └────────────────────┘     └────────────────────┘
```

---

## Foundation Dependencies

Operational Model **наследует** принятые артефакты **без их изменения**. При конфликте толкования — побеждает документ нижнего уровня в таблице (более специфичный charter/model), затем NEXT-PRIORITIES для global status.

### Tier 0 — Status and era closure

| Document | Operational use |
|----------|-----------------|
| [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) | Live register: Foundation/Engine/doctrine **COMPLETE**; workstream **Operational Design** |
| [WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md](WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md) | Doctrine vs implementation split (CHARTERED vs NOT STARTED) |
| [WEBSITE-FACTORY-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](WEBSITE-FACTORY-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) | Двухконтурность: reference v1 (канон) vs `projects/mars-website-factory/` (операционный пакет) |

### Tier 1 — Foundation Era (14 layers)

Принятая цепочка: Legal (+ Entity) → Site Type Registry → Blueprints → Page Architecture → Block Registry → Page Block Validation → SEO → Design → Content → Content Validation → Generation → Production QA → Runtime Architecture v1.

Factory **потребляет** layer contracts как **T1 authority** для производства артефактов; Factory **не** переопределяет FROZEN/ACCEPTED layer docs.

### Tier 2 — Factory Engine Architecture v1

| Stage | Document | Operational role |
|-------|----------|------------------|
| 1 | [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Что движется через Factory |
| 2 | [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Как занимает Runtime states |
| 3 | [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Как собирается observability |
| 4 | [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Что авторизует движение |
| 5 | [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | Полный lifecycle-нарратив |
| 6 | [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | Границы Engine; участие в production |

### Tier 3 — Post-Engine operational doctrine (charters)

| Charter | Document | Operational role |
|---------|----------|------------------|
| Manifest (RT-G10 doctrine) | [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Entry anchor, minimum understanding |
| Registry (RT-G05 doctrine) | [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Multi-project catalog, discoverability |
| Tracking Surface (RT-G12 doctrine) | [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Operator visibility contract |

### Tier 4 — Parallel operational corpus (не канон architecture)

| Corpus | Location | Rule |
|--------|----------|------|
| MARS Website Factory pack | `projects/mars-website-factory/` | Wave/Forge/Gulp runbooks — **применяет** канон, не supersede reference v1 без explicit routing |
| Reference workspaces | `workspaces/*` | Lane A implementation — **где** строится сайт, не **где** Factory SoT |

**Authority precedence:** Foundation Freeze + Engine + post-Engine charters → **этот Operational Model** для «как Factory работает как production system» → будущие operational playbooks (enrollment, registry card, surface workflow) **не могут** нарушать MA-*, MT-*, RA-*, TS-* principles.

---

## Operational Actors

Операционные **роли** (не permission model). Один человек может совмещать роли.

| Actor class | Operational function | Typical interaction with Factory |
|-------------|---------------------|----------------------------------|
| **Factory operator** | Ведёт Factory Project: charter, declarations, layer work coordination, gate sign-offs, tracking honesty | Primary actor; владеет human-operated v1 model |
| **Reviewer / validator** | HITL: проверяет layer outputs, подтверждает PASS/FAIL semantics, участвует в gate decisions | Invoked at Runtime stop points (LS-*) and layer gates — **не** отдельный Engine plane |
| **Charter author / sponsor** | Задаёт production intent, scope tier, declared endpoint, exclusions | Source of charter content indexed by Engine/Manifest |
| **Client / stakeholder** | Внешние требования, approvals, brand/legal constraints | **Вне** Factory indexes unless charter-bound ref; не Factory operator по умолчанию |
| **Layer specialist** | Производит artefact bodies (SEO spec, content pack, design mapping, legal input) | Works in layer workstreams; Factory holds **refs** only |
| **Frontend implementer** | Реализация в external workspace (`src/`, Gulp) | Post-Factory relative to architecture closure; handoff consumer |
| **External systems** | Git, CI, MIG, ORCA, MetaBOT, Cursor session, content packs | Execution surface — **не** Factory runtime; may supply refs (ERA-W03, ER-07) |

### Actor principles

| ID | Principle |
|----|-----------|
| **OA-ACT-01** | **Operator** — единственный носитель **обязательных** Factory declarations (state, gate PASS, handoff clearance) в v1 |
| **OA-ACT-02** | **Reviewer** не заменяет Runtime definitions — подтверждает соответствие layer criteria |
| **OA-ACT-03** | **Client** не является источником canonical state — только через charter amendments / explicit approvals as refs |
| **OA-ACT-04** | **External systems** не мутируют Engine indexes без operator-declared binding |

---

## Operational Flow

### Как работа **входит** в Factory

| Phase | What happens | Readiness |
|-------|--------------|-----------|
| **Pre-Factory** | Idea, client brief, raw workspace, MIG/incoming request | **Не** Factory-scoped |
| **Intake / recognition** | Operator признаёт **Factory-scoped** production case: identity shell, charter, scope tier | `NEW_PROJECT` doctrine; Object Model |
| **Manifest orientability** | Minimum understanding categories explicit (MRDY-*) | Manifest-ready |
| **Optional catalog enrollment** | Operator **declares** discoverability in portfolio | Registry-ready (RD-04: no auto-scan) |

**Work enters** через **явное Factory-scoped recognition + charter**, не через обнаружение папки в git alone (RD-04, RAP-10).

### Как работа **движется** в Factory

| Movement type | Mechanism | Owner |
|---------------|-----------|-------|
| **State occupancy** | Operator declares forward / rollback / re-entry per TR/RB rules | Engine state instance + Runtime vocabulary |
| **Layer production** | Specialists produce contracts, specs, validation runs | Foundation layers (T1 bodies) |
| **Authorization** | Gate sign-off (`RG-*` + mapped `GATE_*`) | Operator declaration → gate outcome index |
| **Boundary crossing** | Handoff clearance (`HO-*`) | Operator declaration → handoff event index |
| **Observation** | Tracking composition + Surface visibility classes | Engine + Surface charter |

**Movement is declared, not executed** by Factory as a product.

### Как работа **выходит** из Factory

| Exit kind | Operational meaning | Not equivalent to |
|-----------|---------------------|-------------------|
| **Factory terminal** | Active state `COMPLETE` + lifecycle at declared full-chain endpoint | Client deploy, DNS, hosting |
| **Partial charter closure** | `FACTORY_TRACK_CLOSED_PARTIAL` + endpoint short of full chain | «Almost done» без explicit charter |
| **Suspended track** | `FACTORY_TRACK_SUSPENDED` — pause in Factory scope | Cancelled project (may resume) |
| **Withdrawn from catalog** | Registry discoverability off; Engine history may remain | Deletion of layer artefacts |
| **Never Factory-scoped** | Stays external (raw repo, methodology-only session) | Registry entry |

```text
  ENTER                    MOVE                         EXIT
    │                        │                            │
    ▼                        ▼                            ▼
 Intake ──▶ Manifest ──▶ States+Gates+Layers ──▶ COMPLETE / partial / suspended
           (optional          (human declarations)         (Factory terminal)
            Registry)
```

---

## Project Movement Model

Операционная модель движения **использует** Engine + Runtime **без переопределения**.

### Unit of movement

**Один Factory Project** (Engine EO-05) движется по **фиксированному** набору из 14 Runtime state codes от `NEW_PROJECT` до `COMPLETE` (или по charter-masked subset).

### Movement planes (operational view)

| Plane | Operator sees | Factory does |
|-------|---------------|--------------|
| **State** | Active code + history + eligibility | Indexes instance; does not invent codes |
| **Lifecycle segment** | LC-* label aligned 1:1 with active state | Composes narrative (Stage 5) |
| **Gates** | PASS/FAIL/blocked/stale per `RG-*` | Indexes outcomes; does not evaluate criteria automatically |
| **Handoffs** | HO clearance at layer boundaries | Indexes events; does not deliver packages |
| **Legal parallel track** | RG-LEGAL / entity when scope requires | Co-tracks until Generation Ready window |

### Scope variants

| Scope tier | Movement effect |
|------------|-----------------|
| **FULL_SITE** (default) | Full chain to `COMPLETE` unless halted |
| **Partial / design-only / PHASE_SLICE** | LR-07 mask: EXCLUDED states; declared endpoint may precede `COMPLETE` |

### Operational movement rules (normative summary)

| ID | Rule |
|----|------|
| **OPM-01** | Forward transition requires **eligible** state + satisfied gates + cleared handoffs — operator **declares** when true |
| **OPM-02** | Halt (LS-*) = remain in current state until remediation — **не** новый state |
| **OPM-03** | Rollback invalidates stale gate/handoff indexes per Engine cascade — history **visible**, not erased |
| **OPM-04** | Re-entry requires fresh authorization — prior PASS may be STALE |
| **OPM-05** | Portfolio movement (another project) uses Registry — **не** смешивается с per-project Engine |

---

## Decision Model

### Классы решений

| Class | Required / optional | Who decides (v1) | Examples |
|-------|-------------------|------------------|----------|
| **A — Charter & scope** | **Required** at intake | Operator + sponsor input | Scope tier, exclusions, declared endpoint |
| **B — Factory-scoped recognition** | **Required** to start track | Operator | «This is a Factory Project» |
| **C — Classification & binding** | **Required** when entering applicable phases | Operator (+ specialist evidence) | `site_type_code`, `blueprint_ref` |
| **D — Layer artefact acceptance** | **Required** per layer gate | Operator/reviewer per layer criteria | Validation PASS, SEO approval |
| **E — Runtime gate sign-off** | **Required** at transitions | **Human operator** | `RG-*` PASS declaration |
| **F — Handoff clearance** | **Required** at HO boundaries | **Human operator** | HO-04…HO-13 clearance |
| **G — State transition declaration** | **Required** to move active state | **Human operator** | Forward to `SEO_READY` |
| **H — Rollback / re-entry** | **Required** when invoked | **Human operator** | RB path + cascade acknowledgment |
| **I — Catalog enrollment** | **Optional** | Operator | Add to Factory portfolio (Registry) |
| **J — Implementation tooling** | **Optional** | Operator | Cursor, Gulp, CI — external to Factory product |
| **K — Deploy / go-live** | **Outside Factory terminal** | Client/ops | Not a Factory state |

### Required vs optional (operational)

| Required for **valid Factory track** | Optional but valuable |
|--------------------------------------|------------------------|
| A, B, manifest-ready (MRDY-*) | I — Registry enrollment |
| C…H for each **applicable** state in scope mask | Physical manifest file (RT-G10 impl) |
| Declared endpoint explicit | Automated validator CLI |
| Append-only honesty on amendments (AT-01 analog) | Dashboard (RT-G12 impl) |

### Human-only decisions (v1 — non-negotiable in this model)

- Active state change  
- `RG-*` outcome declaration  
- Handoff clearance  
- Charter/scope amendment affecting LR-07 mask  
- Registry discoverability enrollment / withdrawal  
- Reconciliation when Surface/Tracking shows integrity violation (SV-05, MS-02)

**Optional automation** (future) **не** меняет ownership — только implementation charters (RT-G01, RT-G11).

---

## Artifact Production Model

Factory **координирует производство**; **владеет телами** только через layer authority, не через Engine.

### Artifact classes

| Class | Produced by | Factory holds | Operator uses for |
|-------|-------------|---------------|-------------------|
| **Layer contracts & specs** | Layer workstreams (T1) | Ref + link | Gate criteria source |
| **Validation runs / reports** | Layer validation | Ref in tracking | Evidence for gate D |
| **PAGE-CONTRACT, blueprint bindings** | Page Architecture / Blueprints | Ref index | IA truth |
| **Content / design / SEO packs** | Respective layers | Ref index | Phase completion |
| **Generation outputs / handoff packages** | Generation Contracts | Package **ref**; body in layer | HO boundaries |
| **Gate / handoff declaration records** | Operator via Engine | Instance indexes | Movement authorization |
| **Charter & scope documents** | Operator-authored | Indexed refs | Scope mask, endpoint |
| **Frontend implementation** | External workspace | External pointer (optional) | Post-Factory build |
| **Operational reports (REPORT)** | Operator/session discipline | External unless charter-bound | Session evidence — not Engine SoT |

### Production flow (operational, not implementation)

```text
  Charter defines scope
        │
        ▼
  Layer specialists produce bodies ──▶ T1 authority validates semantics
        │
        ▼
  Operator declares gate PASS + handoff clearance
        │
        ▼
  Engine indexes refs + outcomes (not bodies)
        │
        ▼
  At GENERATION_READY+: scope freeze / generation_id visible
        │
        ▼
  FRONTEND_READY → external workspace consumes handoff
        │
        ▼
  COMPLETE (Factory) ──▶ deploy is separate workstream
```

### Principles

| ID | Principle |
|----|-----------|
| **OAP-01** | Factory **indexes**, layers **own** artefact bodies (EO-02) |
| **OAP-02** | Gate PASS **не** заменяет наличие layer artefact — оба нужны операционно |
| **OAP-03** | Global layer ACCEPTED (T5) **≠** per-project gate PASS (T4) |

---

## Operational Visibility Model

Как **Registry, Manifest и Surface** поддерживают операции **без redesign** charters.

### Operator path (normative)

```text
  Portfolio (optional)          Per-project entry              Operational depth
        │                              │                              │
        ▼                              ▼                              ▼
   REGISTRY                      MANIFEST                      TRACKING
   «какие проекты?»              «что это? с чего начать?»      «где сейчас? что прошло?»
   catalog / distinction         minimum understanding          composition + indexes
        │                              │                              │
        └────────────── select one project ──────────────────────────┘
                                       │
                                       ▼
                              TRACKING SURFACE
                              «что оператор должен ВИДЕТЬ?»
                              eight questions · S-A/B/C tiers
```

### Role separation (operational)

| Surface | Answers | Does not replace |
|---------|---------|------------------|
| **Registry** | Which Factory projects exist; how to tell them apart | Manifest depth; Tracking seven questions |
| **Manifest** | What is this project; where truths live (topology) | Live gate index (MT-01) |
| **Tracking (Engine)** | Composition rules; instance indexes; audit trail | Layer criteria text |
| **Tracking Surface** | Visibility contract for eight questions | UI, storage, gate definitions |

### When operator uses which

| Situation | Start here |
|-----------|------------|
| New session, unknown project | Registry (if portfolio) → Manifest |
| Known project, need blockers | Tracking composition → Surface classes |
| Intake only, early `NEW_PROJECT` | Manifest (MRDY-*) — may be manifest-ready but not surface-ready |
| Multi-project prioritization | Registry summaries — **then** per-project path (RE-01) |

### Freshness

- **Authoritative** = last **operator-declared** truth (EO-03, VP-03)  
- Registry orientation snapshot = **non-authoritative** unless reconciled (RS-03)  
- Surface must flag invalid active state (VP-04, SRDY-02)

---

## Completion Model

### Что операционно считается завершением Factory-track

| Completion type | Operational criteria | Engine / Runtime anchor |
|-----------------|---------------------|-------------------------|
| **Full Factory completion** | Declared full-chain endpoint reached; active `COMPLETE`; `RG-PROJECT_COMPLETE` / HO-13 satisfied per declarations | Terminal state Stage 2; LC-13 |
| **Partial Factory completion** | Charter endpoint reached short of full chain; `FACTORY_TRACK_CLOSED_PARTIAL` visible | LCMP-5; OQ-S6-09 operational detail OPEN |
| **Gate-complete (mid-track)** | Authorization through declared endpoint — **not** necessarily `COMPLETE` | GCO-* Stage 4 |
| **Lifecycle-complete narrative** | Composition says endpoint reached | Stage 5 — **not** deploy |

### Explicit non-completion

| Condition | Meaning |
|-----------|---------|
| Deployed to production | **Post-Factory** — may occur before or after Factory `COMPLETE` |
| Frontend build green in CI | Implementation — does not auto-declare `FRONTEND_READY` |
| All layer docs ACCEPTED globally (T5) | Global register — not per-project |
| Manifest file exists on disk | **Implementation** — not required for doctrine closure |

### Completion principles

| ID | Principle |
|----|-----------|
| **OCM-01** | Factory completion = **movement + authorization** closure in scope — not client happiness metric alone |
| **OCM-02** | Operator must **declare** terminal transition to `COMPLETE` — no auto-complete |
| **OCM-03** | Partial closure **must** be charter-explicit — implicit ambiguity = manifest-incomplete (MRDY-03) |
| **OCM-04** | COMPLETE project may remain in Registry as **archived** discoverable category |

---

## Operational Boundaries

### Включено в Factory operations

| Included | Statement |
|----------|-----------|
| Factory-scoped project coordination | One logical Factory Project per production case |
| Human-operated state/gate/handoff declarations | v1 operating reality |
| Layer chain application for in-scope states | Core 5 default path |
| Distributed authority with Engine indexes | No merged mega-document |
| Manifest / Registry / Surface **doctrine** application | Entry, portfolio, visibility |
| Parallel legal track when scope demands | Co-track through Generation window |
| Reference to external workspace for implementation | Pointer only |
| Session discipline (REPORT, explicit git) | Operational honesty — parallel corpus |

### Явно исключено из Factory operations

| Excluded | Statement |
|----------|-----------|
| Shipped Factory runtime / workflow engine in repo | **EXCLUDED** — Phase 1 honesty |
| Autonomous agents executing transitions | RT-G03, RT-G11 FUTURE |
| Persistence, state store, manifest JSON on disk as product | RT-G04, RT-G10 impl |
| Operator dashboard as Factory deliverable | RT-G12 impl |
| n8n workflows, MIG execution semantics | External |
| Redesign Foundation/Engine/Runtime | Forbidden |
| Site Type Registry operations confused with Factory Project Registry | RAP-11 |
| Passport, second tracking SoT, Manifest-as-gate-index | MAP-*, MT-01, BV-15 |
| Parallel canonical business registry (org/person/website/project/relationship) | ADOPT-01; ATLAS consumer contract |

### ATLAS terminology guards (TG-ATLAS)

Website Factory is an **ATLAS consumer** per [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md). Operator **must not** conflate:

| Factory term | ATLAS term | Guard |
|--------------|------------|-------|
| **Factory Project** | **ATLAS Project** (`PRJ-*`) | Different entities — production case vs structural initiative |
| **Factory Registry** (ROC portfolio) | **ATLAS Business Reality Registry** | Different domains — Factory Projects vs business entities |
| **Factory Identity** (identity shell) | **ATLAS Identity** (`ORG-*`, `PER-*`, …) | Different authority — production shell vs canonical business facts |

| ID | Principle |
|----|-----------|
| **TG-ATLAS-01** | Homonyms require explicit disambiguation in charter, manifest, and enrollment |
| **TG-ATLAS-02** | ATLAS owns canonical business reality; Factory consumes as **refs** — never parallel registry |

### Dual corpus boundary

| Corpus | Role |
|--------|------|
| `workspaces/website-factory-reference-v1/` | **Canonical** architecture + this operational model |
| `projects/mars-website-factory/` | **Operational pack** (Forge, Wave, v0 registries) — applies canon; v0 IDs must not mix with v1 without routing |

---

## Operational Readiness

### Operationally usable (можно вести production по модели)

Factory считается **operationally usable** для оператора, когда:

| # | Criterion | ID |
|---|-----------|-----|
| 1 | Foundation 14 layers + Runtime **ACCEPTED/FROZEN** for intended site class | **OR-01** |
| 2 | Operator understands human-operated declaration model | **OR-02** |
| 3 | Factory-scoped intake can reach **manifest-ready** (MRDY-*) | **OR-03** |
| 4 | Per-project path Manifest → Tracking → Surface is followed | **OR-04** |
| 5 | Engine participates via **declarations + indexes**, not expected automation | **OR-05** |
| 6 | Core 5 classification and blueprints match project scope | **OR-06** |
| 7 | Governance registers read for status (NEXT-PRIORITIES), not stale «Engine NOT QUEUED» | **OR-07** |

**Typical usable moment:** pilot LANDING/CORPORATE with operator + Cursor + layer docs + external workspace — **без** physical manifest/registry files.

### Operationally incomplete (система как production **ещё не закрыта**)

| Gap | Signal |
|-----|--------|
| No Factory-scoped charter at intake | Cannot start valid track |
| Operator treats folder/git as Registry enrollment (RAP-10) | Integrity violation |
| Expectation of autonomous Factory runtime in repo | Misread of Phase 1 |
| Extended site type without blueprint | Architecture gap — track invalid for that class |
| Physical manifest/registry/UI **required** by operator but not authorized | Implementation plane NOT STARTED — not operational model gap |
| Missing playbooks: enrollment, registry card, surface workflow | **Operational Design** successors — Charter 01 defines model only |

### Readiness relationships

| Concept | Meaning |
|---------|---------|
| **Architecture doctrine complete** | Foundation + Engine + post-Engine charters |
| **Operational model complete** | This document — **how** Factory runs |
| **Operational playbooks complete** | **FUTURE** charters (enrollment, card template, surface workflow) |
| **Implementation complete** | RT-G04/05/10/12, RT-G01, RT-G11 — **NOT STARTED** |

**OR-03 ⊄ implementation:** manifest-ready is **doctrinal**, not «file exists».

---

## Explicit Non-Claims

This document and Factory Operational Model v1:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** automation, agent systems, n8n workflows, or implementation plans;
- **are not** UI, dashboard, CLI, storage, database, or serialization specifications;
- **do not** redefine Foundation Era, Engine Stages 1–6, Runtime states/`RG-*`/`HO-*`, or Manifest/Registry/Tracking Surface charters;
- **do not** claim physical manifest, registry index, or operator UI exists in-repo;
- **do not** claim `projects/mars-website-factory/` is superseded by this file;
- **do not** define permissions, RBAC, or security architecture;
- **do not** authorize deploy or client go-live by Factory `COMPLETE`.

Human-operated production remains the v1 operating reality per [runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md).

---

## Open Questions

Bounded for **future operational charters** — not resolved in Charter 01.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-OM01** | Canonical repo path for de-facto manifest/registry if operators already use ad-hoc files | **OPEN** — implementation / playbook |
| **OQ-OM02** | Manifest enrollment playbook steps (physical vs doctrinal only) | **OPEN** — Charter 02+ recommended |
| **OQ-OM03** | Registry index card template fields | **OPEN** — OQ-R02 |
| **OQ-OM04** | Tracking surface daily workflow (session checklist) | **OPEN** — OQ-TS01, display charter |
| **OQ-OM05** | Partial closure operator playbook (`FACTORY_TRACK_CLOSED_PARTIAL`) | **OPEN** — OQ-S6-09 |
| **OQ-OM06** | v0 ↔ v1 routing card for agents using mars-website-factory pack | **OPEN** — operational hygiene |
| **OQ-OM07** | Triumph / pilot workspaces: catalog vs external-only | **SAFE UNKNOWN** per case charter |
| **OQ-OM08** | MIG incoming request → Factory intake binding | **OPEN** — RT-G08 |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **Factory Operational Model v1** as Charter 01 **complete** — answers «how Factory operates» without implementation.
2. **Operational Design continuation (class B charters, separate tasks):**
   - Manifest enrollment playbook (RT-G10 operational binding)
   - Registry catalog card template (RT-G05 operational binding)
   - Tracking surface operator workflow (RT-G12 operational binding)
3. **Do not start:** runtime plans, storage schemas, dashboard specs, n8n, or Engine v2 — unless explicitly authorized.
4. **Hygiene:** When adding playbooks, update NEXT-PRIORITIES in same change window (governance sync lesson).
5. **Optional P3:** Link this document from NEXT-PRIORITIES Operational Design row — operator action, outside deliverable scope.

**Engine Architecture v1 requires no further stages.** Operational Model **sits above** implementation plane, **below** operator playbooks.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether operators already run a de-facto manifest/registry discipline | **UNKNOWN** — no canonical physical artefact |
| Calendar for RT-G04/10/05/12 implementation charters | **not scheduled** |
| Auto-sync display from Tracking | **BOUNDED** — non-authoritative only (OQ-TS07) |
| Full repo-wide single entry for Website Factory sessions | **UNKNOWN** — dual corpus (reference v1 vs mars-website-factory) |

---

*Factory Operational Model v1 — Operational Design Charter 01. Canonical location: `workspaces/website-factory-reference-v1/`. Git: no commit, no push.*

---

# REPORT — Factory Operational Model v1

**Stage:** Operational Design — Charter 01 (Factory Operational Model)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-OPERATIONAL-MODEL-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-OPERATIONAL-MODEL-v1.md` (created)  
**Summary:** Определена операционная модель Website Factory как human-operated production system: назначение и границы, акторы, поток входа/движения/выхода, модель движения проекта через Engine/Runtime, классы решений, производство артефактов, visibility path Registry→Manifest→Tracking→Surface, модель завершения без переопределения `COMPLETE`, operational readiness usable vs incomplete — без runtime, automation, implementation, UI, storage.  
**Git:** no commit, no push (per task charter).
