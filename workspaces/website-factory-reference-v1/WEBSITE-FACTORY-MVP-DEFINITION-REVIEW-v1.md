# REPORT — Website Factory MVP Definition Review v1

**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `projects/mars-website-factory/` (операционный пакет, не замена канона)  
**Тип:** MVP definition review only — **без** implementation plans, runtime design, storage design, schemas, UI design, automation plans  
**Метод:** синтез принятых артефактов (Implementation Planning Review, Operational Design Consolidation Review, Operational Model, charters, Playbooks 01–05) в каноническую границу MVP  
**Принятая реальность (контекст задачи):** Foundation Era **COMPLETE**; Factory Engine Architecture **COMPLETE**; Post-Engine Doctrine **COMPLETE**; Governance Synchronization **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning Review **COMPLETE**; runtime / storage / automation **отсутствуют**

---

## Executive Summary

**Вердикт:** Канонический MVP Website Factory определён как **минимальная физическая привязка** трёх doctrinal planes — **Manifest**, **Registry**, **Tracking Surface** — для **одного human operator** и **Core 5** production path, **без** автоматизации мутации Engine indexes и **без** shipped Factory runtime / workflow engine.

**MVP существует, чтобы закрыть один конкретный пробел:** сегодня Factory **уже работает** documentation-first (Playbooks 01–05 полностью исполнимы без файлов на диске); MVP **не доказывает** новую doctrine и **не создаёт** orchestration — MVP **доказывает**, что operator может вести тот же human-operated path с **авторизованной канонической привязкой** вместо ad-hoc scatter по workspace.

**MVP must include (capability-level):**

| Plane | MVP capability |
|-------|----------------|
| Persistence substrate | Единый физический слой для Factory Project records (RT-G04) |
| Manifest binding | Per-project entry anchor + minimum understanding categories (RT-G10 impl) |
| Registry binding | Portfolio catalog с указателем на Manifest (RT-G05 impl) |
| Surface binding | Operator read path для восьми visibility questions (RT-G12 impl) |
| Manual declaration path | Operator остаётся единственным declarer; writes — human/assisted, не automated |

**MVP must exclude:** workflow engine, agents, automation of state/gate mutation, validator CLI product, queue, multi-operator concurrency, Engine runtime product, layer generation automation, extended site types без blueprint parity.

**MVP success:** один Core 5 pilot case проходит полный operator path (Playbooks 01→02→03↔04→05) с bound Manifest + Registry + Surface visibility **без workspace archaeology** и **без** workflow engine.

**MVP completion:** все must-include capabilities продемонстрированы на pilot case; explicit non-claims сохранены; scope creep items отсутствуют — **без** runtime metrics как условия закрытия.

**Рекомендация:** MVP scope **готов к authorization** как единая граница перед любыми implementation charters (RT-G04/10/05/12 planning pack — **следующий** authorized track, **не** часть этого deliverable).

---

## MVP Purpose

### Зачем существует MVP

MVP Website Factory — **не** «первая версия Factory runtime» и **не** proof-of-concept automation. MVP — **минимальный capability closure** между:

- **Сегодня:** doctrine-complete, human-operated Factory path **исполним полностью** по документации (Operational Design Consolidation Review: «Core Operational Design документарно завершён»).
- **Цель MVP:** operator **не зависит** от археологии workspace, ad-hoc markdown indexes и implicit discipline для Manifest entry, portfolio discoverability и Surface visibility.

MVP **материализует** то, что charters уже определили **логически**, но **не физически** (RUNTIME-GAPS: RT-G04/05/10/12 — **NOT STARTED**).

### Какой вопрос MVP должен ответить

| Вопрос | MVP ответ |
|--------|-----------|
| Может ли один operator вести Factory Project с **канонической** точкой входа, portfolio visibility и operational depth **без** shipped orchestrator? | **Да** — если bound planes работают |
| Достаточна ли принятая doctrine stack для **physical binding** без новой architecture? | **Да** — Implementation Planning Review подтвердил |
| Можно ли завершить Core 5 pilot от recognition до Factory-terminal closure **только** human declarations + bound visibility? | **Да** — success criterion |

### Что MVP **не** пытается доказать

| Не доказывается | Почему вне MVP |
|-----------------|----------------|
| Factory runtime / workflow engine жизнеспособен | RT-G01/G09 — post-MVP, highest risk |
| Automation, agents, CI могут **мутировать** Engine indexes | Противоречит DA-01, OA-ACT-04, Engine ES-04 |
| Validators **заменяют** operator gate declarations | RT-G11 — post-MVP; риск authority drift |
| Multi-operator, queue, concurrency | RT-G06/G14 — не single-operator MVP |
| Layer artefact production автоматизирована | GG-* — отдельный product plane |
| Extended site types (SAAS, MARKETPLACE, …) | Architecture charter work — не Core 5 |
| MIG / MetaBOT / ORCA интеграции закрыты | RT-G08 — integration territory |
| Deploy, hosting, client go-live | Post-Factory; `COMPLETE` ≠ deploy |
| «Hands-off factory» как продукт | Explicit misread per Operational Model |

**MVP purpose statement:** MVP доказывает, что **human-operated Factory v1** может опираться на **авторизованную physical binding** Manifest + Registry + Surface для одного operator — **не** что Factory стала autonomous system.

---

## MVP Capabilities

Минимальный capability set — **принципы**, не implementation design.

### Must exist for MVP

| # | Capability | Principle | Doctrine / gap anchor |
|---|------------|-----------|------------------------|
| C1 | **Factory Project existence** | Logical Factory Project может быть Factory-scoped, manifest-enrolled и отличим от raw workspace | Playbook 01; Object Model EO-05 |
| C2 | **Persistence substrate** | Существует **один** authorized physical layer для Factory Project records operator может читать и **вручную** обновлять | RT-G04 |
| C3 | **Manifest persistence** | Per-project **entry anchor** + **minimum understanding categories** (MRDY-*) сериализованы и стабильны для case | RT-G10 impl; Manifest Charter |
| C4 | **Registry visibility** | Portfolio catalog перечисляет enrolled Factory projects, distinction summaries, pointer to Manifest entry | RT-G05 impl; Registry Charter; Playbook 02 |
| C5 | **Tracking visibility** | Operator может ответить на **все восемь** Surface visibility questions из bound data **без** полного workspace search | RT-G12 impl; Surface Charter SRDY-*; Playbook 03 |
| C6 | **Manual declarations** | Playbook 04 declarations **отражаются** в persisted indexes через operator-controlled write path — **не** automated gate evaluation | Playbook 04 DA-01; Engine indexes |
| C7 | **Closure persistence** | Factory-track terminal outcomes (Playbook 05) **могут быть зафиксированы** в bound records | Playbook 05; OCM-* |
| C8 | **Single-operator scope** | Один Factory operator, один logical portfolio scope (single-machine / single-repo discipline) | Operational Model OR-*; OA-ACT-01 |
| C9 | **Core 5 constraint** | Pilot и MVP demonstration ограничены Core 5 site classes с принятыми blueprints | OR-06; Foundation freeze |

### May exist for MVP (optional, not blocking)

| Capability | Status in MVP | Notes |
|------------|---------------|-------|
| Registry enrollment | **May** — doctrine optional (Playbook 02 RD-04), **MVP mission includes** portfolio for single operator managing cases | Implementation Planning Review: catalog **in MVP scope** |
| Declaration/session record persistence | **May** — operable manually pre-impl; **near-MVP** if bound early | Supports Surface recency class (SRDY-07) |
| Registry index card field template (OQ-R02) | **May** — reduces ambiguity; workflows operable without | Operational gap OD-01 — MEDIUM, not blocking |
| Lightweight assisted write (non-mutating helpers) | **May** — if **never** replaces operator declaration authority | Read-only advisors OK per RUNTIME-ROADMAP R6 |
| v0↔v1 routing discipline | **May** — hygiene for dual corpus | OQ-OM06 — not MVP core |

### Capability dependency (planning-level, not design)

```text
  C2 Persistence substrate (RT-G04)
           │
           ▼
  C3 Manifest binding (RT-G10 impl)
           │
           ├──▶ C4 Registry binding (RT-G05 impl)
           │
           └──▶ C5 Surface binding (RT-G12 impl)
                     ▲
                     │
           C6 Manual declarations (Playbook 04 writes)
                     │
                     ▼
           C7 Closure persistence (Playbook 05)
```

**MVP capability floor:** без C2–C5 MVP **не существует** как отличимый от documentation-first baseline. C6–C7 **завершают** lifecycle honesty; C8–C9 **ограничивают** scope.

---

## MVP Operator Model

### Кто использует MVP

| Actor | MVP role | MVP assumption |
|-------|----------|----------------|
| **Factory operator** | Primary — единственный обязательный actor для declarations, enrollment, supervision, closure | **One** human operator per MVP demonstration |
| **Reviewer / validator** | Optional input evidence — **не** authoritative declarer | Same as doctrine v1 |
| **Layer specialist** | Produces layer bodies external to Factory SoT | Unchanged from Operational Model |
| **External systems** (Git, CI, Cursor, MIG) | Execution surface — **never** mutates indexes without operator act | Unchanged |

### Сколько operators MVP предполагает

**Ровно один Factory operator** как normative MVP assumption:

- Нет RBAC, permissions, tenant isolation (explicitly out of Charter 01).
- Нет concurrency rules, locking, queue scheduling (RT-G06/G14 deferred).
- Portfolio catalog serves **one operator managing one or few projects** — not enterprise multi-team ops.

Multi-operator expansion — **post-MVP** charter territory.

### Какой operational path MVP поддерживает

Normative steady-state path (unchanged from Operational Design):

```text
  PRE-FACTORY
       │
       ▼
  [01] Recognition + Manifest enrollment ──▶ manifest-enrolled
       │                                      (+ C3 physical binding)
       ├── [02] Registry enrollment ──▶ catalog-discoverable
       │                                 (+ C4 physical binding)
       ▼
  [03] Tracking Surface sessions (repeat) ◀──┐
       │         (+ C5 read surface)          │
       ├── [04] Declarations (repeat) ────────┘
       │         (+ C6 manual index writes)
       ▼
  [05] Closure ──▶ Factory-terminal metadata
                   (+ C7 closure persistence)
```

**Operator visibility path (MVP):**

```text
  Registry (portfolio) → Manifest (entry) → Surface (eight questions)
```

**Movement model:** declared, not executed — operator declares; MVP **persists and displays**, **не** evaluates gates or executes transitions.

**Pilot constraint:** LANDING / CORPORATE / ECOMMERCE / PORTFOLIO / SERVICE (Core 5) — extended types **invalid** for MVP demonstration.

---

## MVP Lifecycle Coverage

### MUST be supported (MVP lifecycle floor)

| Stage | Required capability | MVP support mechanism | Simplification allowed? |
|-------|---------------------|----------------------|-------------------------|
| **Recognition** | Factory-scoped production case | Playbook 01 + C1 | No |
| **Manifest enrollment** | MRDY-* categories explicit | Playbook 01 + C3 | No — doctrinal + physical |
| **Portfolio visibility** | Discover enrolled projects | Playbook 02 + C4 | Card template (OQ-R02) may be informal |
| **Supervision** | Session discipline, blockers, next actions | Playbook 03 + C5 | Session cadence — operator convention |
| **Declaration** | Operator-declared Engine truth | Playbook 04 + C6 | Evidence bundle formality — operator convention |
| **Mid-track movement** | States, gates, handoffs via 03↔04 cycle | C5 + C6 | No dedicated «movement playbook» — by design |
| **Closure** | Terminal / partial / suspended outcomes | Playbook 05 + C7 | Reconciliation path may require extra 04 acts |

### MAY be simplified for MVP

| Stage / aspect | Simplification | Boundary |
|----------------|----------------|----------|
| Registry enrollment | Faster card without OQ-R02 template | Must still satisfy RRDY-* categories |
| Surface recency class | Manual session notes until declaration persistence | Must not fake SRDY-07 |
| Layer production coordination | External workspace refs only | Factory indexes refs — not bodies |
| Legal parallel track | Single-operator manual co-track | No automated legal gate product |
| Evidence attestation carrier | REPORT vs index-only (OQ-PD05) | Operator convention — not blocking MVP |

### Explicitly deferred (NOT in MVP lifecycle)

| Deferred stage / capability | Deferred to |
|------------------------------|-------------|
| Automated state transition execution | RT-G01 workflow engine |
| CI/git-triggered gate PASS | RT-G03 automation |
| Validator-enforced gate blocking | RT-G11 |
| Queue-based multi-project scheduling | RT-G06 |
| MIG incoming → Factory intake standard | RT-G08 / OQ-OM08 |
| External approval webhooks | RT-G13 |
| Rollback cascade automation | RT-G15 |
| Frontend site generation automation | GG-03 |
| Deploy / go-live as Factory state | Post-Factory |

**Lifecycle verdict:** MVP **must** cover recognition → closure **полностью** на human-operated path. MVP **must not** add lifecycle stages beyond accepted doctrine. MVP **may** simplify **formality**, not **authority** or **stage existence**.

---

## MVP Exclusions

### Must NOT exist for MVP

| Exclusion | Rationale | Violation signal |
|-----------|-----------|------------------|
| **Workflow engine** (RT-G01) | Highest ordering risk; contradicts human-operated MVP | Transitions execute without Playbook 04 operator act |
| **Agent execution** (RT-G02) | No AI orchestration in Factory v1 scope | Agent declares gate PASS |
| **Automation mutating indexes** (RT-G03) | Violates operator-declared truth model | CI/n8n writes Engine outcomes |
| **Queue system** (RT-G06) | Multi-project scheduling beyond single operator | Priority queue product shipped |
| **Validator CLI as gate authority** (RT-G11) | Conflates validation PASS with operator declaration | Validator output = gate index |
| **Engine runtime product** (RT-G09 impl) | Distinct from documentation-complete Engine | «Shipped Factory runtime» narrative |
| **Multi-operator concurrency** (RT-G14) | Not single-operator MVP | Locking / RBAC required for MVP demo |
| **Rollback automation** (RT-G15) | Cascade scripts — post human-operated MVP | Automated cascade invalidation |
| **MIG execution binding** (RT-G08) | External pipeline — not Factory SoT | MIG mutates Factory indexes |
| **Notification / webhook gates** (RT-G13) | External integrations | Approval webhooks as authority |
| **Layer generation automation** (GG-03, GG-07) | Separate product plane | MVP ≠ site builder |
| **Operator dashboard product / SaaS** | MVP = minimum read binding only | Full UX program masquerading as RT-G12 |
| **Database / multi-tenant storage as requirement** | File-backed single-operator sufficient for MVP | DB chosen before MVP charter |
| **Extended Type blueprints** | No architecture parity | SAAS/MARKETPLACE pilot in MVP |
| **Redesign Foundation / Engine / Playbooks** | Forbidden by task charter | Any doctrine rewrite in MVP track |

### Architectural anti-patterns explicitly forbidden in MVP

| Anti-pattern | Charter anchor |
|--------------|----------------|
| Manifest owns live gate index | MT-01, MAP-05 |
| Registry substitutes Tracking depth | RA-05, RAP-05 |
| Surface authorizes transitions | Surface charter — read-only visibility |
| Registry enrollment by git folder scan | RAP-10, RD-04 |
| Site Type Registry confused with Factory Project Registry | RAP-11 |
| `COMPLETE` treated as deploy authorization | OCM-*, Operational Model exit table |

### What «no runtime» means for MVP

MVP **may include** minimal persistence and read binding — это **implementation**, не «Factory runtime product». MVP **must not** ship orchestrator, workflow engine, or autonomous execution layer. Фраза «without runtime» в контексте задачи = **without Factory runtime product (RT-G09/G01)**, **not** «without any persisted bytes on disk».

---

## MVP Success Criteria

Success criteria — **evidence-based**, **без** runtime metrics, **без** implementation specs.

### Primary success evidence

| # | Criterion | Evidence (what proves it works) |
|---|-----------|----------------------------------|
| S1 | **One Core 5 pilot** completes full operator path | Playbooks 01→02→03↔04→05 executed with bound artefacts |
| S2 | **Manifest-enrolled** with persisted entry anchor | Operator identifies **one canonical** entry point per project (C3) |
| S3 | **Catalog-discoverable** in portfolio | Operator finds project in registry **without** opening each workspace (C4) |
| S4 | **Eight Surface questions answerable** | Operator completes Playbook 03 session using read surface — **not** full-repo search (C5) |
| S5 | **Declarations reflected** | Playbook 04 acts visible in persisted indexes; Tracking/Surface show updated truth (C6) |
| S6 | **Closure persistable** | Playbook 05 terminal outcome recorded referencing bound records (C7) |
| S7 | **No workflow engine required** | Entire pilot path completed with human declarations only |
| S8 | **Authority preserved** | No automated system declared gate PASS or state transition |
| S9 | **Explicit non-claims intact** | No false «shipped Factory runtime» or «automation exists» narrative |

### Secondary success signals (supporting, not sufficient alone)

| Signal | Notes |
|--------|-------|
| Operator time-to-orient reduced vs ad-hoc baseline | Qualitative — not a metric gate |
| Second project enrollable without rework of substrate | Validates C2 generality |
| Reconciliation declaration (Playbook 04) recoverable from bound data | Integrity path works |
| Registry withdrawal orthogonal to Engine closure demonstrated | CL-03 / CC-03 honored |

### What does NOT count as MVP success

| Non-success | Why |
|-------------|-----|
| Documentation-only operation without physical binding | That is **pre-MVP baseline** — already works |
| Validator CLI shipped | Post-MVP |
| Automated CI gate pipeline | Scope creep |
| Frontend site deployed | Post-Factory |
| Global layer ACCEPTED (T5) for all 14 layers | Global register — not per-project MVP |
| Triumph/pilot workspace deploy-authorized | **SAFE UNKNOWN** — separate case charter |

---

## MVP Completion Criteria

MVP **declared complete** when capability floor met and exclusions verified — **without** runtime metrics as hard gates.

### Completion checklist (normative)

| # | Completion condition | Verification method |
|---|---------------------|---------------------|
| M1 | All **must-exist** capabilities C1–C9 **demonstrated** on at least one Core 5 pilot | Operator walkthrough evidence |
| M2 | Dependency order respected: substrate → manifest → registry → surface | No surface-before-manifest violation |
| M3 | Full lifecycle Playbooks 01–05 **executable** with bound planes | End-to-end pilot narrative |
| M4 | All **must NOT exist** exclusions **absent** from MVP deliverable set | Scope audit |
| M5 | Explicit non-claims document **published and honored** | No runtime/automation false claims |
| M6 | Authority model unchanged: operator sole declarer | DA-01 / OA-ACT-01 preserved |
| M7 | No HIGH scope creep items merged into MVP | Scope creep review pass |
| M8 | MVP boundary **handed off** to post-MVP charter queue with clear separation | Post-MVP boundary acknowledged |

### Completion is NOT conditioned on

| Not required for MVP complete | Reason |
|-------------------------------|--------|
| Production uptime SLA | No runtime product |
| Performance benchmarks | Out of scope |
| Multi-operator pilot | Post-MVP |
| OQ-R02 card template finalized | Optional binding |
| NEXT-PRIORITIES register updated | Hygiene — recommended, not completion gate |
| All OPEN questions (OQ-*) resolved | Bounded UNKNOWN acceptable |
| Second pilot case | One demonstration sufficient |
| Implementation charters for post-MVP gaps | Separate authorization |

### MVP complete vs MVP successful

| Term | Meaning |
|------|---------|
| **MVP successful** | Pilot evidence satisfies S1–S9 |
| **MVP complete** | Organization declares MVP **closed** — capability floor shipped, exclusions verified, post-MVP boundary active |

MVP may be **successful** before organizational **completion** declaration if evidence exists but governance handoff pending — operator choice.

---

## Scope Creep Review

### Major scope creep risks (HIGH)

| Risk | Description | Classification | Guard |
|------|-------------|----------------|-------|
| **SC-01** | MVP persistence conflated with «shipped Factory runtime» | **HIGH** — premature runtime narrative | Preserve explicit non-claims; MVP ≠ RT-G09 |
| **SC-02** | RT-G12 before RT-G10/04 stable | **HIGH** — ordering violation | Enforce C2→C3→C4→C5 dependency |
| **SC-03** | Validators/CI replace Playbook 04 declarations | **HIGH** — authority drift | Defer RT-G11; DA-01 non-negotiable |
| **SC-04** | Workflow engine «just for convenience» | **HIGH** — recreates automation debt | RT-G01 forbidden in MVP |
| **SC-05** | Registry dashboard with seven/eight tracking questions | **HIGH** — RA-05 violation | Registry = catalog only; Surface = depth |

### Medium scope creep risks

| Risk | Description | Guard |
|------|-------------|-------|
| **SC-06** | RT-G04 charter smuggles storage design into doctrine | Separate implementation charter |
| **SC-07** | Over-built dashboard vs minimum read surface | RT-G12 = visibility binding, not UX program |
| **SC-08** | Extended type pilot before blueprint charter | Core 5 only |
| **SC-09** | Dual corpus v0/v1 ID mixing during binding | OQ-OM06 routing before agent-assisted work |
| **SC-10** | Declaration persistence merged into workflow product | Persistence supports rituals — does not auto-execute |

### Low scope creep risks (still watch)

| Risk | Notes |
|------|-------|
| **SC-11** | OQ-R02 card template treated as MVP blocker | Optional — do not expand MVP waiting for template |
| **SC-12** | MIG intake binding pulled into MVP | OQ-OM08 — integration charter |
| **SC-13** | Gate sign-off micro-playbook added to MVP | LOW — Playbook 04 sufficient |
| **SC-14** | Execution logs (RT-G07) bundled «since we have storage» | Post-MVP natural successor |

### Scope creep decision rule

**Any addition is scope creep if it:**

1. Mutates Engine indexes without Playbook 04 operator act.
2. Introduces orchestration, queue, or multi-operator requirements.
3. Redefines Manifest / Registry / Surface authority boundaries.
4. Expands beyond Core 5 without architecture charter.
5. Claims MVP **is** Factory runtime product.

**Safe additions (not creep):** hygiene docs, explicit non-claims, operator acknowledgment, NEXT-PRIORITIES sync, read-only advisors that **never** write indexes.

---

## Post-MVP Boundary

### Immediately after MVP (Tier 1 — natural successors)

Authorize via **separate** implementation charters — not bundled into MVP closure.

| Item | Why post-MVP | Relationship to MVP |
|------|--------------|---------------------|
| **RT-G07** Execution logs | Machine-readable audit trail after persistence stable | Builds on C2 |
| **RT-G11** Validator CLI | Wires layer validators; gate **aid**, not authority | Risk if conflated with DA-01 |
| **Declaration/session automation helpers** | Mutation helpers → RT-G03 territory | Read-only advisors OK earlier |
| **OQ-R02** registry card template | Reduces friction | MVP operable without |
| **OQ-OM06** v0↔v1 routing card | Dual corpus hygiene | Parallel to MVP |
| **OQ-OM08** MIG intake binding | External pipeline integration | RT-G08 |

### Runtime territory (Tier 2 — high risk / high scope)

| Item | Notes |
|------|-------|
| RT-G01 Workflow engine | Charter last per RUNTIME-GAPS |
| RT-G03 Automation / n8n | Only with strict non-mutation or operator-in-loop charter |
| RT-G06 Queue | Multi-project scheduling |
| RT-G08 MIG execution | Execution binding |
| RT-G09 Engine runtime product | Distinct from MVP physical binding |
| RT-G13 Webhooks / external approval | External integrations |
| RT-G14 Concurrency rules | Multi-operator |
| RT-G15 Rollback automation | Cascade scripts |
| GG-03 Frontend generation automation | Site generation product |
| GG-07 Orchestration | Meta-factory automation |

### Future optional territory (Tier 3 — not immediate post-MVP)

| Item | Notes |
|------|-------|
| Extended Type blueprints | SAAS, WEB_APPLICATION, MARKETPLACE |
| ECOMMERCE legal extension | Beyond frozen Legal Pack |
| Chrome blocks binding | HEADER_NAV, FILTERS, SEARCH |
| Engine v2 / PHASE_SLICE formalization | OQ-S6-03 |
| Unified gate-namespace index | AG-05 optional hygiene |
| Optional micro-playbooks | Gate ritual, registry withdrawal |

**Post-MVP principle:** MVP **closes physical binding gap** for Core 5 single operator; **does not** close automation, multi-project operations, or integration gaps.

```text
  MVP (this review)
       │
       ├── Tier 1: logs, validators, templates, routing, MIG binding
       │
       ├── Tier 2: workflow, automation, queue, runtime product
       │
       └── Tier 3: architecture extensions, integrations, micro-playbooks
```

---

## Canonical MVP Definition

**Website Factory MVP** — минимальная **авторизованная физическая привязка** трёх post-Engine planes (**Manifest**, **Registry**, **Tracking Surface**) поверх единого persistence substrate, позволяющая **одному Factory operator** вести **Core 5** production case от **manifest-enrolled** recognition до **Factory-track closure** по Playbooks 01–05 с **human-operated declarations** как единственным источником обязательной Engine truth — **без** workflow engine, **без** automation мутации indexes, **без** shipped Factory runtime product.

**MVP in one sentence:** Replace ad-hoc workspace scatter with canonical bound Manifest + Registry + Surface visibility for a single human operator — nothing more, nothing less.

### MVP boundary table (canonical)

| Dimension | MVP includes | MVP excludes |
|-----------|--------------|--------------|
| **Purpose** | Prove physical binding suffices for human-operated v1 | Prove automation or runtime product |
| **Actors** | One Factory operator | Multi-operator, RBAC, tenants |
| **Scope** | Core 5 site classes | Extended types without blueprints |
| **Planes** | RT-G04 + RT-G10/05/12 impl | RT-G01/02/03/06/08/09/11/13/14/15 |
| **Lifecycle** | Playbooks 01–05 full path | New stages, automated movement |
| **Authority** | Operator declares (Playbook 04) | CI/agents/validators as declarer |
| **Visibility** | Eight Surface questions via read binding | Dashboard product, Registry as tracking |
| **Persistence** | Substrate + manifest + catalog + indexes | DB/multi-tenant as MVP requirement |
| **Completion** | Demonstrated pilot + exclusions verified | Uptime metrics, production SLA |

### MVP vs adjacent concepts

| Concept | Relation to MVP |
|---------|-----------------|
| **Documentation-first Factory (today)** | Pre-MVP baseline — MVP **adds** physical binding |
| **Operational Design complete** | Prerequisite — **not** replaced by MVP |
| **Implementation Planning Review** | Predecessor — MVP Definition **narrows** to canonical boundary |
| **MVP Implementation Planning charters** | Successor — **how** to bind (still not this doc) |
| **Factory runtime product** | Post-MVP — **not** MVP |

---

## Explicit Non-Claims

This review **does not** claim:

- Any **implementation spec**, storage model, UI design, schema, file format, folder layout, or code was created.
- A shipped Website Factory **runtime**, workflow engine, validator engine, persistence layer, or operator UI **exists** or **was designed** in this deliverable.
- MVP **has been built**, **implemented**, or **demonstrated** — only **defined**.
- RT-G04/05/10/12 **implementation** is complete or started because this MVP definition exists.
- Physical manifest files, registry index, or declaration store **exist** in-repo.
- Registry enrollment remains **optional** in MVP mission sense — Implementation Planning Review included catalog **in MVP scope** for single-operator portfolio need; doctrine optional flag (Playbook 02) **≠** MVP exclusion.
- `projects/mars-website-factory/` v0 registries supersede `website-factory-reference-v1` v1.
- Extended site types, ecommerce legal extension, or MIG/MetaBOT/ORCA integrations are MVP-ready.
- Operators have updated NEXT-PRIORITIES to MVP or Implementation Planning era (**UNKNOWN** — not verified post-2026-06-05).
- Triumph or pilot workspaces are deploy-authorized or Factory-terminal in production sense.
- Any accepted artefact was modified — **definition deliverable only**.

This review **does** claim (evidence-based):

- MVP scope is **definable without new doctrine** from accepted Implementation Planning Review and Operational Design stack.
- MVP **must include** persistence substrate + Manifest + Registry + Surface binding + manual declaration path for one Core 5 operator.
- MVP **must exclude** workflow engine, automation of index mutation, validator CLI as authority, queue, multi-operator complexity, Engine runtime product, layer generation automation.
- MVP **success** = one pilot completes Playbooks 01–05 with bound planes without workspace archaeology and without workflow engine.
- MVP **completion** = must-capabilities demonstrated, exclusions absent, non-claims preserved — **without** runtime metrics.
- Pre-MVP baseline **already operates** documentation-first; MVP **improves** persistence and visibility — **does not unblock** missing lifecycle doctrine.
- Post-MVP Tier 1 (logs, validators, templates) and Tier 2 (workflow, automation) are **clearly separated** from MVP boundary.

---

*Website Factory MVP Definition Review v1 — scope definition only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md`. Git: no commit, no push.*

---

# REPORT — Website Factory MVP Definition Review v1
