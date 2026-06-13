# REPORT — Factory Registry Enrollment Workflow v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Operational Design — **Operational Playbook 02** (Registry Catalog Enrollment Workflow)  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 **COMPLETE**; Post-Engine Doctrine **COMPLETE**; [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) **COMPLETE**; [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) **COMPLETE**  
**Тип:** operational workflow only — **без** runtime, automation, implementation, storage, schemas, agents  
**Не переопределяет:** [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md), [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), Engine Stages 1–6, Runtime Architecture  

---

## Purpose

### Зачем существует Registry Catalog Enrollment Workflow

**Registry Catalog Enrollment Workflow** — второй операционный playbook Website Factory. Он описывает **человеко-исполняемую** последовательность, по которой **manifest-enrolled** Factory Project становится **видимым в Factory portfolio** — то есть получает доктринальный статус **catalog-discoverable** через operator-declared catalog enrollment.

Workflow закрывает координационную проблему **мультипроектной ориентации**:

| Проблема | Как workflow решает |
|----------|---------------------|
| Проект существует в Factory scope, но оператор не видит его в портфеле | Явное **Registry enrollment decision** (decision class **I**) после manifest path |
| Git-папки, incoming paths или workspace discovery подменяют каталог | Enrollment **не** от сканирования — только **declaration** (RD-04, RAP-10) |
| Registry путают с Tracking, Manifest или Site Type Registry | Workflow фиксирует **роль каталога** — distinction summaries, не seven questions |
| Ожидание physical registry-файла блокирует portfolio visibility | **Catalog-discoverable** = doctrinal outcome; persistence — **implementation**, не условие workflow |
| Один оператор ведёт несколько cases без «списка проектов» | Portfolio discoverability **отдельно** от per-project Manifest depth |

Оператор после прохождения workflow должен уметь ответить **без чтения всего workspace**:

- Когда разрешено Registry enrollment?
- Что делает проект **registry-ready**?
- Кто принимает решение о enrollment?
- Какие **классы** evidence требуются?
- Что блокирует enrollment?
- Как проект становится **discoverable**?
- Как проект **покидает** Registry без уничтожения Factory reality?

### Что workflow **не** решает

| Вне scope | Почему |
|-----------|--------|
| Factory-scoped recognition, manifest-ready, manifest enrollment | [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) — **предшествует** |
| Per-project movement, gates, state transitions | Engine + Runtime — **после** catalog enrollment |
| Полная observability (seven/eight tracking questions) | Tracking + Surface — per-project path, **не** portfolio card |
| Physical registry index, paths, card field templates | RT-G05 **implementation** — NOT STARTED |
| Persistence, state store, manifest serialization | RT-G04, RT-G10 implementation |
| Automation, agents, n8n, CI catalog sync | Explicitly forbidden in v1 |
| Queue rank, scheduling, prioritization | RT-G06 — **FUTURE** |
| Layer artefact production, Site Type Registry operations | Foundation / T1 — RAP-11 |

**Граница playbook:** от **сигнала catalog enrollment need** (при уже **manifest-enrolled** project) до **registry-enrolled / catalog-discoverable** (или явного deferred/rejected/withdrawn). Manifest enrollment — **обязательный предшественник**, не часть этого workflow.

```text
  MANIFEST PLAYBOOK (01)              THIS WORKFLOW (02)              POST-ENROLLMENT
  Recognition → manifest-enrolled            │                              │
        │                                    ▼                              ▼
        └────────────────────────▶  Readiness → Decision  →  Portfolio select → Manifest → Tracking
                                              (catalog-discoverable)              (per-project depth)
```

### Registry vs Manifest vs Tracking (операционно)

| Surface | Отвечает на | Этот workflow |
|---------|-------------|---------------|
| **Manifest** | «Что это за **один** проект? С чего начать?» | **Предусловие** — manifest-enrolled |
| **Registry** | «**Какие** Factory projects в портфеле? Как отличить?» | **Цель** workflow |
| **Tracking** | «Где **сейчас**? Что блокирует? Что прошло?» | **Не** enrollment criteria; orientation snapshot **non-authoritative** (RS-03) |

**Существование** logical Factory Project (Engine) **≠** **discoverability** в каталоге. **Discoverability** **≠** **fully trackable** или **surface-ready**.

---

## Foundation Dependencies

Workflow **наследует** принятые артефакты **без их изменения**. При конфликте — побеждает более специфичный charter (Registry, Manifest), затем Operational Model.

### Tier 0 — Operational model and Playbook 01

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | Decision class **I** (catalog enrollment), operator path Registry→Manifest→Tracking, human-only registry withdrawal, optional Registry |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Предусловие manifest-enrolled; Registry Eligibility Principles; ordering normative |

### Tier 1 — Post-Engine doctrine (обязательные)

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | RRDY-*, RD-*, RA-*, RM-*, RE-*, RS-*, RAP-*, discovery/withdrawal doctrine |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | MRDY-*, MR-01, MR-02, manifest entry anchor — **не** переопределяется |
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | RE-01, VP-05, RA-05 — portfolio glance **не** заменяет Surface |
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Logical identity vs registry entry (ES-03, RA-03) |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Граница: Registry **не** seven questions |

### Tier 2 — Engine context (reference)

Factory Engine Stages 1–6; Runtime Architecture v1. Workflow **не** переопределяет state codes, gates или catalog lifecycle as Runtime states.

**Authority precedence:** Foundation + Engine + Manifest/Registry/Tracking Surface charters → Manifest Playbook 01 → **этот playbook** для Registry enrollment steps → будущий registry index card template (OQ-R02) **не может** нарушить RA-*, RD-*, RM-*, RAP-*.

---

## Enrollment Trigger Principles

Registry enrollment workflow **стартует** не от технического события (commit, folder create, CI green), а от **операционной потребности** сделать уже manifest-enrolled case **видимым в Factory portfolio**.

### Классы триггеров (не исчерпывающий список)

| Trigger class | Typical signal | Operational note |
|---------------|----------------|------------------|
| **Manifest enrollment completed** | Playbook 01 outcome **Enrolled** | Наиболее частый нормативный триггер — case orientable |
| **Portfolio visibility request** | Operator или sponsor: «нужен этот case в общем списке Factory projects» | Требует manifest-enrolled **до** enrollment |
| **Multi-project session start** | Оператор открывает сессию с несколькими активными tracks | Catalog enrollment **per project**, не batch automation |
| **Governance / coordination requirement** | Charter, program, или Factory discipline требует portfolio listing | Enrollment **declaration**, не policy engine |
| **Active project already in motion** | State beyond `NEW_PROJECT`, gates declared — **догоняющий** catalog enrollment | Допустимо, если manifest-enrolled; readiness по RRDY-* |
| **Re-enrollment after withdrawal** | Ранее withdrawn — снова discoverable | **Новая** enrollment declaration — append-only (RAP-17 analog) |

### Принципы триггера

| ID | Principle |
|----|-----------|
| **RET-01** | Trigger **не** создаёт Factory Project — logical project **уже** существует (RA-02) |
| **RET-02** | Trigger **не** равен Registry enrollment — между ними **registry readiness evaluation** |
| **RET-03** | Trigger **без** manifest-enrolled precondition → workflow **не открывается** — сначала Playbook 01 (RAP-16, RD-02) |
| **RET-04** | Raw workspace / git tree / incoming folder **без** manifest path — **не** триггер catalog enrollment (RD-04) |
| **RET-05** | Site Type Registry maintenance, global layer work, MIG session alone — **не** Factory Project catalog triggers (RD-01, RAP-11) |

### Событие, открывающее workflow

**Workflow instance opens** when operator фиксирует: *«manifest-enrolled Factory Project требует решения о catalog enrollment / portfolio discoverability»*.

Это **не** state transition, **не** registry storage write, **не** Tracking mutation — только **начало** операционной проверки RRDY-* и enrollment decision.

---

## Registry Readiness Evaluation

Оценка **только** по [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) — **категории знания каталога**, не поля, не файлы, не schemas.

### Обязательные предусловия (до RRDY)

Перед evaluation operator подтверждает **вне** RRDY checklist:

| # | Precondition | Source |
|---|--------------|--------|
| P1 | Factory-scoped logical project **exists** | RA-02, Object Model |
| P2 | **Manifest-enrolled** (Playbook 01 **Enrolled**) | MRDY-* satisfied; entry anchor identified |
| P3 | Operator understands Manifest **precedes** Registry (RM-04, RA-04) | MRDY-07 / RRDY-06 |

### Registry-ready criteria (RRDY-*)

Перед положительным enrollment decision operator подтверждает:

| # | Criterion | ID | Evaluation question (operational) |
|---|-----------|-----|----------------------------------|
| 1 | Logical Factory Project identity **explicit** and Factory-scoped | **RRDY-01** | Есть ли устойчивая logical identity, отличимая от registry entry slot? |
| 2 | Manifest entry anchor **identified** (manifest-ready) | **RRDY-02** | Указана ли доктринальная точка входа для этого case (RM-01)? |
| 3 | Registry entry **distinct** from logical identity understood | **RRDY-03** | Понимает ли operator, что catalog slot ≠ project identity (ES-03, RA-03)? |
| 4 | Distinction summaries **sufficient** for portfolio | **RRDY-04** | Достаточно ли charter label, scope tier, endpoint **categories** чтобы отличить case в списке? |
| 5 | Discoverability status category **explicit** | **RRDY-05** | Заявлена ли категория discoverable (vs withdrawn/archived intent at enrollment)? |
| 6 | Operator understands Registry ≠ Tracking ≠ Manifest | **RRDY-06** | Нет ли планов дублировать gate index или Manifest bodies в catalog card? |

### Registry-incomplete signals (блокируют enrolled)

| Condition | Action in workflow |
|-----------|-------------------|
| Not Factory-scoped / no logical identity | **Reject** — not catalog-eligible (RRDY-01) |
| Not manifest-enrolled | **Defer** — complete Playbook 01 first (RRDY-02, RD-02) |
| Registry entry ID conflated with project identity | **Defer** — integrity remediation (RRDY-03, RAP-09) |
| Insufficient distinction summaries for portfolio | **Defer** — RRDY-04 |
| Discoverability category unstated | **Defer** — RRDY-05 |
| Catalog card duplicates live Tracking gate/handoff index | **Defer** — RAP-06, RA-05 |
| Orientation snapshot contradicts Engine without flag | **Defer** — RS-03 |
| Site Type Registry row mistaken for Factory Project | **Reject** or **Defer** — RAP-11 |

### Важные соотношения (не блокеры при норме)

| Concept | Relation to enrollment |
|---------|------------------------|
| **Registry-ready ⊄ gate-complete** | Mid-chain `SEO_READY` may enroll — normal |
| **Registry-ready ⊄ fully trackable** | Early `NEW_PROJECT` with empty indexes — valid (RD discoverable analog) |
| **Registry-ready ⊄ surface-ready** | Surface depth — **после** portfolio select |
| **Physical registry artefact** | **Не** требуется для RRDY в v1 |

### Evaluation ownership

**Factory operator** выполняет RRDY-* attestation; **reviewer** may audit portfolio integrity — **не** заменяет operator enrollment declaration (OA-ACT-01, OA-ACT-02 analog).

---

## Enrollment Decision Model

### Кто принимает решения

| Decision | Owner (v1) | Human-only |
|----------|------------|------------|
| Open workflow on trigger | Factory operator | **Yes** |
| RRDY-* attestation | Factory operator | **Yes** |
| Catalog enrollment outcome (enrolled / deferred / rejected / withdrawn) | Factory operator | **Yes** |
| Discoverability status category at enrollment | Factory operator | **Yes** |
| Distinction summary content (derived from charter) | Operator + sponsor input on charter — operator **declares** catalog summary | **Yes** |
| Registry withdrawal (later) | Factory operator | **Yes** — **отдельная** declaration |
| State / gate / handoff declarations | Factory operator | **Yes** — **вне** этого workflow |

### Что остаётся человеческим навсегда в v1

- Catalog membership enrollment и withdrawal  
- Attestation registry-ready (RRDY-*)  
- Binding logical identity ↔ catalog entry (без silent remap — RS-01)  
- Portfolio orientation snapshot reconciliation honesty (RS-03)  
- Любая «enrollment by discovery» (repo scan, agent index, CI artifact)

### Что **никогда** не может быть автоматическим

| Forbidden automation | Principle |
|---------------------|-----------|
| Auto-enroll on manifest file write | MAP-12 analog; RT-G10 impl ≠ enrollment |
| Auto-enroll on git folder / incoming path | RD-04, RAP-10 |
| Auto-pass RRDY-* from template without operator attestation | Human-operated v1 |
| Agent-declared catalog-discoverable without operator record | OA-ACT-04 analog |
| CI / webhook / deploy event as catalog authority | RAP-15 |
| Registry write as side-effect of manifest enrollment | Playbook 01 explicit block |
| Auto-sync catalog snapshot as authoritative Tracking copy | RAP-06, OQ-R08 bounded |

Future tooling **may assist** distinction summaries; **ownership** enrollment decision остаётся у operator.

### Decision record (logical, not format)

Каждое решение enrollment порождает **declaration category**:

- Outcome code (enrolled / deferred / rejected / withdrawn)  
- Operator identity (role class)  
- Timestamp (logical)  
- RRDY checklist result summary  
- Discoverability category declared (discoverable default vs explicit archived intent if applicable)  
- Pointer categories: logical identity ref, manifest entry anchor ref, registry entry slot doctrine (distinct from identity)  
- Evidence classes used (см. ниже)  
- If deferred: gap list mapped to RRDY-* / preconditions  
- If rejected: reason category (never Factory-scoped, wrong registry type, duplicate, integrity)

**Append-only:** correction = new declaration — not silent erase (RAP-17, AT-01 analog at catalog level).

---

## Enrollment Outcomes

### Primary outcomes

| Outcome | Meaning | Catalog / project state |
|---------|---------|-------------------------|
| **Enrolled** | Registry enrollment workflow **complete**; RRDY-* attested; operator declared catalog membership | **Catalog-discoverable** in default Factory portfolio view (RD-03); logical project **unchanged** in Engine; manifest-enrolled **сохраняется** |
| **Deferred** | Manifest-enrolled, но RRDY gaps or integrity **явные** | **Not** catalog-discoverable; remains manifest-enrolled only |
| **Rejected** | Case **не** будет в Factory Project catalog (never eligible, wrong catalog, duplicate entry policy) | No catalog slot; may still be manifest-enrolled Factory Project **или** pre-catalog reject |
| **Withdrawn** | Operator **закрывает** enrollment attempt before positive enrolled | Not discoverable; may re-open workflow later (**new** instance) |

### Дополнительные различия (не отдельные outcome codes)

| Situation | Treatment |
|-----------|-----------|
| **Enrolled without prior deferred gaps** | **Норма** при clean RRDY pass |
| **Manifest-enrolled, Registry never sought** | **Норма** v1 — decision I optional (Operational Model) |
| **Enrolled then later withdrawn** | **Withdrawal playbook path** — not re-run enrollment as «un-enroll» silent delete |
| **Archived after Factory terminal** | Catalog lifecycle category change — **may** follow enrollment; OQ-R03 OPEN for extended view |

Outcome **«superseded»** для catalog binding: rebinding registry entry to **different** logical identity requires **explicit** declaration (RS-01) — not default enrollment outcome.

### Outcome → operator next step

| Outcome | Next step (operational) |
|---------|-------------------------|
| **Enrolled** | Portfolio path: select project from catalog → Manifest anchor → Tracking → Surface when ready |
| **Deferred** | Close RRDY gaps; do **not** use Tracking or gate work as substitute for catalog integrity |
| **Rejected** | Document rejection; no portfolio pointer; revisit manifest path only if case still valid |
| **Withdrawn** | Archive trigger evidence; ensure no phantom discoverable entry |

---

## Discoverability Principles

Discoverability — **доктринальная видимость в Factory portfolio**, не физический индекс и не runtime state.

### Как проект становится discoverable

A Factory Project becomes **catalog-discoverable** when **all** hold (Registry Charter discovery doctrine + this workflow **Enrolled**):

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | Factory-scoped logical project **exists** | RD-01 |
| 2 | **Manifest-enrolled** (MRDY-* / Playbook 01) | RD-02, RM-01 |
| 3 | **Registry-ready** (RRDY-*) attested | Catalog integrity |
| 4 | Operator **declared** catalog enrollment — this workflow **Enrolled** | RD-04 |
| 5 | Manifest entry anchor **identified** on catalog card | RM-01, RD-02 |

```text
  EXISTS (Engine)     ORIENTABLE (Manifest)     DISCOVERABLE (Registry)
       │                      │                         │
       ▼                      ▼                         ▼
  logical project      manifest-enrolled          catalog-discoverable
  at recognition       Playbook 01 complete       Playbook 02 Enrolled
```

### Discoverability vs existence

| Dimension | Exists | Discoverable |
|-----------|--------|--------------|
| **Definition** | Logical Factory Project in Engine model | Listed in Factory-scoped **portfolio catalog** doctrine |
| **Moment** | Factory-scoped recognition (may precede manifest) | After **Enrolled** outcome this workflow |
| **Operator question** | «Does this production case run in Factory?» | «Can I **find** it among Factory projects?» |
| **Without other** | May exist years without Registry | May **not** exist without prior logical project |

### Discoverability vs Tracking

| Dimension | Discoverable | Tracking |
|-----------|--------------|----------|
| **Scope** | Multi-project portfolio | Single-project composition |
| **Depth** | Distinction **summaries** + pointers | Seven questions, gate index, audit trail |
| **Authority** | Catalog lifecycle — **non-authoritative** orientation snapshot (RS-03) | Engine indexes — authoritative for movement |
| **Anti-pattern** | Copying live gate index to catalog card | RAP-06, RA-05 |
| **Operator rule** | RE-01: seven questions **never** primary on Registry card | Manifest → Tracking path after select |

**Discoverable ⊄ fully trackable:** empty gate indexes at `NEW_PROJECT` — valid discoverable entry.

### Discoverability vs manifest-enrolled

| State | Meaning |
|-------|---------|
| **Manifest-enrolled** | Per-project entry anchor + minimum understanding — Playbook 01 |
| **Catalog-discoverable** | In default portfolio per RD-03 — Playbook 02 **Enrolled** |

Проект **manifest-enrolled** без Registry enrollment — **валидная** v1 практика. Обратное (**discoverable** without manifest-enrolled) — **запрещено** (RAP-16).

### Default vs extended portfolio view

Default view shows **discoverable** active portfolio entries. **Withdrawn** / **archived** categories may appear in extended view — **implementation OPEN** (OQ-R03); workflow declares category at enrollment or withdrawal.

---

## Operational Evidence Principles

Поддержка Registry enrollment decisions — **классы evidence**, не хранилища, не card templates, не folders.

### Evidence classes

| Class | Supports | Typical content (category, not format) |
|-------|----------|----------------------------------------|
| **R1 — Manifest enrollment attestation** | Preconditions P2 | Playbook 01 Enrolled record (E7 analog) or operator attestation manifest-enrolled |
| **R2 — Logical identity & distinction** | RRDY-01, RRDY-04 | Identity rationale; charter label; why distinct from other catalog entries |
| **R3 — Manifest entry anchor reference** | RRDY-02, RM-01 | Pointer category to per-project entry anchor |
| **R4 — Scope & endpoint summaries** | RRDY-04 | Scope tier, declared endpoint **summary** for portfolio (not full charter body) |
| **R5 — Classification summary** (when present) | RRDY-04 | `site_type_code` label category after classification — not Site Type Registry authority |
| **R6 — Registry role integrity** | RRDY-06 | Acknowledgment Registry ≠ Tracking ≠ Manifest ≠ Site Type Registry |
| **R7 — Registry enrollment decision record** | Outcome | Enrolled / deferred / rejected / withdrawn + operator + logical time |
| **R8 — RRDY evaluation record** | Readiness | Per-criterion pass/fail with gap notes |
| **R9 — Discoverability category declaration** | RRDY-05, RD-03 | Explicit discoverable vs intentional non-discoverable at this time |
| **R10 — Catalog binding doctrine** | RRDY-03, RS-01 | Attestation registry entry slot ≠ logical identity |
| **R11 — Orientation snapshot honesty** (optional at enroll) | RS-03 | If snapshot shown: reconciled or flagged stale-risk |
| **R12 — Prior catalog declaration** (if re-enrollment) | Audit | Pointer to withdrawn/superseded enrollment being corrected |

### Evidence principles

| ID | Principle |
|----|-----------|
| **REP-01** | Evidence **подтверждает категории каталога**, не заменяет Engine indexes |
| **REP-02** | R1 **обязателен** для open workflow — без manifest-enrolled **нет** Registry enrollment |
| **REP-03** | R4/R5 summaries **не** authoritative copy of Manifest (RM-02) — follow charter amendments |
| **REP-04** | Git paths, SERP, screenshots — **допустимы** как R2 attachments, **не** as RD-04 discovery |
| **REP-05** | Reuse Manifest evidence classes E1–E6 **allowed** for summaries — **не** skip R7/R8 attestation |

### What evidence is NOT

- Not gate PASS records or handoff bodies  
- Not Tracking composition export as sole authority  
- Not physical registry file or index card template instance  
- Not automated portfolio crawler output  

---

## Registry Withdrawal Principles

Withdrawal — **изменение catalog visibility**, не удаление Factory Project, Manifest, или Engine history.

### Как проект покидает Registry visibility

| Situation | Catalog doctrine | Engine / Manifest / Tracking |
|-----------|------------------|------------------------------|
| Operator declares **withdrawn** from portfolio | **Ceases default discoverability** (RD cease table) | Logical project **may remain**; manifest-enrolled **may remain** |
| **Archived** after `COMPLETE` or partial closure | Historical catalog membership — distinction from active portfolio | Terminal metadata visible; Tracking audit **preserved** |
| **Duplicate entry** reconciled | One logical identity — one catalog entry (RA-03) | Correction declaration — not silent delete (RAP-17) |
| **Mistaken enrollment** | New declaration record corrects — **not** erase history | Integrity remediation |
| **Never was Factory-scoped** | Entry **invalid** — should not have been enrolled | Reject narrative; audit trail |

### Withdrawal vs project reality

| Principle | Statement |
|-----------|-----------|
| **RW-01** | Ceasing discoverability **≠** deleting Factory Project |
| **RW-02** | Ceasing discoverability **≠** revoking manifest-enrolled — unless separate manifest amendment path (out of scope Playbook 02) |
| **RW-03** | Ceasing discoverability **≠** erasing Tracking indexes, gate history, or state instance |
| **RW-04** | Withdrawn project **may** re-enter catalog via **new** enrollment workflow instance + R12 evidence |
| **RW-05** | Suspended track (`FACTORY_TRACK_SUSPENDED`) — **не** automatic withdrawal; operator **declares** catalog visibility separately |

### Withdrawal decision model

| Decision | Owner (v1) | Human-only |
|----------|------------|------------|
| Declare withdrawn from portfolio | Factory operator | **Yes** |
| Declare archived catalog category | Factory operator | **Yes** |
| Re-enroll after withdrawal | Factory operator | **Yes** |

**Never automatic:** deploy complete, `COMPLETE` state, CI inactive repo — **не** withdraw catalog without operator declaration.

### Withdrawal evidence classes (logical)

| Class | Supports |
|-------|----------|
| **W1 — Withdrawal declaration record** | Outcome + operator + logical time |
| **W2 — Reason category** | Program ended, mistaken enrollment, duplicate, client request, portfolio hygiene |
| **W3 — Prior enrollment reference** | R7/R12 linkage |
| **W4 — Continuity attestation** | Manifest/Tracking remain for audit (if applicable) |

---

## Failure And Exception Handling

### Incomplete projects (catalog perspective)

| Situation | Treatment |
|-----------|-----------|
| Manifest-enrolled but distinction summaries thin | **Deferred** — RRDY-04 |
| Manifest entry anchor unclear | **Deferred** — RRDY-02 (should not happen if Playbook 01 clean) |
| Catalog card draft includes gate outcomes | **Deferred** — RAP-06 remediation |
| Discoverability category not stated | **Deferred** — RRDY-05 |

**Запрещено:** **Enrolled** with open RRDY fails; using portfolio listing as substitute for Manifest topology (RAP-07).

### Uncertain projects

| Situation | Treatment |
|-----------|-----------|
| Pilot external-only vs Factory catalog (OQ-OM07 analog) | **SAFE UNKNOWN** until case charter — default **Defer** |
| PHASE_SLICE: one catalog entry vs per slice (OQ-R05) | **Defer** until operator convention explicit |
| Duplicate logical identity suspected | **Defer** or **Reject** — OQ-R04 operational detail OPEN |
| Orientation snapshot unknown vs Engine | **Defer** — RS-03 until reconciled or flagged |

Uncertainty → **Defer** with documented gaps, not **Enrolled** «исправим в каталоге позже».

### Legacy projects

| Situation | Treatment |
|-----------|-----------|
| Long-running workspace never manifest-enrolled | **Defer** Registry — Playbook 01 first |
| De-facto «folder catalog» without declarations | **Reject** or remediate: recognition + manifest + registry sequence |
| v0 mars-website-factory pack vs reference v1 routing | **Defer** — OQ-OM06; enrollment declarations must name corpus category |
| Triumph / pilot in catalog vs external-only | **SAFE UNKNOWN** per case charter |

Legacy **не** получает discoverability by age or repo presence alone (RD-04).

### Integrity violations during workflow

| Violation | Response |
|-----------|----------|
| Registry before manifest-enrolled | Stop — RAP-16 — **Defer** or roll back catalog declaration |
| Registry entry ID = project identity | Stop — RAP-09 — **Defer** |
| Site Type Registry conflated with Factory catalog | Stop — RAP-11 — **Reject** or **Defer** |
| Catalog snapshot authoritative over Tracking | Stop — RAP-06 — **Defer** |

### Exception: duplicate catalog entry

One logical identity — one catalog entry (RA-03). Second enrollment → **Reject** or merge via explicit declaration (OQ-R04 OPEN) — **не** second **Enrolled** without reconciliation record.

---

## Workflow Completion

### When Registry Enrollment Workflow is complete

Workflow считается **завершённым** только при outcome **Enrolled** и выполнении:

| # | Completion criterion |
|---|---------------------|
| 1 | Preconditions P1–P3 **satisfied** |
| 2 | RRDY-01…06 **attested pass** |
| 3 | Enrollment decision **Enrolled** recorded (R7) |
| 4 | Discoverability category **discoverable** declared (R9) |
| 5 | Catalog binding doctrine attested — entry slot ≠ logical identity (R10) |
| 6 | Evidence classes R1–R8 **satisfied** for audit trail |
| 7 | Manifest entry anchor **referenced** on catalog doctrine (R3) |

### Operational state after completion (doctrinal, not files)

| Artefact role | State after completion |
|---------------|------------------------|
| **Factory Project** (logical) | Unchanged — exists since recognition |
| **Manifest** | Remains **manifest-enrolled** |
| **Registry doctrine** | **Catalog-discoverable** in Factory portfolio |
| **Catalog entry** | Doctrine: registry entry slot bound to logical identity + manifest pointer — **not** physical file |
| **Engine / Tracking** | **Unchanged** by enrollment alone — indexes evolve only via declarations |
| **Surface** | Unchanged — per-project after portfolio select |

### What completion does NOT imply

- Physical registry index or card template instance  
- `RG-*` PASS or state transition  
- Fully trackable / surface-ready  
- Queue position (RT-G06)  
- Implementation of RT-G05 / RT-G12  
- Deploy or client go-live  

### Workflow NOT complete outcomes

**Deferred**, **Rejected**, **Withdrawn** — workflow instance **closed** with outcome; **not** catalog-discoverable (except invalid mistaken enroll requiring correction record).

---

## Explicit Non-Claims

This playbook and Registry Catalog Enrollment Workflow v1:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** **automation**, **agent workflow**, n8n, or CI-driven catalog enrollment;
- **are not** **storage**, **database**, **file format**, **YAML**, **JSON**, **schemas**, tables, or folder standards;
- **are not** **implementation** of registry (RT-G05), manifest (RT-G10), or tracking storage (RT-G04);
- **are not** **registry implementation**, catalog index product, or discovery crawler;
- **are not** **registry UI**, **dashboard**, **CLI**, or operator display (RT-G12);
- **are not** **manifest implementation** or enrollment automation;
- **do not** redefine [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md), [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), Engine, or Runtime;
- **do not** define registry index card fields, JSON catalog, registry file paths, or tracking surface session checklist;
- **do not** claim physical Registry artefact exists in-repo.

Human-operated catalog enrollment remains the v1 operating reality.

---

## Open Questions

Bounded for **future operational artifacts** — not resolved in Playbook 02.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-RE01** | Minimum R1 evidence when Playbook 01 run was informal | **OPEN** — operator convention |
| **OQ-RE02** | Registry index card template fields (OQ-R02) | **OPEN** — separate task; must map RRDY-* categories |
| **OQ-RE03** | Default vs extended portfolio view for archived/withdrawn (OQ-R03) | **OPEN** — display charter |
| **OQ-RE04** | Duplicate detection playbook detail (OQ-R04) | **OPEN** — operational binding |
| **OQ-RE05** | PHASE_SLICE — one catalog entry per shell vs per slice (OQ-R05) | **OPEN** |
| **OQ-RE06** | Mandatory catalog enrollment for pilots vs external-only default | **SAFE UNKNOWN** per case |
| **OQ-RE07** | MIG incoming → catalog correlation category (OQ-R09, OQ-OM08) | **OPEN** — integration charter |
| **OQ-RE08** | Auto-sync orientation snapshot — display-only vs forbidden (OQ-R08) | **BOUNDED** — non-authoritative only |
| **OQ-RE09** | Physical registry creation moment relative to Enrolled | **OPEN** — implementation only |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **Registry Catalog Enrollment Workflow v1** as Operational Playbook 02 **complete** — use after Manifest Playbook 01 when portfolio visibility is needed.
2. **Operational Design continuation (separate tasks):**
   - Registry index card template (OQ-R02 / OQ-RE02 operational binding)
   - Tracking surface operator session workflow (OQ-OM04)
   - Registry withdrawal session checklist (optional micro-playbook)
3. **Per pilot:** Run Playbook 01 then 02 explicitly; record R7/R8 even if evidence is session REPORT — not Engine SoT.
4. **Do not start:** registry JSON standard, catalog database, storage charters, runtime, dashboard — unless explicitly authorized.
5. **Optional P3:** Reference Playbook 02 from [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) Operational Design row — operator action.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether operators already maintain ad-hoc Factory project lists | **UNKNOWN** — no canonical catalog artefact |
| Default catalog entry naming convention | **not standardized** in v1 |
| Calendar for RT-G05 physical registry | **not scheduled** |

---

*Factory Registry Catalog Enrollment Workflow v1 — Operational Playbook 02. Canonical location: `workspaces/website-factory-reference-v1/`. Git: no commit, no push.*

---

# REPORT — Factory Registry Enrollment Workflow v1

**Stage:** Operational Design — Operational Playbook 02 (Registry Catalog Enrollment Workflow)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md` (created)  
**Summary:** Определён операционный workflow зачисления manifest-enrolled Factory Project в Factory Registry: триггеры catalog need, оценка registry-ready (RRDY-*), модель решений и исходы (enrolled/deferred/rejected/withdrawn), принципы discoverability vs existence vs Tracking, классы operational evidence, withdrawal без удаления project reality, обработка incomplete/uncertain/legacy, критерии завершения — без runtime, automation, storage, schemas, registry implementation/UI.  
**Git:** no commit, no push (per task charter).
