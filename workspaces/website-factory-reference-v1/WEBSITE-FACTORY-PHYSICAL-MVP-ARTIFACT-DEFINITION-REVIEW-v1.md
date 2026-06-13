# REPORT — Website Factory Physical MVP Artifact Definition Review v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical MVP Artifact Era — **definition review only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE** (RT-G04, RT-G10, RT-G05, RT-G12); Physical MVP Artifact Era **AUTHORIZED**  
**Тип:** definition review only — **без** folder creation, file creation, manifests, registry entries, tracking records, schemas, storage layouts, implementation execution  
**Primary inputs:** [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md), [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md), [RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md](RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [WEBSITE-FACTORY-IMPLEMENTATION-STANDARDS-CONSOLIDATION-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-STANDARDS-CONSOLIDATION-REVIEW-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), Operational Playbooks 01–05

---

## Executive Summary

**Вердикт:** MVP Wave 1 определён как **минимальный физический набор** structured filesystem records в authorized zone `workspaces/website-factory-operations/`, достаточный для демонстрации capability floor **C2–C7** и success classes **S1–S9** на **одном Core 5 pilot case** через Playbooks 01→05 — **без** runtime, automation, workflow engine и **без** post-MVP charter artefacts.

**Wave 1 содержит:** authorized zone + per-project record home; mandatory POC-01…POC-10 (когда соответствующий playbook act произошёл); mandatory MOC-01…MOC-12 (subset per bind rules); mandatory ROC-01…ROC-10 для portfolio catalog; mandatory SOC-01…SOC-08 per-project read binding.

**Wave 1 исключает:** workflow engine records, automation/queue state, runtime products, validator authority artefacts, dashboard/SaaS assets, analytics rollups, layer bodies, Passport/mega-records, discovery-enrollment artefacts.

**Последовательность создания (Wave 1):** RT-G04 zone + homes → RT-G10 manifest bind → RT-G05 registry bind → Playbook 04 index shells (may start empty) → RT-G12 surface read bind → Playbook 04/05 population during pilot.

**Рекомендация:** **A — Begin Physical Artifact Specification** — definition достаточна; следующий authorized track = specification (serialization, layout, naming) **без** immediate physical creation until separately authorized.

**Verified repo state:** `workspaces/website-factory-operations/` **не существует** on disk — ожидаемо; Wave 1 **определён**, не создан.

---

## Physical MVP Inventory

Inventory derived from implementation object classes **POC**, **MOC**, **ROC**, **SOC** — normative **classes**, not file names, schemas, or folder trees.

### POC — Persistence Substrate (RT-G04)

| Class ID | Class name | Wave 1 disposition | Trigger / notes |
|----------|------------|-------------------|-----------------|
| **POC-01** | Identity | **Mandatory** | Per-project home; stabilized at manifest bind |
| **POC-02** | Binding (manifest + registry facets) | **Mandatory** (when bound) | Hosts MOC-* and ROC-* — **separate facets**, same class ID |
| **POC-03** | State | **Mandatory** | After first Playbook 04; **empty shell permitted** at `NEW_PROJECT` |
| **POC-04** | Gate | **Mandatory** | After first Playbook 04; may start empty |
| **POC-05** | Handoff | **Mandatory** | After first Playbook 04; may start empty |
| **POC-06** | Declaration | **Mandatory** | Append-only; first Playbook 04 act |
| **POC-07** | Ledger | **Mandatory** | Append-only; first Playbook 04 act |
| **POC-08** | Closure | **Mandatory when Playbook 05 executed** | Not required at Wave 1 bootstrap |
| **POC-09** | Reference | **Mandatory** | Topology + external workspace pointers at manifest bind |
| **POC-10** | Audit | **Mandatory** | After first Playbook 04 or explicit recency marker |
| **POC-D1** | Derived cache | **Optional** | Regeneratable; non-authoritative |
| **POC-O1** | Operational note | **Optional** | Playbook 03 session notes |
| **POC-O2** | Enrollment draft | **Optional** | Pre-bind notes; not authoritative |

### MOC — Manifest Binding (RT-G10, within POC-02 manifest facet)

| Class ID | Class name | Wave 1 disposition | Trigger / notes |
|----------|------------|-------------------|-----------------|
| **MOC-01** | Entry anchor | **Mandatory** on bind | MVP hinge — S2, C3, MRDY-06 |
| **MOC-02** | Identity | **Mandatory** | Category 1 |
| **MOC-03** | Scope | **Mandatory** | Category 2; minimal intake valid |
| **MOC-04** | Endpoint | **Mandatory** | Category 3 |
| **MOC-05** | Applicability | **Mandatory** | Category 4 |
| **MOC-06** | Classification anchors | **Conditional mandatory** | When lifecycle demands; may defer at bind |
| **MOC-07** | Position summary | **Optional** | Pointer-only; must not duplicate live state |
| **MOC-08** | Topology | **Mandatory** | Category 7; points to POC-03…09 loci |
| **MOC-09** | Foundation pins | **Optional** | Category 8 when declared |
| **MOC-10** | Enrollment | **Mandatory** on bind | Links to Playbook 01 act |
| **MOC-11** | Amendment | **Mandatory when amendments occur** | Append-oriented |
| **MOC-12** | External refs | **Mandatory** | Category 7 target locators |
| **MOC-X1** | Tracking zone snapshot | **Forbidden default** | Default absent (TZ-01) |
| **MOC-O1** | Pre-bind draft | **Optional** | Not authoritative until bind |

### ROC — Registry Catalog (RT-G05, within POC-02 registry facet at portfolio scope)

| Class ID | Class name | Wave 1 disposition | Trigger / notes |
|----------|------------|-------------------|-----------------|
| **ROC-01** | Catalog aggregate | **Mandatory** for C4/S3 | One central portfolio listing (TOP-01) |
| **ROC-02** | Catalog entry | **Mandatory** per enrolled project | One slot per logical Factory Project |
| **ROC-03** | Registry entry identity | **Mandatory** | Distinct from ROC-04 |
| **ROC-04** | Logical identity reference | **Mandatory** | Points to MOC-02 / POC-01 |
| **ROC-05** | Manifest pointer | **Mandatory** | Hard pointer to MOC-01 (RM-01) |
| **ROC-06** | Distinction summary | **Mandatory** | Echo of MOC-03…05 — not full bodies |
| **ROC-07** | Discoverability status | **Mandatory** | discoverable / withdrawn / archived |
| **ROC-08** | Orientation snapshot | **Optional** | Default absent (OS-01); non-authoritative |
| **ROC-09** | Enrollment bind metadata | **Mandatory** on catalog bind | Links to Playbook 02 act |
| **ROC-10** | Catalog amendment narrative | **Mandatory when lifecycle events** | Append-oriented |
| **ROC-11** | External workspace pointer | **Optional** | Refs only |
| **ROC-X1** | Derived orientation cache | **Optional** | Non-authoritative |
| **ROC-O1** | Pre-bind draft | **Optional** | Not authoritative until bind |

### SOC — Surface Read Binding (RT-G12, read composition — not substrate storage)

| Class ID | Class name | Wave 1 disposition | Trigger / notes |
|----------|------------|-------------------|-----------------|
| **SOC-01** | Read convergence point | **Mandatory** | C5/S4 hinge; one per project |
| **SOC-02** | Orientation view | **Mandatory** | Question #1 |
| **SOC-03** | State view | **Mandatory** | Question #2 |
| **SOC-04** | Blocking view | **Mandatory** | Question #3 |
| **SOC-05** | Completion view | **Mandatory** | Question #4 |
| **SOC-06** | Remaining view | **Mandatory** | Question #5 |
| **SOC-07** | Recency view | **Mandatory** | Question #6; REC-01…04 |
| **SOC-08** | Forward view | **Mandatory** | Question #7 |
| **SOC-09** | Integrity warnings | **Mandatory when detected** | Cross-index reconciliation |
| **SOC-10** | Portfolio select assist | **Optional** | Recommended for full S3 path demo |
| **SOC-11** | Tier S-B conditional views | **Optional** | When substrate supplies data |
| **SOC-D1** | Derived read cache | **Optional** | Non-authoritative |
| **SOC-O1** | Session read notes | **Optional** | Not SRDY-07 authority |

### Cross-model composition (Wave 1 logical layout)

```text
  workspaces/website-factory-operations/          ← Wave 1 Step 1 (RT-G04)
  │
  ├── portfolio scope
  │     └── POC-02 registry facet
  │           └── ROC-01…ROC-10 (+ optional ROC-11/X1/O1)   ← Wave 1 Step 3 (RT-G05)
  │
  └── per-project record home (one per pilot)       ← Wave 1 Step 1 (RT-G04 P1)
        ├── POC-01 identity
        ├── POC-02 manifest facet → MOC-01…MOC-12   ← Wave 1 Step 2 (RT-G10)
        ├── POC-03…POC-07 (+ POC-10)                ← Wave 1 Step 4 (Playbook 04 path)
        ├── POC-08 (on Playbook 05)                 ← Wave 1 Step 6 (pilot closure)
        ├── POC-09 external refs
        └── SOC-01 → SOC-02…SOC-09                  ← Wave 1 Step 5 (RT-G12)
```

**Principle INV-01:** Wave 1 inventory = **classes that may be physically instantiated** under authorized zone — **not** a prescription of serialization format, folder tree, or file count.

---

## Mandatory Artifacts

Mandatory = **required for MVP Wave 1 success** (C2–C7, S1–S9 on one Core 5 pilot). Justification anchored to MVP Definition, standards, and Playbooks 01–05.

### Tier 0 — Zone infrastructure (C2)

| Artifact class | Standard | MVP justification |
|----------------|----------|-------------------|
| **Authorized zone** at `workspaces/website-factory-operations/` | RT-G04 AZ-01…07, DF-03 | C2 — единый physical layer; без zone нет substrate |
| **Per-project record home** (exactly one per Factory Project) | RT-G04 P1, POC-RULE-01 | P1 discoverable locus; prerequisite для MOC-01 и SOC-01 |

### Tier 1 — Manifest binding (C3, S2)

| Artifact class | Standard | MVP justification |
|----------------|----------|-------------------|
| **POC-01** + **POC-02 manifest facet** | RT-G04 P2; RT-G10 | C3 physical binding |
| **MOC-01…MOC-05, MOC-08, MOC-10, MOC-12** | RT-G10; MRDY-01…06 | S2 entry anchor + minimum understanding |
| **MOC-06** when classification mandatory per charter | RT-G10 | Core 5 pilot typically requires site_type binding |
| **POC-09** topology refs at bind | RT-G04 P8; MOC-08 | Operator locates indexes without archaeology |

**Doctrinal precondition (not a disk artefact):** Playbook 01 manifest-enrolled outcome **must precede** physical bind (INT-M01, LC-01).

### Tier 2 — Registry catalog (C4, S3)

| Artifact class | Standard | MVP justification |
|----------------|----------|-------------------|
| **ROC-01** catalog aggregate | RT-G05 TOP-01 | S3 — portfolio listing without per-workspace search |
| **ROC-02…ROC-07, ROC-09** per enrolled pilot | RT-G05; RRDY-* | C4 — catalog-discoverable with manifest pointer |
| **ROC-05 → MOC-01** pointer chain | RM-01, M-H01 | Registry → Manifest operator path |

**Note:** Single-project Factory path **without** catalog remains doctrinally valid (M-H03, G05-REL-02), but **MVP Definition** includes C4/S3 for demonstration — Wave 1 **mandates** registry bind for the pilot demo track.

### Tier 3 — Tracking indexes (C6, S5)

| Artifact class | Standard | MVP justification |
|----------------|----------|-------------------|
| **POC-03…POC-07, POC-10** | RT-G04 P4/P5; Playbook 04 | C6 — declarations reflected in persisted indexes |
| **POC-06, POC-07** on first declaration | INT-01, P7 | Append-only declaration honesty |

**Wave 1 bootstrap allowance:** POC-03…POC-05 **may exist as empty index loci** at `NEW_PROJECT` after manifest bind; **meaningful C5/S4** requires at least one Playbook 04 declaration cycle before Playbook 03 demonstration (RT-G12 COMP-02).

### Tier 4 — Surface read binding (C5, S4)

| Artifact class | Standard | MVP justification |
|----------------|----------|-------------------|
| **SOC-01…SOC-08** | RT-G12; eight questions | S4 — Playbook 03 without full-repo search |
| **SOC-09** when integrity conditions detected | RT-G12 INT-S04…S10 | VP-04, MS-02 reconciliation visibility |

### Tier 5 — Closure (C7, S6)

| Artifact class | Standard | MVP justification |
|----------------|----------|-------------------|
| **POC-08** | RT-G04 P6; Playbook 05 | S6 — terminal outcome on pilot completion |

**Timing:** POC-08 **mandatory for full pilot path** but **not** part of Wave 1 bootstrap — created when Playbook 05 executes.

### Capability mapping summary

| Capability | Wave 1 mandatory physical classes |
|------------|-----------------------------------|
| **C2** | Authorized zone, per-project home, POC taxonomy host |
| **C3** | POC-01, POC-02(m), MOC-01…05/08/10/12, POC-09 |
| **C4** | ROC-01…07, ROC-09, ROC-05 |
| **C5** | SOC-01…08 (+ SOC-09 when applicable) |
| **C6** | POC-03…07, POC-06, POC-07, POC-10 |
| **C7** | POC-08 (on closure) |

---

## Optional Artifacts

May exist in Wave 1 **without blocking** MVP success if omitted.

| Class(es) | Rationale for optional | If omitted |
|-----------|------------------------|------------|
| **POC-D1** | Derived convenience only (DR-01) | Playbook 03 reads POC-03…07 directly |
| **POC-O1, POC-O2** | Pre-declaration / pre-bind notes | Manual notes outside zone acceptable |
| **MOC-07** | Pointer-only orientation; may omit | SOC-03 reads POC-03 directly |
| **MOC-09** | Foundation pins when not declared | Valid for early intake |
| **MOC-O1** | Pre-bind draft | Playbook 01 attestation sufficient |
| **ROC-08, ROC-X1** | Non-authoritative glance (OS-01 default absent) | ROC-06 distinction sufficient for S3 |
| **ROC-11** | External workspace on card | POC-09 / MOC-12 carry refs |
| **ROC-O1** | Pre-bind catalog draft | Playbook 02 attestation sufficient |
| **SOC-10** | Portfolio select assist | Direct MOC-01 navigation valid (G05-REL-02) |
| **SOC-11** | Tier S-B conditional | S-A classes sufficient for MVP floor |
| **SOC-D1, SOC-O1** | Read-side convenience | Direct index read sufficient |

**Second pilot project:** Not required for Wave 1 closure — **may** validate C2 generality (MVP Definition optional success signal).

---

## Forbidden Artifacts

Must **not** exist in Wave 1 — violation of MVP, standards, or boundary rules.

### Forbidden system roles (no physical artefact class)

| Forbidden role | Guard | Why Wave 1 excludes |
|----------------|-------|---------------------|
| **Workflow engine / state machine executor** | RT-G01, MAP-04 | Transitions declared, not executed |
| **Factory runtime product** | RT-G09, SC-01 | MVP ≠ shipped runtime |
| **Automation layer mutating indexes** | RT-G03, SC-03, INT-08 | Violates OA-ACT-04, DA-01 |
| **Agent orchestration records** | RT-G02 | No AI declarer |
| **Queue / scheduler state** | RT-G06, RAP-04 | Single-operator MVP |
| **Validator / gate authority engine** | RT-G11 | Human Playbook 04 only |
| **Execution logs as authority** | RT-G07 | Post-MVP |
| **MIG pipeline SoT** | RT-G08 | External integration |
| **Notification / webhook hub** | RT-G13 | Post-MVP |
| **Rollback automation state** | RT-G15 | Post-MVP |
| **Multi-operator concurrency / RBAC** | RT-G14 | Single-operator scope |
| **Operator dashboard / SaaS / widget product** | TX-07, FF-02 | Read binding ≠ UI product |
| **Portfolio analytics / KPI rollups** | RA-05 extension | Not Registry v1 |
| **CRM / project management artefacts** | Scope creep | Tasks, sprints, pipeline |
| **Database / ORM / multi-tenant store** | DF-02, MAP-02 | Filesystem-backed sufficient |

### Forbidden storage content in authorized zone

| Content | Actual owner | Standard guard |
|---------|--------------|----------------|
| Layer artefact bodies (Legal Pack, blueprints, HTML, src) | T1 / external workspaces | RR-02, MAP-11 |
| Gate/handoff **criteria** definitions | Runtime Architecture | MAP-10 |
| Handoff package payloads | Generation Outputs | MAP-11 |
| Site Type Registry entries | Foundation `registry/` | RAP-11 |
| Engine doctrine copies | `website-factory-reference-v1/` | AZ-02 |
| Automated transition logs as SoT | RT-G07 | BP forbidden storage |
| Agent chat, CI logs, MIG transcripts as SoT | External | RAP-18 |
| Deploy/hosting state | Post-Factory | Charter boundary |

### Forbidden artefact anti-patterns

| Anti-pattern | Prevention |
|--------------|------------|
| **Passport / unified project mega-record** | MA-03, MAP-06, BV-05 |
| **Single file swallowing manifest + tracking + surface** | POC-RULE-02, MOC-RULE-02, ROC-RULE-03, SOC-RULE-02 |
| **Registry card with eight Surface answers** | RA-05, RE-01 |
| **Manifest facet with live gate/handoff index** | MT-01, MAP-05, MOC-X1 default absent |
| **Surface read layer duplicating POC-04/05 as SoT** | SRDY-09, INT-S05 |
| **Discovery / git-scan enrollment records** | RD-04, RAP-10, BIND-03 |
| **Physical bind before doctrinal enrollment** | INT-M01, INT-R01 |
| **Runtime records** (execution state, workflow queues, automation state) | Explicit MVP exclusions |
| **Analytics dashboards / BI assets** | TX-07, BP sections |
| **FACTORY-DASHBOARD-v1, UI spec, tracking storage schemas** | RT-G12 Recommended Next Step forbidden list |

**Principle FORB-01:** If an artefact **executes**, **mutates indexes without Playbook 04**, or **substitutes** Manifest/Registry/Tracking/Surface planes — it is **forbidden** in Wave 1.

---

## Creation Sequence

Logical order validated against RT-G04 → RT-G10 → RT-G05 → RT-G12 standards chain and Playbooks 01–05 lifecycle.

### Normative Wave 1 creation sequence

```text
  PHASE A — SUBSTRATE (RT-G04)
  ─────────────────────────────
  A1. Operator authorization for physical creation (governance — not optional)
  A2. Create authorized zone: workspaces/website-factory-operations/
  A3. Create per-project record home for pilot (POC-01 shell / P1 locus)

  PHASE B — MANIFEST (RT-G10)          [requires Playbook 01 doctrinal enrolled]
  ─────────────────────────────
  B1. Operator manifest bind act
  B2. Materialize POC-02 manifest facet: MOC-01…MOC-12 per mandatory rules
  B3. Populate POC-09 topology refs (point to index loci even if empty)

  PHASE C — REGISTRY (RT-G05)          [requires Playbook 02 doctrinal enrolled]
  ─────────────────────────────
  C1. Operator catalog bind act
  C2. Materialize ROC-01 aggregate + ROC-02 entry for pilot
  C3. Wire ROC-05 → MOC-01 pointer

  PHASE D — TRACKING INDEX SCAFFOLD (RT-G04 / Playbook 04 path)
  ─────────────────────────────
  D1. Establish POC-03…POC-05 index loci (empty allowed at NEW_PROJECT)
  D2. First Playbook 04 declaration → POC-06, POC-07, POC-03…05 mutations, POC-10

  PHASE E — SURFACE READ BIND (RT-G12) [requires MOC-01 + index loci]
  ─────────────────────────────
  E1. Operator read-bind act → SOC-01 convergence point
  E2. Wire SOC-02…SOC-08 composition to POC-* + MOC-* read feeds
  E3. Optional SOC-10 portfolio select assist (ROC-01 → MOC-01 chain)

  PHASE F — PILOT OPERATION (Playbooks 03↔04↔05)
  ─────────────────────────────
  F1. Playbook 03 sessions via SOC-* read path (repeat)
  F2. Playbook 04 declarations populate POC-* (repeat)
  F3. Playbook 05 → POC-08 closure metadata
  F4. Optional ROC-07 archived update (orthogonal to POC-08)
```

### Sequence validation matrix

| Edge | Valid? | Evidence |
|------|--------|----------|
| RT-G04 before RT-G10 | **Yes** | H-01…H-02; zone + P1 before MOC-* |
| RT-G10 before RT-G05 per entry | **Yes** | REG-IMPL-02; ROC-05 → MOC-01 |
| RT-G05 before RT-G12 SOC-10 | **Yes** | Optional; SOC-10 consumes ROC-* |
| RT-G10 before RT-G12 SOC-01 | **Yes** | SOC-01 starts from MOC-01 |
| Playbook 01 enrolled before manifest bind | **Yes** | INT-M01, MR-REL-01 |
| Playbook 02 enrolled before registry bind | **Yes** | INT-R01, BIND-01 |
| Meaningful SOC-02…08 before first Playbook 04 | **Partial** | Empty-allowed signals valid; **depth** needs declarations (COMP-02) |
| Playbook 04 before Playbook 03 demo (recommended) | **Yes** | At least one declaration cycle for credible S4 |
| RT-G12 before RT-G04 substrate | **No** | SC-02; forbidden |
| Registry bind before manifest anchor | **No** | G04-IMPL-02; forbidden |
| Physical bind before doctrinal enrollment | **No** | Discovery bind forbidden |
| Surface read bind auto-mutating POC-* | **No** | TRK-REL-01; forbidden |

**Principle SEQ-01:** Standards sequencing (RT-G04→10→05→12) maps **directly** to Wave 1 physical creation phases A→E; Playbook operational cycle (03↔04→05) is **Phase F**, not a substitute for phases A–E.

---

## Pilot Viability Review

Minimum physical set to run **one Core 5 pilot** (LANDING / CORPORATE / ECOMMERCE / PORTFOLIO / SERVICE) through Playbooks 01–05.

### Playbook → minimum physical prerequisites

| Playbook | Minimum physical set at start | Physical writes during playbook |
|----------|------------------------------|--------------------------------|
| **01** Manifest enrollment | **None required** (doctrinal only) | After enrolled: Phase B manifest bind |
| **02** Registry enrollment | Phase B complete (MOC-01 stable) | Phase C registry bind |
| **03** Surface session | Phases B–E; POC-03…07 populated for credible session | Optional POC-O1 / SOC-O1 only |
| **04** Declaration | Phases A–E; index loci exist | POC-03…07, POC-06, POC-07, POC-10 |
| **05** Closure | Full track records; POC-03…07 history | POC-08; optional ROC-07 archived |

### Minimum bootstrap set (before Playbook 03 first session)

| # | Physical element | Phase |
|---|------------------|-------|
| 1 | Authorized zone exists | A2 |
| 2 | One per-project record home | A3 |
| 3 | MOC-01…MOC-05, MOC-08, MOC-10, MOC-12 bound | B |
| 4 | POC-09 refs to index loci | B |
| 5 | ROC-01 + pilot ROC-02 with ROC-05→MOC-01 | C |
| 6 | POC-03…POC-05 loci (empty OK) | D1 |
| 7 | SOC-01…SOC-08 read binding wired | E |
| 8 | At least one Playbook 04 declaration (recommended before 03 demo) | D2 |

### Operator path viability check

| Path step | Wave 1 support |
|-----------|----------------|
| Portfolio select → project | ROC-01 → ROC-05 → MOC-01 (SOC-10 optional) |
| Manifest entry → depth | MOC-01 → MOC-08 → POC-03…07 |
| Eight Surface questions | SOC-02…SOC-08 compose from bound data |
| Declaration → visible truth | Playbook 04 → POC-* → next read reflects (INT-S03) |
| Closure → persisted terminal | Playbook 05 → POC-08 |

**Pilot viability verdict:** Wave 1 inventory **sufficient** for Core 5 pilot **if** phases A–E complete before Playbook 03 demonstration and at least one Playbook 04 cycle provides index depth.

---

## Readiness Review

### Is Wave 1 artifact set sufficient?

| Question | Answer |
|----------|--------|
| Covers C2–C7? | **Yes** — mapped in Mandatory Artifacts |
| Covers S1–S9 success path? | **Yes** — with Phase F operational execution |
| Aligns with four implementation standards? | **Yes** — POC/MOC/ROC/SOC inventory matches standards |
| Aligns with MVP Definition Review? | **Yes** — capability floor preserved |
| Aligns with Consolidation Review? | **Yes** — physical era authorized; no standards gaps blocking |
| Sufficient for specification phase? | **Yes** — classes defined; serialization/layout deferred **by design** |
| Sufficient alone to claim MVP built? | **No** — physical instantiation + pilot evidence required |

### What Wave 1 definition deliberately does NOT resolve (specification era)

| Topic | Disposition | Blocks Wave 1 definition? |
|-------|-------------|---------------------------|
| Serialization format (JSON/YAML/markdown) | Physical Artifact Specification | **No** |
| Per-project home internal layout | Specification + operator tooling | **No** |
| DF-07 form factor choice (markdown index vs CLI vs static HTML) | Operator at first SOC bind | **No** |
| DF-08 pilot workspace pointer policy | Per-case operational | **No** |
| DF-10 git policy for SoT records | Operator workshop | **No** |
| Exact recency window N (OQ-TS01) | Playbook 03 convention | **No** |

### Readiness verdict

**Wave 1 definition is complete and sufficient** to authorize **Physical Artifact Specification** as the next track. **Physical creation** remains subject to **separate operator authorization** per all implementation standards.

---

## Risk Review

### Definition risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Wave 1 confused with «create everything on day one» | **MEDIUM** | Phased sequence A–F; POC-08 only on Playbook 05 |
| Optional classes documented as mandatory | **LOW** | Optional Artifacts section explicit |
| Registry treated as optional despite MVP C4 | **LOW** | Mandatory section clarifies demo track requires ROC-* |
| SOC-* mistaken for dashboard product | **LOW** | Forbidden list + FF-02 guard |
| Class separation lost in specification | **MEDIUM** | Specification must enforce POC-RULE-02 across format choice |

### Implementation risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Zone path creation without operator authorization | **HIGH** | Phase A1 governance gate |
| Mega-record anti-pattern in first physical files | **HIGH** | Forbidden list; specification review |
| Registry bind before stable MOC-01 | **HIGH** | Sequence validation; G04-IMPL-02 |
| Playbook 03 demo before any Playbook 04 indexes | **MEDIUM** | Pilot viability recommends D2 before 03 |
| Serialization choice locks wrong co-location | **MEDIUM** | COL-* class separation normative regardless of format |
| Triumph / external workspace refs ambiguous | **LOW** | DF-08 per-case; POC-09 pointer discipline |
| v0↔v1 corpus routing confusion | **LOW** | AZ-04; OQ-OM06 hygiene |
| Scope creep into RT-G11 validators | **MEDIUM** | Forbidden; post-MVP |
| False «MVP shipped» narrative | **HIGH** | Explicit Non-Claims; S9 authority preserved |

### Risk summary

| Category | HIGH | MEDIUM | LOW |
|----------|------|--------|-----|
| Definition risks | 0 | 2 | 3 |
| Implementation risks | 3 | 4 | 2 |

**Interpretation:** HIGH implementation risks are **preventable** via sequence discipline, class separation in specification, and governance gates — **not** indicators that Wave 1 definition is incomplete.

---

## Owner Decision Review

### Resolved (inherited — no re-decision required)

| ID | Decision | Source |
|----|----------|--------|
| **DF-01** | MARS monorepo | Topology + standards |
| **DF-02** | Filesystem + structured artifacts | TOPOLOGY-B-v1 |
| **DF-03** | Factory zone = `workspaces/website-factory-operations/` | RT-G04 |
| **DF-04** | Co-location: separate record classes permitted | RT-G10 COL-* |
| **DF-05** | Central registry aggregate ROC-01 | RT-G05 TOP-* |
| **DF-06** | No HomeGateway | Topology |
| **DF-07** | Form-factor agnostic read binding | RT-G12 FF-* |

### Open (non-blocking for Wave 1 definition and specification start)

| ID | Topic | Blocks specification? | Disposition |
|----|-------|----------------------|-------------|
| **DF-08** | Pilot workspace pointer policy | **No** | Resolve per pilot in specification |
| **DF-09** | Network/hosting beyond local git | **No** | LOW for MVP |
| **DF-10** | Git versioning policy for SoT | **No** | May inherit monorepo git |
| Serialization format | JSON vs YAML vs markdown | **No** | First specification deliverable |
| Internal folder layout | Per-project home structure | **No** | Specification era |
| OQ-ME05 exact bind ritual timing | Same session OK | **No** | Operator convention |
| OQ-TS01, OQ-M03, OQ-R05 PHASE_SLICE | Multi-slice policy | **No** | Engine v2 or case policy |

### Blocking assessment

**No unresolved owner decision blocks Wave 1 definition completion or transition to Physical Artifact Specification.**

Open items are **specification-era** or **per-pilot operational** choices — consistent with Implementation Standards Consolidation Review owner decision section.

**Operator acknowledgment** for era transition and **separate authorization** for physical file creation remain **normative governance discipline** — not unresolved DF blockers.

---

## Final Recommendation

### **A — Begin Physical Artifact Specification**

### Justification

1. **Wave 1 inventory complete:** All candidate classes from POC, MOC, ROC, SOC mapped with mandatory/optional/forbidden disposition.

2. **MVP alignment:** Mandatory set covers C2–C7 and enables S1–S9 on one Core 5 pilot; exclusions match MVP Definition and standards boundary protection.

3. **Sequence validated:** RT-G04 → RT-G10 → RT-G05 → RT-G12 creation order confirmed; Playbook lifecycle integrated as Phase F.

4. **Pilot viability confirmed:** Minimum bootstrap set (phases A–E + recommended Playbook 04 cycle) supports Playbooks 01–05.

5. **Standards sufficient:** Implementation Standards Consolidation Review already closed standards era; this review **instantiates** that verdict into concrete Wave 1 class inventory **without** contradicting it.

6. **No blocking owner decisions:** DF-01…07 resolved; DF-08…10 and serialization are **specification** topics, not definition gaps.

7. **Risks manageable:** HIGH implementation risks addressed by sequence and anti-pattern guards in specification phase.

### Not recommended

| Option | Why not |
|--------|---------|
| **B — More Definition Required** | Wave 1 class inventory, mandatory/optional/forbidden split, and sequence **fully derivable** from complete standards; additional definition risks **specification smuggling** without authorization |
| **C — Return To Standards** | No material contradictions found; standards standard-complete per Consolidation Review |

### Immediate next authorized actions (reference — not executed by this review)

1. **Begin Physical Artifact Specification** — serialization, layout, naming conventions per POC/MOC/ROC/SOC class separation.
2. **Preserve Wave 1 scope** — no forbidden artefact classes; no runtime/automation/dashboard scope.
3. **Physical creation** — **only** after specification **and** separate operator authorization for disk writes.
4. **Pilot sequencing** — Core 5 case; phases A→E before Playbook 03 demonstration.

---

## Explicit Non-Claims

This definition review:

- **is not** physical artefact creation, folder creation, manifest/registry/tracking record creation, schema, storage layout, or implementation execution plan;
- **does not** create anything under `workspaces/website-factory-operations/` or elsewhere in the repo;
- **does not** modify RT-G04, RT-G10, RT-G05, RT-G12 implementation standards or accepted doctrine;
- **does not** claim Website Factory **runtime**, workflow engine, automation layer, database, application, or operator dashboard **exist** in-repo;
- **does not** claim MVP **has been built**, Wave 1 artefacts **exist on disk**, or pilot **has been demonstrated**;
- **does not** claim Physical Artifact Specification **automatically** authorizes physical creation — **separate operator authorization** required;
- **does not** resolve serialization format, internal layout, DF-08, DF-09, DF-10 — assigns to **Physical Artifact Specification** era;
- **does not** replace Playbooks 01–05, MVP Definition, Operational Model, or Consolidation Review.

Human-operated declaration path (Playbook 04 DA-01, OA-ACT-04) remains the v1 normative model.

Wave 1 definition establishes **which physical artefact classes belong to the first wave** — **not** that they exist on disk.

---

*Website Factory Physical MVP Artifact Definition Review v1 — definition only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md`. Git: no commit, no push.*

---

# REPORT — Website Factory Physical MVP Artifact Definition Review v1

**Stage:** Physical MVP Artifact Era — Definition Review (Wave 1 inventory)  
**Deliverable:** `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md` (created)  
**Summary:** Определён MVP Wave 1 physical artefact set: mandatory POC-01…POC-10 (+ MOC/ROC/SOC mandatory classes), optional derived/draft classes, forbidden runtime/automation/dashboard/analytics artefacts, validated creation sequence RT-G04→RT-G10→RT-G05→RT-G12 + Playbooks 03↔04→05, Core 5 pilot viability, readiness and risk review — рекомендация **A Begin Physical Artifact Specification**; zone path verified absent; no blocking owner decisions.  
**Git:** no commit, no push (per task).
