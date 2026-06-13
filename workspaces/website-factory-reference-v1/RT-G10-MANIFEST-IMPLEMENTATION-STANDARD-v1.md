# REPORT — RT-G10 Manifest Implementation Standard v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Implementation Standards — **RT-G10 implementation standard only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; Topology Decision **COMPLETE** (TOPOLOGY-B-v1); RT-G04 Persistence Substrate Implementation Standard **COMPLETE**; RT-G10 Manifest Implementation Planning Charter **COMPLETE**  
**Тип:** implementation standard only — **без** runtime, database, automation, queue, workflow engine, UI, application, schemas, folder layout, physical artefact creation, code  
**Upstream:** [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md), [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md), Operational Playbooks 01–05  
**Связь:** [RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-PLANNING-CHARTER-v1.md), [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md) RT-G10

**Owner decisions (fixed — inherited):**

| ID | Decision |
|----|----------|
| **DF-01** | MARS monorepo (`C:\AI MARS`) |
| **DF-02** | Filesystem + structured artifacts (TOPOLOGY-B-v1) |
| **DF-03** | Factory Records Zone = `workspaces/website-factory-operations/` |
| **DF-06** | No HomeGateway dependency |

---

## Purpose

### Зачем существует RT-G10 Implementation Standard

**RT-G10 Manifest Implementation Standard v1** переводит [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) и [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md) из **роли entry anchor** (doctrine + planning) в **конкретную MVP-модель физического существования** Manifest binding — оставаясь **filesystem-backed**, **documentation-first** и **human-operated**, без runtime-концепций.

| Charter / Planning отвечает | Implementation Standard отвечает |
|-----------------------------|----------------------------------|
| Какова **роль** Manifest (entry anchor, minimum understanding) | Как Manifest binding **существует физически** в MVP |
| Какие **категории** Manifest владеет doctrinally (Categories 1–8) | Какие **implementation object classes** должны быть сериализованы |
| MRDY-* как orientability threshold | MRDY-* как **implementation expectations** при physical bind |
| MAP-*, MT-*, MA-* anti-patterns | Что Manifest implementation **must never become** on disk |
| IM-* planning obligations | IM-* как **implementation obligations** для POC-02 manifest facet |

### Нормативная формулировка implementation responsibility

**RT-G10 Manifest Implementation (MVP implementation)** — **авторизованная per-project physical binding** Manifest doctrine в POC-02 manifest facet внутри per-project record home на RT-G04 substrate, которую operator **читает и вручную создаёт/обновляет** после Playbook 01 enrollment — **без** shipped runtime, **без** automated bind on discovery и **без** выбора serialization format в этом standard (implementation classes only).

Manifest implementation **материализует entry anchor (MRDY-06)** и **minimum understanding categories (MRDY-01…05)** — **не** Passport, **не** Tracking composition, **не** Registry catalog.

### Implementation purpose statement

Manifest implementation **материализует** для одного Factory Project:

1. **One canonical persisted entry anchor** (S2, C3) — operator «начинает здесь» без workspace archaeology.
2. **Faithful physical representation** of MRDY-* categories attested at Playbook 01 — **not** re-evaluation ritual.
3. **Reference topology pointers** (Category 7) — where state, gate, handoff, artefact truths live on substrate or externally.
4. **Stable separation** from POC-03…POC-07 tracking indexes — manifest binding **orients**, tracking **observes**.

Manifest implementation **не сериализует** Registry catalog, Surface display, gate criteria, layer bodies, or declaration authority — it **populates POC-02 manifest facet** within substrate homes RT-G04 already defined.

---

## Foundation Dependencies

Implementation Standard **наследует** Manifest Charter, RT-G10 planning charter, RT-G04 standard и operational doctrine **без их переопределения**.

### Tier 0 — Charter, standard, and decision chain

| Document | Standard использует |
|----------|---------------------|
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | Categories 1–8, MRDY-*, MA-*, MT-*, MR-*, ST-*, MAP-* — **sole doctrine source** |
| [RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-PLANNING-CHARTER-v1.md) | IM-*, MRB-*, G04-REL-*, REG-REL-*, TRK-REL-*, AUTH-*, BP-* |
| [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md) | POC-01, POC-02 (manifest facet), POC-09, H-01…H-10, P1/P2, POC-RULE-02 |
| [WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md](WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md) | TOPOLOGY-B-v1; DF-01/02/03/06 |
| [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) | C3 manifest persistence; S2 success; C2→C3→C4 dependency |

### Tier 1 — Operational doctrine

| Document | Standard использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | OA-ACT-01/04; operator path Registry→Manifest→Tracking→Surface; OR-03 manifest-ready ⊄ file |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Playbook 01 — doctrinal manifest-enrolled precedes physical bind |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Playbook 02 — manifest anchor precondition |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Playbook 03 — E4 manifest entry anchor reachable |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Playbook 04 — separate write plane for POC-03…POC-07 |
| [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md) | Playbook 05 — manifest enrollment never revoked |

### Tier 2 — Engine and neighbor charters

| Document | Constraint on implementation |
|----------|------------------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Manifest serves Object — **no new mandatory components** |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Tracking owns instance indexes — MT-01 separation |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | ES-04 — persistence external to Engine docs |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | MR-01, RA-04 — registry follows manifest anchor |
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | TS-02 — Surface assumes manifest entry, does not redefine |

**Authority precedence:** Foundation Freeze + Engine → Manifest Charter (doctrine) → RT-G04 Standard → RT-G10 Planning Charter → **этот standard** → RT-G05/RT-G12 standards **не могут** нарушить MAP-01, MT-01, MA-01, MR-01, OA-ACT-04, ES-04, POC-RULE-02.

---

## Manifest Object Model

Implementation standard определяет **двенадцать implementation object classes** — нормативные категории structured content within POC-02 manifest facet and associated POC-01/POC-09 bindings, **не** schema labels, field names, or file names.

### Class taxonomy

| Class ID | Class name | Physical meaning | MVP disposition |
|----------|------------|------------------|-----------------|
| **MOC-01** | **Entry anchor** | Canonical per-project «start here» locus — materialization of MRDY-06 | **Must persist** on bind |
| **MOC-02** | **Identity** | Stable logical Factory Project identity reference (Category 1) | **Must persist** |
| **MOC-03** | **Scope** | Charter & scope tier categories (Category 2) — intent, exclusions, operator assignment | **Must persist** (minimal at intake allowed) |
| **MOC-04** | **Endpoint** | Declared lifecycle endpoint category (Category 3) | **Must persist** |
| **MOC-05** | **Applicability** | Scope applicability doctrine — full chain vs partial with exclusions (Category 4) | **Must persist** |
| **MOC-06** | **Classification anchors** | Lifecycle-dependent binding refs when applicable (Category 5) — `site_type_code`, blueprint, generation slice | **May persist** at bind; **must persist** when category mandatory per charter |
| **MOC-07** | **Position summary** | Non-authoritative «where now» orientation pointer (Category 6) | **May persist** as pointer only; **must not** duplicate live state ledger |
| **MOC-08** | **Topology** | Authoritative reference topology — map of maps (Category 7) | **Must persist** |
| **MOC-09** | **Foundation pins** | Logical dependency pins when explicitly declared (Category 8) | **May persist** |
| **MOC-10** | **Enrollment** | Physical bind metadata linking to Playbook 01 manifest-enrolled act | **Must persist** on bind |
| **MOC-11** | **Amendment** | Stable-category amendment narrative (ST-01) — append-oriented | **Must persist** when amendments occur |
| **MOC-12** | **External refs** | Topology target locators and optional workspace pointers (POC-09 discipline) | **Must persist** for Category 7 targets |

### Optional extension classes (bounded — default exclude)

| Class | Content | Notes |
|-------|---------|-------|
| **MOC-X1** | **Selected Tracking zone snapshot** | OQ-M01 — **only** if explicitly authorized; **must not** include live gate/handoff index (MT-01) |
| **MOC-O1** | **Pre-bind enrollment draft** | POC-O2 analog — supports OQ-ME05; **not authoritative** until bind act |

### Class composition model (implementation-level, not folder design)

```text
  per-project record home (RT-G04 P1)
  │
  ├── POC-01 identity shell ──────────────────── MOC-02
  │
  └── POC-02 manifest binding carrier
        ├── MOC-01 Entry anchor ◀── MVP hinge (MRDY-06, S2)
        ├── MOC-03 Scope
        ├── MOC-04 Endpoint
        ├── MOC-05 Applicability
        ├── MOC-06 Classification anchors (when applicable)
        ├── MOC-07 Position summary (pointer only)
        ├── MOC-08 Topology ──▶ MOC-12 external refs
        ├── MOC-09 Foundation pins (optional)
        ├── MOC-10 Enrollment bind metadata
        ├── MOC-11 Amendment narrative (when needed)
        └── MOC-X1 optional zone snapshot (default: absent)
```

**Principle MOC-RULE-01:** MOC-01 **must** be **one** canonical entry anchor per Factory Project identity — no competing manifest binding carriers.

**Principle MOC-RULE-02:** POC-02 manifest facet **must remain** a **distinct record class** from POC-03…POC-07 tracking indexes on substrate (POC-RULE-02, MT-01) — co-location within same per-project home **permitted**; **collapse into undifferentiated project mega-record forbidden**.

**Principle MOC-RULE-03:** MOC-08 topology **must** point to authoritative loci — typically POC-03 (state), POC-04 (gates), POC-05 (handoffs), POC-09 (artefacts) on same substrate, plus external layer/Runtime refs — **never** embed bodies.

### Mapping: Manifest Charter categories → implementation classes

| Charter category | Implementation classes |
|------------------|------------------------|
| Category 1 — Stable project identity | MOC-02 (+ POC-01 shell) |
| Category 2 — Charter & production intent | MOC-03 |
| Category 3 — Declared lifecycle endpoint | MOC-04 |
| Category 4 — Scope applicability doctrine | MOC-05 |
| Category 5 — Classification & binding anchors | MOC-06 |
| Category 6 — Current position summary | MOC-07 (pointer only) |
| Category 7 — Authoritative reference topology | MOC-08, MOC-12 |
| Category 8 — Foundation version pins | MOC-09 |
| MRDY-06 entry anchor | MOC-01 |
| Playbook 01 enrollment act | MOC-10 |
| ST-01 stable amendments | MOC-11 |

---

## Manifest Ownership

### What Manifest physically owns

Manifest binding **owns serialized representation** of minimum understanding categories within POC-02 manifest facet — **orientability content**, not observability depth.

| Owned content | Implementation class | Owner write path |
|---------------|---------------------|------------------|
| Entry anchor locus identity | MOC-01 | Operator manifest bind/amend act (post Playbook 01) |
| Stable identity reference binding | MOC-02, POC-01 facet | Operator bind act |
| Charter & scope tier categories | MOC-03 | Operator bind + explicit amendment (MOC-11) |
| Declared endpoint category | MOC-04 | Operator bind + charter amendment |
| Applicability doctrine | MOC-05 | Operator bind + scope amendment |
| Classification anchor refs when present | MOC-06 | Operator bind/update when lifecycle demands |
| Topology structure & role labels | MOC-08 | Operator bind; target list grows with refs |
| Foundation pin categories when declared | MOC-09 | Operator bind/amendment |
| Enrollment-to-bind linkage metadata | MOC-10 | Operator bind act |
| Stable category amendment narrative | MOC-11 | Operator explicit amendment — append-oriented |
| Topology pointer locators (not bodies) | MOC-12, POC-09 subset | Operator maintains refs |

### What Manifest physically references

Manifest binding **indexes and points** — **does not own** authoritative truth bodies or live indexes.

| Referenced content | Typical locus | Reference rule |
|--------------------|---------------|----------------|
| Active state instance | POC-03 on substrate | MOC-07 **pointer**; MS-02 reconciliation if surfaced |
| Gate outcome index | POC-04 on substrate | MOC-08 topology target only |
| Handoff event index | POC-05 on substrate | MOC-08 topology target only |
| Artefact ref index | POC-09 on substrate | MOC-08 / MOC-12 |
| Runtime vocabulary docs | `runtime-architecture/` canon | External ref — MA-01 |
| Foundation layer contracts | T1 docs, `registry/` Site Type Registry | External ref — MAP-08 |
| Client / layer workspaces | `workspaces/*`, Lane A `src/` | External ref only — RR-03 |
| Closure terminal metadata | POC-08 on substrate | **Reference category only** — primary owner Playbook 05 |
| Registry catalog entry | POC-02 registry facet (portfolio) | **Optional back-ref** — manifest **does not require** registry slot |

### What Manifest must never own

| Forbidden ownership | Actual owner | Guard |
|---------------------|--------------|-------|
| Live gate/handoff/state indexes | POC-03…POC-05; Playbook 04 | MT-01, MAP-05 |
| Declaration records & progression ledger | POC-06, POC-07; Playbook 04 | MA-02, DA-01 |
| Gate/handoff **criteria** | Runtime + Foundation | MAP-10 |
| Layer artefact **bodies** | T1 layers / external workspaces | MAP-11, RR-02 |
| Handoff package payloads | Generation Outputs | MAP-11 |
| Portfolio catalog membership | POC-02 registry facet; RT-G05 | MAP-07, MR-02 |
| Eight Surface question **answers** | RT-G12 read composition | MAP-09 |
| Closure outcome **primary** persistence | POC-08; Playbook 05 | Playbook 05 scope |
| Site Type Registry entries | Foundation `registry/` | RAP-11 |
| Automated transition / execution state | **Nobody in MVP** | MAP-12, SC-03 |

### Ownership principles

| ID | Principle |
|----|-----------|
| **MOWN-01** | RT-G10 **populates** POC-02 manifest facet; RT-G04 **hosts** physical home — **must not** create parallel manifest SoT outside authorized zone |
| **MOWN-02** | Only **Factory operator** **authoritatively creates/updates** manifest binding — enrollment attestation (Playbook 01) **precedes** bind; amendments follow ST-01 |
| **MOWN-03** | Playbook 04 **owns** POC-03…POC-07 mutations — manifest bind **does not grant** declaration write path |
| **MOWN-04** | RT-G12 Surface **reads** manifest binding — **never writes** MOC-* authoritative content |
| **MOWN-05** | Logical Factory Project **precedes** physical manifest; registry slot **follows** manifest anchor (MR-01, REG-REL-01) |
| **MOWN-06** | MOC-07 position summary **must not** become parallel active state ledger — **pointer or omitted**, not second SoT |

### Substrate vs manifest vs downstream ownership

| Layer | Owns | Does not own |
|-------|------|--------------|
| **RT-G04 substrate** | Physical homes; POC class taxonomy; zone discipline | Manifest category content; MRDY field binding |
| **RT-G10 manifest (this standard)** | MOC-* content within POC-02 manifest facet; entry anchor; topology pointers | Tracking indexes; registry catalog; Surface display |
| **RT-G05 registry** | POC-02 registry facet catalog content | Per-project manifest depth; tracking indexes |
| **Playbook 04 / Tracking** | POC-03…POC-07 authoritative indexes | Manifest minimum understanding categories |
| **RT-G12 Surface** | Read composition for eight questions | Any authoritative write |

---

## Manifest Readiness Model

MRDY-* governs **doctrinal orientability** at Playbook 01; RT-G10 standard defines **implementation expectations** when physical bind occurs — **without** schemas, field lists, or storage labels.

### MRDY → implementation standard mapping

| ID | Doctrinal criterion | Implementation expectation at physical bind |
|----|---------------------|---------------------------------------------|
| **MRDY-01** | Stable project identity category explicit | MOC-02 **must** carry stable logical identity reference — **distinct** from registry entry ID (ES-03, RA-03) |
| **MRDY-02** | Charter & scope tier explicit | MOC-03 **must** persist charter/scope **categories** — minimal intake **valid** |
| **MRDY-03** | Declared lifecycle endpoint explicit | MOC-04 **must** record endpoint category — full chain default **or** partial with acknowledged boundary |
| **MRDY-04** | Scope applicability doctrine explicit | MOC-05 **must** make full vs partial applicability **explicit** — aligns with scope mask category |
| **MRDY-05** | Reference topology declared | MOC-08 + MOC-12 **must** declare topology targets — operator knows where state/gate/artefact truths live **without repo search** |
| **MRDY-06** | Manifest entry anchor identified | MOC-01 **must** materialize** discoverable entry anchor on substrate — **core MVP obligation** (S2, C3) |
| **MRDY-07** | Operator understands Manifest ≠ Passport ≠ Registry | **Not serialized** — Playbook 01 attestation **precedes** bind; implementation **must not** create Passport or registry-substitute artefact |

### Readiness relationships (implementation terms)

| Concept | Implementation rule |
|---------|---------------------|
| **Manifest-ready** | Playbook 01 threshold — **prerequisite** for physical bind, **not replaced** by bind |
| **Physical bind complete** | MOC-01…MOC-05, MOC-08, MOC-10, MOC-12 **present**; MOC-06/07/09 per lifecycle |
| **Manifest-ready ⊄ fully trackable** | Valid bind at `NEW_PROJECT` with **empty** POC-04/POC-05 — MOC-08 still points to index loci |
| **Manifest-ready ⊄ surface-ready** | Physical bind **does not imply** SRDY-* — POC-03…POC-07 separate |
| **Physical bind ⊄ retroactive enrollment** | MOC-10 **must** reference prior Playbook 01 enrollment act — bind **follows** doctrinal enrolled (OQ-ME05: same session **permitted**, discovery bind **forbidden**) |

### Stability expectations at implementation layer

| Stability class | Charter | Implementation rule |
|-----------------|---------|---------------------|
| **Expected stable** (identity core, charter intent, scope tier, endpoint, pins) | ST-01 | MOC-02…MOC-05, MOC-09, MOC-11 — amendment **via** MOC-11 narrative; silent overwrite **forbidden** |
| **Expected evolving** (position summary, classification bindings, ref targets) | ST-02 | MOC-06, MOC-07, MOC-12 — **may update**; **must not** freeze live gate index into stable manifest facet (MAP-05) |

### Principle MRDY-IMPL-01 — Readiness ritual vs physical representation

Playbook 01 **owns** MRDY attestation. RT-G10 **owns** faithful MOC-* representation of attested categories — **not** re-evaluation gates, **not** automated MRDY pass/fail engine.

### Principle MRDY-IMPL-02 — MRDY-06 is the MVP hinge

MVP success S2 maps **directly** to MOC-01 physical materialization. Standard is **incomplete** if entry anchor discoverability is ambiguous.

### MVP manifest bind readiness checklist (operator, post-standard)

Before claiming C3 satisfied on pilot:

| # | Check |
|---|-------|
| R-M1 | Playbook 01 manifest-enrolled outcome recorded (doctrinal) |
| R-M2 | MOC-01 entry anchor discoverable within authorized zone |
| R-M3 | MOC-02…MOC-05 present and consistent with enrollment attestation |
| R-M4 | MOC-08 topology points to POC-03…POC-05/POC-09 loci (even if indexes empty) |
| R-M5 | MOC-07 absent or pointer-only — no live gate index in manifest facet |
| R-M6 | No Passport / registry-card / tracking-index duplication in POC-02 manifest facet |
| R-M7 | Operator reaches manifest entry from Registry pointer or direct knowledge without archaeology |

---

## RT-G04 Relationship

RT-G04 **hosts** manifest binding; RT-G10 **populates** POC-02 manifest facet **within** substrate assumptions H-01…H-10 — **without** storage redesign.

### Consumption of RT-G04 assumptions

| Assumption ID | RT-G10 implementation binding |
|---------------|-------------------------------|
| **H-01** | Manifest physical bind **occurs within** `workspaces/website-factory-operations/` — zone **must exist or be created** before bind |
| **H-02** | MOC-* content **resides in** exactly **one** stable per-project record home per Factory Project |
| **H-03** | All MOC-* serialization **within** POC-02 manifest facet — RT-G10 **defines content classes**, not substrate zone |
| **H-04** | Manifest bind **may exist without** POC-02 registry facet entry — MR-01 honored |
| **H-05** | MOC-10 enrollment metadata **follows** Playbook 01 doctrinal enrolled — **no** auto-bind on folder/git discovery |
| **H-06** | MOC-08 topology **may point to** POC-03…POC-05 on same substrate (MAP-05 pointer pattern) |
| **H-07** | Manifest facet **must not** duplicate POC-03…POC-05 as live authoritative gate/state index (MT-01) |
| **H-08** | Manifest bind/amend acts **do not** grant Playbook 04 automation path to POC-03…POC-07 |
| **H-09** | MOC-12 **may reference** POC-08 closure metadata — **must not** own closure plane |
| **H-10** | MOC-11 amendment narrative **inherits** append-only honesty (P7, INT-01) |

### Bind sequence on substrate (implementation, not workflow)

```text
  PRE-FACTORY (no zone manifest records)
       │
       ▼
  Playbook 01 ──▶ manifest-enrolled (doctrinal)
       │
       ▼
  Operator manifest bind act ──▶ POC-01 + POC-02(m) + POC-09 refs
       │                              MOC-01…MOC-12 per rules
       ▼
  Playbook 02 / RT-G05 (optional) ──▶ registry pointer TO manifest anchor
       │
       ▼
  Playbook 03 ──read──▶ MOC-01 entry + POC-03…07 indexes
       │
       ▼
  Playbook 04 ──write──▶ POC-03…07 (separate plane — not manifest facet)
```

### Co-location policy (OQ-M04 — resolved at implementation standard)

| Rule ID | Implementation rule |
|---------|---------------------|
| **COL-01** | Manifest facet (POC-02 manifest) and tracking indexes (POC-03…POC-07) **may share** same per-project record home container |
| **COL-02** | **Must remain** separate **record classes** on disk — POC-RULE-02, MOC-RULE-02 |
| **COL-03** | **Forbidden:** single undifferentiated record merging MOC-08 topology with live POC-04 gate tail as co-authoritative |
| **COL-04** | Serialization format choice **does not** determine co-location — class separation **is normative** |

### Optional Tracking zone serialization (OQ-M01 — resolved at implementation standard)

| Rule ID | Implementation rule |
|---------|---------------------|
| **TZ-01** | **Default MVP:** MOC-X1 **absent** — all live indexes remain POC-03…POC-07 only |
| **TZ-02** | **If authorized later:** MOC-X1 **may** hold **non-authoritative** snapshot of **selected** zones — **never** gate/handoff live index |
| **TZ-03** | Any MOC-X1 **must be labeled** derived/subordinate — DR-01 analog within manifest facet |

**Principle G04-IMPL-01:** RT-G10 **must not** require substrate redesign — COL-* and TZ-* resolve **within** this standard, not by expanding RT-G04 scope.

---

## Registry Relationship

Registry **depends on** Manifest implementation for stable pointer; RT-G10 **enables** catalog linkage — **without** catalog design.

### What Registry may assume from Manifest implementation

| Assumption | Doctrine anchor | RT-G10 guarantee |
|------------|-----------------|------------------|
| **One stable manifest entry pointer** per enrolled project | RA-04, RAP-16 | MOC-01 discoverable locus stable for catalog slot |
| **Logical identity precedes registry entry ID** | ES-03, RA-02, RA-03 | MOC-02 carries logical identity — registry **references**, not replaces |
| **Manifest bind may exist without catalog entry** | MR-01, Playbook 01→02 | H-04 — registry enrollment **optional** |
| **Distinction summaries at catalog level — not manifest depth** | RA-05, RRDY-* | MOC-03…MOC-05 supply **source categories** for card summaries — RT-G05 **derives** display, **not** manifest |
| **Manifest enrollment precedes registry enrollment** | RD-02, RET-03 | MOC-10 enrollment metadata **predates** catalog declare |
| **Withdrawn catalog ≠ manifest revocation** | Playbook 05, CL-03 analog | Manifest facet **persists** — registry status **orthogonal** |

### What Registry must never derive independently

| Forbidden independent derivation | Reason |
|----------------------------------|--------|
| Factory Project logical identity **without** manifest anchor | MR-01, REG-REL-01 |
| Charter intent, scope tier, endpoint **from** catalog card alone | RA-05 depth limit |
| Reference topology **from** portfolio listing | Category 7 lives in manifest facet |
| Manifest-enrolled status **from** filesystem scan | RD-04, RAP-10 |
| Live tracking depth **from** registry card | RA-05, MT-01 |

### Dependency edge

```text
  MOC-01 Entry anchor (RT-G10)
       │
       │ stable pointer
       ▼
  RT-G05 POC-02 registry facet ──▶ catalog card Manifest pointer
       │
       │ portfolio select
       ▼
  Playbook 03 / RT-G12 ──▶ read MOC-01 then POC-03…07
```

**Principle REG-IMPL-01:** RT-G10 **must not** embed registry catalog content in manifest facet — **pointer target**, not catalog owner.

**Principle REG-IMPL-02:** RT-G05 implementation **must not precede** stable MOC-01 on pilot — ordering per Implementation Planning Review.

---

## Tracking Relationship

Tracking **owns** instance indexes on substrate; Manifest **precedes** deep read; RT-G10 **must not** duplicate Tracking (MT-01).

### What Tracking / Surface may assume from Manifest implementation

| Assumption | Consumer | RT-G10 guarantee |
|------------|----------|------------------|
| Entry anchor **reachable** without repo-wide search | Playbook 03 E4; MRDY-06 | MOC-01 discoverable |
| Minimum understanding categories **already attested** | Playbook 03 OR-01 | MOC-02…MOC-05 reflect Playbook 01 attestation |
| Topology pointers **exist** for authoritative sources | Surface PO-* | MOC-08 + MOC-12 declare targets |
| Active state in manifest orientation **matches** Engine or flagged invalid | MS-02 | MOC-07 **pointer-only** or absent — reconcilable |
| Manifest facet **does not hold** live gate/handoff index | MT-01, SRDY-09, MAP-05 | MOC-X1 default absent; POC-04/05 sole live index |

### What Tracking knows that Manifest must never store inside manifest facet

| Tracking knowledge | Manifest exclusion |
|--------------------|-------------------|
| Full gate outcome index with STALE/INVALID | POC-04 — not MOC-* duplicate |
| Complete handoff event sequence | POC-05 |
| Artefact ref index exhaustiveness | POC-09 |
| Eligibility snapshot, open gate set | Derived — DR-01 |
| Append-only audit trail detail | POC-06, POC-07 |
| Eight Surface question **answers** | RT-G12 read binding |
| State history / progression ledger bodies | POC-03 history zones |

### Playbook write plane separation

| Playbook | Manifest facet interaction |
|----------|---------------------------|
| **01** | Doctrinal enrolled → **triggers** bind obligation; **does not** write MOC-* without bind act |
| **03** | **Read** MOC-01…MOC-08; depth in POC-03…POC-07 |
| **04** | **Mutates** POC-03…POC-07 only — **may** require MOC-07 pointer refresh **via separate operator manifest amend**, not as side effect of declaration |
| **05** | Manifest enrollment **never revoked** — MOC-* **persists**; MOC-12 **may add** closure ref |

**Principle TRK-IMPL-01:** Surface-ready ⊇ manifest-ready ⊄ manifest bind complete — SRDY-* indexes remain **substrate P4** + RT-G12, **not** manifest duplication.

**Principle TRK-IMPL-02:** Playbook 04 declaration **must not** silently append live gate rows into POC-02 manifest facet — INT-M06.

---

## Integrity Model

Minimum manifest binding integrity expectations for MVP — **without** validators, automated checks, or RT-G11.

### Core integrity standards

| ID | Standard | Implementation expectation |
|----|----------|---------------------------|
| **INT-M01** | **Enrollment-before-bind honesty** | MOC-10 **must** reference Playbook 01 enrollment act — bind **without** prior enrolled **forbidden** |
| **INT-M02** | **Single entry anchor** | Exactly **one** MOC-01 per Factory Project identity — no competing anchors |
| **INT-M03** | **Stable category amendment narrative** | MOC-11 append-oriented — corrections to MOC-02…MOC-05 **via** amendment, not silent overwrite (ST-01, AT-*) |
| **INT-M04** | **Topology pointer validity (minimal)** | MOC-12 locators **identify** target loci — broken refs **visible** to operator; no silent copy of external bodies |
| **INT-M05** | **Plane separation** | POC-02 manifest facet **must not** embed POC-04/POC-05 live tails as co-authoritative (MT-01, MAP-05) |
| **INT-M06** | **Declaration plane isolation** | Playbook 04 acts **must not** mutate MOC-* as automatic side effect — manifest amend **separate operator act** |
| **INT-M07** | **Position summary honesty** | MOC-07 **matches** POC-03 active state **or** marked invalid/unset — MS-02 |
| **INT-M08** | **Identity distinctness** | MOC-02 logical identity **≠** registry entry ID when catalog exists — ES-03 |
| **INT-M09** | **Human-only bind path** | Only operator manifest bind/amend acts **authoritatively change** MOC-* — SC-03, OA-ACT-04 |
| **INT-M10** | **Closure persistence non-ownership** | POC-08 **referenced** by MOC-12 **optional** — manifest **does not** replace Playbook 05 primary write |

### What integrity model explicitly excludes

| Excluded | Reason |
|----------|--------|
| Automated schema validation of manifest facet | RT-G11 post-MVP |
| MRDY pass/fail re-evaluation engine | Playbook 01 owns attestation |
| CI/git-hook auto-bind | INT-M09 |
| Cross-record referential integrity engine | Single-operator MVP; operator resolves |
| Automated sync manifest ↔ tracking indexes | INT-M06 |

### Integrity verification (human-operated)

MVP **accepts** operator manual review: Playbook 03 session surfaces MOC-07/POC-03 mismatches; Playbook 01 checklist covers MRDY-07 role distinction. Formal validators **deferred**.

---

## Boundary Protection

RT-G10 manifest implementation **must never become** the following — inherited from Manifest Charter, planning charter, RT-G04 separation, MVP exclusions.

### Forbidden system roles

| Manifest implementation must not become | Guard |
|------------------------------------------|-------|
| **Passport** — parallel mega-document SoT | MA-03, MAP-06, BV-15 |
| **Registry / portfolio catalog** | MAP-07, MR-02; RT-G05 |
| **Tracking composition / live observability index** | MT-01, MAP-05; POC-03…07 |
| **Tracking Surface / operator dashboard** | MAP-09, TS-01; RT-G12 |
| **Persistence substrate product** | MAP-01; RT-G04 owns zone |
| **Database / query engine / multi-tenant store** | MAP-02; DF-02 sufficient |
| **Workflow engine / state machine executor** | MAP-04, MAP-12; RT-G01 |
| **Factory runtime product** | SC-01; RT-G09 |
| **Gate Results System** | MAP-10; POC-04 |
| **Project management system** | Tasks, sprints beyond charter category |
| **Automation / discovery enrollment** | Playbook 01 forbidden automation; RD-04 |
| **Foundation authority merge** | MAP-08; Legal Pack, Site Type matrices embedded |
| **Handoff package / artefact body store** | MAP-11; RR-02 |
| **Closure registry / terminal workflow engine** | Playbook 05 + POC-08 primary |
| **Validator / gate authority engine** | RT-G11 |
| **Declaration / progression ledger owner** | POC-06/07; Playbook 04 |

### Forbidden content inside manifest facet

| Must never persist as manifest-owned authoritative content | Actual owner |
|-------------------------------------------------------------|--------------|
| Live gate outcome rows | POC-04 |
| Live handoff event sequence | POC-05 |
| Full state history | POC-03 |
| Declaration event bodies | POC-06 |
| Progression ledger | POC-07 |
| Registry catalog entries | POC-02 registry facet |
| Layer artefact bodies | External workspaces |
| Gate/handoff criteria text | Runtime Architecture |
| Site Type Registry definitions | Foundation `registry/` |

### Implementation anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| Single «manifest.yaml» swallowing manifest + full tracking | MOC-RULE-02; POC-RULE-02 |
| Manifest facet containing seven Surface answers | RA-05; RT-G12 scope |
| Physical bind **before** Playbook 01 enrolled | INT-M01; MR-REL-01 |
| Registry impl creating manifest content as side effect | REG-IMPL-01 |
| MOC-07 frozen copy of gate index labeled «stable» | ST-02, MAP-05 |
| Manifest bind triggering automated POC-03 mutation | INT-M06; H-08 |
| `COMPLETE` / deploy conflated with manifest «completion» | MAP-13, MS-04 |

**Principle BP-IMPL-01:** Physical manifest binding **extends operability** of entry anchor doctrine — **does not execute** Factory movement or replace Engine declaration authority.

---

## RT-G05 Handoff Assumptions

RT-G05 Registry Implementation Standard **may assume** the following from RT-G10 Manifest Implementation Standard — **without** RT-G05 redefining manifest doctrine or substrate.

### Guaranteed manifest provisions for Registry

| Assumption ID | RT-G05 may assume |
|---------------|-------------------|
| **M-H01** | Each manifest-bound Factory Project exposes **one** stable MOC-01 entry anchor discoverable within authorized zone |
| **M-H02** | MOC-02 logical identity reference **stable** for catalog slot linkage — distinct from registry entry ID |
| **M-H03** | Manifest bind **may exist** before any POC-02 registry facet entry — catalog enrollment **optional** |
| **M-H04** | MOC-10 enrollment metadata confirms Playbook 01 preceded bind — registry **must not** treat discovery as enrollment |
| **M-H05** | MOC-03 scope tier and MOC-04 endpoint **available** as **source categories** for distinction summaries — RT-G05 **does not** duplicate full charter in catalog |
| **M-H06** | MOC-01 locus **stable** across registry withdraw/re-enroll — catalog status **orthogonal** to manifest persistence |
| **M-H07** | MOC-08 topology **not required** in registry card — catalog holds **pointer to manifest entry**, not full map-of-maps |
| **M-H08** | Manifest facet **does not embed** registry catalog — registry facet at portfolio scope **separate** POC-02 face |
| **M-H09** | Operator path Registry→Manifest **works** — MOC-01 reachable from catalog pointer without archaeology |
| **M-H10** | Append-only amendment honesty (MOC-11) applies — registry card **may show stale summary** until operator refresh; **manifest facet wins** on conflict |

### Explicitly **not** provided to RT-G05 (RT-G05 must decide)

| Topic | Owner |
|-------|-------|
| Registry catalog serialization format | RT-G05 standard |
| Catalog card field template (OQ-R02) | RT-G05 standard |
| Portfolio catalog physical shape (OQ-R01 / DF-05) | RT-G05 standard |
| Derived orientation snapshot refresh policy | RT-G05 + RS-03 |
| Registry enrollment ritual steps | Playbook 02 — unchanged |

### Dependency edge (implementation sequence)

```text
  RT-G04 Implementation Standard
       │ hosts POC-01, POC-02 manifest facet
       ▼
  RT-G10 Manifest Implementation Standard (this)
       │ populates MOC-* ; M-H01…M-H10
       ▼
  RT-G05 Registry Implementation Standard
       │ populates POC-02 registry facet ; catalog pointers to MOC-01
       ▼
  RT-G12 Surface Implementation Standard
       │ reads MOC-01 + POC-03…07
```

**Principle HAND-M01:** RT-G05 **must not** require manifest facet redesign — OQ-M05 (card fields from Manifest categories) resolves **within** RT-G05 bounds using M-H05 source categories, not by expanding manifest scope.

---

## Explicit Non-Claims

This document and the RT-G10 Manifest Implementation Standard it defines:

- **are not** a Website Factory **runtime**, execution engine, workflow engine, or shipped product;
- **are not** **storage product**, **database**, **ORM**, or **multi-tenant** persistence service;
- **are not** **application**, **standalone service**, **SaaS**, or **HomeGateway** integration;
- **are not** **automation layer**, **agent orchestration**, **queue**, or **validator engine**;
- **are not** **operator UI**, **dashboard**, or **CLI** (RT-G12);
- **are not** **Registry catalog standard** (RT-G05) or **Surface read standard** (RT-G12);
- **are not** **Persistence Substrate standard** (RT-G04) — only **consumption** of H-01…H-10;
- **do not** define JSON/YAML/markdown schemas, field lists, folder trees, file naming, or database tables;
- **do not** create physical artefacts under `workspaces/website-factory-operations/`;
- **do not** modify Manifest Charter, RT-G04 Standard, Engine Stages 1–6, or Playbooks 01–05;
- **do not** claim MVP **has been built** or pilot-demonstrated with bound manifest facet;
- **do not** claim manifest binding records **exist on disk** today — **SAFE UNKNOWN** until separately created.

Human-operated declaration path remains the v1 model per Operational Model OA-ACT-04 and Playbook 04 DA-01.

Manifest remains **Entry Anchor** — **not** Passport, Tracker, Registry, or Workflow Engine.

---

## Open Questions (deferred — not blockers for this standard)

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-M02** | Partial closure metadata — Manifest category vs Tracking flag only | Playbook 05 + RT-G12; MOC-12 ref **optional** |
| **OQ-M03** | PHASE_SLICE / multi-`generation_id` — one bind per shell vs per slice | Engine v2 or operational case policy |
| **OQ-M06** | External workspace pointer — Manifest MOC-12 vs tracking-only | Operational + RT-G12 |
| **OQ-M07** | `PASS_WITH_WARNINGS` — Manifest orientation category | Validation binding — MOC-07 pointer semantics |
| **OQ-M08** | Chrome blocks without `block_id` — Manifest binding category | MOC-06 when applicable |
| **OQ-ME05** | Physical bind moment vs doctrinal Enrolled timing | **Bounded:** same session permitted; discovery bind forbidden — exact ritual **operator convention** |
| **DF-04** | Co-location layout within per-project home | COL-* resolved — internal layout **operator/tooling** |
| **DF-07…DF-10** | Git policy, pilot pointer policy, read surface form | Cross-charter; not manifest scope |

**Resolved in this standard (were OPEN in planning):**

| ID | Resolution |
|----|------------|
| **OQ-M04** | COL-01…COL-04 — separate record classes; co-location within home permitted |
| **OQ-M01** | TZ-01…TZ-03 — default exclude live indexes; MOC-X1 optional bounded extension |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **RT-G10 Manifest Implementation Standard v1** as **RT-G10 standard-complete** — second Implementation Standard in authorized sequence.
2. **Authorize next standard:** **RT-G05 Registry Implementation Standard** — catalog serialization **within** substrate and M-H01…M-H10 assumptions.
3. **Preserve sequencing:** RT-G05 → RT-G12 implementation standards — **before** physical MVP artefact creation unless separately authorized.
4. **Do not create yet:** manifest yaml/json samples, folder trees, schemas, passport documents, manifest-as-gate-index prototypes, registry-in-manifest merges under `workspaces/website-factory-operations/`.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `workspaces/website-factory-operations/` **exists** on disk today | **UNKNOWN** — RT-G04 standard records authorized zone |
| Whether any manifest binding records **exist** in-repo | **UNKNOWN** — standard authorizes; creation not part of deliverable |
| Calendar for RT-G05 Implementation Standard | **not scheduled** |
| Triumph / client workspaces as MOC-12 targets vs external-only | **UNKNOWN** — DF-08 per case |
| Operators updated NEXT-PRIORITIES to Implementation Standards era | **UNKNOWN** |

---

*RT-G10 Manifest Implementation Standard v1 — second Website Factory Implementation Standard. Canonical location: `workspaces/website-factory-reference-v1/RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G10 Manifest Implementation Standard v1

**Stage:** RT-G10 — Manifest Implementation Standard (post–Planning Charter, second Implementation Standard)  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md` (created)  
**Summary:** Второй Implementation Standard Website Factory: перевод Manifest Charter и RT-G10 planning charter в конкретную MVP-модель физического существования Manifest binding — двенадцать implementation object classes (MOC-01…MOC-12), ownership matrix (owns / references / never owns), MRDY-* implementation expectations, RT-G04 binding через H-01…H-10, relationships к Registry (M-H01…M-H10 handoff) и Tracking, minimum integrity model, boundary protection (Entry Anchor ≠ Passport/Tracker/Registry), co-location (OQ-M04) и zone serialization (OQ-M01) resolved — без runtime, schemas, folders, code и physical artefacts.  
**Git:** no commit, no push (per task; document does not recommend commit).
