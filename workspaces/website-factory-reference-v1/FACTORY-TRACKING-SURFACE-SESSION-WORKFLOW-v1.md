# REPORT — Factory Tracking Surface Session Workflow v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Operational Design — **Operational Playbook 03** (Tracking Surface Session Workflow)  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 **COMPLETE**; Post-Engine Doctrine **COMPLETE**; [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) **COMPLETE**; [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) **COMPLETE**; [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) **COMPLETE**  
**Тип:** operational workflow only — **без** runtime, automation, implementation, storage, schemas, agents, UI  
**Не переопределяет:** [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), Manifest/Registry charters, Engine Stages 1–6, Runtime Architecture  

---

## Purpose

### Зачем существует Tracking Surface Session Workflow

**Tracking Surface Session Workflow** — третий операционный playbook Website Factory. Он описывает **человеко-исполняемую** операционную сессию, в которой Factory operator **наблюдает, оценивает и принимает решения** по **одному** Factory Project, используя композицию Tracking и доктрину Tracking Surface — **без** определения экранов, инструментов или автоматизации.

Workflow закрывает координационную проблему **ежедневного надзора за production case**:

| Проблема | Как workflow решает |
|----------|---------------------|
| Проект manifest-enrolled и/или в каталоге, но оператор не знает «что сейчас правда» | Нормативная **сессия** с фазами: вход → ориентация → reality → blockers → actionability → исход → закрытие |
| Registry/Manifest дают entry, но не заменяют operational depth | Сессия **обязательно** углубляется в Tracking composition + Surface visibility classes после per-project entry |
| Блокеры смешивают gate FAIL, stale PASS, handoff, halt | Раздельные **принципы оценки** blockers без gate criteria text на Surface |
| «Что делать дальше» подменяется git-работой или layer work без declarations | **Actionability assessment** различает should / may / cannot — declarations остаются human-only |
| Сессии без дисциплины оставляют неявные решения | **Session outcomes** и **closure criteria** фиксируют, что сессия завершена и что записано |

Оператор после прохождения workflow (или его нормативного чеклиста в одной сессии) должен уметь ответить **без чтения всего workspace**:

- Как начать Factory session?
- Как ориентироваться?
- Как установить текущую реальность?
- Как определить блокеры?
- Как определить следующие действия?
- Как завершить сессию?

### Что workflow **не** решает

| Вне scope | Почему |
|-----------|--------|
| Factory-scoped recognition, manifest enrollment | [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) |
| Catalog enrollment, portfolio discoverability | [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) |
| Исполнение state transitions, gate evaluation, handoff delivery | Runtime + Engine; operator **declares** вне этого playbook |
| Physical manifest/registry/tracking files, persistence | RT-G04, RT-G05, RT-G10 implementation — NOT STARTED |
| Automation, agents, n8n, CI-driven session open/close | Explicitly forbidden in v1 |
| Layer artefact production (bodies) | Foundation workstreams — сессия **наблюдает refs**, не производит тела |
| Operator display, dashboard, session UI | RT-G12 implementation — **запрещено** в этом playbook |
| Multi-project queue rank, scheduling | RT-G06 — FUTURE |

**Граница playbook:** от **открытия операционной сессии** по выбранному Factory Project до **закрытия сессии** с зафиксированным outcome. Enrollment playbooks **предшествуют** первой полноценной Surface session; повторные сессии — **норма** на всём жизненном цикле track.

```text
  PLAYBOOK 01/02 (enrollment)          THIS WORKFLOW (03)              BETWEEN SESSIONS
  manifest / catalog optional               │                              │
        │                                   ▼                              ▼
        └──────────────▶  Entry → Orient → Reality → Blockers  →  Declarations (Engine)
                              → Action → Outcome → Close              (human, separate acts)
```

---

## Foundation Dependencies

Workflow **наследует** принятые артефакты **без их изменения**. При конфликте — побеждает более специфичный charter/model (Surface, Tracking, Gate/Lifecycle composition), затем Operational Model.

### Tier 0 — Operational model and Playbooks 01–02

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | Operator path Registry→Manifest→Tracking→Surface; decision classes C–H; visibility model; human-only declarations; OR-04 per-project path |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Предусловие manifest-enrolled для valid session (типично) |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Optional portfolio select; RE-01; RS-03 non-authoritative snapshot |

### Tier 1 — Post-Engine doctrine and Engine composition (обязательные)

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Eight operator questions; S-A/B/C tiers; SRDY-*; VP-*, GV-*, LV-*, OA-* actionability |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking zones, seven questions, TC-* trackability, eligibility snapshot, audit trail |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Entry anchor, MRDY-*, MT-01 — Manifest precedes Surface depth |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Portfolio select only; RA-05, RAP-06 — catalog ≠ tracking SoT |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | SV-*, SHV-*, active state, rollback, eligibility |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Active gate set, STALE/INVALID, blocking exit gate, GF-* |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | LC-* segment, endpoint, halt, rollback/re-entry, partial/suspended |

### Tier 2 — Engine context (reference)

[FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md); Factory Engine Stages 1–6; Runtime Architecture v1. Workflow **не** переопределяет state codes, `RG-*`, `HO-*`, или gate criteria.

**Authority precedence:** Foundation + Engine + Manifest/Registry/Tracking/Surface charters → Playbooks 01–02 → **этот playbook** для операционной сессии надзора → будущие playbooks (registry card template, declaration rituals) **не могут** нарушить MAP-05, MT-01, TV-01, RE-01, OA-ACT-01.

---

## Session Trigger Principles

Сессия **стартует** не от cron, CI или agent tick, а от **операционной потребности** принять решение о состоянии, блокерах или следующем шаге **одного** Factory Project.

### Классы триггеров (не исчерпывающий список)

| Trigger class | Typical signal | Operational note |
|---------------|----------------|------------------|
| **Active project review** | Регулярный надзор, weekly check, перед layer work | Нормативный steady-state trigger |
| **Blocked project review** | Известный FAIL, halt (LS-*), stale gate, handoff blocked | Сессия **не** заменяет remediation — фиксирует blocker picture |
| **Handoff review** | Подготовка или проверка HO boundary (e.g. Generation → Frontend) | Оценка handoff index + package refs — не package bodies |
| **Lifecycle progression review** | Перед объявлением forward transition или gate sign-off | Eligibility + active gate set **до** declaration |
| **Milestone review** | Достижение LC-* exit, composite gate window, `GENERATION_READY` | Completion picture + remaining to endpoint |
| **Post-rollback / re-entry review** | После RB-* или integrity warning | Stale/invalid gates, superseded segments — EV-02 |
| **Post-enrollment first depth session** | После Playbook 01/02 — первый уход в Tracking depth | Может быть ранний `NEW_PROJECT` — surface-ready ⊄ gate-complete |
| **Handoff between operators** | Смена ответственного, audit continuity | Recent narrative (question #6) + orientation |
| **Charter amendment impact** | Scope mask / endpoint change affecting track | LR-07 visibility — may defer declarations until reconciled |
| **Integrity alarm** | Ledger ≠ active, undeclared stale PASS, invalid active (SV-05) | Reconciliation **before** forward action (MS-02 analog) |

### Принципы триггера

| ID | Principle |
|----|-----------|
| **ST-01** | Один trigger → **одна** session instance на **один** logical Factory Project — не portfolio-wide Surface session |
| **ST-02** | Trigger **не** равен state transition — между trigger и declaration лежат фазы assessment этого workflow |
| **ST-03** | Trigger **без** Factory-scoped project → **не** открывать Surface session — сначала Playbook 01 |
| **ST-04** | Portfolio multi-select — **не** session; каждый проект получает **отдельную** session (RE-01) |
| **ST-05** | External events (deploy green, git push, MIG run) — **допустимый** повод открыть сессию, **не** authoritative truth |

### Событие, открывающее сессию

**Session instance opens** when operator фиксирует: *«требуется операционная сессия надзора по Factory Project X»* — с явным project identity (логическая ссылка), независимо от наличия catalog entry.

---

## Session Entry Model

Вход в сессию — **операционный путь к одному проекту**, не навигация по UI.

### Normative operator path

```text
  [optional] REGISTRY          MANIFEST              TRACKING              SURFACE
  «какие проекты?»      →    «что это? entry»   →   «композиция indexes»  →  «что ВИДЕТЬ?»
  portfolio select           anchor + MRDY           zones + tiers            eight questions
        │                         │                        │                        │
        └──────── select ONE logical Factory Project ──────┴────────────────────────┘
```

### Relationship: Registry, Manifest, Tracking, Surface

| Layer | Session role | Operator uses for |
|-------|--------------|-----------------|
| **Registry** | **Optional** first step when portfolio needed | Locate project among Factory projects; distinction summaries only — **не** seven/eight questions (RE-01) |
| **Manifest** | **Required** per-project entry before operational depth | Confirm identity, charter/scope, endpoint, topology pointers (MR-01); **не** live gate index (MT-01) |
| **Tracking** | **Required** for reality/blocker/actionability phases | Consume Engine composition: state instance, gate/handoff indexes, artefact refs, audit trail (Stage 3) |
| **Surface** | **Required** lens for assessment phases | Apply visibility contract: Tier S-A/B classes, eight questions, SRDY-* readiness of observability |

### Entry preconditions (typical)

| # | Precondition | If fail |
|---|--------------|---------|
| E1 | Logical Factory Project **Factory-scoped** | Defer session → Playbook 01 |
| E2 | **Manifest-enrolled** (MRDY-* attested) | Defer — orientability missing |
| E3 | Operator **identified** project (not folder guess) | Stop — RAP-10 analog |
| E4 | Manifest entry anchor **reachable** | Defer — MRDY-06 |
| E5 | Registry enrollment | **Optional** — manifest-only path valid (OR-04, decision I) |

### Entry without full trackability

| Situation | Rule |
|-----------|------|
| Early `NEW_PROJECT`, empty gate indexes | Session **allowed** — Tier S-A may be empty-allowed (SRDY-01); reality = intake position |
| Partially trackable (TC-* fail) | Session **allowed** — integrity warnings become session focus |
| Not surface-ready (SRDY fail) | Session **allowed** — outcome often **clarification required** or **defer** until indexes reconciled |
| Manifest used as gate dump | Session **blocked** — remediate MAP-05 first |

### Entry principles

| ID | Principle |
|----|-----------|
| **SE-01** | Registry **никогда** не заменяет Manifest+Tracking path для session depth |
| **SE-02** | Catalog orientation snapshot **non-authoritative** — reconcile before trusting blockers (RS-03, VP-05) |
| **SE-03** | Surface session **не** создаёт новых indexes — только **reads** composition + declares session outcome |
| **SE-04** | Dual corpus (reference v1 vs mars-website-factory pack) — operator **declares** which corpus category applies at entry (OQ-OM06 analog) |

---

## Operational Orientation Principles

Ориентация — **что оператор обязан установить в начале сессии**, до оценки blockers и forward actions. Принципы, не layout.

### Establish first (order normative)

| Priority | Understanding | Source classes | Surface question |
|----------|---------------|----------------|------------------|
| 1 | **Project identity** — один production case, не repo folder | Identity shell, stable ref | #1 |
| 2 | **Charter intent + scope tier** summary | Charter category | #1, #5 |
| 3 | **Declared lifecycle endpoint** (full / partial) | LCMP-5, MRDY-03 | #5, #7 |
| 4 | **Scope applicability mask** (full chain vs EXCLUDED) | LR-07 mask | #1, #5 |
| 5 | **Current active state** (exactly one code) | SV-01 | #2 |
| 6 | **Active lifecycle segment** (LC-*) | SV-02 | #2 |
| 7 | **Suspension / partial closure flags** if present | `FACTORY_TRACK_SUSPENDED`, `FACTORY_TRACK_CLOSED_PARTIAL` | #2, #4 |
| 8 | **Authoritative truth pointers** (where state/gates/artefacts live) | Manifest Category 7 topology — pointer only | follow refs |

### Orientation vs Manifest

| Rule | Statement |
|------|-----------|
| **OR-01** | Manifest уже дал entry understanding — сессия **подтверждает**, не переучивает MRDY-07 |
| **OR-02** | Surface orientation (PO-01) = «**in operation**» — не повтор полного Manifest essay |
| **OR-03** | Classification / blueprint **when present** — Tier S-B; absent at intake **не** fail orientation |

### Orientation complete when

Operator can **name without ambiguity**: which project; which state/LC segment; which endpoint; full or partial path — **before** declaring blockers resolved or forward eligible.

---

## Reality Assessment Principles

**Текущая реальность** = последняя **operator-declared** истина в Engine indexes, согласованная с Tracking composition и Surface visibility — **не** filesystem, **не** CI, **не** agent narrative alone (VP-03, EO-03).

### How operator establishes current reality

| Assessment step | Tracking zones | Surface classes | Question |
|-----------------|----------------|-----------------|----------|
| Confirm **active state** | Current state reference | SV-01, invalid flag SV-05 | #2 |
| Confirm **segment narrative** | State history + LC binding | LC active segment, halt LS-* | #2, #6 |
| Confirm **completion prefix** | State history, gate index, handoff index | SHV-01, gate PASS valid, HO cleared | #4 |
| Confirm **remaining to endpoint** | Eligibility snapshot, scope mask, artefact gaps | LPC-03 remaining picture | #5 |
| Confirm **recent movement** | Progression ledger tail, audit trail | EV-01 bounded window | #6 |
| Cross-check **integrity** | TC-03 ledger vs active; TC-04 stale hygiene | SRDY-02, integrity warnings | #3 (if mismatch) |

### Reality assessment principles

| ID | Principle |
|----|-----------|
| **RA-01** | Reality = **declared** indexes — если declaration отсутствует, реальность «undeclared», не «assumed green» |
| **RA-02** | Stale / superseded / invalidated **видимы** (TV-02, GV-05) — reality включает **invalidated prior truth**, не только current PASS |
| **RA-03** | Surface **не** нормализует invalid active state (VP-04) — reality assessment **флагует**, не скрывает |
| **RA-04** | Layer artefact **refs** confirm production evidence — bodies read **outside** Surface core (AV-01) |
| **RA-05** | Global layer ACCEPTED (T5) **не** входит в per-project reality |
| **RA-06** | Deploy / hosting / frontend build status — **post-Factory** — не Factory reality unless charter-bound ref |

### Trackability during session

| Trackability | Session use |
|--------------|-------------|
| **Fully trackable** (TC-01…07) | Reality assessment **proceeds** to blockers |
| **Partially trackable** | Reality assessment **documents gaps** — outcome often clarification or defer |
| **Non-trackable** | Session **cannot** complete reality phase honestly — defer to enrollment/integrity remediation |

### Reality vs wishful state

Operator **запрещено** трактовать «работа в git велась» как substitute для active state or gate index. Reality assessment **останавливается** at last declaration chain.

---

## Blocker Assessment Principles

**Блокер** — условие, **запрещающее** честно считать forward transition или gate sign-off **authorized** без remediation или reconciliation declaration.

### Blocker categories (assessment, not implementation)

| Category | What operator identifies | Composition sources |
|----------|-------------------------|---------------------|
| **Open gates** | `RG-*` required for exit not PASS or NOT_EVALUATED | Active gate set; GV-02 primary blocker |
| **Stale gates** | PASS with validity STALE after rollback/upstream change | GST-01…04; GF-07 |
| **Invalid gates** | FAIL or INVALID — stronger than stale | GV-03; eligibility fails |
| **Handoff blocks** | HO blocked, uncleared, superseded downstream | Handoff event index; HV-* |
| **Pending handoffs** | Required HO for boundary not cleared when active state implies | HV-02 e.g. HO-12 window |
| **Lifecycle halt** | LS-* stop — remain in segment | SV-03; GRS-05 |
| **Parallel legal block** | RG-LEGAL / entity in window not satisfied | GC-03 |
| **Artefact gaps** | Mandatory ref absent for current/completed state | AV-04 |
| **Eligibility violations** | FT/DR/RB rules — forward illegal regardless of local work | Derived snapshot — read Runtime ref |
| **Integrity interruptions** | Ledger ≠ active; catalog snapshot contradicts Engine | MS-02; RS-03 |
| **Suspension** | `FACTORY_TRACK_SUSPENDED` | Factory questions frozen at last declared — not same as blocked gate |

### Assessment sequence (principles)

| Step | Action |
|------|--------|
| 1 | From reality: active state + LC segment |
| 2 | Derive **active gate set** for that state (Stage 4) |
| 3 | List **primary blocking gate** (first open exit blocker) — Surface #3 |
| 4 | Scan **stale/invalid** in set — do not treat as active PASS (TC-04) |
| 5 | Scan **handoff** blocks at current boundary |
| 6 | Scan **halt / suspension** — movement frozen vs blocked authorization |
| 7 | Scan **lifecycle interruptions**: rollback in progress narrative, re-entry without fresh PASS |
| 8 | Compose **blocking summary** — at least first blocker (SRDY-04) |

### Blocker principles

| ID | Principle |
|----|-----------|
| **BA-01** | Blocker assessment cites **classes** (gate ID, HO-ID, LS code) — **не** gate criteria text on Surface (GV-01) |
| **BA-02** | «No blockers» = eligibility snapshot **derivable** as forward-legal — operator **attests**, not assumes |
| **BA-03** | Stale PASS **is** a blocker for forward until reconciled — **не** archival-only if in active gate set |
| **BA-04** | Blocked project may be **surface-ready** (OA-03) — blockers ≠ bad observability |
| **BA-05** | Registry card **cannot** be source of blocker truth (RAP-06) |

### What blocker assessment does NOT do

- Does not **evaluate** criteria (layer docs, RUNTIME-GATES)  
- Does not **execute** remediation or auto-rollback  
- Does not **invent** new `RG-*` or states  

---

## Actionability Assessment Principles

Actionability — **что оператор может решить в этой сессии** относительно Factory track, разделяя обязательное, допустимое и запрещённое.

### Three action classes

| Class | Meaning | Examples (operational) |
|-------|---------|------------------------|
| **Should happen next** | Единственный coherent next Factory step при текущей реальности и без blockers | Declare forward transition when eligible; declare gate PASS when evidence + criteria met; reconcile integrity first if ledger mismatch |
| **May happen next** | Допустимо, но не единственный path; charter/scope dependent | Defer layer work; escalate to reviewer; charter amendment; rollback declaration; partial closure review; registry withdrawal (separate decision) |
| **Cannot happen next** | Запрещено без supersession, remediation, or prerequisite declarations | Forward while blocking gate open/stale/invalid; skip EXCLUDED state without charter jump; auto-complete to `COMPLETE`; treat deploy as Factory terminal; substitute git work for gate declaration |

### Derivation from Surface actionability (OA-*)

| Surface actionable class | Session maps to |
|--------------------------|-----------------|
| Active state + halt/suspension | Should: remain vs escalate |
| Primary open blocker | Should: remediate target before forward |
| Eligibility snapshot | Should / cannot: declare forward only if legal |
| Stale gate after rollback | Should: reconcile before re-forward |
| Declared endpoint vs position | Should: continue vs initiate partial closure path |
| Integrity warnings | Should: reconciliation declaration **before** movement |
| Archival history | May inform — **not** should for immediate forward |

### Actionability principles

| ID | Principle |
|----|-----------|
| **AA-01** | Session **recommends** action class — **не** executes declarations (OA-01) |
| **AA-02** | **Should** без устранения blockers → outcome **defer** or **clarification**, не progression |
| **AA-03** | **May** включает «no Factory declaration this session» — valid **no action** outcome |
| **AA-04** | **Cannot** включает automation expectations (RT-G01, RT-G11) — not available in v1 |
| **AA-05** | Gate criteria read **authoritative layer/Runtime** — Surface alone insufficient for PASS decision |

### Forward picture (question #7)

Operator completes actionability when can state: **eligible next** (segment/state + declaration type) **or** **blocked with cause** (blocker class reference) **or** **terminal** (`COMPLETE` / partial closure / suspended).

---

## Session Outcomes

Каждая сессия **заканчивается** одним primary outcome + optional notes. Outcomes — **операционные**, не Runtime state codes.

### Primary outcomes

| Outcome | Meaning | Typical follow-up |
|---------|---------|-------------------|
| **Progression decision** | Operator **decides** declare forward transition, gate PASS, handoff clearance, or terminal — **may execute after session** | Human declarations per Engine (separate acts) |
| **Defer** | Blockers or gaps prevent decision now; remediation scheduled | Re-open session after layer work or evidence |
| **Escalation** | Requires reviewer, sponsor, charter author, or architecture gap | HITL, extended type ER-01, legal parallel |
| **Clarification required** | Reality or trackability incomplete; topology/endpoint/identity ambiguous | Close MRDY/SRDY gaps; reconciliation |
| **No action** | Reality assessed; blockers understood; **no** Factory declaration warranted now | Valid closure — track stable |
| **Reconciliation decision** | Integrity (stale hygiene, ledger mismatch, invalid active) must be declared before movement | Operator declaration correcting index honesty |
| **Scope / charter amendment decision** | LR-07 or endpoint change needed before movement | Amendment path — outside routine session |

### Outcome selection principles

| ID | Principle |
|----|-----------|
| **SO-01** | Exactly **one** primary outcome per session instance |
| **SO-02** | **Progression decision** **requires** blockers absent or explicitly accepted as remediated in same declaration window |
| **SO-03** | **No action** **≠** failed session — honest stability is valid |
| **SO-04** | **Defer** **must** cite blocker class or MRDY/SRDY/TC gap — not «later» alone |
| **SO-05** | Session outcome **does not** auto-write Engine — operator declarations **follow** if progression chosen |

### Outcome record (logical, not format)

| Category | Content |
|----------|---------|
| Session outcome code | Primary outcome from table |
| Operator identity | Role class |
| Logical timestamp | Session close |
| Project identity ref | Logical Factory Project |
| Reality summary | Active state + LC + endpoint position (categories) |
| Blocker summary | None or enumerated classes |
| Actionability summary | Should / may / cannot one-liners |
| Evidence classes | See session evidence (optional S1–S8) |

**Append-only:** correction = new session record or amendment declaration — not silent overwrite (AT-01 analog).

---

## Session Closure

### When a session is considered complete

Session **closed** when operator has:

| # | Closure criterion |
|---|-------------------|
| 1 | Completed **entry** along normative path (Manifest minimum; Tracking engaged) |
| 2 | Completed **orientation** (OR priorities 1–8 or documented defer reason) |
| 3 | Completed **reality assessment** (RA phases or documented non-trackable) |
| 4 | Completed **blocker assessment** (BA sequence or explicit «none» attestation) |
| 5 | Completed **actionability assessment** (AA forward picture) |
| 6 | Recorded **primary session outcome** (SO-01) |
| 7 | Recorded **closure** operator + logical time |

### What must be true before closure

| Must be true | Rationale |
|--------------|-----------|
| Project identity **unambiguous** | SE-03 |
| Active state **known or flagged invalid** | SRDY-02 |
| Blocking summary **derivable** (may be «none») | SRDY-04 |
| Operator **not** leaving implicit progression decision | SO-05 |
| Session **did not** treat Registry/Manifest as live gate index | MT-01, MAP-05 |

### Closure does NOT require

- Physical session log file or REPORT artefact (optional evidence)  
- Gate PASS or state transition in same calendar sitting  
- Surface-ready if outcome is **clarification** or **defer** with documented SRDY gaps  
- Registry enrollment  

### Premature closure (forbidden)

| Violation | Response |
|-----------|----------|
| Close without blocker assessment when blockers suspected | Re-open session |
| Close with «progression» outcome while primary blocker open | Change outcome to **defer** |
| Close without naming project | Invalid session — restart entry |

---

## Workflow Completion

### When Tracking Surface Session Workflow is considered complete

**Playbook 03** как документ считается **complete** когда operator organization **приняла** его как норматив для supervision sessions — deliverable = этот файл.

**Per-session** workflow complete = **Session Closure** criteria satisfied.

### Relationship to enrollment playbooks

```text
  Playbook 01 (Manifest enrollment)  ──▶  manifest-enrolled
  Playbook 02 (Registry enrollment)  ──▶  catalog-discoverable [optional]
  Playbook 03 (this workflow)        ──▶  repeatable per-project supervision
```

Playbook 03 **не заменяет** 01/02; первую Surface-depth session **типично** открывают после Playbook 01 (и 02 при portfolio need).

### Connection to future playbooks

| Future artifact | Relationship |
|-----------------|--------------|
| Registry index card template (OQ-R02) | Feeds **Registry entry** only — not session depth |
| Declaration ritual / gate sign-off playbook | **Executes** outcomes of **progression decision** sessions |
| Partial closure operator playbook (OQ-S6-09) | Specialized session trigger — **uses** this workflow phases |
| Operator Display Charter (OQ-TS05) | May **render** Surface classes — **must** map SRDY-*, VP-* |
| RT-G04/10/12 implementation | Persistence/UI — **не** changes session principles |

### Operational readiness (OR analog)

Factory supervision is **operationally usable** when operators run Playbook 03 **explicitly** for active tracks — per [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) OR-04 path.

---

## Explicit Non-Claims

This playbook and Tracking Surface Session Workflow v1:

- **are not** a **dashboard**, **tracking UI**, **screen layout**, **widget system**, or **navigation** design;
- **are not** **UI**, **HTML**, **CSS**, **JS**, **frontend**, or **operator product**;
- **are not** a Website Factory **runtime**, **execution engine**, **workflow engine**, or **shipped product**;
- **are not** **automation**, **agent workflow**, n8n, CI-driven sessions, or **orchestrator**;
- **are not** **storage**, **database**, **file format**, **serialization**, **YAML**, **JSON**, **schemas**, or **tables**;
- **are not** **tracking implementation**, **tracking storage**, **state store**, or **recorder product**;
- **are not** **implementation** of manifest (RT-G10), registry (RT-G05), or display (RT-G12);
- **do not** redefine [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), Engine Stages 1–6, Manifest/Registry charters, Gate/Lifecycle/State models;
- **do not** define screens, menus, panels, wireframes, database tables, or tracking files;
- **do not** claim physical Surface artefact, dashboard, or session store exists in-repo.

Human-operated supervision and declarations remain the v1 operating reality.

---

## Open Questions

Bounded for **future operational artifacts** — not resolved in Playbook 03.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-TSW01** | Minimum session evidence (S1–S8) formality: REPORT-only vs structured attestation | **OPEN** — operator convention |
| **OQ-TSW02** | Recent event window for reality phase (OQ-TS01) — «since last session» semantics | **OPEN** — ties Surface EV classes |
| **OQ-TSW03** | PHASE_SLICE: one session per shell vs per slice | **OPEN** — OQ-S6-03, OQ-TS03 |
| **OQ-TSW04** | Mandatory session cadence per active project | **OPEN** — governance, not architecture |
| **OQ-TSW05** | Combined session: supervision + gate sign-off declaration in one sitting | **OPEN** — ritual playbook |
| **OQ-TSW06** | MIG / incoming correlation as session trigger evidence | **OPEN** — OQ-TS08, OQ-OM08 |
| **OQ-TSW07** | Pilot external-only: skip Playbook 03 vs lightweight session | **SAFE UNKNOWN** per case charter |
| **OQ-TSW08** | `PASS_WITH_WARNINGS` actionability class (OQ-S6-08) | **OPEN** — gate composition |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **Tracking Surface Session Workflow v1** as Operational Playbook 03 **complete** — use for per-project supervision after Manifest path (and Registry when portfolio used).
2. **Operational Design continuation (separate tasks):**
   - Registry index card template (OQ-R02) — portfolio entry only
   - Gate sign-off / state transition declaration ritual playbook
   - Partial closure operator playbook (OQ-S6-09)
3. **Per active Factory Project:** Run session explicitly; record session outcome even if evidence is session REPORT — not Engine SoT unless separate declarations.
4. **Do not start:** dashboard, tracking storage, session database, runtime, agents — unless explicitly authorized.
5. **Optional P3:** Reference Playbook 03 from [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) Operational Design row — operator action.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether operators already run ad-hoc «status sessions» without this playbook | **UNKNOWN** — no canonical session artefact |
| Default session cadence across pilots | **not standardized** in v1 |
| Calendar for RT-G12 display binding sessions | **not scheduled** |

---

*Factory Tracking Surface Session Workflow v1 — Operational Playbook 03. Canonical location: `workspaces/website-factory-reference-v1/`. Git: no commit, no push.*

---

# REPORT — Factory Tracking Surface Session Workflow v1

**Stage:** Operational Design — Operational Playbook 03 (Tracking Surface Session Workflow)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md` (created)  
**Summary:** Определён операционный workflow сессии надзора за одним Factory Project: триггеры, вход Registry→Manifest→Tracking→Surface, принципы ориентации, оценки текущей реальности, блокеров (open/stale/invalid gates, handoffs, halt, integrity) и actionability (should/may/cannot), исходы сессии (progression/defer/escalation/clarification/no action/reconciliation/scope), критерии закрытия и связь с Playbooks 01–02 и будущими ritual/display артефактами — без dashboard, UI, runtime, automation, storage, implementation.  
**Git:** no commit, no push (per task charter).
