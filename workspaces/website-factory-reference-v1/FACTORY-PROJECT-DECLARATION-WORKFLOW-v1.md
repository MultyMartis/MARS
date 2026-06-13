# REPORT — Factory Project Declaration Workflow v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Operational Design — **Operational Playbook 04** (Project Declaration Workflow)  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 **COMPLETE**; Post-Engine Doctrine **COMPLETE**; [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) **COMPLETE**; Playbooks 01–03 **COMPLETE**  
**Тип:** operational workflow only — **без** runtime, automation, implementation, storage, schemas, agents, UI  
**Не переопределяет:** Engine Stages 1–6, Runtime Architecture, Manifest/Registry/Tracking Surface charters, Playbooks 01–03  

---

## Purpose

### Зачем существует Project Declaration Workflow

**Project Declaration Workflow** — четвёртый операционный playbook Website Factory. Он описывает **человеко-исполняемую** дисциплину, по которой **операционная реальность** production case становится **декларированной реальностью** Factory — то есть последней **operator-declared** истиной в Engine indexes (state, gates, handoffs, lifecycle metadata, audit trail), которую Tracking и Surface **отображают** как authoritative.

Workflow закрывает координационную проблему **разрыва между работой и истиной**:

| Проблема | Как workflow решает |
|----------|---------------------|
| Layer work, git, CI или внешние системы создают впечатление прогресса без Factory authorization | Нормативные **классы declaration** и **prerequisites** — что можно объявить и когда |
| Playbook 03 фиксирует «что видно», но не ритуал **записи** решений в Engine | Declaration workflow — **исполнение** human-only decisions (classes E–H, reconciliation) **после** assessment |
| Gate PASS, state move, handoff clearance смешиваются с evidence review | Разделение: **evidence classes** поддерживают declaration; declaration **не** заменяет criteria review в layer docs |
| Stale PASS, ledger mismatch, charter drift остаются неявными | **Reconciliation** и **invalid declaration** principles — когда declared truth недействительна |
| Partial closure, suspension, scope change без единой дисциплины | **Closure and amendment** declaration classes привязаны к lifecycle composition без новых Runtime states |

Оператор после применения workflow должен уметь ответить **без чтения всего workspace**:

- Кто может объявлять?
- Что может быть объявлено?
- Когда declaration разрешена?
- Когда declaration запрещена?
- Какие **классы** evidence поддерживают declaration?
- Что происходит после declaration?

### Что declarations **решают** и **не решают**

| Declarations **решают** | Declarations **не решают** |
|-------------------------|----------------------------|
| Какой **active state** занимает Factory Project сейчас | Автоматическое исполнение TR/FT/DR — нет enforcement engine |
| Какие **gate outcomes** авторизуют движение для **этого** case | Определение pass/fail criteria — остаётся Runtime + layers |
| Какие **handoff events** зафиксированы как cleared | Сборку или доставку handoff package bodies |
| Какие **lifecycle interpretations** (endpoint, partial closure, suspension) видны оператору | Frontend deploy, hosting, client go-live |
| **Reconciliation** при конфликте indexes vs assessed reality | Производство layer artefact bodies |
| **Append-only** audit honesty для Factory track | Catalog enrollment (Playbook 02) или manifest enrollment (Playbook 01) |

**Граница playbook:** от **решения объявить** (после типичной Surface session или эквивалентной assessment) до **фиксации declaration outcome** в логической модели Engine — **без** определения формата записи, хранилища или автоматизации.

```text
  PLAYBOOKS 01–02 (entry)     PLAYBOOK 03 (supervision)     THIS WORKFLOW (04)
  manifest / catalog                 │                              │
        │                            ▼                              ▼
        └──────────▶  Reality assessed ──▶  Declaration decision ──▶  Declared truth
              (indexes read)              (human acts)              (indexes updated logically)
                                                    │
                                                    ▼
                                         Tracking composition + Surface freshness
```

---

## Foundation Dependencies

Workflow **наследует** принятые артефакты **без их изменения**. При конфликте — побеждает более специфичный model (State, Gate, Lifecycle, Tracking), затем Operational Model.

### Tier 0 — Operational model and Playbooks 01–03

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | Decision classes C–H; OA-ACT-01 human-only declarations; movement «declared, not executed»; completion model; reconciliation (MS-02 analog) |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Предусловие manifest-enrolled Factory Project; enrollment declarations **вне** scope Playbook 04 |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Catalog enrollment/withdrawal — **отдельный** declaration plane (decision I) |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Типичный **предшественник**: progression / reconciliation / defer outcomes → declaration acts |

### Tier 1 — Engine composition (обязательные)

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Identity shell; gate/handoff indexes; EO-03 declaration truth |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Forward/rollback progression; CS-*, SG-*, SH-*; terminal `COMPLETE` |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | GS-* sufficiency; GST-*/GIN-* stale/invalid; GF-* failure impact |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | LCP-*, LRC-* cascade; partial closure; `FACTORY_TRACK_*` metadata |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | AT-* audit; TV-02 freshness; TC-* trackability after declaration |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | EO-01…EO-07; HB-* handoff binding; human-operated boundary |

### Tier 2 — Post-Engine doctrine (reference)

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | VP-03 authoritative = last declared; post-declaration Surface must reflect indexes |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | MT-01 — Manifest **не** gate index; amendments via charter refs |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | RA-05 — catalog **не** substitutes Engine declarations |

**Authority precedence:** Runtime + Foundation (criteria) → Engine Stages 1–6 (composition semantics) → Operational Model → Playbooks 01–03 → **этот playbook** для **ритуала declaration** → implementation charters **не могут** ослабить OA-ACT-01, AT-01, EO-03.

---

## Declaration Authority Principles

### Кто может объявлять (v1)

| Actor | May declare (v1) | May not declare |
|-------|------------------|-----------------|
| **Factory operator** | Все **обязательные** Factory declarations по этому playbook | — |
| **Reviewer / validator** | Подтверждение соответствия layer criteria **как input** к operator declaration — **не** substitute for operator gate/state/handoff declaration | Active state, `RG-*` PASS, HO clearance, rollback, reconciliation, closure |
| **Charter author / sponsor** | Charter content **через** operator-mediated amendment declaration | Direct Engine index mutation |
| **Client / stakeholder** | Approvals **как** charter-bound refs — не canonical state | Gate PASS, state occupancy |
| **External systems** (CI, MIG, agents) | **Никогда** — may trigger operator to **open** Playbook 03, not declare | Any Engine authoritative outcome |

### Authority principles (normative)

| ID | Principle |
|----|-----------|
| **DA-01** | **Factory operator** — единственный носитель **обязательных** declarations state / gate / handoff / rollback / reconciliation / Factory-track closure metadata (OA-ACT-01) |
| **DA-02** | Reviewer attestation **без** operator declaration = **evidence class**, не gate outcome index |
| **DA-03** | Sponsor charter change **требует** operator **scope/amendment declaration** — не silent mask update |
| **DA-04** | Catalog enrollment/withdrawal — operator declaration per Playbook 02 — **не** смешивается с Engine progression declarations |
| **DA-05** | Один declaration act = **один** logical Factory Project identity — не portfolio batch |
| **DA-06** | Declaration **не** делегируется automation в v1 — future tooling may **assist**, ownership остаётся human (Operational Model) |

### Decisions that can **never** be automatic (v1)

- Active state change (forward, rollback, re-entry forward)  
- `RG-*` / layer-mapped `GATE_*` outcome PASS/FAIL/BLOCKED for project instance  
- Handoff clearance (`HO-*`) and Frontend ack records  
- Rollback (`RB-*`) and cascade acknowledgment  
- Reconciliation correcting ledger vs active or stale hygiene  
- Charter/scope amendment affecting LR-07 mask or declared endpoint  
- `FACTORY_TRACK_CLOSED_PARTIAL`, `FACTORY_TRACK_SUSPENDED`, suspension lift  
- Registry discoverability (Playbook 02)  

**Optional automation (FUTURE)** не меняет DA-01 — только implementation charters.

---

## Declaration Classes

Классы — **категории операционных актов**, не шаблоны, не формы, не registry записей.

### Core classes (required analysis)

| Class | Operational meaning | Typical Engine planes affected |
|-------|----------------------|--------------------------------|
| **State progression** | Operator declares forward transition `from_code` → `to_code` per TR-* when eligibility satisfied | State: active + history + progression ledger; Lifecycle: segment advance |
| **Rollback** | Operator declares `RB-*` backward move + acknowledges cascade | State; Gate STALE/INVALID; Handoff SUPERSEDED; Artefact ref INVALIDATED |
| **Gate satisfaction** | Operator declares `RG-*` (and mapped constituents) **PASS** + validity ACTIVE | Gate outcome index; may unlock eligibility |
| **Gate invalidation** | Operator declares FAIL, void, or correction superseding prior PASS | Gate index validity; may block forward without state change |
| **Handoff acknowledgement** | Operator declares `HO-*` **CLEARED** (and ack when required) | Handoff event index; progression `handoff_ref` alignment |
| **Lifecycle interpretation** | Operator declares how charter endpoint, segment, or track status **reads** for observers — без новых Runtime codes | Lifecycle metadata; Tracking Tier A/B flags |
| **Scope amendment** | Operator declares charter change affecting exclusions, endpoint, tier | Scope mask; may trigger GST-03 / RB-10 path |
| **Reconciliation** | Operator declares correction when assessed reality ≠ indexes | Audit trail; may restate active/gate/handoff without movement |
| **Closure decision** | Operator declares Factory-track terminal or partial terminal per charter | State → `COMPLETE` or partial endpoint; `FACTORY_TRACK_CLOSED_PARTIAL`; gate closure |

### Additional justified classes

| Class | When justified | Notes |
|-------|----------------|-------|
| **Re-entry authorization** | After rollback, operator declares readiness to re-forward through segment | Combines fresh gate PASS + forward progression — may be **one** or **sequenced** declarations |
| **Intra-segment gate re-declaration** | Active unchanged; validation re-run → new PASS record (R-02) | **Not** state progression — gate class only |
| **Suspension / lift** | Charter pauses or resumes Factory work without Runtime terminal | `FACTORY_TRACK_SUSPENDED` metadata — LCMP + Playbook 03 suspension |
| **Enrollment attestation** (cross-reference) | Manifest/Registry enrollment outcomes | Owned by Playbooks 01–02 — **cite**, do not redefine here |

### Class interaction rules

| Rule | ID | Statement |
|------|-----|-----------|
| Gate before move at boundary | **DC-01** | State progression across segment boundary **requires** exit gate satisfaction declaration **unless** rollback target already satisfied fresh PASS |
| Handoff coupling | **DC-02** | Gate satisfaction at boundary **не** substitutes handoff acknowledgement (GC-05, HB-02) |
| Rollback supersedes downstream | **DC-03** | Rollback declaration **implies** cascade markers — operator **acknowledges**, не выбирает partial cascade |
| Closure is composite | **DC-04** | Closure decision **requires** terminal state declaration + closure gates + HO-13 path when full chain |
| Amendment may forbid silent forward | **DC-05** | Scope amendment may **require** defer progression until mask reconciled (Playbook 03 outcome) |

**Запрещено в этом разделе:** templates, field lists, declaration IDs as schema, storage keys.

---

## Declaration Prerequisites

Принципы **до** того, как declaration разрешена. **Не** file paths, **не** storage.

### Universal prerequisites

| # | Prerequisite | Rationale |
|---|--------------|-----------|
| P0 | **Factory-scoped** logical Factory Project exists | Playbook 01 recognition |
| P1 | **Manifest-enrolled** (MRDY-*) for normative track | Orientability; entry anchor known |
| P2 | **Operator authority** per DA-01 | Authority violation → invalid declaration |
| P3 | **Declaration class** identified — не смешивать gate PASS с state move в одном неявном акте | Audit honesty (AT-01) |
| P4 | **Assessed reality** — Playbook 03 или эквивалент: blockers understood | SO-02 progression outcome |
| P5 | **Tracking engagement** — operator consumed composition, not Manifest/Registry alone | MT-01, RE-01, SE-01 |

### Class-specific prerequisites (principles)

| Declaration class | Must exist before declare |
|-------------------|---------------------------|
| **State progression** | Active state known; TR transition legal; exit `RG-*` satisfied ACTIVE; HO cleared if boundary; scope mask allows target; **not** suspended |
| **Rollback** | RB-* pair legal; operator narrative for rework; acceptance of cascade (LRC-*) |
| **Gate satisfaction** | Criteria reviewed in authoritative layer/Runtime doc; evidence classes present; scope APPLICABLE; **not** declaring on stale upstream |
| **Gate invalidation** | Basis: FAIL evaluation, correction, or reconciliation — prior record identified |
| **Handoff acknowledgement** | Package ref exists when HO requires; blocked conditions cleared; gate context at boundary satisfied |
| **Lifecycle interpretation** | Charter endpoint explicit; active state coherent with interpretation |
| **Scope amendment** | Sponsor input or charter ref; impact on LR-07 understood; may require **defer** progression |
| **Reconciliation** | Integrity gap identified (ledger ≠ active, stale PASS treated active, invalid active code) |
| **Closure decision** | Declared endpoint reachable; gate-complete for path (GCO-*); handoffs through endpoint; AP-09 where full chain |

### When declaration is **prohibited**

| Condition | Prohibited declarations |
|-----------|-------------------------|
| Pre-Factory / not manifest-enrolled | All Engine progression declarations |
| Blocking gate open/stale/invalid for intended forward | State progression to next state |
| Handoff blocked | Handoff acknowledgement as CLEARED |
| `COMPLETE` active | Any outbound state progression |
| FT-* / DR-* violation | Target state progression |
| Undeclared integrity gap | Forward progression **until** reconciliation |
| `FACTORY_TRACK_SUSPENDED` | State progression, gate PASS that implies movement — **unless** lift declared first |
| Registry/catalog only knowledge | Any Engine declaration — catalog ≠ Engine (RA-05) |
| Criteria not reviewed | Gate satisfaction — evidence alone insufficient |

---

## Evidence Principles

Evidence поддерживает declaration — **не** заменяет declaration. Только **классы**, не файлы и не storage.

### Evidence class catalogue

| Class | Supports declarations | Operator use |
|-------|----------------------|--------------|
| **E1 — Charter & scope** | Recognition context, amendments, endpoint | Scope tier, exclusions, declared endpoint |
| **E2 — Classification & binding** | Gate satisfaction at intake/architecture phases | `site_type_code`, blueprint ref attestation |
| **E3 — Layer artefact ref** | Gate satisfaction, handoff | Pointer to authoritative body — criteria read **outside** Surface |
| **E4 — Validation run outcome** | `RG-VALIDATION_PASS`, content validation gates | PASS/FAIL summary ref — not criteria text |
| **E5 — Reviewer attestation** | Gate satisfaction where HITL required | Input to operator — **not** automatic PASS |
| **E6 — Gate/handoff declaration chain** | Reconciliation, rollback narrative | Prior declarations in audit trail |
| **E7 — Session assessment** | Any declaration after supervision | Playbook 03 outcome + reality/blocker summary |
| **E8 — AP-* sign-off** | Gates requiring lifecycle sign-off | Linked to gate outcome record (GS-07) |
| **E9 — External bound ref** | Charter-bound client approval, MIG/ORCA ref | **Never** sole evidence without operator binding |
| **E10 — Correction / supersession** | Reconciliation, gate invalidation | Points to `corrects_declaration_id` analog |

### Evidence principles (normative)

| ID | Principle |
|----|-----------|
| **EV-01** | Evidence **classes** may combine — ни один класс **не** auto-writes Engine |
| **EV-02** | Git activity, CI green, deploy — **не** E3/E4 unless charter binds ref — post-Factory by default |
| **EV-03** | Global layer ACCEPTED (T5) — **не** per-project gate evidence |
| **EV-04** | Stale upstream artefact — **blocks** new PASS until ref refreshed or rollback |
| **EV-05** | Playbook 03 **progression decision** outcome — рекомендует declaration; **не** equals declaration |
| **EV-06** | Physical REPORT/session note — optional **E7** carrier — **не** Engine SoT unless separate declaration act |

---

## Declaration Outcomes

После **valid** declaration операционные последствия — **логические** изменения в Engine composition, наблюдаемые через Tracking и Surface.

### Effects by plane

| Plane | Outcome of valid declaration |
|-------|------------------------------|
| **State** | Active code updates on progression/rollback; progression ledger append; eligibility snapshot recomputed |
| **Gate** | Outcome records added/updated; validity ACTIVE/STALE/INVALID; active gate set derived |
| **Handoff** | Events CLEARED/SUPERSEDED; package refs linked; ack recorded |
| **Lifecycle** | Active LC-* segment aligns with state; continuity LCC-* restored or break recorded |
| **Tracking** | Tier A freshness updates (TV-02); trackability TC-* may improve or flag gaps |
| **Surface** | Eight questions reflect new truth; stale markers visible per GV-05, HV-03 |
| **Audit** | Append-only declaration record (AT-01) |

### Outcome principles

| ID | Principle |
|----|-----------|
| **DO-01** | Declaration **не** исполняет layer work — только **indexes** operator truth |
| **DO-02** | Satisfied gate **не** implies state moved — progression declaration **отдельно** (GS satisfied ≠ movement) |
| **DO-03** | State moved **implies** operator claims exit gate + HO were satisfied at boundary — unless reconciliation corrects |
| **DO-04** | Rollback declaration **triggers** cascade semantics (GST-01, HV-03, AV-03) — not optional subset |
| **DO-05** | Closure declaration **не** authorizes deploy — Factory terminal only |
| **DO-06** | Registry orientation snapshot **unchanged** by Engine declaration — reconcile RS-03 if catalog edited separately |

### Relationship to Playbook 03 session outcomes

| Session outcome (Playbook 03) | Typical declaration follow-up |
|------------------------------|--------------------------------|
| **Progression decision** | State progression + gate + handoff declarations as needed |
| **Reconciliation decision** | Reconciliation declaration class |
| **Scope / charter amendment decision** | Scope amendment → possible rollback RB-10 |
| **Defer / No action** | **No** Engine declaration required |
| **Clarification required** | **No** progression until MRDY/SRDY gaps closed |

---

## Invalid Declaration Principles

**Invalid declaration** — акт, который **не должен** становиться authoritative в Engine, или должен быть **немедленно superseded** reconciliation.

### Invalidity categories

| Category | Description | Typical response |
|----------|-------------|------------------|
| **Insufficient evidence** | PASS or progression without E3/E4/E5 where required | Supersede; do not treat as ACTIVE |
| **Authority violation** | Non-operator or external system as declarer | Reject; no index write |
| **Contradiction** | PASS while mapped validation FAIL; active `SEO_READY` while ledger says `BLOCK_READY` | Reconciliation before trust |
| **Unsupported progression** | Forward while blocking gate open/stale/invalid | Invalidate progression record; restore active |
| **Illegal rollback** | `COMPLETE` → any; multi-hop RB without charter | Reject rollback declaration |
| **Scope violation** | Progression into EXCLUDED state without charter jump | Invalidate; amend charter or rollback |
| **Handoff without gate** | HO CLEARED while exit `RG-*` insufficient | Invalidate HO; freeze segment |
| **Criteria bypass** | Gate PASS without operator criteria review | Invalidate; re-declare after review |
| **Catalog substitution** | Registry card treated as gate/state truth | Invalidate; Engine reconciliation |
| **Phantom declaration** | Assumed progress from filesystem/CI only | **Undeclared** — not invalid record — remediate with explicit declaration |

### Invalidity principles (normative)

| ID | Principle |
|----|-----------|
| **IV-01** | Invalid declaration **не** удаляется silently — supersession or reconciliation record (AT-01) |
| **IV-02** | Stale PASS **не** invalid merely by age — invalid when rollback/upstream **without** re-declaration |
| **IV-03** | Integrity gap discovery **invalidates trust**, not necessarily every historical record |
| **IV-04** | Operator **must not** stack forward declarations to «skip» remediation |
| **IV-05** | Manifest/Registry enrollment declarations **не** валидируют** Engine progression by themselves |

---

## Reconciliation Principles

**Reconciliation** — declaration class, устраняющий **конфликт интерпретаций** между assessed reality (Playbook 03), Engine indexes, и optional catalog snapshot.

### When reconciliation is required

| Signal | Conflict type |
|--------|---------------|
| Active state ≠ latest progression ledger | Ledger integrity (TC-03) |
| Stale PASS used as blocking authorization | Gate hygiene (TC-04, GST-*) |
| Active Runtime code invalid (SV-05) | State integrity |
| HO refs ≠ handoff event index | Handoff alignment (TC-05) |
| Catalog snapshot contradicts Engine (RS-03) | Portfolio vs per-project |
| Post-rollback indexes not cascaded | Cascade incomplete (LRC-*) |
| Duplicate identity shells | Enrollment integrity (OQ-R04 analog) |

### Reconciliation workflow (operational, not implementation)

```text
  Detect conflict (Surface session / audit)
        │
        ▼
  Halt forward declarations (IV-04)
        │
        ▼
  Classify conflict plane (state / gate / handoff / charter / catalog)
        │
        ▼
  Operator reconciliation declaration
        │── may: restate active, mark STALE, SUPERSEDE HO, amend charter ref
        │── may: require rollback declaration instead of in-place fix
        ▼
  Re-run Playbook 03 reality + blocker assessment
        │
        ▼
  Resume normal declaration classes when TC-* coherent
```

### Reconciliation principles (normative)

| ID | Principle |
|----|-----------|
| **RC-01** | Reconciliation **precedes** forward progression when integrity alarm (Playbook 03) |
| **RC-02** | Reconciliation **не** mutates Foundation documents or artefact bodies |
| **RC-03** | Reconciliation **may** reference correction chain — append-only |
| **RC-04** | Catalog reconciliation **≠** Engine reconciliation — may require **both** |
| **RC-05** | Reconciliation **не** auto-rollback — operator may **choose** RB-* after assessment |

---

## Closure And Amendment Principles

Без переопределения lifecycle model — только **declaration discipline** для scope и terminal outcomes.

### Scope amendment declarations

| Principle | ID | Statement |
|-----------|-----|-----------|
| Charter drives mask | **CA-01** | Amendment declares new LR-07 applicability / endpoint — Engine **indexes**, не invent scope |
| Stale review | **CA-02** | Amendment may STALE gates per GST-03 — operator re-evaluates active set |
| Rollback coupling | **CA-03** | Material scope shrink through generation boundary → **likely** RB-10 — operator declares |
| Defer movement | **CA-04** | Amendment mid-session → Playbook 03 **defer** until mask explicit |

### Closure declarations

| Closure type | Declaration bundle (conceptual) | Runtime terminal? |
|--------------|--------------------------------|-------------------|
| **Full Factory closure** | State → `COMPLETE`; `RG-PROJECT_COMPLETE` + HO-13; AP-09; lifecycle LC-13 | **Yes** |
| **Partial Factory closure** | Active = charter endpoint state; `FACTORY_TRACK_CLOSED_PARTIAL`; gate-complete for prefix; **not** `RG-PROJECT_COMPLETE` unless at `COMPLETE` | **No** |
| **Suspended track** | `FACTORY_TRACK_SUSPENDED` declared; active frozen | **No** |
| **Suspension lift** | Clear suspension; resume declarations from frozen segment | **No** |

### Closure/amendment principles

| ID | Principle |
|----|-----------|
| **CL-01** | Partial closure **must** be charter-explicit (LPC-03, OCM-03) — implicit ambiguity = invalid closure |
| **CL-02** | Partial closure **≠** `COMPLETE` unless charter includes full LC-13 path |
| **CL-03** | Withdrawn catalog (Playbook 02) **≠** Factory track closure |
| **CL-04** | Client deploy **не** triggers closure declaration |
| **CL-05** | Suspension **не** substitute for LS-* halt — different operator narratives |

---

## Workflow Completion

### When Project Declaration Workflow is considered complete (document)

**Playbook 04** как документ **complete** когда организация приняла его как норматив для превращения assessed reality в declared truth — deliverable = этот файл.

### Per-declaration instance completion

Один **declaration workflow instance** завершён когда:

| # | Criterion |
|---|-----------|
| 1 | Declaration class **named** (DC-*) |
| 2 | Prerequisites P0–P5 and class-specific **attested** |
| 3 | Evidence classes **cited** (E*) where required |
| 4 | Operator with DA-01 authority **performed** act |
| 5 | Valid declaration **produced** Engine outcomes (DO-*) or invalidity **handled** (IV-*, RC-*) |
| 6 | Playbook 03 follow-up **scheduled** if trackability changed |

### Relationship to existing playbooks

```text
  Playbook 01  Manifest enrollment     ──▶  Factory-scoped + manifest-enrolled
  Playbook 02  Registry enrollment     ──▶  catalog discoverability [optional]
  Playbook 03  Surface session         ──▶  assessed reality + session outcome
  Playbook 04  Project declaration     ──▶  declared truth in Engine indexes
        │                                        │
        └──────── repeat 03 → 04 cycle ──────────┘
              throughout Factory track life
```

| Playbook | Feeds Playbook 04 | Playbook 04 feeds |
|----------|-------------------|-------------------|
| **01** | Valid project exists | Intake state/gate declarations after enrollment |
| **02** | — | **No** Engine merge — parallel catalog plane |
| **03** | Progression / reconciliation / defer decisions | Fresh Surface truth on next session |

### Future artifacts (reference only)

| Future artifact | Relationship |
|-----------------|--------------|
| Gate sign-off ritual specialization | May **narrow** gate satisfaction steps — **не** replace DA-01 |
| Partial closure playbook (OQ-S6-09) | Specialized **closure** triggers using CL-* |
| RT-G10 / RT-G04 implementation | May **persist** logical outcomes — **не** change declaration semantics |
| Operator Display (RT-G12) | May **capture** declaration acts — **не** author them |

### Operational readiness

Factory declaration discipline is **usable** when operators treat Playbook 04 as **mandatory** companion to Playbook 03 **progression** outcomes — per OR-02 human-operated model.

---

## Explicit Non-Claims

This playbook and Project Declaration Workflow v1:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** **automation**, **agent workflow**, n8n, CI-driven declarations, or **orchestrator**;
- **are not** **storage**, **database**, **file format**, **YAML**, **JSON**, **schemas**, or folder standards;
- **are not** **implementation** of manifest (RT-G10), registry (RT-G05), tracking storage (RT-G04), or display (RT-G12);
- **are not** a **declaration template**, **declaration form**, **declaration registry**, or **declaration database**;
- **are not** **UI**, **dashboard**, **CLI**, or operator display product;
- **do not** redefine Engine Stages 1–6, Runtime states/`RG-*`/`HO-*`, Gate/Lifecycle/State/Tracking models, or Playbooks 01–03;
- **do not** define physical declaration artefacts, serialization, or central declaration catalog;
- **do not** claim automated enforcement, Gate Results System, or Lifecycle System exists in-repo.

Human-operated declaration remains the v1 operating reality per [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) and [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md).

---

## Open Questions

Bounded for **future operational artifacts** — not resolved in Playbook 04.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-PD01** | Minimum evidence bundle per gate class (E3+E5 always?) | **OPEN** — operator convention |
| **OQ-PD02** | Single sitting: Playbook 03 close + declarations same session | **OPEN** — ties OQ-TSW05 |
| **OQ-PD03** | `PASS_WITH_WARNINGS` — gate satisfaction vs invalid | **OPEN** — OQ-S6-08 |
| **OQ-PD04** | PHASE_SLICE: declarations per shell vs per slice | **OPEN** — OQ-S6-03 |
| **OQ-PD05** | Formal declaration attestation carrier (REPORT vs index-only) | **OPEN** — implementation plane |
| **OQ-PD06** | MIG correlation as E9 only vs standard trigger | **OPEN** — OQ-OM08 |
| **OQ-PD07** | Partial closure declaration minimum bundle standardization | **OPEN** — OQ-S6-09 specialized playbook |
| **OQ-PD08** | Duplicate identity reconciliation declaration steps | **OPEN** — OQ-R04 |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **Project Declaration Workflow v1** as Operational Playbook 04 **complete** — use after Playbook 03 when session outcome is progression, reconciliation, or closure.
2. **Operational Design continuation (separate tasks):**
   - Registry index card template (OQ-R02) — portfolio only
   - Partial closure operator playbook (OQ-S6-09) — specializes CL-*
   - Optional gate sign-off ritual narrow playbook
3. **Per active Factory Project:** Never treat layer/git work as progress without explicit declaration class; record reconciliation before forward after integrity alarms.
4. **Do not start:** declaration storage, declaration registry product, automation agents, runtime — unless explicitly authorized.
5. **Optional P3:** Reference Playbook 04 from [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) Operational Design row — operator action.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether operators already run ad-hoc declaration discipline | **UNKNOWN** — no canonical declaration store |
| Default bundling of gate+state+HO in one operator act | **not standardized** in v1 |
| Calendar for RT-G04/10 persistence of declaration records | **not scheduled** |

---

*Factory Project Declaration Workflow v1 — Operational Playbook 04. Canonical location: `workspaces/website-factory-reference-v1/`. Git: no commit, no push.*

---

# REPORT — Factory Project Declaration Workflow v1

**Stage:** Operational Design — Operational Playbook 04 (Project Declaration Workflow)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md` (created)  
**Summary:** Определён операционный workflow декларирования Factory reality: authority (factory operator, human-only), классы declarations (state, rollback, gate, handoff, lifecycle, scope, reconciliation, closure), prerequisites, evidence classes, outcomes по Engine planes, invalidity и reconciliation, closure/amendment principles, связь с Playbooks 01–03 — без runtime, automation, storage, templates, registry, implementation.  
**Git:** no commit, no push (per task charter).
