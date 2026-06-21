# ATLAS Registry Architecture v1

**Status:** **documented** — Phase 4 Registry Architecture Foundation (normative).  
**Program:** ATLAS — **Business Reality Registry**  
**Classification:** Registry Layer · Cross-Cutting Infrastructure  
**Date:** 2026-06-04  
**Is not:** database, tables, APIs, runtime, storage engines, synchronization, automation, folder layout, MDM product, CRM, ERP.

**Foundation chain (Phase 4):** Phase 1–3 (approved) → **this document** → [ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md) → [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) → [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) → [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md)

**Phase 1–3 constraint:** No changes to approved Phase 1–3 documents unless contradictions are discovered. None identified at Phase 4 authoring.

---

## 1. Mission of the registry layer

| Phase | Question answered |
|-------|-------------------|
| Phase 1 | **What** exists in business reality? |
| Phase 2 | **How** do entities relate? |
| Phase 3 | **How** is each thing uniquely identified? |
| Phase 4 | **How** is ATLAS organized as a **registry system**? |

Phase 4 does not add new entity types. It defines **registry architecture semantics** — the contract future implementations must honor without prescribing technology.

**Normative mission statement:**

> Organize **canonical business reality** as a **human-supervised registry system** that downstream programs may **trust for identity and structure**, while **never** absorbing their operational workloads.

---

## 2. Registry philosophy

### 2.1 ATLAS owns business reality

ATLAS is the **canonical source of business reality** for the MARS ecosystem:

- organizations, people, projects, websites, domains exist **because ATLAS attests they exist** (when active canonical);
- structural relationships exist **because ATLAS attests the link**;
- identity is **because ATLAS assigns and governs** stable ids ([ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md)).

### 2.2 ATLAS does not own business operations

ATLAS does **not** perform or own:

- document generation, contracts, invoices, reports;
- SEO, PPC, analytics, campaigns, content production;
- CMS operations, deploy pipelines, task management;
- market acquisition (SERP packs remain MIG).

**Consumers perform work.** ATLAS supplies **referenceable structure**.

### 2.3 Registry as business system, not technical system

| Registry **is** (conceptual) | Registry **is not** (technical) |
|------------------------------|----------------------------------|
| A governed catalog of attested business facts | A microservice mesh |
| A trust model for “what exists” | A message bus |
| A contract for cross-program reference | An ORM schema |
| Slow-changing structural truth | Real-time operational dashboard |

Implementation may use files, databases, or APIs later — **architecture is independent of storage**.

### 2.4 Documentation-first Phase 4

Phase 4 delivers **principles, layers, boundaries, and governance hooks** only. No implementation claims unless future phases add evidenced code with explicit charter.

---

## 3. What the ATLAS registry is

The **ATLAS registry** is the **organized union** of:

1. **Entity registries** — conceptual partitions by entity class ([ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md));
2. **Relationship registry** — first-class structural edges ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md));
3. **Attestation layer** — how facts become canonical ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md));
4. **Consumer contract layer** — how programs may interact ([ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md));
5. **Change governance layer** — how the registry evolves ([ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md)).

Together these form the **Business Reality Registry** named ATLAS — not a single monolithic table, but a **coherent semantic system** with one canonical truth discipline.

---

## 4. What the ATLAS registry is not

| Not ATLAS registry | Belongs to |
|--------------------|------------|
| MARS program registry (`project_id` rows) | `registry/project-registry.md` |
| MIG market evidence store | MIG acquisition artifacts |
| CRM / ERP / accounting master | Consumer or finance systems |
| CMS content, orders, products | WPilot, OCPilot, storefront |
| Agent orchestration graph | MARS automation layers |
| Infrastructure host inventory | `governance/mars-infrastructure-reality-v1.md` |
| Business Scope classification store | Future metadata — not registry core |

See [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) for the full exclusion matrix.

---

## 5. Registry responsibilities

### 5.1 Core responsibilities (RA-*)

| ID | Responsibility |
|----|----------------|
| **RA-01** | Maintain **one canonical identity** per attested business subject per entity class |
| **RA-02** | Maintain **structural relationships** between entities — not operational workflows |
| **RA-03** | Expose **stable identifiers** for cross-consumer reference |
| **RA-04** | Record **attestation provenance** for canonical promotion (design principle) |
| **RA-05** | Support **explicit lifecycle states** (proposed, active, disputed, deprecated) — semantics in companion docs |
| **RA-06** | Enforce **SAFE UNKNOWN** when facts are not attested |
| **RA-07** | Govern **expansion** of entity types, fields, and relationship semantics ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)) |
| **RA-08** | Provide **consumer reference contract** — read canonical; no silent overwrite |

### 5.2 Non-responsibilities (explicit)

| ID | Non-responsibility |
|----|-------------------|
| **RA-N01** | Execute or schedule work in any consumer domain |
| **RA-N02** | Store high-churn operational metrics as canonical truth |
| **RA-N03** | Auto-merge duplicate candidates without human attestation |
| **RA-N04** | Become system of record for money, pipeline, or tasks |
| **RA-N05** | Replace consumer-local caches — consumers may cache; ATLAS is not the cache |

---

## 6. Registry layers

Conceptual stack (bottom = slowest, most durable):

```text
┌─────────────────────────────────────────────────────────────┐
│  L5 — Change Governance                                      │
│       expansion · amendments · version discipline            │
├─────────────────────────────────────────────────────────────┤
│  L4 — Consumer Contracts                                     │
│       read · reference · classify · suggest (not overwrite)│
├─────────────────────────────────────────────────────────────┤
│  L3 — Attestation & Trust                                    │
│       evidence · stewardship · review · SAFE UNKNOWN         │
├─────────────────────────────────────────────────────────────┤
│  L2 — Entity & Relationship Registries                       │
│       org · person · project · website · domain · edges      │
├─────────────────────────────────────────────────────────────┤
│  L1 — Identity & Aliases                                     │
│       stable ids · namespaces · aliases · merge/split rules  │
├─────────────────────────────────────────────────────────────┤
│  L0 — Reality & Taxonomy (Phase 1)                           │
│       what exists · boundaries · MVP entity set              │
└─────────────────────────────────────────────────────────────┘
```

**Rule RA-L01:** Upper layers may not contradict lower approved layers without explicit governance amendment.

**Rule RA-L02:** Consumers interact primarily at **L2–L4** (reference + propose); **L3** promotion is human-gated.

---

## 7. Registry boundaries

### 7.1 Internal boundary — registry vs identity

| Concern | Owner document |
|---------|----------------|
| **Whether** `ORG-00042` exists and is active | Entity registry + attestation |
| **What id format** and alias rules apply | [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md) |
| **Whether** two records merge | [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) |

Registry architecture **coordinates** identity governance; it does not replace Phase 3 rules.

### 7.2 External boundary — registry vs consumers

| Allowed | Forbidden |
|---------|-----------|
| Consumer reads `ORG-*`, `WEB-*`, relationship ids | Consumer writes canonical without attestation |
| Consumer stores foreign-key mapping to ATLAS id | Consumer maintains parallel canonical org list |
| Consumer proposes new entity (future) | Consumer auto-attests from import |

Full matrix: [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md).

### 7.3 Business Scope independence

**Business Scope** (e.g. `andrey`, `sergey`, `roman`) may classify activity for operators — it is **not** an entity, identity, or ownership construct ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §8.3).

**Rule RA-BS01:** Registry architecture **must not** require Business Scope for canonical records, routing, or attestation.

**Rule RA-BS02:** Future Business Scope metadata **must not** appear as registry partition keys (no “andrey-org-registry”).

---

## 8. Canonical source principles

### 8.1 What makes a registry record canonical?

A record is **canonical** when **all** hold:

| Criterion | Source |
|-----------|--------|
| **C-01** | Entity or relationship type is in **approved taxonomy** |
| **C-02** | Record is in **active** canonical lifecycle state (not merely proposed) |
| **C-03** | **Human attestation** promoted the record ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)) |
| **C-04** | **Stable identifier** assigned per Phase 3 rules |
| **C-05** | No unresolved **dispute** blocking canonical use |
| **C-06** | Claim does not violate [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) |

Until C-01–C-06 are satisfied, consumers must treat references as **proposed** or **SAFE UNKNOWN**.

### 8.2 Single source per structural claim

For each defined relationship kind between a fixed entity pair, **at most one active canonical** relationship ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-04, CR-07).

### 8.3 Canonical wins after reconciliation

When consumer cache disagrees with ATLAS:

1. If ATLAS is **active canonical** and attested → **ATLAS wins** for identity/structure.
2. If ATLAS is **unknown or disputed** → **SAFE UNKNOWN**; consumer must not invent ATLAS ids.
3. Reconciliation is **human-driven**, not batch auto-merge.

---

## 9. Consumer interaction principles

### 9.1 Permitted interactions

| Interaction | Meaning |
|-------------|---------|
| **Read** | Query canonical ids, names, relationships for work |
| **Reference** | Embed ATLAS ids in consumer artifacts (reports, sites, pilots) |
| **Classify** | Tag consumer-local objects with ATLAS ids (non-canonical metadata) |
| **Suggest** | Submit proposals for new entities, aliases, relationships |

### 9.2 Forbidden interactions

| Interaction | Why forbidden |
|-------------|---------------|
| **Silent overwrite** | Breaks canonical trust |
| **Auto-merge** | Duplicates require human merge ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md)) |
| **Auto-attest** | Machines/agents cannot promote to active alone (GV-01, IGV-01) |
| **Fork registries** | Parallel canonical org lists per tool |

### 9.3 Consumer-agnostic design

Architecture **must not** embed consumer-specific fields in canonical core (e.g. “MIG-only org flag”). Consumer-specific data lives in **consumer systems**, linked by **foreign reference** to ATLAS ids.

Known consumers (current): MIG, ORCA, Website Factory, WPilot, OCPilot, HomeGateway.  
Known consumers (future): Secretary, contract, document, reporting, administrative systems.

---

## 10. Required architectural analysis (Phase 4 decisions)

### 10.1 What makes a registry canonical?

**Decision RA-D01:** Canonical status is a **governance outcome** (attested + active + in-taxonomy), not a **technical default** (first insert wins).

### 10.2 Can consumers create reality?

**Decision RA-D02:** Consumers **cannot create canonical reality alone**. They may create **proposals** that enter non-canonical intake; stewards or owners **attest** promotion.

### 10.3 Can consumers propose reality?

**Decision RA-D03:** **Yes** — propose entities, aliases, relationships, and corrections. Proposals are **first-class non-canonical** inputs, never silent promotion.

### 10.4 Who owns attestation?

**Decision RA-D04:** **ATLAS governance roles** own attestation — program owner (final), registry steward (delegated day-to-day). Consumers and agents **do not** own attestation. Detail: [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md).

### 10.5 Who owns identity corrections?

**Decision RA-D05:** **Registry steward and program owner** per [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md). Consumers may **flag** duplicates or submit mapping proposals; they **cannot** approve merge/split or reassign canonical ids.

### 10.6 How should future imports behave?

**Decision RA-D06:** Imports produce **proposed** records + **evidence references** + optional **foreign-key mapping** — never bulk auto-canonicalization. Steward reviews against evidence tiers; conflicts → disputed or SAFE UNKNOWN.

### 10.7 How should secretary/document systems interact?

**Decision RA-D07:** Secretary, contract, and document systems are **consumers**: **read** org/person/project ids; **reference** them in generated artifacts; **suggest** corrections via proposal channel. Generated PDFs/contracts **remain external**; ATLAS holds **pointers**, not document bodies ([ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §3.2).

### 10.8 Can ATLAS ever become operational authority?

**Decision RA-D08:** **No.** ATLAS remains **reality authority only** — identity and structural graph. Operational authority (what to do, what to ship, what to invoice) stays in OPS and domain consumers. Expanding ATLAS into “the system that runs the business” is a **boundary defect** ([ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) AD-02–AD-04).

---

## 11. Anti-patterns

| Anti-pattern | Corrective principle |
|--------------|---------------------|
| “ATLAS database” as ERP | RA-D08 — reality only |
| Per-consumer canonical org | RA-08 — one graph |
| Placeholder ids to unblock export | CR-10 — SAFE UNKNOWN |
| Business Scope as org partition | RA-BS01 |
| SERP evidence in ATLAS core | E-10 — MIG territory |
| Relationship stores deal stage | E-14 — CRM territory |

---

## 12. Phase 4 deliverables and non-deliverables

| Delivered in Phase 4 | Explicitly not delivered |
|----------------------|---------------------------|
| Registry architecture (this doc) | Database schema |
| Entity registry model | API specification |
| Attestation model | Storage layout |
| Consumer contracts | Synchronization design |
| Change governance | Automation / runtime |

---

## 13. Open implications for next package

Unified **registry lifecycle** semantics across entity registries (intake → proposed → active → deprecated) are referenced here and in entity registry model but not fully specified as a cross-cutting lifecycle package. See Phase 4 closeout REPORT for recommended next package.

---

*ATLAS Registry Architecture v1 — Phase 4 Foundation. Documentation only; no runtime claims.*
