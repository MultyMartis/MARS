# REPORT — Factory Gate Composition Model v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Factory Engine Architecture v1 — **Stage 4 only**  
**Контекст:** Website Factory Foundation Era **COMPLETE**; [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) **ACCEPTED** (Stage 1); [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) **ACCEPTED** (Stage 2); [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) **ACCEPTED** (Stage 3); Engine Readiness Audit v1 — **PASS WITH WARNINGS**  
**Тип:** architecture only — **без** implementation, runtime product, agents, code, workflows, databases, automation, storage format, Gate Results system  
**Связь:** [runtime-architecture/RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md), [runtime-architecture/STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md), [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md)

---

## Purpose

Stage 1 ответил: **«Что движется?»** — [Factory Project](FACTORY-PROJECT-OBJECT-MODEL-v1.md).

Stage 2 ответил: **«Как это движется?»** — [модель состояния](FACTORY-PROJECT-STATE-MODEL-v1.md): occupancy, progression, rollback, re-entry.

Stage 3 ответил: **«Как это наблюдается?»** — [Project Tracking Model](FACTORY-PROJECT-TRACKING-MODEL-v1.md): visibility composition без хранилища.

Stage 4 отвечает: **«Что авторизует движение?»** — **Gate Composition Model**: как gates **участвуют в Engine** для одного Factory Project, без создания Gate Results System, storage, schemas или Runtime redesign.

### Зачем существуют gates

Gates — **контрольные точки авторизации** движения Factory Project по canonical chain. Каждый gate фиксирует, что **определённые условия Foundation + Runtime** выполнены **для этого production case** и оператор **объявил** результат.

| Gate **авторизует** | Gate **не авторизует** |
|---------------------|------------------------|
| Forward state transition, для которого gate указан в STATE-TRANSITION-RULES §5 | Смену state без operator declaration |
| Handoff clearance на границе слоя, когда Runtime связывает gate с `HO-*` | Автоматическое продвижение, CI/webhook enforcement |
| Composite readiness (Generation Ready, Production QA Pass) как **rollup** upstream условий | Изменение layer contracts, Legal Pack, Registry |
| Parallel legal track completion перед `GENERATION_READY` (LR-01–LR-03) | Frontend implementation, deploy, hosting |
| Re-entry forward path после rollback — **после** повторной оценки | Skip-forward (FT-09, FT-12–FT-15) |
| Operator sign-off там, где Lifecycle требует AP-* | Приоритет в очереди проектов |

### Operator questions (Stage 4 scope)

| Вопрос | Ответ даёт Gate Composition Model |
|--------|-----------------------------------|
| Почему проект **может** двигаться вперёд? | Blocking `RG-*` для active → next = PASS + **valid**; constituents satisfied; handoff cleared |
| Почему **не может**? | Open / FAIL / **stale** / **invalid** gate; parallel legal block; handoff blocked; FT/DR violation |
| Какие gates **важны сейчас**? | **Active gate set** — blocking exit gate + open constituents + parallel legal if in window |
| Какие gates **уже satisfied**? | Outcome index: PASS + validity = ACTIVE |
| Какие gates **stale**? | Prior PASS, invalidated by rollback or upstream rework without re-declaration |
| Какие gates **invalid**? | FAIL, BLOCKED, superseded, or contradicted by invalidated artefact refs |

Документ **не** заменяет [RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) и **не** добавляет `RG-*` IDs.

---

## Foundation Dependencies

Gate Composition Model **наследует** Stage 1–3 и **компонует** только принятую Foundation + Runtime:

| Dependency | Role for gate composition |
|------------|---------------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Gate outcome index; three namespaces; composite Generation Ready |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | SG-01…SG-06; forward eligibility; rollback stale semantics |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | GV-01…GV-05; gate visibility; **does not own** composition rules |
| [runtime-architecture/RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) | **Единственный** источник `RG-*` definitions и dependency graph |
| [runtime-architecture/STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md) | Gate-gated transitions §5; parallel legal LR-01–LR-03 |
| [runtime-architecture/PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) | LS-* halt; AP-* sign-offs |
| [generation-contracts/GENERATION-GATES-v1.md](generation-contracts/GENERATION-GATES-v1.md) | Layer `GATE_*` for Generation scope |
| [production-qa/PRODUCTION-QA-GATES-v1.md](production-qa/PRODUCTION-QA-GATES-v1.md) | Layer `GATE_*` for Production QA rollup |
| [page-block-validation/VALIDATION-CONTRACT-v1.md](page-block-validation/VALIDATION-CONTRACT-v1.md) | Validation PASS/FAIL semantics for block stack |
| [content-validation/](content-validation/) validation contracts | Content validation PASS/FAIL semantics |
| [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md) | ERA-W02 triple namespace; mapping charter |

**Authority:** при конфликте pass/fail **criteria** → defining layer doc wins. При конфликте «какой `RG-*` блокирует TR-06» → Runtime wins. При конфликте «passed **this** project on date X» → Project gate outcome index (Engine), **используя** Runtime gate IDs.

---

## Runtime Binding Principles

### Principle GB-1 — Reference, never redefine

Engine **consumes** `RG-*` из RUNTIME-GATES как **read-only vocabulary**. Gate Composition Model **не** добавляет, не переименовывает и не ослабляет meta-gates.

### Principle GB-2 — Class vs instance

| Layer | Owns |
|-------|------|
| **Runtime** | Gate **definition**: purpose, inputs, pass/fail criteria, unlocks-state, dependency graph |
| **Factory Project (Engine)** | Gate **instance composition**: outcome records, validity status, constituent rollup for **this** project |

Runtime отвечает: «Что означает `RG-GENERATION_READY`?»  
Engine отвечает: «Как **этот** проект **составляет** readiness из upstream PASS refs?»

### Principle GB-3 — Transition binding is imported

Какой `RG-*` требуется для перехода active → next — **только** из STATE-TRANSITION-RULES §5 + RUNTIME-GATES maps. Engine **не** вводит дополнительные blocking gates для forward без supersession charter (ERA-W07).

### Principle GB-4 — Layer gates are constituents, not substitutes

`RG-VALIDATION_PASS` **координирует** Page Block Validation PASS; **не заменяет** validation contract. Аналогично: `RG-GENERATION_READY` → GENERATION-GATES; `RG-PRODUCTION_QA_PASS` → PRODUCTION-QA-GATES.

### Principle GB-5 — Human declaration boundary

Gate PASS для project instance = operator-declared outcome + sign-off where AP-* applies. Engine composition **не** implies automated evaluator (RT-G01, RT-G03, RT-G11 — FUTURE).

### Runtime binding map (Engine consumption)

Engine **reads** dependency graph из RUNTIME-GATES §4 — **не** дублирует criteria:

```text
RG-INTAKE_COMPLETE → … → RG-CONTENT_VALIDATION_PASS
    → [RG-LEGAL_COMPLETE + RG-ENTITY_VERIFIED if required]
    → RG-GENERATION_READY → RG-PRODUCTION_QA_PASS
    → RG-FRONTEND_HANDOFF_APPROVED → RG-PROJECT_COMPLETE
```

Для каждого active state **exit authorization** = `RG-*` из binding map в [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) (Runtime binding map table).

---

## Gate Ownership

Три complementary namespaces (ERA-W02) — **definitions vs instance**:

| Namespace | Definer (class) | Engine / Project holds (instance) |
|-----------|-----------------|-----------------------------------|
| **`RG-*`** | RUNTIME-GATES-v1 | Outcome record + validity + sign-off ref |
| **Layer `GATE_*`** | e.g. GENERATION-GATES, PRODUCTION-QA-GATES | Outcome refs **mapped to** parent `RG-*` |
| **Validation gates** | Page Block Validation, Content Validation contracts | PASS/FAIL run ref **mapped to** `RG-VALIDATION_PASS` / `RG-CONTENT_VALIDATION_PASS` |

### Ownership split (extended)

| Belongs to **gate system** (definitions) | Belongs to **Project / Tracking** (instance) |
|------------------------------------------|-----------------------------------------------|
| Gate ID, purpose, inputs, pass/fail criteria | That **this** project: outcome + validity status |
| `RG-*` dependency graph | **Active gate set** relative to active state |
| Layer `GATE_*` catalogues | Constituent outcome refs under composite `RG-*` |
| Validation PASS/FAIL rule text | Validation run ref + summary outcome |
| HITL AP-* **requirements** | AP-* **records** linked to outcomes |
| Failure remediation playbooks | Remediation **status pointer** (not playbook text) |

| Belongs to **Runtime** only | Belongs to **Tracking** only |
|------------------------------|------------------------------|
| `RG-*`, TR/FT/DR gate-gated rules | **Visibility** of outcomes (GV-*), stale markers |
| HO-* blocked conditions **definitions** | Display rollup for composite gates |
| — | Eligibility snapshot **derivation** from gate index |

| Belongs to **State Model** (Stage 2) | Belongs to **Gate Composition** (Stage 4) |
|--------------------------------------|-------------------------------------------|
| Forward eligibility **uses** gate PASS | **What constitutes** satisfied / stale / invalid gate |
| Rollback marks stale **requirement** | **Namespace mapping** and composite composition |
| SG-01…SG-06 coupling rules | **Active gate set** enumeration logic |

**Recording:** operator / project tracking — human-declared v1. **No** Gate Results System, **no** gate database.

---

## Gate Composition Principles

### What constitutes a gate **for a project**

**Project gate instance** (logical composition, not a storage schema) = **authorization claim** that a defined gate was evaluated for **this** production case.

Минимальная логическая composition unit:

```text
┌─────────────────────────────────────────────────────────┐
│              PROJECT GATE INSTANCE (logical)             │
├─────────────────────────────────────────────────────────┤
│  Gate reference        ← RG-* and/or mapped GATE_* /     │
│                          validation run ref              │
│  Outcome status        ← PASS | FAIL | BLOCKED |         │
│                          NOT_EVALUATED                   │
│  Validity status       ← ACTIVE | STALE | INVALID |      │
│                          SUPERSEDED                    │
│  Scope applicability   ← APPLICABLE | N_A | EXCLUDED     │
│                          (LR-07 partial scope)           │
│  Operator declaration  ← who, when (logical); AP-* link  │
│  Input refs            ← artefact / handoff refs used    │
│                          (not bodies)                    │
│  Constituent refs      ← for composite RG-* only         │
└─────────────────────────────────────────────────────────┘
```

**Gate composition** для проекта = **gate outcome index** как ordered set of instance units + **derived views**:

| Derived view | Definition |
|--------------|------------|
| **Active gate set** | Gates that **matter now** for forward eligibility from active state |
| **Satisfied set** | PASS + validity ACTIVE + scope APPLICABLE |
| **Open set** | NOT_EVALUATED, FAIL, BLOCKED, or constituent gap under composite |
| **Stale set** | PASS recorded but validity STALE |
| **Invalid set** | validity INVALID or SUPERSEDED |

### How multiple requirements combine

| Composition pattern | Rule ID | Statement |
|---------------------|---------|-----------|
| **Sequential chain** | **GC-01** | Primary path: each `RG-*` depends on prior `RG-*` PASS per RUNTIME-GATES §4 |
| **Composite rollup** | **GC-02** | `RG-GENERATION_READY`, `RG-PRODUCTION_QA_PASS` = PASS iff **all mandatory constituents** PASS + operator sign-off on composite |
| **Parallel legal** | **GC-03** | `RG-LEGAL_COMPLETE` (+ conditional `RG-ENTITY_VERIFIED`) **AND** upstream chain before TR-10 |
| **Layer backing** | **GC-04** | `RG-*` PASS **insufficient** if mapped layer `GATE_*` or validation run ref open/FAIL |
| **Handoff coupling** | **GC-05** | Gate PASS at boundary **does not replace** `HO-*` clearance — both required for progression (Stage 2 forward rules) |
| **Partial scope** | **GC-06** | Gates for `EXCLUDED` states → scope `N_A` — **omit** from active gate set, not treated as open |

### Gate visibility vs gate composition

| Concern | Gate **composition** (Stage 4) | Gate **visibility** (Stage 3) |
|---------|-------------------------------|--------------------------------|
| What is satisfied / stale / invalid | **Defines** semantics | **Shows** index status |
| Namespace mapping | **Defines** RG ↔ GATE_* ↔ validation | **References** mapping; no criteria text |
| Active gate set logic | **Defines** derivation | **Displays** derived set |
| Composite rollup rules | **Defines** constituent requirements | **Shows** rollup + expandable refs (GV-04) |

Tracking **implements visibility** over composition rules — **не** переопределяет sufficiency.

### Namespace mapping table (ERA-W02 / OQ-S4-01)

Logical mapping — **не** schema. Criteria remain in defining docs.

| Primary `RG-*` | Mapped layer `GATE_*` (where applicable) | Validation / other input |
|----------------|--------------------------------------------|--------------------------|
| `RG-INTAKE_COMPLETE` | — | Charter, scope tier (HO-01 inputs) |
| `RG-CLASSIFICATION_COMPLETE` | — | Registry `site_type_code` compliance |
| `RG-BLUEPRINT_APPROVED` | `GATE_BLUEPRINT_APPROVED` | Blueprint ref |
| `RG-PAGE_ARCHITECTURE_APPROVED` | `GATE_PAGE_ARCHITECTURE_APPROVED` | PAGE-CONTRACT set |
| `RG-BLOCK_MAPPING_COMPLETE` | (within architecture completeness) | Block mapping audit |
| `RG-VALIDATION_PASS` | `GATE_BLOCK_VALIDATION_PASS` | Page Block Validation run PASS |
| `RG-SEO_APPROVED` | `GATE_SEO_APPROVED` | SEO contracts |
| `RG-DESIGN_APPROVED` | `GATE_DESIGN_APPROVED` | `VF_*` bindings |
| `RG-CONTENT_APPROVED` | `GATE_CONTENT_APPROVED` | Content signal bindings |
| `RG-CONTENT_VALIDATION_PASS` | `GATE_CONTENT_VALIDATION_PASS` | Content Validation run PASS |
| `RG-LEGAL_COMPLETE` | `GATE_LEGAL_PACK_PASS` | Legal Pack mapping |
| `RG-ENTITY_VERIFIED` | `GATE_ENTITY_CARD_READY` | Entity Card (conditional) |
| `RG-GENERATION_READY` | `GATE_GENERATION_READY` | **Composite**: all mandatory upstream `RG-*` + GENERATION gates |
| `RG-PRODUCTION_QA_PASS` | `GATE_PRODUCTION_QA_PASS` | **Composite**: PRODUCTION-QA-GATES categories |
| `RG-FRONTEND_HANDOFF_APPROVED` | `GATE_FRONTEND_HANDOFF_APPROVED` | FRONTEND_HANDOFF_PACKAGE + ack |
| `RG-PROJECT_COMPLETE` | — | Closure checklist; prior handoff gates |

**Composite representation (OQ-S4-02):** one **parent** outcome record for `RG-GENERATION_READY` / `RG-PRODUCTION_QA_PASS` with **constituent refs** to child `RG-*`, `GATE_*`, and validation refs — rollup status derived, criteria not duplicated.

---

## Gate Sufficiency

### When a gate is **satisfied**

Gate **satisfied** for forward eligibility iff **все** условия:

| # | Condition | ID |
|---|-----------|-----|
| 1 | Outcome = PASS (or documented conditional skip: entity NOT_APPLICABLE) | **GS-01** |
| 2 | Validity = ACTIVE (not STALE, not INVALID) | **GS-02** |
| 3 | Scope applicability = APPLICABLE (not EXCLUDED / N_A for this charter) | **GS-03** |
| 4 | Mapped layer `GATE_*` constituents satisfied where GC-04 applies | **GS-04** |
| 5 | Validation run ref = PASS where mapped | **GS-05** |
| 6 | Required input artefact refs present and not INVALIDATED | **GS-06** |
| 7 | Operator sign-off recorded where AP-* or Runtime requires | **GS-07** |
| 8 | For composite: **all** mandatory constituents satisfied per GC-02 | **GS-08** |

**Satisfied ≠ movement occurred.** Gate may be satisfied while project **remains** in active state (intra-state work complete; transition not yet declared).

### When a gate is **insufficient**

| Situation | Insufficiency |
|-----------|---------------|
| NOT_EVALUATED | Gate never declared for required scope |
| FAIL or BLOCKED | Explicit non-PASS |
| Constituent gap under composite | Parent cannot be satisfied |
| Missing sign-off | PASS claimed without AP-* where required |
| Missing validation run ref | `RG-VALIDATION_PASS` without PASS run |
| Handoff blocked | Gate PASS but HO blocked conditions open — **blocks progression**, not necessarily gate outcome rewrite |

### When a gate becomes **stale**

**Stale** = historical PASS **no longer authorizes** forward until re-evaluated and re-declared.

| Trigger | ID | Effect |
|---------|-----|--------|
| Rollback active state to earlier code (RB-*) | **GST-01** | All `RG-*` tied to states **above** rollback target → STALE |
| Upstream artefact ref INVALIDATED without new gate declaration | **GST-02** | Dependent `RG-*` / `GATE_*` → STALE |
| Scope charter amendment affecting LR-07 | **GST-03** | Gates for newly EXCLUDED/APPLICABLE states → STALE or N_A review |
| Composite parent PASS while constituent later marked STALE | **GST-04** | Parent **inherits** STALE |

Stale records **remain visible** (GV-05) — not deleted.

### When a gate becomes **invalid**

**Invalid** = outcome **must not** be used for eligibility; stronger than stale in FAIL cases.

| Trigger | ID | Effect |
|---------|-----|--------|
| Explicit FAIL outcome | **GIN-01** | INVALID until new PASS declaration |
| Operator correction superseding prior PASS | **GIN-02** | Prior → SUPERSEDED; replacement ACTIVE or FAIL |
| Rollback + operator declares gate void for rework | **GIN-03** | INVALID (optional operator narrative — not criteria) |
| Contradiction: PASS but artefact ref INVALIDATED and operator reconciles as void | **GIN-04** | INVALID |

**Stale vs invalid:**

| Status | Typical cause | Re-entry path |
|--------|---------------|---------------|
| **STALE** | Rollback; upstream change | Re-evaluate + new PASS declaration |
| **INVALID** | FAIL; superseded false PASS | Fix + new evaluation; prior kept in history |
| **SUPERSEDED** | Correction chain | New record is authoritative |

---

## Gate Dependency Model

Gates **may depend on** the following — with boundaries:

### Dependency on **artefacts**

| Allowed | Boundary |
|---------|----------|
| Gate inputs reference layer artefact refs (blueprint, contracts, validation runs) | Engine **indexes refs**; layer owns bodies |
| Artefact INVALIDATED → dependent gates STALE/INVALID | Engine **does not** mutate artefacts |
| Missing ref → gate insufficient | Operator declares or rolls back |

### Dependency on **handoffs**

| Allowed | Boundary |
|---------|----------|
| Gate PASS often aligns with `HO-*` boundary (Stage 2 SH-*) | Handoff **clearance** separate record |
| `RG-FRONTEND_HANDOFF_APPROVED` depends on package completeness per GENERATION-OUTPUTS | Package **contents** not embedded in gate record |
| HO-12 blocked until Production QA PASS | Gate composition **respects** FT-07 via gate + handoff coupling |

### Dependency on **previous gates**

| Allowed | Boundary |
|---------|----------|
| Sequential `RG-*` chain per RUNTIME-GATES §4 | Engine **does not** shorten chain |
| Composite rollup of prior PASS | Parent **cannot** PASS if child STALE/INVALID |
| Layer `GATE_*` backing single `RG-*` | Mapping table only — no new IDs |

### Dependency on **state position**

| Allowed | Boundary |
|---------|----------|
| **Active gate set** derived from active `runtime_state_code` | State **does not** define pass criteria |
| Entering state S **implies** prior exit gate satisfied (SG-01) unless rollback | Occupying S **does not imply** exit gate PASS (SG-02) |
| Parallel legal worked in LC-02–LC-09 but must PASS before `GENERATION_READY` (LR-01) | Legal gates in active set when approaching TR-10 |

### Forbidden dependencies

| Forbidden | Why |
|-----------|-----|
| Gate depending on Frontend deploy / hosting | Post-Factory / SAFE UNKNOWN |
| Gate depending on queue position | Not per-project |
| New `RG-*` for intra-workstream milestones | Use layer gates + intra-state work |
| Automated inference without operator declaration | v1 model |

---

## Gate Relationship To State

State = **where**; gate = **whether exit to next is authorized**. Orthogonal but coupled (Stage 2 SG-*).

```text
ACTIVE STATE (S)                    GATE PLANE
─────────────────                   ─────────────────────────────
Occupancy pointer          ←───→    Exit gate for S → S+1
Progression ledger                  Full chain validity (stale sweep)
Rollback target                     Cascade STALE above target
Re-entry                            Fresh PASS required (R-03)
```

| Rule | ID | Statement |
|------|-----|-----------|
| Forward requires exit gate | **GRS-01** | TR forward from S requires `RG-*` for S→S+1 PASS + valid (Stage 2 forward rules 1–8) |
| Intra-state work | **GRS-02** | Work inside S toward layer gates **without** transition — active unchanged; open constituents visible |
| Rollback cascade | **GRS-03** | RB-* → gates for states above target STALE/INVALID per GST-01 |
| Re-entry | **GRS-04** | Re-forward through S→S+1 requires **new** PASS; prior COMPLETED occupancy ≠ current authorization |
| Halt | **GRS-05** | LS-* stop: active frozen; **blocking gate** visible in active gate set |
| Terminal | **GRS-06** | `COMPLETE`: `RG-PROJECT_COMPLETE` satisfied; no outbound gates |
| Partial scope | **GRS-07** | EXCLUDED states: gates N_A; effective path jumps documented in charter — **lifecycle Stage 5** |

**Active gate set derivation (from active state S):**

1. **Primary blocking gate** — `RG-*` required for TR transition S → S+1 (if not terminal).
2. **Open constituents** — layer `GATE_*` / validation refs mapped to primary or composite parent still insufficient.
3. **Parallel legal** — if active ∈ {approaching `CONTENT_VALIDATED` … `GENERATION_READY`} and scope requires: `RG-LEGAL_COMPLETE`, `RG-ENTITY_VERIFIED`.
4. **Composite parents** — if primary is composite, enumerate mandatory constituents not satisfied.
5. **Exclude** — gates for EXCLUDED states (GC-06); gates already satisfied for **prior** transitions unless STALE.

---

## Gate Relationship To Tracking

| Tracking must know (from Stage 3) | Gate composition supplies |
|-----------------------------------|---------------------------|
| Outcome PASS/FAIL/blocked | Sufficiency rules (GS-*) |
| Stale / invalid markers | GST-* / GIN-* semantics |
| Composite rollup display | GC-02 + constituent refs |
| Active vs historical | Validity status + active gate set |
| Operator sign-off refs | GS-07 linkage |

| Tracking must **not** know | Owner |
|----------------------------|-------|
| Pass/fail criteria text | RUNTIME-GATES, layer docs |
| Failure playbooks | RUNTIME-FAILURE-LIBRARY |
| Automated evaluation logic | FUTURE |
| **Composition derivation rules** | **Stage 4** — tracking **consumes**, does not redefine |

| Rule | ID | Statement |
|------|-----|-----------|
| Outcome without criteria | **GRT-01** | Tracking shows status; composition doc defines **when** status counts |
| Eligibility snapshot | **GRT-02** | Derived from gate index + GRS active gate set — not stored as new state |
| Integrity | **GRT-03** | Undeclared stale PASS treated as active → **partial trackability** (TC-04) until reconciled |
| Append-only | **GRT-04** | New PASS after STALE → new record; prior remains STALE |

**Minimum outcome record content (OQ-S4-03)** — logical minimum, **not** a schema:

- namespace-qualified gate reference (`RG-*` and/or mapped `GATE_*` / validation ref id),
- outcome status,
- validity status,
- scope applicability,
- operator declaration anchor (logical who/when),
- sign-off ref when AP-* applies,
- input artefact refs (pointers only),
- constituent refs for composite parents,
- optional link to progression ledger transition that **relied on** this gate.

Physical serialization — **NOT DEFINED** (RT-G10 FUTURE). **Not** FACTORY-GATE-RESULTS.

---

## Gate Failure Principles

Without implementation — **operative principles** only:

### When a gate **fails**

| Principle | ID | Statement |
|-----------|-----|-----------|
| Active state preserved | **GF-01** | FAIL → no forward transition; active unchanged (CS-04) |
| FAIL visible | **GF-02** | Outcome INVALID/FAIL remains in index (GV-03) |
| Halt narrative | **GF-03** | LS-* stop aligns with open blocking gate |
| Layer failure libraries | **GF-04** | Remediation guidance **referenced**, not copied into gate record |
| Composite failure | **GF-05** | Any mandatory constituent FAIL → parent insufficient |
| Parallel legal FAIL | **GF-06** | Blocks TR-10 even if main chain gates PASS |

### When a previously satisfied gate becomes **invalid**

| Principle | ID | Statement |
|-----------|-----|-----------|
| Forward blocked immediately | **GF-07** | STALE/INVALID on blocking exit gate → eligibility fails |
| Downstream cascade | **GF-08** | GST-04: composite parents inherit child staleness |
| No silent carry-forward | **GF-09** | Progression ledger `gate_refs_passed` **historical**; re-forward needs fresh ACTIVE PASS |
| Rollback option | **GF-10** | Operator may RB-* instead of in-place re-eval — triggers GST-01 |
| Handoff supersession | **GF-11** | Invalidated gates beyond rollback target → related HO events SUPERSEDED (HV-03) |
| No auto-rollback | **GF-12** | Gate invalidation **does not** auto-change active state — operator declares rollback or rework |

### Failure without Gate Results System

Engine defines **semantics** of failure impact on composition and eligibility. **Does not** define: failure storage service, retry automation, webhook notifications, or CI integration.

---

## Gate Completeness

**Without introducing new project states.**

### Gate-complete (project)

Factory Project is **gate-complete** relative to declared scope endpoint iff:

| # | Criterion | ID |
|---|-----------|-----|
| 1 | Scope endpoint declared (default: full chain through `RG-PROJECT_COMPLETE`) | **GCO-01** |
| 2 | Every **required** `RG-*` on path to endpoint: satisfied (GS-*) | **GCO-02** |
| 3 | No required gate STALE or INVALID for endpoint eligibility | **GCO-03** |
| 4 | Parallel legal satisfied if scope requires | **GCO-04** |
| 5 | Composite parents satisfied including constituents | **GCO-05** |
| 6 | Terminal: `RG-PROJECT_COMPLETE` ACTIVE PASS aligns with active `COMPLETE` | **GCO-06** |

**Examples:**

| Situation | Gate-complete? |
|-----------|----------------|
| Active `COMPLETE`, all closure gates valid | **Yes** (full scope) |
| Active `SEO_READY`, all gates through entry to `SEO_READY` valid | **Yes** for reached prefix; **No** for full chain endpoint |
| Active `GENERATION_READY`, legal gate STALE after entity rework | **No** until reconciled |
| Partial charter ending at `DESIGN_READY` | **Yes** iff endpoint gates through `RG-DESIGN_APPROVED` valid — **partial closure convention OPEN** Stage 5 |

### Gate-incomplete (project)

**Gate-incomplete** iff any required gate on path to declared endpoint is: NOT_EVALUATED, insufficient, STALE, INVALID, or scope-applicability unresolved.

| Distinction | Gate-incomplete | State |
|-------------|-----------------|-------|
| Meaning | Authorization gap | Position in chain |
| At `BLOCK_READY` with validation FAIL | Incomplete (`RG-VALIDATION_PASS`) | Still `BLOCK_READY` |
| At `COMPLETE` | Should be gate-complete | Terminal |

**Gate completeness ≠ trackability.** Project may be fully trackable (Stage 3) yet gate-incomplete. **Gate completeness ≠ production readiness** — QA may pass while charter endpoint not reached.

### Relationship to state progression

| Concept | Gate-complete | State |
|---------|---------------|-------|
| Full factory closure | All `RG-*` through `RG-PROJECT_COMPLETE` | active = `COMPLETE` |
| Mid-chain | Prefix gates only | active = current S |
| After rollback | Gates above target STALE → incomplete until re-declared | active = rollback target |

---

## Explicit Non-Claims

This document and the Factory Gate Composition Model it defines:

- **are not** a Website Factory runtime, execution engine, or shipped product;
- **are not** an autonomous factory, agent system, MIG orchestration, or AI workflow;
- **are not** a queue, job scheduler, or work prioritization system;
- **are not** a workflow engine, BPMN executor, or n8n replacement;
- **are not** an orchestrator or automation layer;
- **are not** an application, dashboard, operator UI (RT-G12), or CLI;
- **are not** implementation — no code, validators, CI binding, or agents;
- **are not** a storage layer, database, file format, or **gate database**;
- **are not** FACTORY-GATE-RESULTS, FACTORY-PROJECT-MANIFEST, FACTORY-PROJECT-PASSPORT, FACTORY-STATE-STORE, FACTORY-HANDOFF-PACKAGE, FACTORY-ENGINE-LIFECYCLE, or FACTORY-ENGINE-SYSTEM documents;
- **do not** define JSON/YAML schemas, field lists, folder structures, tracking files, or persistence;
- **do not** modify Runtime Architecture, add `RG-*`, or redefine layer `GATE_*` / validation semantics;
- **do not** claim automated gate evaluation, Gate Results System, or project registry (RT-G05).

Human-operated declaration remains the v1 authorization model per Runtime Architecture.

---

## Open Questions For Stage 5

| ID | Question | Primary dependency |
|----|----------|-------------------|
| **OQ-S5-01** | Cascade **invalidation table** — artefact ref types → gate STALE/INVALID per RB-* target (OQ-S4-04) | Lifecycle binding + handoff model |
| **OQ-S5-02** | Partial scope **effective path** / jump table when states `EXCLUDED` (OQ-S4-05) | Lifecycle model |
| **OQ-S5-03** | `FACTORY_TRACK_SUSPENDED` vs gate active set when track frozen (OQ-S4-06) | Lifecycle model |
| **OQ-S5-04** | Partial closure without `COMPLETE` — gate endpoint vs state occupancy (OQ-S4-07) | Lifecycle + charter |
| **OQ-S5-05** | Multiple `generation_id` / PHASE_SLICE — gate index per slice vs project shell (OQ-S4-08) | Generation binding |
| **OQ-S5-06** | Handoff record minimum + gate–handoff binding at boundary (OQ-S4-09) | **Handoff binding Stage 5** |
| **OQ-S5-07** | RT-G05 registry entry vs gate outcome index boundary (OQ-S4-10) | Engine system boundary |
| **OQ-S5-08** | RT-G10 manifest — which gate composition elements may serialize (OQ-S4-11) | Manifest charter — not design here |
| **OQ-S5-09** | Extended types ER-01 — gate prerequisites before production path (OQ-S4-12) | Registry charter |
| **OQ-S5-10** | Chrome blocks without `block_id` (ERA-W01) — gate input refs vs implementation | Engine charter |
| **OQ-S5-11** | `PASS_WITH_WARNINGS` validation — operator decision gate composition | Validation + AP-* binding |

Stage 5 primary charter target: **Handoff Binding Model** — gate–handoff boundary records without Handoff Package system.

---

## Recommended Next Step

**Stage 5 — Factory Project Handoff Binding Model (Engine Architecture v1):** formalize how `HO-*` events bind to gate clearance at layer boundaries, minimum handoff event semantics, and rollback supersession — **without** defining FACTORY-HANDOFF-PACKAGE, storage, or renaming Runtime handoff contracts.

Subsequent Engine stages: lifecycle binding (partial paths, invalidation tables) → engine system boundary (RT-G09 documentation closure).

Optional P3 hygiene (non-blocking): sync stale RUNTIME-ROADMAP acceptance checkbox per ERA-W05.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Physical format of gate outcome records | **NOT DEFINED** — RT-G10 FUTURE; explicitly not Gate Results system |
| Automated gate evaluator | **FUTURE** — RT-G01, RT-G03, RT-G11 |
| Partial closure canonical gate endpoint | **OPEN** — OQ-S5-04 |
| Calendar for Engine Stages 5–6 | **not scheduled** |
| Triumph production deploy vs gate closure | **UNKNOWN** — external |

---

*Factory Gate Composition Model v1 — Stage 4 complete. Architecture only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Gate Composition Model v1

**Stage:** Factory Engine Architecture v1 — Stage 4 (Gate Composition Model)  
**Deliverable:** `FACTORY-GATE-COMPOSITION-MODEL-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-GATE-COMPOSITION-MODEL-v1.md` (created)  
**Summary:** Определена Gate Composition Model: назначение gates и авторизация движения; Runtime binding без владения RG-*; ownership split (Runtime / layers / Project / Tracking); composition principles, namespace mapping RG ↔ GATE_* ↔ validation; sufficiency (satisfied / insufficient / stale / invalid); dependency model; связи со state и tracking; failure principles; gate-complete vs gate-incomplete без новых states; закрыты OQ-S4-01…OQ-S4-03 из Stage 3 — без Gate Results system, storage, schemas, implementation.  
**Git:** no commit, no push (per task charter).
