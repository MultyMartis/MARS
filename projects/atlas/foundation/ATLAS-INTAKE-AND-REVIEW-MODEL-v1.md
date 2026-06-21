# ATLAS Intake and Review Model v1

**Status:** **documented** — Phase 8 operational flow for reality entry and review (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md)  
**Is not:** workflow automation, ticket system, API design, queue software, SLA timers.

**Phase 1–7 constraint:** Consolidates review types in AT §6 and population gates without changing attestation semantics.

---

## 1. Purpose

Define **how new business reality enters review** and **how human review produces outcomes** — proposal intake, review queue, defer, reject, challenge, dispute, and attestation.

**Human process only.** No automation requirements. Any future tooling must implement this model — not replace it.

---

## 2. Operational flow overview

```text
┌──────────────┐
│  PROPOSAL    │  Consumer · Steward · Agent · Import
│  SOURCES     │
└──────┬───────┘
       ▼
┌──────────────┐
│  INTAKE      │  Class · boundary · minimum metadata
└──────┬───────┘
       ▼
┌──────────────┐
│  REVIEW      │  Queue · prioritization · review types
│  QUEUE       │
└──────┬───────┘
       │
       ├────► ATTEST ──► active (canonical)
       ├────► DEFER ───► proposed (held)
       ├────► REJECT ──► no canonical / logged rationale
       ├────► DISPUTED ► blocked dependencies
       └────► SAFE UNKNOWN ► explicit gap
```

---

## 3. Proposal intake

### 3.1 What is a proposal

A **proposal** is a **non-canonical claim** that a fact belongs in ATLAS — entity instance, relationship instance, alias, or lifecycle transition requiring attestation.

Proposals enter **proposed** state (or intake queue before record creation). They are **not** canonical until attested ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §2.1).

### 3.2 Intake sources

| Source | Typical proposal | Initial state |
|--------|------------------|---------------|
| **Registry Steward** | New org, site, edge from known context | proposed |
| **Consumer operator** | Mapping suggestion, missing entity flag | proposed |
| **Agent / import** | Bulk rows from consumer export | proposed + E3 evidence |
| **Program Owner** | Strategic seed for population wave | proposed or direct attest path |
| **Dispute resolution** | Corrected claim after challenge | proposed → review |

### 3.3 Minimum intake package (conceptual)

Every proposal should carry:

| Field (conceptual) | Required |
|--------------------|----------|
| Target class or relationship type | Yes |
| Claim summary | Yes |
| Proposer role | Yes |
| Evidence tier + ref | Yes (may be E0 for steward-known facts) |
| Wave / prerequisite note | If population active |
| Consumer foreign key (if any) | When consumer-originated |

**INT-01:** Intake missing class or boundary smell → **reject at intake** or return to proposer.

**INT-02:** Import proposals **always** require steward batch review (AT-IMP-01).

### 3.4 Intake outcomes (pre-queue)

| Outcome | Meaning |
|---------|---------|
| **Accepted to queue** | Valid proposal — enters review queue |
| **Returned** | Missing metadata — proposer fixes |
| **Rejected at intake** | Boundary violation (CRM field, task object, etc.) |

---

## 4. Review queue

### 4.1 Queue nature

The **review queue** is a **human-managed ordered list** of proposals awaiting review. It is **not** a ticket system — it may be implemented as spreadsheet, doc list, or future UI.

### 4.2 Prioritization (operational guidance)

| Priority | Proposal type | Rationale |
|----------|---------------|-----------|
| **P0 — Blocker** | D1 duplicate; disputed OWNER; STOP trigger | Halt harm |
| **P1 — Dependency** | Endpoint needed for wave progression | Population order |
| **P2 — Consumer blocker** | Certified consumer cannot proceed (UNKNOWN gap) | Adoption |
| **P3 — Routine** | Standard intake | Normal flow |
| **P4 — Bulk import** | Agent batch | Spot-check discipline |

**RQ-01:** P0 **preempts** all other review.

**RQ-02:** Wave order ([ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md)) informs P1 — not automatic rejection of out-of-wave proposals (POP-PROP-01).

### 4.3 Review types

From [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §6.1 — operational playbook:

| Review type | Trigger | Primary reviewer |
|-------------|---------|------------------|
| **Intake review** | New proposal accepted | Steward |
| **Evidence review** | Tier challenge, insufficient proof | Steward |
| **Duplicate review** | D1–D5 identity signals | Steward |
| **Boundary review** | CRM/finance/PM smell | Steward → Owner |
| **Dispute review** | Conflicting claims | Steward → Owner |
| **Expansion review** | New type/field/class | Owner |

### 4.4 Review completion

Each completed review records (conceptually): **reviewer role**, **review type**, **outcome**, **rationale**, **timestamp**.

---

## 5. Defer

### 5.1 Meaning

**Defer** keeps the proposal in **proposed** (or held queue) — **not** canonical, **not** rejected.

Use when the claim may be valid but **cannot be attested now**.

### 5.2 Defer triggers

| Trigger | Example |
|---------|---------|
| Evidence pending | Awaiting E2 contract extract |
| Wave prerequisite | Website before org attested |
| Homonym investigation | Similar name — need disambiguation |
| Owner strategic pause | Population cooling |
| Capacity | Steward backlog — hold low priority (not P0) |

### 5.3 Defer rules

| Rule ID | Rule |
|---------|------|
| **DEF-01** | Defer **requires documented reason** |
| **DEF-02** | Defer is **not** SAFE UNKNOWN — proposal still exists |
| **DEF-03** | Deferred proposals **age** per [ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md) |
| **DEF-04** | Owner may convert defer → reject if abandoned |

---

## 6. Reject

### 6.1 Meaning

**Reject** terminates the proposal — **no active canonical** record from that claim. Rationale logged.

### 6.2 Reject triggers

| Trigger | Example |
|---------|---------|
| Boundary violation | CRM deal as entity |
| Fabricated evidence | Tier misrepresented |
| Non-MVP class demand | “Service” as entity without expansion |
| Repeated consumer violation | Shadow registry pattern |
| Invalid relationship family | Wrong endpoint types |

### 6.3 Reject rules

| Rule ID | Rule |
|---------|------|
| **REJ-01** | Reject at intake for clear boundary violations |
| **REJ-02** | Steward may reject; Owner may reject with policy override note |
| **REJ-03** | Reject **does not** block reproposal with corrected claim |
| **REJ-04** | Reject **≠** deprecated — no canonical record existed |

---

## 7. Challenge

### 7.1 Meaning

**Challenge** is a **qualified flag** that an existing or proposed canonical fact is wrong, incomplete, or conflicting — **without** granting rewrite rights.

Any role with flag authority may challenge ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §8.2).

### 7.2 Challenge package

| Element | Required |
|---------|----------|
| Target record or proposal | Yes |
| Nature of challenge | factual error · evidence insufficient · duplicate · boundary |
| Counter-evidence or rationale | Yes |
| Challenger role | Yes |

### 7.3 Challenge flow

```text
Challenge opened
      │
      ▼
Steward triage ──► Minor: evidence review ──► attest correction | defer | UNKNOWN
      │
      └──► Material conflict ──► mark DISPUTED ──► Dispute review
```

**CH-01:** Challenge **does not** change canonical state until review completes (AT-CH-01).

---

## 8. Dispute

### 8.1 Meaning

**Dispute** is **disputed** lifecycle state — competing claims with material conflict. Blocks new irreversible canonical dependencies on affected nodes.

### 8.2 Dispute triggers

| Trigger | Example |
|---------|---------|
| Dual OWNER claims | Two orgs claim same domain |
| Merge disagreement | Consumer keys map to different survivors |
| Conflicting attestations | Two stewards, incompatible E1 narratives |
| Unresolved challenge | Steward cannot reconcile |

### 8.3 Dispute resolution flow

```text
disputed
   │
   ▼
Steward evidence review
   │
   ├──► Attest one side (deprecate other)
   ├──► Merge (if same subject)
   ├──► Separate (if distinct subjects)
   ├──► SAFE UNKNOWN
   └──► Escalate to Owner (legal, split, stale)
```

**DISP-01:** While **disputed**, POP-DISP-01 applies — block new canonical dependencies.

**DISP-02:** Stale disputes escalate to Owner **faster** than routine defer ([ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md)).

### 8.4 Consumer escalation (Architectural Analysis #7)

Consumers **escalate disagreement** through:

1. **Challenge** with evidence (preferred first step)
2. **Dispute** if steward marks disputed or challenge unresolved
3. **Owner escalation** if steward decision contested with new evidence
4. **Certification / health review** if pattern of semantic drift

Consumers **never**:

- Write active canonical records locally and demand sync
- Threaten operational blockers to bypass attestation
- Create parallel “client master” and cite OPS C-01 as entity class

**DISP-C-01:** Consumer escalation is **governance process**, not **operational veto** over ATLAS boundaries.

---

## 9. Attestation

### 9.1 Meaning

**Attestation** is the recorded human decision promoting a reviewed proposal to **active** canonical state ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §4).

### 9.2 Pre-attest checklist (operational)

| Check | Gate |
|-------|------|
| Class valid | G1 |
| Wave satisfied (if population) | G2 |
| Evidence tier ≥ minimum | G3 |
| Duplicate clear | G4 |
| Relationship endpoints valid | G5 |
| Slot uniqueness | G6 |

From [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) §4.1.

### 9.3 Attest act (conceptual record)

| Element | Capture |
|---------|---------|
| Attestor role | Owner or delegated Steward |
| Target | Entity or relationship id |
| Evidence tier accepted | E0–E3 |
| Short rationale | Required |
| Timestamp | Required |

**ATT-01:** No attest without completed review (except Owner emergency — noted in health review).

**ATT-02:** Split path **never** uses steward attest alone — Owner only.

---

## 10. End-to-end scenarios

### 10.1 Routine org proposal (Wave 1)

```text
Steward proposes Organization → intake → intake review
  → duplicate review clear → evidence E1 → attest → active
```

### 10.2 Consumer missing website org

```text
Consumer proposes Website + flags UNKNOWN org
  → defer website active until org attested OR attest UNKNOWN on org gap
  → never invent org-unknown-* placeholder (AT-UK-02)
```

### 10.3 Import batch

```text
Agent import → all proposed + E3
  → steward batch intake review + spot checks
  → subset attest; duplicates → merge workflow; orphans → defer or UNKNOWN
```

### 10.4 OPS requisites mismatch

```text
Consumer flags ATLAS org record missing invoicing fields
  → boundary review: requisites not MVP entity
  → defer expansion OR consumer-local until field expansion chartered
  → see OPS-ATLAS-ALIGNMENT-v1.md
```

---

## 11. Consolidated outcome table

| Outcome | Canonical effect | Queue effect |
|---------|------------------|--------------|
| **Attest → active** | Canonical SoT | Remove from queue |
| **Defer** | None (proposed remains) | Hold with reason |
| **Reject** | None | Close |
| **Disputed** | Block dependencies | Priority P0 review |
| **SAFE UNKNOWN** | Explicit gap | Close proposal path; gap tracked |
| **Merge** | Survivor active; loser deprecated | Duplicate queue cleared |
| **Split** | Owner-only; new ids | Escalation complete |

Normative semantics: [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §6.2, [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md).

---

## 12. Non-deliverables

No ticket schema, queue software, notification system, or automated routing.

---

*ATLAS Intake and Review Model v1 — Phase 8 Foundation. Documentation only.*
