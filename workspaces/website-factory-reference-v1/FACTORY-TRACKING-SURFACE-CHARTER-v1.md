# REPORT — Factory Tracking Surface Charter v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Post–Factory Engine Architecture v1 — **RT-G12 charter only**  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 Stages 1–6 **COMPLETE**; [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) (RT-G10) **COMPLETE**; [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) (RT-G05) **COMPLETE**  
**Тип:** charter only — **без** implementation, runtime, storage format, schemas, field lists, files, UI, layouts, widgets, screens  
**Связь:** [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md), [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G12

---

## Purpose

### Зачем существует Factory Tracking Surface

**Factory Tracking Surface** — архитектурная **доктрина операторской наблюдаемости** для **одного** Factory Project. Surface отвечает: **какие классы информации** оператор **обязан иметь возможность увидеть**, чтобы понять production case **без** археологии по всему workspace — **независимо** от того, реализован ли dashboard, CLI, файл или только логическая композиция Engine.

| Проблема оператора | Как Surface решает |
|--------------------|-------------------|
| Истина распределена по Engine planes, Runtime и layer workstreams | Surface **агрегирует видимость по классам**, не по файлам — «что показать», не «где хранить» |
| После Manifest оператору нужен **операционный срез**, а не только entry doctrine | Surface **charterит** полноту observability поверх Tracking composition |
| Tracking Model определяет **зоны и tiers**, но не operator path целиком | Surface **связывает** tiers с восемью operator questions RT-G12 |
| Риск подмены Tracking Surface dashboard’ом или storage | Surface **явно** отделяет doctrine видимости от UI и persistence |

### Operator questions (нормативный scope Surface)

Surface существует, чтобы оператор мог ответить **без открытия всего workspace**:

| # | Вопрос | Surface information class |
|---|--------|---------------------------|
| 1 | **Что это за проект?** | Project orientation (identity, charter, scope — **не** дублируя Manifest doctrine) |
| 2 | **Где он сейчас?** | Current position (active state, active segment, halt/suspension) |
| 3 | **Что заблокировано?** | Blocking picture (open gates, handoff blocks, eligibility, LS halt) |
| 4 | **Что завершено?** | Completion picture (completed states/segments, satisfied gates, cleared handoffs) |
| 5 | **Что остаётся?** | Remaining work (to declared endpoint: gaps, open gates, artefact refs) |
| 6 | **Что произошло недавно?** | Recent narrative (progression ledger tail, declarations, invalidations) |
| 7 | **Что должно произойти дальше?** | Forward eligibility (next segment, blocking set — **derived**, not prescribed automation) |

Восьмой вопрос расширяет семь вопросов [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) явным **event / recency** срезом — без определения хранилища событий.

### Что Surface **не** решает

| Проблема | Куда относится |
|----------|----------------|
| Минимальное понимание и entry anchor «с чего начать» | [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) |
| Перечень всех Factory projects в портфеле | [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) |
| Владение instance records, composition rules, visibility tiers | [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) (Stage 3) |
| Gate sufficiency, namespace mapping, stale semantics | [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) |
| Lifecycle segmentation, rollback cascade, partial closure | [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) |
| Критерии pass/fail, gate definitions, transition legality | Runtime + Foundation layers |
| Физическое отображение (экраны, панели, виджеты) | **Запрещено** в этом charter — future display charter only |
| Persistence, serialization, automation | RT-G04, RT-G10 implementation, RT-G01, RT-G11 |

**Tracking Surface — charter роли наблюдаемости, не продукт, не экран, не движок.**

---

## Foundation Dependencies

Tracking Surface Charter **наследует** завершённый Engine v1, Manifest и Registry doctrine; **не изменяет** Foundation, Runtime или Engine Stages 1–6.

### Tier 1 — Engine + post-Engine charters (обязательные)

| Document | Surface использует |
|----------|-------------------|
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking zones, Tier A/B/C, seven questions, TC-* trackability — **источник composition** |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Entry path, MT-01, minimum understanding — **граница** vs Surface |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Portfolio path, RE-01 — Surface **per-project only** |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | Lifecycle visibility content (Stage 5 §Lifecycle Visibility) |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Gate visibility boundaries — **не** Gate Results System |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | EO-*, ER-05, ES-04, Allowed Future Documents (Tracking Surface spec) |

### Tier 2 — Engine stages (reference)

| Document | Role |
|----------|------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Identity shell, mandatory components — orientation classes |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | SV-*, SHV-* — state visibility rules Surface **charters for operators** |

### Tier 3 — Runtime + Foundation (reference only)

Runtime Architecture v1; принятая 14-layer Foundation chain. Surface **не** переопределяет layer contracts.

**Authority precedence:** Foundation Freeze + Engine Readiness Audit → Engine Stages 1–6 → Manifest (RT-G10) → Registry (RT-G05) → **этот charter** для роли Tracking Surface → **будущий** display/storage implementation **не может** нарушить MT-01, TV-01, GV-01, RA-05.

---

## Tracking Surface Position

```text
  OPERATOR (one Factory Project)
       │
       ▼
  ┌─────────────┐     portfolio only — RE-01
  │  REGISTRY   │     «Which projects exist?»
  └──────┬──────┘
         │ select one
         ▼
  ┌─────────────┐     entry — MR-01, MRDY-*
  │  MANIFEST   │     «What is this? Where truths live?»
  └──────┬──────┘
         │ operational depth
         ▼
  ┌─────────────┐     composition — Stage 3 owns rules
  │  TRACKING   │     indexes · tiers · audit trail
  │  (Engine)   │
  └──────┬──────┘
         │ visibility doctrine (this charter)
         ▼
  ┌─────────────┐     «What must operator SEE?»
  │  TRACKING     │     eight questions · info classes
  │  SURFACE      │     NOT UI · NOT storage
  │  (charter)    │
  └─────────────┘
         │ future only
         ▼
  ┌─────────────┐     display binding — separate charter
  │  UI / CLI   │     may render Surface classes
  └─────────────┘
```

### Позиция относительно соседних ролей

| Neighbor | Relationship |
|----------|--------------|
| **Registry** | Registry **указывает** на Manifest; Surface **не** в portfolio view. RE-01: seven/eight questions **never** primary on Registry card |
| **Manifest** | Manifest **предшествует** Surface; Surface **углубляет** observability **без** дублирования Categories 1–5 Manifest scope (MAP-05) |
| **Tracking Model** | Tracking **владеет** composition semantics; Surface **charterит** operator-facing **visibility contract** поверх тех же zones |
| **Lifecycle Composition** | Lifecycle **владеет** narrative rules; Surface **экспонирует** lifecycle **information classes** (LC label, endpoint, segment history) |
| **Factory Project** | Surface наблюдает **один** logical Factory Project — EO-05 |
| **Runtime** | Surface показывает **instance values** Runtime vocabulary — **не** definitions |

### Principle TS-01 — Surface is visibility doctrine, not a system

Tracking Surface **не** создаёт tracking engine, recorder, storage или application. Surface **определяет**, какие **классы информации** должны быть **доступны оператору** при потреблении Engine tracking composition.

### Principle TS-02 — Surface follows Tracking, Manifest precedes Surface

Operator path: **Registry (optional) → Manifest → Tracking composition → Surface visibility contract**. Surface **не** может опережать manifest-ready без потери orientability (RD-02 analog at depth).

### Principle TS-03 — Surface points, never merges authority

TV-01 / ER-05: Surface visibility **ссылается** на authoritative sources — **не становится** Legal Pack, Site Type Registry, Runtime doc или live gate criteria.

---

## Visibility Principles

Visibility — **классы информации**, не widgets, panels или layout regions.

### Tier S-A — Must always be visible on Surface

Information без которой Surface **не выполняет** charter для **этого** Factory Project:

| Information class | Source zone (Tracking Model) | Operator question served |
|-------------------|------------------------------|--------------------------|
| Stable project identity reference | Identity shell | #1 (orientation anchor) |
| Charter / scope tier (summary) | Charter & scope refs | #1, #5 |
| Active `runtime_state_code` (exactly one) | Current state reference | #2 |
| Active lifecycle segment label (LC-*) | Derived from Runtime binding | #2 |
| Scope applicability mask (or full-chain default) | Scope state mask | #1, #5 |
| Declared lifecycle endpoint | Charter + Lifecycle LCMP-5 | #5, #7 |
| Blocking summary (at least first open blocker) | Eligibility snapshot | #3, #7 |
| Index **presence** for gates, handoffs, artefacts | Structure exists | #4, #5 (may be empty early) |
| Last declaration recency marker (logical) | Audit trail tail | #6 |

### Tier S-B — Conditionally visible on Surface

| Information class | When visible | Operator question served |
|-------------------|--------------|----------------------------|
| `site_type_code`, blueprint ref | From `CLASSIFIED` / `BLUEPRINT_READY` | #1, #4 |
| Per-route / per-phase artefact ref summaries | From corresponding LC phase | #4, #5 |
| `generation_id`, scope freeze marker | From `GENERATION_READY` | #4, #5 |
| Parallel legal co-track status | When scope requires legal track | #3, #5 |
| Gate outcome detail beyond first blocker | When operator drills (any medium) | #3, #4 |
| Handoff event sequence summary | When handoffs declared | #4, #6 |
| Progression ledger recent events (bounded window) | When any transition recorded | #6, #7 |
| `FACTORY_TRACK_SUSPENDED` | When charter suspends track | #2, #7 |
| `FACTORY_TRACK_CLOSED_PARTIAL` | When partial endpoint reached | #4, #5 |
| Foundation version pins | When charter pins | #1 (audit context) |
| External workspace pointer (ERA-W03) | Charter-declared only | #1 (ref class) |

### Tier S-C — Must never belong on Tracking Surface

| Information class | Why excluded | Actual owner |
|-------------------|--------------|--------------|
| Gate pass/fail **criteria** and failure library text | Definitions — not observation | RUNTIME-GATES, layer docs |
| Handoff package **payload bodies** | Package data — ref only | Generation Outputs / layers |
| Layer contract **full bodies** (Legal Pack templates, matrices) | T1 class authority | Foundation layers |
| Frontend source, CI logs, deploy status | Post-Factory | External workstreams |
| Agent prompts, chat, MIG transcripts | Non-canonical | External |
| Queue rank among projects | Not per-project Surface | RT-G06 |
| Automated predicted dates, ML inference | Not in v1 model | — |
| Registry catalog membership for **other** projects | Portfolio scope | Registry charter |
| Manifest reference topology **full map** as Surface core | Manifest Category 7 — entry depth | Manifest charter |
| Duplicate live gate/handoff index as «second Surface SoT» | MAP-05 / MT-01 violation | Tracking only |

### Visibility composition principles

| ID | Principle |
|----|-----------|
| **VP-01** | Surface = Tier S-A + available Tier S-B composed from Tracking zones **without merging authority** |
| **VP-02** | Stale / superseded / invalidated markers **remain visible** (TV-02) — Surface **не** скрывает rollback narrative |
| **VP-03** | Surface reflects **last declared truth** (EO-03) — freshness = declaration chain, not filesystem mtime |
| **VP-04** | Surface **не** нормализует** invalid active state (SV-05) — must flag |
| **VP-05** | Portfolio glance from Registry **не заменяет** Surface — RS-03 analog |

---

## Project Orientation Principles

Project orientation — **минимальный операционный контекст** на Surface **без** дублирования Manifest.

### What Surface must expose (orientation classes)

| Class | Manifest overlap | Surface rule |
|-------|------------------|--------------|
| Identity reference (recognize production case) | Category 1 | **Required** — same fact, Surface **не** расширяет identity semantics |
| Charter intent summary + scope tier | Category 2 | **Required** — operational label, not full charter text |
| Declared endpoint + partial/full | Category 3 | **Required** |
| Scope applicability (full / EXCLUDED path) | Category 4 | **Required** |
| Classification / blueprint binding **when present** | Category 5 | **Conditional** Tier S-B |
| «Where authoritative truths live» | Category 7 (topology) | **Pointer only** — Manifest owns map; Surface **may repeat one-line pointer**, not full topology essay |

### What Surface must not duplicate from Manifest

| Excluded on Surface | Why |
|-------------------|-----|
| Full minimum understanding contract restatement | Manifest MRDY-* already satisfied at entry |
| Manifest entry anchor identification ritual | Manifest MRDY-06 — once at entry |
| Stability expectations essay (ST-*) | Manifest doctrine — Surface consumes outcome |
| Registry vs Passport distinction teaching | Manifest MRDY-07 / Registry RRDY-06 — onboarding, not daily Surface |

### Principles

| ID | Principle |
|----|-----------|
| **PO-01** | Surface answers «what project is this **in operation**?» — Manifest answers «what project is this **at entry**?» |
| **PO-02** | Surface **never** embeds layer artefact bodies as orientation (AV-01) |
| **PO-03** | Surface orientation **must** stay consistent with Engine identity shell (MS-02 analog) |
| **PO-04** | Extended types (ER-01) may show orientation **incomplete** flag — not hidden |

---

## State Visibility Principles

State visibility на Surface **реализует** Stage 2/3 rules для оператора — **не** новую state semantics.

### Must expose (state classes)

| Class | Rules | Questions |
|-------|-------|-----------|
| Current active state (single code) | SV-01 | #2 |
| LC phase / segment for active state | SV-02 | #2 |
| Halt at current state (LS-*) | SV-03 | #3 |
| Terminal `COMPLETE` closure | SV-04 | #4 |
| Invalid active flag | SV-05 | #3 |
| Completed state occupancy list | SHV-01 | #4 |
| Progression ledger (forward / rollback events) | SHV-02 | #6 |
| Superseded segments after rollback | SHV-03 | #4, #6 |
| Re-entry segments (linked) | SHV-04 | #6 |
| EXCLUDED / N_A in mask | SHV-05 | #5 |
| Eligibility snapshot (blocking / next) | Derived | #3, #5, #7 |

### Belongs elsewhere (not primary on Surface)

| Class | Owner |
|-------|-------|
| TR/FT/DR/RB rule **text** | STATE-TRANSITION-RULES |
| Intra-state work without transition | Gates / artefact refs (SHV-06) |
| Full progression archive unbounded | Audit proportionality AT-04 — Surface shows **recent window** Tier S-B |

### Principles

| ID | Principle |
|----|-----------|
| **STV-01** | «Where now?» = active code + LC label + halt/suspension annotation — **not** synthetic sub-states |
| **STV-02** | «What completed?» = history occupancy — **not** gate criteria |
| **STV-03** | Surface **не** записывает transitions — только **показывает** declared ledger |

---

## Gate Visibility Principles

Gate visibility — **instance observation** — **не** Gate Results System (Stage 4 non-claim).

### Must expose (gate classes)

| Class | Rules | Questions |
|-------|-------|-----------|
| Outcome per `RG-*` (PASS/FAIL/blocked/stale) | GV-01 | #3, #4 |
| First / primary open blocking gate | GV-02 | #3, #7 |
| FAIL outcomes (remain visible) | GV-03 | #3, #6 |
| Composite rollup status + constituent refs | GV-04 | #3, #4 |
| Stale after rollback (not erased) | GV-05 | #4, #6 |
| Active gate set relative to active state | Stage 4 | #3, #7 |
| Parallel legal gate status when in window | GC-03 | #3 |

### Must not expose on Surface

| Class | Owner |
|-------|-------|
| Gate definitions, inputs, criteria | RUNTIME-GATES, layer *-GATES-v1 |
| Failure remediation playbooks | RUNTIME-FAILURE-LIBRARY |
| Namespace mapping table as authoritative doc | Gate Composition Model — ref link only |
| Automated evaluation narrative | RT-G11 FUTURE |

### Principles

| ID | Principle |
|----|-----------|
| **GV-01** | Surface shows **that** gate passed/failed — **not why** criteria met (layer artefact for why) |
| **GV-02** | Surface **не** becomes gate evaluator |
| **GV-03** | «What blocks?» cites gate class + HO block + LS halt — **composed**, not new state code |

---

## Lifecycle Visibility Principles

Lifecycle visibility — **composed narrative classes** from Stage 5 — Surface **не владеет** lifecycle.

### Must expose (lifecycle classes)

| Class | Tier | Questions |
|-------|------|-----------|
| Lifecycle origin (intake / identity entry) | S-A | #1, #6 |
| Active segment (LC-*) | S-A | #2 |
| Segment history (COMPLETED / SUPERSEDED / N_A) | S-A | #4 |
| Declared endpoint | S-A | #5, #7 |
| Progress relative to endpoint | S-B | #5 |
| Parallel legal co-track | S-B | #3, #5 |
| Rollback / re-entry markers | S-A | #6 |
| Halt context (LS-*) at segment | S-A | #3 |
| Next segment eligibility | S-B | #7 |
| Partial / suspended closure flags | S-B | #4, #5 |

### Must not expose as lifecycle authority

| Class | Why |
|-------|-----|
| Invented micro-segments (`SEO_IN_PROGRESS`) | ERA-W07 |
| Layer contract bodies | T1 |
| Handoff package payloads | Package data |
| Predicted completion dates | Not v1 |
| LC phase **definitions** full text | PROJECT-LIFECYCLE — link only |

### Principles

| ID | Principle |
|----|-----------|
| **LV-01** | Surface **не** executes segment transitions (LCMP-1) |
| **LV-02** | «What remains?» = segments/gates/artefacts **to declared endpoint** (LPC-03) |
| **LV-03** | `COMPLETE` on Surface = Factory terminal — **≠** deploy go-live (BV-09) |

---

## Event Visibility Principles

Event visibility — **исторический и недавний срез** без определения storage.

### Belongs on Surface (event classes)

| Event class | Purpose | Questions |
|-------------|---------|-----------|
| State transition declarations (forward / rollback) | Movement narrative | #6 |
| Gate outcome sign-offs | Authorization changes | #6 |
| Handoff clearance / supersession | Boundary crossings | #6 |
| Scope mask / charter amendments affecting track | LR-07 visibility | #6 |
| Invalidation markers (stale / invalidated / superseded) | Rollback honesty | #6 |
| Correction records (`corrects_declaration_id`) | No silent delete | #6 |
| Recent bounded window (logical «last N» or «since last visit» — **implementation OPEN**) | Recency | #6 |

### Belongs elsewhere (may link, not Surface core)

| Event class | Owner |
|-------------|-------|
| Validation run detailed logs | Layer workstreams |
| Legal generation audit | Legal Pack workflow |
| Git commit history | Workspace tooling |
| Global layer ACCEPTED changes | NEXT-PRIORITIES T5 |
| MIG / agent session transcripts | External |

### Principles

| ID | Principle |
|----|-----------|
| **EV-01** | Surface events = **Factory movement declarations** — not full workspace telemetry (AT-04) |
| **EV-02** | Append-only narrative — superseded **visible**, not deleted (AT-05, LCC-06) |
| **EV-03** | «What happened recently?» **не** implies automated event ingestion in v1 (AT-02) |
| **EV-04** | Archival depth beyond recent window — **optional** Tier S-B drill-down, not S-A requirement |

---

## Operator Actionability Principles

Surface различает информацию, **включающую решения**, и **архивную**.

### Actionable information classes

| Class | Enables operator to… |
|-------|----------------------|
| Active state + halt / suspension | Decide remain in segment vs escalate |
| Primary open blocker (gate / HO / legal) | Decide remediation target |
| Eligibility snapshot (next transition legal?) | Decide whether to **declare** forward |
| Artefact gap at current state | Decide declare ref vs rollback |
| Stale gate after rollback | Decide reconcile before re-forward |
| Declared endpoint vs current position | Decide scope complete vs continue |
| Integrity warnings (ledger ≠ active) | Decide reconciliation declaration |
| Recent rollback / invalidation | Decide re-entry path |

### Archival / contextual (supports judgment, not immediate action)

| Class | Role |
|-------|------|
| Full superseded segment history | Audit narrative |
| Historical PASS marked STALE | Proof of prior work |
| Old handoff SUPERSEDED events | Traceability |
| Foundation version pin | Contract audit |
| Classification label at intake | Context |

### Non-actionable on Surface (do not pretend operational)

| Class | Why |
|-------|-----|
| Gate criteria text | Read layer doc — not decide on Surface alone |
| Global layer ACCEPTED status | T5 — not per-project action |
| Queue rank | RT-G06 |
| Deploy / hosting status | Post-Factory |

### Principles

| ID | Principle |
|----|-----------|
| **OA-01** | Surface **enables** human declaration — **не** substitutes automation |
| **OA-02** | Actionable **must** be visually/logically **prioritized** over archival in any future display — **without** defining layout |
| **OA-03** | Blocked project may be **fully surface-ready** — readiness ≠ unblocked |

---

## Surface Completeness

Completeness — **качество observability doctrine**, не production readiness.

### Surface-ready

Factory Project is **surface-ready** when operator can answer **all eight** RT-G12 questions from Surface information classes alone, with **only follow refs** to authoritative bodies — **without** workspace-wide search.

| # | Criterion | ID |
|---|-----------|-----|
| 1 | Tier S-A classes **present or explicitly empty-allowed** (early intake indexes) | **SRDY-01** |
| 2 | Valid active state (or invalid flagged) | **SRDY-02** |
| 3 | Declared endpoint explicit | **SRDY-03** |
| 4 | Blocking summary derivable (may be «none» if eligible) | **SRDY-04** |
| 5 | Completion picture derivable for reached prefix | **SRDY-05** |
| 6 | Remaining picture derivable to endpoint | **SRDY-06** |
| 7 | Recent event window non-empty **or** «no declarations yet» explicit | **SRDY-07** |
| 8 | Forward picture derivable (eligible next or blocked with cause) | **SRDY-08** |
| 9 | No Surface/Manifest tracking duplication violation (MAP-05) | **SRDY-09** |

**Typical surface-ready:** same moments as **fully trackable** (TC-01…TC-07) — tracking composition supplies Surface classes.

**Surface-ready ⊇ manifest-ready:** Manifest-ready **необходим** для orientability; Surface-ready **требует** Tracking indexes coherent.

### Surface-incomplete

| Condition | Signal |
|-----------|--------|
| Missing Tier S-A class | **SRDY-01** fail |
| Active state absent or silent-normalized invalid | **SRDY-02** fail |
| Endpoint undeclared | **SRDY-03** fail |
| Undeclared transition (ledger ≠ active) unflagged | Integrity — **SRDY-02** |
| Stale PASS treated as active for blocking | **SRDY-04** / TC-04 |
| Surface duplicates live Manifest/Tracking SoT | **SRDY-09** / MAP-05 |
| No Factory-scoped identity | Not in Surface scope |

### Completeness relationships

| Concept | Meaning |
|---------|---------|
| **Manifest-ready** | Entry orientability (MRDY-*) |
| **Fully trackable** | Seven tracking questions (TC-*) |
| **Surface-ready** | Eight RT-G12 visibility questions (SRDY-*) |
| **Gate-complete** | Authorization through endpoint (GCO-*) |
| **Lifecycle complete** | Narrative at endpoint (Stage 5) |

Project at `BLOCK_READY` with validation FAIL may be **surface-ready** and **blocked** simultaneously (OA-03).

---

## Explicit Non-Claims

This document and the Factory Tracking Surface Charter it defines:

- **are not** a **dashboard**, **application**, **screen layout**, **widget system**, or **navigation** design;
- **are not** **UI**, **HTML**, **CSS**, **JS**, **frontend**, or **operator product**;
- **are not** a Website Factory **runtime**, **execution engine**, or **shipped product**;
- **are not** **storage**, **database**, **file format**, **serialization**, **YAML**, **JSON**, or **schemas**;
- **are not** a **workflow engine**, **BPMN executor**, **orchestrator**, or **automation layer**;
- **are not** a **tracking engine**, **tracking storage**, **state store**, or **recorder product**;
- **are not** **implementation**, **agents**, **validators**, or **CI binding**;
- **are not** **Gate Results System**, **Lifecycle System**, **Handoff Package System**, or **Passport**;
- **are not** **manifest** (RT-G10) or **registry** (RT-G05) — per-project Surface vs their scopes;
- **are not** FACTORY-TRACKING-SURFACE-STANDARD-v1.md, FACTORY-DASHBOARD-v1.md, FACTORY-UI-SPEC-v1.md, FACTORY-PROJECT-PASSPORT-v1.md, FACTORY-TRACKING-STORAGE-v1.md;
- **do not** define screens, layouts, wireframes, components, widgets, menus, panels, database tables, or tracking files;
- **do not** modify Factory Engine Architecture v1 Stages 1–6, Manifest Charter, or Registry Charter semantics;
- **do not** modify Runtime Architecture or Foundation layers;
- **do not** claim physical Surface artefact or UI exists in repo — **charter only**.

Human-operated declaration remains the v1 observation model per Runtime Architecture.

---

## Open Questions

Charter **bounds** future work — **does not answer** display or storage choices.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-TS01** | Recent event window size / «since last visit» semantics | **OPEN** — display or operational playbook |
| **OQ-TS02** | Whether RT-G10 manifest serializes Surface Tier S-A subset | **OPEN** — implementation charter (OQ-M01) |
| **OQ-TS03** | PHASE_SLICE — one Surface per shell vs per slice | **OPEN** — OQ-S6-03 |
| **OQ-TS04** | Portfolio Registry card fields vs Surface class overlap | **BOUNDED** — RA-05 forbids authoritative copy |
| **OQ-TS05** | Separate «Operator Display Charter» vs this Surface charter | **OPEN** — UI must reference SRDY-*, VP-* |
| **OQ-TS06** | `PASS_WITH_WARNINGS` actionable class on Surface | **OPEN** — OQ-S6-08 |
| **OQ-TS07** | Auto-sync Surface from Tracking — display-only vs forbidden SoT | **BOUNDED** — authoritative = declarations; sync **non-authoritative** only |
| **OQ-TS08** | MIG / incoming request correlation as Surface event class | **OPEN** — RT-G08 |
| **OQ-TS09** | Relationship RUNTIME-GAPS RT-G12 «dashboard» line vs this charter | **BOUNDED** — doctrine complete here; dashboard = **future display**, not Surface role |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat this charter as **RT-G12 Tracking Surface doctrine complete** — RUNTIME-GAPS RT-G12 remains **NOT STARTED** for **UI/dashboard implementation**.
2. **If operator display needed:** Authorize **separate** display/CLI charter — **must** map to Tier S-A/B/C and SRDY-*; **must** carry VP-*, MAP-05, RAP-06 forward; **do not** create FACTORY-DASHBOARD-v1.md or FACTORY-UI-SPEC-v1.md without explicit authorization.
3. **If persistence needed:** RT-G04 — Surface **does not** choose storage; Tracking zones may persist under storage charter.
4. **If serialization needed:** RT-G10 implementation standard — **may** include Surface classes per OQ-TS02; Manifest charter precedes.
5. **Do not create:** FACTORY-TRACKING-SURFACE-STANDARD-v1.md, tracking engine, tracking storage, passport, or Gate Results System.
6. **Optional P3:** Update RUNTIME-GAPS RT-G12 to «CHARTERED (Tracking Surface doctrine)» — operator action, outside deliverable.

**Engine Architecture v1 requires no further architecture stages.** Tracking Surface charter is **post-Engine, post-Manifest, post-Registry** documentation.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether any tool already renders Engine composition | **UNKNOWN** — no canonical UI chartered |
| Calendar for display implementation | **not scheduled** |
| Triumph / client deploy vs Surface «completion» | **UNKNOWN** — external |
| 1:1 mapping Surface classes to future manifest fields | **requires** RT-G10 implementation charter |

---

*Factory Tracking Surface Charter v1 — RT-G12 doctrine complete. Architecture charter only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Tracking Surface Charter v1

**Stage:** RT-G12 — Factory Tracking Surface Charter (post–Engine Architecture v1, post–Manifest, post–Registry)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-TRACKING-SURFACE-CHARTER-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-TRACKING-SURFACE-CHARTER-v1.md` (created)  
**Summary:** Определена доктрина Factory Tracking Surface как операторской observability plane для одного Factory Project: восемь operator questions, позиция Registry → Manifest → Tracking → Surface, tiers S-A/B/C (классы информации, не widgets), принципы видимости state/gate/lifecycle/events, actionability vs archival, surface-ready (SRDY-*) vs surface-incomplete; границы vs Manifest (без дублирования entry), vs Tracking Model (composition vs visibility charter), vs Gate Results — без dashboard, UI, storage, runtime, tracking engine, schemas.  
**Git:** no commit, no push (per task charter).
