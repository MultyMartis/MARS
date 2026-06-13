# REPORT — Factory Project Object Model v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Factory Engine Architecture v1 — **Stage 1 only**  
**Контекст:** Website Factory Foundation Era **COMPLETE**; Engine Readiness Audit v1 — **PASS WITH WARNINGS**  
**Тип:** architecture only — **без** implementation, runtime, agents, code, workflows, databases, automation  
**Связь:** [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md), [runtime-architecture/PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md), [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md)

---

## Purpose

Stage 1 определяет **канонический объект**, который проходит через Website Factory: что такое Factory Project, из чего он состоит, где истина, что принадлежит проекту, а что — принятым Foundation-слоям.

Цель — дать оператору **единую логическую модель**, по которой можно ответить на вопросы «что это за проект», «где он сейчас», «что завершено», «что ждёт», «какие gates пройдены», «какие handoffs существуют» и «где source of truth» — **без** чтения всего workspace и **без** проектирования файлов, схем или хранилищ.

Документ **не** заменяет Runtime Architecture v1 и **не** изменяет frozen/accepted layer contracts.

---

## Design Constraints

| Constraint | Source |
|------------|--------|
| Foundation redesign **не авторизован** | Engine Readiness Audit v1; Foundation Freeze |
| Runtime state names (14 states) **не переопределяются** без supersession charter | ERA-W07; [PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) |
| Layer gate semantics (`GATE_*`, validation PASS/FAIL) **не переопределяются** Engine | [RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) |
| Frozen Legal Pack, Registry, 29 `block_id`, Core 5 blueprints — **reference only** | Engine Protected Documents (ERA audit) |
| Human-operated gates; **нет** automated state mutation в v1 | [RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) §7 |
| Partial / design-only scope **допустим** через charter — default = full chain | [PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md) LR-07 |
| **Запрещено** в этом Stage: schemas, YAML/JSON, file layouts, folder structures, manifest/passport/state-store specs | Task charter Stage 1 |

**Authority precedence при конфликте:** Foundation Freeze + Finalization Pass + Engine Readiness Audit → затем [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) для operational status.

---

## Foundation Dependencies

Factory Project **существует только** как применение принятой Foundation-цепочки к конкретному производственному случаю.

```text
Intake / Identity
    ↓
Site Type Registry          → classification
    ↓
Blueprints                  → site-level IA
    ↓
Page Architecture           → per-route contracts
    ↓
Block Registry              → canonical block stacks
    ↓
Page Block Validation       → architecture PASS/FAIL
    ↓
SEO Architecture v2
    ↓
Design System Mapping v1
    ↓
Content Contracts v1
    ↓
Content Validation v1
    ↓
Generation Contracts v1     → production package + generation slice
    ↓
Production QA v1            → Frontend readiness gate
    ↓
Runtime Architecture v1     → movement discipline (states, RG-*, HO-*)
    ↓
Frontend Layer              → implementation (outside Factory architecture closure)
```

**Parallel (conditional):** Legal Pack v1 (FROZEN) + Legal Entity Discovery v1 — обязательны для `FULL_SITE` / PII / commercial disclosure до exit Phase 10 ([PROJECT-LIFECYCLE-v1.md](runtime-architecture/PROJECT-LIFECYCLE-v1.md)).

Factory Project **зависит от** всех перечисленных accepted layers как от **внешней архитектурной истины**. Factory Project **не владеет** их контрактами.

---

## Canonical Definition Of Factory Project

**Factory Project** — логическая единица отслеживания, представляющая **один** Website Factory production case: от фиксации intake до terminal state `COMPLETE`.

Factory Project — это **не**:

- git-репозиторий, workspace folder или HTML/CSS/JS deliverable;
- экземпляр MIG, n8n workflow или agent session;
- запись в БД, очередь или registry (RT-G04–G06 — **FUTURE**);
- копия Foundation-документов;
- Frontend implementation workstream (хотя handoff к нему — часть lifecycle).

Factory Project **есть**:

- **контекст применения** frozen/accepted layer contracts к одному scope;
- **индекс** текущего положения в canonical 14-state model;
- **сборник ссылок** на layer artefacts, gate outcomes и handoff records **для этого scope**;
- **scope boundary** — что включено / исключено из Factory track (charter-driven).

**Минимальная идентичность** (логические измерения, выведенные из Foundation — не schema):

| Измерение | Когда возникает | Роль | Foundation source |
|-----------|-----------------|------|-------------------|
| **Stable project identity** | Intake (`NEW_PROJECT`) | Уникальная ссылка на production case в Factory scope | [PROJECT-STATE-MODEL-v1.md](runtime-architecture/PROJECT-STATE-MODEL-v1.md) — logical `project_id`; [RUNTIME-HANDOFFS-v1.md](runtime-architecture/RUNTIME-HANDOFFS-v1.md) HO-01 |
| **Project charter** | Intake | Цели, exclusions, operator assignment, stakeholder context | HO-01; Registry implementation rules (intake close) |
| **Scope tier** | Intake | `FULL_SITE` vs partial / design-only / phase slice | PROJECT-STATE-MODEL `NEW_PROJECT` outputs; [GENERATION-CONTRACT-v1.md](generation-contracts/GENERATION-CONTRACT-v1.md) `generation_scope.scope_type` |
| **Site classification** | После `CLASSIFIED` | Canonical `site_type_code`, Core vs Extended, production tier | [SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md); RG-CLASSIFICATION_COMPLETE |
| **Blueprint binding** | После `BLUEPRINT_READY` | Frozen site-level IA reference for this project | [BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md); RG-BLUEPRINT_APPROVED |
| **Generation slice identity** | При входе в Generation scope | Logical `generation_id` для production package boundary | GENERATION-CONTRACT — immutable after Generation Ready |
| **Current Factory state** | Continuous | Одно из 14 canonical states | PROJECT-STATE-MODEL |
| **Foundation version pins** | Implicit at start | Какие ACCEPTED/FROZEN layer versions apply | NEXT-PRIORITIES; GENERATION-CONTRACT `required_dependencies.acceptance_state` |

**Не входят в минимальную идентичность как обязательные на intake:** client commercial name (может жить в charter), deploy target, hosting, Triumph-style workspace path — unless charter declares them. Legal entity facts — **lifecycle-dependent** (Legal Entity Card), not intake minimum.

**Ответ оператору «What is this project?»** = charter + scope tier + `site_type_code` (when classified) + current state + active generation slice (when applicable) + declared exclusions.

---

## Mandatory Project Components

**Mandatory components** — части логического объекта Factory Project, которые **всегда** присутствуют в модели, как только проект признан Factory-scoped (даже если некоторые — пустые индексы на ранней стадии).

| Component | Always present | Owned by | Purpose |
|-----------|----------------|----------|---------|
| **Identity shell** | Yes | Engine / project tracking (future) | Stable reference to this production case |
| **Charter & scope declaration** | Yes | Project (operator-authored) | Bounds Factory work; drives partial paths |
| **Current canonical state pointer** | Yes | Runtime vocabulary; **instance value** — project tracking | «Where is it now?» |
| **State history index** | Yes (may be empty → grows) | Project tracking | Audit of declared transitions |
| **Gate outcome index** | Yes (grows with lifecycle) | Project tracking **records**; gate **semantics** — defining layer | «What gates passed?» |
| **Handoff record index** | Yes (grows with lifecycle) | Project tracking | «What handoffs exist?» |
| **Layer artefact reference index** | Yes (grows with lifecycle) | **Artefacts** — layers; **refs** — project | Pointers to applied contracts, not copies of Foundation |
| **Scope freeze marker** | Yes from Generation Ready onward | Generation slice within project | Prevents silent scope drift |
| **Parallel legal track status** | Yes when scope requires legal | Legal Pack workflow | RG-LEGAL_COMPLETE / RG-ENTITY_VERIFIED status refs |

**Mandatory Foundation layers (full default track)** — project **must bind** each before corresponding state; layers themselves are **not components inside** the project object:

Registry → Blueprint → Page Architecture → Block Registry → Page Block Validation → SEO → Design → Content → Content Validation → Generation → Production QA → (Frontend handoff boundary).

Legal Pack + Entity Discovery — **mandatory parallel components** for scopes requiring legal production ([RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) parallel track).

---

## Lifecycle-Dependent Components

Компоненты, которые **появляются или обогащаются** по мере прохождения lifecycle — не существуют как полноценные bindings на intake.

| Lifecycle phase | State boundary | Components that appear / activate |
|-----------------|----------------|-----------------------------------|
| LC-00 Intake | `NEW_PROJECT` | Intake record; scope tier; operator assignment |
| LC-01 Classification | `CLASSIFIED` | `site_type_code`, Core/Extended flag, Registry matrix refs |
| LC-02 Blueprint | `BLUEPRINT_READY` | `blueprint_ref`, site-level block intent |
| LC-03 Page Architecture | `PAGE_READY` | Per-route `page_type`, PAGE-CONTRACT refs |
| LC-04 Blocks | `BLOCK_READY` | Resolved `block_id` stacks, mapping audit |
| LC-05 Validation | `VALIDATED` | Page Block Validation run record (PASS) |
| LC-06 SEO | `SEO_READY` | SEO strategy ref, PAGE-SEO-CONTRACT set |
| LC-07 Design | `DESIGN_READY` | `VF_*` bindings per required block/page |
| LC-08 Content | `CONTENT_READY` | Content signal bindings |
| LC-09 Content Validation | `CONTENT_VALIDATED` | Content validation PASS record |
| LC-10 Generation | `GENERATION_READY` | `generation_id`, GENERATION-CONTRACT READY marker, Legal Complete (+ Entity when required) |
| LC-11 Production QA | `PRODUCTION_QA_READY` | Production QA run, checklist completion |
| LC-12 Frontend Handoff | `FRONTEND_READY` | FRONTEND_HANDOFF_PACKAGE ref, Frontend ack |
| LC-13 Closure | `COMPLETE` | Closure record; no further Factory advances |

**Parallel legal (lifecycle-dependent):**

| Component | Appears when | Blocks |
|-----------|--------------|--------|
| Legal route mapping | Before Generation exit | `RG-LEGAL_COMPLETE` |
| Legal Entity Card | When commercial disclosure / PII requires entity | `RG-ENTITY_VERIFIED` |
| Legal Input Sheet | Before legal generation | Legal placeholder gate |

**Post-Factory (outside project closure, not Factory Project components):**

- Frontend HTML/partials/SCSS/JS implementation;
- Deploy authorization, hosting, CI for client site;
- Triumph-style workspace build outputs.

---

## Authority Structure

Source of truth — **распределённая**, не монолитная. Factory Project — **агрегирующая проекция**, не единый authoritative document.

### Authority tiers

| Tier | Role | Authoritative for | Not authoritative for |
|------|------|-------------------|----------------------|
| **T1 — Layer contracts** | Foundation accepted/frozen docs | *What* must be true (semantics, matrices, PASS/FAIL rules, templates) | Per-project state, gate sign-offs, handoff ack |
| **T2 — Runtime movement** | Runtime Architecture v1 | Canonical **state names**, transition rules, `RG-*` gate definitions, `HO-*` handoff contracts | Layer validation logic, legal template text, block registry contents |
| **T3 — Layer gate namespaces** | Each `*-GATES-v1.md`, VALIDATION-CONTRACT, etc. | Domain-specific gate IDs and pass/fail criteria | Project-wide state pointer |
| **T4 — Project tracking (Engine)** | Future Engine docs (Stage 2+) | **This project's** current state, gate outcome records, handoff records, artefact refs, scope freeze | Redefining layer or runtime semantics |
| **T5 — Operational status register** | [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) | Which Foundation layers are ACCEPTED/FROZEN globally | Individual project progress |

### Resolution rules

1. **«What must a LANDING blueprint contain?»** → Blueprint layer (T1), not Project.
2. **«May this project advance to SEO_READY?»** → Runtime transitions (T2) + Validation PASS record (T3/T4).
3. **«What is this project's current state?»** → Project tracking (T4) using Runtime state vocabulary (T2).
4. **«Is SEO Architecture Layer v2 accepted?»** → NEXT-PRIORITIES (T5), not Project.
5. **Conflict between FREEZE header date and post-freeze ACCEPTED** → NEXT-PRIORITIES wins (Finalization Pass).

### What the Project object is **not** as authority

- Not a replacement for Legal Pack FROZEN templates.
- Not a canonical registry of `block_id` or `site_type_code` definitions.
- Not the definition of `RG-*` or `GATE_*` pass criteria — only the **instance record** that a gate was evaluated and signed off.

**Operator-facing «single view»** (future Stage 2+ tracking model) composes T4 from T1–T3 references — without merging authority into one file.

---

## State Ownership

| Concern | Owner | Project object role |
|---------|-------|---------------------|
| **Canonical state vocabulary** (14 state codes, terminal `COMPLETE`) | Runtime Architecture v1 | **References** vocabulary; does not define new states |
| **Transition rules** (forward, forbidden, rollback) | [STATE-TRANSITION-RULES-v1.md](runtime-architecture/STATE-TRANSITION-RULES-v1.md) | Project **declares** transitions occurred; rules stay in Runtime |
| **Current state instance** | Project tracking (Engine) | **Owns** «this project is now `SEO_READY`» |
| **State history / rollback declarations** | Project tracking | **Owns** operator records of rollback with charter where required |
| **Layer-produced artefacts** (PAGE-CONTRACT, validation run, SEO profile, specs) | Respective Foundation layer workstreams | Project **indexes refs**; layer owns content truth |
| **Foundation frozen docs** | Legal, Registry, Block Registry, etc. | **Never** hold per-project state |
| **Generation package / spec assembly** | Generation Contracts layer | Project holds `generation_id` + refs; spec semantics — GENERATION-OUTPUTS |
| **Frontend implementation state** | Frontend workstream (client workspace) | **Outside** Factory state model until handoff ack; then ack ref in project |
| **Automated persistence** | **NOT STARTED** (RT-G04) | No storage owner exists in v1 |

**Layers that must never own project state:** all T1 Foundation contract documents (they are class-level, not instance-level). Runtime **defines movement discipline** but explicitly excludes DB/file-backed state (RT-G04) — instance ownership is chartered to Engine tracking, not to Runtime docs themselves.

---

## Gate Ownership

Three complementary gate namespaces (ERA-W02) — Project **composes records**, not definitions:

| Namespace | Definer | Project holds |
|-----------|---------|---------------|
| **`RG-*`** | [RUNTIME-GATES-v1.md](runtime-architecture/RUNTIME-GATES-v1.md) | Outcome record: PASS/FAIL/blocked + operator sign-off + timestamp (logical) |
| **Layer `GATE_*`** | e.g. [GENERATION-GATES-v1.md](generation-contracts/GENERATION-GATES-v1.md), [PRODUCTION-QA-GATES-v1.md](production-qa/PRODUCTION-QA-GATES-v1.md) | Outcome records mapped to runtime advance |
| **Validation gates** | Page Block Validation, Content Validation contracts | PASS/FAIL run records referenced before state advance |

### Ownership split

| Belongs to **Gate system** (definitions) | Belongs to **Project** (instance) |
|------------------------------------------|-----------------------------------|
| Gate ID, purpose, inputs, pass/fail criteria | That **this** project passed `RG-VALIDATION_PASS` on date X |
| Dependency graph between gates | Index of open vs closed gates for current state |
| Layer-specific failure libraries | Pointers to failure remediation status (not failure definitions) |
| HITL approval **requirements** | Approval **records** (AP-01…AP-09) |

**Recording gate outcomes:** operator / project tracking workstream — human-declared in v1. No CI, webhook, or agent recorder (RT-G01, RT-G03, RT-G11 — FUTURE).

**Legal gates:** `RG-LEGAL_COMPLETE`, `RG-ENTITY_VERIFIED` — definitions in Runtime; Legal Pack owns legal pass semantics; Project holds parallel track status refs.

**Generation Ready composite gate:** `RG-GENERATION_READY` requires upstream `RG-*` PASS + layer GENERATION gates — Project must reflect **composite** readiness without redefining layer gates.

---

## Handoff Ownership

| Concern | Owner | Classification |
|---------|-------|----------------|
| **Handoff contract definitions** (`HO-01`…`HO-13`, `HO-L1`, `HO-L2`) | [RUNTIME-HANDOFFS-v1.md](runtime-architecture/RUNTIME-HANDOFFS-v1.md) | Gate system / Runtime — not Project |
| **Required artefacts list per handoff** | Runtime + upstream layer docs | Project verifies presence via checklist |
| **Producer layer artefacts** | Respective Foundation layer | **Not** duplicated inside Project — referenced |
| **Handoff event record** (producer → consumer declared) | Project tracking | **Project data** — who handed off, when, which HO-ID |
| **FRONTEND_HANDOFF_PACKAGE** | Generation Outputs ([GENERATION-OUTPUTS-v1.md](generation-contracts/GENERATION-OUTPUTS-v1.md)) | **Handoff package data** — spec bundle for Frontend; indexed by project + `generation_id` |
| **Frontend acknowledgement** | Frontend workstream + operator | **Project data** — ack record required for `FRONTEND_READY` → `COMPLETE` |
| **Blocked conditions evaluation** | Operator checklist per HO-* | Project records blocked / cleared status |

### Project data vs handoff package data

| **Project data** | **Handoff package data** |
|------------------|--------------------------|
| Handoff ID, state boundary crossed, gate PASS at boundary | PAGE_BUILD_SPEC, BLOCK_STACK_SPEC, SEO_SPEC, DESIGN_SPEC, CONTENT_SPEC contents |
| Operator sign-off on handoff complete | FRONTEND_HANDOFF_PACKAGE assembly per GENERATION-OUTPUTS |
| Index linking package to `generation_id` | Production QA checklist artefacts consumed by Frontend |
| Frontend ack timestamp / operator approval | Implementation code (explicitly out of GENERATION-OUTPUTS scope) |

**Critical boundary:** Production QA → Frontend handoff (`HO-12`) — package completeness is **handoff package data**; declaration that handoff occurred is **project data**. Frontend before Production QA PASS — **forbidden** (FT-07, HO-12 blocked conditions).

---

## Relationship Map

```text
                    ┌─────────────────────────────────────┐
                    │         FACTORY PROJECT             │
                    │  (identity, state, indexes, scope)  │
                    └─────────────────────────────────────┘
           references │                    │ records
                     ▼                    ▼
    ┌──────────────────────┐    ┌──────────────────────┐
    │  FOUNDATION LAYERS   │    │  RUNTIME DISCIPLINE   │
    │  (T1 authority)      │    │  (T2 movement)        │
    └──────────────────────┘    └──────────────────────┘
```

| Related domain | Relationship to Factory Project |
|----------------|--------------------------------|
| **Legal** | Parallel track; project refs legal route mapping, Input Sheet, placeholder gate status; **does not own** Legal Pack templates |
| **Legal Entity** | Conditional component; Entity Card ref + VERIFIED status; discovery artefacts stay in legal-entity workflow |
| **Blueprint** | Project binds one frozen `blueprint_ref` per scope; Blueprint System owns IA semantics |
| **Pages** | Project holds per-route PAGE-CONTRACT refs; Page Architecture owns `page_type` contracts |
| **Blocks** | Project holds resolved stacks; Block Registry owns canonical `block_id` |
| **SEO** | Project refs strategy + PAGE-SEO-CONTRACT set; SEO layer owns architecture slots |
| **Design** | Project refs `VF_*` bindings; Design System Mapping owns pattern families |
| **Content** | Project refs signal bindings; Content Contracts own signal architecture |
| **Generation** | Project owns `generation_id` + scope freeze; Generation Contract owns package assembly rules |
| **QA** | Project refs Production QA PASS + checklist; Production QA owns gate categories |
| **Runtime Architecture** | Project **uses** state model, RG-*, HO-*; Runtime **does not store** project instances |
| **Handoff** | Project indexes HO events + package refs; Runtime defines HO contracts |
| **Frontend** | Consumer of handoff package; ack returns to project; implementation **outside** Factory closure |
| **Registry** | Project receives classification outputs; Registry owns type definitions |
| **Validation layers** | Project refs PASS runs; validation layers own FAIL/CRITICAL semantics |

**Dependency direction:** Foundation layers → produce artefacts → Project indexes → Runtime gates authorize state advance → next layer consumes via handoff.

**Project never mutates upstream layer authority** — rollback **invalidates downstream project refs** (operator-declared), not Foundation documents.

---

## Explicit Non-Claims

This document and the Factory Project object model it defines:

- **are not** a Website Factory runtime, execution engine, or shipped product;
- **are not** an autonomous factory or unattended production pipeline;
- **are not** an agent system, MIG orchestration, or AI workflow;
- **are not** a queue, job scheduler, or work prioritization system;
- **are not** a workflow engine, BPMN executor, or n8n replacement;
- **are not** an application, dashboard, operator UI (RT-G12), or database (RT-G04);
- **are not** implementation — no code, validators CLI, CI binding, or automation;
- **do not** define JSON/YAML schemas, manifest file paths, folder layouts, or storage format;
- **do not** authorize Foundation redesign, Legal Pack expansion, or new `block_id`;
- **do not** claim existence of project registry (RT-G05) or manifest standard (RT-G10).

Human-operated declaration remains the v1 execution model per Runtime Architecture.

---

## Open Questions For Stage 2

Stage 2+ Engine documents must resolve (without answering here):

| ID | Question | Primary dependency |
|----|----------|-------------------|
| **OQ-01** | How does project tracking **bind** canonical state to operator-visible records without redefining Runtime states? | State model Stage |
| **OQ-02** | What is the minimal **tracking surface** (logical, not file format) for «single view»? | Project tracking model |
| **OQ-03** | **Gate namespace mapping table** — `RG-*` ↔ layer `GATE_*` ↔ validation gates (ERA-W02) | Gate model Stage |
| **OQ-04** | How are **composite gates** (Generation Ready, Production QA Pass) represented in project index? | Gate model |
| **OQ-05** | Rollback **cascade invalidation** — which project refs invalidate on declared rollback? | Lifecycle model |
| **OQ-06** | Relationship between **project** and **`generation_id`** when multiple slices or PHASE_SLICE scopes exist | Lifecycle + Generation binding |
| **OQ-07** | Partial scope charter — which mandatory components **drop out** vs stay indexed as N/A | Lifecycle model |
| **OQ-08** | Handoff record **minimum content** (format deferred) — blocked on RT-G10? | Handoff model |
| **OQ-09** | Extended site types (`SAAS`, `WEB_APPLICATION`, `MARKETPLACE`) — project prerequisites before production path | Registry charter |
| **OQ-10** | Chrome blocks without `block_id` (HEADER_NAV, FILTERS, SEARCH — ERA-W01) — project binding vs implementation note | Block GAPS + Engine charter |
| **OQ-11** | External pointer discipline (`projects/mars-website-factory/` v0 — ERA-W03) vs canonical project refs | Tracking model |
| **OQ-12** | Relationship to future RT-G05 Project registry — logical project vs registry entry | Engine system boundary |

---

## Recommended Next Step

**Stage 2 — Factory Project State Model (Engine Architecture v1):** formalize how the Factory Project object **binds** to Runtime's 14 canonical states and transition rules — instance semantics, rollback ref invalidation, and partial-scope state paths — **without** defining storage, schemas, or renaming states.

Subsequent Engine stages (per RT-G09 / Engine Readiness Audit): lifecycle binding → gate composition model → handoff binding → project tracking model.

Optional P3 hygiene (non-blocking): sync stale RUNTIME-ROADMAP acceptance checkbox per ERA-W05.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Physical location of per-project tracking artefacts | **NOT DEFINED** — RT-G10 FUTURE |
| Calendar for Engine Stages 2–6 | **not scheduled** |
| Triumph production deploy authorization | **UNKNOWN** — external to Factory Project closure |
| Whether Extended Type Blueprints precede full Engine tracking model | **requires charter** if scope changes |

---

*Factory Project Object Model v1 — Stage 1 complete. Architecture only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Project Object Model v1

**Stage:** Factory Engine Architecture v1 — Stage 1 (Project Object Model)  
**Deliverable:** `FACTORY-PROJECT-OBJECT-MODEL-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-OBJECT-MODEL-v1.md` (created)  
**Summary:** Определён канонический Factory Project как логическая единица отслеживания с распределённой authority structure; выведены минимальная идентичность, mandatory vs lifecycle-dependent components, ownership для state/gates/handoffs, relationship map к Foundation layers; explicit non-claims зафиксированы; Stage 2 open questions перечислены.  
**Git:** no commit, no push (per task charter).
