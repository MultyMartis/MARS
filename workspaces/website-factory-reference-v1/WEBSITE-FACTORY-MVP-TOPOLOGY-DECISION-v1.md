# REPORT — Website Factory MVP Topology Decision v1

**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `X:\AI MARS` (MARS monorepo)  
**Тип:** owner topology decision record + RT-G04 planning preparation only — **без** storage design, **без** file schema, **без** physical MVP folders, **без** implementation plan  
**Метод:** фиксация operator decision по результатам [WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md) и синтез принятых артефактов (MVP Definition Review, Implementation Planning Review, Operational Model, charters, Playbooks 01–05)  
**Принятая реальность (контекст задачи):** Foundation Era **COMPLETE**; Engine Architecture **COMPLETE**; Post-Engine Doctrine **COMPLETE**; Governance Synchronization **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Deployment Topology Review **COMPLETE**; RT-G04/05/10/12 implementation **NOT STARTED**; shipped Factory runtime **отсутствует**

**Upstream decision input:** [WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md) — topology analysis only; owner decision recorded **here**.

---

## Decision Summary

**Owner decision (зафиксировано):** Website Factory MVP размещается как **B — Filesystem + structured artifacts** внутри **`X:\AI MARS`** (MARS monorepo) в виде **структурированных filesystem-артефактов**.

**Смысл решения в одной строке:** MVP закрывает пробел **physical binding** (C2) через **единый file-backed persistence substrate** с **structured records** — operator может читать и **вручную** обновлять Factory Project records **без** shipped runtime, **без** database и **без** HomeGateway dependency.

**Что решение закрывает из Deployment Topology Review:**

| Factor ID | Status after this decision |
|-----------|---------------------------|
| **DF-01** Primary repo locus | **RESOLVED** — MARS monorepo (`X:\AI MARS`), не отдельный repo |
| **DF-02** Artifact class | **RESOLVED** — structured artifacts (class **B**), не markdown-only |
| **DF-06** HomeGateway integration depth | **RESOLVED by default** — **none**; Factory SoT **не** hosted by HomeGateway |
| **DF-03** Canon vs operational pack routing | **OPEN** — переносится в RT-G04 planning workshop |
| **DF-04…DF-10** | **OPEN** — вопросы RT-G04 planning, не blockers для старта planning |

**Что этот deliverable не делает:** не проектирует substrate, не создаёт папки MVP, не создаёт manifest/registry/tracking files, не авторизует RT-G04 charter text.

---

## Selected Topology

### Decision ID: **TOPOLOGY-B-v1**

| Dimension | Selected value |
|-----------|----------------|
| **Topology class** | **B — Filesystem + structured artifacts** |
| **Host / repo locus** | **`X:\AI MARS`** (MARS monorepo) |
| **Substrate nature** | Локальный **file-backed** слой с **structured records** для Factory Project persistence |
| **Operator model** | Single operator; human/assisted writes; **не** automated index mutation |
| **Integration stance** | MARS-embedded persistence; **без** HomeGateway SoT; **без** standalone application |

### Описание выбранной топологии (decision-level only)

MVP Website Factory **физически существует** как **авторизованный набор structured filesystem-артефактов** внутри MARS monorepo. Substrate:

- хранит per-project Manifest binding, Registry catalog binding, Tracking/Surface visibility data, declaration writes и closure outcomes;
- допускает git versioning артефактов;
- остаётся **читаемым и обновляемым operator'ом** через editor и/или lightweight local helpers (**design helpers explicitly out of scope**);
- **отделяет** Factory SoT от narrative doctrine docs и ad-hoc workspace scatter.

**Format structured records (JSON/YAML/SQLite file/иное) — NOT DECIDED.** Выбор формата — территория RT-G04 planning и последующих implementation charters (RT-G10/05/12), **не** этого decision record.

### Связь с MVP capability floor (из MVP Definition Review)

Выбранная топология **намеренно** поддерживает TR-01…TR-10 и **не** форсирует TX-01…TX-08:

| MVP anchor | Topology support |
|------------|------------------|
| **C2** Persistence substrate | **Primary target** — единый authorized physical locus |
| **C3** Manifest binding | Structured per-project records |
| **C4** Registry visibility | Structured portfolio catalog / index |
| **C5** Tracking visibility | Structured read path для eight Surface questions |
| **C6** Manual declarations | Operator-controlled write path |
| **C7** Closure persistence | Substrate принимает closure metadata |
| **C8–C9** Single operator, Core 5 | File-backed single-machine discipline sufficient |

---

## Meaning Of The Decision

### В принятых терминах Website Factory

1. **MVP ≠ новая doctrine.** Factory **уже работает** documentation-first (Playbooks 01–05 исполнимы без physical files). Решение **B** материализует то, что charters определили **логически** (Manifest, Registry, Tracking Surface), **не** переопределяя Engine Stages 1–6.

2. **MVP = physical binding gap closure.** Operator переходит от ad-hoc scatter и workspace archaeology к **авторизованной канонической привязке** в MARS repo — при сохранении **human-operated** model (Operational Model OR-*, OA-ACT-04, Playbook 04 DA-01).

3. **RT-G04 получает owner constraints.** Persistence substrate charter **должен** проектироваться **внутри** class **B** + MARS locus — не как unbounded placement exercise (guard SC-06).

4. **Structured artifacts ≠ Factory runtime product.** Substrate — **implementation territory** для file-backed records; **не** RT-G09 Engine runtime, **не** workflow engine (RT-G01), **не** automation layer (RT-G03). Structured files **могут** приглашать tooling discipline; tooling **не** заменяет operator declaration authority.

5. **Три doctrinal planes остаются разделёнными.** Manifest Charter (entry anchor), Registry Charter (portfolio catalog), Tracking Surface Charter (eight visibility questions) — **роли не сливаются**; substrate **хранит bindings**, charters **определяют ownership rules** (MAP-01, RAP-01, TS-*).

6. **Playbook path сохраняется.** Полный operator path Playbooks 01→02→03↔04→05 **исполним** с bound planes: enrollment → catalog → supervision → declarations → closure — **без** workflow engine.

7. **MARS — дом, не продукт.** Factory persistence **живёт в** `X:\AI MARS`, но **не** поглощает весь monorepo как Factory surface; client workspaces (`workspaces/triumph-*` и др.) остаются **external pointers**, не Factory SoT (ER-06, RAP-10).

### Что решение **явно включает**

| Included | Meaning |
|----------|---------|
| Единый persistence substrate | Один authorized physical layer для Factory Project records (C2) |
| Structured file-backed records | Machine-assistable read **без** orchestrator |
| MARS monorepo placement | Canon docs и SoT records под общей git discipline |
| Human-operated writes | Playbook 04 declarations reflected via operator-controlled path |
| Evolution headroom | Natural path к RT-G07 logs, RT-G11 validators **после** MVP — отдельными charters |

### Что решение **явно не включает**

| Excluded | Meaning |
|----------|---------|
| Physical folder tree | **Not created** by this decision |
| Record schemas / field lists | **Deferred** to RT-G04 planning → implementation charters |
| Manifest/registry/tracking **files** | **Not created** — planning only |
| Shipped application / service | No standalone Factory app |
| Database / multi-tenant storage | MVP sufficient with file-backed single-operator model |
| HomeGateway hosting | No HG SoT; no dashboard product requirement |
| Workflow / automation / queue | TX-01…TX-04 remain exclusions |

---

## Rejected Alternatives

Для MVP **не выбраны** следующие topology classes из Deployment Topology Review. Причины — decision-level, без implementation design.

### A — Git + Markdown only

| Aspect | Rejection rationale |
|--------|---------------------|
| **Суть** | MVP только как markdown-документы в git |
| **Почему не выбрано** | Недостаточная **C5 fidelity** для eight Surface visibility questions без жёсткой index discipline; выше риск **ad-hoc scatter** (OQ-OM01) и conflation narrative docs ↔ Factory SoT; слабее evolution path к structured Tier 1 capabilities |
| **Что сохраняется из A** | Git audit trail, single-repo discipline, zero deployment footprint — **как свойства** выбранного B, не как exclusive artifact class |

### C — Factory inside MARS as broad conceptual surface

| Aspect | Rejection rationale |
|--------|---------------------|
| **Суть** | Treating MARS monorepo **целиком** или неограниченно как Factory operational surface |
| **Почему не выбрано** | Нарушает **bounded Factory zone** principle; смешивает Site Type Registry (`registry/`), Lane A frontend (`src/`), unrelated MARS programs с Factory Project SoT (RAP-11); воспроизводит dual-corpus confusion (v0 operational pack vs v1 canon) без explicit routing |
| **Уточнение** | **MARS locus выбран** (repo = `X:\AI MARS`), но **не** как «весь repo = Factory». Placement — **ограниченная зона** внутри monorepo; exact zone = RT-G04 planning question (DF-03, OQ-OM01) |

### D — HomeGateway-integrated MVP

| Aspect | Rejection rationale |
|--------|---------------------|
| **Суть** | Factory persistence and/or read surface через HomeGateway program |
| **Почему не выбрано** | **Highest premature runtime/UI pressure** (SC-07); couples Factory MVP timeline к HG maturity (**SAFE UNKNOWN**); риск HG mutating indexes (TX-02, authority drift); Playbook 03 **forbids** UI in playbook; MVP excludes dashboard **product** (TX-07) |
| **Default stance** | DF-06 = **none** unless future owner override |

### E — Standalone Factory application

| Aspect | Rejection rationale |
|--------|---------------------|
| **Суть** | Отдельное приложение, microservice или repo вне MARS |
| **Почему не выбрано** | **Highest** delivery surface (install, deploy, versioning); split-brain между canon (in MARS) и SoT (outside); **reads as** Factory runtime product (SC-01, TX-05); слабее governance fit с accepted dual-contour MARS model |
| **Implication** | DF-01 resolved **against** separate repo |

### Not selected but noted (no owner decision required now)

| ID | Class | Note |
|----|-------|------|
| **F** | Hybrid documentation-first | Policy complement, not competing selection; phased materialization **may** inform RT-G04 planning **within** B |
| **G** | Per-project workspace colocation | Weak C4 catalog fit without mandatory aggregator; OQ-R01 remains planning question |

---

## Boundary Protection

Выбранная топология **B** **не имплицирует** следующие системы или зависимости. Любое появление нижеперечисленного в RT-G04 track требует **отдельного owner decision** и **не следует** из TOPOLOGY-B-v1.

| Boundary | Protection statement |
|----------|---------------------|
| **Database** | File-backed single-operator substrate **sufficient** per MVP Definition (TX-06). DB — post-MVP unless explicitly chartered later |
| **Runtime** | No shipped Factory runtime (RT-G09 impl), no workflow engine (RT-G01), no Engine execution product |
| **Application** | No standalone app shell, no SaaS operator product, no deployable Factory service |
| **Automation** | No CI/git-triggered SoT mutation (TX-02); validators **не** replace Playbook 04 (SC-03) |
| **Queue** | No multi-project scheduling substrate (RT-G06/G14) |
| **HomeGateway dependency** | Factory MVP **не требует** HG для persistence, visibility или writes |
| **UI / dashboard product** | RT-G12 = minimum read binding; Surface charter **≠** UI; no operator dashboard as MVP deliverable |
| **Agents / orchestration** | RT-G02/G03 explicitly out of MVP |
| **MIG / external pipeline ownership** | External triggers remain refs only (RT-G08) |

### Anti-pattern guards active for topology B

| Guard | Application |
|-------|-------------|
| **SC-01** | Structured persistence **≠** shipped Factory runtime narrative |
| **SC-03** | Scripts/CI **must not** mutate Engine indexes without operator act |
| **SC-06** | Storage/format design **must not** collapse into doctrine rewrite |
| **RAP-10** | Registry enrollment **declared**, not discovered by folder scan |
| **MAP-01** | Manifest charter **≠** storage owner — RT-G04 is separate substrate role |

### Discipline requirement (planning note, not design)

Topology **B** carries **medium** implementation pressure vs markdown-only. RT-G04 planning **must** preserve **human-only write authority** for declaration path (C6) and read-only Surface semantics (C5) — tooling helpers **may** exist later but **never** replace operator declarer.

---

## RT-G04 Planning Implications

Этот раздел определяет **вопросы**, которые RT-G04 Planning **обязан** закрыть. **Ответы и design — не в этом документе.**

### A. Substrate role and scope (charter-level questions)

| # | Planning question | Why it follows from TOPOLOGY-B-v1 |
|---|-------------------|-----------------------------------|
| Q1 | Какова **нормативная роль** RT-G04 persistence substrate относительно Engine boundary (ES-04, MAP-01, RAP-01)? | B creates physical layer **external** to Engine — charter must state boundaries |
| Q2 | Какие **классы записей** substrate **владеет** vs **указывает** (external workspace refs, layer bodies)? | Structured artifacts invite scope creep into T1 layer authority |
| Q3 | Как substrate обеспечивает **единый locus** (TR-01) без scatter (OQ-OM01)? | B trades simplicity for structure — path authority becomes critical |
| Q4 | Какие **non-goals** RT-G04 charter фиксирует, чтобы B **не** стал RT-G09 runtime? | SC-01 guard — highest risk for structured approach |

### B. Placement within MARS (DF-03, OQ-OM01, OQ-OM06)

| # | Planning question | Options space (not decided here) |
|---|-------------------|----------------------------------|
| Q5 | Где **authorized Factory zone** внутри `X:\AI MARS`? | `workspaces/website-factory-reference-v1/` subtree vs `projects/mars-website-factory/` vs **new** dedicated root |
| Q6 | Как routing разделяет **v1 canon** vs **v0 operational pack** (BCP-019)? | Canon docs remain doctrine; SoT records **не** supersede reference v1 without explicit rule |
| Q7 | Как substrate **ссылается** на client workspaces без colocating SoT (DF-08, ER-06)? | Pointers only vs partial colocation |
| Q8 | Как избежать путаницы с Site Type Registry (`registry/`) и Lane A `src/`? | Bounded zone naming / separation rules |

### C. Structured artifact class (format deferred)

| # | Planning question | Constraint from decision |
|---|-------------------|-------------------------|
| Q9 | Какой **class** structured records нужен для MVP bindings (не конкретный syntax)? | Must support C3–C7 **without** mandating database |
| Q10 | Какие **write paths** operator-controlled для Playbooks 03–04? | Human/assisted only; external systems **не** mutating indexes |
| Q11 | Какие **read paths** read-only для RT-G12 Surface binding? | Eight questions answerable **без** full workspace search |
| Q12 | Git versioning policy для SoT records (DF-10)? | Audit trail vs local-only operator state |

### D. Multi-plane binding (charter open questions)

| # | Planning question | Source |
|---|-------------------|--------|
| Q13 | Manifest vs tracking **co-location** (OQ-M04, DF-04)? | Same zone vs separated stores |
| Q14 | Registry index **shape** (OQ-R01, DF-05)? | Central catalog artefact vs distributed pointers + aggregator |
| Q15 | Declaration/session record binding (OQ-PD05)? | Near-MVP — supports SRDY-07 recency class |
| Q16 | RT-G12 read surface **form factor** (DF-07)? | Markdown index vs CLI vs static HTML — **coupled** to B but **not** dashboard product |

### E. Dependency sequencing (from Implementation Planning Review)

RT-G04 planning **must** preserve order:

```text
  TOPOLOGY-B-v1 (this decision)
           │
           ▼
  RT-G04 Planning → RT-G04 charter authorization
           │
           ├──▶ RT-G10 manifest impl planning
           │         │
           │         ├──▶ RT-G05 registry impl planning
           │         │
           │         └──▶ RT-G12 surface read binding planning
           │
           └──▶ declaration/session write binding (Playbooks 03–04)
```

### F. Planning workshop outputs (expected, not created now)

RT-G04 Planning **should produce** (future deliverables):

- RT-G04 persistence substrate **charter** (role, boundaries, non-goals)
- Resolved DF-03 placement recommendation for owner confirmation
- Resolved DF-04…DF-10 **inside** charter scope where appropriate
- Explicit SC-01/SC-03/SC-06 compliance checklist
- **No** folder trees, schemas, or physical files in planning pack unless separately authorized

---

## Planning Dependencies

Следующие **принятые** артефакты **сдерживают** RT-G04 planning. Planning **не может** нарушить их ownership rules.

### Tier 0 — Decision and review chain

| Document | Constraint on RT-G04 planning |
|----------|------------------------------|
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | **This document** — artifact class B, MARS locus, no HG/app/DB |
| [WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md) | TR-01…TR-10, TX-01…TX-08, DF checklist, risk matrix |
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C2–C9 capability floor; MVP success S1–S9; scope creep guards SC-* |
| [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md) | RT-G04 first; dependency graph; MVP vs post-MVP classification |

### Tier 1 — Operational doctrine

| Document | Constraint |
|----------|------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | Human-operated v1; single operator; no storage in doctrine |
| Playbook 01 — [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Manifest-enrolled path; file **не** блокирует enrollment ritual |
| Playbook 02 — [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Catalog enrollment declared; portfolio in MVP mission |
| Playbook 03 — [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Eight questions session; no UI in playbook |
| Playbook 04 — [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | DA-01 operator sole declarer; writes reflected in indexes |
| Playbook 05 — [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Terminal outcomes persistable in bound records |

### Tier 2 — Post-Engine charters (ownership rules)

| Document | Constraint |
|----------|------------|
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Manifest **≠** storage (MAP-01); OQ-M04 co-location OPEN |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Registry **≠** database (RAP-01); OQ-R01 index shape OPEN; RAP-11 Site Type vs Factory Registry |
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Surface **≠** UI **≠** storage; eight SRDY-* classes; read-only semantics |

### Tier 3 — Engine boundary (hard limits)

| Document | Constraint |
|----------|------------|
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04; persistence **external** to Engine; forbidden conflation docs |
| Engine Stages 1–6 | Logical models authoritative; RT-G04 **serializes**, не переопределяет |
| [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) | RT-G04 gap definition; RT-G10/05/12 depend on substrate |

### Tier 4 — MARS context (placement awareness)

| Corpus | Rule |
|--------|------|
| `workspaces/website-factory-reference-v1/` | Canonical doctrine + Engine; primary candidate zone for records |
| `projects/mars-website-factory/` | Operational pack v0 — **не** supersede v1 canon without routing |
| `workspaces/*` client pilots | External pointers; **не** Factory SoT by default |

---

## Pending Owner Decisions

Решения, **ещё требующие** owner attention **после** TOPOLOGY-B-v1. Marker **ОБРАТИ ВНИМАНИЕ — ТЫ НУЖЕН** используется **только** если решение блокирует немедленный следующий шаг.

### Resolved by TOPOLOGY-B-v1 (не pending)

- **DF-01** — MARS monorepo locus
- **DF-02** — structured artifacts class
- **DF-06** — no HomeGateway SoT (default)
- **E** standalone app — rejected
- **D** HomeGateway-integrated — rejected

### Pending — addressable inside RT-G04 planning workshop

| ID | Decision | Urgency | Notes |
|----|----------|---------|-------|
| **DF-03** | Canon vs operational pack vs new root for Factory records zone | **Before RT-G04 charter authorization** | OQ-OM01, OQ-OM06; planning **may** recommend default |
| **DF-04** | Manifest vs tracking co-location | Planning workshop | OQ-M04 |
| **DF-05** | Registry central catalog vs distributed + aggregator | Planning workshop | OQ-R01 |
| **DF-07** | RT-G12 read surface form factor | Planning workshop | Must respect TX-07 (no dashboard product) |
| **DF-08** | Pilot workspace pointer policy | Planning workshop | Triumph/external workspaces |
| **DF-09** | Network/hosting beyond local git | Low for MVP | Single-machine sufficient |
| **DF-10** | Git versioning policy for SoT records | Planning workshop | Audit vs privacy tradeoff |

### Pending — post-MVP or non-blocking

| Topic | Notes |
|-------|-------|
| OQ-R02 Registry card field template | Near-MVP; reduces registry impl ambiguity — **not** topology blocker |
| ATLAS consumer alignment | Future; MVP excludes MIG/MetaBOT/ORCA integrations |
| HomeGateway read-only consumer | **Optional future** — **not** MVP requirement |

### Immediate owner attention required?

**No.** TOPOLOGY-B-v1 resolves sufficient constraints для **старта RT-G04 Planning**. **DF-03** и производные **DF-04…DF-10** — workshop questions; **не** требуют отдельного owner session **до** начала planning track.

---

## RT-G04 Readiness

| Question | Assessment |
|----------|------------|
| Topology decision recorded? | **Yes** — TOPOLOGY-B-v1 |
| DF-01 + DF-02 resolved? | **Yes** |
| DF-03 blocking **planning start**? | **No** — blocks **charter authorization**, not planning workshop |
| RT-G04 implementation started? | **No** — correctly NOT STARTED |
| RT-G04 **Planning** may begin? | **Yes** |
| RT-G04 **charter authorization** may begin immediately? | **Partial** — planning workshop first; charter sign-off waits DF-03 resolution **minimum** |
| Physical MVP artifacts required for planning? | **No** — explicitly forbidden |

### Readiness verdict

**RT-G04 Planning — AUTHORIZED TO START** after this decision record.

**RT-G04 charter authorization — NOT YET**; requires RT-G04 Planning workshop outputs + **DF-03** placement resolution (recommendation or owner confirm).

### What planning may do now

- Use Q1–Q16 from [RT-G04 Planning Implications](#rt-g04-planning-implications)
- Apply TR/TX constraints from Deployment Topology Review
- Sequence against Implementation Planning dependency graph
- Prepare charter **role/boundaries/non-goals** text — **without** schemas, folders, or sample files

### What planning must not do now

- Create Factory MVP folder structure
- Create manifest/registry/tracking physical files
- Select JSON/YAML/SQLite or field lists
- Design database, runtime, UI, automation, or queue
- Modify accepted architecture except status/cross-reference if strictly necessary

---

## Explicit Non-Claims

This decision record **does not** claim:

- Any **physical MVP folders**, manifest files, registry indexes, or tracking stores **were created**.
- Any **storage schema**, file format, folder layout, YAML, JSON, or database design **was defined**.
- RT-G04/05/10/12 **implementation** is complete, started, or charter-authorized.
- A shipped Website Factory **runtime**, workflow engine, validator engine, persistence **product**, or operator UI **exists** or **was designed**.
- **HomeGateway** is ready as Factory host — remains **SAFE UNKNOWN**.
- **DF-03** placement zone **was selected** — only MARS repo locus + structured class.
- MVP **has been built** or **demonstrated** on pilot case.
- Operators updated NEXT-PRIORITIES to RT-G04 planning era — **UNKNOWN**.
- Any accepted artefact was modified — **decision record only**.

This decision record **does** claim:

- Owner selected **B — Filesystem + structured artifacts** inside **`X:\AI MARS`**.
- **DF-01**, **DF-02**, **DF-06 (default)** are **resolved**.
- Rejected for MVP: **A** (markdown-only), **C** (broad MARS surface), **D** (HomeGateway), **E** (standalone app).
- Topology **does not imply** database, runtime, app, automation, queue, or HomeGateway dependency.
- **RT-G04 Planning may start**; charter authorization follows planning + DF-03.

---

## Recommended Next Step

**Authorized next track:** **RT-G04 Persistence Substrate — Planning v1** (planning workshop only).

Suggested sequencing:

1. **Open RT-G04 planning workshop** using Q1–Q16 and Planning Dependencies tables above.
2. **Resolve DF-03** (Factory records zone within MARS) as **first planning deliverable** — recommendation for owner confirm, not silent default.
3. **Draft RT-G04 charter** (role, boundaries, non-goals) **within** TOPOLOGY-B-v1 constraints — **no** physical artifacts.
4. **Gate charter authorization** on DF-03 confirm + SC-01/SC-03/SC-06 checklist pass.
5. **Only after RT-G04 charter authorization** — proceed to RT-G10/05/12 **implementation planning** charters (still not implementation).

**Not recommended:** parallel physical MVP folder creation, schema drafting, or RT-G10/05/12 implementation before RT-G04 charter.

---

*Website Factory MVP Topology Decision v1 — owner decision + RT-G04 planning preparation only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md`. Git: no commit, no push.*

---

# REPORT — Website Factory MVP Topology Decision v1
