# REPORT — RT-G12 Tracking Surface Implementation Planning Charter v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Planning — **RT-G12 planning charter only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Persistence Substrate Charter **COMPLETE**; RT-G10 Manifest Implementation Planning Charter **COMPLETE**; RT-G05 Registry Implementation Planning Charter **COMPLETE**  
**Тип:** implementation **planning** charter only — **без** implementation, UI design, dashboard design, screen design, storage design, schema design, yaml/json design, folder layout, runtime plan  
**Upstream:** [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md), Operational Playbooks 01–05  
**Связь:** [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G12, [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md)

---

## Purpose

### Зачем существует Tracking Surface implementation (RT-G12)

**RT-G12 Tracking Surface Implementation** — архитектурная **роль физической read binding** доктрины Factory Tracking Surface для **одного** Factory Project. Implementation закрывает capability **C5** (MVP Definition Review) и устраняет gap между **doctrine-complete Surface visibility contract** (Tracking Surface Charter, Playbook 03) и **operator path**, который сегодня зависит от ad-hoc scatter и workspace archaeology для ответа на **восемь** visibility questions без полного обхода repo.

| Операционная проблема | Как RT-G12 implementation решает (на уровне planning) |
|-----------------------|--------------------------------------------------------|
| Surface Charter определяет **классы информации**, которые оператор **должен видеть**, но **не** физический read path | RT-G12 определяет **какие read-binding обязательства** несёт implementation — **не** UI, **не** формат |
| Playbook 03 исполним **логически**, но без bound data operator ищет truth по workspace | RT-G12 связывает doctrinal eight-question session с **stable read composition** поверх substrate RT-G04 |
| Operator не может ответить на все eight questions **из одной авторизованной точки** per project | RT-G12 обязан обеспечить **discoverable per-project read surface** aligned with SRDY-* и Tier S-A/B/C |
| MVP S4 требует eight Surface questions **без full-repo search** | RT-G12 — **minimum read binding** для C5; **не** dashboard product (TX-07, SC-07) |

Tracking Surface implementation — **implementation-plane responsibility** для operator read binding standard **поверх** RT-G04 substrate + RT-G10 manifest anchor (+ optional RT-G05 portfolio drill-down) — **без** переопределения Surface Charter doctrine.

### Нормативная формулировка роли (planning)

**RT-G12 Tracking Surface Implementation** — архитектурная **роль authorized physical read binding** Surface doctrine (eight operator questions, Tier S-A/B/C visibility classes, SRDY-* completeness checks) для одного Factory Project, **вне** Engine documentation boundary и **вне** Tracking composition ownership (Stage 3), **на** RT-G04 Persistence Substrate read feed, **внутри** MVP capability floor (C5) и TOPOLOGY-B-v1 constraints.

RT-G12 **сам по себе не выбирает display product, screen layout или storage product** — он **определяет implementation responsibility** для Surface read binding, которую **следующий** authorized track (implementation charter / standard) **может** материализовать без нарушения TS-*, VP-*, MAP-05, OA-ACT-04, TRK-REL-01.

### Что RT-G12 implementation **не** решает

| Не решает | Владелец / gap |
|-----------|----------------|
| «Что такое Surface» doctrinally — eight questions, tiers, SRDY-* | [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) — **COMPLETE** |
| Tracking zones, composition rules, TC-* trackability | [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) — Stage 3 |
| Где **физически** живут Factory records (locus, zone, P1–P8) | [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) — substrate, не read binding |
| Per-project manifest entry anchor, MRDY-* | RT-G10 Manifest implementation |
| Portfolio catalog listing, RRDY-* | RT-G05 Registry implementation |
| Live gate/handoff/state index **authoritative writes** | Engine Tracking + Playbook 04 on substrate (C6) |
| Movement execution, gate evaluation, automation | RT-G01, RT-G03, RT-G11 — **forbidden in MVP** |
| Surface session ritual, session outcome discipline | Playbook 03 — **doctrine-complete** |
| Declaration acts, progression ledger mutation | Playbook 04 — **separate write plane** |
| Closure terminal metadata **as primary owner** | Playbook 05 + substrate P6 |
| Operator dashboard product, SaaS, widget system | MVP explicit exclusion (TX-07) |

**Planning boundary:** RT-G12 closes **per-project Surface read binding gap** — **не** Factory runtime, **не** persistence substrate charter, **не** tracking engine, **не** UI/UX program.

---

## Foundation Dependencies

Tracking Surface Implementation Planning Charter **наследует** завершённый Engine v1, post-Engine charters, Operational Design, MVP Definition, RT-G04 charter, RT-G10 and RT-G05 planning charters; **не изменяет** Foundation, Runtime, Engine Stages 1–6, Surface Charter, Tracking Model, Manifest/Registry charters, Playbooks 01–05.

### Tier 0 — Decision and review chain

| Document | RT-G12 planning использует |
|----------|---------------------------|
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C5 Tracking visibility; S4 success; dependency C2→C3→C4→C5; read-only Surface semantics |
| [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md) | RT-G12 impl scope; Playbook 03 binding; sequencing after RT-G04/RT-G10 |
| [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) | P4 tracking indexes; Surface read feed; TRK-REL-01 read-only; SRDY-07 recency |
| [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | Manifest anchor prerequisite; TRK-REL-01; no Surface duplication from Manifest |
| [RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | Optional portfolio drill-down; RE-01; registry ≠ Surface depth |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-07 form factor bounded; TX-07 no dashboard product |

### Tier 1 — Surface and Tracking doctrine (authoritative — do not redesign)

| Document | Constraint on RT-G12 |
|----------|------------------------|
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | Eight questions, Tier S-A/B/C, SRDY-*, VP-*, PO-*, STV-*, GV-*, LV-*, EV-*, OA-* — **sole source** of Surface scope |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking zones, Tier A/B/C, seven questions, TC-* — **composition source** RT-G12 **reads**, **does not own** |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Gate visibility boundaries — instance observation only |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | Lifecycle visibility classes — Surface exposes, **does not execute** |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04; Allowed Future Documents — Surface read binding spec |

### Tier 2 — Operational doctrine

| Document | RT-G12 planning использует |
|----------|---------------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; operator path Registry→Manifest→Tracking→Surface; OR-04 per-project path |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — manifest-enrolled precondition; E4 entry anchor |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — optional portfolio select; RE-01 |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — eight questions session; SE-03 read-only; SRDY assessment |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — declarations update indexes Surface **reads** |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — terminal flags visible on Surface; closure metadata on substrate P6 |

### Tier 3 — Neighbor implementation planning (relationship only)

| Charter | Document | RT-G12 boundary |
|---------|----------|-----------------|
| Manifest (RT-G10 planning) | [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | Entry anchor reachable; **no** Manifest depth duplication |
| Registry (RT-G05 planning) | [RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | Portfolio select **optional**; **never** seven/eight questions on catalog |

**Authority precedence:** Foundation Freeze + Engine Readiness Audit → Engine Stages 1–6 → Surface Charter (doctrine) → Tracking Model → Manifest/Registry charters → RT-G04 Substrate Charter → RT-G10/RT-G05 planning charters → **этот planning charter** для RT-G12 implementation responsibility → **будущий** RT-G12 implementation standard **не может** нарушить TS-01, VP-01, MAP-05, OA-ACT-04, TRK-REL-01, RE-01.

---

## Tracking Surface Implementation Responsibility

### Что RT-G12 **must provide** (capability-level)

Implementation responsibility derives **only** from Surface Charter scope (eight questions, Tier S-A/B/C, SRDY-*) and MVP C5 — **без** inventing new doctrine.

| # | Capability | Doctrine anchor | Planning obligation |
|---|------------|-----------------|---------------------|
| IS-01 | **Per-project Surface read binding** — operator can consume eight visibility question classes from **one authorized read path** per Factory Project on RT-G04 substrate | C5; S4; Playbook 03; TS-01 | Operator answers eight questions **without** full workspace search when indexes exist |
| IS-02 | **SRDY-* completeness binding** — read path **must** expose or explicitly signal empty-allowed Tier S-A classes per SRDY-01…09 | SRDY-*; Surface §Completeness | Physical bind **implies** observability contract testable — not silent omission |
| IS-03 | **Question #1 — Project orientation read** | PO-*, Tier S-A identity/charter/scope/endpoint | Identity ref, charter summary, scope tier, endpoint, mask — **operational depth**, not Manifest essay |
| IS-04 | **Question #2 — Current position read** | STV-01, SV-*, LC active segment | Active state (one), LC label, halt/suspension — invalid flagged (VP-04) |
| IS-05 | **Questions #3–#4 — Blocking and completion read** | GV-*, SHV-*, eligibility snapshot | Open blocker summary, completion prefix, gate/handoff index presence |
| IS-06 | **Question #5 — Remaining work read** | LPC-03, scope mask, artefact gaps | Remaining picture **to declared endpoint** — derived, not invented |
| IS-07 | **Question #6 — Recent narrative read** | EV-*, Tier S-A recency marker | Progression ledger tail or explicit «no declarations yet» (SRDY-07) |
| IS-08 | **Question #7 — Forward eligibility read** | Derived eligibility, OA-01 | Next segment or blocked-with-cause — **enables** declaration decision, **does not** execute |
| IS-09 | **Read-only semantics** | TRK-REL-01; SE-03; OA-ACT-04 | RT-G12 **never** writes authoritative Engine indexes |
| IS-10 | **Composition without authority merge** | VP-01, TV-01, TS-03 | Compose Tier S-A + available Tier S-B from Tracking zones — **pointers only** to T1/Runtime bodies |
| IS-11 | **Anti-pattern guards carried forward** | MAP-05, MT-01, TS-01 | **Reject** second Surface SoT, live gate index duplicate, Passport, manifest-as-tracking-dump |
| IS-12 | **Optional portfolio entry assist** (planning-bound) | RE-01; Playbook 03 ST-03 | **May** consume RT-G05 catalog for project select — **must not** answer eight questions at portfolio level |

**Planning rule SI-01:** если отсутствие physical Surface read binding **ломает** operator ability to satisfy Playbook 03 post-MVP success (S4), MVP C5, или eight questions **without workspace archaeology** при наличии persisted indexes — obligation **входит** в RT-G12 responsibility scope.

### Что RT-G12 **must not provide** (remains outside)

| Outside RT-G12 | Actual owner |
|----------------|--------------|
| Persistence substrate locus, P1–P8 substrate classes **as substrate design** | RT-G04 charter + RT-G04 implementation track |
| Per-project manifest binding, MRDY-* serialization | RT-G10 implementation |
| Portfolio catalog binding, RRDY-* | RT-G05 implementation |
| Tracking composition rules, zone ownership, TC-* evaluation | Tracking Model (Stage 3) |
| Engine instance index **authoritative writes** | Playbook 04 on substrate P4/P5 |
| Gate/handoff **criteria**, Runtime vocabulary definitions | Runtime + Foundation |
| Surface session workflow steps, session outcome ritual | Playbook 03 |
| Automated Surface sync as authoritative SoT | Forbidden — OQ-TS07 bounded |
| UI screens, dashboards, widgets, wireframes, navigation | **Explicitly forbidden** in planning scope |
| Closure metadata **primary** persistence design | Substrate P6; Playbook 05 |
| Layer artefact bodies, handoff payloads | T1 Foundation / external |

**Planning rule SI-02:** RT-G12 defines **Surface read binding responsibility**, not **Tracking composition existence** — logical Tracking indexes precede read bind; empty-allowed early intake **valid** (SRDY-01).

### Doctrine vs physical binding (planning distinction)

| Layer | Status | RT-G12 scope |
|-------|--------|--------------|
| **Doctrinal** Surface visibility contract | Surface Charter — **COMPLETE** | RT-G12 **does not replace** visibility doctrine |
| **Doctrinal** Playbook 03 session | Operational Design — **COMPLETE** | RT-G12 **does not replace** supervision ritual |
| **Physical** Surface read binding | MVP C5 — **NOT STARTED** | RT-G12 **must plan** read rules linking substrate indexes → eight-question answers |
| **Surface-ready (SRDY-*)** | Evaluated per project observability | RT-G12 bind **must enable** SRDY checks when indexes coherent — **not** re-invent trackability rules |

### What must become physically visible vs doctrinal only

| Must become physically visible (via read binding) | Must remain doctrinal only |
|---------------------------------------------------|----------------------------|
| Tier S-A information classes when indexes exist or empty-allowed | Tier S-A **definition** and SRDY pass/fail **semantics** |
| Tier S-B classes when tracking data present | Tier B **optional/deferred rules** (Tracking Model) |
| Explicit «no declarations yet» for SRDY-07 when ledger empty | Event window size policy (OQ-TS01) |
| Integrity warnings (invalid active, stale blocking) when detected | Gate criteria text, failure library bodies |
| Read path discoverability per project after MVP bind | Eight question **wording** and session phase order (Playbook 03) |
| Composition of persisted P4 indexes + manifest pointers | Tracking zone **ownership** rules |

---

## Surface Readiness Binding

SRDY-* concepts govern **doctrinal observability completeness**; RT-G12 planning determines **how readiness relates to implementation** — **without** defining formats, fields, display labels, or storage layouts.

### SRDY → implementation planning mapping

| ID | Doctrinal criterion (Surface Charter) | RT-G12 planning binding rule |
|----|----------------------------------------|------------------------------|
| **SRDY-01** | Tier S-A classes present or explicitly empty-allowed | Read binding **must** surface each S-A class or explicit empty-allowed signal — **not** silent gap |
| **SRDY-02** | Valid active state (or invalid flagged) | Read path **must** show active code or integrity warning — **no** silent normalization (VP-04) |
| **SRDY-03** | Declared endpoint explicit | Read path **must** expose endpoint category from charter/lifecycle bind |
| **SRDY-04** | Blocking summary derivable | Read path **must** compose eligibility + open gate/handoff/halt — may be «none» if eligible |
| **SRDY-05** | Completion picture derivable for reached prefix | Read path **must** expose completed states/gates/handoffs with stale markers visible |
| **SRDY-06** | Remaining picture derivable to endpoint | Read path **must** derive remaining segments/gates/artefacts — **not** invent micro-states |
| **SRDY-07** | Recent event window non-empty or «no declarations yet» explicit | Read binding **must** show declaration recency tail or explicit none — ties substrate P4/P5 audit |
| **SRDY-08** | Forward picture derivable | Read path **must** expose next eligibility or blocked-with-cause |
| **SRDY-09** | No Surface/Manifest/Tracking duplication violation | Read composition **must not** present second live gate/handoff SoT (MAP-05) |

### Readiness relationships (unchanged by planning)

| Concept | Meaning for RT-G12 |
|---------|-------------------|
| **Surface-ready** | Operator can answer eight questions from Surface classes — **target** for read binding fidelity |
| **Surface-ready ⊇ manifest-ready** | Manifest-enrolled **precedes** meaningful Surface depth — RT-G12 **assumes** entry path |
| **Surface-ready ⊄ gate-complete** | Blocked project may be surface-ready (OA-03) — read binding **shows** blockers |
| **Surface-ready ≈ fully trackable** | Typical co-occurrence (TC-* + SRDY-*) — RT-G12 **reads** indexes, **does not** define TC-* |
| **Physical read bind ⊄ surface-ready retroactively** | Indexes may exist before read path — bind **enables** archaeology-free consumption |

### Tier binding (S-A / S-B / S-C)

| Tier | Surface Charter | RT-G12 planning rule |
|------|-----------------|----------------------|
| **S-A — must always be visible** | Surface §Tier S-A | Read binding **must** include all S-A classes or explicit empty-allowed — **core MVP read obligation** |
| **S-B — conditionally visible** | Surface §Tier S-B | Read binding **may** expose when substrate indexes supply data — **must not** fake presence |
| **S-C — must never belong** | Surface §Tier S-C | Read binding **must not** surface Tier C material as Surface core — link-out only if any |

### Principle SRB-01 — Readiness criteria bind; readiness ritual does not move

Playbook 03 **owns** session assessment using SRDY-* as observability lens. RT-G12 **owns** faithful read access to persisted classes — **not** session workflow redesign, **not** automated SRDY pass evaluation as authority.

### Principle SRB-02 — SRDY-07 is the recency hinge

Substrate P4/P5 declaration tail feeds SRDY-07. RT-G12 planning is **incomplete** if recency class read obligation from persisted audit markers is ambiguous (OQ-PD05 bounded for implementation standard).

---

## RT-G04 Relationship

RT-G04 **enables** RT-G12; RT-G12 **consumes** RT-G04 read feed; Surface Charter **neither is nor owns** storage (TS-01).

### Consumption model (planning)

```text
  RT-G04 SUBSTRATE                    RT-G12 SURFACE IMPLEMENTATION
  (persistence locus)                 (read binding responsibility)
         │                                      │
         │  provides P4 tracking indexes        │  defines WHAT eight questions read
         │  P5 declaration writes (read-only)   │  defines read-only composition rules
         │  optional derived SRDY views           │
         │                                      │
         └──────────── feeds ──────────────────▶ Surface read path (C5)
```

| RT-G04 provides | RT-G12 consumes (planning) |
|-----------------|----------------------------|
| Tracking instance records (P4) — state, gates, handoffs, artefact refs | **Primary** read source for questions #2–#8 |
| Declaration writes persistence (P5) | Read-only feed for recent narrative (SRDY-07) |
| Persistent audit markers / recency | Tier S-A last declaration marker |
| Manifest binding carrier (P2) | Entry path integration — **not** owned by RT-G12 |
| Registry catalog carrier (P3) | Optional portfolio drill-down — **not** Surface depth |
| Derived eligibility / SRDY views (optional cache) | Read binding **may** consume — **must not** treat cache as sole SoT if indexes diverge |
| Human-only write path (PS-03) | RT-G12 **excluded** from write path — read-only only (TRK-REL-01) |

### RT-G04 obligations RT-G12 depends on

| Substrate obligation | RT-G12 dependency |
|----------------------|-------------------|
| P4 — Tracking instance records | **Hard** — Surface questions #2–#8 require persisted indexes for MVP demonstration |
| Surface read feed semantics | **Hard** — substrate supplies data; RT-G12 composes for operator |
| SRDY-07 recency persistence | **Near-hard** — manual session notes operable pre-impl; bound recency **required** for S4 honesty |
| P2 — Manifest binding carrier | **Hard** — per-project read path **starts from** manifest anchor (Playbook 03 E4) |
| Read-only Surface semantics (C5) | **Hard** — TRK-REL-01, B-04 |

### RT-G04 forbidden overlap (RT-G12 must respect)

| Forbidden | Reason |
|-----------|--------|
| RT-G12 defining substrate zone structure | RT-G04 charter — DF-03 only |
| RT-G12 owning P4–P6 **writes** | Playbook 04 only — DA-01, OA-ACT-04 |
| RT-G12 choosing persistence product | RT-G04 + topology DF-02 |
| Read binding auto-mutating indexes on read | SC-03, TRK-REL-01 |

### Open co-location (bounded for implementation charter)

| ID | Question | RT-G12 planning disposition |
|----|----------|----------------------------|
| **DF-07** | Read surface form factor (markdown index vs CLI vs static HTML) | **OPEN** — RT-G12 **implementation** standard; **must** respect TX-07 |
| **OQ-PD05** | Declaration/session record binding for SRDY-07 | **OPEN** — cross RT-G04/10/12 implementation planning |

**Principle G04-REL-01:** RT-G04 answers **where** Factory records live; RT-G12 answers **how operator reads** eight Surface question classes from that locus — **orthogonal** planning planes.

**Principle G04-REL-02:** RT-G12 **must not** precede RT-G04 substrate availability and RT-G10 manifest anchor stability for meaningful C5 demonstration (SC-02).

---

## RT-G10 Relationship

Manifest implementation **precedes** Surface read depth; RT-G10 **enables** entry anchor; RT-G12 **must never duplicate** Manifest minimum understanding.

### What Surface read binding may assume from Manifest implementation

| Surface need | Doctrine anchor | RT-G12 planning obligation |
|--------------|-----------------|----------------------------|
| Manifest entry anchor **reachable** per project | Playbook 03 E4; MRDY-06; TS-02 | Read path **starts** from discoverable manifest locus — **not** repo-wide search |
| MRDY-* categories **already attested** at enrollment | Playbook 03 OR-01 | Read binding **confirms** orientation — **does not** re-teach MRDY-07 |
| Reference topology pointers (Category 7) | PO-*, TS-03 | Read path **uses** pointers to locate authoritative indexes — **not** full topology essay |
| Manifest **does not** hold live gate index | MT-01, SRDY-09 | Surface depth **reads** P4 indexes — **not** manifest bind as gate SoT |

### What RT-G12 must never duplicate from Manifest

| Manifest scope | RT-G12 exclusion |
|----------------|----------------|
| Minimum understanding contract restatement (Categories 1–5 depth) | Surface PO-01 — operational slice only |
| Manifest entry anchor identification ritual | MRDY-06 — enrollment-time only |
| Authoritative reference topology **full map** | One-line pointer repeat **allowed**; essay **forbidden** |
| Stable category amendment narrative (ST-*) | Manifest bind owns stable amendments — Surface **reads outcome** |
| Per-project «start here» enrollment contract | RT-G10 scope — Surface **assumes** entry completed |

### What Surface read binding provides that Manifest does not

| Surface read scope | Manifest exclusion |
|--------------------|-------------------|
| Eight operator questions answered from **live** index composition | Manifest = entry + minimum understanding — **not** blocking/completion/remaining/event depth |
| Tier S-A operational visibility (active state, blockers, recency) | Manifest Category 6 orientation **pointer** — Surface **materializes** observation |
| Actionability classes (OA-*) for Playbook 03 phases | Manifest **does not** enable daily supervision session |
| Integrity warnings when indexes inconsistent | Manifest **does not** own declaration truth (MA-02) |

### Dependency edge (planning)

```text
  Playbook 01 ──▶ manifest-enrolled
         │
         ▼
  RT-G10 impl ──▶ physical manifest anchor on RT-G04
         │
         ▼
  Playbook 03 / RT-G12 impl ──▶ read path: Manifest entry → Tracking indexes → eight questions
```

**Principle M10-REL-01:** RT-G12 planning **must not** absorb manifest enrollment (Playbook 01) or MRDY-* evaluation — **entry consumption only**.

**Principle M10-REL-02 (inherited MT-01):** Surface read **must not** treat manifest bind as substitute for Tracking gate/handoff index.

**Principle M10-REL-03:** RT-G12 implementation planning **must not** precede RT-G10 Manifest Implementation Planning Charter — **satisfied** by upstream COMPLETE; implementation **track** must respect stable manifest anchor (REG-REL-01 analog at Surface plane).

---

## RT-G05 Relationship

Registry implementation **optional** for Surface entry; RT-G05 **never** substitutes per-project Surface depth.

### What Surface read binding may assume from Registry implementation

| Surface need | Doctrine anchor | RT-G12 planning obligation |
|--------------|-----------------|----------------------------|
| Portfolio listing for **project select** before per-project depth | Playbook 03; RE-01; OR-04 | RT-G12 **may** integrate catalog drill-down — **optional** for single-project MVP |
| Each catalog entry **points to** Manifest entry anchor | RM-01, RA-04 | Read path after select **follows** manifest pointer — **not** registry card depth |
| Catalog orientation snapshot **non-authoritative** | RS-03, VP-05, SE-02 | Read binding **must** reconcile before trusting blockers from card alone |
| Registry **does not** answer seven/eight questions | RA-05, RE-01, SC-05 | Portfolio view **excluded** from Surface core obligation |

### What RT-G12 must never duplicate from Registry

| Registry scope | RT-G12 exclusion |
|----------------|------------------|
| Cross-project listing, discoverability lifecycle | RT-G05 — Surface is **per-project** only (TS-02, EO-05) |
| Distinction summaries at portfolio scale | Registry card summaries — **not** Surface orientation depth |
| Catalog membership / withdrawn / archived categories | Registry lifecycle — Surface **may read** archived flag as context only |
| RRDY-* enrollment attestation | Playbook 02 — **not** read binding scope |

### What Surface read binding provides that Registry does not

| Surface read scope | Registry exclusion |
|--------------------|-------------------|
| Eight visibility questions for **one** selected project | Registry answers «which projects» — RE-01 |
| Blocking, completion, remaining, forward pictures | RA-05 — **forbidden** on catalog |
| Recent declaration narrative (SRDY-07) | Registry **does not** own audit trail |
| Per-project actionability assessment (Playbook 03) | Catalog **never** primary supervision surface |

### Dependency edge (planning)

```text
  [optional] RT-G05 impl ──▶ portfolio select
         │
         ▼
  RT-G10 impl ──▶ manifest anchor
         │
         ▼
  RT-G12 impl ──▶ per-project eight-question read binding
```

**Principle G05-REL-01:** RT-G12 planning **must not** absorb registry enrollment (Playbook 02) or RRDY-* evaluation — **optional portfolio consumer only**.

**Principle G05-REL-02:** Single-project Factory path **without** catalog remains **valid** — RT-G12 read binding **must not** require registry entry (M10-REL-02 analog).

**Principle G05-REL-03:** RT-G12 **must not** implement portfolio Surface session (Playbook 03 ST-01, ST-04) — one session = one project.

---

## Authority Model

Authority principles derive **only** from accepted Surface Charter, Tracking Model, Operational Model, and Playbooks — **no new authority classes**.

### Who owns Surface truth

| Truth class | Owner | RT-G12 planning implication |
|-------------|-------|----------------------------|
| **Visibility doctrine** (what operator **must see**) | Surface Charter — **COMPLETE** | RT-G12 **implements read binding**, not role redefinition |
| **Information classes** (Tier S-A/B/C, eight questions) | Surface Charter | Read composition **maps to** classes — **cannot add** mandatory visibility beyond charter |
| **Tracking composition truth** (indexes, zones) | Tracking Model + Playbook 04 declarations | Surface **reads** — MA-02, STV-03 |
| **Last declared state/gate/handoff truth** | Engine tracking planes via Playbook 04 | Read binding **reflects** — **does not author** |
| **Manifest entry / minimum understanding** | Manifest Charter + Playbook 01 | Read path **enters through** manifest anchor — **does not amend** |
| **Portfolio catalog membership** | Registry Charter + Playbook 02 | Optional select only — **non-authoritative** for blockers |
| **Surface-ready (SRDY-*) evaluation** | Derived from index coherence + Surface rules | Read binding **enables** check — **does not** replace human session judgment (Playbook 03) |

### Who may modify Surface reality

| Actor | Permitted (v1) | Forbidden |
|-------|----------------|-----------|
| **Factory operator** | Playbook 04 declarations mutating indexes Surface reads; Playbook 03 session outcomes (non-SoT unless declared) | RT-G12 read path mutating indexes |
| **Reviewer** | Audit Surface read fidelity, SRDY assessment in session — **not** replace declarations | Write via Surface channel |
| **External systems** (CI, agents, git hooks) | **None** for Surface authority | Auto-update indexes on read/sync |
| **RT-G12 implementation** | **Read** substrate; compose visibility; flag integrity warnings | **Write** authoritative state/gate/handoff records |
| **Manifest / Registry impl** | **Read** by Surface consumer | Side-effect writes to tracking indexes |

### Inherited principles (non-negotiable in planning)

| ID | Principle | RT-G12 guard |
|----|-----------|--------------|
| **TS-01** | Surface is visibility doctrine — impl is read binding, not system | **No** tracking engine, **no** storage product |
| **TS-02** | Manifest precedes Surface depth | Read path **requires** entry anchor |
| **TS-03** | Surface points, never merges authority | VP-01, TV-01 — refs only |
| **OA-ACT-04** | External systems never mutate without operator act | No auto-write on read/sync |
| **TRK-REL-01** | RT-G12 never writes authoritative indexes | Read-only **hard** |
| **SE-03** | Surface session does not create indexes | Playbook 03 preserved |
| **MAP-05** | No duplicated tracking SoT | Single gate/handoff index read source |

**Principle AUTH-01:** Physical Surface read binding **extends operability** of observability doctrine — **does not transfer** declaration authority to read channel or display layer.

**Principle AUTH-02:** Read binding freshness follows **declaration chain** (VP-03) — **not** filesystem mtime or CI status.

---

## Boundary Protection

RT-G12 Tracking Surface Implementation **must never become** следующие системы — по Surface Charter anti-patterns, MVP exclusions, Engine boundary, RT-G04/RT-G10/RT-G05 separation.

### Core forbidden roles

| Forbidden system | Why | Guard anchor |
|------------------|-----|--------------|
| **Dashboard platform / operator SaaS / widget product** | TX-07, SC-07; Surface charter ≠ UI | MVP = minimum read binding only |
| **Tracking composition engine / tracking storage** | TS-01; Stage 3 owns composition | RT-G12 **reads** indexes — **does not own** zones |
| **Persistence substrate product** | MAP-01 analog; RT-G04 owns locus | Substrate design — **not RT-G12** |
| **Manifest / Passport / minimum understanding store** | MT-01, MAP-06; RT-G10 separate | Entry depth duplication **forbidden** |
| **Registry / portfolio catalog product** | RE-01, RA-05; RT-G05 separate | Portfolio ≠ Surface depth |
| **Database / query engine / analytics platform** | Scope creep; cross-project KPI rollups | No portfolio analytics on Surface |
| **Workflow engine / state machine executor** | MAP-04; RT-G01 | Forward picture **enables** declare — **does not** transition |
| **Factory runtime product** | SC-01; RT-G09 | «Surface drives execution» — **rejected** |
| **Gate Results System / gate evaluator** | GV-02, MAP-10 | Surface **shows** outcomes — **does not evaluate** |
| **Project management system** | Scope creep | Tasks, sprints, assignments — **out of scope** |
| **Session workflow engine / automated supervision** | Playbook 03 human ritual | No CI/agent session open/close |
| **Declaration write path** | Playbook 04, DA-01 | Read binding **≠** declaration channel |
| **Automation / agent index mutation** | OA-ACT-04, SC-03 | Sync as authoritative — **forbidden** |
| **Notification / webhook hub** | RT-G13 | External approval — **post-MVP** |
| **Closure registry / terminal workflow engine** | Playbook 05 | Closure metadata — substrate P6 |

### Architectural anti-patterns RT-G12 planning must resist

| Anti-pattern | Guard |
|--------------|-------|
| RT-G12 conflated with «shipped Factory runtime» or «dashboard MVP» | C5 ≠ RT-G09; TX-07 |
| UI design smuggled into **this** planning charter | Task charter forbidden list |
| Surface read duplicates live Manifest gate index | MT-01, SRDY-09, MAP-05 |
| Registry card answers eight questions | SC-05, RE-01 |
| Read binding **before** substrate indexes + manifest anchor stable | SC-02, G04-REL-02 |
| Surface read replaces Playbook 04 declaration path | DA-01, C6, TRK-REL-01 |
| `COMPLETE` / deploy conflated with Surface «completion» | LV-03, MAP-13 |
| RUNTIME-GAPS «dashboard» line interpreted as UX program mandate | OQ-TS09 — doctrine complete; impl = read binding |

### Additional justified non-responsibilities

| Role | Rationale |
|------|-----------|
| Validator / gate authority engine | RT-G11 — post-MVP |
| Queue / scheduler | RT-G06 |
| MIG / external pipeline SoT | RT-G08 |
| Rollback automation executor | RT-G15 |
| Layer generation / frontend build | GG-* — external product plane |
| Operator Display Charter (OQ-TS05) as substitute for this planning charter | Separate **future** artifact — **must** map SRDY-* |
| Site Type Registry operations | RAP-11 — Foundation T1 |

**Principle BP-01:** RT-G12 is **per-project Surface read binding responsibility** — **one plane**, **one project**, **eight questions**, **read-only** — not a platform.

**Principle BP-02:** RT-G12 planning **must remain** form-factor-agnostic — markdown vs CLI vs static HTML is **implementation standard** territory (DF-07), not planning charter resolution.

---

## Readiness Model

### When RT-G12 **planning charter** is complete

RT-G12 Tracking Surface Implementation Planning Charter v1 считается **planning-complete** когда:

| Criterion | Status in this deliverable |
|-----------|---------------------------|
| Purpose defined — C5 gap, eight questions, vs doctrine-only baseline | **Yes** |
| Implementation responsibility — must provide / must not provide | **Yes** — IS-*, SI-* |
| SRDY-* binding rules without format or UI design | **Yes** — SRB-* |
| RT-G04 consumption model — read feed vs writes | **Yes** — G04-REL-* |
| RT-G10 dependency — entry anchor, non-duplication | **Yes** — M10-REL-* |
| RT-G05 dependency — optional portfolio, RE-01 | **Yes** — G05-REL-* |
| Authority model — read-only, Playbook 03/04 split | **Yes** — AUTH-* |
| Boundary protection — forbidden roles explicit | **Yes** — BP-* |
| Physical visibility vs doctrinal-only distinction | **Yes** — §Implementation Responsibility |
| Future implementation implications identified | **Yes** — see below |
| Explicit non-claims — no UI, schemas, storage | **Yes** |

### What planning-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| RT-G12 **implementation** started or complete | Separate authorized track |
| Physical read surface artefacts **created** | Forbidden in planning scope |
| Display form factor **selected** | RT-G12 implementation standard (DF-07) |
| OQ-TS01, DF-07, OQ-PD05 **resolved** | Bounded OPEN for implementation charter |
| MVP **demonstrated** | S1–S9 post-implementation |
| Operator dashboard **authorized** | Explicitly excluded |

### Planning-complete vs implementation-ready

```text
  Surface Charter v1 (doctrine) ── COMPLETE
           │
           ▼
  RT-G04 Persistence Substrate Charter v1 ── COMPLETE
           │
           ▼
  RT-G10 Manifest Implementation Planning Charter v1 ── COMPLETE
           │
           ▼
  RT-G05 Registry Implementation Planning Charter v1 ── COMPLETE
           │
           ▼
  RT-G12 Surface Implementation Planning Charter v1 ── THIS (planning-complete)
           │
           ▼
  RT-G12 Surface Read Binding Implementation Standard (implementation charter) ── NEXT authorized track
```

**Principle RDY-01:** Loss of RT-G12 planning clarity **must not** block Surface doctrine or Playbook 03 — doctrine **already operable** without physical read bind (manual composition).

**Principle RDY-02:** MVP S4 success **requires** RT-G12 implementation **after** RT-G04 substrate + RT-G10 manifest anchor (+ indexes from Playbook 04) — not planning alone.

**Principle RDY-03:** RT-G12 planning-complete **does not** authorize physical MVP artefact creation or UI mockups — operator implementation charter required per RUNTIME-GAPS governance rule.

---

## Future Implementation Implications

Без implementation design — **logical successors and dependency edges only**.

### Immediate successor (Tier 1)

| Next charter | Role | Depends on | Must carry forward |
|--------------|------|------------|-------------------|
| **RT-G12 Surface Read Binding Implementation Standard** (implementation charter — **not this doc**) | Read path scope, DF-07 form factor choice, SRDY-07 recency binding (OQ-PD05), optional registry drill-down integration, integrity warning rules | This planning charter + RT-G04 substrate impl + RT-G10 manifest anchor + persisted P4 indexes | TS-*, VP-*, SRDY-*, MAP-05, Playbook 03, TRK-REL-01, OA-ACT-04 |

**Success signal (from Implementation Planning Review):** Operator completes Playbook 03 session answering **all eight** Surface visibility questions from bound read path — **not** full-repo search (S4, C5).

### Parallel / sequential predecessors (MVP sequence)

| Charter | Relationship to RT-G12 | Sequencing rule |
|---------|------------------------|-----------------|
| **RT-G04 Implementation** (physical substrate artefacts) | **Enables** P4 read feed | **Before or with** RT-G12 impl — C2→C5 |
| **RT-G10 Manifest Implementation Standard** | **Precedes** meaningful Surface entry | **Before** RT-G12 impl bind per project |
| **RT-G05 Registry Implementation Standard** | **Optional** portfolio select consumer | **May parallel** RT-G12; **not** hard for single-project MVP |
| **Playbook 04 declaration persistence** (C6) | Supplies indexes Surface reads | **Required** for non-trivial S4 demo — may be manual pre-impl |

### Post-MVP (not blocked by RT-G12 planning)

| Item | Notes |
|------|-------|
| Operator Display Charter (OQ-TS05) | May formalize render rules — **must** reference SRDY-* |
| RT-G11 Validator CLI | Gate **aid** — must not replace Playbook 04 or write via Surface |
| OQ-TS01 recent event window semantics | Playbook 03 + implementation standard |
| OQ-TS03 PHASE_SLICE — one Surface per shell vs slice | Engine v2 or implementation standard |
| Auto-sync display from Tracking — non-authoritative | OQ-TS07 — bounded forbidden as SoT |

### MVP operator path after RT-G12 impl (planning reference)

```text
  Playbook 01 ──▶ manifest-enrolled
         │
         ▼
  RT-G10 impl ──▶ physical manifest anchor (C3)
         │
         ├──▶ [optional] Playbook 02 / RT-G05 ──▶ portfolio select
         │
         ▼
  RT-G12 impl ──▶ per-project read binding (C5, S4)
         │
         ▼
  Playbook 03 ──▶ Surface session (eight questions via read path)
         │
         ▼
  Playbook 04 ──▶ declaration writes update indexes (C6) ──▶ Surface read reflects
         │
         ▼
  Playbook 05 ──▶ closure metadata visible on read path
```

**Principle FUT-01:** RT-G12 implementation standard **must not** authorize automated index mutation, workflow hooks, or gate evaluation as side effects of read binding.

**Principle FUT-02:** RT-G12 implementation standard **must not** define FACTORY-DASHBOARD-v1.md, FACTORY-UI-SPEC-v1.md, FACTORY-TRACKING-SURFACE-STANDARD-v1.md, or FACTORY-TRACKING-STORAGE-v1.md **without** explicit operator authorization beyond planning charter.

---

## Explicit Non-Claims

This document and the RT-G12 Tracking Surface Implementation **planning** role it defines:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** **UI design**, **dashboard design**, **screen layout**, **wireframe**, **widget system**, or **navigation** design;
- **are not** **storage design**, **database design**, **file format**, **JSON/YAML schema**, **folder structure**, or **physical MVP artefacts**;
- **are not** **implementation spec**, **read binding standard**, or **code**;
- **are not** **tracking engine**, **tracking storage**, **state store**, or **recorder product**;
- **are not** **Manifest** (RT-G10) or **Registry** (RT-G05) redesign;
- **are not** **Persistence Substrate** (RT-G04) redesign — only **consumption** relationship;
- **are not** **Tracking Surface Charter** or **Tracking Model** rewrite — doctrine taken as authoritative input;
- **are not** Playbooks 01–05 rewrite;
- **do not** define screens, panels, CLI commands, markdown templates, database tables, or read file paths;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** claim physical Surface read artefacts or operator dashboard **exist** in-repo — **planning charter only**;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound Surface read path;
- **do not** claim RT-G12 **implementation** is authorized beyond **planning** by existence of this document alone.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01. Surface read binding remains **read-oriented only** per TRK-REL-01.

---

## Open Questions

Charter **bounds** questions for **future RT-G12 implementation standard** — **does not answer** display, form factor, or read path serialization choices.

| ID | Question | Disposition |
|----|----------|-------------|
| **DF-07** | Read surface form factor — markdown index vs CLI vs static HTML vs local UI shell | **OPEN** — RT-G12 implementation standard; **must** respect TX-07 (no dashboard product) |
| **OQ-TS01** | Recent event window size / «since last visit» semantics for question #6 | **OPEN** — Playbook 03 + implementation standard |
| **OQ-TS02** | Whether RT-G10 manifest serializes Surface Tier S-A subset | **OPEN** — RT-G10 implementation standard (OQ-M01); default **read from P4** |
| **OQ-TS03** | PHASE_SLICE — one Surface read bind per shell vs per slice | **OPEN** — Engine v2 or implementation standard |
| **OQ-TS05** | Separate Operator Display Charter vs this implementation standard | **OPEN** — display artifact **must** map SRDY-*, VP-* |
| **OQ-TS06** | `PASS_WITH_WARNINGS` actionable class on read binding | **OPEN** — gate composition |
| **OQ-TS07** | Auto-sync read view from Tracking — display-only vs forbidden SoT | **BOUNDED** — authoritative = declarations; sync **non-authoritative** only |
| **OQ-TS08** | MIG / incoming request correlation as Surface event class | **OPEN** — RT-G08 |
| **OQ-TS09** | RUNTIME-GAPS «dashboard» line vs read binding scope | **BOUNDED** — resolved: impl = minimum read binding, not UX program |
| **OQ-PD05** | Declaration/session record binding for SRDY-07 recency | **OPEN** — cross RT-G04/10/12 implementation planning |
| **OQ-R03** | Default vs extended portfolio view for archived/withdrawn before Surface select | **OPEN** — RT-G05/12 implementation |
| **OQ-TSW02** | «Since last session» semantics tied to Playbook 03 reality phase | **OPEN** — operational + implementation |

**Resolved by upstream (not open in this planning scope):** Surface doctrine (eight questions, SRDY-*, Tier S-A/B/C); Playbook 03 session workflow; RT-G04 read-only Surface semantics (TRK-REL-01); MVP includes C5 Surface binding; Manifest precedes Surface (TS-02); Registry ≠ Surface depth (RE-01, RA-05); Tracking owns composition (Stage 3).

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G12 Tracking Surface Implementation Planning Charter v1** as **RT-G12 planning role complete** — gap RT-G12 in RUNTIME-GAPS remains **NOT STARTED** for **implementation**, not for planning.
2. **Authorize next track:** **RT-G12 Surface Read Binding Implementation Standard** (implementation charter) — read path scope, DF-07 form factor, SRDY-07 recency binding, integrity warning rules — **still requires** separate authorization; **must** carry TS-*, VP-*, SRDY-*, MAP-05, Playbook 03, TRK-REL-01 forward.
3. **Preserve sequencing:** RT-G04 substrate + RT-G10 manifest implementation **before** RT-G12 read binding demonstration; Playbook 04 persisted indexes **required** for meaningful S4; RT-G05 registry **optional** for portfolio select.
4. **Do not create yet:** dashboard mockups, FACTORY-DASHBOARD-v1.md, FACTORY-UI-SPEC-v1.md, FACTORY-TRACKING-SURFACE-STANDARD-v1.md, tracking storage schemas, Surface-as-write-channel prototypes, registry-as-Surface-depth prototypes.
5. **Optional P3:** Update RUNTIME-GAPS RT-G12 line to «PLANNING CHARTERED» — **operator action**, outside this deliverable.

**Engine Architecture v1 requires no further architecture stages.** RT-G12 planning charter is **post-RT-G04, post-RT-G10-planning, post-RT-G05-planning, post-MVP-definition** documentation.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` path **exists** on disk today | **UNKNOWN** — RT-G04 charter records zone; physical creation not part of this deliverable |
| Calendar for RT-G12 implementation standard authorization | **not scheduled** |
| De-facto ad-hoc Surface read discipline already used by operators (manual index assembly) | **UNKNOWN** — no canonical read binding chartered |
| Triumph / pilot workspaces as read bind targets vs external-only refs | **UNKNOWN** — per case (DF-08) |
| Whether any tool already renders Engine composition for supervision | **UNKNOWN** — OQ-TS09 analog |
| Operators updated NEXT-PRIORITIES to RT-G12 planning-complete era | **UNKNOWN** |

---

*RT-G12 Tracking Surface Implementation Planning Charter v1 — RT-G12 planning complete. Planning charter only. Canonical location: `workspaces/website-factory-reference-v1/RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G12 Tracking Surface Implementation Planning Charter v1

**Stage:** Implementation Planning — RT-G12 Tracking Surface Implementation Planning Charter  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G12-TRACKING-SURFACE-IMPLEMENTATION-PLANNING-CHARTER-v1.md` (created)  
**Summary:** Определена planning-ответственность RT-G12 Tracking Surface Implementation: физическая read binding доктрины Surface (eight operator questions, Tier S-A/B/C, SRDY-*) на RT-G04 substrate для MVP C5/S4; read-only semantics (TRK-REL-01); границы must/must-not vs RT-G04 substrate, RT-G10 Manifest, RT-G05 Registry, Tracking Model, Playbooks 01–05; SRDY binding без форматов и UI; authority model (operator declares via Playbook 04, Surface reads only); boundary protection от dashboard/tracking engine/workflow/PM/analytics; readiness planning-complete vs successor RT-G12 Surface Read Binding Implementation Standard; без UI, storage, schemas, implementation design.  
**Git:** no commit, no push (per task charter).
