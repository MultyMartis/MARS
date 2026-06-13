# REPORT — RT-G05 Registry Implementation Planning Charter v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Planning — **RT-G05 planning charter only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Persistence Substrate Charter **COMPLETE**; RT-G10 Manifest Implementation Planning Charter **COMPLETE**  
**Тип:** implementation **planning** charter only — **без** implementation, storage design, file design, schema design, catalog structure design, yaml/json design, folder layout, runtime plan  
**Upstream:** [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md), Operational Playbooks 01–05  
**Связь:** [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G05, [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md)

---

## Purpose

### Зачем существует Registry implementation (RT-G05)

**RT-G05 Registry Implementation** — архитектурная **роль физической привязки** доктрины Factory Project Registry для **мультипроектного portfolio view**. Implementation закрывает capability **C4** (MVP Definition Review) и устраняет gap между **doctrine-complete catalog-discoverable** (Playbook 02) и **operator path**, который сегодня зависит от ad-hoc scatter и workspace archaeology для ответа на вопрос «какие Factory projects существуют и как их отличить».

| Операционная проблема | Как RT-G05 implementation решает (на уровне planning) |
|-----------------------|--------------------------------------------------------|
| Registry Charter определяет **роль** мультипроектного каталога, но **не** физический носитель | RT-G05 определяет **что должно быть сериализовано** на уровне catalog binding и **какие binding-обязательства** несёт implementation — **не** формат и **не** структуру каталога |
| Playbook 02 достигает **catalog-discoverable** без файла; MVP требует **persisted portfolio listing** (S3, C4) | RT-G05 связывает doctrinal catalog enrollment с **stable physical binding** на substrate RT-G04 |
| Operator не может перечислить enrolled Factory projects **без** обхода каждого workspace | RT-G05 обязан обеспечить **discoverable portfolio catalog** aligned with RRDY-* и RD-* |
| Tracking Surface и supervision sessions предполагают **portfolio select → Manifest → Tracking** (OR-04, Playbook 03) | RT-G05 создаёт **catalog layer**, через который operator **выбирает** case — **не** заменяя per-project depth |

Registry implementation — **implementation-plane responsibility** для portfolio catalog serialization standard **поверх** RT-G04 substrate — **без** переопределения Registry Charter doctrine.

### Нормативная формулировка роли (planning)

**RT-G05 Registry Implementation** — архитектурная **роль authorized physical binding** Registry doctrine (catalog membership, discoverability, distinction summaries, Manifest pointer per entry) для Factory portfolio scope, **вне** Engine documentation boundary (ES-03, EO-05), **на** RT-G04 Persistence Substrate, **внутри** MVP capability floor (C4) и TOPOLOGY-B-v1 constraints.

RT-G05 **сам по себе не выбирает storage product** — он **определяет implementation responsibility** для registry catalog binding, которую **следующий** authorized track (implementation charter / standard) **может** материализовать без нарушения RA-*, RM-*, RD-*, RAP-*.

### Что RT-G05 implementation **не** решает

| Не решает | Владелец / gap |
|-----------|----------------|
| «Что такое Registry» doctrinally | [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) — **COMPLETE** |
| Где **физически** живут Factory records (locus, zone) | [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) — substrate, не serialization |
| Per-project entry anchor, minimum understanding | RT-G10 Manifest implementation |
| Eight visibility questions, operator read surface | RT-G12 Surface implementation |
| Live gate/handoff/state indexes, progression ledger | Engine Tracking + Playbook 04 writes on substrate |
| Movement execution, gate evaluation, automation | RT-G01, RT-G03, RT-G11 — **forbidden in MVP** |
| Registry enrollment ritual, RRDY attestation steps | Playbook 02 — **doctrine-complete** |
| Manifest enrollment, MRDY attestation | Playbook 01 — **предшествует** |
| Closure terminal metadata **as primary owner** | Playbook 05 + substrate P6; RT-G05 **may reflect** archived catalog status only |
| Site Type Registry, `site_type_code` **definitions** | Foundation T1 — RAP-11 |
| Queue rank, prioritization | RT-G06 — **FUTURE** |

**Planning boundary:** RT-G05 closes **portfolio catalog binding gap** — **не** Factory runtime, **не** persistence substrate charter, **не** per-project observability product, **не** catalog structure design.

---

## Foundation Dependencies

Registry Implementation Planning Charter **наследует** завершённый Engine v1, post-Engine charters, Operational Design, MVP Definition, RT-G04 charter, RT-G10 planning charter; **не изменяет** Foundation, Runtime, Engine Stages 1–6, Registry Charter, Manifest Charter, Playbooks 01–05.

### Tier 0 — Decision and review chain

| Document | RT-G05 planning использует |
|----------|---------------------------|
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C4 registry visibility; S3 success; dependency C2→C3→C4→C5 |
| [WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-PLANNING-REVIEW-v1.md) | RT-G05 impl scope; Playbook 02 binding; sequencing after RT-G10 |
| [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md) | P3 registry catalog carrier; REG-REL-01; substrate hosts, RT-G05 serializes |
| [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | REG-REL-01/02; manifest anchor dependency; ordering |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-01/02/03/06 |

### Tier 1 — Registry doctrine (authoritative — do not redesign)

| Document | Constraint on RT-G05 |
|----------|------------------------|
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | RRDY-*, RD-*, RA-*, RM-*, RE-*, RS-*, RAP-*, Scope Categories 1–7 — **sole source** of registry scope |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | MR-01, MR-02, RA-04 — registry **follows** manifest anchor |
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Identity shell; ES-03 — logical project vs registry entry |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-03 external registry; EO-05 one Engine per project |

### Tier 2 — Operational doctrine

| Document | RT-G05 planning использует |
|----------|---------------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; operator path Registry→Manifest→Tracking→Surface; Decision class **I** (catalog enrollment) |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — manifest-enrolled precondition for Playbook 02 |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — catalog-discoverable outcome; RRDY evaluation; physical file **not** blocking ritual |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — portfolio select; RE-01; Registry **not** Surface depth |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — catalog **does not** mutate Engine indexes |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — archived catalog category; withdrawal orthogonal to Factory-track closure |

### Tier 3 — Neighbor charters (relationship only)

| Charter | Document | RT-G05 boundary |
|---------|----------|-----------------|
| Manifest (RT-G10 planning) | [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | Stable manifest pointer — **hard dependency** |
| Tracking Surface (RT-G12 doctrine) | [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | RE-01, VP-05, RA-05 — Surface **per-project**; Registry **portfolio only** |

**Authority precedence:** Foundation Freeze + Engine Readiness Audit → Engine Stages 1–6 → Registry Charter (doctrine) → Manifest Charter (doctrine) → RT-G04 Substrate Charter → RT-G10 Manifest Implementation Planning Charter → **этот planning charter** для RT-G05 implementation responsibility → **будущий** RT-G05 implementation standard **не может** нарушить RA-*, RM-*, RD-*, RAP-*, OA-ACT-04, ES-03.

---

## Registry Implementation Responsibility

### Что RT-G05 **must provide** (capability-level)

Implementation responsibility derives **only** from Registry Charter scope categories and MVP C4 — **без** inventing new doctrine.

| # | Capability | Doctrine anchor | Planning obligation |
|---|------------|-----------------|---------------------|
| IR-01 | **Portfolio catalog physical binding** — Factory-scoped catalog listing on RT-G04 substrate | C4; S3; Playbook 02 | Operator can identify **enrolled Factory projects** in portfolio **without** workspace archaeology per case |
| IR-02 | **RRDY-* category binding** when MVP physically binds — all six readiness categories materializable from bound catalog record | RRDY-01…06; Registry §Registry-ready | Physical bind **implies** catalog integrity categories explicit — not empty placeholder listing |
| IR-03 | **Logical identity reference binding** (Category 2) | RRDY-01; RA-02, RA-03, ES-03 | Stable logical identity **indexed** — **distinct** from registry entry ID |
| IR-04 | **Manifest entry pointer binding** (Category 3) | RRDY-02; RM-01, RA-04 | Each discoverable entry **must** reference stable Manifest entry anchor |
| IR-05 | **Distinction summary binding** (Category 4) | RRDY-04; Scope Category 4 | Charter label, scope tier, endpoint **summary categories** — portfolio-safe only |
| IR-06 | **Discoverability status binding** (Category 6) | RRDY-05; RD-* | Registered / discoverable / withdrawn / archived — **catalog lifecycle**, not Runtime state |
| IR-07 | **Orientation snapshot category** (Category 5 — optional, non-authoritative) | RS-03; RA-05 | **May** surface portfolio glance — **must** reconcile with Engine or flag stale/invalid |
| IR-08 | **Enrollment precedence discipline** | Playbook 02; REG-REL-01; RD-02 | Doctrinal catalog-discoverable **precedes** physical bind; bind **follows** operator enrollment act |
| IR-09 | **Stability class honor** | RS-01, RS-02 | Stable catalog binding (identity ↔ entry) **must not** silently remap; evolving snapshot **must not** become tracking duplicate |
| IR-10 | **Anti-pattern guards carried forward** | RAP-01…RAP-18; RA-05 | Implementation planning **must** bound serialization to catalog/distinction/pointer — **reject** database, tracking SoT, manifest merge, auto-scan |
| IR-11 | **Optional bounded extension** (planning-bound only) | OQ-R06; Category 7 | **May** plan external workspace pointer **category** on catalog card — **refs only**; **must not** default to full external body index |

**Planning rule RI-01:** если отсутствие physical registry catalog binding **ломает** operator ability to satisfy Playbook 02 post-MVP success (S3), portfolio select before Playbook 03, или MVP mission C4 **without workspace archaeology** — obligation **входит** в RT-G05 responsibility scope.

### Что RT-G05 **must not provide** (remains outside)

| Outside RT-G05 | Actual owner |
|----------------|--------------|
| Persistence substrate locus, authorized zone, P1–P8 substrate classes **as substrate design** | RT-G04 charter + RT-G04 implementation track |
| Per-project manifest binding, MRDY-* | RT-G10 implementation |
| Eight Surface questions read binding, SRDY-* display | RT-G12 implementation |
| Engine instance indexes (state, gates, handoffs, artefacts) **as authoritative live index** | Tracking Model + Playbook 04 on substrate |
| Gate/handoff **criteria**, Runtime vocabulary | Runtime + Foundation |
| Registry enrollment workflow steps, RRDY attestation ritual | Playbook 02 |
| Manifest enrollment, MRDY attestation | Playbook 01 |
| Automated catalog creation on folder/git discovery | Forbidden — RD-04, RAP-10 |
| Site Type Registry operations, class-level matrices | Foundation T1 — RAP-11 |
| Queue position, priority rank | RT-G06 |
| Closure metadata **primary** persistence | Substrate P6; Playbook 05 |
| Layer artefact bodies, Legal Pack, handoff payloads | T1 Foundation / external |
| Catalog **structure** (central index vs distributed pointers layout) | RT-G05 **implementation** standard — **not** this planning charter |

**Planning rule RI-02:** RT-G05 defines **registry catalog serialization responsibility**, not **Factory Project existence** — logical Factory Project precedes catalog entry (RA-02, Playbook 01 recognition).

### Doctrine vs physical binding (planning distinction)

| Layer | Status | RT-G05 scope |
|-------|--------|--------------|
| **Doctrinal** catalog-discoverable | Playbook 02 outcome today — **COMPLETE** operatively | RT-G05 **does not replace** enrollment ritual |
| **Physical** registry catalog binding | MVP C4 — **NOT STARTED** | RT-G05 **must plan** bind rules linking enrolled state → persisted portfolio listing |
| **Registry-ready (RRDY-*)** | Evaluated at enrollment | RT-G05 bind **must reflect** categories already attested — not re-invent intake |
| **Discoverable ⊄ fully trackable** | Normal mid-chain | Early `NEW_PROJECT` may appear in catalog with empty gate indexes — valid per RD discoverable analog |

---

## Registry Readiness Binding

RRDY-* concepts govern **doctrinal catalog integrity**; RT-G05 planning determines **how readiness relates to implementation** — **without** defining formats, fields, or storage labels.

### RRDY → implementation planning mapping

| ID | Doctrinal criterion (Registry Charter) | RT-G05 planning binding rule |
|----|----------------------------------------|------------------------------|
| **RRDY-01** | Logical Factory Project identity explicit and Factory-scoped | Physical bind **must** carry stable logical identity reference — **not** conflated with registry entry ID |
| **RRDY-02** | Manifest entry anchor identified (manifest-ready) | Bind **must** include pointer to Manifest entry anchor — **hard** per RM-01 |
| **RRDY-03** | Registry entry distinct from logical identity understood | Bind **must** preserve **two-identifier** discipline — index slot ≠ identity shell |
| **RRDY-04** | Distinction summaries sufficient for portfolio | Bind **must** persist charter label, scope tier, endpoint **summary categories** — not full Manifest bodies |
| **RRDY-05** | Discoverability status category explicit | Bind **must** record catalog lifecycle category (discoverable / withdrawn / archived intent) |
| **RRDY-06** | Operator understands Registry ≠ Tracking ≠ Manifest | **Doctrinal** — not a serialized field; Playbook 02 attestation **precedes** bind; implementation **must not** create tracking/manifest-substitute on catalog card |

### Readiness relationships (unchanged by planning)

| Concept | Meaning for RT-G05 |
|---------|-------------------|
| **Registry-ready** | Threshold for Playbook 02 enrollment — **prerequisite** for physical bind, not replaced by it |
| **Registry-ready ⊄ gate-complete** | Mid-chain enrollment with open gates — **valid** catalog entry |
| **Registry-ready ⊄ fully trackable** | Early discoverable with empty indexes — **valid** |
| **Registry-ready ⊄ surface-ready** | Physical registry bind **does not** imply SRDY-* — Tracking indexes separate |
| **Physical bind ⊄ catalog-discoverable retroactively** | Enrollment decision **precedes** bind moment — timing **OPEN** for implementation charter (OQ-ME05 analog at registry plane) |
| **Manifest-ready ⊄ registry-ready** | Manifest-enrolled **required** before registry enrollment — RRDY-02 |

### Stability binding (Categories stable vs evolving)

| Stability class | Registry Charter | RT-G05 planning rule |
|-----------------|------------------|----------------------|
| **Expected stable** (identity ↔ entry binding, manifest pointer, charter label summary, scope tier, endpoint, enrollment declaration record) | RS-01; Stability §Expected stable | Physical bind **must** preserve amendment/reconciliation narrative — silent identity remap **forbidden** |
| **Expected evolving** (orientation snapshot, classification summary, discoverability status, track flags) | RS-02, RS-03 | Bind **may** surface evolving categories as **non-authoritative** summaries — **must not** freeze live gate index into catalog card (RA-05, RAP-06) |

### Principle RRB-01 — Readiness categories bind; readiness ritual does not move

Playbook 02 **owns** RRDY attestation. RT-G05 **owns** faithful physical representation of attested catalog categories — **not** re-evaluation gates, **not** automated RRDY pass.

### Principle RRB-02 — RRDY-02 is the registry hinge

Success criterion S3 («operator finds project in registry without opening each workspace») **maps directly** to persisted portfolio listing with Manifest pointer per entry. RT-G05 planning is **incomplete** if RRDY-02 / RM-01 pointer binding obligation is ambiguous.

---

## RT-G04 Relationship

RT-G04 **enables** RT-G05; RT-G05 **consumes** RT-G04; Registry Charter **neither is nor owns** storage (RAP-01).

### Consumption model (planning)

```text
  RT-G04 SUBSTRATE                    RT-G05 REGISTRY IMPLEMENTATION
  (persistence locus)                 (serialization responsibility)
         │                                      │
         │  provides portfolio catalog carrier  │  defines WHAT catalog categories bind
         │  (P3, authorized zone DF-03)         │  defines bind rules vs Playbook 02
         │                                      │
         └──────────── hosts ──────────────────▶ registry catalog binding (P3)
```

| RT-G04 provides | RT-G05 consumes (planning) |
|-----------------|----------------------------|
| Portfolio catalog physical carrier class (P3) | Catalog binding **placement** on substrate — **not** layout design here |
| Per-project manifest anchor on substrate (P2) | Registry entry **links to** manifest binding — **not** replaces it |
| Distinction summaries at catalog level only (P3, RA-05) | Persist summary categories — **not** tracking depth |
| Discoverability status categories (P3, RRDY-05) | Catalog lifecycle persistence |
| Logical identity ≠ registry entry ID discipline (ES-03) | Substrate **must allow** both identifiers without conflation |
| Human-only write path (PS-03) | Catalog bind writes **distinct** from Playbook 04 index writes — enrollment/bind acts **operator-controlled** |

### RT-G04 obligations RT-G05 depends on

| Substrate obligation | RT-G05 dependency |
|----------------------|-------------------|
| P3 — Registry catalog carrier | **Hard** — RT-G05 cannot exist without substrate locus for portfolio listing |
| REG-REL-01 — Registry implementation **must not** precede stable manifest anchor on shared substrate | Manifest bind (RT-G10) **before or with** registry catalog bind per entry |
| P2 — Manifest binding carrier | **Hard** — each catalog entry needs resolvable Manifest pointer target |
| Separation from live gate index (RA-05) | RT-G05 **must not** plan catalog-as-second-tracking-store |

### RT-G04 forbidden overlap (RT-G05 must respect)

| Forbidden | Reason |
|-----------|--------|
| RT-G05 defining substrate zone structure | RT-G04 charter — DF-03 only |
| RT-G05 owning P4–P6 (indexes, declarations, closure) **as registry scope** | Tracking/Playbook 04/05 territory |
| Catalog bind auto-mutating Engine indexes | OA-ACT-04, SC-03 |
| RT-G05 choosing persistence product or database | RAP-01; RT-G04 + topology DF-02 |

### Open catalog topology (bounded for implementation charter)

| ID | Question | RT-G05 planning disposition |
|----|----------|----------------------------|
| **OQ-R01** | Central registry artefact vs distributed pointers + aggregator | **OPEN** — resolved in RT-G05 **implementation** standard, not here |

**Principle G04-REL-01:** RT-G04 answers **where** Factory records live; RT-G05 answers **what registry catalog binding means** on that locus — **orthogonal** planning planes.

**Principle G04-REL-02:** RT-G05 **must not** precede RT-G10 manifest anchor availability on substrate for each catalog entry (inherited REG-REL-01 from RT-G04).

---

## RT-G10 Relationship

Manifest implementation **precedes** Registry catalog binding per entry; RT-G10 **enables** stable Manifest pointer; RT-G05 **must never duplicate** Manifest depth.

### What Registry depends on from Manifest implementation

| Registry need | Doctrine anchor | RT-G05 planning obligation |
|---------------|-----------------|----------------------------|
| Stable **pointer to Manifest entry** per catalog slot | RM-01, RA-04, RAP-16 | Physical manifest anchor **discoverable** and **stable** — registry bind **references only** |
| Logical Factory Project identity on manifest bind | ES-03, RA-02 | Catalog entry **references** same logical identity — **not** redefines |
| Manifest enrollment **precedes** catalog enrollment | Playbook 01→02, RD-02, RET-03 | RT-G05 bind **must not** exist for case **without** manifest-enrolled + RT-G10 anchor path |
| Distinction summaries — **not** manifest bodies | RM-02, RA-05 | RT-G05 **echoes summary categories** — **must not** copy Categories 1–8 as authoritative catalog content |

### What Registry must never duplicate from Manifest

| Manifest scope | RT-G05 exclusion |
|----------------|----------------|
| Minimum understanding categories in operational depth | Registry index card = **summary** only (Scope Category 4) |
| Authoritative reference topology map (Category 7 full) | Registry **points to** manifest entry — RE-01 path |
| Entry anchor doctrine definition | Manifest Charter — RT-G05 **consumes** anchor, **does not** redefine MRDY-06 |
| Per-project «start here» minimum understanding contract | Registry answers «which projects» — RE-01 |

### What Registry provides that Manifest does not

| Registry bind scope | Manifest exclusion |
|---------------------|-------------------|
| Coexistence of **multiple** Factory Projects in one portfolio view | Manifest is **per-project** only (MR-02) |
| Catalog membership and discoverability lifecycle | Manifest has no «list all projects» role |
| Cross-project distinction in one listing | Manifest does not compare cases |
| Withdrawn / archived **catalog visibility** categories | Manifest enrollment **never revoked** (Playbook 05) — catalog visibility **may** change |

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

**Principle M10-REL-01:** RT-G05 planning **must not** absorb manifest enrollment workflow (Playbook 01) or MRDY-* evaluation — **pointer consumption only**.

**Principle M10-REL-02 (inherited MR-01):** Registry follows Manifest, not vice versa — RT-G05 **must not** require registry entry for manifest bind; single-project Factory path **without** catalog remains **valid**.

**Principle M10-REL-03:** RT-G05 implementation planning **must not** precede RT-G10 Manifest Implementation Planning Charter completion — **satisfied** by upstream COMPLETE status; implementation **track** must respect RT-G10 anchor before registry bind per project.

---

## Tracking Relationship

Tracking composition **owns** per-project instance indexes; Registry **never** substitutes Tracking at portfolio scale (RA-05, RE-01).

### What Tracking / Surface may assume from Registry implementation

| Assumption | Consumer | Planning basis |
|------------|----------|----------------|
| Portfolio listing of **catalog-discoverable** Factory Projects exists | Playbook 03 ST-03; operator path OR-04 | RT-G05 **must** make portfolio **operator-locatable** without repo-wide search per case (S3) |
| Each listed entry **points to** Manifest entry anchor | Playbook 03 input chain Registry→Manifest→Tracking | RM-01 via catalog pointer |
| Registry card **does not** answer seven/eight tracking questions | RE-01; Surface charter | Portfolio select only — depth in Manifest→Tracking→Surface |
| Orientation snapshot on card, if present, is **non-authoritative** | RS-03; Playbook 02 | Derived from Tracking read or operator summary — reconcilable |
| Catalog membership **≠** gate-complete or surface-ready | Registry-ready ⊄ fully trackable | Playbook 03 may open on early `NEW_PROJECT` discoverable entry |

### What Tracking knows that Registry implementation must exclude

| Tracking knowledge | Why excluded from registry bind |
|--------------------|--------------------------------|
| Full gate outcome index with STALE/INVALID | Gate Composition + Tracking — RAP-06, RAP-13 |
| Complete handoff event sequence | Handoff Binding + Tracking |
| Artefact ref index exhaustiveness | AV-* — Surface Tier S-B |
| Eligibility snapshot, open gate set as catalog SoT | Derived — DR-01; RA-05 |
| Append-only audit trail detail | AT-* — Playbook 04 |
| Eight Surface question **answers** | SRDY-* — RT-G12 read binding |
| State history, progression ledger | State Model / Tracking — Scope Categories excluded |

### Registry orientation snapshot (planning-bound)

Registry Charter Category 5 (orientation snapshot) and RT-G04 derived reality class «registry orientation summary»:

- RT-G05 implementation **may** plan **optional** non-authoritative portfolio glance category
- **Defaults** to **minimum** distinction summaries — **exclude** live gate/handoff index unless explicitly authorized later (forbidden per RA-05)
- **Requires** RS-03 reconciliation discipline if surfaced

**Principle TRK-REL-01:** Operator answering seven/eight Tracking questions **never** uses Registry as primary surface — only Manifest → Tracking → Surface path (RE-01).

**Principle TRK-REL-02:** Registry implementation **must not** absorb Playbook 03 session workflow or Playbook 04 declaration writes — catalog plane **read-oriented** for tracking truth except enrollment/withdrawal/amendment acts on catalog itself.

### Playbook consumption

| Playbook | Registry implementation touchpoint |
|----------|-----------------------------------|
| **01** | Manifest-enrolled — **precondition** for catalog bind; RT-G05 **does not** participate |
| **02** | Enrolled → triggers physical catalog bind obligation (MVP C4) |
| **03** | Portfolio select from bound catalog → Manifest → Tracking depth |
| **04** | Updates indexes on substrate — **separate write plane**; catalog **does not** receive gate outcomes |
| **05** | Archived / withdrawn catalog categories — **may** update discoverability; **orthogonal** to Factory-track closure (CA-05) |

---

## Authority Model

Authority principles derive **only** from accepted Registry Charter, Operational Model, and Playbooks — **no new authority classes**.

### Who owns Registry truth

| Truth class | Owner | RT-G05 planning implication |
|-------------|-------|----------------------------|
| **Catalog doctrine** (what Registry **is**) | Registry Charter — **COMPLETE** | RT-G05 **implements binding**, not role redefinition |
| **Catalog membership / discoverability categories** (RRDY-*, RD-*) | Registry Charter | Serialization **maps to** categories — **cannot add** portfolio authority beyond charter |
| **Catalog-discoverable outcome** | Operator via Playbook 02 | Bind **follows** enrollment declaration — not discovery |
| **Logical Factory Project identity** | Engine Object Model — identity shell | Registry **indexes reference** — RA-02 |
| **Manifest entry anchor** | Manifest Charter + RT-G10 bind | Registry **points** — RA-04 |
| **Distinction summary content** (charter label, scope tier, endpoint) | Operator-authored charter / Manifest categories | Registry bind **echoes summaries** — follows amendments |
| **Last declared state/gate/handoff truth** | Engine tracking planes | Orientation snapshot **non-authoritative** — RS-03 |
| **Catalog enrollment / withdrawal history** | Operator declaration (append-only analog AT-01) | Bind **must** preserve enrollment narrative — RAP-17 |

### Who may modify Registry reality

| Actor | Permitted (v1) | Forbidden |
|-------|----------------|-----------|
| **Factory operator** | Playbook 02 enrollment; catalog withdrawal/re-enrollment; distinction summary updates following charter amendments; registry bind/update acts | Automated catalog enrollment without attestation |
| **Reviewer** | Audit RRDY checklist / portfolio integrity — **not** replace enrollment attestation | Declare catalog-discoverable |
| **External systems** (CI, agents, git hooks) | **None** for catalog bind authority | Auto-create/update catalog on scan (RAP-10, RD-04) |
| **Manifest workflow** | **None** for catalog content | Manifest side-effect creating registry entry |
| **Tracking/Surface impl** | **Read** catalog for portfolio drill-down | Write Engine indexes via registry channel |

### Inherited principles (non-negotiable in planning)

| ID | Principle | RT-G05 guard |
|----|-----------|--------------|
| **RA-02** | Logical project precedes registry entry | Bind **does not create** Factory Project |
| **RA-03** | Registry entry ID ≠ logical identity | **Forbidden** conflation in physical bind |
| **RA-04** | Registry follows Manifest | No registry-only project (RD-02) |
| **RA-05** | Registry ≠ Tracking at scale | No gate/handoff catalog |
| **OA-ACT-04** | External systems never mutate without operator act | No auto-enrollment |
| **RD-04** | No discovery by filesystem inference alone | Human-operated enrollment only |

**Principle AUTH-01:** Physical registry catalog binding **extends operability** of portfolio doctrine — **does not transfer** Engine declaration authority to catalog storage.

**Principle AUTH-02:** Catalog bind writes and Playbook 04 index writes are **separate authority planes** — registry enrollment **does not** imply gate PASS or state transition.

---

## Boundary Protection

RT-G05 Registry Implementation **must never become** следующие системы — по Registry Charter anti-patterns, MVP exclusions, Engine boundary, RT-G04/RT-G10 separation.

### Core forbidden roles

| Forbidden system | Why | Guard anchor |
|------------------|-----|--------------|
| **Manifest / per-project minimum understanding store** | RAP-07, MR-02; RT-G10 separate | Manifest bodies, MRDY-* depth — **out of scope** |
| **Tracking composition / live observability index** | RAP-06, RA-05 | Gate/handoff/history catalog — **Tracking only** |
| **Tracking Surface / operator dashboard** | RAP-05; RT-G12 separate | Eight questions display — **read consumer** |
| **Persistence substrate product** | RAP-01; RT-G04 owns locus | Substrate design, zone layout — **not RT-G05** |
| **Database / query engine / multi-tenant store** | RAP-01; MVP file-backed sufficient | DB-as-registry — **rejected** |
| **Workflow engine / state machine executor** | RAP-03; RT-G01 | Catalog-driven transitions — **forbidden** |
| **Factory runtime product** | SC-01; RT-G09 | «Registry drives execution» — **rejected** |
| **Queue / scheduler / prioritization** | RAP-04; RT-G06 | Queue rank on card — **forbidden** |
| **Project management system** | Scope creep | Tasks, sprints, assignments beyond distinction summary — **out of scope** |
| **Portfolio analytics platform** | RA-05 extension | Cross-project gate rollups, KPI dashboards — **forbidden** |
| **Passport / unified project mega-document** | RAP-08, BV-15 | Second SoT — **explicitly rejected** |
| **Site Type Registry** | RAP-11 | Foundation T1 class-level registry — **distinct system** |
| **Discovery crawler / git folder scanner** | RAP-10, RD-04 | Auto-enrollment — **forbidden** |
| **Agent registry / MCP tool catalog** | RAP-18 | External systems — **not** Factory Project catalog |
| **Automation / agent enrollment** | Playbook 02 forbidden automation | CI catalog sync — **forbidden** |
| **Closure registry / terminal workflow engine** | Playbook 05 scope | Closure metadata primary — **substrate P6**; catalog **archived category only** |
| **Foundation authority merge** | RAP-12 | Embedding Legal Pack, matrices — **forbidden** |
| **Implementation spec documents** (FACTORY-PROJECT-INDEX, DISCOVERY, PASSPORT) | RAP-14 | Forbidden sibling docs without authorization |

### Architectural anti-patterns RT-G05 planning must resist

| Anti-pattern | Guard |
|--------------|-------|
| Registry impl conflated with «shipped Factory runtime» | MVP explicit non-claims; C4 ≠ RT-G09 |
| Serialization / catalog structure design smuggled into **this** planning charter | Task charter forbidden list |
| Registry card duplicates live Tracking gate index | RA-05, RAP-06, SC-05 |
| Physical bind **before** doctrinal catalog enrollment | Playbook 02 ordering |
| Registry impl **precedes** manifest anchor per project | REG-REL-01, M10-REL-03 |
| Registry bind replaces Playbook 04 declaration path | DA-01, C6 |
| Deploy / go-live conflated with catalog «completion» | RAP-15 |
| Conflating Site Type Registry with Factory Project Registry | RAP-11 |
| Silent deletion of enrollment history | RAP-17 |
| Registry as **central** Engine for all projects | RE-02 — no «Stage 7» |

### Additional justified non-responsibilities

| Role | Rationale |
|------|-----------|
| Validator / gate authority engine | RT-G11 — post-MVP |
| MIG / external pipeline SoT | RT-G08 |
| Notification / webhook hub | RT-G13 |
| Rollback automation executor | RT-G15 |
| Layer generation / frontend build | GG-* — external product plane |
| Multi-operator RBAC | Operational Model — out of Charter 01 |
| Git policy / backup product | May inherit discipline — not Factory subsystem charter |

**Principle BP-01:** RT-G05 is **portfolio catalog serialization responsibility** — **many projects listed**, **one Engine depth per project** — not a platform.

**Principle BP-02:** RT-G05 planning **must remain** catalog-structure-agnostic — central index vs distributed pointers is **implementation standard** territory (OQ-R01), not planning charter resolution.

---

## Readiness Model

### When RT-G05 **planning charter** is complete

RT-G05 Registry Implementation Planning Charter v1 считается **planning-complete** когда:

| Criterion | Status in this deliverable |
|-----------|---------------------------|
| Purpose defined — C4 gap, portfolio listing, vs doctrine-only baseline | **Yes** |
| Implementation responsibility — must provide / must not provide | **Yes** — IR-*, RI-* |
| RRDY-* binding rules without format or catalog structure design | **Yes** — RRB-* |
| RT-G04 consumption model — hosts vs serializes | **Yes** — G04-REL-* |
| RT-G10 dependency — pointer stability, ordering, non-duplication | **Yes** — M10-REL-* |
| Tracking assumptions — RE-01, RA-05, no duplication | **Yes** — TRK-REL-* |
| Authority model — operator, Playbook 02, RA-* | **Yes** — AUTH-* |
| Boundary protection — forbidden roles explicit | **Yes** — BP-* |
| Future implementation implications identified | **Yes** — see below |
| Explicit non-claims — no schemas, files, catalog layout | **Yes** |

### What planning-complete **does not** mean

| Not implied | Reason |
|-------------|--------|
| RT-G05 **implementation** started or complete | Separate authorized track |
| Physical registry artefacts **created** | Forbidden in planning scope |
| Serialization format or catalog topology **selected** | RT-G05 implementation standard |
| OQ-R01, OQ-R02, OQ-R05 **resolved** | Bounded OPEN for implementation charter |
| MVP **demonstrated** | S1–S9 post-implementation |
| RT-G12 planning **complete** | Separate charter |

### Planning-complete vs implementation-ready

```text
  Registry Charter v1 (doctrine) ── COMPLETE
           │
           ▼
  RT-G04 Persistence Substrate Charter v1 ── COMPLETE
           │
           ▼
  RT-G10 Manifest Implementation Planning Charter v1 ── COMPLETE
           │
           ▼
  RT-G05 Registry Implementation Planning Charter v1 ── THIS (planning-complete)
           │
           ▼
  RT-G05 Registry Implementation Standard (implementation charter) ── NEXT authorized track
           │
           └──▶ RT-G12 Surface Read Binding Implementation Planning Charter (may parallel after RT-G10)
```

**Principle RDY-01:** Loss of RT-G05 planning clarity **must not** block Registry doctrine or Playbook 02 — doctrine **already operable** without physical bind.

**Principle RDY-02:** MVP S3 success **requires** RT-G05 implementation **after** this planning charter and stable RT-G10 manifest anchor — not planning alone.

**Principle RDY-03:** RT-G05 planning-complete **does not** authorize physical MVP artefact creation — operator implementation charter required per RUNTIME-GAPS governance rule.

---

## Future Implementation Implications

Без implementation design — **logical successors and dependency edges only**.

### Immediate successor (Tier 1)

| Next charter | Role | Depends on | Must carry forward |
|--------------|------|------------|-------------------|
| **RT-G05 Registry Implementation Standard** (implementation charter — **not this doc**) | Catalog serialization scope, OQ-R01 topology decision, card template (OQ-R02), bind moment rules, operator write path for enrollment/withdrawal/amendment | This planning charter + RT-G04 substrate impl + RT-G10 manifest anchor per project + Registry Charter | RA-*, RM-*, RD-*, RAP-*, RRDY-*, Playbook 02, OA-ACT-04 |

**Success signal (from Implementation Planning Review):** Operator finds enrolled Factory Project in **portfolio catalog** with distinction summary and Manifest pointer **without** opening each workspace (S3, C4).

### Parallel / sequential successors (MVP sequence)

| Charter | Relationship to RT-G05 | Sequencing rule |
|---------|------------------------|-----------------|
| **RT-G12 Surface Read Binding Implementation Planning Charter** | May consume registry for portfolio drill-down; **must not** use registry as Surface depth | After RT-G10; may parallel RT-G05 **planning**; impl reads catalog optionally |
| **RT-G10 Manifest Implementation Standard** | **Precedes** RT-G05 impl per entry — manifest anchor **hard** | Before or concurrent with RT-G05 impl bind per project |
| **RT-G04 Implementation** (physical substrate artefacts) | **Enables** catalog carrier P3 | Substrate **before or with** RT-G05 impl — C2→C4 |

### Post-MVP (not blocked by RT-G05 planning)

| Item | Notes |
|------|-------|
| RT-G06 Queue | May reference catalog entries — separate charter |
| RT-G08 MIG correlation | OQ-R09 — catalog category for incoming refs |
| OQ-R05 PHASE_SLICE catalog entry policy | Engine v2 or implementation standard |
| OQ-R03 extended view for archived/withdrawn | RT-G12 display policy |
| Auto-sync orientation snapshot from Tracking | **Forbidden** as authoritative (OQ-R08); display-only **implementation** question |

### MVP operator path after RT-G05 impl (planning reference)

```text
  Playbook 01 ──▶ manifest-enrolled
         │
         ▼
  RT-G10 impl ──▶ physical manifest anchor persisted (C3, S2)
         │
         ▼
  Playbook 02 ──▶ catalog-discoverable
         │
         ▼
  RT-G05 impl ──▶ physical portfolio catalog persisted (C4, S3)
         │
         ├──▶ Playbook 03 / RT-G12 ──▶ select project → Surface reads bound data
         │
         └──▶ (portfolio glance only — not tracking depth)
                    │
                    ▼
              Playbook 04 ──▶ index writes on substrate (separate plane)
                    │
                    ▼
              Playbook 05 ──▶ closure metadata + catalog archived category
```

**Principle FUT-01:** RT-G05 implementation standard **must not** authorize automated index mutation, workflow engine hooks, or manifest auto-enrollment as side effects of catalog bind.

**Principle FUT-02:** RT-G05 implementation standard **must not** define FACTORY-PROJECT-INDEX-v1, FACTORY-PROJECT-DISCOVERY-v1, FACTORY-REGISTRY-STORAGE-v1, or unified YAML catalog schema **without** explicit operator authorization beyond planning charter.

---

## Explicit Non-Claims

This document and the RT-G05 Registry Implementation **planning** role it defines:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** **storage design**, **database design**, **file format**, **JSON/YAML schema**, **folder structure**, **catalog structure**, or **physical MVP artefacts**;
- **are not** **implementation spec**, **serialization standard**, or **code**;
- **are not** **operator UI**, **dashboard**, **portfolio analytics platform**, or **CLI** (RT-G12);
- **are not** **Manifest** (RT-G10) or **Tracking Surface** (RT-G12 doctrine) redesign;
- **are not** **Persistence Substrate** (RT-G04) redesign — only **consumption** relationship;
- **are not** **Registry Charter** rewrite — doctrine taken as authoritative input;
- **are not** Playbooks 01–05 rewrite;
- **do not** define registry file paths, catalog index topology, field lists, database tables, or card templates;
- **do not** modify Factory Engine Architecture v1 Stages 1–6 semantics;
- **do not** claim physical registry records **exist** in-repo — **planning charter only**;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound registry catalog;
- **do not** claim RT-G05 **implementation** is authorized beyond **planning** by existence of this document alone.

Human-operated catalog enrollment path remains the v1 model per Operational Model OA-ACT-04 and Playbook 02.

---

## Open Questions

Charter **bounds** questions for **future RT-G05 implementation standard** — **does not answer** serialization or catalog topology choices.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-R01** | Physical registry artefact vs distributed pointers + aggregator | **OPEN** — RT-G05 implementation standard |
| **OQ-R02** | Registry index card field template derived from Manifest categories | **OPEN** — near-MVP; reduces ambiguity; not doctrine blocker |
| **OQ-R03** | Default vs extended portfolio view for archived/withdrawn | **OPEN** — RT-G12 display; RD-03 |
| **OQ-R04** | Duplicate detection across logical identities | **OPEN** — operational playbook + implementation standard |
| **OQ-R05** | PHASE_SLICE — one catalog entry per shell vs per slice | **OPEN** — Engine v2 or implementation standard |
| **OQ-R06** | External workspace pointer in catalog card | **OPEN** — operational + implementation |
| **OQ-R07** | Relationship RT-G06 queue to catalog entry | **OPEN** — queue charter |
| **OQ-R08** | Auto-sync catalog snapshot from Tracking — allowed or forbidden | **BOUNDED** — forbidden as authoritative (RAP-06, OQ-R08); display sync **implementation** only |
| **OQ-R09** | MIG / incoming request correlation as catalog category | **OPEN** — RT-G08 integration charter |
| **OQ-RE05** | Physical catalog bind moment vs doctrinal catalog-discoverable timing | **OPEN** — RT-G05 implementation standard (OQ-ME05 analog) |
| **DF-04…DF-10** | Substrate workshop inputs affecting registry bind co-location with manifest | **OPEN** — cross-charter implementation planning |

**Resolved by upstream (not open in this planning scope):** Registry doctrine (RRDY-*, Scope Categories 1–7); Playbook 02 enrollment without file blocking; RT-G04 authorized zone DF-03; MVP includes C4 registry visibility; Manifest anchor precedes registry (MR-01, RA-04, REG-REL-01); Registry ≠ Tracking (RA-05); Registry ≠ Site Type Registry (RAP-11).

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G05 Registry Implementation Planning Charter v1** as **RT-G05 planning role complete** — gap RT-G05 in RUNTIME-GAPS remains **NOT STARTED** for **implementation**, not for planning.
2. **Authorize next track:** **RT-G05 Registry Implementation Standard** (implementation charter) — catalog serialization scope, OQ-R01 topology, card template (OQ-R02), bind rules — **still requires** separate authorization; **must** carry RA-*, RM-*, RD-*, RAP-*, RRDY-*, Playbook 02 forward.
3. **Preserve sequencing:** RT-G10 manifest implementation standard **before or with** RT-G05 registry implementation per project; RT-G04 substrate artefacts **available** for catalog carrier P3; RT-G12 Surface planning **may** proceed in parallel **after** RT-G10 planning — registry portfolio drill-down **optional** consumer.
4. **Do not create yet:** registry yaml/json samples, FACTORY-PROJECT-INDEX-v1.md, FACTORY-PROJECT-DISCOVERY-v1.md, FACTORY-REGISTRY-STORAGE-v1.md, catalog folder trees under `workspaces/website-factory-operations/`, database designs, tracking-in-registry prototypes, passport documents.
5. **Optional P3:** Update RUNTIME-GAPS RT-G05 line to «PLANNING CHARTERED» — **operator action**, outside this deliverable.

**Engine Architecture v1 requires no further architecture stages.** RT-G05 planning charter is **post-RT-G04, post-RT-G10-planning, post-MVP-definition** documentation.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` path **exists** on disk today | **UNKNOWN** — RT-G04 charter records zone; physical creation not part of this deliverable |
| Calendar for RT-G05 implementation standard authorization | **not scheduled** |
| De-facto ad-hoc portfolio listing discipline already used by operators | **UNKNOWN** — no canonical catalog chartered |
| Triumph / pilot workspaces in catalog vs external-only refs | **UNKNOWN** — per case (DF-08, OQ-R06) |
| Operators updated NEXT-PRIORITIES to RT-G05 planning-complete era | **UNKNOWN** |

---

*RT-G05 Registry Implementation Planning Charter v1 — RT-G05 planning complete. Planning charter only. Canonical location: `workspaces/website-factory-reference-v1/RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G05 Registry Implementation Planning Charter v1

**Stage:** Implementation Planning — RT-G05 Registry Implementation Planning Charter  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md` (created)  
**Summary:** Определена planning-ответственность RT-G05 Registry Implementation: физическая привязка Registry doctrine (portfolio catalog, RRDY-*, Manifest pointer, distinction summaries) на RT-G04 substrate для MVP C4/S3; границы must/must-not vs RT-G10 Manifest, Tracking, Playbooks; RRDY binding без форматов; authority model (operator, Playbook 02, RA-*); boundary protection от manifest/tracking/runtime/database/PM/analytics; readiness planning-complete vs implementation successor RT-G05 Registry Implementation Standard; без storage, schemas, catalog structure, files, implementation design.  
**Git:** no commit, no push (per task charter).
