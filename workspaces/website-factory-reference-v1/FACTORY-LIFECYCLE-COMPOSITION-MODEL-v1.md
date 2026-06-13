# REPORT — Factory Lifecycle Composition Model v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Factory Engine Architecture v1 — **Stage 5 only**  
**Контекст:** Website Factory Foundation Era **COMPLETE**; [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) **ACCEPTED** (Stage 1); [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) **ACCEPTED** (Stage 2); [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) **ACCEPTED** (Stage 3); [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) **ACCEPTED** (Stage 4); Engine Readiness Audit v1 — **PASS WITH WARNINGS**  
**Тип:** architecture only — **без** implementation, runtime product, agents, code, workflows, databases, automation, storage format, Lifecycle System  
**Связь:** [runtime-architecture/PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md), [runtime-architecture/STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md), [runtime-architecture/RUNTIME-HANDOFFS-v1.md](runtime-architecture/RUNTIME-HANDOFFS-v1.md)

---

## Purpose

Stage 1 ответил: **«Что движется?»** — [Factory Project](FACTORY-PROJECT-OBJECT-MODEL-v1.md).

Stage 2 ответил: **«Как это движется?»** — [модель состояния](FACTORY-PROJECT-STATE-MODEL-v1.md): occupancy, progression, rollback, re-entry.

Stage 3 ответил: **«Как это наблюдается?»** — [Project Tracking Model](FACTORY-PROJECT-TRACKING-MODEL-v1.md): visibility composition.

Stage 4 ответил: **«Что авторизует движение?»** — [Gate Composition Model](FACTORY-GATE-COMPOSITION-MODEL-v1.md): gate sufficiency, stale/invalid semantics.

Stage 5 отвечает: **«Как всё это складывается в полный lifecycle одного проекта?»** — **Lifecycle Composition Model**: единая логическая модель прохождения Factory Project от intake до closure **без** создания Lifecycle System, Runtime redesign или implementation.

### Зачем существует Lifecycle (Engine sense)

| Lifecycle **координирует** | Lifecycle **не владеет** |
|----------------------------|--------------------------|
| Связь между Object, State, Gates, Handoffs и Tracking в **одном нарративе** для оператора | Canonical state vocabulary, TR/FT/DR/RB rules — **Runtime** |
| Какой **lifecycle segment** активен относительно LC-* фаз | Определения `RG-*`, `GATE_*`, validation criteria — **Runtime + layers** |
| Что **завершено**, **остаётся**, **следует дальше** — derived composition | Тела layer artefacts, handoff package payloads — **layers / Generation Outputs** |
| Как **rollback** и **re-entry** меняют целостность lifecycle | Автоматическое исполнение, persistence, orchestration — **FUTURE / вне scope** |
| Когда lifecycle **завершён** (full или partial charter endpoint) | Frontend implementation, deploy, hosting — **post-Factory** |
| **Continuity** — непрерывность vs разрыв и восстановление | Foundation contract redesign, новые states/gates/handoffs |

**Lifecycle Composition Model** — это **composition layer** Engine: не новая подсистема, а правила **сборки** уже принятых моделей в ответы на operator questions **без** открытия всего workspace.

### Operator questions (Stage 5 scope)

| Вопрос | Ответ даёт Lifecycle Composition |
|--------|-------------------------------------|
| Где проект **начался**? | LC-00 / `NEW_PROJECT` + charter + identity shell |
| Где проект **сейчас**? | Active state + active lifecycle segment |
| Какой **segment активен**? | LC-* phase bound to active Runtime state |
| Что **завершено**? | Completed state occupancy + satisfied gates/handoffs for reached prefix |
| Что **остаётся**? | Eligibility snapshot + open gates + artefact gaps до declared endpoint |
| Что **дальше**? | Next eligible TR transition + blocking gate set + HO at boundary |
| Что после **rollback**? | Rollback cascade + stale/invalid indexes + re-entry path |
| Что после **re-entry**? | Fresh authorization requirements; history preserved |

Документ **не** заменяет [PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) и **не** добавляет LC IDs, states, gates или handoffs.

---

## Foundation Dependencies

Lifecycle Composition Model **наследует** Stage 1–4 и **компонует** только принятую Foundation + Runtime:

| Dependency | Role for lifecycle composition |
|------------|--------------------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Mandatory components, lifecycle-dependent bindings, authority tiers |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Active state, progression, rollback, re-entry, terminal rules |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | How lifecycle narrative **surfaces** to operator |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Authorization plane; stale/invalid cascade |
| [runtime-architecture/PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) | LC-00…LC-13, LR-*, LS-*, AP-* — **segment vocabulary** |
| [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) | 14 states — **не** переопределяются |
| [runtime-architecture/STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md) | TR/FT/DR/RB/LR/ER — movement legality |
| [runtime-architecture/RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) | `RG-*` at segment boundaries |
| [runtime-architecture/RUNTIME-HANDOFFS-v1.md](runtime-architecture/RUNTIME-HANDOFFS-v1.md) | `HO-*` at layer crossings |
| [generation-contracts/GENERATION-CONTRACT-v1.md](generation-contracts/GENERATION-CONTRACT-v1.md) | `scope_type`, `generation_id`, scope freeze |
| [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md) | Engine ↔ Runtime boundary |

**Authority:** Runtime owns LC-* phase labels and state semantics. Engine lifecycle composition **binds** Factory Project instance data to that vocabulary — **не** расширяет его.

---

## Lifecycle Composition Principles

### Composed lifecycle (logical model)

```text
┌─────────────────────────────────────────────────────────────────────┐
│              FACTORY LIFECYCLE (composition view)                    │
├─────────────────────────────────────────────────────────────────────┤
│  PROJECT OBJECT          identity, charter, scope, indexes           │
│       │                                                              │
│       ├── STATE PLANE     active state, history, progression ledger  │
│       ├── GATE PLANE      outcome index, active gate set, validity   │
│       ├── HANDOFF PLANE   HO events, package refs, ack               │
│       └── TRACKING VIEW   composed operator surface (Stage 3)        │
│                                                                      │
│  Declared endpoint       full chain → COMPLETE | partial → charter   │
│  Parallel legal track    LC-02…LC-09 work; must PASS before LC-10    │
└─────────────────────────────────────────────────────────────────────┘
         │ reads                          │ does not execute
         ▼                                ▼
   Runtime LC/TR/RG/HO              Layer workstreams
```

### Principle LCMP-1 — Composition, not execution

Lifecycle composition **describes** how planes interact. **Не** исполняет transitions, **не** evaluates gates, **не** delivers handoff packages.

### Principle LCMP-2 — Single active segment

**Active lifecycle segment** = LC-* phase, 1:1 с active `runtime_state_code` (full chain default). Ровно один segment активен в любой момент — зеркало CS-01.

### Principle LCMP-3 — Planes are orthogonal but synchronized at boundaries

| Plane | Lifecycle role at segment boundary |
|-------|--------------------------------------|
| **State** | Occupancy pointer moves on declared transition |
| **Gate** | Exit authorization for S → S+1 must be satisfied |
| **Handoff** | `HO-*` clearance records what crossed the boundary |
| **Artefact refs** | Layer outputs indexed; inputs to next segment |
| **Tracking** | Composes all planes into operator view |

Forward progression **legal** only when **all five** align at boundary (Stage 2 forward rules 1–8 + GC-05 handoff coupling).

### Principle LCMP-4 — History is append-only narrative

Lifecycle **не** стирает пройденные segments. Rollback **добавляет** новую ветку occupancy и invalidation markers — не rewrite.

### Principle LCMP-5 — Endpoint is charter-declared

Default endpoint = full chain through LC-13 / `COMPLETE`. Partial charter may declare **earlier endpoint** — lifecycle composition tracks **declared endpoint**, not assume full chain.

### Principle LCMP-6 — Parallel legal is a co-track, not a segment skip

Legal work **параллелен** LC-02…LC-09 (LR-01 Runtime). Lifecycle composition treats legal gates as **mandatory co-requirements** before LC-10 exit — **не** as alternate main-chain segment.

### Component binding table

| Stage model | Lifecycle composition contribution |
|-------------|-----------------------------------|
| **Object** | Scope boundary, identity anchor, indexes lifecycle planes attach to |
| **State** | **Where** in chain; progression events; rollback target |
| **Gate** | **Whether** exit authorized; stale sweep on rollback |
| **Handoff** | **What** crossed boundary; package ref linkage |
| **Tracking** | **How operator sees** composed lifecycle without merged authority |

---

## Lifecycle Segmentation

### Natural segments (inherited — no new IDs)

Runtime [PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) already defines **14 lifecycle phases** LC-00…LC-13, each 1:1 с Runtime state upon phase **completion** (target state = occupancy after forward transition into segment exit).

| Segment | LC ID | Target state (on segment exit) | Macro-group |
|---------|-------|--------------------------------|-------------|
| Intake | LC-00 | `NEW_PROJECT` (occupancy **in** segment) → exit to `CLASSIFIED` | **Architecture foundation** |
| Classification | LC-01 | `CLASSIFIED` | Architecture foundation |
| Blueprint | LC-02 | `BLUEPRINT_READY` | Architecture foundation |
| Page Architecture | LC-03 | `PAGE_READY` | Architecture foundation |
| Blocks | LC-04 | `BLOCK_READY` | Architecture foundation |
| Validation | LC-05 | `VALIDATED` | Architecture foundation |
| SEO | LC-06 | `SEO_READY` | **Experience layer** |
| Design | LC-07 | `DESIGN_READY` | Experience layer |
| Content | LC-08 | `CONTENT_READY` | Experience layer |
| Content Validation | LC-09 | `CONTENT_VALIDATED` | Experience layer |
| Generation Ready | LC-10 | `GENERATION_READY` | **Production package** |
| Production QA | LC-11 | `PRODUCTION_QA_READY` | Production package |
| Frontend Handoff | LC-12 | `FRONTEND_READY` | **Closure boundary** |
| Closure | LC-13 | `COMPLETE` | Closure boundary |

**Macro-groups** — Engine **composition labels only**; **не** Runtime states и **не** skip units.

```text
[ LC-00 … LC-09 ]  Architecture + experience binding
        ↓
[ LC-10 … LC-11 ]  Generation scope + production readiness
        ↓
[ LC-12 … LC-13 ]  Handoff + Factory closure
```

### What constitutes a segment

| Element | Definition |
|---------|------------|
| **Segment identity** | LC-* ID from Runtime |
| **Segment occupancy** | Project active state maps to segment whose **target state equals active code** while work proceeds toward exit gate |
| **Segment entry** | Forward transition into state S where S is segment target (or initial `NEW_PROJECT` at birth) |
| **Segment exit** | Forward transition from S to S+1 with gate PASS + HO cleared |
| **Segment work** | Intra-segment layer work **without** state change — validation runs, mapping, legal parallel |
| **Segment halt** | LS-* stop — **remain in segment**; active state unchanged |

**Active segment** = segment containing current active state. Operator «what lifecycle segment is active?» = LC label for active code.

### Partial scope segmentation (LR-07)

Charter may mark states `EXCLUDED` in scope mask. Segments whose target states are EXCLUDED:

| Treatment | Rule ID |
|-----------|---------|
| Never become active occupancy | **LCS-01** |
| Gates for excluded segments → `N_A` (GC-06) | **LCS-02** |
| History shows `N_A`, not COMPLETED | **LCS-03** |
| Effective path **jumps** documented TR-permitted edges only | **LCS-04** |

**Effective path principle:** when state S is EXCLUDED, forward progression **skips** S as occupancy — next applicable state is next **non-EXCLUDED** state in TR order **only** where charter documents the jump and DR-* order still satisfied for **included** layers. Charter **must** declare endpoint and exclusions; composition **does not** invent skip table beyond TR + documented charter.

| Partial pattern (examples) | Typical endpoint | Notes |
|----------------------------|------------------|-------|
| Design-only | `DESIGN_READY` | SEO/Content/Generation segments EXCLUDED |
| Architecture-only | `VALIDATED` | Experience + production segments EXCLUDED |
| Generation slice (`PHASE_SLICE`) | Charter-defined | May bind separate `generation_id`; shell lifecycle OPEN Stage 6 |
| Legal-only (`LEGAL_ONLY`) | Legal track completion | Main chain largely EXCLUDED; charter-driven |

---

## Lifecycle Progression

### How lifecycle advances

Lifecycle advances through **declared state transitions** (Stage 2), each synchronizing planes:

```text
Intra-segment work (same LC, same state)
    → layer artefacts produced
    → layer gates evaluated
    → exit RG-* approaches satisfaction

Segment boundary (forward transition)
    → exit RG-* PASS + valid
    → HO-* cleared
    → progression ledger entry
    → active state S → S+1
    → active segment LC-* → LC-*+1
    → artefact refs for new segment become relevant
```

### Advancement coupling rules

| Rule | ID | Statement |
|------|-----|-----------|
| Gate before move | **LCP-01** | No lifecycle segment exit without satisfied exit gate (GRS-01) |
| Handoff before move | **LCP-02** | No segment boundary crossing without HO clearance (SH-02) |
| State records move | **LCP-03** | Lifecycle **advances segment** only when active state changes — not on gate PASS alone |
| Halt preserves segment | **LCP-04** | LS-* → lifecycle **stays** in current segment until block cleared |
| Legal window | **LCP-05** | Approaching LC-10: parallel legal gates enter active set (GC-03, LCP-parallel) |
| Composite gates | **LCP-06** | LC-10 / LC-11 exits require composite rollup PASS (GC-02) |
| No skip-forward | **LCP-07** | FT-09 / FT-12–FT-15 — lifecycle **cannot** jump segments without occupying intermediate states (except LR-07 EXCLUDED skips) |

### Gate influence on advancement

Gates **authorize** segment exit — **не** segment entry (SG-01: entering S implies prior exit satisfied unless rollback).

| Lifecycle moment | Gate role |
|------------------|-----------|
| Mid-segment | Open constituents visible; block toward exit |
| Segment exit | Blocking `RG-*` must be satisfied (GS-*) |
| Post-rollback | Exit gates for re-traversed segments must be **fresh** ACTIVE PASS |
| Terminal | `RG-PROJECT_COMPLETE` — no further segment |

### Handoff influence on advancement

Each TR forward across layer boundary aligns with one `HO-*` (Stage 2 binding map):

| Handoff role | Lifecycle effect |
|--------------|------------------|
| **Declares** producer → consumer boundary crossed | Segment exit **recorded** in handoff plane |
| **Package ref** links spec bundle | Next segment work consumes via refs — not embedded in lifecycle |
| **Blocked HO** | Lifecycle **frozen** at segment despite gate PASS (GC-05) |
| **HO-12** | LC-12 entry blocked until Production QA plane satisfied (FT-07) |
| **Frontend ack** | Required for LC-12 → LC-13 progression |

**Lifecycle tells the story; handoff tells what crossed.**

### State progression influence

State is the **backbone** of lifecycle segmentation:

| State event | Lifecycle effect |
|-------------|------------------|
| Forward TR | Close prior segment occupancy; open new segment |
| Rollback RB | Rewind active segment; cascade invalidation (see Rollback) |
| Re-entry forward | Re-traverse segments with new progression events |
| `COMPLETE` | All segments through declared endpoint **closed**; Factory track terminal |

### Operator «what happens next?»

Derived answer chain:

1. Active segment (LC from active state)
2. If LS halt → «remediate [trigger]; remain in LC-*»
3. Else enumerate active gate set (Stage 4)
4. If gates satisfied → «eligible for transition to [next state / next LC-*] pending operator declaration»
5. If handoff blocked → cite HO-ID
6. If partial scope → next **applicable** non-EXCLUDED segment

---

## Lifecycle Continuity

### What makes lifecycle continuous

**Continuous Factory lifecycle** = operator can trace an **unbroken narrative** from intake identity through current position with **consistent** cross-plane indexes.

| Continuity criterion | ID | Requirement |
|---------------------|-----|-------------|
| Identity stable | **LCC-01** | Same project identity shell throughout |
| Active state coherent | **LCC-02** | Active state matches latest progression ledger |
| Gate validity coherent | **LCC-03** | No stale PASS treated as active for eligibility (TC-04) |
| Handoff alignment | **LCC-04** | Progression handoff_refs match declared HO events |
| Artefact refs aligned | **LCC-05** | Mandatory refs for completed segments present or explicitly gap-flagged |
| History append-only | **LCC-06** | No silent deletion of segments, gates, or handoffs |
| Charter version traceable | **LCC-07** | Scope mask changes documented when LR-07 amended |

### What breaks continuity

| Break type | Cause | Lifecycle signal |
|------------|-------|------------------|
| **Rollback** | Declared RB-* | Active segment rewinds; downstream planes invalidated |
| **Gate invalidation** | FAIL, STALE, upstream artefact INVALIDATED | Forward eligibility breaks; may require rollback or in-place rework |
| **Handoff rejection** | HO-12 / package incomplete | Segment freeze at LC-12 or rollback RB-12 |
| **Charter amendment** | Scope tier / endpoint change | Scope mask STALE review; may force RB-10 |
| **Integrity gap** | Undeclared transition | Active state ≠ ledger — **discontinuous until reconciled** |
| **Track suspension** | `FACTORY_TRACK_SUSPENDED` (logical metadata) | Factory lifecycle questions **frozen** at last declared truth |
| **Abandonment** | Charter cancelled | Remains at last active state — **not** terminal; continuity of **record** preserved |

**Continuity break ≠ project deletion.** History and invalidated records **remain visible**.

### What restores continuity

| Restoration path | Actions (conceptual) |
|------------------|---------------------|
| **Post-rollback re-forward** | Re-occupy segments; fresh gate PASS; re-declare HO; new artefact refs |
| **In-segment rework** | Same segment; fix artefacts; re-run validation; gate re-declaration — **no** rollback if active unchanged |
| **Reconciliation** | Operator declares correction record linking ledger gap |
| **Charter re-baseline** | Document new scope mask + endpoint; invalidate incompatible downstream refs |
| **Suspension lift** | Clear `FACTORY_TRACK_SUSPENDED`; resume from frozen active segment |

Restoration **never** bypasses FT-* / DR-* on re-forward (RE-01).

---

## Rollback Cascade Principles

Rollback is a **lifecycle discontinuity event** with **prescribed cascade** across planes. **Без** implementation — conceptual treatment only.

### Rollback event (composition view)

```text
Operator declares RB-* : from_state → to_state (rollback target)
    │
    ├─ State plane:     active → to_state; ledger ROLLBACK entry
    ├─ Gate plane:      gates for states STRICTLY ABOVE to_state → STALE (GST-01)
    ├─ Handoff plane:   HO events for boundaries above target → SUPERSEDED (HV-03)
    ├─ Artefact plane:  downstream refs above target → INVALIDATED (AV-03)
    └─ Tracking:        supersession markers visible; eligibility recomputed
```

**Above rollback target** = all Runtime states later in TR order than `to_state` that project had **occupied** or **claimed** via indexes.

### Cascade invalidation table (OQ-S5-01)

Logical mapping — **не** schema. «Invalidate» = status change in project indexes; **не** mutation of Foundation docs or layer artefact bodies.

| Rollback rule | Target state | Gate outcomes invalidated | Handoff events superseded | Artefact ref classes invalidated |
|---------------|--------------|---------------------------|---------------------------|----------------------------------|
| **RB-01** | `NEW_PROJECT` | All above `NEW_PROJECT` | HO-01 onward | Classification, blueprint, page, block, validation, SEO, design, content, generation, QA, handoff refs |
| **RB-02** | `CLASSIFIED` | Above `CLASSIFIED` | HO-02 onward | Blueprint through handoff refs |
| **RB-03** | `BLUEPRINT_READY` | Above `BLUEPRINT_READY` | HO-03 onward | Page contracts through handoff refs |
| **RB-04** | `PAGE_READY` | Above `PAGE_READY` | HO-04 onward | Block stacks through handoff refs |
| **RB-05** | `BLOCK_READY` | Above `BLOCK_READY` | HO-05 onward | Validation run, SEO through handoff refs |
| **RB-06** | `VALIDATED` | Above `VALIDATED` | HO-06 onward | SEO through handoff refs |
| **RB-07** | `SEO_READY` | Above `SEO_READY` | HO-07 onward | Design through handoff refs |
| **RB-08** | `DESIGN_READY` | Above `DESIGN_READY` | HO-08 onward | Content through handoff refs |
| **RB-09** | `CONTENT_READY` | Above `CONTENT_READY` | HO-09 onward | Content validation through handoff refs |
| **RB-10** | `CONTENT_VALIDATED` | Above `CONTENT_VALIDATED` | HO-10 onward | Generation slice, scope freeze, legal completion refs for generation exit, QA, handoff |
| **RB-11** | `GENERATION_READY` | Above `GENERATION_READY` | HO-11 onward | Production QA, FRONTEND_HANDOFF_PACKAGE refs |
| **RB-12** | `PRODUCTION_QA_READY` | Above `PRODUCTION_QA_READY` | HO-12 onward | Frontend handoff ack, handoff package consumption refs |

**Parallel legal:** rollback to target **before** LC-10 may STALE `RG-LEGAL_COMPLETE` / `RG-ENTITY_VERIFIED` if operator declares legal rework — **not automatic**; operator decides per charter.

**Scope freeze:** rollback from `GENERATION_READY` or below via RB-10 **invalidates** scope freeze marker — new forward path requires re-freeze at Generation Ready re-entry.

### Cascade principles

| Principle | ID | Statement |
|-----------|-----|-----------|
| Target preserved | **LRC-01** | Refs **at or before** rollback target remain **valid** unless independently contradicted |
| No upstream mutation | **LRC-02** | Cascade affects **project indexes only** — not Foundation layer authority |
| Composite inheritance | **LRC-03** | STALE children → composite parent STALE (GST-04) |
| History preserved | **LRC-04** | Prior COMPLETED segments → `SUPERSEDED_BY_ROLLBACK` — visible |
| No auto-rollback | **LRC-05** | Gate STALE alone **does not** auto-trigger RB — operator declares |
| Forbidden rollback | **LRC-06** | `COMPLETE` → any forbidden (FT-10); multi-hop backward without charter forbidden |
| Handoff package | **LRC-07** | Package **data** may exist on disk — project index marks ref INVALIDATED; operator manages physical cleanup **externally** |

### Lifecycle behaviour after rollback

| Aspect | Behaviour |
|--------|-----------|
| **Active segment** | LC of rollback target state |
| **Completed narrative** | Prefix through target **still** in history; downstream superseded |
| **Next forward** | Re-traverse from target following TR — each transition new event |
| **Endpoint unchanged** | Unless charter amended — declared endpoint still applies |
| **Tracking** | Must show rewind + stale/superseded markers (TV-02) |

---

## Re-entry Behaviour

Re-entry extends Stage 2 Re-entry Model in **lifecycle composition** context.

### Definition

**Re-entry** = project **occupies again** a lifecycle segment (Runtime state) already present in history after rollback or after stale gate invalidation requiring re-approval.

### What must be reconsidered on re-entry

| Element | Reconsideration |
|---------|-----------------|
| **Exit gates** for re-traversed segments | Fresh ACTIVE PASS required (R-03, GRS-04) |
| **Layer gates / validation runs** | Re-evaluation where upstream artefacts changed |
| **Handoffs** at re-crossed boundaries | New HO event records; prior SUPERSEDED |
| **Artefact refs** invalidated by cascade | Re-bind or replace refs before gate satisfaction |
| **Composite parents** | Re-rollup after constituents fresh |
| **Parallel legal** | Reconfirm if legal inputs changed |
| **Scope freeze** | Re-establish if re-entering LC-10 |
| **Frontend ack** | New ack if re-entering LC-12 |

### What must NOT be reconsidered

| Element | Stable across re-entry |
|---------|------------------------|
| **Project identity shell** | LCC-01 |
| **Charter** (unless explicit amendment) | Scope intent unless RB-10 scope change |
| **Runtime rules** | TR/FT/DR/RB unchanged |
| **Foundation layer contracts** | T1 authority — class-level |
| **Historical records** | Append-only; superseded markers remain |
| **Excluded segments (LR-07)** | Still N_A — no re-entry to never-applicable segments |
| **Terminal `COMPLETE`** | Not re-enterable (RE-02) |

### Re-entry vs intra-segment rework

| Pattern | Active state | Lifecycle label |
|---------|--------------|-----------------|
| **Intra-segment rework** (R-02) | Unchanged | Same LC; gate re-run — **not** re-entry |
| **Post-rollback re-forward** (R-01) | Changes on transitions | Re-entry on each re-occupied state |
| **Same-state re-occupancy after rollback to S** | Returns to S | Re-entry segment S |

### Re-entry progression

```text
Rollback to S*
    → cascade invalidation
    → intra-segment work at S* (optional)
    → fresh exit gate PASS
    → HO cleared
    → forward to S*+1  (new progression event — re-entry segment S*+1)
    → repeat until catches up to former position OR new charter endpoint
```

Prior «fast path» through segments **does not** authorize — only fresh ACTIVE gates.

---

## Partial Completion Principles

Partial completion addresses scopes **narrower than full LC-00…LC-13 chain** — **без** new Runtime states и **без** inventing closure categories.

### Partial scope (LR-07)

| Principle | ID | Statement |
|-----------|-----|-----------|
| Charter declares exclusions | **LPC-01** | EXCLUDED states documented in scope mask |
| Segments skipped, not hidden | **LPC-02** | EXCLUDED LC visible as N_A in lifecycle view |
| Endpoint declared | **LPC-03** | Charter names **last applicable state** as factory deliverable boundary |
| Gate endpoint follows state | **LPC-04** | Gate-complete relative to **declared endpoint** (GCO-01) — not full chain |
| No fake COMPLETE | **LPC-05** | Partial delivery **≠** `COMPLETE` unless charter explicitly includes LC-13 path |

### Partial lifecycle completion (without `COMPLETE`)

When charter endpoint is **before** `COMPLETE` (e.g. design-only ends at `DESIGN_READY`):

| Criterion | Requirement |
|-----------|-------------|
| Active state = charter endpoint state | Occupancy at declared last state |
| All non-EXCLUDED segments through endpoint **completed** in history | Prefix narrative closed |
| Gate-complete for prefix through endpoint `RG-*` | GCO-02…GCO-05 for prefix |
| Operator sign-off on partial factory closure | Logical charter closure record — **not** `RG-PROJECT_COMPLETE` unless at `COMPLETE` |
| Factory track status | `FACTORY_TRACK_CLOSED_PARTIAL` (logical metadata — **not** Runtime state) |
| Frontend / generation | May be **out of scope** — lifecycle composition **does not** imply handoff occurred |

**Distinction:**

| Outcome | Active state | Runtime terminal? | Factory narrative |
|---------|--------------|-------------------|-------------------|
| **Full closure** | `COMPLETE` | Yes (FT-10) | LC-13 complete |
| **Partial closure** | e.g. `DESIGN_READY` | No | Prefix complete; Factory track closed per charter |
| **Suspended** | Last active | No | Frozen mid-chain |
| **Blocked** | Any | No | Open gates / LS halt |

### Partially completed scope mid-chain

Project at `SEO_READY` with open downstream work is **partially complete relative to full endpoint** but **fully occupying** current segment — operator «what remains?» = eligibility to declared endpoint, not «partial project» in sense of closure.

### PHASE_SLICE / multi-generation

When charter binds multiple `generation_id` slices:

| Aspect | Composition treatment |
|--------|----------------------|
| Project shell lifecycle | Single active state pointer (default) |
| Slice scope | Each slice may have own artefact/gate refs — **OPEN** Stage 6 for index split |
| Segment re-entry | New slice may re-enter LC-10+ without full RB if charter defines — **requires charter** |

---

## Lifecycle Completion

### Full lifecycle completion (= Factory closure)

Lifecycle **fully complete** iff **all** conditions (composition of Stage 2 terminal + Stage 4 gate-complete):

| # | Criterion | Source |
|---|-----------|--------|
| 1 | Active `runtime_state_code` = `COMPLETE` | Stage 2 CS-03 |
| 2 | Active segment = LC-13 | Runtime binding |
| 3 | History includes completed occupancy through `FRONTEND_READY` | TR-13 |
| 4 | `RG-FRONTEND_HANDOFF_APPROVED` + `RG-PROJECT_COMPLETE` satisfied ACTIVE PASS | GCO-06 |
| 5 | HO-12 + HO-13 cleared with Frontend ack | Stage 1 handoff |
| 6 | Gate-complete for full chain endpoint | GCO-01 default |
| 7 | Operator closure AP-09 declared | PROJECT-LIFECYCLE |
| 8 | Tracking fully trackable at closure | TC-01…TC-07 |

**Lifecycle completion implies `COMPLETE` state.** **`COMPLETE` state with satisfied closure gates implies lifecycle completion** for full-chain charter.

### Relationship to COMPLETE state

| Concept | Scope |
|---------|-------|
| **`COMPLETE` (Runtime)** | Terminal state code — vocabulary |
| **Lifecycle completion (Engine)** | Composed narrative: all planes aligned at LC-13 |
| **Gate-complete** | Authorization plane closed through endpoint |
| **Trackability complete** | Observability plane coherent |

Lifecycle completion **is not**:

- Frontend production deploy
- Client site go-live
- Triumph workspace build success
- Registry entry creation (RT-G05 FUTURE)

### Partial lifecycle completion

See Partial Completion — endpoint before `COMPLETE` with `FACTORY_TRACK_CLOSED_PARTIAL`. **Not** equivalent to Runtime terminal.

### Incomplete lifecycle

| Situation | Classification |
|-----------|----------------|
| Mid-chain active state | **In progress** |
| LS halt | **Blocked** — not incomplete lifecycle record; incomplete **relative to endpoint** |
| Gate STALE after rollback | **Discontinuous** until restored |
| Abandoned charter | **Suspended narrative** at last state |

---

## Lifecycle Visibility

Lifecycle visibility = **what Tracking exposes** about composed lifecycle (Stage 3 implements; Stage 5 defines **content**).

### Tracking must expose about lifecycle

| Visibility element | Tier | Content |
|-------------------|------|---------|
| **Lifecycle origin** | A | Intake declaration: identity + charter + `NEW_PROJECT` entry in history |
| **Active segment** | A | LC-* label + active state code |
| **Segment history** | A | Ordered LC occupancy with COMPLETED / SUPERSEDED / N_A |
| **Declared endpoint** | A | Full chain default or charter partial endpoint |
| **Progress relative to endpoint** | B | Segments completed vs remaining to endpoint |
| **Parallel legal co-track status** | B | When in scope — visible before LC-10 |
| **Rollback / re-entry markers** | A | Visible in history + invalidation status |
| **Halt context** | A | LS-* annotation at current segment |
| **Next segment eligibility** | B | Derived — next LC if forward legal |
| **Partial closure flag** | B | `FACTORY_TRACK_CLOSED_PARTIAL` when applicable |
| **Suspension flag** | B | `FACTORY_TRACK_SUSPENDED` when applicable |

### Tracking must NOT expose as lifecycle authority

| Excluded | Why |
|----------|-----|
| Layer contract bodies | T1 — ref only |
| Gate pass/fail criteria | Definitions — not lifecycle |
| Handoff package payloads | Package data — ref only |
| Invented sub-segments / micro-states | Forbidden — no `SEO_IN_PROGRESS` |
| Automated predicted completion dates | Not in v1 model |
| Queue rank among projects | RT-G06 FUTURE |

### Operator single-view composition (lifecycle slice)

```text
LIFECYCLE VIEW (composed from Tracking)
──────────────────────────────────────
Origin:     [identity] started at LC-00 / NEW_PROJECT [date]
Now:        LC-* / [active state]  [halt? LS-*]
Endpoint:   [full COMPLETE | partial DESIGN_READY | …]
Done:       [LC-00 … LC-(n-1)] completed | [superseded segments greyed]
Active work: [open gates] + [artefact gaps] in current segment
Next:       [eligible LC-*+1 | blocked by RG-* | HO-*]
Continuity: [continuous | rollback at RB-* | suspended]
```

**Lifecycle visibility defers format** to RT-G10 FUTURE — composition rules only.

### `FACTORY_TRACK_SUSPENDED` (OQ-S5-03)

When charter suspends Factory work without terminal state:

| Aspect | Treatment |
|--------|-----------|
| Active state | **Frozen** at last declared — displayed unchanged |
| Active gate set | **Frozen** — not recomputed until suspension lifted |
| Lifecycle questions | «Remains» = resume from frozen segment |
| Distinction from LS halt | Suspension = **operator charter**; LS = **gate/block failure** |

---

## Explicit Non-Claims

This document and the Factory Lifecycle Composition Model it defines:

- **are not** a Website Factory runtime, execution engine, or shipped product;
- **are not** an autonomous factory, agent system, MIG orchestration, or AI workflow;
- **are not** a queue, job scheduler, or work prioritization system;
- **are not** a workflow engine, BPMN executor, or n8n replacement;
- **are not** an orchestrator or automation layer;
- **are not** an application, dashboard, operator UI (RT-G12), or CLI;
- **are not** implementation — no code, validators, CI binding, or agents;
- **are not** a storage layer, database, file format, state store, or **lifecycle database**;
- **are not** a Lifecycle System — no executor, scheduler, or lifecycle engine product;
- **are not** FACTORY-ENGINE-LIFECYCLE, FACTORY-PROJECT-MANIFEST, FACTORY-PROJECT-PASSPORT, FACTORY-GATE-RESULTS, FACTORY-HANDOFF-PACKAGE, FACTORY-ENGINE-SYSTEM, or FACTORY-STATE-STORE documents;
- **do not** define JSON/YAML schemas, field lists, folder structures, manifests, passports, or persistence;
- **do not** modify Runtime Architecture, add states, gates, handoffs, or LC phases;
- **do not** claim automated lifecycle enforcement, project registry (RT-G05), or manifest standard (RT-G10).

Human-operated declaration remains the v1 lifecycle model per Runtime Architecture.

---

## Open Questions For Stage 6

| ID | Question | Primary dependency |
|----|----------|-------------------|
| **OQ-S6-01** | **Handoff binding model** — minimum HO event semantics, gate–HO coupling at boundary, package ref rules (OQ-S5-06 deferred) | Engine Stage 6 or parallel charter |
| **OQ-S6-02** | **Engine system boundary** — RT-G09 documentation closure; relationship to RT-G05 registry (OQ-S5-07) | FACTORY-ENGINE-SYSTEM charter |
| **OQ-S6-03** | **PHASE_SLICE / multi-`generation_id`** — shell vs slice lifecycle indexes (OQ-S5-05) | Generation binding + tracking |
| **OQ-S6-04** | **Partial scope jump table** — formal TR edges when multiple consecutive EXCLUDED states | Charter templates |
| **OQ-S6-05** | **RT-G10 manifest** — which lifecycle composition elements may serialize (OQ-S5-08) | Manifest charter — not design in Stage 6 by default |
| **OQ-S6-06** | **Extended types ER-01** — lifecycle prerequisites before full production path (OQ-S5-09) | Registry charter |
| **OQ-S6-07** | **Chrome blocks without `block_id`** (ERA-W01) — lifecycle artefact ref conventions | Engine charter |
| **OQ-S6-08** | **`PASS_WITH_WARNINGS` validation** — lifecycle gate decision composition (OQ-S5-11) | Validation + AP-* binding |
| **OQ-S6-09** | **`FACTORY_TRACK_CLOSED_PARTIAL` vs gate endpoint** — operator convention standardization | Operational playbook |
| **OQ-S6-10** | **External workspace pointers** (ERA-W03) — lifecycle ref discipline vs canonical project refs | Tracking + charter |
| **OQ-S6-11** | **Tracking ↔ lifecycle composition** — final alignment audit across Stages 1–5 | Engine integration pass |

---

## Recommended Next Step

**Stage 6 — Factory Engine System Boundary (Engine Architecture v1):** close RT-G09 documentation charter — define how Stages 1–5 compose into Engine **system boundary** document, resolve handoff binding minimum semantics, and align with RT-G05/RT-G10 **without** creating runtime, storage, manifest implementation, or FACTORY-ENGINE-SYSTEM implementation product.

Optional parallel: **Handoff Binding Model** if chartered separately from system boundary — formalize `HO-*` event records referenced throughout this lifecycle composition.

Optional P3 hygiene (non-blocking): sync stale RUNTIME-ROADMAP acceptance checkbox per ERA-W05.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Physical serialization of lifecycle composition view | **NOT DEFINED** — RT-G10 FUTURE |
| Automated lifecycle orchestrator | **FUTURE** — explicitly not Lifecycle System |
| Calendar for Engine Stage 6 | **not scheduled** |
| Triumph production deploy vs lifecycle closure | **UNKNOWN** — external |
| Whether partial closure metadata becomes RT-G10 field | **requires manifest charter** |

---

*Factory Lifecycle Composition Model v1 — Stage 5 complete. Architecture only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Lifecycle Composition Model v1

**Stage:** Factory Engine Architecture v1 — Stage 5 (Lifecycle Composition Model)  
**Deliverable:** `FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md` (created)  
**Summary:** Определена Lifecycle Composition Model: как Object, State, Gate Composition, Handoffs и Tracking складываются в полный lifecycle одного Factory Project; сегментация по LC-00…LC-13 без новых states; progression/continuity; rollback cascade table; re-entry; partial completion; lifecycle completion vs `COMPLETE`; lifecycle visibility через Tracking; закрыты OQ-S5-01…OQ-S5-04, OQ-S5-03 из Stage 4 — без Lifecycle System, runtime, storage, schemas, manifests.  
**Git:** no commit, no push (per task charter).
