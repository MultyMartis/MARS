# REPORT — Factory Project Registry Charter v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Post–Factory Engine Architecture v1 — **RT-G05 charter only**  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 Stages 1–6 **COMPLETE**; [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) (RT-G10) **COMPLETE**  
**Тип:** charter only — **без** implementation, runtime, storage format, schemas, field lists, files, UI, indexes, discovery implementation  
**Связь:** [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) ES-03, EO-05, [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) MR-01…MR-02, [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G05

---

## Purpose

### Зачем существует Factory Project Registry

**Factory Project Registry** — архитектурная **доктрина мультипроектного указателя** Website Factory. Registry отвечает на вопросы, которые **один** Engine v1 и **один** Manifest **не могут** закрыть без обхода каждого production workspace:

| Вопрос оператора | Роль Registry |
|------------------|---------------|
| **Какие Factory projects существуют?** | Доктрина **перечисления** Factory-scoped production cases в Factory scope |
| **Как проекты обнаруживаются?** | Доктрина **discoverability** — когда case входит в Factory index и когда выходит |
| **Как проекты идентифицируются?** | Доктрина **stable logical identity** vs **registry entry** — без подмены Engine identity shell |
| **Как проекты различаются?** | Доктрина **distinction** — charter-level и scope-level различия **категориями**, не полным tracking |
| **Где точка входа в конкретный проект?** | Registry **указывает** на Manifest entry anchor — **не** заменяет Manifest |

Registry решает **координационную проблему мультипроектной ориентации**: при распределённой authority (Engine per-project, Manifest per-project, layers T1) оператору, ведущему **несколько** production cases, нужен **единый Factory-scoped каталог**, который **не дублирует** tracking, state, gates или layer bodies.

### Что Registry **не** решает

| Проблема | Куда относится |
|----------|----------------|
| «Что это за **один** проект?» (minimum understanding) | [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) |
| «Где проект **сейчас**? Что прошло? Что блокирует?» | [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) + Engine Stages 1–5 |
| Как проект **движется** по chain | Runtime + [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) |
| Как gates **авторизуют** переходы | [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) |
| Как lifecycle **складывается** в нарратив | [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) |
| Где **физически** хранятся записи | **FUTURE** RT-G04 storage |
| Приоритет очереди, scheduling | **FUTURE** RT-G06 queue |
| Канонические `site_type_code`, matrices | Foundation **Site Type Registry** (`registry/`) — **другой** Registry |
| Исполнение, automation, agents | External / RT-G01, RT-G03, RT-G11 |

**Registry — charter (конституция роли), не продукт, не индекс-файл и не база данных.**

### Именование: Factory Project Registry vs Site Type Registry

| Term | Scope | This charter |
|------|-------|--------------|
| **Site Type Registry** | Foundation layer — class-level `site_type_code`, matrices | **Out of scope** — T1 authority |
| **Factory Project Registry** | Post-Engine — multi-project Factory production cases | **In scope** — RT-G05 |

Путаница между ними — **архитектурное нарушение** (см. Anti-Patterns).

---

## Foundation Dependencies

Registry Charter **наследует** завершённый Engine v1 и Manifest doctrine; **не изменяет** Foundation, Runtime или Engine Stages 1–6.

### Tier 1 — Engine + Manifest (обязательные)

| Document | Registry использует |
|----------|---------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Factory Project, identity shell, minimum identity dimensions, OQ-12 logical project vs registry entry |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Граница: Registry **не** tracking; seven questions — per-project only |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Entry anchor, MR-01…MR-02, manifest-ready categories Registry **may reference** |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-03, EO-05, BV-14, external RT-G05 placement |

### Tier 2 — Engine composition context

| Document | Role |
|----------|------|
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Active state — **orientation summary** category only in index card doctrine |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | Declared endpoint — distinction category; Registry **не** владеет progression |
| [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) | T5 global layer status — **не** per-project registry content |

### Tier 3 — Runtime + Foundation (reference only)

Runtime Architecture v1; принятая 14-layer Foundation chain. Registry **не** переопределяет layer contracts или `registry/SITE-TYPE-REGISTRY-v1.md`.

**Authority precedence:** Foundation Freeze + Engine Readiness Audit → Engine Stages 1–6 → Manifest Charter (RT-G10) → **этот charter** для роли Registry → **будущий** implementation/index standard (если авторизован) **не может** нарушить ES-03, MR-01, EO-05.

---

## Registry Position In Factory

```text
                    ┌─────────────────────────────────────┐
                    │   FACTORY PROJECT REGISTRY (charter)   │
                    │   multi-project catalog doctrine       │
                    │   discoverability · distinction        │
                    └─────────────────────────────────────┘
                          │ lists / points          │ never executes
                          ▼                         ▼
        ┌──────────────────────────┐    ┌──────────────────────────┐
        │  PER-PROJECT MANIFEST     │    │  PER-PROJECT ENGINE v1    │
        │  entry anchor (1 case)    │    │  Object·State·Tracking…   │
        └──────────────────────────┘    └──────────────────────────┘
                          │                         │
                          └──────── one logical ────┘
                                    Factory Project
```

### Позиция относительно Engine planes

| Plane | Registry relationship |
|-------|-------------------------|
| **Project Object** | Registry **индексирует существование** Factory-scoped logical project — **не** заменяет Object Model |
| **State** | Registry **may surface** orientation summary (category) — **не** владеет state instance |
| **Tracking** | Registry **указывает** на tracking/Manifest entry — **не** дублирует composition |
| **Gate / Lifecycle** | Registry **не** хранит gate index или segment progression |
| **Engine boundary** | Engine scope = **one** project (EO-05); Registry = **many** projects — **explicitly external** to Engine v1 |

### Позиция в эре Website Factory

| Эра | Status | Registry |
|-----|--------|----------|
| Foundation Era | **COMPLETE** | Registry **не** заменяет Site Type Registry |
| Factory Engine Architecture v1 | **COMPLETE** | Registry **дополняет** Engine — post-Stage 6, multi-project |
| RT-G10 Manifest Charter | **COMPLETE** (doctrine) | Registry **depends on** Manifest anchor per project |
| RT-G05 implementation | **NOT STARTED** | Этот документ — **только** charter роли |

### Operator path (multi-project)

```text
  OPERATOR (portfolio view)
       │
       ▼
  ┌─────────────┐     «What Factory projects exist? Which is which?»
  │  REGISTRY   │     catalog · discoverability · distinction
  │  (charter)  │     points to Manifest entry per case
  └──────┬──────┘
         │ select one project
         ▼
  ┌─────────────┐     «What is this? Where do I start?»
  │  MANIFEST   │     minimum understanding · entry anchor
  └──────┬──────┘
         │ deep read
         ▼
  ┌─────────────┐     «Where now? What passed? What blocks?»
  │  TRACKING   │     full observability (Engine)
  └─────────────┘
```

---

## Registry Authority Principles

### Authority Registry **имеет**

| Authority class | Statement |
|-----------------|-----------|
| **Catalog doctrine** | Определяет, что считается **зарегистрированным** Factory Project в Factory-scoped каталоге |
| **Discoverability contract** | Определяет, когда production case **входит** в discoverable set и когда **выходит** — без формата хранения |
| **Identity distinction doctrine** | Разделяет **logical Factory Project identity** (Engine) и **registry entry** (index slot) — ES-03 |
| **Index card category ownership** | Какие **категории** знания допустимы на уровне каталога (summary), не на уровне Manifest/Tracking |
| **Distinction principles** | Как оператор **различает** проекты в списке без чтения полного workspace |
| **Entry lifecycle doctrine** | Registered / discoverable / withdrawn / archived — **категории статуса каталога**, не Runtime states |
| **Pointer authority to Manifest** | Registry **объявляет**, что canonical per-project entry — Manifest doctrine anchor |

### Authority Registry **не имеет**

| Non-authority | Actual owner |
|---------------|--------------|
| Factory Project **logical identity** definition | Engine Object Model — identity shell |
| Per-project **minimum understanding** contract | Manifest Charter |
| Active state, gate/handoff indexes, artefact bodies | Engine Tracking (T4) |
| State/gate/handoff **vocabulary** | Runtime Architecture v1 |
| Layer semantics, `site_type_code` **definitions** | Foundation Site Type Registry (T1) |
| Global ACCEPTED/FROZEN layer status | NEXT-PRIORITIES (T5) |
| Queue rank, prioritization | RT-G06 |
| Physical persistence, serialization | RT-G04, future implementation charters |
| Automated discovery crawlers, agents | External — **not** Registry v1 |

### Principle RA-01 — Registry is catalog, not case file

Registry **перечисляет и различает** Factory Projects. Registry **не становится** dossier, заменяющим Manifest + Tracking для одного case.

### Principle RA-02 — Logical project precedes registry entry

Factory Project **существует** в Engine model при Factory-scoped recognition **до** любой registry index slot. Registry entry **добавляет** discoverability в portfolio view — **не создаёт** проект.

### Principle RA-03 — Registry entry ID ≠ Factory Project identity

**ES-03:** registry entry identifier — **index slot**; stable logical identity — **Engine identity shell**. Слияние или подмена — **forbidden**.

### Principle RA-04 — Registry follows Manifest, not vice versa

Per-project Manifest entry anchor **обязателен** для registry discoverability doctrine (MR-01). Manifest Charter **не зависит** от Registry.

### Principle RA-05 — Registry ≠ Tracking at scale

Registry **запрещает** копирование live gate/handoff/state composition в каталог. Portfolio view **ссылается** на Tracking — **не** дублирует seven questions.

---

## Registry Scope Principles

Scope Registry — **категории мультипроектного знания** и **владение категорией**. **Не** field lists, **не** schemas, **не** tables.

### Category 1 — Catalog membership

| Aspect | Ownership |
|--------|-----------|
| Принадлежность production case к Factory Project catalog | Registry **doctrine**; Factory-scoped recognition — Engine/Object |
| Distinction registered vs never registered | Registry entry lifecycle category |

### Category 2 — Stable logical identity reference

| Aspect | Ownership |
|--------|-----------|
| Pointer to Engine identity shell (logical `project_id` doctrine) | Engine owns semantics; Registry **indexes reference** |
| Binding registry entry ↔ logical identity | Registry **doctrine** once entry exists — **not** redefinition of identity |

### Category 3 — Manifest entry pointer

| Aspect | Ownership |
|--------|-----------|
| Where operator starts for **this** case | Manifest Charter — entry anchor |
| Registry holds **pointer category** «manifest entry» | Registry **не** владеет Manifest categories content |

### Category 4 — Distinction summaries (portfolio-safe)

| Aspect | Ownership |
|--------|-----------|
| Charter intent **summary** (human-readable label category) | Derived from operator-authored charter — **summary only** |
| Scope tier summary (`FULL_SITE`, partial, PHASE_SLICE) | Manifest Category 2 — Registry **may echo summary** |
| Declared lifecycle endpoint summary | Manifest Category 3 — for portfolio distinction |
| Site classification summary (`site_type_code` when present) | Classification binding — **label category**, not Registry matrix authority |

### Category 5 — Orientation snapshot (non-authoritative)

| Aspect | Ownership |
|--------|-----------|
| Active `runtime_state_code` as **portfolio glance** | State instance — Engine; Registry **may show stale-risk summary** with freshness doctrine |
| Factory track open / suspended / closed partial | Logical metadata flags — Engine Stage 5; Registry **category only** |
| **Must** reconcile with Engine or flag invalid | RA-05 — not independent SoT |

### Category 6 — Discoverability status

| Aspect | Ownership |
|--------|-----------|
| Discoverable / hidden / withdrawn / archived | Registry **catalog lifecycle** — **not** Runtime state |
| Operator visibility in Factory portfolio | Registry doctrine |

### Category 7 — External workspace pointer (optional)

| Aspect | Ownership |
|--------|-----------|
| Charter-declared external ref (ERA-W03) | Operational — Registry **may index category** «external pointer» |
| Not canonical layer authority | ER-06 — pointer only |

### Categories **explicitly outside** Registry scope

| Excluded category | Why |
|-------------------|-----|
| Gate outcome index, handoff event bodies | Tracking — MAP/MT analog at multi-project scale |
| State history, progression ledger | State Model / Tracking |
| Artefact reference exhaust | Tracking AV-* |
| Manifest reference topology map (full) | Manifest Category 7 — per-project depth |
| Layer contract bodies, Legal Pack text | Foundation T1 |
| Site type matrices, `block_id` definitions | Site Type Registry / Block Registry |
| Queue position, priority rank | RT-G06 |
| MIG sessions, agent transcripts | External unless charter-bound ref category |
| Implementation paths, git trees, deploy status | Post-Factory / external |

**Registry owns the catalog of pointers — not the territories of each project.**

---

## Relationship To Manifest

### Why Registry depends on Manifest

| Reason | Statement |
|--------|-----------|
| **Entry anchor** | MR-01: multi-project index needs **stable per-project entry pointer** — Manifest doctrine defines it |
| **Minimum understanding gate** | Registry discoverability **should not** precede manifest-ready threshold for orientable catalog (see Registry Readiness) |
| **Non-duplication** | Manifest holds minimum understanding categories; Registry holds **portfolio summaries** — not second Manifest |
| **Authority direction** | Logical Factory Project → Manifest anchor → Registry index card **points to both** |

### Why Manifest does not depend on Registry

| Reason | Statement |
|--------|-----------|
| **Precedence** | Object Model: logical project at intake **before** registry (OQ-12, ES-03) |
| **Single-project work** | Operator may run one Factory Project with Manifest doctrine **without** portfolio catalog |
| **MR-02** | Manifest **не** является центральным реестром |

### Authority direction (normative)

```text
  Engine logical Factory Project  ──exists first──▶  (identity shell)
           │
           ▼
  Manifest entry anchor doctrine  ──orients one case──▶  (minimum understanding)
           │
           ▼
  Registry catalog entry          ──lists many cases──▶  (discoverability only)
```

### What Registry knows that Manifest does not (at portfolio level)

| Registry scope | Manifest exclusion |
|----------------|-------------------|
| Coexistence of **multiple** Factory Projects | Manifest is **per-project** only |
| Catalog membership and discoverability lifecycle | Manifest has no «list all projects» role |
| Cross-project distinction in one view | Manifest does not compare cases |

### What Manifest knows that Registry does not

| Manifest scope | Registry exclusion |
|----------------|-------------------|
| Full minimum understanding contract for **one** case | Registry index card = **summary categories** |
| Authoritative reference topology (state/gate/artefact map) | Registry **points** — does not charter topology |
| Scope & endpoint doctrine in operational depth | Registry may hold **summary** only |

### Principles

| ID | Principle |
|----|-----------|
| **RM-01** | Registry **must** reference Manifest entry anchor for each discoverable entry |
| **RM-02** | Manifest content categories **must not** be merged into Registry as authoritative copy |
| **RM-03** | Amending charter/scope **starts** in Manifest/Engine declaration trail — Registry summary **follows**, does not lead |

---

## Relationship To Engine

### What Engine exposes to Registry

| Engine exposure | Registry use |
|-----------------|--------------|
| Existence of Factory-scoped logical project | Catalog membership eligibility |
| Identity shell stability reference | Distinction + deduplication doctrine |
| Factory-scoped recognition moment (`NEW_PROJECT` doctrine) | Discoverability **candidate** signal — not automatic registry write |
| Tracking-derived **orientation** (via operator declaration chain) | Non-authoritative portfolio snapshot category |
| Terminal / partial closure metadata categories | Catalog status distinction — not deploy go-live |

### What Registry never owns from Engine

| Engine-owned domain | Registry prohibition |
|---------------------|----------------------|
| State instance + history | RA-05; not portfolio SoT for «where now» |
| Gate outcome index + validity (ACTIVE/STALE/INVALID) | No gate catalog |
| Handoff event index | No handoff catalog |
| Lifecycle composition narrative | No segment progression in registry |
| Tracking audit trail bodies | AT-01 scope stays per-project Tracking |
| Composition rules Stages 1–5 | Engine **defines** per-project semantics — Registry **does not extend** |

### Engine boundary alignment

| Boundary rule | Source | Registry compliance |
|---------------|--------|---------------------|
| One Engine model per project | EO-05 | One catalog entry **per** logical project — not one Engine for all |
| Registry external to Engine v1 | ES-03, External Systems table | Registry charter **confirms** external placement |
| Human-operated declaration | Runtime §7 | Registry reflects **declared** catalog membership — no autonomous enrollment |

### Principle RE-01 — Engine depth stays per-project

Operator answering seven Tracking questions **never** uses Registry as primary surface — only Manifest → Tracking path.

### Principle RE-02 — Registry does not extend Engine stages

No «Stage 7 Multi-Project Engine». Registry is **implementation-plane catalog charter**, not Engine architecture stage.

---

## Discovery Principles

Без определения crawlers, files, APIs или automation.

### Becoming discoverable

A Factory Project **becomes discoverable** in Registry doctrine when **all** hold:

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | Recognized **Factory-scoped** (identity shell exists) | Not a raw workspace folder |
| 2 | **Manifest-ready** per Manifest Charter (MRDY-01…07) | Catalog must not list unorientable cases |
| 3 | **Registry-ready** (RRDY-01…05 below) | Catalog integrity |
| 4 | Operator **declares** catalog enrollment (human-operated v1) | No silent auto-index from git scan |
| 5 | Manifest entry anchor **identified** for the case | RM-01 |

**Discoverable ≠ fully trackable:** early `NEW_PROJECT` may be discoverable with empty gate indexes — same as Manifest-ready ⊄ fully trackable.

### Ceasing discoverability

A catalog entry **ceases discoverability** (categories — not implementation) when:

| Situation | Catalog doctrine |
|-----------|------------------|
| Operator declares **withdrawn** from Factory portfolio | Hidden from default discoverable set; logical project may still exist in Engine |
| **Archived** after Factory terminal or charter partial closure | Historical catalog membership — distinction from active portfolio |
| **Duplicate entry** reconciled | One logical identity — one catalog entry (RA-03) |
| **Never was Factory-scoped** | Entry **invalid** — should not have been enrolled |
| Mistaken enrollment | Correction = new declaration record — **not** silent erase (AT-01 analog at catalog level) |

**Ceasing discoverability ≠ deleting Engine history:** Tracking/Manifest authority for the case may remain for audit — catalog visibility only changes.

### Discovery principles (normative)

| ID | Principle |
|----|-----------|
| **RD-01** | Discovery is **Factory-scoped** only — Frontend repos, MIG sessions, Foundation docs **without** Factory Project shell are **out of catalog** |
| **RD-02** | Discovery **requires** Manifest anchor — no «registry-only» project |
| **RD-03** | Default portfolio view shows **discoverable** entries — withdrawn/archived categories **may** appear in extended view (implementation OPEN) |
| **RD-04** | No discovery by **inferring** state from filesystem layout alone | BV-05 analog |
| **RD-05** | Site Type Registry paths **do not** imply Factory Project discovery | Naming collision guard |

---

## Stability Principles

Без определения storage — **ожидания эволюции категорий каталога**.

### Expected stable (slow-changing)

| Category | Stability rationale |
|----------|---------------------|
| Binding logical identity ↔ catalog entry | RA-03 — survives entire Factory track |
| Manifest entry pointer (doctrinal anchor) | Re-identification of same case |
| Charter core label / intent summary (for distinction) | Changes require explicit amendment — Registry summary **follows** |
| Scope tier summary | Amends drive catalog distinction update — not silent drift |
| Declared lifecycle endpoint summary | Charter event |
| Catalog enrollment declaration record | Append-only enrollment narrative |

### Expected evolving (fast-changing)

| Category | Evolution pattern |
|----------|-------------------|
| Orientation snapshot (active state glance) | Changes on each declared state transition |
| Classification summary | Appears after `CLASSIFIED` |
| Discoverability status (active vs archived) | Operator-declared catalog lifecycle |
| Factory track suspended / partial closed flags | Logical metadata visibility |

### Principle RS-01 — Stable catalog binding must not silently remap identity

Rebinding registry entry to **different** logical project requires **explicit** operator declaration — not overwrite.

### Principle RS-02 — Evolving snapshot must not become Registry-as-tracking

Copying live gate index into catalog card for «convenience» violates RA-05 — creates stale portfolio SoT.

### Principle RS-03 — Registry summary freshness

Portfolio orientation snapshot **must** be treated as **non-authoritative** unless reconciled with Engine active instance (MS-02 analog).

---

## Anti-Patterns

| ID | Anti-pattern | Why forbidden |
|----|--------------|---------------|
| **RAP-01** | Registry **as database** or ORM layer | RT-G04 / explicit non-claims |
| **RAP-02** | Registry **as storage** or git-backed SoT for project data | Storage charter territory |
| **RAP-03** | Registry **as runtime** or workflow executor | BV-04; not RT-G01 |
| **RAP-04** | Registry **as queue** or scheduler | RT-G06; BV-14 |
| **RAP-05** | Registry **as dashboard/UI** | RT-G12 — UI **displays** catalog after implementation |
| **RAP-06** | Registry **as project tracking system** | Duplicates Stage 3 at portfolio scale — RA-05 |
| **RAP-07** | Registry **as manifest** for all projects | MR-02; MAP-07 analog |
| **RAP-08** | Registry **as Passport** — second identity SoT | BV-15 |
| **RAP-09** | Registry entry ID **replaces** logical Factory Project identity | ES-03, RA-03 |
| **RAP-10** | Auto-discovery by scanning repos without Factory-scoped declaration | RD-04; violates human-operated v1 |
| **RAP-11** | Conflating **Site Type Registry** with Factory Project Registry | Class-level vs instance catalog |
| **RAP-12** | Registry **merging** Legal Pack, Registry matrices, Runtime docs | BV-03, MA-01 analog |
| **RAP-13** | Registry **as Gate Results** or handoff index for portfolio | Stage 4 non-claims at scale |
| **RAP-14** | Registry **as implementation spec** (FACTORY-PROJECT-INDEX, DISCOVERY, PASSPORT) | Forbidden sibling docs per task charter |
| **RAP-15** | Treating deploy / go-live as catalog «completion» | Terminal `COMPLETE` ≠ deploy — Stage 2 |
| **RAP-16** | Registry **preceding** Manifest at intake — catalog before orientability | RM-01, RD-02 |
| **RAP-17** | Silent deletion of enrollment history | AT-01 analog |
| **RAP-18** | Registry **as agent registry** or MCP tool catalog | External systems — not Factory Project catalog |

---

## Registry Readiness

Readiness — **doctrinal качество catalog integrity**, не production readiness проекта.

### Registry-ready (catalog entry)

A Factory Project catalog entry is **registry-ready** when:

| # | Criterion | ID |
|---|-----------|-----|
| 1 | Logical Factory Project identity is **explicit** and Factory-scoped | **RRDY-01** |
| 2 | Manifest entry anchor is **identified** (manifest-ready) | **RRDY-02** |
| 3 | Registry entry **distinct** from logical identity (RA-03 understood) | **RRDY-03** |
| 4 | Distinction summaries sufficient for portfolio (charter label, scope tier, endpoint category) | **RRDY-04** |
| 5 | Discoverability status category is **explicit** (discoverable vs withdrawn/archived) | **RRDY-05** |
| 6 | Operator understands Registry ≠ Tracking ≠ Manifest (integrity) | **RRDY-06** |

**Typical registry-ready moment:** after manifest-ready at intake, upon operator catalog enrollment declaration.

### Registry-incomplete

| Condition | Signal |
|-----------|--------|
| No Factory-scoped identity | **RRDY-01** fail — not catalog-eligible |
| Manifest-incomplete | **RRDY-02** fail — RD-02 |
| Registry entry ID conflated with project identity | **RRDY-03** integrity violation |
| Catalog card duplicates live Tracking index | **RAP-06** — incomplete until separated |
| Orientation snapshot contradicts Engine without flag | **RS-03** violation |
| Site Type Registry row mistaken for Factory Project | **RAP-11** |

### Registry-ready vs manifest-ready vs fully trackable

| Concept | Meaning |
|---------|---------|
| **Manifest-ready** | Per-project orientability (MRDY-*) |
| **Registry-ready** | Catalog entry integrity (RRDY-*) |
| **Fully trackable** | All seven Tracking questions (TC-*) |
| **Discoverable** | In default Factory portfolio per RD-* |

A project may be **registry-ready** and **gate-incomplete** — normal mid-chain. A project may be **manifest-ready** but **not discoverable** until operator enrolls catalog.

---

## Explicit Non-Claims

This document and the Factory Project Registry Charter it defines:

- **are not** a Website Factory **runtime**, execution engine, or shipped product;
- **are not** **storage**, **database**, **file format**, **queue**, or **workflow engine**;
- **are not** a **dashboard**, **operator UI** (RT-G12), or **CLI**;
- **are not** **implementation**, **automation**, **agents**, or **serialization standard**;
- **are not** **manifest** (RT-G10) or **passport**;
- **are not** **tracking system** — per-project or portfolio-scale;
- **are not** Foundation **Site Type Registry** (`registry/SITE-TYPE-REGISTRY-v1.md`);
- **are not** FACTORY-PROJECT-INDEX-v1, FACTORY-PROJECT-DISCOVERY-v1, FACTORY-PROJECT-PASSPORT-v1, FACTORY-TRACKING-SURFACE-v1, FACTORY-REGISTRY-STORAGE-v1;
- **do not** define JSON/YAML schemas, field lists, folder structures, database tables, indexes, or registry file paths;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** modify Manifest Charter, Runtime Architecture, or Foundation layers;
- **do not** claim physical Registry artefact exists in repo — **charter only**.

Human-operated catalog enrollment remains the v1 model per Runtime Architecture human-operated discipline.

---

## Open Questions

Charter **bounds** questions for **future** implementation — **does not answer** storage or index format.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-R01** | Physical registry artefact vs distributed pointers (RT-G04 relationship) | **OPEN** — storage charter |
| **OQ-R02** | Index card fields derived from Manifest categories (OQ-M05) | **OPEN** — implementation standard only |
| **OQ-R03** | Default vs extended portfolio view for archived/withdrawn | **OPEN** — RT-G12 display |
| **OQ-R04** | Duplicate detection across logical identities | **OPEN** — operational playbook |
| **OQ-R05** | PHASE_SLICE — one catalog entry per shell vs per slice | **OPEN** — Engine v2 or implementation |
| **OQ-R06** | External workspace pointer in catalog card (OQ-M06) | **OPEN** — operational |
| **OQ-R07** | Relationship RT-G06 queue to catalog entry | **OPEN** — queue charter |
| **OQ-R08** | Auto-sync catalog snapshot from Tracking — allowed or forbidden | **BOUNDED** — forbidden as authoritative (RAP-06); display sync **implementation** only |
| **OQ-R09** | MIG / incoming request correlation as catalog category | **OPEN** — integration charter RT-G08 |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat this charter as **RT-G05 role definition complete** — gap RT-G05 in RUNTIME-GAPS remains **NOT STARTED** for **implementation**, not for doctrine.
2. **If physical catalog needed:** Authorize **separate** «Project Registry Standard» implementation charter — **must** carry RA-*, RM-*, RAP-* forward; **do not** create FACTORY-PROJECT-INDEX-v1 in Engine path without explicit authorization.
3. **If operator UI needed:** RT-G12 — portfolio view **reads** Registry **after** implementation; per-project drill-down → Manifest → Tracking.
4. **If persistence needed:** RT-G04 before or with registry implementation — Registry **does not** choose storage.
5. **Do not create:** FACTORY-PROJECT-INDEX-v1.md, FACTORY-PROJECT-DISCOVERY-v1.md, FACTORY-REGISTRY-STORAGE-v1.md, or unified YAML catalog schema in Engine path.
6. **Optional P3:** Update RUNTIME-GAPS RT-G05 line to «CHARTERED (doctrine)» — **operator action**, outside this deliverable.

**Engine Architecture v1 requires no further architecture stages.** Registry charter is **post-Engine, post-Manifest-doctrine** documentation.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether any repo path is already used as de-facto Factory Project catalog | **UNKNOWN** — no canonical catalog chartered |
| Calendar for Registry implementation standard | **not scheduled** |
| Triumph / client workspaces in catalog vs external-only | **UNKNOWN** — charter per case |
| MARS v2 repo-wide baseline vs `website-factory-reference-v1` | **not verified** in this charter scope |

---

*Factory Project Registry Charter v1 — RT-G05 doctrine complete. Architecture charter only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Project Registry Charter v1

**Stage:** RT-G05 — Factory Project Registry Charter (post–Engine Architecture v1, post–Manifest Charter)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-REGISTRY-CHARTER-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-REGISTRY-CHARTER-v1.md` (created)  
**Summary:** Определена доктрина Factory Project Registry как мультипроектного каталога Factory-scoped cases: purpose, position vs Manifest/Engine/Tracking, authority (catalog/discoverability/distinction) и non-authority (state, gates, manifest bodies, Site Type Registry); категории scope без полей; зависимость Registry от Manifest (RM-*, RD-02) и внешность к Engine (RE-*, ES-03); discovery/stability models; anti-patterns; registry-ready vs incomplete — без storage, schemas, indexes, runtime, dashboard, implementation.  
**Git:** no commit, no push (per task charter).
