# REPORT — Website Factory Implementation Planning Review v1

**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `projects/mars-website-factory/` (операционный пакет, не замена канона)  
**Тип:** implementation planning review only — **без** implementation specs, runtime specs, storage/UI design, schemas, code  
**Метод:** инвентаризация принятых артефактов, dependency review по RUNTIME-GAPS и charters, MVP/post-MVP classification, operational continuity cross-check  
**Принятая реальность (контекст задачи):** Foundation Era **COMPLETE**; Factory Engine Architecture **COMPLETE**; Post-Engine Doctrine **COMPLETE**; Governance Synchronization **COMPLETE**; Operational Design **COMPLETE**; runtime / storage / automation **отсутствуют**

---

## Executive Summary

**Вердикт:** Website Factory **готов к MVP Implementation Planning** — документарный стек (Foundation + Engine + post-Engine charters + Operational Model + Playbooks 01–05) достаточен, чтобы определить **что** реализовывать первым, **что** оставить документацией и **что** отложить в runtime-территорию, **без** проектирования реализации в этом deliverable.

**Если implementation начнётся завтра — первая очередь (planning-level):**

1. **RT-G04** — persistence substrate (единый физический слой хранения Factory Project records).
2. **RT-G10 implementation** — per-project manifest serialization (entry anchor + minimum understanding categories).
3. **RT-G05 implementation** — portfolio registry index (catalog discoverability; optional в doctrine, **в scope MVP** по миссии).
4. **RT-G12 implementation** — operator read surface для одного проекта (visibility classes, **не** workflow engine).

**Что не строить в MVP:** workflow engine (RT-G01), automation/agents (RT-G02–03), queue (RT-G06), validator CLI binding (RT-G11), MIG execution (RT-G08), Engine runtime product (RT-G09 impl), multi-operator concurrency (RT-G14), rollback automation (RT-G15), layer generation automation (GG-*).

**MVP definition (planning):** минимальная **физическая привязка** doctrinal planes Manifest + Registry + Tracking Surface для **одного** human operator, **без** автоматизации state mutation и **без** shipped Factory runtime/orchestrator.

**Рекомендация (одна):** **A — Ready for MVP Planning** (см. [Final Recommendation](#final-recommendation)).

---

## Implementation Inventory

Классификация **принятых** артефактов Website Factory. Канон: `workspaces/website-factory-reference-v1/`.

### A — Documentation only (не требует implementation для эксплуатации)

| Domain | Canonical artefact(s) | Evidence / role |
|--------|----------------------|-----------------|
| Foundation (14 layers) | Legal Pack, Site Type Registry, Blueprints (Core 5), Page Architecture, Block Registry, Page Block Validation, SEO, Design System, Content, Content Validation, Generation, Production QA, Runtime Architecture | **ACCEPTED/FROZEN** per Foundation Finalization Pass 2026-06-04 |
| Foundation meta | ARCHITECTURE-FOUNDATION-v1, WEBSITE-FACTORY-FOUNDATION-v1-FREEZE, FOUNDATION-FINALIZATION-PASS, ENGINE-READINESS-AUDIT, PRE-ENGINE-INTEGRITY-AUDIT | Consolidation / audit registers |
| Engine Stages 1–6 | FACTORY-PROJECT-OBJECT/STATE/TRACKING-MODEL, GATE/LIFECYCLE-COMPOSITION-MODEL, FACTORY-ENGINE-SYSTEM-BOUNDARY | **ACCEPTED/COMPLETE** — documentation architecture |
| Post-Engine doctrine | FACTORY-PROJECT-MANIFEST/REGISTRY-CHARTER, FACTORY-TRACKING-SURFACE-CHARTER | RT-G10/05/12 **CHARTERED** — role definition only |
| Operational design | FACTORY-OPERATIONAL-MODEL-v1, Playbooks 01–05 | Human-operated workflows **без** physical artefacts |
| Consolidation / governance | ARCHITECTURE-CONSOLIDATION-REVIEW, OPERATIONAL-DESIGN-CONSOLIDATION-REVIEW, GOVERNANCE-SYNCHRONIZATION-PASS | Meta-audit; no implementation |
| Gap / roadmap registers | RUNTIME-GAPS, RUNTIME-ROADMAP, layer *-GAPS-v1 | Future work registers — **documentation** |
| Parallel operational pack | `projects/mars-website-factory/` (Wave 1–6, Forge/Gulp, v0 registries) | Operational methodology + frontend workspaces — **не** Factory persistence product |

### B — Requires implementation (MVP and near-MVP territory)

| Gap / capability | Doctrine source | Implementation status | MVP relevance |
|------------------|-----------------|----------------------|---------------|
| **RT-G04** Runtime storage | All charters defer physical persistence | **NOT STARTED** | **Prerequisite** — substrate for B-plane |
| **RT-G10 impl** Project manifest standard | Manifest Charter + Playbook 01 | **NOT STARTED** | **Core MVP** — per-project entry anchor |
| **RT-G05 impl** Project registry | Registry Charter + Playbook 02 | **NOT STARTED** | **Core MVP** — portfolio catalog |
| **RT-G12 impl** Operator display | Tracking Surface Charter + Playbook 03 | **NOT STARTED** | **Core MVP** — eight visibility questions |
| Declaration / session record persistence | Playbooks 03–04 (OQ-PD05) | **NOT STARTED** | **Near-MVP** — supports Surface recency class; operable manually pre-impl |
| Registry index card field template | OQ-R02 (Registry Charter) | **NOT STARTED** | **Near-MVP binding** — operational or first impl input |
| RT-G07 Execution logs | RUNTIME-GAPS | **NOT STARTED** | **Post-MVP** preferred — audit trail automation |
| RT-G11 Validator CLI | VALIDATION-GAPS, layer validators | **NOT STARTED** | **Post-MVP** — gate enforcement aid |

### C — Future runtime (explicitly out of MVP; charter before start)

| Gap ID | Topic | Why deferred |
|--------|-------|--------------|
| RT-G01 | Workflow engine | Highest ordering risk; contradicts human-operated MVP |
| RT-G02 | Agent execution | No AI orchestration in Factory v1 scope |
| RT-G03 | Automation (n8n, CI state mutation) | Violates operator-declared truth model |
| RT-G06 | Queue system | Multi-project scheduling — not single-operator MVP |
| RT-G08 | MIG integration | External pipeline; OQ-OM08 binding OPEN |
| RT-G09 impl | Factory Engine runtime product | Separate from documentation closure |
| RT-G13 | Notification / webhook gates | External approval integrations |
| RT-G14 | Multi-project concurrency | Resource locking — post single-operator MVP |
| RT-G15 | Rollback automation | Scripted cascade — post human-operated MVP |
| GG-03, GG-07 | Frontend generation, orchestration | Layer automation — separate product plane |
| Extended Type blueprints | SAAS, WEB_APPLICATION, MARKETPLACE | Architecture charter work — not Core 5 |

**Inventory verdict:** принятая **документация** покрывает A полностью для Core 5. Implementation plane — **B + C**; только **RT-G04/05/10/12** входят в MVP scope по миссии.

---

## Dependency Review

### Normative doctrine stack (already satisfied — no implementation)

```text
Foundation (T1) + Runtime (T2)
        │
        ▼
Engine Stages 1–6 (per-project composition)
        │
        ▼
Post-Engine Charters (Manifest → Registry → Tracking Surface roles)
        │
        ▼
Operational Model + Playbooks 01–05 (human rituals)
```

### Implementation dependency graph (planning-level)

Источники: [RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) §4, Manifest/Registry/Tracking Surface charters, Engine System Boundary §Implementation Plane.

```text
                    ┌─────────────────────────────────┐
                    │  Operator MVP Planning Charter   │
                    │  (authorized AFTER this review)  │
                    └─────────────────────────────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────────┐
                    │  RT-G04 — Persistence substrate  │◀── prerequisite for ALL physical bindings
                    └─────────────────────────────────┘
                          │                    │
              ┌───────────┘                    └───────────┐
              ▼                                            ▼
    ┌─────────────────────┐                    ┌─────────────────────┐
    │ RT-G10 impl         │                    │ Declaration/session │
    │ Manifest serialize  │                    │ record binding      │
    │ (per-project anchor)│                    │ (Playbooks 03–04)   │
    └─────────────────────┘                    └─────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │ RT-G05 impl         │◀── depends on stable manifest anchor + project identity (MR-01, RA-02)
    │ Registry catalog    │
    └─────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │ RT-G12 impl         │◀── reads Manifest + Tracking composition + optional Registry portfolio view
    │ Operator read surface│
    └─────────────────────┘
              │
              ▼ (post-MVP branches — parallel forbidden without charter)
    ┌──────────────────────────────────────────────────────────┐
    │ RT-G07 logs │ RT-G11 validators │ RT-G06 queue │ RT-G08 MIG │
    └──────────────────────────────────────────────────────────┘
              │
              ▼ (highest risk — last)
    ┌──────────────────────────────────────────────────────────┐
    │ RT-G01 workflow │ RT-G03 automation │ RT-G09 runtime product │
    └──────────────────────────────────────────────────────────┘
```

### Prerequisite order (recommended sequence for MVP planning authorization)

| Order | Component | Depends on | Rationale (from accepted docs) |
|-------|-----------|------------|--------------------------------|
| 0 | Governance hygiene (NEXT-PRIORITIES lists Implementation Planning era) | This review | Register lag — LOW; not blocking |
| 1 | RT-G04 persistence charter | Doctrine complete | Manifest Charter OQ-M04; Registry OQ-R01; Tracking OQ-TS02 — storage **не выбирается** charters |
| 2 | RT-G10 manifest implementation charter | RT-G04 (+ Engine/Manifest doctrine) | RUNTIME-GAPS: manifest impl **before** registry in suggested order |
| 3 | RT-G05 registry implementation charter | RT-G10 anchor + RT-G04 | Registry Charter: **depends on** Manifest per project (RAP-16, Playbook 01→02) |
| 4 | RT-G12 display implementation charter | RT-G10 + Tracking composition data + RT-G04 | Surface charter: display **reads** classes; **не** UI in doctrine doc |
| 5 | Optional OQ-R02 card template | RT-G05 impl planning input | MEDIUM — workflows operable without; reduces registry impl ambiguity |

**Cross-dependencies explicitly NOT in MVP critical path:**

- Layer validators (RT-G11) — Foundation gates remain human-operated.
- MIG (RT-G08) — external trigger; Playbook 01 intake works without.
- `projects/mars-website-factory/` frontend workspaces — Lane A build; orthogonal to Factory SoT.

---

## RT Review

Focused review of **RT-G04, RT-G05, RT-G10, RT-G12** — doctrine vs implementation, MVP role, dependency edges.

### RT-G04 — Runtime storage

| Dimension | Assessment |
|-----------|------------|
| Doctrine | **N/A** — no architecture charter; persistence explicitly **external** to Engine boundary |
| Implementation | **NOT STARTED** |
| Role | Substrate for manifest records, registry index, tracking/declaration persistence, closure outcomes |
| Charter authority | Manifest MAP-01 anti-pattern: Manifest **≠** storage; Registry RAP-01: Registry **≠** database; Storage charter **must not** violate Engine ownership |
| Open questions | OQ-M04 (manifest vs tracking co-location); OQ-R01 (registry artefact vs distributed pointers) — **resolve in implementation charter**, not here |
| MVP | **Required first** — without RT-G04, RT-G10/05/12 remain doctrine-only |
| Runtime territory? | **Partially** — file-backed persistence for single operator is **MVP implementation**; DB/queue/multi-tenant = post-MVP |

### RT-G05 — Project registry (implementation)

| Dimension | Assessment |
|-----------|------------|
| Doctrine | **CHARTERED** — [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) **COMPLETE** |
| Implementation | **NOT STARTED** |
| Role | Multi-project catalog, discoverability, distinction summaries, pointer to Manifest entry |
| Depends on | RT-G10 manifest anchor per project; RT-G04 for physical index; **not** Site Type Registry (Foundation T1) |
| Playbook binding | Playbook 02 — catalog enrollment **optional** in doctrine but **required for MVP mission** (portfolio + single operator managing cases) |
| Must not | Substitute tracking (RA-05), act as dashboard (RAP-05 → RT-G12), mutate Engine indexes automatically |
| MVP | **Core** — minimum catalog for one operator with one or few projects |

### RT-G10 — Project manifest standard (implementation)

| Dimension | Assessment |
|-----------|------------|
| Doctrine | **CHARTERED** — [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) **COMPLETE** |
| Implementation | **NOT STARTED** |
| Role | Physical serialization of entry anchor + minimum understanding categories + reference topology |
| Depends on | Engine Stages 1–6 (logical model); RT-G04 (where stored); **precedes** RT-G05 |
| Playbook binding | Playbook 01 — manifest-enrolled **doctrinal** today; physical file **not** blocking enrollment ritual |
| Open questions | OQ-M01 (which Tracking zones may serialize); OQ-ME05 (creation moment vs Enrolled) — **implementation charter scope** |
| Must not | Own live gate index (MT-01), replace Tracking composition, auto-mutate state |
| MVP | **Core** — first per-project physical artefact |

### RT-G12 — Operator UI / dashboard (implementation)

| Dimension | Assessment |
|-----------|------------|
| Doctrine | **CHARTERED** — [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) **COMPLETE** |
| Implementation | **NOT STARTED** |
| Role | Render **eight operator visibility questions** as information classes — read-oriented |
| Depends on | Tracking composition data (Engine Stage 3 + Playbook 03/04 declarations); Manifest entry path; RT-G04 reads; optional Registry portfolio drill-down |
| Playbook binding | Playbook 03 — session workflow **explicitly forbids** UI implementation in playbook |
| Must not | Authorize transitions, evaluate gates, replace operator declaration authority |
| MVP | **Core** — minimum read surface (CLI, static view, or lightweight local UI — **choice deferred** to MVP charter, not this review) |
| vs Surface doctrine | Surface = **what must be visible**; RT-G12 impl = **how operator sees it** |

### RT implementation dependency summary

```text
RT-G04 ──▶ RT-G10 impl ──▶ RT-G05 impl
                │                 │
                └────────┬────────┘
                         ▼
                   RT-G12 impl
```

**None of RT-G04/05/10/12** may start without **operator implementation charter** per RUNTIME-GAPS governance rule.

---

## MVP Review

### MVP mission constraint (from task)

Minimum implementation capable of supporting **Manifest**, **Registry**, **Tracking Surface** for a **single operator**, **without automation**, **without runtime** (orchestrator/workflow engine).

### What MVP **is** (planning definition)

| Capability | MVP includes | Doctrine / playbook anchor |
|------------|--------------|----------------------------|
| Per-project entry anchor (physical) | Yes | Manifest Charter MRDY-*; Playbook 01 |
| Minimum understanding categories persisted | Yes | Manifest Charter categories (not field design here) |
| Portfolio catalog (physical index) | Yes | Registry Charter RRDY-*; Playbook 02 |
| Operator can answer eight Surface questions from bound data | Yes | Tracking Surface Charter SRDY-*; Playbook 03 |
| Human declaration writes update visible indexes | Yes (manual write path) | Playbook 04 — operator remains sole declarer |
| Closure outcomes persistable | Yes (minimal) | Playbook 05 — may bind to RT-G04/10 |
| Single operator, single-machine or single-repo scope | Yes | Operational Model OR-* |
| Automation of state/gate mutation | **No** | Engine boundary ES-04 |
| Workflow engine / agents | **No** | RT-G01–03 |
| Validator CLI / CI gate product | **No** | RT-G11 |
| Multi-operator concurrency / queue | **No** | RT-G06, RT-G14 |
| Full dashboard product / SaaS | **No** | MVP = minimum read binding only |

### What MVP **is not**

- Shipped **Factory runtime** or Engine automation product (RT-G09 impl).
- Replacement of Playbooks — implementation **supports** rituals, **does not** auto-execute them.
- Layer artefact production (Foundation T1) — remains human + external workspace.
- Frontend site generation (GG-03) — remains `projects/mars-website-factory/` / client workspace track.
- Extended site types without blueprints.

### MVP operational scenario (single operator)

1. Operator runs Playbook 01 → manifest-enrolled → **physical manifest record created** (RT-G10 impl).
2. Operator optionally runs Playbook 02 → catalog-discoverable → **registry entry** (RT-G05 impl).
3. Operator runs Playbook 03 sessions → assessments → Playbook 04 declarations → **indexes updated** via manual/assisted write to RT-G04-backed store.
4. Operator opens RT-G12 read surface → answers eight questions **without workspace archaeology**.
5. Operator runs Playbook 05 closure → terminal metadata **persisted** referencing existing records.

**Pre-MVP baseline (today):** steps 1–5 are **already executable doctrinally** using markdown indexes, operator notes, and external workspace pointers — **no HIGH gap** per Operational Design Consolidation Review.

**MVP delta:** replace ad-hoc scattered notes with **authorized physical binding** of Manifest + Registry + Surface visibility — still human-operated.

### MVP completeness criteria (planning-level acceptance)

- [ ] One Factory Project can be manifest-enrolled with persisted entry anchor.
- [ ] Registry lists that project with distinction summary and Manifest pointer.
- [ ] Operator read surface exposes eight Surface question classes for that project.
- [ ] Declarations from Playbook 04 can be reflected in persisted indexes **without** automated gate evaluation.
- [ ] No workflow engine required to complete a Core 5 pilot case.
- [ ] Explicit non-claims preserved — no false «shipped runtime» narrative.

---

## Post-MVP Review

Explicit **exclusions** from MVP — authorize only via separate charters.

### Tier 1 — Post-MVP implementation (natural successors)

| Item | Rationale for deferral |
|------|------------------------|
| RT-G07 Execution logs | Machine-readable audit trail — valuable after persistence stable |
| RT-G11 Validator CLI | Wires layer validators; risk of conflating validation PASS with operator declaration |
| Declaration/session **automation** helpers | Read-only advisors OK (RUNTIME-ROADMAP R6); mutation helpers → RT-G03 territory |
| OQ-R02 registry card template (if skipped pre-MVP) | Reduces friction; not blocking doctrinal operation |
| v0↔v1 agent routing card (OQ-OM06) | Hygiene across dual corpus |
| MIG intake binding (OQ-OM08) | Integration charter — external pipeline |

### Tier 2 — Runtime territory (high risk / high scope)

| Item | Rationale |
|------|-----------|
| RT-G01 Workflow engine | RUNTIME-GAPS: «highest risk; charter last» |
| RT-G03 Automation / n8n | Violates human-operated declaration authority if mutates indexes |
| RT-G06 Queue | Multi-project scheduling beyond single-operator MVP |
| RT-G08 MIG execution | Execution binding, not Factory SoT |
| RT-G09 Engine runtime product | Distinct from documentation-complete Engine |
| RT-G13 Webhooks / external approval | External integrations |
| RT-G14 Concurrency rules | Multi-operator |
| RT-G15 Rollback automation | Cascade invalidation scripts |
| GG-03 Frontend generation automation | Separate generation product |
| GG-07 Orchestration | Meta-factory automation |

### Tier 3 — Architecture / documentation (not implementation)

| Item | Notes |
|------|-------|
| Extended Type blueprints | SAAS, WEB_APPLICATION, MARKETPLACE |
| ECOMMERCE legal extension | Beyond frozen Legal Pack |
| Chrome blocks binding | HEADER_NAV, FILTERS, SEARCH — OQ-S6-07 |
| Engine v2 / PHASE_SLICE formalization | OQ-S6-03 |
| Unified gate-namespace index | AG-05 optional hygiene |

**Post-MVP principle:** MVP **closes physical binding gap** for Core 5 single operator; **does not** close automation or multi-project operations gap.

---

## Risk Review

| Risk | Type | Severity | Mitigation (planning) |
|------|------|----------|------------------------|
| Conflating MVP persistence with «shipped Factory runtime» | Premature runtime | **HIGH** | Preserve explicit non-claims; MVP ≠ RT-G09 impl |
| Starting RT-G12 before RT-G10/04 stable | Ordering | **HIGH** | Enforce dependency graph in MVP charter |
| RT-G04 charter smuggling storage design into doctrine | Scope creep | **MEDIUM** | Separate implementation charter; charters forbid format in doctrine docs |
| Automated writes from validators/CI replacing Playbook 04 | Authority drift | **HIGH** | Defer RT-G11; operator remains declarer (DA-01) |
| Registry substituting Tracking (RA-05 violation) | Architectural | **MEDIUM** | Registry impl charter must reference anti-patterns RAP-* |
| Manifest owning live gate index (MT-01 violation) | Architectural | **MEDIUM** | Manifest impl bounded to entry anchor categories |
| Dual corpus v0/v1 ID mixing during impl | Operational | **MEDIUM** | OQ-OM06 routing before agent-assisted impl |
| Extended type pilot before blueprint charter | Scope | **MEDIUM** | Restrict MVP pilot to Core 5 site classes |
| Register lag (Implementation Planning not in NEXT-PRIORITIES) | Governance | **LOW** | Hygiene at MVP charter kickoff |
| Over-building dashboard vs minimum read surface | Over-engineering | **MEDIUM** | MVP RT-G12 = visibility binding, not product UX program |

**Ordering risk summary:** highest failure mode = **RT-G01/G03 before RT-G04/10** — skips human-operated binding and recreates automation debt flagged in Engine Readiness Audit and both consolidation reviews.

**Premature runtime risk summary:** any implementation that **mutates** Engine indexes without Playbook 04 operator act is **out of MVP scope** and contradicts accepted operational design.

---

## Operational Continuity Review

Which playbooks function **before** implementation vs **benefit from** implementation support.

| Playbook | Pre-implementation status | Implementation support needed |
|----------|----------------------------|------------------------------|
| **01 Manifest Enrollment** | **Fully functional** — manifest-enrolled is doctrinal outcome; physical file not required | RT-G10 impl reduces ad-hoc scatter; OQ-ME05 resolved |
| **02 Registry Enrollment** | **Fully functional** — catalog-discoverable is doctrinal; optional | RT-G05 impl + OQ-R02 template reduce ambiguity |
| **03 Tracking Surface Session** | **Fully functional** — session ritual independent of UI | RT-G12 impl reduces workspace archaeology; declaration persistence helps recency class |
| **04 Project Declaration** | **Fully functional** — operator declares to logical indexes | RT-G04-backed index writes; OQ-PD05 attestation carrier |
| **05 Project Closure** | **Fully functional** — terminal outcomes doctrinal | RT-G04/10 persist closure metadata |

### Operational Model OR-readiness (pre-implementation)

| Criterion | Met without impl? |
|-----------|-------------------|
| OR-01 Foundation ACCEPTED for Core 5 | **Yes** |
| OR-02 Operator understands declaration model | **Yes** |
| OR-03 Intake → manifest-ready | **Yes** (doctrinal) |
| OR-04 Manifest → Tracking → Surface path | **Yes** |
| OR-05 Engine via declarations | **Yes** |
| OR-06 Core 5 classification | **Yes** |
| OR-07 Governance registers current | **Partial** — playbooks not listed in NEXT-PRIORITIES |

**Continuity verdict:** Website Factory **already operates** as documentation-first system for Core 5. Implementation ** improves** persistence and visibility — **does not unblock** a missing lifecycle doctrine.

**Playbooks that gain most from MVP impl:** 03 (Surface sessions), 04 (declaration persistence), 02 (catalog consistency).

**Playbooks least blocked today:** 01, 05 — enrollment and closure rituals complete without files.

---

## Implementation Readiness Assessment

| Dimension | Status | Evidence |
|-----------|--------|----------|
| Foundation documentation | **Ready** | 14 layers ACCEPTED/FROZEN |
| Engine documentation | **Ready** | Stages 1–6 + Boundary COMPLETE |
| Post-Engine doctrine | **Ready** | RT-G10/05/12 CHARTERED |
| Operational design | **Ready** | Operational Model + Playbooks 01–05 COMPLETE |
| Governance doctrine vs impl split | **Ready** | Governance Synchronization Pass 2026-06-04 |
| MVP scope definable | **Ready** | This review |
| Implementation charters (RT-G04/10/05/12) | **NOT STARTED** | Expected — next authorized deliverables |
| Physical artefacts in repo | **Absent** | Expected — explicit non-claims |
| HIGH documentation gaps | **None** for Core 5 | Architecture + Operational consolidation reviews |
| HIGH governance gaps | **None** in doctrine content | Register lag LOW (OD-04 analog) |
| Extended types / ecommerce legal | **Not ready** for impl pilot | Out of Core 5 MVP |

**Readiness question:** Is Website Factory ready for **MVP Implementation Planning** (authorized charters that define how to bind persistence — still not technical design in this doc)?

**Answer: Yes.**

**Blockers absent:**

- No unresolved authority conflict between Manifest / Registry / Surface / Playbooks.
- No missing lifecycle stage requiring new doctrine.
- Partial closure (formerly AG-06) closed by Playbook 05.

**Non-blockers (bounded):**

- OQ-R02 card template — first MVP charter input or optional operational binding.
- OQ-OM06/08 — integration/routing — post-MVP or parallel hygiene.
- NEXT-PRIORITIES not listing Implementation Planning era — register update at charter kickoff.

---

## Implementation Phases

Planning-level phases only — **no technical design**, **no artefact formats**.

### Phase 1 — Persistence + Manifest binding (MVP foundation)

**Goal:** Establish RT-G04 substrate and RT-G10 per-project physical manifest binding for one operator.

**Authorized planning outputs (future, not this deliverable):**

- RT-G04 implementation charter (persistence role, boundaries, non-goals).
- RT-G10 implementation charter (serialization scope, manifest-ready → physical binding rules).

**Depends on:** Doctrine complete ( satisfied ).

**Success signal (planning):** Operator can point to **one canonical persisted entry anchor** per Factory Project aligned with Playbook 01 outcomes.

**Explicitly excluded:** Registry catalog, UI, automation, validators.

### Phase 2 — Registry catalog binding (MVP portfolio)

**Goal:** RT-G05 implementation — physical catalog index listing Factory projects with Manifest pointers and distinction summaries.

**Authorized planning outputs:**

- RT-G05 implementation charter.
- Resolution of OQ-R01 (artefact vs distributed pointers) and optionally OQ-R02 (card template).

**Depends on:** Phase 1 stable manifest anchor + RT-G04.

**Success signal (planning):** Operator can discover enrolled projects from catalog without opening each workspace.

**Explicitly excluded:** Dashboard product, queue, multi-operator rules.

### Phase 3 — Tracking Surface read binding (MVP observability)

**Goal:** RT-G12 implementation — minimum operator read surface exposing eight visibility question classes for active project.

**Authorized planning outputs:**

- RT-G12 implementation charter (display binding, not UX program).
- Declaration/session persistence rules feeding Surface recency class (Playbooks 03–04).

**Depends on:** Phases 1–2 + Engine tracking composition data available to read path.

**Success signal (planning):** Operator completes Playbook 03 session using read surface instead of full-workspace search.

**Explicitly excluded:** Workflow engine, automated gate evaluation, CI integration, MIG.

### Post-Phase 3 horizon (not MVP — charter-gated)

```text
Phase 4+: RT-G07 logs → RT-G11 validators → RT-G08 MIG → RT-G06 queue → RT-G01/G03 automation
```

Each requires **separate operator charter** per RUNTIME-GAPS governance rule.

---

## Final Recommendation

### **A — Ready for MVP Planning**

**Justification:**

1. **Mission criteria met for planning authorization:** Foundation, Engine, post-Engine doctrine, Operational Model, and Playbooks 01–05 are **COMPLETE** per accepted artefacts and both consolidation reviews.
2. **MVP scope is definable without new doctrine:** RT-G04 → RT-G10 → RT-G05 → RT-G12 dependency graph is **bounded** and **consistent** with charters, RUNTIME-GAPS, and Engine System Boundary.
3. **Operational continuity proven:** Factory already runs documentation-first; implementation **binds** physical artefacts — **does not** prerequisite missing lifecycle work.
4. **Needs More Documentation (B) not chosen:** Residual items (OQ-R02, OQ-OM06/08, optional micro-playbooks) are **LOW–MEDIUM** optional bindings — addressable **inside** MVP charter kickoff, not blocking planning.
5. **Needs Governance Repair (C) not chosen:** Governance Synchronization Pass closed major doctrine/implementation split; remaining register lag (playbooks / Implementation Planning era not in NEXT-PRIORITIES) is **hygiene**, not doctrine conflict — disproportionate as sole next track.

**Immediate next authorized work (after this review — outside this deliverable):**

- Operator authorizes **MVP Implementation Planning charter pack** starting Phase 1 (RT-G04 + RT-G10 planning charters).
- Sync NEXT-PRIORITIES: Implementation Planning era **ACTIVE**; Operational Design → **COMPLETE**.
- Pilot constraint: **Core 5** site class only; single operator.

**Do not authorize yet:** RT-G01, RT-G03, RT-G09 impl, GG-07, or any automation that mutates Engine indexes without Playbook 04 operator act.

---

## Explicit Non-Claims

This review **does not** claim:

- Any **implementation spec**, storage model, UI design, schema, file format, folder layout, or code was created.
- A shipped Website Factory **runtime**, workflow engine, validator engine, persistence layer, or operator UI **exists** or **was designed** in this deliverable.
- RT-G04/05/10/12 **implementation** is complete or started because this planning review exists.
- MVP **has been built** — only **defined at planning level**.
- Physical manifest files, registry index, or declaration store **exist** in-repo.
- `projects/mars-website-factory/` v0 registries supersede `website-factory-reference-v1` v1.
- Extended site types, ecommerce legal extension, or MIG/MetaBOT/ORCA integrations are implementation-ready.
- Operators have updated NEXT-PRIORITIES to Implementation Planning era (**UNKNOWN** — not verified post-2026-06-05).
- Triumph or pilot workspaces are deploy-authorized or Factory-terminal in production sense.
- Any accepted artefact was modified — **audit/planning deliverable only**.

This review **does** claim (evidence-based):

- Website Factory documentation stack is **sufficient** to authorize MVP Implementation Planning for Core 5 single-operator path.
- **First implementation priority** at planning level: **RT-G04 → RT-G10 impl → RT-G05 impl → RT-G12 impl**.
- MVP **excludes** workflow engine, automation, validator CLI binding, queue, and Engine runtime product.
- All five operational playbooks **function before implementation**; MVP ** improves** persistence and Surface visibility.
- Residual documentation work is **bounded optional binding**, not missing core doctrine.
- Implementation and full runtime planes remain **NOT STARTED** per RUNTIME-GAPS and explicit non-claims across the stack.

---

*Website Factory Implementation Planning Review v1 — planning only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md`. Git: no commit, no push.*

---

# REPORT — Website Factory Implementation Planning Review v1
