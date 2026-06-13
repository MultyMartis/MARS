# REPORT — Factory Project Manifest Charter v1

**Версия:** v1  
**Дата:** 2026-06-04  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Post–Factory Engine Architecture v1 — **RT-G10 charter only**  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 Stages 1–6 **COMPLETE**; Engine Readiness Audit v1 — **PASS WITH WARNINGS**  
**Тип:** charter only — **без** implementation, runtime, storage format, schemas, field lists, files, UI, registry design  
**Связь:** [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md), [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G10

---

## Purpose

### Зачем существует Project Manifest

**Project Manifest** — архитектурная **доктрина канонической точки входа** для одного Factory Project. Manifest отвечает на вопросы, которые Engine v1 уже разрешил **логически**, но которые оператору нужно связывать **без археологии по workspace**:

| Вопрос оператора | Роль Manifest |
|------------------|---------------|
| **Что это за проект?** | Фиксирует **минимальное понимание** production case: идентичность, charter, scope, declared endpoint — как **категории знания**, не как поля файла |
| **Где авторитетная точка входа?** | Объявляет Manifest как **доктринальный entry anchor** — «начни здесь», прежде чем углубляться в Tracking composition и layer refs |
| **Какое минимальное понимание должно существовать?** | Определяет **обязательные категории** project understanding, достаточные для Factory-scoped работы |
| **Куда смотреть за истиной по state/gates/artefacts?** | **Не сливает** authority — указывает **топологию ссылок** на Engine planes и Foundation layers |

Manifest решает **координационную проблему ориентации**: при распределённой authority (T1–T5 в Object Model) оператору нужен **один согласованный вход**, который **не подменяет** ни один authoritative source.

### Что Manifest **не** решает

| Проблема | Куда относится |
|----------|----------------|
| Как проект **движется** по chain | Runtime + [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) |
| Как оператор **наблюдает** полный прогресс в реальном времени | [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) |
| Как gates **авторизуют** переходы | [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) |
| Как lifecycle **складывается** в нарратив | [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) |
| Где **физически** хранятся записи | **FUTURE** RT-G04 storage |
| Как **сериализовать** записи | **FUTURE** RT-G10 implementation standard (отдельный charter) |
| Индекс **всех** Factory projects | **FUTURE** RT-G05 registry |
| Исполнение, automation, agents | External / RT-G01, RT-G03, RT-G11 |

**Manifest — charter (конституция роли), не продукт и не формат.**

---

## Foundation Dependencies

Manifest Charter **наследует** завершённый Engine v1 и **не изменяет** Foundation или Runtime.

### Tier 1 — Engine Architecture (обязательные)

| Document | Manifest использует |
|----------|---------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Factory Project, mandatory components, authority tiers, «What is this project?» |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Active state instance — **категория** в Manifest, vocabulary — Runtime |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking zones, visibility tiers, seven operator questions — **граница** vs Manifest |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Gate instance semantics — **не** дублировать в Manifest |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | Declared endpoint, segments — Manifest **ссылается**, не владеет progression |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | Engine boundary, ES-04, BV-03, forbidden documents |

### Tier 2 — Readiness context

| Document | Role |
|----------|------|
| [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md) | RT-G10 как post-Engine gap; distributed authority confirmed |
| [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) | Global layer ACCEPTED — **не** per-project Manifest content |

### Tier 3 — Runtime + Foundation (reference only)

Runtime Architecture v1 (states, `RG-*`, `HO-*`, LC-*); принятая 14-layer Foundation chain. Manifest **не** переопределяет layer contracts.

**Authority precedence:** Foundation Freeze + Finalization Pass + Engine Readiness Audit → Engine Stages 1–6 → **этот charter** для роли Manifest → **будущий** implementation standard (если авторизован) **не может** нарушить ownership rules Engine.

---

## Manifest Position In Factory

```text
                    ┌─────────────────────────────────────┐
                    │   PROJECT MANIFEST (charter role)    │
                    │   entry anchor · minimum understanding │
                    │   reference topology · scope doctrine  │
                    └─────────────────────────────────────┘
                          │ orients          │ does not execute
                          ▼                  ▼
        ┌─────────────────────────────────────────────────────┐
        │              FACTORY ENGINE v1 (Stages 1–6)          │
        │  Object · State · Tracking · Gates · Lifecycle     │
        └─────────────────────────────────────────────────────┘
              │ references                    │ references
              ▼                               ▼
    ┌──────────────────┐              ┌──────────────────┐
    │  RUNTIME (T2)    │              │  FOUNDATION (T1) │
    │  vocabulary only │              │  layer authority │
    └──────────────────┘              └──────────────────┘
              │
              │ future binding (separate charters)
              ▼
    ┌──────────────────────────────────────────┐
    │  RT-G04 Storage · RT-G05 Registry         │
    │  RT-G10 Serialization · RT-G12 UI         │
    └──────────────────────────────────────────┘
```

### Позиция относительно Engine planes

| Plane | Manifest relationship |
|-------|----------------------|
| **Project Object** | Manifest **отражает doctrine** identity shell и charter — не заменяет Object Model |
| **State** | Manifest **категоризирует** «текущее положение» как entry fact; **не** владеет state vocabulary |
| **Tracking** | Manifest **предшествует** deep tracking read — entry before composition surface |
| **Gate Composition** | Manifest **не** хранит gate outcome index — указывает, что authoritative gate truth в tracking/gate index |
| **Lifecycle Composition** | Manifest **может** фиксировать declared endpoint и scope tier; **не** владеет segment progression |

### Позиция в эре Website Factory

| Эра | Status | Manifest |
|-----|--------|----------|
| Foundation Era | **COMPLETE** | Manifest **не** заменяет layer contracts |
| Factory Engine Architecture v1 | **COMPLETE** | Manifest **дополняет** Engine — post-Stage 6 charter |
| RT-G10 implementation | **NOT STARTED** | Этот документ — **только** charter роли |

---

## Manifest Authority Principles

### Authority Manifest **имеет**

| Authority class | Statement |
|-----------------|-----------|
| **Entry-point doctrine** | Manifest объявлен как **каноническая точка входа** для понимания **этого** Factory Project в Factory scope |
| **Minimum understanding contract** | Определяет, какие **категории** project knowledge **должны** быть явными, чтобы проект считался orientable |
| **Reference topology** | Определяет, **куда** оператор направляется за authoritative truth (Engine planes, Runtime, layers) — без копирования тел |
| **Scope & endpoint doctrine** | Charter-driven scope tier и declared lifecycle endpoint — **категории**, принадлежащие operator-authored charter, **индексируемые** Manifest doctrine |
| **Stability expectations** | Какие категории **должны** оставаться стабильными vs какие **ожидаемо** эволюционируют (см. Stability Principles) |

### Authority Manifest **не имеет**

| Non-authority | Actual owner |
|---------------|--------------|
| Canonical state / gate / handoff **definitions** | Runtime Architecture v1 |
| Pass/fail **criteria** | Foundation layers + RUNTIME-GATES |
| Layer artefact **bodies** | Layer workstreams |
| **Live** gate outcome index, progression ledger | Engine tracking instance (T4) |
| Global layer ACCEPTED status | NEXT-PRIORITIES (T5) |
| Multi-project discovery, queue rank | **FUTURE** RT-G05, RT-G06 |
| Automated state mutation | **Nobody in v1** |
| Foundation redesign | Protected documents |

### Principle MA-01 — Manifest is anchor, not aggregator of authority

Manifest **ориентирует** оператора к распределённым источникам. Manifest **не становится** единым authoritative document, заменяющим Legal Pack, Registry, Runtime или Engine indexes (см. BV-03 в System Boundary).

### Principle MA-02 — Declaration truth stays in Engine

**Последняя объявленная истина** по state, gates, handoffs остаётся в Engine tracking planes. Manifest doctrine **не** переопределяет operator declarations и **не** подменяет append-only audit trail (AT-01).

### Principle MA-03 — Manifest ≠ Passport

**Passport** (запрещённый артефакт) подразумевает второй parallel SoT, дублирующий Object + Tracking identity. Manifest charter **явно отвергает** эту роль — см. Anti-Patterns.

---

## Manifest Scope Principles

Scope Manifest — **категории project knowledge** и **владение категорией**. **Не** field lists, **не** schemas.

### Category 1 — Stable project identity

| Aspect | Ownership |
|--------|-----------|
| Уникальная ссылка на production case в Factory scope | Engine identity shell (Object Model); Manifest **доктринально требует** явности категории |
| Distinction from registry entry ID | Registry **FUTURE** — logical identity precedes registry index |

### Category 2 — Charter & production intent

| Aspect | Ownership |
|--------|-----------|
| Цели, exclusions, stakeholder context, operator assignment | **Operator-authored** charter; Manifest **требует** категорию, не содержание шаблона |
| Partial / design-only / PHASE_SLICE scope | Charter drives LR-07 mask — Manifest **фиксирует doctrine** scope tier |

### Category 3 — Declared lifecycle endpoint

| Aspect | Ownership |
|--------|-----------|
| Full chain → `COMPLETE` vs partial charter endpoint | Lifecycle Composition LCMP-5; Manifest **категоризирует** endpoint **без** владения progression |
| `FACTORY_TRACK_SUSPENDED` / partial closure flags | Logical metadata (Stage 5) — Manifest may **reference category**, not invent Runtime states |

### Category 4 — Scope applicability doctrine

| Aspect | Ownership |
|--------|-----------|
| Full chain default vs EXCLUDED states | State scope mask (Stage 2); Manifest states **that** applicability must be explicit |
| Effective path for partial scope | **OPEN** operational — Manifest does not define jump table |

### Category 5 — Classification & binding anchors (lifecycle-dependent)

| Aspect | Ownership |
|--------|-----------|
| `site_type_code` when classified | Registry outputs — Manifest **category** «classification binding» when applicable |
| `blueprint_ref`, `generation_id`, scope freeze | Layer/Engine refs — Manifest marks **when** category becomes mandatory, not artefact body |

### Category 6 — Current position summary (non-authoritative snapshot)

| Aspect | Ownership |
|--------|-----------|
| Active `runtime_state_code` as **orientation fact** | State instance owned by Engine; Manifest **may surface category** «where now» as **pointer to** tracking, not independent SoT |
| Active LC segment label | Derived from Runtime binding map — **read-only** |

### Category 7 — Authoritative reference topology

| Aspect | Ownership |
|--------|-----------|
| Where state truth lives | Engine state instance + Runtime vocabulary |
| Where gate truth lives | Gate outcome index (Stage 4) |
| Where handoff truth lives | Handoff event index (Stage 6 HB-*) |
| Where artefact truth lives | Layer workstreams; project holds refs only |
| Where movement rules live | Runtime STATE-TRANSITION-RULES |
| Where layer semantics live | Foundation T1 docs |
| Where ATLAS business identity lives | ATLAS Business Reality Registry — Factory holds **refs only** via Category 7 external topology (MOC-12) |

**Manifest owns the map of maps — not the territories.**

#### ATLAS reference convention (Category 7 / MOC-12)

When binding ATLAS canonical ids in charter or external-ref topology, operator **SHOULD** use normative field names per [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md):

| Field name | ATLAS id | Semantics |
|------------|----------|-----------|
| `atlas_client_org_ref` | `ORG-*` | Commissioning / client organization |
| `atlas_person_ref` | `PER-*` | Person identity when charter-bound |
| `atlas_website_ref` | `WEB-*` | Structural website identity |
| `atlas_project_ref` | `PRJ-*` | Structural ATLAS project — **not** Factory Project id |
| `atlas_relationship_ref` | `REL-*` | Structural relationship edge when relevant |
| `atlas_domain_ref` | `DOM-*` | Domain identity when relevant |

**Disposition:** When active attested canonical exists → field **SHOULD** be populated (ref only). When unknown or disputed → **SAFE UNKNOWN**; **MUST NOT** invent OWNER/ORG. Factory Project identity **MUST remain distinct** from `atlas_project_ref`. **Convention only** — no serialization or schema defined in this charter.

### Category 8 — Foundation version & dependency pins (logical)

| Aspect | Ownership |
|--------|-----------|
| Which ACCEPTED/FROZEN layer versions apply to this case | Implicit default or charter-pinned — Manifest **category** for operator clarity |
| Not per-project redefinition of global ACCEPTED | T5 remains global register |

### Categories **explicitly outside** Manifest scope

| Excluded category | Why |
|-----------------|-----|
| Gate outcome bodies, composite constituent detail | Tracking + Gate Composition |
| Handoff package payloads | Generation Outputs / layers |
| Validation run logs, failure playbook text | Layer workstreams |
| Full state history, progression ledger | State Model / Tracking |
| Frontend code, deploy, hosting | Post-Factory |
| Queue position among projects | RT-G06 |
| Agent transcripts, MIG sessions | External unless charter-bound ref |

---

## Relationship To Project Object

| Relationship | Statement |
|--------------|-----------|
| **Manifest serves Object** | Manifest — **доктринальная оболочка entry** для Factory Project как Object Model defines it |
| **Object serves Manifest** | Mandatory components (identity shell, charter, indexes) — **логические источники** категорий Manifest; Manifest **не** добавляет новых mandatory components |
| **Minimum identity alignment** | Object Model minimum identity dimensions (stable id, charter, scope tier, state when tracked, classification when present) — **совпадают** с Manifest minimum understanding categories **без** превращения в schema |
| **Not a substitute object** | Manifest **не** заменяет Factory Project как логическую единицу — проект существует в Engine model **до** любой физической сериализации |

**Operator «What is this project?»** = ответ **начинается** с Manifest entry doctrine, **завершается** через Tracking composition (charter + scope + state + classification + exclusions) — Manifest **не** дублирует полный Tracking surface.

---

## Relationship To State

| Concern | State Model | Manifest |
|---------|-------------|----------|
| State **vocabulary** | Runtime — 14 codes | **References only** — MA-01 |
| State **instance** | Engine owns active + history | Manifest **категория** «current position» — **pointer**, не parallel ledger |
| Progression / rollback | State Model owns semantics | Manifest **не** записывает transitions |
| Eligibility / blocking | Derived in tracking | Manifest **направляет** к tracking eligibility snapshot |

### Principles

| ID | Principle |
|----|-----------|
| **MS-01** | Manifest **never** introduces state codes or sub-states |
| **MS-02** | If Manifest surfaces active state, it **must** match Engine active instance or be flagged invalid (SV-05) |
| **MS-03** | State **history** belongs in State/Tracking planes — **not** Manifest scope as live index |
| **MS-04** | Terminal `COMPLETE` in Manifest orientation **implies** Factory closure doctrine — not deploy go-live |

---

## Relationship To Tracking

Tracking и Manifest — **соседние, не дублирующие** роли post-Engine.

```text
  OPERATOR PATH
       │
       ▼
  ┌─────────────┐     «What is this? Where do I start?»
  │  MANIFEST   │     minimum understanding · entry anchor
  │  (charter)  │     reference topology
  └──────┬──────┘
         │ deep read
         ▼
  ┌─────────────┐     «Where now? What passed? What blocks?»
  │  TRACKING   │     full observability composition
  │  (Engine)   │     seven questions · Tier A/B/C visibility
  └─────────────┘
```

### What Tracking knows that Manifest does not

| Tracking knowledge | Why Manifest excludes |
|--------------------|----------------------|
| Full gate outcome index with STALE/INVALID | Live authorization plane — Gate Composition + Tracking |
| Complete handoff event sequence | Handoff Binding + Tracking |
| Artefact reference index by LC phase | AV-* rules — exhaustive refs |
| Eligibility snapshot, open gate set | Derived real-time blocking |
| Append-only audit trail detail | AT-* — operational depth |
| Tier B deferred visibility rules | Tracking-specific composition |

### What Manifest knows that Tracking does not (doctrinally)

| Manifest knowledge | Why Tracking does not own |
|--------------------|---------------------------|
| **Entry-point authority** — «start here» | Tracking is composition surface, not entry doctrine |
| **Minimum understanding contract** before full trackability | TC-* allows partial trackability at intake; Manifest defines **orientability** threshold |
| **Reference topology map** (where truths live) | Tracking points to refs; Manifest **charters** the map structure |
| **Stability expectations** for charter-bound categories | Tracking reflects last declared truth (TV-02) — Manifest sets **what should remain stable** |

### Principle MT-01 — No duplicated tracking

Manifest charter **запрещает** использование Manifest (или будущей сериализации) как **второго live gate/handoff index**. Tracking остаётся **единственной** observability composition для instance records.

### Principle MT-02 — Future serialization maps to Tracking zones

Когда RT-G10 implementation standard будет авторизован, он **может сериализовать** Tracking zones (ES-04, OQ-S4-11) — **только** под отдельным implementation charter и **без** нарушения MT-01. **Этот charter не выбирает**, какие zones сериализуются.

---

## Relationship To Lifecycle

| Concern | Lifecycle Composition | Manifest |
|---------|----------------------|----------|
| LC-00…LC-13 segments | Runtime vocabulary + composition narrative | Manifest **категория** declared endpoint only |
| Active segment | 1:1 active state | Manifest may **summarize** «active segment» as orientation — **not** own segment transitions |
| Rollback cascade | LRC-* invalidation on indexes | Manifest **не** исполняет cascade |
| Parallel legal co-track | LCMP-6 | Manifest **категория** «legal track required» when scope demands — detail in tracking |
| Partial completion | Charter endpoint vs `COMPLETE` | Manifest **must** make endpoint category explicit at intake |

### Principles

| ID | Principle |
|----|-----------|
| **ML-01** | Manifest **does not own** lifecycle progression — only **declares** endpoint doctrine and scope boundaries |
| **ML-02** | Lifecycle halt (LS-*) visible through Tracking — Manifest **does not** replace halt narrative |
| **ML-03** | `FACTORY_TRACK_SUSPENDED` — Manifest may require **visibility category**; semantics stay Stage 5 |
| **ML-04** | Manifest **never** automates segment transitions |

---

## Relationship To Future Registry

### Why Registry may depend on Manifest

| Reason | Statement |
|--------|-----------|
| **Discovery** | RT-G05 registry indexes **many** projects — needs stable **logical key** and entry pointer per project |
| **Separation of concerns** | Registry = **multi-project index**; Manifest doctrine = **single-project entry anchor** |
| **Non-identity** | ES-03: registry entry ID ≠ Factory Project identity — Manifest anchors **logical project**, registry **may reference** that anchor when implemented |

### What Registry would know that Manifest does not

| Registry scope | Manifest exclusion |
|----------------|-------------------|
| Cross-project listing, search, filters | Per-project charter only |
| Queue position, prioritization (RT-G06) | Explicitly external |
| Org-wide operational dashboards | RT-G12 display layer |
| Duplicate detection across projects | **FUTURE** — not Manifest charter |

### What Manifest knows that Registry does not

| Manifest scope | Registry exclusion |
|----------------|-------------------|
| Per-project minimum understanding | Registry holds **index cards**, not full charter intent |
| Authoritative reference topology for **one** case | Registry **points to** manifest/tracking entry — does not merge layer authority |
| Scope & endpoint doctrine for **this** production case | Registry may store **summary** — not replace charter |

### Principle MR-01 — Registry follows Manifest doctrine, not vice versa

Logical Factory Project **precedes** registry entry. Manifest charter **не проектирует** registry schema, API, or storage.

### Principle MR-02 — Manifest is not Registry

Manifest **не** является центральным реестром проектов. Один Manifest doctrine applies **per** Factory Project.

---

## Stability Principles

Без определения storage — **ожидания эволюции категорий**.

### Expected stable (slow-changing)

| Category | Stability rationale |
|----------|---------------------|
| Stable project identity reference | Must survive entire Factory track |
| Charter core intent & exclusions | Changes require explicit charter amendment doctrine |
| Scope tier (`FULL_SITE`, partial, PHASE_SLICE) | Amends drive LR-07 mask review — **not** silent drift |
| Declared lifecycle endpoint | Changes = charter event — affects gate-complete endpoint (GCO-01) |
| Foundation version pins (when explicitly pinned) | Auditability of which contracts applied |

### Expected evolving (fast-changing)

| Category | Evolution pattern |
|----------|-------------------|
| Current position summary | Changes on every declared state transition |
| Classification / blueprint / generation bindings | Appear as lifecycle phases complete |
| Reference topology **targets** (which refs exist) | Grow with artefact index — topology **structure** stable, **instances** grow |
| Orientation to Tracking composition | Tracking reflects TV-02 last declared truth |

### Principle ST-01 — Stable categories must not be silently overwritten

Charter amendments and scope changes **require** explicit operator declaration — aligned with append-only audit (AT-01). Future serialization **must** preserve amendment narrative — **implementation OPEN**.

### Principle ST-02 — Evolving categories must not be frozen into Manifest-as-database

Manifest doctrine **rejects** copying live gate index into «stable» Manifest — that would violate MT-01 and create stale SoT.

---

## Anti-Patterns

| ID | Anti-pattern | Why forbidden |
|----|--------------|---------------|
| **MAP-01** | Manifest **as storage** or state store | RT-G04 territory; Manifest is charter only |
| **MAP-02** | Manifest **as database** or query engine | No persistence claims |
| **MAP-03** | Manifest **as YAML/JSON/file format** charter in this doc | Implementation standard is **separate** future work |
| **MAP-04** | Manifest **as runtime** or workflow executor | BV-04; explicit non-claims |
| **MAP-05** | Manifest **as duplicated Tracking** — live gate/handoff/history index | MT-01; second observability SoT |
| **MAP-06** | Manifest **as Passport** — parallel identity document | BV-15; forbidden PASSPORT doc class |
| **MAP-07** | Manifest **as Registry** — multi-project index | MR-02; RT-G05 separate |
| **MAP-08** | Manifest **merging Foundation authority** — embedding Legal Pack, Registry matrices | BV-03, MA-01 |
| **MAP-09** | Manifest **as dashboard/UI** | RT-G12 — display may read Manifest **after** implementation |
| **MAP-10** | Manifest **as Gate Results System** | Stage 4 non-claims |
| **MAP-11** | Manifest **as Handoff Package** or artefact body store | HB-08, AV-01 |
| **MAP-12** | Treating Manifest serialization **as** automated state mutation source | Violates human-operated v1 |
| **MAP-13** | Conflating deploy / go-live with Manifest «completion» | Terminal `COMPLETE` ≠ deploy — Stage 2 |
| **MAP-14** | Silent deletion of charter history on amendment | AT-01 violation |
| **MAP-15** | Using Manifest to add Runtime states, `RG-*`, or `HO-*` | ERA-W07; Engine consumes vocabulary only |

---

## Manifest Readiness

Readiness — **doctrinal качество orientability**, не production readiness и не trackability alone.

### Manifest-ready

Factory Project is **manifest-ready** when an operator can answer **from Manifest doctrine categories alone** (with **only** follow-through to authoritative sources, not workspace search):

| # | Criterion | ID |
|---|-----------|-----|
| 1 | Stable project identity category is **explicit** | **MRDY-01** |
| 2 | Charter & scope tier category is **explicit** (may be minimal at intake) | **MRDY-02** |
| 3 | Declared lifecycle endpoint category is **explicit** (default full chain stated) | **MRDY-03** |
| 4 | Scope applicability doctrine is **explicit** (full chain or partial with exclusions acknowledged) | **MRDY-04** |
| 5 | Authoritative reference topology is **declared** — operator knows where state, gate, artefact truths live | **MRDY-05** |
| 6 | Manifest entry anchor is **identified** for this production case (doctrinal, not necessarily physical file yet) | **MRDY-06** |
| 7 | Distinction from Passport/Registry roles is **understood** by operator | **MRDY-07** |

**Typical manifest-ready moments:** Factory-scoped recognition at intake (`NEW_PROJECT`) with charter; reinforced at `CLASSIFIED` and beyond as binding categories appear.

**Manifest-ready ⊄ fully trackable:** Early intake may be manifest-ready with **empty** gate/handoff indexes (TC early partial trackable) — Manifest requires **categories**, Tracking requires **indexes**.

### Manifest-incomplete

| Condition | Signal |
|-----------|--------|
| No stable project identity | Not Factory-scoped — no Manifest role |
| Charter / scope tier absent | **MRDY-02** fail |
| Declared endpoint unstated (implicit ambiguity) | **MRDY-03** fail |
| Operator cannot locate authoritative sources (topology undeclared) | **MRDY-05** fail |
| Manifest confused with live Tracking index (MAP-05) | **Integrity violation** — incomplete until separated |
| Active state in Manifest contradicts Engine without reconciliation | **MS-02** violation |

### Manifest-ready vs Engine completeness

| Concept | Meaning |
|---------|---------|
| **Manifest-ready** | Orientability threshold for entry doctrine |
| **Fully trackable** (Stage 3 TC-*) | All seven tracking questions answerable from composition |
| **Gate-complete** (Stage 4 GCO-*) | Authorization through declared endpoint |
| **Lifecycle complete** (Stage 5) | Declared endpoint reached in composition narrative |

A project may be **manifest-ready** and **gate-incomplete** simultaneously — normal mid-chain state.

---

## Explicit Non-Claims

This document and the Project Manifest Charter it defines:

- **are not** a Website Factory **runtime**, execution engine, or shipped product;
- **are not** **storage**, **database**, **file format**, **queue**, or **workflow engine**;
- **are not** a **dashboard**, **operator UI** (RT-G12), or **CLI**;
- **are not** **implementation**, **automation**, **agents**, or **serialization standard**;
- **are not** **registry** (RT-G05) or **passport**;
- **are not** FACTORY-PROJECT-MANIFEST-v1.md **implementation spec**, FACTORY-PROJECT-PASSPORT, FACTORY-STATE-STORE, FACTORY-GATE-RESULTS, FACTORY-ENGINE-SYSTEM **product**;
- **do not** define JSON/YAML schemas, field lists, folder structures, database tables, or manifest file paths;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** modify Runtime Architecture, Foundation layers, or Legal Pack;
- **do not** claim physical Manifest artefact exists in repo — **charter only**.

Human-operated declaration remains the v1 model per Runtime Architecture.

---

## Open Questions

Charter **bounds** questions for **future** implementation standard — **does not answer** serialization choices.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-M01** | Which Tracking zones **may** serialize into physical Manifest (OQ-S4-11, OQ-S6-05) | **OPEN** — implementation charter only |
| **OQ-M02** | Whether partial closure metadata is a Manifest category vs Tracking flag only (OQ-S6-09) | **OPEN** — operational playbook may precede serialization |
| **OQ-M03** | PHASE_SLICE / multi-`generation_id` — one Manifest doctrine per shell vs per slice (OQ-S6-03) | **OPEN** — Engine v2 or implementation charter |
| **OQ-M04** | Physical co-location of Manifest vs tracking records (RT-G04 relationship) | **OPEN** — storage charter |
| **OQ-M05** | Registry index card fields derived from Manifest categories (RT-G05) | **OPEN** — registry charter |
| **OQ-M06** | External workspace pointer (ERA-W03) as Manifest category vs tracking-only | **OPEN** — operational playbook |
| **OQ-M07** | `PASS_WITH_WARNINGS` — Manifest orientation category (OQ-S6-08) | **OPEN** — validation binding |
| **OQ-M08** | Chrome blocks without `block_id` — Manifest binding category (ERA-W01) | **OPEN** |
| **OQ-M09** | Minimum progression record exposure via Manifest vs Tracking-only (OQ-S3-06) | **BOUNDED** — progression stays State/Tracking; Manifest points, does not duplicate |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat this charter as **RT-G10 role definition complete** — gap RT-G10 in RUNTIME-GAPS remains **NOT STARTED** for **implementation**, not for doctrine.
2. **If physical Manifest needed:** Authorize **separate** «Project Manifest Standard» implementation charter — may create serialization spec **mapping to** Tracking zones per ES-04; **must** carry forward MA-*, MT-*, MAP-* anti-patterns.
3. **If multi-project ops needed:** RT-G05 Registry charter — registry **references** Manifest anchor per ES-03.
4. **Do not create:** FACTORY-PROJECT-PASSPORT-v1.md, unified YAML schema in Engine path, or Manifest-as-Gate-Results (Forbidden list in System Boundary).
5. **Optional P3:** Update RUNTIME-GAPS RT-G10 line to «CHARTERED (doctrine)» — **operator action**, outside this deliverable scope.

**Engine Architecture v1 requires no further architecture stages.** Manifest charter is **post-Engine** documentation.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether any repo path is already used as de-facto Manifest | **UNKNOWN** — no canonical path chartered |
| Calendar for Manifest implementation standard | **not scheduled** |
| Triumph / client deploy vs Manifest «completion» | **UNKNOWN** — external |
| MARS v2 repo-wide baseline vs `website-factory-reference-v1` | **not verified** in this charter scope |

---

*Factory Project Manifest Charter v1 — RT-G10 doctrine complete. Architecture charter only. Canonical location: `workspaces/website-factory-reference-v1/`.*

---

# REPORT — Factory Project Manifest Charter v1

**Stage:** RT-G10 — Project Manifest Charter (post–Engine Architecture v1)  
**Deliverable:** `FACTORY-PROJECT-MANIFEST-CHARTER-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-MANIFEST-CHARTER-v1.md` (created)  
**Summary:** Определена доктрина Project Manifest как канонической точки входа и minimum understanding contract для одного Factory Project; зафиксированы authority (entry anchor, topology) и non-authority (definitions, live tracking, layer bodies); категории scope без полей; отличия от Tracking, State, Lifecycle и будущего Registry; stability model, anti-patterns, manifest-ready vs manifest-incomplete — без storage, schemas, serialization, runtime, passport, registry implementation.  
**Git:** no commit, no push (per task charter).
