# REPORT — RT-G04 Physical Artifact Specification Review v1

**Версия:** v1  
**Дата:** 2026-06-06  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical Artifact Specification Era — **RT-G04 specification review only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE** (RT-G04, RT-G10, RT-G05, RT-G12); Physical MVP Artifact Definition **COMPLETE**; Physical Artifact Specification Era **AUTHORIZED**  
**Тип:** specification review only — **без** artifact creation, folder creation, file creation, serialization design, layout design, runtime design, implementation execution  
**Primary inputs:** [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md), [RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-CHARTER-v1.md), [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md), [WEBSITE-FACTORY-IMPLEMENTATION-STANDARDS-CONSOLIDATION-REVIEW-v1.md](WEBSITE-FACTORY-IMPLEMENTATION-STANDARDS-CONSOLIDATION-REVIEW-v1.md), [RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md](RT-G10-MANIFEST-IMPLEMENTATION-STANDARD-v1.md), [RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md](RT-G05-REGISTRY-IMPLEMENTATION-STANDARD-v1.md), [RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md](RT-G12-TRACKING-SURFACE-READ-BINDING-IMPLEMENTATION-STANDARD-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), Operational Playbooks 01–05

---

## Executive Summary

**Вердикт:** Концептуальная модель физических артефактов RT-G04 **достаточна** для авторизации отдельного deliverable **RT-G04 Physical Artifact Specification** — без создания артефактов на диске и без выбора serialization/layout в рамках этого review.

**RT-G04 physical artifact model** определяет **тринадцать normative classes** (POC-01…POC-10 + POC-D1/O1/O2) и **два infrastructure loci** (authorized zone + per-project record home) внутри `workspaces/website-factory-operations/`. Классы разделены по scope (portfolio vs project), authority (authoritative vs derived vs operational), и lifecycle trigger (Playbooks 01–05).

**Рекомендация:** **A — Authorize RT-G04 Physical Artifact Specification**

**Verified repo state:** `workspaces/website-factory-operations/` **не существует** on disk — ожидаемо; review **определяет модель**, не создаёт артефакты.

---

## Review Scope

### Что покрывает этот review

| Вопрос | Ответ в этом документе |
|--------|------------------------|
| Какие **physical artifact classes** существуют в RT-G04? | POC-01…POC-10 + optional POC-D1/O1/O2 + zone/home infrastructure |
| Как классы **связаны**? | Composition model, facet hosting, lifecycle triggers |
| Portfolio-scope vs project-scope | Явное разделение |
| Optional vs mandatory | По playbook trigger и MVP Wave 1 |
| Authoritative vs derived | Четыре persistence categories |
| Prohibited | Boundary protection + anti-patterns |

### Что **не** покрывает этот review (territory RT-G04 Physical Artifact Specification deliverable)

| Topic | Disposition |
|-------|-------------|
| Serialization format (JSON/YAML/markdown) | RT-G04 Physical Artifact Specification |
| Per-project home internal folder layout | RT-G04 Physical Artifact Specification |
| File naming conventions | RT-G04 Physical Artifact Specification |
| Field lists / schemas | RT-G04 Physical Artifact Specification |
| MOC-* / ROC-* / SOC-* serialization | RT-G10 / RT-G05 / RT-G12 Physical Artifact Specifications (separate tracks) |
| Physical file creation | Separate operator authorization post-specification |

**Principle REV-SCOPE-01:** Этот review **авторизует концептуальную модель** — не подменяет specification deliverable и **не** создаёт физические артефакты.

---

## Physical Artifact Classes

Normative **classes** — не file names, не schemas, не folder trees. Derived from [RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md](RT-G04-PERSISTENCE-SUBSTRATE-IMPLEMENTATION-STANDARD-v1.md) § Persistence Object Classes.

### Infrastructure loci (RT-G04 substrate containers)

| Locus ID | Locus name | Physical meaning | MVP disposition |
|----------|------------|------------------|-----------------|
| **LOC-ZONE** | **Authorized zone** | Bounded Factory SoT filesystem root at `workspaces/website-factory-operations/` (DF-03) | **Must exist** before any POC class materialization |
| **LOC-HOME** | **Per-project record home** | Exactly one discoverable physical locus per Factory Project identity (P1, POC-RULE-01) | **Must exist** per manifest-bound project |

### POC — Persistence Substrate record classes

| Class ID | Class name | Physical meaning | MVP disposition |
|----------|------------|------------------|-----------------|
| **POC-01** | **Identity** | Stable Factory Project identity shell bound to per-project physical locus | **Must persist** |
| **POC-02** | **Binding** | Manifest and registry binding **carriers** — hosts RT-G10/05 serialized content in separate facets | **Must persist** (when bound) |
| **POC-03** | **State** | Active state instance + declared state history | **Must persist** |
| **POC-04** | **Gate** | Gate outcome index — observed PASS/FAIL/BLOCKED outcomes, not criteria | **Must persist** |
| **POC-05** | **Handoff** | Handoff event index + package refs — events/refs, not payloads | **Must persist** |
| **POC-06** | **Declaration** | Append-only operator declaration records and reconciliation acts | **Must persist** |
| **POC-07** | **Ledger** | Progression ledger / audit trail linking declarations to index mutations | **Must persist** |
| **POC-08** | **Closure** | Factory-terminal / partial / suspended outcome metadata | **Must persist** (when Playbook 05 executed) |
| **POC-09** | **Reference** | External workspace, layer body, handoff payload, Runtime doc pointers | **Must persist** (refs only) |
| **POC-10** | **Audit** | Last declaration recency markers; session outcome refs for SRDY-07 | **Must persist** |
| **POC-D1** | **Derived cache** | Eligibility snapshots, SRDY pass/fail views, registry orientation summaries | **Optional** — regeneratable |
| **POC-O1** | **Operational note** | Pre-declaration Playbook 03 session notes | **Optional** — not authoritative |
| **POC-O2** | **Enrollment draft** | Pre-bind enrollment decision notes before RT-G10 physical bind | **Optional** — not authoritative |

### Class inventory summary

```text
  RT-G04 Physical Artifact Model (conceptual)
  ═══════════════════════════════════════════

  Infrastructure:
    LOC-ZONE  — authorized zone (portfolio root)
    LOC-HOME  — per-project record home (project root)

  Authoritative persistent classes:
    POC-01 Identity
    POC-02 Binding (manifest facet + registry facet)
    POC-03 State
    POC-04 Gate
    POC-05 Handoff
    POC-06 Declaration
    POC-07 Ledger
    POC-08 Closure (conditional)
    POC-09 Reference
    POC-10 Audit

  Optional / subordinate classes:
    POC-D1 Derived cache
    POC-O1 Operational note
    POC-O2 Enrollment draft
```

**Principle RTG04-CLASS-01:** RT-G04 Physical Artifact Specification **covers POC-* and infrastructure loci only** — MOC-*, ROC-*, SOC-* belong to downstream standard-specific specification tracks **within** POC-02 facets or read composition layer.

---

## Class Relationships

### Composition model (conceptual — not layout)

```text
  workspaces/website-factory-operations/          ← LOC-ZONE (portfolio root)
  │
  ├── portfolio scope
  │     └── POC-02 registry facet                 ← binding carrier; ROC-* content = RT-G05
  │
  └── per-project record home (LOC-HOME)          ← one per Factory Project
        ├── POC-01 identity
        ├── POC-02 manifest facet                 ← binding carrier; MOC-* content = RT-G10
        ├── POC-03 state instance + history
        ├── POC-04 gate outcome index
        ├── POC-05 handoff event index
        ├── POC-06 declaration records
        ├── POC-07 progression ledger
        ├── POC-08 closure metadata               ← on Playbook 05
        ├── POC-09 external ref index
        ├── POC-10 audit / recency markers
        ├── POC-D1 derived cache (optional)
        ├── POC-O1 session notes (optional)
        └── POC-O2 enrollment draft (optional)
```

### Relationship rules

| Rule ID | Relationship | Normative constraint |
|---------|--------------|-------------------|
| **REL-01** | LOC-ZONE **contains** all POC-* classes | AZ-01 — no scattered Factory SoT |
| **REL-02** | LOC-HOME **contains** POC-01…POC-10 for one project | POC-RULE-01 — exactly one home per identity |
| **REL-03** | POC-02 manifest facet **hosts** MOC-* (RT-G10) | Substrate hosts; RT-G10 serializes content |
| **REL-04** | POC-02 registry facet **hosts** ROC-* (RT-G05) | Portfolio scope; separate from manifest facet |
| **REL-05** | POC-02 facets **must remain separate record classes** | POC-RULE-02, MOC-RULE-02 — no mega-record |
| **REL-06** | POC-03…POC-05 **mutated by** Playbook 04 only | OWN-02, LC-04 |
| **REL-07** | POC-06/POC-07 **append-only**; POC-03…05 reflect last declaration | INT-01, INT-03 |
| **REL-08** | POC-09 **points to** external bodies — never embeds | RR-01…RR-04 |
| **REL-09** | POC-08 **references** POC-01 identity | INT-10 — no orphan closure |
| **REL-10** | POC-D1 **subordinate to** POC-03…POC-07 | INT-04, DR-02 |
| **REL-11** | RT-G12 **reads** POC-03…07, POC-10 — **never writes** | OWN-03, TRK-REL-01 |
| **REL-12** | ROC-05 (RT-G05) **points to** MOC-01 (RT-G10) via POC-02 facets | Cross-facet pointer; not RT-G04 content |

### Lifecycle dependency graph

```text
  PRE-FACTORY (no zone)
       │
       ▼
  LOC-ZONE created ───────────────────────────── portfolio infrastructure
       │
       ▼
  Playbook 01 enrolled → RT-G10 bind
       │
       ├──▶ LOC-HOME + POC-01 + POC-02(m) + POC-09
       │
       ▼
  Playbook 02 enrolled → RT-G05 bind (optional path)
       │
       └──▶ POC-02(r) at portfolio scope
       │
       ▼
  Playbook 04 declarations (repeat)
       │
       └──▶ POC-03…07, POC-06, POC-07, POC-10
       │
       ▼
  Playbook 05 closure
       │
       └──▶ POC-08
```

**Principle REL-13:** Class relationships are **normative at conceptual level** — physical co-location within LOC-HOME **permitted** (COL-01); class **separation on disk** **mandatory** regardless of serialization choice (COL-02…COL-04).

---

## Portfolio-Scope Artifacts

Artifacts whose **primary locus** is portfolio scope within LOC-ZONE.

| Artifact | Scope | RT-G04 role | Content owner |
|----------|-------|-------------|---------------|
| **LOC-ZONE** | Portfolio | RT-G04 — zone root infrastructure | RT-G04 specification |
| **POC-02 registry facet** | Portfolio | RT-G04 — binding **carrier** at portfolio scope | RT-G05 populates ROC-* **within** facet |

### Portfolio-scope rules

| Rule ID | Rule |
|---------|------|
| **PS-01** | Exactly **one** canonical portfolio catalog binding locus at MVP (ROC-01 via TOP-01) — hosted in POC-02 registry facet |
| **PS-02** | Portfolio scope **does not** contain per-project tracking indexes (POC-03…POC-07) |
| **PS-03** | Portfolio scope **does not** answer eight Surface questions — portfolio select only (G05-REL-03) |
| **PS-04** | LOC-ZONE **must not** expand to entire MARS monorepo (AZ-05) |
| **PS-05** | Registry facet **may exist without** any per-project homes — but MVP demo track requires both |

**Note:** Per [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md), single-project Factory path without catalog remains doctrinally valid — portfolio-scope POC-02 registry facet is **mandatory for MVP Wave 1 demo track (C4/S3)**, not for all Factory work.

---

## Project-Scope Artifacts

Artifacts whose **primary locus** is per-project within LOC-HOME.

| Artifact | Scope | RT-G04 role | Content owner |
|----------|-------|-------------|---------------|
| **LOC-HOME** | Project | RT-G04 — per-project container (P1) | RT-G04 specification |
| **POC-01** | Project | RT-G04 — identity shell | RT-G04 + stabilized at RT-G10 bind |
| **POC-02 manifest facet** | Project | RT-G04 — binding carrier | RT-G10 populates MOC-* **within** facet |
| **POC-03** | Project | RT-G04 — state index | Operator Playbook 04 |
| **POC-04** | Project | RT-G04 — gate index | Operator Playbook 04 |
| **POC-05** | Project | RT-G04 — handoff index | Operator Playbook 04 |
| **POC-06** | Project | RT-G04 — declaration records | Operator Playbook 04 |
| **POC-07** | Project | RT-G04 — progression ledger | Operator Playbook 04 |
| **POC-08** | Project | RT-G04 — closure metadata | Operator Playbook 05 |
| **POC-09** | Project | RT-G04 — external ref index | Operator all playbooks |
| **POC-10** | Project | RT-G04 — audit/recency | Operator Playbooks 03–04 |
| **POC-D1** | Project | RT-G04 — derived cache (optional) | Non-authoritative |
| **POC-O1** | Project | RT-G04 — session notes (optional) | Non-authoritative |
| **POC-O2** | Project | RT-G04 — enrollment draft (optional) | Non-authoritative |

### Project-scope rules

| Rule ID | Rule |
|---------|------|
| **PRJ-01** | Exactly **one** LOC-HOME per Factory Project identity — no competing homes |
| **PRJ-02** | All POC-01…POC-10 for a project **reside within** its LOC-HOME (co-location permitted) |
| **PRJ-03** | POC-02 manifest facet and POC-03…POC-07 **must remain distinct record classes** even when co-located |
| **PRJ-04** | Playbook 05 closure (POC-08) **binds to existing** LOC-HOME — no orphan records (LC-05) |
| **PRJ-05** | SOC-* read composition (RT-G12) **references** project-scope POC-* — SOC-* is **not** RT-G04 storage |

---

## Optional Artifacts

May exist in MVP Wave 1 **without blocking** RT-G04 substrate success.

| Class | Rationale | If omitted |
|-------|-----------|------------|
| **POC-D1** | Derived convenience only (DR-01…DR-04) | Playbook 03 / RT-G12 read POC-03…07 directly |
| **POC-O1** | Pre-declaration Playbook 03 session notes (OR-01) | Manual notes outside zone acceptable |
| **POC-O2** | Pre-bind enrollment draft (OQ-ME05 support) | Playbook 01 attestation sufficient |
| **POC-08** (pre-closure) | Only required when Playbook 05 executes | Valid during active pilot track |
| **POC-02 registry facet** (doctrinal) | Single-project path without catalog (M-H03) | Valid; **not** valid for MVP Wave 1 C4/S3 demo |

**Principle OPT-01:** Optional classes **must not** be promoted to authoritative status by convention drift — POC-O1/O2 **never** substitute for POC-06 (LC-03, OR-02).

---

## Authoritative Artifacts

Structured filesystem records whose loss **breaks** Playbooks 03/04/05 or eight Surface questions without workspace archaeology (PS-01 charter rule).

### Authoritative inventory by persistence category

| Category | Classes | Authority rule |
|----------|---------|----------------|
| **Persistent authoritative** | POC-01…POC-10 | Must survive between sessions (PR-01…PR-04) |
| **Persistent authoritative (conditional)** | POC-08 | Authoritative **when** Playbook 05 executed |
| **Persistent authoritative (trigger-bound)** | POC-02 facets | Authoritative **when** RT-G10/05 bind acts occurred |

### Authority matrix

| Class | Authoritative for | Not authoritative for | Write authority |
|-------|-------------------|----------------------|-----------------|
| **POC-01** | Factory Project identity binding to locus | Manifest categories; tracking state | Playbook 01 bind + RT-G10 |
| **POC-02 (manifest facet)** | Manifest binding **carrier existence** | MOC-* content authority → RT-G10 | RT-G10 bind act |
| **POC-02 (registry facet)** | Catalog binding **carrier existence** | ROC-* content authority → RT-G05 | RT-G05 bind act |
| **POC-03** | Active state + declared history | Gate criteria; manifest scope tier | Playbook 04 only |
| **POC-04** | Gate **outcomes** observed | Gate **criteria** definitions | Playbook 04 only |
| **POC-05** | Handoff **events/refs** | Handoff **payloads** | Playbook 04 only |
| **POC-06** | Declaration truth trail | — | Playbook 04 only |
| **POC-07** | Progression audit trail | — | Playbook 04 only |
| **POC-08** | Terminal closure outcome | Manifest enrollment revocation | Playbook 05 only |
| **POC-09** | External **locators** | External **bodies** | Operator maintains refs |
| **POC-10** | Recency markers for SRDY-07 | Session notes authority | Playbooks 03–04 |

### Authoritative precedence (conflict resolution)

| Precedence rule | Source |
|-----------------|--------|
| POC-06/POC-03 tail **wins over** POC-D1 | DR-02, INT-04, TV-02 |
| POC-06/POC-07 **append-only** — corrections = new events | INT-01, P7 |
| Last Playbook 04 act **wins** for POC-03…05 active view | INT-03 |
| POC-09 pointers **identify** external locus — broken refs visible, no silent copy | INT-05 |
| Manifest facet **must not** embed live gate index as second authoritative store | INT-06, MT-01 |

---

## Derived Artifacts

Structured records **permitted** on substrate for operator convenience; **must be regeneratable** from persistent authoritative records.

| Class | Derived content examples | Regeneration source |
|-------|-------------------------|---------------------|
| **POC-D1** | Eligibility snapshot; blocking/completion picture; active lifecycle segment label; composite gate rollup; SRDY-* derived views | POC-03…POC-07 + Runtime vocabulary |

### Derived rules

| Rule ID | Rule |
|---------|------|
| **DER-01** | POC-D1 **must be labeled** as derived — not declarer authority (DR-01) |
| **DER-02** | Derived **may be omitted** at MVP; Playbook 03 operable via direct index read (DR-04) |
| **DER-03** | RT-G12 **may read** POC-D1 or reconstruct — substrate **must not require** duplicate live index in manifest (DR-03, MAP-05) |
| **DER-04** | Derived material **must not** override POC-06/POC-03 when in conflict (INT-04) |

**Principle DER-05:** RT-G04 Physical Artifact Specification **may define** POC-D1 physical shape — but POC-D1 **remains optional** and **non-authoritative** regardless of format choice.

---

## Prohibited Artifacts

Must **not** exist as RT-G04 physical artifact classes — violation of MVP, standards, or boundary rules.

### Prohibited storage content in authorized zone

| Prohibited content | Actual owner | Guard |
|--------------------|--------------|-------|
| Layer artefact bodies (Legal Pack, blueprints, HTML, src) | T1 / external workspaces | RR-02, MAP-11 |
| Gate/handoff **criteria** definitions | Runtime Architecture | MAP-10 |
| Handoff package payloads | Generation Outputs | MAP-11 |
| Site Type Registry entries | Foundation `registry/` | RAP-11 |
| Engine doctrine copies | `website-factory-reference-v1/` | AZ-02 |
| Runtime vocabulary canon | Runtime Architecture v1 docs | Charter boundary |
| Automated transition logs as authority | RT-G07 (post-MVP) | BP forbidden storage |
| Agent chat, CI logs, MIG transcripts as SoT | External | RAP-18 |
| Deploy/hosting state | Post-Factory | Charter boundary |

### Prohibited system roles (no physical artifact class)

| Prohibited role | Guard |
|-----------------|-------|
| Database / multi-tenant storage product | DF-02, TX-06 |
| Workflow engine / state machine executor | RT-G01 |
| Factory runtime product | RT-G09, SC-01 |
| Automation layer mutating indexes | RT-G03, SC-03, INT-08 |
| Operator UI / dashboard / SaaS | TX-07, FF-02 |
| Validator / gate authority engine | RT-G11 |
| Discovery crawler (auto-enrollment) | RAP-10, RD-04 |
| Unified Passport / second YAML SoT | BV-05, MA-03 |

### Prohibited anti-patterns (RT-G04 specific)

| Anti-pattern | Prevention |
|--------------|------------|
| Single «project.yaml» swallowing manifest + full tracking | POC-RULE-02, MT-01 |
| POC-02 registry facet embedding full tracking depth | RA-05, INT-07 |
| Substrate docs inside `website-factory-reference-v1/` mixed with Engine | AZ-02 |
| Entire MARS repo as Factory zone | DF-03 bounded zone |
| Structured files inviting CI auto-write | INT-08, SC-03 |
| Physical bind before doctrinal enrollment | INT-M01, LC-06 |
| POC-O1/O2 treated as declaration authority | OR-02, LC-03 |

**Principle PROH-01:** If an RT-G04 artifact **executes**, **mutates indexes without Playbook 04**, **embeds external bodies**, or **collapses plane separation** — it is **prohibited**.

---

## Cross-Standard Boundary Review

RT-G04 Physical Artifact Specification **must preserve** handoff assumptions to RT-G10/05/12.

| Boundary | RT-G04 owns | RT-G10/05/12 own |
|----------|-------------|------------------|
| Zone + homes | LOC-ZONE, LOC-HOME topology | — |
| POC class taxonomy | POC-01…POC-10 definition | — |
| POC-02 manifest facet | Carrier existence + hosting rules | MOC-* serialization (RT-G10 spec) |
| POC-02 registry facet | Carrier existence + hosting rules | ROC-* serialization (RT-G05 spec) |
| Tracking indexes | POC-03…07, POC-10 physical locus | — |
| Surface read | — | SOC-* composition (RT-G12 spec) |
| Serialization format | POC-* substrate records | MOC/ROC/SOC within facets |

### Handoff validation (H-01…H-10)

| Assumption | Specification review verdict |
|------------|------------------------------|
| H-01 Zone exists before bind | **Compatible** — LOC-ZONE is first infrastructure artifact |
| H-02 One LOC-HOME per project | **Compatible** — PRJ-01 |
| H-03 POC-02 hosts manifest facet | **Compatible** — REL-03 |
| H-04 Manifest without registry valid | **Compatible** — optional registry facet |
| H-05 Doctrinal enrollment precedes bind | **Compatible** — LC-01, LC-06 |
| H-06 POC-09 may point to POC-03…05 | **Compatible** — REL-08 |
| H-07 No duplicate live gate index in manifest | **Compatible** — INT-06, REL-05 |
| H-08 Playbook 04 owns index mutations | **Compatible** — REL-06 |
| H-09 POC-08 primary owner Playbook 05 | **Compatible** — PRJ-04 |
| H-10 Append-only honesty | **Compatible** — DER/precedence rules |

**Boundary verdict:** No material contradiction between RT-G04 conceptual model and RT-G10/05/12 implementation standards.

---

## Readiness Review

### Is RT-G04 conceptual model sufficient for specification?

| Question | Answer |
|----------|--------|
| All POC classes defined? | **Yes** — POC-01…POC-10 + optional POC-D1/O1/O2 |
| Infrastructure loci defined? | **Yes** — LOC-ZONE + LOC-HOME |
| Scope split clear? | **Yes** — portfolio (zone + registry facet) vs project (home + POC-01…10) |
| Authority/derived split clear? | **Yes** — four persistence categories formalized |
| Relationships defined? | **Yes** — REL-01…13 + lifecycle graph |
| Prohibited set defined? | **Yes** — inherited from implementation standard boundary protection |
| Aligns with Physical MVP Definition Review? | **Yes** — POC inventory matches Wave 1 |
| Aligns with Implementation Standards Consolidation? | **Yes** — no contradictions |
| Blocks specification deliverable? | **No** — open serialization/layout topics **are** specification content |

### What RT-G04 Physical Artifact Specification will resolve (next deliverable)

| Topic | In scope for specification |
|-------|---------------------------|
| LOC-ZONE internal topology conventions | **Yes** |
| LOC-HOME discoverability and naming | **Yes** |
| POC class → physical locus mapping rules | **Yes** |
| Serialization format for POC-* substrate records | **Yes** |
| Co-location policy implementation (COL-01…04) | **Yes** — class separation preserved |
| DF-10 git policy for SoT records | **May reference** — operator workshop |
| DF-08 pilot workspace pointer policy | **May reference** — per-case in POC-09 |
| MOC-* / ROC-* / SOC-* format | **No** — separate standard-specific specifications |

### Readiness verdict

**RT-G04 conceptual artifact model is complete and sufficient** to authorize **RT-G04 Physical Artifact Specification** as the next deliverable. **Physical creation** remains subject to **separate operator authorization** post-specification.

---

## Risk Review

| Risk | Severity | Mitigation |
|------|----------|------------|
| Specification smuggles MOC/ROC serialization into RT-G04 spec | **MEDIUM** | REV-SCOPE-01; explicit boundary table |
| Mega-record anti-pattern in first physical files | **HIGH** | POC-RULE-02 enforced in specification |
| Zone creation without operator authorization | **HIGH** | Governance gate preserved from Wave 1 sequence |
| POC-D1 promoted to authoritative by naming | **LOW** | DER-01 labeling requirement in specification |
| Layout choice locks wrong co-location | **MEDIUM** | COL-02 class separation normative regardless of format |
| Triumph / external workspace refs ambiguous | **LOW** | DF-08 per-case; POC-09 pointer discipline in spec |
| False «substrate built» narrative | **HIGH** | Explicit Non-Claims; zone verified absent |

**Interpretation:** HIGH risks are **preventable** via specification discipline — **not** indicators that conceptual model is incomplete.

---

## Owner Decision Review

### Resolved (inherited — no re-decision required)

| ID | Decision | Source |
|----|----------|--------|
| **DF-01** | MARS monorepo | Topology + RT-G04 standard |
| **DF-02** | Filesystem + structured artifacts | TOPOLOGY-B-v1 |
| **DF-03** | Factory zone = `workspaces/website-factory-operations/` | RT-G04 AZ-* |
| **DF-06** | No HomeGateway | Topology |

### Open (non-blocking — specification deliverable topics)

| ID | Topic | Blocks RT-G04 spec authorization? |
|----|-------|-------------------------------------|
| Serialization format | JSON vs YAML vs markdown | **No** |
| Internal folder layout | Per-project home structure | **No** |
| **DF-08** | Pilot workspace pointer policy | **No** — per-case in POC-09 |
| **DF-09** | Network/hosting beyond local git | **No** |
| **DF-10** | Git versioning policy for SoT | **No** |
| OQ-ME05 | Exact bind ritual timing | **No** — operator convention |

**Blocking assessment:** **No unresolved owner decision blocks** RT-G04 Physical Artifact Specification authorization.

---

## Final Recommendation

### **A — Authorize RT-G04 Physical Artifact Specification**

### Justification

1. **Class model complete:** Thirteen POC classes + two infrastructure loci fully defined with physical meaning, MVP disposition, and scope assignment.

2. **Relationships explicit:** Composition model, facet hosting, lifecycle triggers, and cross-standard boundaries (H-01…H-10) validated — no material contradictions with RT-G10/05/12.

3. **Scope split clear:** Portfolio-scope (LOC-ZONE, POC-02 registry facet carrier) vs project-scope (LOC-HOME, POC-01…10) unambiguous.

4. **Authority model formalized:** Authoritative (POC-01…10), derived (POC-D1), operational/non-authoritative (POC-O1/O2), and reference-only (POC-09 bodies) distinguished with precedence rules.

5. **Prohibited set inherited:** Boundary protection and anti-patterns from implementation standard apply without gap.

6. **Upstream alignment:** Physical MVP Artifact Definition Review authorized specification era; RT-G04 POC inventory matches Wave 1; Implementation Standards Consolidation closed standards era.

7. **Open topics are specification content:** Serialization, layout, naming — **purpose** of the specification deliverable, not blockers to authorizing it.

8. **Risks manageable:** HIGH risks addressed by class separation guards and governance gates in specification phase.

### Not recommended

| Option | Why not |
|--------|---------|
| **B — More Definition Required** | Conceptual model **fully derivable** from complete RT-G04 implementation standard and Wave 1 definition; additional definition risks **specification smuggling** without authorization |
| **C — Return To Standards** | No material contradictions found; RT-G04 implementation standard standard-complete per Consolidation Review |

### Immediate next authorized actions (reference — not executed by this review)

1. **Author RT-G04 Physical Artifact Specification** — zone topology, LOC-HOME conventions, POC class-to-locus mapping, serialization format for POC-* records, naming — **preserving POC-RULE-02 class separation**.
2. **Preserve scope boundary** — MOC/ROC/SOC serialization deferred to RT-G10/05/12 specification tracks.
3. **Physical creation** — **only** after specification **and** separate operator authorization for disk writes.
4. **Sequence discipline** — LOC-ZONE → LOC-HOME → POC-02 facets (RT-G10/05) → POC-03…07 scaffold → pilot population.

---

## Explicit Non-Claims

This specification review:

- **is not** physical artefact creation, folder creation, file creation, serialization design, layout design, schema design, or implementation execution;
- **does not** create anything under `workspaces/website-factory-operations/` or elsewhere in the repo;
- **does not** modify RT-G04 Implementation Standard, RT-G04 Charter, or accepted doctrine;
- **does not** define JSON/YAML/markdown format, folder trees, file naming, or field lists — assigns to **RT-G04 Physical Artifact Specification** deliverable;
- **does not** claim Website Factory **runtime**, workflow engine, automation layer, database, application, or operator dashboard **exist** in-repo;
- **does not** claim MVP **has been built**, substrate artefacts **exist on disk**, or pilot **has been demonstrated**;
- **does not** claim RT-G04 Physical Artifact Specification **automatically** authorizes physical creation — **separate operator authorization** required;
- **does not** replace Playbooks 01–05, Physical MVP Artifact Definition Review, or Implementation Standards Consolidation Review.

Human-operated declaration path (Playbook 04 DA-01, OA-ACT-04) remains the v1 normative model.

This review establishes **how authorized RT-G04 physical artifacts are organized conceptually** — **not** that they exist on disk.

---

*RT-G04 Physical Artifact Specification Review v1 — specification review only. Canonical location: `workspaces/website-factory-reference-v1/RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-REVIEW-v1.md`. Git: no commit, no push.*

---

# REPORT — RT-G04 Physical Artifact Specification Review v1

**Stage:** Physical Artifact Specification Era — RT-G04 Specification Review  
**Deliverable:** `workspaces/website-factory-reference-v1/RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-REVIEW-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-REVIEW-v1.md` (created)  
**Summary:** Определена концептуальная модель физических артефактов RT-G04: infrastructure loci (LOC-ZONE, LOC-HOME), thirteen POC classes с scope/authority/optional split, relationship rules REL-01…13, portfolio vs project scope, authoritative/derived/prohibited inventory, cross-standard boundary validation H-01…H-10, readiness и risk review — рекомендация **A Authorize RT-G04 Physical Artifact Specification**; zone path verified absent; no blocking owner decisions; no physical artefacts created.  
**Git:** no commit, no push (per task).
