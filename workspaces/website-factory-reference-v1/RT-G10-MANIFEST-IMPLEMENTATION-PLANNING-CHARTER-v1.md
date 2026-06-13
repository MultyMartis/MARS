# REPORT — RT-G10 Manifest Implementation Planning Charter v1

**Версия:** v1  
**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Planning — **RT-G10 planning charter only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Persistence Substrate Charter **COMPLETE**  
**Тип:** implementation **planning** charter only — **без** implementation, storage design, file design, schema design, yaml/json design, folder layout, runtime plan  
**Upstream:** [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), Operational Playbooks 01–05  
**Связь:** [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G10, [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md)

---

## Purpose

### Зачем существует Manifest implementation (RT-G10)

**RT-G10 Manifest Implementation** — архитектурная **роль физической привязки** доктрины Project Manifest для **одного** Factory Project. Implementation закрывает capability **C3** (MVP Definition Review) и устраняет gap между **doctrine-complete manifest-enrolled** (Playbook 01) и **operator path**, который сегодня зависит от ad-hoc scatter и workspace archaeology для entry anchor и minimum understanding.

| Операционная проблема | Как RT-G10 implementation решает (на уровне planning) |
|-----------------------|--------------------------------------------------------|
| Manifest Charter определяет **роль** entry anchor, но **не** физический носитель | RT-G10 определяет **что должно быть сериализовано** и **какие binding-обязательства** несёт implementation — **не** формат |
| Playbook 01 достигает **manifest-enrolled** без файла; MVP требует **persisted entry anchor** (S2, C3) | RT-G10 связывает doctrinal enrollment с **stable physical binding** на substrate RT-G04 |
| Operator не может указать **одну каноническую точку входа** per project без поиска по repo | RT-G10 обязан обеспечить **discoverable per-project manifest binding** aligned with MRDY-* |
| Registry и Surface предполагают **stable manifest pointer** (RA-04, RAP-16, Playbook 03 E4) | RT-G10 создаёт **anchor**, на который Registry catalog и Tracking read path **могут ссылаться** |

Manifest implementation — **implementation-plane responsibility** для per-project serialization standard **поверх** RT-G04 substrate — **без** переопределения Manifest Charter doctrine.

### Нормативная формулировка роли (planning)

**RT-G10 Manifest Implementation** — архитектурная **роль authorized physical binding** Manifest doctrine (entry anchor, minimum understanding categories, reference topology pointers) для одного Factory Project, **вне** Engine documentation boundary (ES-04), **на** RT-G04 Persistence Substrate, **внутри** MVP capability floor (C3) и TOPOLOGY-B-v1 constraints.

RT-G10 **сам по себе не выбирает storage product** — он **определяет implementation responsibility** для manifest binding, которую **следующий** authorized track (implementation charter / spec) **может** материализовать без нарушения MA-*, MT-*, MAP-*.

### Что RT-G10 implementation **не** решает

| Не решает | Владелец / gap |
|-----------|----------------|
| «Что такое Manifest» doctrinally | [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) — **COMPLETE** |
| Где **физически** живут Factory records (locus, zone) | [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) — substrate, не serialization |
| Portfolio catalog, multi-project index | RT-G05 Registry implementation |
| Eight visibility questions, operator read surface | RT-G12 Surface implementation |
| Live gate/handoff/state indexes, progression ledger | Engine Tracking + Playbook 04 writes on substrate |
| Movement execution, gate evaluation, automation | RT-G01, RT-G03, RT-G11 — **forbidden in MVP** |
| Manifest enrollment ritual, MRDY attestation steps | Playbook 01 — **doctrine-complete** |
| Closure terminal metadata **as primary owner** | Playbook 05 + substrate P6; RT-G10 **may reference**, not own closure plane |

**Planning boundary:** RT-G10 closes **per-project entry binding gap** — **не** Factory runtime, **не** persistence substrate charter, **не** portfolio or observability products.

---

## Foundation Dependencies

Manifest Implementation Planning Charter **наследует** завершённый Engine v1, post-Engine charters, Operational Design, MVP Definition, RT-G04 charter; **не изменяет** Foundation, Runtime, Engine Stages 1–6, Manifest Charter, Playbooks 01–05.

### Tier 0 — Decision and review chain

| Document | RT-G10 planning использует |
|----------|---------------------------|
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C3 manifest persistence; S2 success; dependency C2→C3→C4/C5 |
| [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md) | RT-G10 impl scope; Playbook 01 binding; sequencing after RT-G04 |
| [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) | P2 manifest binding carrier; MR-REL-01; substrate hosts, RT-G10 serializes |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-01/02/03/06 |

### Tier 1 — Manifest doctrine (authoritative — do not redesign)

| Document | Constraint on RT-G10 |
|----------|------------------------|
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | MRDY-*, Categories 1–8, MA-*, MT-*, MR-*, ST-*, MAP-* — **sole source** of manifest scope |
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Identity shell; mandatory components — Manifest serves Object, not replaces |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04 external persistence; BV-03, BV-15 forbidden doc classes |

### Tier 2 — Operational doctrine

| Document | RT-G10 planning использует |
|----------|---------------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; operator path Registry→Manifest→Tracking→Surface; OR-03 manifest-ready ⊄ file |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — enrolled outcome; physical file **not** blocking ritual; MRDY evaluation |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — manifest-enrolled precondition; pointer dependency |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — manifest entry anchor reachable (E4, MRDY-06) |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — manifest-enrolled prerequisite P1 |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — manifest enrollment never revoked; orientation may evolve |

### Tier 3 — Neighbor charters (relationship only)

| Charter | Document | RT-G10 boundary |
|---------|----------|-----------------|
| Registry (RT-G05 doctrine) | [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | MR-01, RA-04 — registry **follows** manifest anchor |
| Tracking Surface (RT-G12 doctrine) | [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | TS-02, PO-*, SRDY-* — Surface **assumes** manifest entry, **does not** redefine |

**Authority precedence:** Foundation Freeze + Engine Readiness Audit → Engine Stages 1–6 → Manifest Charter (doctrine) → RT-G04 Substrate Charter → **этот planning charter** для RT-G10 implementation responsibility → **будущий** RT-G10 implementation standard **не может** нарушить MAP-01, MT-01, MA-01, OA-ACT-04, ES-04.

---

## Manifest Implementation Responsibility

### Что RT-G10 **must provide** (capability-level)

Implementation responsibility derives **only** from Manifest Charter scope categories and MVP C3 — **без** inventing new doctrine.

| # | Capability | Doctrine anchor | Planning obligation |
|---|------------|-----------------|---------------------|
| IM-01 | **Per-project physical manifest binding** — one stable entry anchor per Factory Project on RT-G04 substrate | MRDY-06; C3; S2; Playbook 01 | Operator can identify **one canonical** persisted entry point aligned with manifest-enrolled outcome |
| IM-02 | **MRDY-* category binding** when MVP physically binds — all seven readiness categories materializable from bound record | MRDY-01…07; Manifest §Manifest-ready | Physical bind **implies** orientability categories explicit — not merely empty placeholder |
| IM-03 | **Stable identity reference binding** (Category 1) | MRDY-01; Object Model identity shell | Distinct from registry entry ID (ES-03, RA-03) |
| IM-04 | **Charter & scope tier binding** (Category 2) | MRDY-02; ST-01 stable categories | Supports scope tier, exclusions, operator assignment **categories** |
| IM-05 | **Declared lifecycle endpoint binding** (Category 3) | MRDY-03; ML-01 | Endpoint explicit at bind — no implicit ambiguity |
| IM-06 | **Scope applicability doctrine binding** (Category 4) | MRDY-04 | Full chain vs partial with exclusions acknowledged |
| IM-07 | **Reference topology pointer binding** (Category 7) | MRDY-05; MA-01 map-of-maps | Pointers to state/gate/artefact authoritative loci — **refs only**, not bodies |
| IM-08 | **Enrollment precedence discipline** | Playbook 01; MR-REL-01 | Doctrinal manifest-enrolled **precedes** physical bind; bind **follows** operator enrollment act |
| IM-09 | **Stability class honor** | ST-01, ST-02 | Stable categories amend via explicit operator declaration path — not silent overwrite |
| IM-10 | **Anti-pattern guards carried forward** | MAP-01…MAP-15; MT-01; MA-03 | Implementation planning **must** bound serialization to entry/minimum understanding — **reject** passport, second tracking SoT, live gate index in manifest binding |
| IM-11 | **Optional bounded extension** (planning-bound only) | OQ-M01; MT-02; ES-04 | **May** plan serialization of **selected** Tracking zones **only** under separate implementation charter decision — **must not** default to full tracking duplication |

**Planning rule MI-01:** если отсутствие physical manifest binding **ломает** operator ability to satisfy Playbook 01 post-MVP success (S2), Registry pointer stability (RA-04), or Playbook 03 prerequisite E4 **without workspace archaeology** — obligation **входит** в RT-G10 responsibility scope.

### Что RT-G10 **must not provide** (remains outside)

| Outside RT-G10 | Actual owner |
|----------------|--------------|
| Persistence substrate locus, authorized zone, P1–P8 substrate classes **as substrate design** | RT-G04 charter + RT-G04 implementation track |
| Portfolio catalog binding, RRDY-* | RT-G05 implementation |
| Eight Surface questions read binding, SRDY-* display | RT-G12 implementation |
| Engine instance indexes (state, gates, handoffs, artefacts) **as authoritative live index** | Tracking Model + Playbook 04 on substrate |
| Gate/handoff **criteria**, Runtime vocabulary | Runtime + Foundation |
| Manifest enrollment workflow steps, MRDY attestation ritual | Playbook 01 |
| Automated manifest creation on folder/git discovery | Forbidden — RD-04, RAP-10 analog |
| Closure metadata **primary** persistence design | Substrate P6; Playbook 05 — RT-G10 **orientation refs only** |
| Layer artefact bodies, Legal Pack, handoff payloads | T1 Foundation / external |

**Planning rule MI-02:** RT-G10 defines **manifest serialization responsibility**, not **Factory Project existence** — logical Factory Project precedes physical manifest (Object Model, Playbook 01 recognition).

### Doctrine vs physical binding (planning distinction)

| Layer | Status | RT-G10 scope |
|-------|--------|--------------|
| **Doctrinal** manifest-enrolled | Playbook 01 outcome today — **COMPLETE** operatively | RT-G10 **does not replace** enrollment ritual |
| **Physical** manifest binding | MVP C3 — **NOT STARTED** | RT-G10 **must plan** bind rules linking enrolled state → persisted anchor |
| **Manifest-ready (MRDY-*)** | Evaluated at enrollment | RT-G10 bind **must reflect** categories already attested — not re-invent intake |

---

## Manifest Readiness Binding

MRDY-* concepts govern **doctrinal orientability**; RT-G10 planning determines **how readiness relates to implementation** — **without** defining formats, fields, or storage labels.

### MRDY → implementation planning mapping

| ID | Doctrinal criterion (Manifest Charter) | RT-G10 planning binding rule |
|----|----------------------------------------|------------------------------|
| **MRDY-01** | Stable project identity category explicit | Physical bind **must** carry stable logical identity reference — **not** conflated with registry entry ID |
| **MRDY-02** | Charter & scope tier explicit | Bind **must** persist charter/scope **categories** sufficient for orientability — minimal intake allowed |
| **MRDY-03** | Declared lifecycle endpoint explicit | Bind **must** record endpoint category — full chain default or partial with acknowledged boundary |
| **MRDY-04** | Scope applicability doctrine explicit | Bind **must** make full vs partial applicability **explicit** — aligns with LR-07 mask category |
| **MRDY-05** | Reference topology declared | Bind **must** include topology **pointers** (Category 7) — where state, gate, artefact truths live |
| **MRDY-06** | Manifest entry anchor identified | **Core MVP obligation:** physical bind **is** the materialization of entry anchor — doctrinal identification becomes **discoverable locus** on substrate |
| **MRDY-07** | Operator understands Manifest ≠ Passport ≠ Registry | **Doctrinal** — not a serialized field; Playbook 01 attestation **precedes** bind; implementation **must not** create Passport or registry-substitute artefact |

### Readiness relationships (unchanged by planning)

| Concept | Meaning for RT-G10 |
|---------|-------------------|
| **Manifest-ready** | Threshold for Playbook 01 enrollment — **prerequisite** for physical bind, not replaced by it |
| **Manifest-ready ⊄ fully trackable** | Early bind at `NEW_PROJECT` with empty gate indexes — **valid** |
| **Manifest-ready ⊄ surface-ready** | Physical manifest bind **does not** imply SRDY-* — Tracking indexes separate |
| **Physical bind ⊄ manifest-enrolled retroactively** | Enrollment decision **precedes** bind moment (OQ-ME05 — **OPEN** for implementation charter timing, not blocking planning) |

### Stability binding (Categories stable vs evolving)

| Stability class | Manifest Charter | RT-G10 planning rule |
|-----------------|------------------|----------------------|
| **Expected stable** (identity core, charter intent, scope tier, endpoint, pins) | ST-01 | Physical bind **must** preserve amendment narrative — silent overwrite **forbidden** |
| **Expected evolving** (current position summary, classification bindings, ref targets) | ST-02 | Bind **may** surface evolving categories as **pointers** to Tracking — **must not** freeze live gate index into «stable» manifest (MAP-05, ST-02) |

### Principle MRB-01 — Readiness categories bind; readiness ritual does not move

Playbook 01 **owns** MRDY attestation. RT-G10 **owns** faithful physical representation of attested categories — **not** re-evaluation gates, **not** automated MRDY pass.

### Principle MRB-02 — MRDY-06 is the MVP hinge

Success criterion S2 («one canonical persisted entry anchor») **maps directly** to MRDY-06 physical materialization. RT-G10 planning is **incomplete** if MRDY-06 binding obligation is ambiguous.

---

## RT-G04 Relationship

RT-G04 **enables** RT-G10; RT-G10 **consumes** RT-G04; Manifest Charter **neither is nor owns** storage (MAP-01).

### Consumption model (planning)

```text
  RT-G04 SUBSTRATE                    RT-G10 MANIFEST IMPLEMENTATION
  (persistence locus)                 (serialization responsibility)
         │                                      │
         │  provides per-project record home    │  defines WHAT manifest categories bind
         │  (P1, P2, authorized zone DF-03)     │  defines bind rules vs Playbook 01
         │                                      │
         └──────────── hosts ──────────────────▶ manifest binding carrier (P2)
```

| RT-G04 provides | RT-G10 consumes (planning) |
|-----------------|----------------------------|
| Stable per-project physical locus (P1) | Manifest binding **placement** on substrate — **not** layout design here |
| Manifest binding carrier class (P2) | Entry anchor + MRDY-* category persistence obligation |
| Charter-bound stable categories class (P7 subset) | Overlap Categories 2–4 — RT-G10 **serializes** manifest-facing subset |
| External ref discipline (P8) | Topology pointers — refs only |
| Human-only write path for declarations (PS-03) | Manifest bind writes **distinct** from Playbook 04 index writes — enrollment/bind acts **operator-controlled** |

### RT-G04 obligations RT-G10 depends on

| Substrate obligation | RT-G10 dependency |
|----------------------|-------------------|
| P2 — Manifest binding carrier | **Hard** — RT-G10 cannot exist without substrate locus |
| MR-REL-01 — Substrate precedes serialization, follows enrollment | Bind **after** doctrinal enrolled |
| Precedence: manifest before registry on substrate | RT-G10 anchor **must** exist **without** registry entry |
| Separation from live gate index on disk (MT-01) | RT-G10 **must not** plan manifest-as-second-tracking-store |

### RT-G04 forbidden overlap (RT-G10 must respect)

| Forbidden | Reason |
|-----------|--------|
| RT-G10 defining substrate zone structure | RT-G04 charter — DF-03 only |
| RT-G10 owning P4–P6 (indexes, declarations, closure) **as manifest scope** | Tracking/Playbook 04/05 territory — **cross-ref only** |
| Manifest bind auto-mutating Engine indexes | OA-ACT-04, SC-03 |

### Open co-location (bounded for implementation charter)

| ID | Question | RT-G10 planning disposition |
|----|----------|----------------------------|
| **OQ-M04** | Manifest vs tracking record co-location on substrate | **OPEN** — resolved in RT-G10 **implementation** charter, not here |
| **OQ-M01** | Which Tracking zones **may** serialize via RT-G10 | **OPEN** — optional extension; default **exclude** live gate/handoff index |

**Principle G04-REL-01:** RT-G04 answers **where** Factory records live; RT-G10 answers **what manifest binding means** on that locus — **orthogonal** planning planes.

---

## Registry Relationship

Registry **depends on** Manifest; RT-G10 **enables** stable manifest pointer for catalog — **without** catalog design.

### What Registry depends on from Manifest implementation

| Registry need | Doctrine anchor | RT-G10 planning obligation |
|---------------|-----------------|----------------------------|
| Stable **pointer to Manifest entry** per project | RA-04, RAP-16, MR-02 | Physical manifest anchor **discoverable** and **stable** for catalog slot linkage |
| Logical Factory Project identity **precedes** registry entry ID | ES-03, RA-02, RA-03 | Manifest bind carries **logical identity** — registry slot **references**, not replaces |
| Manifest enrollment **precedes** catalog enrollment | Playbook 01→02, RD-02, RET-03 | RT-G10 bind **should** exist before or with registry impl — **registry impl must not precede** stable manifest anchor (REG-REL-01) |
| Distinction summaries at catalog level — **not** manifest depth | RA-05, RRDY-* | RT-G10 **does not** populate registry card — **only** supplies anchor target |

### What Registry knows that Manifest implementation does not own

| Registry scope | RT-G10 exclusion |
|----------------|----------------|
| Cross-project listing, discoverability status, withdrawal/archived | RT-G05 impl |
| Queue position, prioritization | RT-G06 |
| Orientation snapshot on card (non-authoritative) | Derived from Tracking read — RS-03 |

### What Manifest implementation provides that Registry does not

| Manifest bind scope | Registry exclusion |
|---------------------|-------------------|
| Per-project minimum understanding categories | Registry holds **index cards**, not full charter intent |
| Authoritative reference topology for **one** case | Registry **points to** manifest entry |
| Entry anchor «start here» doctrine | Registry answers «which projects» — RE-01 |

### Dependency edge (planning)

```text
  Playbook 01 ──▶ manifest-enrolled (doctrinal)
         │
         ▼
  RT-G10 impl ──▶ physical manifest anchor on RT-G04
         │
         ▼
  Playbook 02 / RT-G05 impl ──▶ catalog entry with Manifest pointer
```

**Principle REG-REL-02:** RT-G10 planning **must not** absorb registry enrollment workflow (Playbook 02) or RRDY-* evaluation — **pointer stability only**.

**Principle MR-01 (inherited):** Registry follows Manifest doctrine, not vice versa — RT-G10 **must not** require registry entry for manifest bind.

---

## Tracking Relationship

Tracking composition **owns** instance indexes; Manifest **precedes** deep tracking read; RT-G10 **must not** duplicate Tracking (MT-01).

### What Tracking / Surface may assume from Manifest implementation

| Assumption | Consumer | Planning basis |
|------------|----------|----------------|
| Manifest entry anchor **reachable** (discoverable locus) | Playbook 03 prerequisite E4; MRDY-06 | RT-G10 **must** make anchor operator-locatable without repo-wide search |
| Manifest-ready categories **already attested** at enrollment | Playbook 03 OR-01 — session **confirms**, not re-teaches MRDY-07 | Bind reflects prior attestation |
| Reference topology pointers **exist** for authoritative sources | Surface PO-* — pointer only, not full map essay | Category 7 bind supplies **targets** Tracking/Surface read |
| Active state in manifest orientation **matches** Engine or flagged invalid | MS-02 | If Category 6 surfaced in bind — **pointer only**, reconcilable |
| Manifest **does not** hold live gate/handoff index | MT-01, SRDY-09, MAP-05 | Tracking remains **sole** live observability composition |

### What Tracking knows that Manifest implementation must exclude

| Tracking knowledge | Why excluded from manifest bind |
|--------------------|--------------------------------|
| Full gate outcome index with STALE/INVALID | Gate Composition + Tracking — MAP-05 |
| Complete handoff event sequence | Handoff Binding + Tracking |
| Artefact ref index exhaustiveness | AV-* — Surface Tier S-B |
| Eligibility snapshot, open gate set | Derived — DR-01 |
| Append-only audit trail detail | AT-* — Playbook 04 |
| Eight Surface question **answers** | SRDY-* — RT-G12 read binding |

### Tracking zones serialization (planning-bound)

Manifest Charter MT-02 and OQ-M01: RT-G10 implementation **may** serialize **selected** Tracking zones under **separate** implementation charter — **this planning charter**:

- **Bounds** the question — does **not** answer which zones
- **Defaults** to **minimum** manifest categories only — **exclude** live gate/handoff index unless explicitly authorized later
- **Requires** MT-01 guard if any zone serialization planned

**Principle TRK-REL-01:** Surface-ready ⊇ manifest-ready ⊄ manifest bind complete — indexes for SRDY-* remain **substrate P4** + RT-G12 read path, **not** manifest duplication.

### Playbook consumption

| Playbook | Manifest implementation touchpoint |
|----------|-----------------------------------|
| **01** | Enrolled → triggers physical bind obligation (MVP) |
| **03** | Assumes anchor reachable — **read** manifest entry, depth in Tracking |
| **04** | Updates indexes on substrate — **separate write plane** from manifest enrollment bind |
| **05** | Manifest enrollment **never revoked** — orientation categories may evolve; bind **persists** as historical anchor |

---

## Authority Model

Authority principles derive **only** from accepted Manifest Charter, Operational Model, and Playbooks — **no new authority classes**.

### Who owns Manifest truth

| Truth class | Owner | RT-G10 planning implication |
|-------------|-------|----------------------------|
| **Entry-point doctrine** (what Manifest **is**) | Manifest Charter — **COMPLETE** | RT-G10 **implements binding**, not role redefinition |
| **Minimum understanding categories** (MRDY-*, Categories 1–8) | Manifest Charter | Serialization **maps to** categories — **cannot add** mandatory components (Object Model) |
| **Manifest-enrolled outcome** | Operator via Playbook 01 | Bind **follows** enrollment declaration — not discovery |
| **Charter content** (intent, exclusions, scope) | Operator-authored charter (sponsor input) | Bind **indexes** charter category — **not** Foundation authority |
| **Last declared state/gate/handoff truth** | Engine tracking planes (MA-02) | Manifest bind **points** — **does not own** declaration truth |
| **Stable category amendments** | Operator explicit declaration (ST-01, AT-01 analog) | Bind **must** preserve amendment narrative — implementation charter resolves **how**, not **whether** |

### Who may modify Manifest reality

| Actor | Permitted (v1) | Forbidden |
|-------|----------------|-----------|
| **Factory operator** | Playbook 01 enrollment; charter amendments; manifest bind/update acts aligned with enrollment | Automated bind without attestation |
| **Reviewer** | Audit MRDY checklist — **not** replace enrollment attestation | Declare manifest-enrolled |
| **External systems** (CI, agents, git hooks) | **None** for manifest bind authority | Auto-create/update manifest on scan |
| **Registry workflow** | **None** for manifest content | Catalog side-effect creating manifest |
| **Tracking/Surface impl** | **Read** manifest bind | Write authoritative indexes via manifest channel |

### Inherited principles (non-negotiable in planning)

| ID | Principle | RT-G10 guard |
|----|-----------|--------------|
| **MA-01** | Manifest is anchor, not aggregator of authority | Bind = orient + point — **not** merge Legal/Runtime bodies |
| **MA-02** | Declaration truth stays in Engine | Playbook 04 owns index mutation — **not** manifest file |
| **MA-03** | Manifest ≠ Passport | **Forbidden** parallel SoT artefact |
| **OA-ACT-04** | External systems never mutate without operator act | No auto-bind |
| **MT-01** | No duplicated tracking | No live gate index in manifest bind scope |

**Principle AUTH-01:** Physical manifest binding **extends operability** of doctrine — **does not transfer** Engine declaration authority to manifest storage.

---

## Boundary Protection

RT-G10 Manifest Implementation **must never become** следующие системы — по Manifest Charter anti-patterns, MVP exclusions, Engine boundary, RT-G04 separation.

### Core forbidden roles

| Forbidden system | Why | Guard anchor |
|------------------|-----|--------------|
| **Registry / portfolio catalog** | MR-02, MAP-07; RT-G05 separate | Catalog listing, RRDY-*, withdrawal — **out of scope** |
| **Tracking composition / live observability index** | MT-01, MAP-05 | Gate/handoff/history index — **Tracking only** |
| **Tracking Surface / operator dashboard** | MAP-09, TS-01; RT-G12 separate | Eight questions display — **read consumer** |
| **Persistence substrate product** | MAP-01; RT-G04 owns locus | Substrate design, zone layout — **not RT-G10** |
| **Database / query engine / multi-tenant store** | MAP-02; MVP file-backed sufficient | DB-as-manifest — **rejected** |
| **Workflow engine / state machine executor** | MAP-04, MAP-12; RT-G01 | Transitions via manifest — **forbidden** |
| **Factory runtime product** | SC-01; RT-G09 | «Manifest drives execution» — **rejected** |
| **Gate Results System** | MAP-10 | Gate outcomes in manifest bind — **forbidden** |
| **Passport / unified project mega-document** | MAP-06, BV-15 | Second SoT — **explicitly rejected** |
| **Project management system** | Scope creep | Tasks, sprints, assignments beyond charter category — **out of scope** |
| **Automation / agent enrollment** | Playbook 01 forbidden automation | Discovery bind — **forbidden** |
| **Foundation authority merge** | MAP-08, BV-03 | Embedding Legal Pack, Site Type Registry matrices — **forbidden** |
| **Handoff package / artefact body store** | MAP-11 | Payload storage — **refs only** |
| **Closure registry / terminal workflow engine** | Playbook 05 scope | Closure metadata primary — **substrate P6** |

### Architectural anti-patterns RT-G10 planning must resist

| Anti-pattern | Guard |
|--------------|-------|
| Manifest impl conflated with «shipped Factory runtime» | MVP explicit non-claims; C3 ≠ RT-G09 |
| Serialization design smuggled into **this** planning charter | Task charter forbidden list |
| Manifest owns live gate index on substrate | MT-01, SC scope creep MAP-05 |
| Physical bind **before** doctrinal enrollment | MR-REL-01, Playbook 01 ordering |
| Registry impl precedes manifest anchor | REG-REL-01, Implementation Planning Review order |
| Manifest bind replaces Playbook 04 declaration path | DA-01, C6 |
| `COMPLETE` / deploy conflated with manifest «completion» | MAP-13, MS-04 |

### Additional justified non-responsibilities

| Role | Rationale |
|------|-----------|
| Validator / gate authority engine | RT-G11 — post-MVP |
| Queue / scheduler | RT-G06 |
| MIG / external pipeline SoT | RT-G08 |
| Notification / webhook hub | RT-G13 |
| Rollback automation executor | RT-G15 |
| Site Type Registry operations | RAP-11 — Foundation T1 |
| Layer generation / frontend build | GG-* — external product plane |

**Principle BP-01:** RT-G10 is **per-project manifest serialization responsibility** — **one plane**, **one project**, **entry + minimum understanding** — not a platform.

---

## Readiness Model

### When RT-G10 **planning charter** is complete

RT-G10 Manifest Implementation Planning Charter v1 считается **planning-complete** когда:

| Criterion | Status in this deliverable |
|-----------|---------------------------|
| Purpose defined — C3 gap, entry anchor, vs doctrine-only baseline | **Yes** |
| Implementation responsibility — must provide / must not provide | **Yes** — IM-*, MI-* |
| MRDY-* binding rules without format design | **Yes** — MRB-* |
| RT-G04 consumption model — hosts vs serializes | **Yes** — G04-REL-01 |
| Registry dependency — pointer stability, ordering | **Yes** — REG-REL-* |
| Tracking assumptions — MT-01, no duplication | **Yes** — TRK-REL-* |
| Authority model — operator, Playbook 01, MA-* | **Yes** — AUTH-* |
| Boundary protection — forbidden roles explicit | **Yes** — BP-* |
| Future implementation implications identified | **Yes** — see below |
| Explicit non-claims — no schemas, files, storage layout | **Yes** |

### What planning-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| RT-G10 **implementation** started or complete | Separate authorized track |
| Physical manifest artefacts **created** | Forbidden in planning scope |
| Serialization format **selected** | RT-G10 implementation charter / standard |
| OQ-M01, OQ-M04, OQ-ME05 **resolved** | Bounded OPEN for implementation charter |
| MVP **demonstrated** | S1–S9 post-implementation |
| RT-G05 or RT-G12 planning **complete** | Separate charters |

### Planning-complete vs implementation-ready

```text
  Manifest Charter v1 (doctrine) ── COMPLETE
           │
           ▼
  RT-G04 Persistence Substrate Charter v1 ── COMPLETE
           │
           ▼
  RT-G10 Manifest Implementation Planning Charter v1 ── THIS (planning-complete)
           │
           ▼
  RT-G10 Manifest Implementation Standard (implementation charter) ── NEXT authorized track
           │
           ├──▶ RT-G05 Registry Implementation Planning Charter
           │
           └──▶ RT-G12 Surface Read Binding Implementation Planning Charter
```

**Principle RDY-01:** Loss of RT-G10 planning clarity **must not** block Manifest doctrine or Playbook 01 — doctrine **already operable** without physical bind.

**Principle RDY-02:** MVP S2 success **requires** RT-G10 implementation **after** this planning charter — not planning alone.

---

## Future Implementation Implications

Без implementation design — **logical successors and dependency edges only**.

### Immediate successor (Tier 1)

| Next charter | Role | Depends on | Must carry forward |
|--------------|------|------------|-------------------|
| **RT-G10 Manifest Implementation Standard** (implementation charter — **not this doc**) | Serialization scope, bind moment rules (OQ-ME05), co-location policy (OQ-M04), optional zone serialization (OQ-M01), operator write path for bind/amendment | This planning charter + RT-G04 substrate impl + Manifest Charter | MA-*, MT-*, MAP-*, MRDY-*, Playbook 01, OA-ACT-04 |

**Success signal (from Implementation Planning Review):** Operator points to **one canonical persisted entry anchor** per Factory Project aligned with Playbook 01 outcomes.

### Parallel / sequential successors (MVP sequence)

| Charter | Relationship to RT-G10 | Sequencing rule |
|---------|------------------------|-----------------|
| **RT-G05 Registry Implementation Planning Charter** | Consumes stable manifest pointer; **must not precede** RT-G10 anchor | After RT-G10 planning + manifest impl track authorized |
| **RT-G12 Surface Read Binding Implementation Planning Charter** | Reads substrate including manifest anchor + indexes; **must not precede** RT-G10/04 stability | After RT-G10; may parallel RT-G05 |
| **RT-G04 Implementation** (physical substrate artefacts) | **Enables** all bindings — if distinct from charter-only | Substrate **before or with** RT-G10 impl — C2→C3 |

### Post-MVP (not blocked by RT-G10 planning)

| Item | Notes |
|------|-------|
| RT-G07 Execution logs | May share substrate — separate charter |
| RT-G11 Validator CLI | Gate **aid** — must not replace Playbook 04 |
| OQ-M02 partial closure manifest category | Playbook 05 + implementation standard |
| OQ-M03 PHASE_SLICE multi-manifest | Engine v2 or implementation standard |

### MVP operator path after RT-G10 impl (planning reference)

```text
  Playbook 01 ──▶ manifest-enrolled
         │
         ▼
  RT-G10 impl ──▶ physical manifest anchor persisted (C3, S2)
         │
         ├──▶ Playbook 02 / RT-G05 ──▶ catalog with Manifest pointer
         │
         └──▶ Playbook 03 / RT-G12 ──▶ Surface reads bound data
                    │
                    ▼
              Playbook 04 ──▶ index writes on substrate (separate plane)
                    │
                    ▼
              Playbook 05 ──▶ closure metadata (substrate P6)
```

**Principle FUT-01:** RT-G10 implementation standard **must not** authorize automated index mutation, workflow engine hooks, or registry auto-enrollment as side effects of manifest bind.

---

## Explicit Non-Claims

This document and the RT-G10 Manifest Implementation **planning** role it defines:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** **storage design**, **database design**, **file format**, **JSON/YAML schema**, **folder structure**, or **physical MVP artefacts**;
- **are not** **implementation spec**, **serialization standard**, or **code**;
- **are not** **operator UI**, **dashboard**, or **CLI** (RT-G12);
- **are not** **Registry** (RT-G05) or **Tracking Surface** (RT-G12 doctrine) redesign;
- **are not** **Persistence Substrate** (RT-G04) redesign — only **consumption** relationship;
- **are not** **Manifest Charter** rewrite — doctrine taken as authoritative input;
- **are not** Playbooks 01–05 rewrite;
- **do not** define manifest file paths, field lists, database tables, or co-location layout;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** claim physical manifest records **exist** in-repo — **planning charter only**;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound manifest;
- **do not** claim RT-G10 **implementation** is authorized beyond **planning** by existence of this document alone.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01.

---

## Open Questions

Charter **bounds** questions for **future RT-G10 implementation standard** — **does not answer** serialization choices.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-M01** | Which Tracking zones **may** serialize into physical Manifest binding | **OPEN** — RT-G10 implementation standard; default **exclude** live indexes |
| **OQ-M02** | Partial closure metadata — Manifest category vs Tracking flag only | **OPEN** — Playbook 05 + implementation standard |
| **OQ-M03** | PHASE_SLICE / multi-`generation_id` — one manifest bind per shell vs per slice | **OPEN** — Engine v2 or implementation standard |
| **OQ-M04** | Physical co-location of Manifest bind vs tracking records on substrate | **OPEN** — RT-G10 implementation standard |
| **OQ-M05** | Registry card fields derived from Manifest categories | **OPEN** — RT-G05 planning/implement |
| **OQ-M06** | External workspace pointer as Manifest category vs tracking-only | **OPEN** — operational + implementation |
| **OQ-M07** | `PASS_WITH_WARNINGS` — Manifest orientation category | **OPEN** — validation binding |
| **OQ-M08** | Chrome blocks without `block_id` — Manifest binding category | **OPEN** |
| **OQ-M09** | Minimum progression record exposure via Manifest vs Tracking-only | **BOUNDED** — progression stays State/Tracking; Manifest points |
| **OQ-ME05** | Physical bind moment vs doctrinal Enrolled timing | **OPEN** — RT-G10 implementation standard |
| **DF-04…DF-10** | Substrate workshop inputs affecting manifest bind | **OPEN** — cross-charter implementation planning |

**Resolved by upstream (not open in this planning scope):** Manifest doctrine (MRDY-*, Categories 1–8); Playbook 01 enrollment without file blocking; RT-G04 authorized zone DF-03; MVP includes C3 manifest persistence; Registry depends on manifest anchor (MR-01, RA-04).

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G10 Manifest Implementation Planning Charter v1** as **RT-G10 planning role complete** — gap RT-G10 in RUNTIME-GAPS remains **NOT STARTED** for **implementation**, not for planning.
2. **Authorize next track:** **RT-G10 Manifest Implementation Standard** (implementation charter) — serialization scope, bind rules, co-location, optional zone policy — **still requires** separate authorization; **must** carry MAP-*, MT-*, MRDY-*, Playbook 01 forward.
3. **Preserve sequencing:** RT-G10 implementation standard **before** RT-G05 registry implementation planning that assumes stable manifest pointer; RT-G04 substrate artefacts **available** for bind demonstration.
4. **Do not create yet:** manifest yaml/json samples, folder trees under `workspaces/website-factory-operations/`, schemas, passport documents, manifest-as-gate-index prototypes, registry-in-manifest merges.
5. **Optional P3:** Update RUNTIME-GAPS RT-G10 line to «PLANNING CHARTERED» — **operator action**, outside this deliverable.

**Engine Architecture v1 requires no further architecture stages.** RT-G10 planning charter is **post-RT-G04, post-MVP-definition** documentation.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` path **exists** on disk today | **UNKNOWN** — RT-G04 charter records zone; physical creation not part of this deliverable |
| Calendar for RT-G10 implementation standard authorization | **not scheduled** |
| De-facto ad-hoc manifest discipline already used by operators | **UNKNOWN** — OQ-OM01 analog |
| Triumph / pilot workspaces as manifest bind targets vs external-only refs | **UNKNOWN** — per case (DF-08) |
| Operators updated NEXT-PRIORITIES to RT-G10 planning-complete era | **UNKNOWN** |

---

*RT-G10 Manifest Implementation Planning Charter v1 — RT-G10 planning complete. Planning charter only. Canonical location: `workspaces/website-factory-reference-v1/RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G10 Manifest Implementation Planning Charter v1

**Stage:** Implementation Planning — RT-G10 Manifest Implementation Planning Charter  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md` (created)  
**Summary:** Определена planning-ответственность RT-G10 Manifest Implementation: физическая привязка Manifest doctrine (entry anchor, MRDY-*, reference topology) на RT-G04 substrate для MVP C3; границы must/must-not vs Registry, Tracking, Playbooks; authority model (operator, Playbook 01, MA-*); boundary protection от registry/tracking/runtime/passport; readiness planning-complete vs implementation successor; без storage, schemas, files, yaml/json, implementation design.  
**Git:** no commit, no push (per task charter).
