# REPORT — Factory Manifest Enrollment Workflow v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Operational Design — **Operational Playbook 01** (Manifest Enrollment Workflow)  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 **COMPLETE**; Post-Engine Doctrine **COMPLETE**; [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) **COMPLETE**  
**Тип:** operational workflow only — **без** runtime, automation, implementation, storage, schemas, agents  
**Не переопределяет:** [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md), Engine Stages 1–6, Runtime Architecture  

---

## Purpose

### Зачем существует Manifest Enrollment Workflow

**Manifest Enrollment Workflow** — первый операционный playbook Website Factory. Он описывает **человеко-исполняемую** последовательность, по которой production case **входит** в Factory scope и достигает статуса **manifest-enrolled** (доктринально готов к роли Project Manifest как entry anchor).

Workflow закрывает координационную проблему **границы входа**:

| Проблема | Как workflow решает |
|----------|---------------------|
| Работа существует в workspace, MIG, brief или pilot — но неясно, это Factory Project или внешний шум | Явная **Factory-scoped recognition** до любой «официальной» Factory-работы |
| Оператор начинает tracking или ищет папку в git без charter и scope | **Manifest readiness evaluation** (MRDY-*) **до** трактовки case как orientable |
| Registry или filesystem подменяют intake | Enrollment **не** создаёт проект и **не** равен catalog enrollment |
| Ожидание physical manifest-файла блокирует старт | **Manifest-enrolled** = doctrinal outcome; файл — **implementation**, не условие workflow |

Оператор после прохождения workflow должен уметь ответить **без чтения всего workspace**:

- Что квалифицируется как Factory Project?
- Как intake становится Factory Project?
- Когда разрешено Manifest enrollment?
- Когда case **eligible** для Registry enrollment (отдельное решение)?
- Что блокирует enrollment?
- Какие **классы** evidence поддерживают решения?

### Что workflow **не** решает

| Вне scope | Почему |
|-----------|--------|
| Движение по Runtime chain, gate sign-off, state transitions | Engine + Runtime; human declarations **после** enrollment |
| Полная observability (seven/eight tracking questions) | Tracking composition + Surface — **после** manifest path |
| Catalog enrollment, portfolio discoverability | Registry charter — **отдельный** operator decision (class I) |
| Physical manifest serialization, paths, formats | RT-G10 **implementation** — NOT STARTED |
| Persistence, state store, registry index on disk | RT-G04, RT-G05 implementation |
| Automation, agents, n8n, CI discovery | Explicitly forbidden in v1 |
| Layer artefact production (SEO pack, blueprint body, etc.) | Foundation workstreams — **после** Factory-scoped track exists |

**Граница playbook:** от **сигнала production intent** до **manifest-enrolled** Factory Project. Registry enrollment — **следующий** optional operational binding, не завершение этого workflow.

```text
  PRE-FACTORY                    THIS WORKFLOW                 POST-ENROLLMENT (other playbooks)
  (idea, brief, raw repo)              │                              │
        │                              ▼                              ▼
        └──────────────▶  Recognition → Readiness → Decision  →  Tracking / Surface
                              (manifest-enrolled)              →  Registry (optional)
```

---

## Foundation Dependencies

Workflow **наследует** принятые артефакты **без их изменения**. При конфликте — побеждает более специфичный charter (Manifest, Registry), затем Operational Model.

### Tier 0 — Operational model

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | Вход в Factory (intake/recognition), decision classes A–B, manifest-ready (OR-03), operator path, human-only decisions |

### Tier 1 — Post-Engine doctrine (обязательные)

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | MRDY-* manifest-ready, manifest-incomplete, MA-*, MT-*, MR-01, entry anchor |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | RD-*, RRDY-*, RA-02, RM-01 — **eligibility only**, не шаги registry enrollment |
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Factory Project definition, identity shell, charter, minimum identity |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Intake occupancy `NEW_PROJECT`, Factory-scoped recognition moment |
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Operator path: Manifest precedes Surface; early intake may be manifest-ready but not surface-ready |

### Tier 2 — Engine context (reference)

Factory Engine Stages 1–6; Runtime Architecture v1 (`NEW_PROJECT`, `RG-INTAKE_COMPLETE`, HO-01). Workflow **не** переопределяет state codes или gates.

**Authority precedence:** Foundation + Engine + Manifest/Registry/Tracking Surface charters → **этот playbook** для операционных шагов enrollment → будущие playbooks (registry card, surface session) **не могут** нарушить MRDY-*, RD-02, RA-02, MT-01.

---

## Enrollment Trigger Principles

Enrollment workflow **стартует** не от технического события (commit, folder create, CI), а от **операционного сигнала production intent**, требующего решения: вести ли case в Website Factory.

### Классы триггеров (не исчерпывающий список)

| Trigger class | Typical signal | Operational note |
|---------------|----------------|------------------|
| **Client / commercial request** | Заказ сайта, контракт, SOW, бриф клиента | Sponsor = client or account owner; charter captures exclusions |
| **Internal initiative** | Внутренний продукт, маркетинговый лендинг, R&D site | Sponsor = internal charter author |
| **Pilot project** | MIG pilot, reference workspace pilot (e.g. lane A production case) | Pilot **может** быть Factory-scoped — требует явного recognition, не автоматически |
| **Migration / replatform** | Перенос существующего сайта в Factory discipline | Scope tier и endpoint часто partial — MRDY-03/04 критичны |
| **Incoming pipeline request** | MIG/incoming request, MetaBOT handoff, ORCA ref | Binding к Factory — **operator decision** (OQ-OM08 analog); trigger ≠ enrollment |

### Принципы триггера

| ID | Principle |
|----|-----------|
| **ET-01** | Один trigger может породить **ноль или один** Factory Project shell — не «авто-форк» на каждый файл |
| **ET-02** | Trigger **не** равен Manifest enrollment — между ними **recognition** и **readiness evaluation** |
| **ET-03** | Повторный trigger на тот же case (amendment, scope change) **не** перезапускает workflow с нуля, если identity shell уже manifest-enrolled — идёт **charter amendment path** (вне этого playbook) |
| **ET-04** | Raw workspace / git repo **без** production intent declaration остаётся **pre-Factory** (RD-04, RAP-10 analog) |

### Событие, открывающее workflow

**Workflow instance opens** when operator (или уполномоченный sponsor через operator) фиксирует: *«есть production case, требующий решения о Factory-scoped recognition»*.

Это **не** declaration state transition и **не** registry write — только **начало** операционной проверки по шагам ниже.

---

## Factory-Scoped Recognition

До Manifest enrollment case должен пройти **Factory-scoped recognition** — decision class **B** в Operational Model.

### Что qualifies as a Factory Project

Factory Project — **логическая** единица одного Website Factory production case ([FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md)), **не** репозиторий и **не** agent session.

**Квалификация (все обязательны для recognition):**

| # | Criterion | Source |
|---|-----------|--------|
| 1 | **Production intent** явен: выпуск статического сайта (Core 5 path или charter-bound exception) в рамках принятой Foundation chain | Operational Model; Object Model |
| 2 | **Operator accountability**: назначен Factory operator (или принят до назначения с explicit placeholder в charter category) | OA-ACT-01 |
| 3 | **Charter-bound scope**: есть или создаётся **project charter** category (цели, exclusions, stakeholder context) — содержание минимально на intake | MRDY-02; Object mandatory components |
| 4 | **Scope tier** category выбрана: `FULL_SITE`, partial, design-only, `PHASE_SLICE` — даже если default | MRDY-02, MRDY-04 |
| 5 | Case **не** является только methodology session, global layer doc work, или Site Type Registry maintenance | RD-01, RAP-11 |
| 6 | Case **не** сводится к post-Factory deploy/hosting без Factory track | Operational boundaries |

**Не квалифицируется** (остаётся external / pre-Factory):

- Идея без charter category и без operator ownership  
- «Папка в incoming/» без Factory-scoped declaration  
- MIG run, n8n workflow, Cursor chat без production case shell  
- Extended site type **без** charter acknowledging architecture gap (invalid track until charter — operator rejects or defers)

### Когда work становится eligible для consideration

| Stage | Status |
|-------|--------|
| Pre-Factory | Brief, repo, pilot folder — **кандидат**, не Factory Project |
| **Recognition declared** | Operator declares: *this is a Factory Project* — identity shell **логически** существует |
| Post-recognition | Mandatory components attach (empty indexes allowed at `NEW_PROJECT`) |

**Recognition moment** aligns с doctrine `NEW_PROJECT` intake: Factory Project **существует** в Engine model **до** physical manifest и **до** registry entry (RA-02, ES-03).

### Recognition vs Manifest enrollment

| Step | Outcome |
|------|---------|
| Factory-scoped recognition | Logical Factory Project + identity shell |
| Manifest readiness pass | MRDY-01…07 satisfied |
| Manifest enrollment decision | **manifest-enrolled** — entry anchor identified doctrinally |

Recognition **без** manifest-ready → **deferred** enrollment, не «половинный» enrolled state.

---

## Manifest Readiness Evaluation

Оценка **только** по [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) — **категории знания**, не файлы и не поля.

### Обязательные условия (MRDY-*)

Перед положительным enrollment decision operator подтверждает:

| # | Criterion | ID | Evaluation question (operational) |
|---|-----------|-----|----------------------------------|
| 1 | Stable project identity category **explicit** | **MRDY-01** | Есть ли устойчивая ссылка на этот production case в Factory scope (логический project identity)? |
| 2 | Charter & scope tier category **explicit** | **MRDY-02** | Зафиксированы ли intent, exclusions, scope tier (допустимо minimal charter)? |
| 3 | Declared lifecycle endpoint category **explicit** | **MRDY-03** | Заявлен ли endpoint: full chain → `COMPLETE` или partial с acknowledged ambiguity **отсутствует**? |
| 4 | Scope applicability doctrine **explicit** | **MRDY-04** | Понятен ли full chain vs partial с EXCLUDED states? |
| 5 | Authoritative reference topology **declared** | **MRDY-05** | Знает ли operator, где истины: state instance, gates, artefacts, Runtime rules (карта ссылок, не копии тел)? |
| 6 | Manifest entry anchor **identified** | **MRDY-06** | Указана ли доктринальная точка входа для этого case (не обязательно physical file)? |
| 7 | Operator understands Manifest ≠ Passport ≠ Registry **and** ATLAS homonyms (TG-ATLAS-*) | **MRDY-07** | Нет ли планов дублировать Tracking или Registry ролями Manifest? Различает ли оператор Factory Project/Registry/Identity и ATLAS Project/Registry/Identity? |

### ATLAS-first enrollment (before org-identifying scope content)

Per [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md) RC-05 — **before** populating charter scope categories (MOC-03 analog) with org-identifying facts (`legal_name`, `inn`, client org name as identity):

| # | Step | Outcome |
|---|------|---------|
| 1 | Check ATLAS population / steward for active `ORG-*`, `WEB-*`, `PRJ-*` for this case | Known ids identified or **SAFE UNKNOWN** recorded |
| 2 | If active canonical exists | Bind refs in external topology (`atlas_client_org_ref`, `atlas_website_ref`, `atlas_project_ref`, etc.) — **reference first, copy second** |
| 3 | If unknown or disputed | **SAFE UNKNOWN** — **MUST NOT** invent OWNER/ORG or parallel registry row (IGV 9.3, CC-02) |
| 4 | Legal Entity Card (if needed) | Follow RC-02 crosswalk — production input, not registry entry; cite `atlas_org_ref` when attested |

**Normative rule ENROLL-ATLAS-01:** When organization already exists in ATLAS, new business facts **never** become primary inside Factory. MOC-03 / charter scope carries **production scope**, not canonical identity restatement.

**Ordering:** ATLAS-first check **precedes** physical bind (MOC-03 population) and **precedes** Legal Entity Card field population from discovery when ATLAS canonical is known.

### Manifest-incomplete signals (блокируют enrolled)

| Condition | Action in workflow |
|-----------|-------------------|
| No stable identity | **Reject** or remain pre-Factory |
| Charter / scope tier absent | **Defer** until category explicit |
| Endpoint unstated | **Defer** — implicit ambiguity fails MRDY-03 |
| Topology undeclared | **Defer** — operator cannot orient (MRDY-05) |
| Manifest conflated with live Tracking index | **Defer** — integrity remediation (MAP-05) |
| Active state in orientation contradicts Engine without reconciliation | **Defer** — MS-02 |

### Важные соотношения (не блокеры enrollment при норме)

| Concept | Relation to enrollment |
|---------|------------------------|
| **Manifest-ready ⊄ fully trackable** | Early `NEW_PROJECT` — нормально enroll с пустыми gate indexes |
| **Manifest-ready ⊄ gate-complete** | Mid-chain позже — не требование enrollment |
| **Physical manifest artefact** | **Не** требуется для MRDY-06 в v1 |

### Evaluation ownership

**Factory operator** выполняет checklist MRDY-*; **reviewer** может audit, но **не** заменяет operator attestation enrollment (OA-ACT-02).

---

## Enrollment Decision Model

### Кто принимает решения

| Decision | Owner (v1) | Human-only |
|----------|------------|------------|
| Open workflow on trigger | Factory operator | **Yes** |
| Factory-scoped recognition (B) | Factory operator | **Yes** |
| MRDY-* attestation | Factory operator | **Yes** |
| Enrollment outcome (enrolled / deferred / rejected / withdrawn) | Factory operator | **Yes** |
| Charter content | Operator + sponsor input | **Yes** — sponsor не объявляет state/gates |
| Registry catalog enrollment | Factory operator | **Yes** — **отдельное** решение после этого workflow |

### Что остаётся человеческим навсегда в v1

- Признание Factory-scoped production case  
- Оценка manifest-ready и запись outcome  
- Идентификация manifest entry anchor (doctrinal)  
- Отклонение, отложение, отзыв до завершения Factory track  
- Любая попытка «enrollment by discovery» (git scan, agent auto-index)

### Что **никогда** не может быть автоматическим

| Forbidden automation | Principle |
|---------------------|-----------|
| Auto-enroll on folder create / incoming path | RD-04, RAP-10 |
| Auto-pass MRDY-* from template fill without operator attestation | MAP-12 analog |
| Agent-declared manifest-enrolled without operator record | OA-ACT-04 |
| CI / webhook as enrollment authority | Not Factory product in Phase 1 |
| Registry write as side-effect of recognition | RA-02, RD-04 |

Future tooling **may assist** checklists; **ownership** enrollment decision остаётся у operator (Operational Model — optional automation не меняет ownership).

### Decision record (logical, not format)

Каждое решение enrollment порождает **declaration category**:

- Outcome code (enrolled / deferred / rejected / withdrawn)  
- Operator identity (role class)  
- Timestamp (logical)  
- MRDY checklist result summary  
- Reference to evidence classes used (см. ниже)  
- If deferred: explicit gap list mapped to MRDY-*  
- If rejected: reason category (out of scope, wrong system, duplicate identity, etc.)

**Append-only:** исправление = новая declaration, не silent overwrite (AT-01 analog).

---

## Enrollment Outcomes

### Primary outcomes

| Outcome | Meaning | Factory Project state |
|---------|---------|------------------------|
| **Enrolled** | Manifest enrollment workflow **complete**; manifest-ready attested; entry anchor identified | Logical Factory Project **manifest-enrolled**; typically active doctrine `NEW_PROJECT` or first applicable state; **eligible** for Registry consideration (not auto-enrolled) |
| **Deferred** | Recognition может быть частичной; MRDY gaps **явные**; дозаполнение charter/topology/endpoint | Case **не** manifest-enrolled; остаётся в «pending enrollment» operational bucket |
| **Rejected** | Case **не** будет Factory Project (out of scope, duplicate, wrong factory, insufficient commitment) | Pre-Factory or closed candidate — **no** identity shell для Factory |
| **Withdrawn** | Sponsor или operator **закрывает** инициативу до завершения enrollment | Не enrolled; trigger может повториться позже как **новый** workflow instance |

### Дополнительное различие (не отдельный outcome code)

| Situation | Treatment |
|-----------|-----------|
| **Recognized but enrollment deferred** | Factory-scoped recognition уже объявлен, MRDY fail → outcome **Deferred** (не путать с pre-Factory) |
| **Enrolled without Registry** | **Норма** — Registry optional (decision class I) |

Дополнительный outcome **«superseded»** не нужен на уровне enrollment: повторный enrollment на ту же identity после enrolled — **amendment**, не второй workflow v1.

### Outcome → operator next step

| Outcome | Next step (operational) |
|---------|-------------------------|
| **Enrolled** | Per-project path: Manifest anchor → Tracking composition when indexes exist → Surface when trackable; **optional** Registry enrollment playbook |
| **Deferred** | Закрыть gaps; re-run readiness; не начинать gate sign-off как substitute |
| **Rejected** | Документировать rejection; не создавать Registry pointer |
| **Withdrawn** | Archive trigger evidence; не оставлять «phantom» catalog entries |

---

## Registry Eligibility Principles

Registry enrollment — **не** часть завершения Manifest Enrollment Workflow. Этот раздел фиксирует **когда case становится eligible** для **отдельного** operator decision по Registry charter.

### Preconditions (все должны выполняться)

| # | Requirement | Source |
|---|-------------|--------|
| 1 | Factory-scoped logical project **exists** | RA-02, Object Model |
| 2 | **Manifest-enrolled** = manifest-ready (MRDY-*) + entry anchor identified | This workflow outcome **Enrolled** |
| 3 | **Registry-ready** (RRDY-01…06): distinction summaries, discoverability category explicit, RA-03 understood | Registry Charter |
| 4 | Operator **declares** catalog enrollment — human-operated | RD-04 |
| 5 | Manifest entry pointer **identified** for catalog card | RM-01, RD-02 |

### Ordering (normative)

```text
  Trigger → Recognition → Manifest Enrollment (this workflow) → [optional] Registry Enrollment
                                      │                                    │
                                      └ manifest-enrolled                  └ discoverable in portfolio
```

### Explicit blocks on Registry (even if manifest-enrolled)

| Block | Principle |
|-------|-----------|
| Manifest-incomplete | RD-02 — no catalog before orientability |
| Operator has not declared catalog enrollment | RD-04 |
| Registry entry ID conflated with project identity | RRDY-03 / RAP-09 |
| Discoverability attempted before Manifest anchor | RAP-16 |
| Case never Factory-scoped | RRDY-01 fail |

### Discoverable vs manifest-enrolled

| State | Meaning |
|-------|---------|
| **Manifest-enrolled** | Per-project entry doctrine satisfied — **этот workflow** |
| **Discoverable** | In Factory portfolio catalog per Registry — **другой** workflow / decision |

Проект может быть **manifest-enrolled** месяцами **без** Registry — валидная v1 практика (Operational Model OR-03, decision I optional).

---

## Operational Evidence Principles

Поддержка enrollment decisions — **классы evidence**, не хранилища и не шаблоны.

### Evidence classes (required categories)

| Class | Supports | Typical content (category, not format) |
|-------|----------|----------------------------------------|
| **E1 — Production intent** | Trigger, recognition | Client brief, SOW excerpt, internal initiative memo, pilot charter ref |
| **E2 — Charter & scope** | MRDY-02, MRDY-04, recognition | Scope tier declaration, exclusions list, stakeholder attribution |
| **E3 — Lifecycle endpoint & applicability** | MRDY-03, MRDY-04 | Declared endpoint (full / partial), acknowledged EXCLUDED states |
| **E4 — Identity & distinction** | MRDY-01, deduplication | Logical project identity rationale; why not duplicate of existing case |
| **E5 — Reference topology acknowledgment** | MRDY-05 | Operator attestation where state/gate/artefact/runtime truths live |
| **E6 — Manifest role integrity** | MRDY-07 | Acknowledgment Manifest ≠ Tracking ≠ Registry ≠ Passport; ATLAS homonym guards (TG-ATLAS-*) |
| **E7 — Enrollment decision record** | Outcome | Enrolled / deferred / rejected / withdrawn + operator + logical time |
| **E8 — Readiness evaluation record** | MRDY pass/fail | Per-criterion pass/fail with gap notes |
| **E9 — Sponsor / client attribution** | Accountability | Who authorized production intent (external to Factory state) |
| **E10 — Amendment / supersession** (if re-evaluation) | Audit | Pointer to prior enrollment declaration being corrected |
| **E11 — ATLAS reference check** (when applicable) | ENROLL-ATLAS-01 | Record of ATLAS id lookup or SAFE UNKNOWN before org-identifying scope content |

### Evidence principles

| ID | Principle |
|----|-----------|
| **EP-01** | Evidence **подтверждает категории**, не заменяет Engine indexes |
| **EP-02** | Отсутствие E1 при recognition → **defer** или **reject**, не «enroll by assumption» |
| **EP-03** | Git history, screenshots, SERP captures — **допустимы** как E1/E2 attachments, **не** как auto-enrollment |
| **EP-04** | Evidence for Registry (portfolio summaries) **может** reuse E2/E3 summaries — **не** authoritative copy of Manifest (RM-02) |

### What evidence is NOT

- Not layer artefact bodies (Legal Pack, blueprint file)  
- Not gate PASS records  
- Not physical manifest/registry file existence  
- Not automated validator output as sole authority  

---

## Failure And Exception Handling

### Incomplete projects

| Situation | Treatment |
|-----------|-----------|
| Partial charter (intent only) | **Deferred** — list MRDY-02/03/04 gaps |
| Identity proposed but unstable | **Deferred** or **Reject** if duplicate / ambiguous |
| Topology «TBD» | **Deferred** — MRDY-05 fail |
| Recognition without operator | **Defer** — assign Factory operator first |

**Запрещено:** silent **Enrolled** с открытыми MRDY fails; «временный» Passport/Manifest-dump как обход (MAP-06).

### Uncertain projects

| Situation | Treatment |
|-----------|-----------|
| Scope unclear (full vs partial) | **Deferred** — explicit endpoint workshop |
| Site class unknown | **Deferred** — classification binding not required at enrollment, но scope/applicability must be explicit |
| External system ownership disputed | **Deferred** — charter amendment or **Reject** |
| Pilot may be external-only (OQ-OM07) | **SAFE UNKNOWN** until case charter reviewed — default **Defer**, not Enroll |

Uncertainty → **Defer** с documented gaps, не **Enrolled** «на потом исправим» без attestation.

### Abandoned initiatives

| Situation | Treatment |
|-----------|-----------|
| Sponsor cancels before enrollment complete | Outcome **Withdrawn** |
| Deferred too long, no progress | Operator **Withdrawn** or **Reject** (explicit); не оставлять вечный Deferred |
| Recognized then abandoned | **Withdrawn**; Engine history may exist — catalog **не** enroll без reversal declaration |

Withdrawn **≠** Rejected: withdrawn may return with new trigger; rejected = decision not to Factory-scope.

### Integrity violations during workflow

| Violation | Response |
|-----------|----------|
| Manifest used as live gate index | Stop — remediate MAP-05 — **Defer** |
| Folder discovery treated as enrollment | Stop — RAP-10 — **Reject** or restart with recognition |
| Registry enrollment before manifest-enrolled | Roll back catalog declaration — RAP-16 |

### Exception: duplicate production case

Operator discovers duplicate identity → **Reject** new shell or merge via explicit declaration (OQ-R04 — operational detail OPEN); **не** второй Enrolled без reconciliation record.

---

## Workflow Completion

### When Manifest Enrollment Workflow is complete

Workflow считается **завершённым** только при outcome **Enrolled** и выполнении:

| # | Completion criterion |
|---|---------------------|
| 1 | Factory-scoped recognition **declared** |
| 2 | MRDY-01…07 **attested pass** |
| 3 | Enrollment decision **Enrolled** recorded (E7) |
| 4 | Manifest entry anchor **identified** doctrinally (MRDY-06) |
| 5 | Evidence classes E1–E8 **satisfied** for audit trail |
| 6 | Operator **не** считает case pre-Factory |

### Artifact state after completion (doctrinal, not files)

| Artefact role | State after completion |
|---------------|------------------------|
| **Factory Project** (logical) | Exists with identity shell + charter + scope tier |
| **Manifest doctrine** | **manifest-enrolled** — orientable per Manifest Charter |
| **Manifest entry anchor** | Identified — operator path «start here» defined |
| **Engine state instance** | Doctrine: typically **`NEW_PROJECT`** intake (или первый applicable state per partial mask — must be **declared**, not assumed) |
| **Tracking indexes** | May be **empty** — valid at intake |
| **Registry** | **Unchanged** unless separate enrollment decision |
| **Surface** | May be **not** surface-ready — valid |

### What completion does NOT imply

- Registry discoverability  
- Physical manifest file  
- `RG-INTAKE_COMPLETE` or any gate PASS  
- Fully trackable / surface-ready  
- Layer artefact production started  

### Workflow NOT complete outcomes

**Deferred**, **Rejected**, **Withdrawn** — workflow instance **closed** с соответствующим outcome, но **не** manifest-enrolled (кроме edge Recognized+Deferred, где recognition может уже существовать).

---

## Explicit Non-Claims

This playbook and Manifest Enrollment Workflow v1:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** **automation**, **agent workflow**, n8n, or CI-driven enrollment;
- **are not** **storage**, **database**, **file format**, **YAML**, **JSON**, **schemas**, or folder standards;
- **are not** **implementation** of manifest (RT-G10), registry (RT-G05), or tracking storage (RT-G04);
- **are not** **registry implementation** or catalog index product;
- **are not** **manifest implementation** or serialization standard;
- **are not** **UI**, **dashboard**, **CLI**, or operator display (RT-G12);
- **do not** redefine [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md), Engine, or Runtime;
- **do not** define manifest file standard, registry card template, or tracking surface session checklist;
- **do not** claim physical manifest or registry artefacts exist in-repo.

Human-operated enrollment remains the v1 operating reality.

---

## Open Questions

Bounded for **future operational playbooks** — not resolved in Playbook 01.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-ME01** | Minimum E1 evidence for pilot vs commercial client | **OPEN** — operator convention |
| **OQ-ME02** | Whether Recognized+Deferred gets partial identity shell in all operators' practice | **OPEN** — aligns OQ-OM02 |
| **OQ-ME03** | MIG incoming → standard trigger binding (ET / OQ-OM08) | **OPEN** — integration charter |
| **OQ-ME04** | PHASE_SLICE: one enrollment per shell vs per slice | **OPEN** — OQ-M03, OQ-R05 |
| **OQ-ME05** | Physical manifest creation moment relative to Enrolled | **OPEN** — implementation charter only |
| **OQ-ME06** | Triumph / pilot workspaces: mandatory Enrolled vs external-only default | **SAFE UNKNOWN** per case |
| **OQ-ME07** | Dual corpus routing (`mars-website-factory` v0 vs reference v1) at enrollment | **OPEN** — OQ-OM06 |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **Manifest Enrollment Workflow v1** as Operational Playbook 01 **complete** — use for intake sessions before Tracking depth or Registry.
2. **Operational Design continuation (separate tasks):**
   - Registry catalog enrollment playbook (optional decision I operational binding)
   - Registry index card template (OQ-R02)
   - Tracking surface operator session workflow (OQ-OM04)
3. **Per pilot:** Run workflow explicitly; record E7/E8 even if evidence is session REPORT — not Engine SoT.
4. **Do not start:** manifest JSON standard, registry index implementation, storage charters, runtime — unless explicitly authorized.
5. **Optional P3:** Reference Playbook 01 from [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) Operational Design row — operator action.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether operators already run ad-hoc enrollment discipline | **UNKNOWN** — no canonical physical artefact |
| Default identity naming convention across pilots | **not standardized** in v1 |
| Calendar for RT-G10 physical manifest | **not scheduled** |

---

*Factory Manifest Enrollment Workflow v1 — Operational Playbook 01. Canonical location: `workspaces/website-factory-reference-v1/`. Git: no commit, no push.*

---

# REPORT — Factory Manifest Enrollment Workflow v1

**Stage:** Operational Design — Operational Playbook 01 (Manifest Enrollment Workflow)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md` (created)  
**Summary:** Определён операционный workflow входа production case в Website Factory: триггеры intent, Factory-scoped recognition, оценка manifest-ready (MRDY-*), модель решений и исходы (enrolled/deferred/rejected/withdrawn), принципы Registry eligibility после enrollment, классы operational evidence, обработка incomplete/uncertain/abandoned, критерии завершения workflow — без runtime, automation, storage, schemas, manifest/registry implementation.  
**Git:** no commit, no push (per task charter).
