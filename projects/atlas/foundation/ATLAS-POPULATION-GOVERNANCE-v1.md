# ATLAS Population Governance v1

**Status:** **documented** — Phase 7 population authority and quality controls (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-POPULATION-STRATEGY-v1.md](ATLAS-POPULATION-STRATEGY-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) · [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md)  
**Is not:** RBAC implementation, ticketing system, steward roster (defer Operational Model), approval UI.

**Phase 1–6 constraint:** Extends existing role matrices; does not weaken IGV-01, GV-01, AT-IMP-01.

---

## 1. Purpose

Define **who may propose, review, attest, reject, and defer** during population; **quality controls** for duplicates and collisions; and **when population must stop** vs when **SAFE UNKNOWN** is mandatory.

---

## 2. Population authority matrix

Actions during population map to attestation governance ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §8).

| Action | Program owner | Registry steward | Consumer | Agent |
|--------|---------------|------------------|----------|-------|
| **Propose** entity/relationship | Yes | Yes | Yes (future) | Yes (proposal) |
| **Review** (intake, evidence, duplicate) | Yes | Yes | No | No |
| **Attest → active** | Yes | Delegated | **No** | **No** |
| **Reject** proposal | Yes | Yes | No | No |
| **Defer** (hold proposed) | Yes | Yes | No | No |
| **Declare SAFE UNKNOWN** | Yes | Yes | No | No |
| **Mark disputed** | Yes | Yes | Flag | Flag |
| **Resolve dispute** | Yes | Delegated | No | No |
| **Approve merge** | Yes | Delegated | No | No |
| **Approve split** | **Owner only** | No | No | No |
| **Halt population wave** | Yes | Escalate | No | No |

**POP-GV-01:** Delegation to stewards must be **written** (GV-02, IGV).

**POP-GV-02:** Challenge flags do not grant consumers rewrite rights (AT-CH-01).

---

## 3. Role definitions in population context

### 3.1 Who may propose

| Proposer | Allowed proposal types | Limits |
|----------|------------------------|--------|
| **Steward** | Any MVP class, any wave | Must follow wave order for **active** promotion |
| **Program owner** | Any | Override defer; split/merge |
| **Consumer operator** | Mapping suggestions, entity proposals | **proposed** only |
| **Agent** | Bulk proposals from intake | **proposed** only; quality review mandatory |

**POP-PROP-01:** Proposals **outside current wave** are queued — not rejected automatically — but **must not** be attested active until wave prerequisites met.

### 3.2 Who may review

**Review** = intake, evidence, duplicate, boundary, dispute reviews ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §6).

| Reviewer | Scope |
|----------|-------|
| **Steward** | Day-to-day population queue |
| **Program owner** | Escalations, expansion overlap, split/merge |

Consumers **flag** for review; they do not **complete** population review.

### 3.3 Who may attest

| Target | Attestor |
|--------|----------|
| Entity → active | Steward (delegated) or Owner |
| Relationship → active | Steward (delegated) or Owner |
| Merge | Owner or delegated steward |
| Split | **Owner only** |
| Alias canonical use | Steward or Owner |

### 3.4 Who may reject

| Reject authority | When |
|------------------|------|
| Steward | Boundary violation, insufficient evidence, CRM bleed, fabricated tier |
| Owner | Policy override, repeated steward error, expansion conflict |

**Reject** leaves **no active canonical** record; rationale logged (conceptual).

### 3.5 Who may defer

| Defer authority | When |
|-----------------|------|
| Steward | Evidence pending, wave prerequisite, homonym investigation |
| Owner | Strategic pause, dispute cooling, capacity halt |

**Defer** keeps **proposed** (or intake queue) — distinct from **SAFE UNKNOWN**.

---

## 4. Population quality controls

### 4.1 Intake quality gates (per record)

| Gate | Check |
|------|-------|
| **G1 — Class** | MVP entity vs boundary exclusion |
| **G2 — Wave** | Prerequisites for active promotion |
| **G3 — Evidence** | Tier ≥ minimum ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md)) |
| **G4 — Identity** | Duplicate class D1–D5 triage |
| **G5 — Relationship** | Endpoint types match taxonomy family |
| **G6 — Collision** | Canonical slot uniqueness (RP-04) |

Failure at G1 → **reject**. Failure at G2–G6 → **defer**, **disputed**, or **UNKNOWN** — not active.

### 4.2 Duplicate prevention

| Control | Mechanism |
|---------|-----------|
| **Pre-attest search** | Steward checks alias + name + consumer keys |
| **D1 halt** | Second active for same subject forbidden |
| **Import mapping** | Consumer key → proposed id before promote |
| **IGV-D01** | String similarity **insufficient** for merge |
| **No placeholder ids** | IGV-D02 / CR-10 |

Population **pause** if D1 detected in wave: resolve before new active promotions in same class.

### 4.3 Identity collision prevention

| Collision type | Prevention |
|----------------|------------|
| **Homonym org/person** | Separate ids + disambiguation note |
| **Cross-type mistake** | D5 review — Person vs Org |
| **Namespace violation** | Identifier model rules |
| **Consumer double-key** | Two proposed → one survivor path |

### 4.4 Relationship collision prevention

| Collision type | Prevention |
|----------------|------------|
| **Duplicate slot** | Same type + endpoints + overlapping window → one active |
| **Conflicting OWNER** | **disputed** until resolved |
| **Edge before endpoint** | **proposed** edge only (EIR-R02) |
| **Wrong family** | Reject type (RR-08) |

**POP-COL-01:** Resolve **entity identity** before **relationship** attest when A4 naming collision ([ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §4).

---

## 5. Wave governance

| Rule | Description |
|------|-------------|
| **POP-W-01** | Active promotions must respect [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md) |
| **POP-W-02** | Wave 2B may begin when Wave 1 core orgs **active** |
| **POP-W-03** | Wave 6 bulk may begin when Waves 1–5 **core set** attested or explicitly deferred with UNKNOWN |
| **POP-W-04** | Skipping waves for “urgent consumer id” requires **owner exception** with documented risk acceptance |

---

## 6. When population must stop

Population **halts** (wave or global) when:

| Stop trigger ID | Condition |
|-----------------|-----------|
| **STOP-01** | Unresolved **D1** duplicate (two active same subject) |
| **STOP-02** | Fabricated evidence tier discovered |
| **STOP-03** | Steward capacity exceeded — queue SLA breach (operational detail in Operational Model) |
| **STOP-04** | Owner declares population freeze (audit, dispute program) |
| **STOP-05** | Expansion change in flight — taxonomy amendment pending |
| **STOP-06** | Systemic import error — > threshold **proposed** without attest trail (conceptual threshold set in ops) |
| **STOP-07** | Repeated boundary violations from same consumer source |

**During stop:** No new **active** promotions; **proposed** intake may continue only if steward can queue without promoting.

**Resume:** Owner or steward lead signs off after root cause cleared.

---

## 7. When UNKNOWN is preferred

| Situation | Prefer UNKNOWN over… |
|-----------|------------------------|
| Org for website unclear | Inventing Organization |
| Relationship type unclear | Guessing OWNER |
| Merge uncertain | Forced merge |
| Import key orphan | Fabricated id |
| Conflicting E1 narratives | Active pick of winner |
| Business Scope label | Entity existence proof |

**POP-UNK-01:** UNKNOWN is **preferred** to **active wrong**.

**POP-UNK-02:** UNKNOWN is **not preferred** to **proposed with good evidence** — use **proposed** when promotion is imminent pending one fact.

---

## 8. Dispute handling (population)

Aligned with [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §6.2 and §8.2:

```text
Flag → Evidence review → Owner escalation (if needed)
  → attest one | merge | separate | SAFE UNKNOWN
```

**POP-DISP-01:** While **disputed**, block new canonical dependencies on affected nodes.

---

## 9. Consumer and agent population limits

| Rule | Description |
|------|-------------|
| **POP-C-01** | Consumers never attest active |
| **POP-C-02** | Agent proposal flood → steward may STOP-03 |
| **POP-C-03** | Consumer may not demand Business Scope shard |
| **POP-C-04** | Certification level caps reference depth ([ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md)) |

---

## 10. Escalation path

| Level | Issue |
|-------|-------|
| **L1 Steward** | Routine intake, E1 evidence |
| **L2 Owner** | Split, legal merge, STOP triggers, wave skip exception |
| **L3 Program / architect** | Expansion + population strategy conflict |

---

## 11. Non-deliverables

No workflow engine, steward roster, SLA numbers, or enforcement code.

---

*ATLAS Population Governance v1 — Phase 7 Foundation. Documentation only.*
