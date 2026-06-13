# REPORT — Factory Project State Model v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Factory Engine Architecture v1 — **Stage 2 only**  
**Контекст:** Website Factory Foundation Era **COMPLETE**; [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) **ACCEPTED** (Stage 1); Engine Readiness Audit v1 — **PASS WITH WARNINGS**  
**Тип:** architecture only — **без** implementation, runtime product, agents, code, workflows, databases, automation, storage format  
**Связь:** [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md), [runtime-architecture/STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md), [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md)

---

## Purpose

Stage 1 ответил: **«Что движется?»** — канонический [Factory Project](FACTORY-PROJECT-OBJECT-MODEL-v1.md) как логическая единица отслеживания.

Stage 2 отвечает: **«Как это движется?»** — каноническая **модель состояния** одного Factory Project: как проект **занимает** Runtime states, как фиксируется текущее положение, история, прогрессия, откат и повторный вход — **без** изменения Runtime Architecture и **без** определения хранилища, манифестов или gate/handoff implementation systems.

Оператор после Stage 2 должен уметь ответить **без чтения всего workspace**:

| Вопрос | Ответ даёт |
|--------|------------|
| Где проект сейчас? | **Current state instance** (Runtime state code) |
| Какие состояния уже завершены? | **State history** — completed occupancy records |
| Какое состояние активно? | **Active state** = единственный current pointer |
| Что дальше? | **Next eligible state** по TR-* при открытых gates |
| Можно ли вперёд? | **Forward eligibility** — gates + forbidden transitions |
| Можно ли назад? | **Rollback eligibility** — RB-* + charter |
| Что блокирует? | **Open gates** + stop points (LS-*) — не новые states |

Документ **не** заменяет [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) и **не** добавляет state codes.

---

## Foundation Dependencies

Factory Project State Model **наследует** Stage 1 и **привязывается** только к принятой Foundation + Runtime:

| Dependency | Role for state model |
|------------|----------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Объект с `current canonical state pointer`, state history index, gate/handoff indexes |
| [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) | **Единственный** источник имён и семантики 14 states |
| [runtime-architecture/STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md) | TR-*, FT-*, DR-*, RB-*, LR-*, ER-* — правила движения |
| [runtime-architecture/RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) | `RG-*` — условия разблокировки переходов |
| [runtime-architecture/RUNTIME-HANDOFFS-v1.md](runtime-architecture/RUNTIME-HANDOFFS-v1.md) | `HO-01`…`HO-13` — границы при forward transitions |
| [runtime-architecture/PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) | LC-00…LC-13, LS-*, AP-* — фазы и halt/resume |
| [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md) | Runtime ↔ Engine boundary; ERA-W07 supersession discipline |
| [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) | Global layer ACCEPTED — не per-project state |

**Authority:** при конфликте имени или семантики state → Runtime wins. При конфликте «где сейчас этот проект» → Factory Project state instance (Engine), **используя** Runtime vocabulary.

---

## Runtime Binding Principles

### Principle RB-1 — Vocabulary reuse only

Каждое Factory Project state **является ссылкой** на ровно один Runtime state code из фиксированного набора:

`NEW_PROJECT`, `CLASSIFIED`, `BLUEPRINT_READY`, `PAGE_READY`, `BLOCK_READY`, `VALIDATED`, `SEO_READY`, `DESIGN_READY`, `CONTENT_READY`, `CONTENT_VALIDATED`, `GENERATION_READY`, `PRODUCTION_QA_READY`, `FRONTEND_READY`, `COMPLETE`.

**Запрещено:** новые state codes, синонимы, под-состояния как «официальные» Factory states (например `SEO_IN_PROGRESS` как canonical state).

### Principle RB-2 — Class vs instance

| Layer | Owns |
|-------|------|
| **Runtime** | State **definition** (purpose, inputs, outputs, allowed/forbidden transitions per state) |
| **Factory Project** | State **instance** для конкретного production case |

Runtime описывает **что означает** `SEO_READY`. Factory Project фиксирует **что этот проект сейчас в** `SEO_READY` (или прошёл через него).

### Principle RB-3 — Binding record shape (logical, not storage)

Минимальная логическая привязка state instance к Runtime (формат хранения **не** определяется):

| Field (logical) | Source | Notes |
|-----------------|--------|-------|
| `runtime_state_code` | Runtime PROJECT-STATE-MODEL | Must match exactly |
| `lifecycle_phase_id` | PROJECT-LIFECYCLE LC-* | 1:1 с target state при full chain |
| `scope_applicability` | Project charter (LR-07) | `APPLICABLE` / `EXCLUDED` / `N_A` per state for partial scope |
| `occupancy_role` | Engine | `ACTIVE` \| `COMPLETED` \| (never `ACTIVE` for two states) |

### Principle RB-4 — Movement rules are read-only

Forward, forbidden, rollback, parallel legal (LR-01–LR-03), extended type (ER-01–ER-02) — **импортируются** из STATE-TRANSITION-RULES и PROJECT-STATE-MODEL. Engine **не** ослабляет FT-* / DR-* без supersession charter (ERA-W07).

### Principle RB-5 — Halt ≠ new state

[PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) stop points (LS-01…LS-09) означают **застой в текущем Runtime state**, не введение дополнительного state. Проект остаётся, например, в `BLOCK_READY`, пока validation FAIL не снят — без перехода к `VALIDATED`.

### Runtime binding map (Factory Project ↔ Runtime)

| Runtime state | LC phase | Primary `RG-*` at entry | Handoff into state (`HO-*`) |
|---------------|----------|---------------------------|-----------------------------|
| `NEW_PROJECT` | LC-00 | — (initial) | — |
| `CLASSIFIED` | LC-01 | `RG-INTAKE_COMPLETE` | `HO-01` complete |
| `BLUEPRINT_READY` | LC-02 | `RG-CLASSIFICATION_COMPLETE` | `HO-02` |
| `PAGE_READY` | LC-03 | `RG-BLUEPRINT_APPROVED` | `HO-03` |
| `BLOCK_READY` | LC-04 | `RG-PAGE_ARCHITECTURE_APPROVED` | `HO-04` |
| `VALIDATED` | LC-05 | `RG-VALIDATION_PASS` | `HO-05` |
| `SEO_READY` | LC-06 | `RG-SEO_APPROVED` | `HO-06` |
| `DESIGN_READY` | LC-07 | `RG-DESIGN_APPROVED` | `HO-07` |
| `CONTENT_READY` | LC-08 | `RG-CONTENT_APPROVED` | `HO-08` |
| `CONTENT_VALIDATED` | LC-09 | `RG-CONTENT_VALIDATION_PASS` | `HO-09` |
| `GENERATION_READY` | LC-10 | `RG-GENERATION_READY` (+ legal) | `HO-10` |
| `PRODUCTION_QA_READY` | LC-11 | `RG-PRODUCTION_QA_PASS` | `HO-11` |
| `FRONTEND_READY` | LC-12 | `RG-FRONTEND_HANDOFF_APPROVED` | `HO-12` |
| `COMPLETE` | LC-13 | `RG-PROJECT_COMPLETE` | `HO-13` |

---

## Canonical Definition Of Project State

**Project state** (Engine sense) — **не** отдельная онтология от Runtime state. Это **экземплярное занятие** Factory Project одним Runtime state code в момент времени, плюс **история** таких занятий и **метаданные прогрессии**, достаточные для операторского контроля.

Состав канонической модели (логические сущности):

```text
┌─────────────────────────────────────────────────────────┐
│              FACTORY PROJECT STATE MODEL                 │
├─────────────────────────────────────────────────────────┤
│  Active State Instance     ← exactly one Runtime code    │
│  State History Index       ← ordered occupancy records   │
│  Progression Ledger        ← declared transitions        │
│  Eligibility Snapshot      ← derived: next / blocked     │
│  Scope State Mask          ← charter exclusions (LR-07)  │
└─────────────────────────────────────────────────────────┘
         │ references                    │ does not define
         ▼                               ▼
   Runtime 14 states              Storage / manifests
   TR / FT / DR / RB / RG-*       Gate Results system
   HO-* contracts                  Handoff Package system
```

**Project state ≠ layer artefact state.** PASS/FAIL validation run, Legal Card status, Frontend build progress — **артефакты и gate inputs**, не substitute для `runtime_state_code`.

**Project state ≠ workstream queue position.** Нет priority rank как canonical state.

---

## Current State

### Active state instance

**Current state** — единственный активный `runtime_state_code` для Factory Project в любой момент.

| Rule | ID | Statement |
|------|-----|-----------|
| Uniqueness | **CS-01** | Ровно **один** state с `occupancy_role = ACTIVE`. |
| Runtime fidelity | **CS-02** | Active code **must** быть из Runtime catalogue; иначе tracking invalid. |
| Terminal lock | **CS-03** | Если active = `COMPLETE`, нет outbound transitions (FT-10); active остаётся `COMPLETE`. |
| Halt preservation | **CS-04** | При LS-* stop project **остаётся** в текущем state до gate PASS + declared forward transition. |

### Operator answers from current state

| Question | Derivation |
|----------|------------|
| «Where now?» | Active `runtime_state_code` |
| «What phase?» | LC-* row from binding map |
| «Stuck or progressing?» | If next transition blocked → halt at current; else work inside state toward gate |

### Partial scope (LR-07)

При charter-narrowed scope states помечаются `EXCLUDED` в scope mask — они **не** становятся active, но **не** удаляются из Runtime vocabulary. Current state **пропускает** excluded states по documented jump rules (Stage 3 lifecycle model); until then: operator documents **effective path** in charter and treats excluded states as `N_A` in history.

**Default:** full chain — все 13 progressive states applicable before `COMPLETE`.

---

## State Progression

### Progression vs transition

| Concept | Definition |
|---------|------------|
| **State progression** | Упорядоченное продвижение Factory Project по Runtime chain согласно TR-01…TR-13 |
| **State transition** | **Дискретное событие** смены active state: `from_code` → `to_code`, human-declared |
| **Intra-state work** | Работа внутри одного state (артефакты, layer gates) **без** смены active code |

Progression **завершена** для проекта, когда active = `COMPLETE` и closure gate `RG-PROJECT_COMPLETE` recorded.

### Forward progression rules

Forward move **legal** iff **все** условия:

| # | Condition | Authority |
|---|-----------|-----------|
| 1 | `to_code` = next state in TR matrix from `from_code` | STATE-TRANSITION-RULES |
| 2 | Transition not in FT-* forbidden set | STATE-TRANSITION-RULES |
| 3 | DR-* layer order satisfied | STATE-TRANSITION-RULES |
| 4 | Required `RG-*` = PASS for target state | RUNTIME-GATES |
| 5 | Corresponding `HO-*` handoff cleared (artefacts + blocked conditions) | RUNTIME-HANDOFFS |
| 6 | Parallel legal LR-01–LR-03 satisfied when entering `GENERATION_READY` | STATE-TRANSITION-RULES §7 |
| 7 | Operator declaration recorded (AP-* where applicable) | PROJECT-LIFECYCLE |
| 8 | Partial scope: target state not `EXCLUDED`, or charter jump documented | LR-07 + charter |

**Can the project move forward?** = evaluate 1–8 at active state; **next eligible** = `to_code` from TR row if all PASS; else **blocked** with reason = first failing condition (open gate, FT violation, LS stop).

### Progression ledger (logical)

Каждый forward transition **должен** породить progression record (storage deferred):

| Logical field | Purpose |
|---------------|---------|
| `transition_id` | Stable reference |
| `from_runtime_state_code` | Prior active |
| `to_runtime_state_code` | New active |
| `rule_id` | e.g. `TR-06` |
| `declared_at` | Operator timestamp (logical) |
| `declared_by` | Operator / role |
| `gate_refs_passed` | List of `RG-*` IDs relied upon (not full gate system) |
| `handoff_ref` | `HO-*` ID at boundary |

### Skip-forward

FT-09 / FT-12–FT-15: skip-forward **forbidden** as progression event. Charter cannot authorize skip without **explicit** supersession of Runtime (outside Stage 2 scope).

---

## Transition Ownership

### Boundary table

| Concern | Owner | Factory Project role |
|---------|-------|----------------------|
| State codes & semantics | **Runtime** | Reference only |
| TR / FT / DR / RB / LR / ER rules | **Runtime** | Evaluate eligibility; **do not** redefine |
| `RG-*` / `HO-*` definitions | **Runtime** (+ layer gates referenced) | Consume pass/fail + handoff clearance |
| **Declaring** a transition occurred | **Factory Project tracking** (Engine) | **Owns** progression ledger entries |
| **Executing** enforcement automatically | **Nobody in v1** | Human-operated per RUNTIME-ARCHITECTURE-SYSTEM §7 |
| Invalid transition detection | **Runtime rules** (normative) + **operator** (operative) | Project may flag violation vs TR/FT; no auto-halt engine |

### Both — split of labor

```text
Runtime answers:     "May ANY project go from VALIDATED to SEO_READY?"
                     → Yes, if TR-06 + RG-SEO_APPROVED + DR-01...

Factory Project answers:
                     "Did THIS project declare that move?"
                     "What is THIS project's active state?"
```

**Runtime does not store instances** (RT-G04). **Project does not define movement vocabulary.**

---

## Rollback Model

### What rollback means

**Rollback** — **declared backward transition** active state с `from_code` на `to_code`, где пара разрешена в STATE-TRANSITION-RULES §6 (RB-01…RB-12).

Rollback **implies**:

1. Active state **changes** to earlier Runtime code.
2. Progression ledger получает запись типа `ROLLBACK` с `rule_id` (e.g. `RB-06`).
3. **Downstream project refs** (layer artefact index, gate outcome index entries tied to states after `to_code`) переходят в **invalidated** status — operator-declared, per Stage 1 authority (invalidates refs, not Foundation docs).
4. **Re-entry** к states between `to_code` and former position — см. Re-entry Model.

Rollback **does not mean**:

- Удаление Foundation layer documents или изменение frozen Legal Pack.
- Автоматический revert git/workspace файлов.
- Отмена истории — prior `COMPLETED` occupancy records **остаются** в history с пометкой `SUPERSEDED_BY_ROLLBACK` (logical).
- Новый Runtime state (например `ROLLED_BACK`).
- Rollback из `COMPLETE` — **forbidden** (FT-10).
- Multi-hop rollback без charter — **forbidden** (STATE-TRANSITION-RULES §6: no skip backward across more than one architectural layer without charter).

### Rollback legality matrix (inherited)

| From | To | Rule | Typical trigger |
|------|-----|------|-----------------|
| `CLASSIFIED` | `NEW_PROJECT` | RB-01 | Intake rework |
| `BLUEPRINT_READY` | `CLASSIFIED` | RB-02 | Reclassification |
| `PAGE_READY` | `BLUEPRINT_READY` | RB-03 | Blueprint change |
| `BLOCK_READY` | `PAGE_READY` | RB-04 | Page contract change |
| `VALIDATED` | `BLOCK_READY` | RB-05 | Block stack change |
| `SEO_READY` | `VALIDATED` | RB-06 | SEO-only rework |
| `DESIGN_READY` | `SEO_READY` | RB-07 | Design-only rework |
| `CONTENT_READY` | `DESIGN_READY` | RB-08 | Content contract rework |
| `CONTENT_VALIDATED` | `CONTENT_READY` | RB-09 | Signal binding fix |
| `GENERATION_READY` | `CONTENT_VALIDATED` | RB-10 | Scope change — **charter required** |
| `PRODUCTION_QA_READY` | `GENERATION_READY` | RB-11 | Package rework |
| `FRONTEND_READY` | `PRODUCTION_QA_READY` | RB-12 | Handoff rejected |

**Forbidden rollback examples:** `COMPLETE` → any; `FRONTEND_READY` → `GENERATION_READY` (skips Production QA); any RB not listed.

### Rollback and gates

Rollback **does not** erase `RG-*` definitions. Prior PASS records for states **above** rollback target become **stale for forward eligibility** until gates re-validated and operator re-declares forward transitions. Project gate index marks stale entries — **without** creating Gate Results system (Stage 4+).

---

## Re-entry Model

### Definition

**Re-entry** — повторное **занятие** Runtime state, который проект **уже** имел в history с `COMPLETED`, после rollback или после intra-layer rework requiring re-approval.

### Allowed re-entry

| Condition | Description |
|-----------|-------------|
| **R-01 Post-rollback** | After legal RB-* rollback to `to_code`, project may forward again through subsequent states following TR rules — each forward transition is a **new** progression event. |
| **R-02 Same-state rework** | Active unchanged; gates re-run (e.g. new validation run in `BLOCK_READY` before `VALIDATED`) — **not** re-entry; intra-state. |
| **R-03 Forward after stale gate** | After rollback, re-entry to `SEO_READY` requires fresh `RG-SEO_APPROVED` + TR-06 — prior completion record alone insufficient. |

### Re-entry constraints

| Rule | Statement |
|------|-----------|
| **RE-01** | Re-entry **never** bypasses FT-* / DR-* on forward path. |
| **RE-02** | `COMPLETE` **не** re-enterable — terminal (FT-10). |
| **RE-03** | Re-entry to state **without** rollback when active is already past that state — **forbidden** unless RB-* first moves active backward. |
| **RE-04** | History preserves **all** occupancy periods; re-entry adds **new** history segment linked to `prior_segment_id` (logical). |

### Re-entry vs partial scope

Excluded states (LR-07) — **no re-entry** because project never **completed** occupancy; mask stays `N_A`.

---

## Terminal State Rules

### Primary terminal: `COMPLETE`

Проект **COMPLETE** (Factory closure) iff:

| # | Criterion |
|---|-----------|
| 1 | Active `runtime_state_code` = `COMPLETE` |
| 2 | Prior occupancy: `FRONTEND_READY` completed in history |
| 3 | `RG-FRONTEND_HANDOFF_APPROVED` + `RG-PROJECT_COMPLETE` recorded PASS |
| 4 | TR-13 satisfied; FT-08 not violated |
| 5 | Operator closure sign-off (AP-09) declared |

**COMPLETE means:** Website Factory architecture track **closed** — no further Factory state advances; Frontend implementation may continue **outside** Factory state model.

### Additional terminal outcomes

Runtime defines **один** terminal state: `COMPLETE`. Stage 2 **не** вводит:

- `CANCELLED`, `ABANDONED`, `ARCHIVED` как canonical Runtime states.

**Non-terminal outcomes** (не separate states):

| Outcome | Representation |
|---------|----------------|
| **Abandoned / cancelled charter** | Project remains at last active state; charter flag `FACTORY_TRACK_SUSPENDED` (logical project metadata — **not** Runtime state); Stage 3 may formalize |
| **Indefinite halt** | Active frozen at e.g. `VALIDATED` + LS-03; **not** terminal |
| **Partial delivery closed** | Charter declares end at e.g. `DESIGN_READY`; active set to last in-scope state; **may** require operator convention for «factory-complete partial» — **OPEN** Stage 3 (OQ-PARTIAL-CLOSURE) |

**Do not** conflate Frontend deploy / production go-live with `COMPLETE` — deploy is **SAFE UNKNOWN** external to Factory closure.

---

## State History Principles

### Must preserve (state model scope)

| History element | Why |
|-----------------|-----|
| Ordered state occupancy segments | `runtime_state_code`, `entered_at`, `exited_at`, `occupancy_role` outcome |
| Transition ledger | Forward, rollback, rule_id, gate_refs_passed, handoff_ref |
| Active state snapshot pointer | Current code + effective since |
| Supersession markers | Post-rollback stale segments |
| Scope mask version | Charter changes affecting LR-07 |

### Belongs in related indexes (not state definition)

| Element | Owner index (Stage 1) | Why separated |
|---------|----------------------|---------------|
| Gate PASS/FAIL detail | Gate outcome index | Gate model Stage 4 |
| Handoff package contents | Handoff package data | Handoff model Stage 5 |
| Layer artefact bodies | Layer workstreams | Project holds refs only |
| Validation run logs | Layer + project ref | Not state vocabulary |
| Frontend code / deploy logs | Frontend workstream | Outside Factory states |
| Operator chat, tickets | External | Not canonical state history |

### History immutability

Declared transitions **append-only**. Correction = **new** declaration record referencing `corrects_transition_id`, not silent delete — storage format deferred.

---

## Relationship To Gates

State and gates — **orthogonal but coupled**:

```text
State  =  where the project stands in the layer chain
Gate   =  whether a specific transition INTO the next state is authorized
```

### Coupling rules (without Gate Results system)

| Rule | Statement |
|------|-----------|
| **SG-01** | Entering state `S` **implies** project claims prior state's exit gates satisfied — unless rollback returned to earlier `S`. |
| **SG-02** | Active state `S` **does not imply** all work inside `S` finished — only that project **occupies** `S`. |
| **SG-03** | Forward to `S+1` requires `RG-*` from STATE-TRANSITION-RULES §5 for that transition — **plus** layer gates where RUNTIME-GATES maps them. |
| **SG-04** | Open FAIL on blocking `RG-*` or layer gate → **no forward**; active unchanged (CS-04). |
| **SG-05** | Composite readiness (e.g. `RG-GENERATION_READY`) — project **indexes** constituent PASS records; definitions stay Runtime/layer. |
| **SG-06** | Gate outcome records **referenced** by progression ledger `gate_refs_passed`; full gate result schema — **Stage 4**, not Stage 2. |

### Operator «what blocks movement?»

At active state `S`, enumerate:

1. `RG-*` required for `S` → `S+1` not PASS;
2. Layer gates upstream of that `RG-*` still open;
3. Parallel legal LR-02/LR-03 if approaching `GENERATION_READY`;
4. Handoff blocked conditions for `HO-*` at boundary;
5. FT/DR violation if attempted skip.

**State model does not** store pass criteria — only **dependency** on gate PASS for progression eligibility.

---

## Relationship To Handoffs

| Rule | Statement |
|------|-----------|
| **SH-01** | Each forward TR transition across layer boundary **aligns** with one `HO-*` (binding map). |
| **SH-02** | Handoff **completion** is prerequisite for progression record — operator declares HO cleared. |
| **SH-03** | Handoff **package contents** (specs, FRONTEND_HANDOFF_PACKAGE) — **not** part of state code; indexed separately (Stage 1 handoff package data). |
| **SH-04** | `HO-12` blocked until Production QA PASS — enforces FT-07 at handoff layer. |
| **SH-05** | Rollback across handoff boundary **invalidates** handoff event records for superseded downstream segment. |

**State tells WHERE; handoff tells WHAT crossed the boundary.** Neither replaces the other.

---

## Explicit Non-Claims

This document and the Factory Project State Model it defines:

- **are not** Website Factory runtime, execution engine, or shipped product;
- **are not** an autonomous factory, agent system, MIG orchestration, or AI workflow;
- **are not** a queue, job scheduler, or work prioritization system;
- **are not** a workflow engine, BPMN executor, or n8n replacement;
- **are not** an application, dashboard, operator UI (RT-G12), or database (RT-G04);
- **are not** implementation — no code, validators CLI, CI binding, or automation;
- **do not** define JSON/YAML schemas, manifest file paths, folder layouts, passport format, or state store;
- **do not** define FACTORY-GATE-RESULTS, FACTORY-HANDOFF-PACKAGE, FACTORY-ENGINE-LIFECYCLE, or FACTORY-ENGINE-SYSTEM documents;
- **do not** modify Runtime Architecture, rename states, or add terminal states;
- **do not** claim automated transition enforcement or persistence (RT-G04, RT-G11 — FUTURE).

Human-operated declaration remains the v1 execution model per Runtime Architecture.

---

## Open Questions For Stage 3

| ID | Question | Notes |
|----|----------|-------|
| **OQ-S3-01** | Partial scope **effective path** — formal jump table when states `EXCLUDED` (LR-07) | Lifecycle model Stage 3 |
| **OQ-S3-02** | `FACTORY_TRACK_SUSPENDED` vs active state — operator conventions | Not a Runtime state |
| **OQ-S3-03** | Partial closure without `COMPLETE` — deliverable boundary | OQ-PARTIAL-CLOSURE |
| **OQ-S3-04** | Multiple `generation_id` / PHASE_SLICE — active state per slice vs project shell | OQ-06 from Stage 1 |
| **OQ-S3-05** | Cascade invalidation table — which ref types invalidate per RB-* target | Lifecycle + tracking |
| **OQ-S3-06** | Minimum progression record fields for RT-G10 manifest (when chartered) | Tracking model |
| **OQ-S3-07** | Extended types ER-01 — remain in `CLASSIFIED` until charter; state mask rules | Registry charter |

Stage 4+ (not Stage 3): gate namespace mapping table (ERA-W02), composite gate representation (OQ-04), handoff record minimum (OQ-08).

---

## Recommended Next Step

**Stage 3 — Factory Project Lifecycle Model (Engine Architecture v1):** bind progression, rollback invalidation, partial-scope paths, and LC/LS/AP alignment to **this** state model — **without** defining storage, manifests, or gate/handoff implementation systems.

Subsequent stages per Engine Readiness Audit: gate composition model (Stage 4) → handoff binding (Stage 5) → project tracking model (Stage 6).

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Physical storage of state history / progression ledger | **NOT DEFINED** — RT-G04, RT-G10 FUTURE |
| Partial closure canonical pattern | **OPEN** — OQ-S3-03 |
| Calendar for Engine Stages 3–6 | **not scheduled** |
| Triumph production deploy vs `COMPLETE` | **UNKNOWN** — external |

---

*Factory Project State Model v1 — Stage 2 complete. Architecture only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Project State Model v1

**Stage:** Factory Engine Architecture v1 — Stage 2 (Project State Model)  
**Deliverable:** `FACTORY-PROJECT-STATE-MODEL-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-STATE-MODEL-v1.md` (created)  
**Summary:** Определена каноническая модель состояния Factory Project как экземплярного занятия 14 Runtime states; зафиксированы current state, progression, transition ownership (Runtime rules / Project declarations), rollback и re-entry, terminal `COMPLETE`, принципы history и связи с gates/handoffs без storage и без новых state codes. Закрыт OQ-01 Stage 1 (Runtime binding).  
**Git:** no commit, no push (per task charter).
