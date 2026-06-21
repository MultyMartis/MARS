# ATLAS Population Strategy v1

**Status:** **documented** — Phase 7 Registry Population Strategy (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-CONSUMER-ADOPTION-MODEL-v1.md](ATLAS-CONSUMER-ADOPTION-MODEL-v1.md)  
**Companion:** [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md) · [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) · [ATLAS-POPULATION-ROADMAP-v1.md](ATLAS-POPULATION-ROADMAP-v1.md)  
**Is not:** import tooling, sync jobs, migration runbooks, database design, APIs, storage layout, implementation schedule, code.

**Phase 1–6 constraint:** No changes to approved Phase 1–6 foundation documents unless contradictions are discovered. None identified at Phase 7 authoring.

**Business Scope constraint:** Population strategy does **not** depend on Business Scope Foundation, `andrey` / `sergey` / `roman` labels, or scope-partitioned registries ([ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md) §9).

---

## 1. Purpose

Semantic architecture (Phases 1–6) answers **what** business reality is, **how** it is identified, attested, lifecycle-managed, and consumed.

Phase 7 answers the next question:

> **How does canonical reality enter ATLAS** — in what order, under what evidence and attestation discipline, and with what controls so the registry grows without pollution?

This document defines **population philosophy, goals, principles, risks, and ownership**. Companion documents define **waves**, **evidence**, **governance**, and **roadmap**.

---

## 2. What population means

**Population** is the **governed, human-supervised process** of introducing **proposed** and **active canonical** records into ATLAS entity and relationship registries — each promotion backed by **evidence**, **review**, and **attestation** per [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md).

Population includes:

| Included | Description |
|----------|-------------|
| **Intake** | Observation → proposal (non-canonical) |
| **Prioritization** | Which entity classes and records enter first ([ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md)) |
| **Evidence discipline** | Minimum tiers per class ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md)) |
| **Attestation** | Human promotion to **active** canonical |
| **Uncertainty handling** | **SAFE UNKNOWN**, **proposed**, **disputed** — never silent invention |
| **Growth control** | Duplicate, identity, and relationship collision prevention ([ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md)) |
| **Maturity progression** | Staged readiness for consumers ([ATLAS-POPULATION-ROADMAP-v1.md](ATLAS-POPULATION-ROADMAP-v1.md)) |

Population is **strategic and operational-governance** language. It describes **what humans and stewards do** to build the graph — not **how software stores or moves data**.

---

## 3. What population does not mean

| Not population | Belongs to (future or other domain) |
|----------------|-------------------------------------|
| **Bulk technical load** without per-record attestation trail | Import tooling (out of scope) |
| **Continuous mirror** of CRM/CMS/ERP | Synchronization architecture (out of scope) |
| **One-time cutover** from legacy MDM | Migration program (out of scope) |
| **Automated canonical promotion** from agents or scripts | Prohibited by AT-IMP-01, IGV-01, GV-01 |
| **Market acquisition** (SERP packs, rankings) | MIG evidence — proposal support only (AT-E-03) |
| **Consumer-local caches** | Consumer systems |
| **MARS program registry rows** | `registry/project-registry.md` |

---

## 4. Population vs Import vs Synchronization vs Migration

### 4.1 Comparison matrix

| Dimension | **Population** | **Import** | **Synchronization** | **Migration** |
|-----------|----------------|------------|---------------------|---------------|
| **Intent** | Build **trusted canonical** business graph | Load **candidate facts** at scale | Keep **consumer copy** aligned with ATLAS | Move **legacy SoT** into ATLAS discipline |
| **Canonical outcome** | **Active** only after human attestation | Default **proposed** + mapping table | ATLAS remains SoT; consumer **reads** | Cutover + reconcile disputes |
| **Human role** | **Central** — review, attest, reject, defer | **Batch triage** — spot checks, not blind promote | **Reconcile** on drift flags | **Program** — mapping, parity, rollback plan |
| **Evidence** | Tiered E0–E3 per claim | Often E3 corroboration only | Not evidence for new facts | Historical exports as E1–E3 |
| **Risk** | Wrong graph structure | Duplicate explosion | Silent overwrite of canonical | False “done” without attestation |
| **Phase 7** | **Defined here** | Referenced as **input** only | **Explicitly excluded** | **Explicitly excluded** |

### 4.2 Normative boundaries

**POP-B-01 — Population is not import.**  
Import may **feed proposals** ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §9). Import **never** equals population complete.

**POP-B-02 — Population is not sync.**  
Consumers may cache; syncing caches does **not** populate ATLAS ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) RA-N05).

**POP-B-03 — Population is not migration.**  
Migration is a **project** with parity checks and rollback. Population is **ongoing discipline** after initial anchor set exists.

**POP-B-04 — Prefer population discipline on day one.**  
Even “initial load” follows **proposal → review → attest** — not “flip switch to active.”

---

## 5. Population philosophy

### 5.1 Anchor before attach

Populate **stable identity nodes** (especially **Organization**, then **Person**) before **edges** and **dependent web identities**. A graph of relationships without endpoints is **ambiguous structure**, not business reality.

### 5.2 Quality over throughput

Aligned with stewardship principles ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §5.2): **fewer canonical records with clear evidence** beat a large polluted registry.

### 5.3 Prefer SAFE UNKNOWN over invention

When org for a website is unclear, **do not** mint `org-unknown-*` ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-10, IGV-D02). Hold **proposed** website, declare **SAFE UNKNOWN** for org slot, or defer.

### 5.4 One graph, generic rules

Strategy applies to **any** operator ecosystem — not only Polygon / MetaCode / i-SEO. Illustrative names in taxonomy docs are **examples**, not population shortcuts.

### 5.5 Consumers propose; humans attest

Population accepts **consumer and agent proposals** ([ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md)) but **canonical active** remains steward/owner attested.

### 5.6 Growth without pollution

Every wave has **stop conditions** ([ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) §8). Expansion of types/fields remains [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) — separate from entity population.

---

## 6. Population goals

| Goal ID | Goal | Success signal (conceptual) |
|---------|------|-----------------------------|
| **PG-01** | **Anchor operator reality** | Core orgs and people **active** with attest trail |
| **PG-02** | **Enable cross-consumer reference** | Stable ids for org/site/project used in handoffs |
| **PG-03** | **Minimize ambiguous canonical** | No active record with unresolved endpoint disputes |
| **PG-04** | **Preserve auditability** | Proposed → active transitions explainable |
| **PG-05** | **Contain duplicate risk** | D1–D5 workflows engaged before second active canonical |
| **PG-06** | **Explicit gaps** | UNKNOWN declared where evidence insufficient |
| **PG-07** | **Consumer-safe maturity** | Certification levels ([ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md)) matched to graph completeness |

---

## 7. Population principles

| ID | Principle |
|----|-----------|
| **POP-P-01** | **Wave order is normative** — see [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md) |
| **POP-P-02** | **Evidence before active** — minimum tiers in [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md) |
| **POP-P-03** | **Endpoints before canonical edges** — active Relationship requires canonical or explicitly scoped proposed endpoints ([ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) EIR-R02) |
| **POP-P-04** | **No auto-org from website** — website intake does not invent Organization |
| **POP-P-05** | **Relationships late for bulk, early for participation slice** — PERSON↔ORG after Wave 1–2; full graph after web entities |
| **POP-P-06** | **Disputed blocks dependency** — no new irreversible canonical dependencies on **disputed** nodes |
| **POP-P-07** | **Import is triage, not truth** — E3 + human review |
| **POP-P-08** | **Business Scope never partitions population** — scope tags are future consumer metadata only |
| **POP-P-09** | **Stop rather than pollute** — governance halt triggers honored |
| **POP-P-10** | **Documentation-first** — population proceeds in governed docs/evidence refs before any runtime |

---

## 8. Population risks

| Risk ID | Risk | Mitigation (strategy-level) |
|---------|------|-----------------------------|
| **PR-01** | **Duplicate org/person explosion** from imports | Wave 1–2 slow attest; duplicate workflow D1–D5 |
| **PR-02** | **Placeholder canonical** (`org-unknown-*`) | POP-P-03; CR-10; reject |
| **PR-03** | **Relationship-before-endpoint** active edges | Wave 6; EIR-R02; remain **proposed** only |
| **PR-04** | **Website without org** asserted as complete | Proposed website + UNKNOWN org; no OWNS/BELONGS_TO active |
| **PR-05** | **CRM/ERP object bleed** | Boundaries review per intake ([ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md)) |
| **PR-06** | **SERP/MIG conflation** | Market evidence → proposal only (AT-E-03) |
| **PR-07** | **Mass agent proposals** without steward capacity | Defer queue; stop conditions |
| **PR-08** | **Consumer pressure for “just give me an id”** | C0 read-only until maturity stage allows reference |
| **PR-09** | **Homonym persons/orgs** | Identity governance before merge; separate ids |
| **PR-10** | **Premature certification** | Roadmap gates C1+ on graph completeness |

---

## 9. Population ownership

| Role | Population accountability |
|------|---------------------------|
| **ATLAS program owner** | Approves population strategy versions; resolves escalated disputes; split/merge final authority |
| **Registry steward** | Executes waves; intake triage; evidence tier assignment; day-to-day attest (delegated) |
| **Consumer operators** | Propose via future channels; **no** canonical attest |
| **Agents** | Proposal only; never population owner |

**POP-O-01:** Population **quality** is stewarded accountability — not “every consumer owns their slice of truth.”

**POP-O-02:** Phase 7 defines **strategy**. Steward roster, intake SLA, and escalation paths defer to **ATLAS Operational Model** (recommended next package).

---

## 10. Required architectural analysis (summary)

Full rationale in [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md) and companions.

| # | Question | Decision |
|---|----------|----------|
| 1 | What first? | **Organizations** (Wave 1) |
| 2 | Relationships early or late? | **Late for bulk** (Wave 6); **early slice** PERSON↔ORG after Person (Wave 2B) |
| 3 | Projects before websites? | **Yes** (Wave 3 before 4) |
| 4 | Website before organization? | **Proposed** website allowed; **active** structural links require org or UNKNOWN |
| 5 | Relationship before both endpoints canonical? | **Proposed** yes; **active canonical** no |
| 6 | First-wave evidence threshold? | **E0–E1** operator-known; **E1+** external/client |
| 7 | Disputed reality? | **proposed** / **disputed** — never **active** until resolved |
| 8 | Never bulk-auto? | **Active** promotion, merges, OWNER/OWNS, import-only relationships, placeholders |

---

## 11. Non-deliverables (Phase 7)

No import scripts, sync protocol, migration plan, schema, API, storage, or runtime services.

---

*ATLAS Population Strategy v1 — Phase 7 Foundation. Documentation only.*
