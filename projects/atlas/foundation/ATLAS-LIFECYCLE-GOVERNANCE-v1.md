# ATLAS Lifecycle Governance v1

**Status:** **documented** — Phase 5 normative governance for lifecycle changes.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-LIFECYCLE-MODEL-v1.md](ATLAS-LIFECYCLE-MODEL-v1.md) · [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](ATLAS-LIFECYCLE-TRANSITIONS-v1.md)  
**Integrates:** [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) · [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) · [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)  
**Is not:** approval UI, RBAC, ticketing integration, automated policy engine.

---

## 1. Purpose

Define **who owns lifecycle decisions**, **how lifecycle changes are approved**, **how conflicts are resolved**, and **how SAFE UNKNOWN interacts with lifecycle** — without duplicating Phase 2–4 domain governance; Phase 5 governs the **unified lifecycle layer**.

---

## 2. Lifecycle ownership

### 2.1 Ownership layers

| Layer | What is owned | Authority |
|-------|---------------|-----------|
| **Vocabulary** | State codes, forbidden ops terms | Program owner (document amendment) |
| **Transition policy** | Valid edges, attest tiers | Phase 5 docs + owner sign-off on change |
| **Record execution** | Applying transitions to rows | Steward (delegated) / owner |
| **Slot posture** | SAFE UNKNOWN declaration | Steward / owner |
| **Consumer mapping** | UI labels for ATLAS states | Each consumer — **must not** alter ATLAS codes |

**Rule LG-OWN-01:** Lifecycle vocabulary changes are **S4** changes ([ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md)) — not steward discretion.

### 2.2 Role definitions

Roles align with Phase 2–4; lifecycle-specific authority extensions:

| Role | Lifecycle authority |
|------|---------------------|
| **Program owner / operator** | Final dispute resolution; merge/split; archived error correction; SAFE UNKNOWN for systemic gaps; vocabulary amendments |
| **Registry steward** | Intake; proposed → active (delegated); deprecate; dispute flag; relationship supersession (delegated); archive routine |
| **Consumer proposer** | Create **proposed** only (future); flag dispute — **no** lifecycle promotion |
| **Agent proposer** | Same as consumer — proposal only |
| **Auditor (read-only)** | Query lifecycle; flag anomalies — no transitions |

---

## 3. Authority matrix

### 3.1 By transition (summary)

| Transition | Owner | Steward | Consumer | Agent |
|------------|-------|---------|----------|-------|
| → **proposed** | Yes | Yes | Propose (future) | Propose |
| **proposed** → **active** | Yes | Delegated | **No** | **No** |
| → **disputed** | Yes | Yes | Flag | Flag |
| **disputed** → **active** (winner) | Yes | Delegated | No | No |
| **active** → **deprecated** | Yes | Delegated | No | No |
| **active** → **merged** (loser) | Approve | Propose | No | No |
| **active** → **split_source** | **Approve only** | Propose | No | No |
| **active** → **replaced** (rel) | Yes | Delegated | No | No |
| → **archived** | Yes | Delegated | No | No |
| **archived** → **deprecated** (error) | **Yes only** | No | No | No |
| **deprecated** → **active** (reactivate) | Approve | Propose | No | No |
| Declare **SAFE UNKNOWN** | Yes | Yes | No | No |
| Amend Phase 5 lifecycle docs | **Yes** | Prepare | No | No |

### 3.2 Consolidated authority types

| Authority type | Definition | Holder |
|----------------|------------|--------|
| **Approval authority** | Permission to move record to **active** or affirm after **disputed** | Owner or delegated steward |
| **Challenge authority** | Permission to mark **disputed** or halt promotion | Owner, steward, consumer flag |
| **Dispute authority** | Permission to resolve **disputed** → outcome | Owner (systemic); steward (routine, delegated) |
| **Restoration authority** | Permission for **deprecated** → **active** or archived error path | **Owner** |
| **Merge authority** | Permission for **merged** transition | Owner approve; steward propose |
| **Split authority** | Permission for **split_source** | **Owner only** |

**Rule LG-01:** No autonomous **active** promotion (extends GV-01, IGV-01).

**Rule LG-02:** Split and archived error correction require **owner** (extends IGV-S01).

**Rule LG-03:** Delegation must be **written** — not assumed from chat.

---

## 4. How lifecycle changes are approved

### 4.1 Approval workflow (conceptual)

```text
Trigger (intake · import · dispute · end · merge)
  → Classify severity (S0–S5 per Change Governance)
  → Attach evidence tier (Attestation Model)
  → Reviewer per Transition doc §7
  → Written attest note (minimum fields below)
  → Apply lifecycle_state transition
  → Notify consumers (future channel)
```

### 4.2 Minimum attestation note (lifecycle change)

| Field | Required |
|-------|----------|
| `transition` | e.g. proposed → active |
| `record_id` | Stable id |
| `attested_by` | Human role reference |
| `attested_at` | ISO timestamp |
| `evidence_ref` | Per tier |
| `rationale` | Plain language — business structural reason |

### 4.3 Severity mapping (lifecycle)

| Severity | Lifecycle examples | Approver |
|----------|-------------------|----------|
| **S0** | proposed → active (routine instance) | Steward |
| **S1** | Alias-only amend (no lifecycle change) | N/A lifecycle |
| **S2** | Merge; disputed resolution affecting multiple consumers | Owner or delegated |
| **S3** | New lifecycle state code (vocabulary) | Owner + doc amendment |
| **S4** | Boundary-violating “lifecycle” (reject) | Owner reject |
| **S5** | Split; archived error correction; ecosystem SAFE UNKNOWN | Owner |

### 4.4 Batch import governance

Per [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §9:

| Step | Lifecycle posture |
|------|-------------------|
| Import | All rows **proposed** |
| Review | Steward batch |
| Promote | Subset → **active** with individual attest |
| Duplicate | → merge workflow (**merged**) |
| Unresolved | **SAFE UNKNOWN** — not **active** placeholder |

**Prohibition LG-IMP-01:** Batch scripts must not set **active** without per-record attest trail.

---

## 5. How lifecycle conflicts are resolved

### 5.1 Conflict classes

| Class | Example | Lifecycle response |
|-------|---------|-------------------|
| **C1 — Dual active same subject** | Two ORG-* active for same unit | Halt; **disputed** or merge |
| **C2 — Slot competition** | Two OWNER for singleton domain | **disputed**; no slot **active** until resolved |
| **C3 — Consumer ≠ ATLAS** | CRM says active client; ATLAS **deprecated** | Flag **disputed** on consumer mapping, not silent ATLAS change |
| **C4 — Identity vs relationship** | Person active but EMPLOYEE ended | Valid — entity **active**, relationship **deprecated** |
| **C5 — Merge redirect loop** | redirect_to missing | Block **merged** until fixed — owner |
| **C6 — Vocabulary drift** | Consumer enum `LIVE` = ATLAS active | Consumer mapping fix — not ATLAS state add |

### 5.2 Resolution principles

| ID | Principle |
|----|-----------|
| **LG-R01** | **Structural resolution** — not commercial adjudication |
| **LG-R02** | **Preserve history** — losers → **merged** / **replaced** / **deprecated**, not delete |
| **LG-R03** | **Document outcome** — written decision for S2+ |
| **LG-R04** | **ATLAS wins** when **active** attested and consumer cache stale ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) §8.3) |
| **LG-R05** | **SAFE UNKNOWN** when evidence insufficient — not forced **active** |

### 5.3 Escalation path

```text
Steward triage
  → resolve routine (S0–S1 lifecycle)
  → escalate S2+ to Owner
  → if boundary/taxonomy touched → Change Governance S3–S4
  → if vocabulary gap → Phase 5 amendment package (not ad-hoc state)
```

### 5.4 Relationship to Phase 2–3 governance

| Domain event | Primary governance | Lifecycle role |
|--------------|-------------------|----------------|
| Relationship dispute | [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) | Uses **disputed** / **replaced** states |
| Identity merge/split | [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) | Uses **merged** / **split_source** |
| Registry expansion | [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) | Does not add lifecycle states without Phase 5 bump |

Phase 5 **does not weaken** prior rules; it **names** outcomes consistently.

---

## 6. SAFE UNKNOWN and lifecycle

### 6.1 Definitions

| Concept | Type | Meaning |
|---------|------|---------|
| **lifecycle_state** | Record field | Where **this row** is in registry posture |
| **SAFE UNKNOWN** | Subject/slot posture | **No attested active** canonical for a business fact |

### 6.2 Interactions

| Situation | Lifecycle on rows | Slot posture |
|-----------|-------------------|--------------|
| Zero rows | — | SAFE UNKNOWN |
| Only **proposed** rows | proposed | SAFE UNKNOWN for canonical use |
| **disputed** rows only | disputed | SAFE UNKNOWN for canonical use |
| **active** attested winner | active | Canonical resolved |
| All **deprecated** / **merged** | terminals | SAFE UNKNOWN for **current** structure unless new **active** exists |

### 6.3 Governance rules

| Rule ID | Rule |
|---------|------|
| **LG-SU-01** | Declaring SAFE UNKNOWN is **not** creating a placeholder entity ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-10) |
| **LG-SU-02** | Stewards and owners may declare; consumers may **request** review |
| **LG-SU-03** | SAFE UNKNOWN must be **visible** to consumers (contract), not silent null |
| **LG-SU-04** | Resolving UNKNOWN → **active** requires same attest as proposed → active |
| **LG-SU-05** | UNKNOWN + **disputed** proposals may coexist — still non-canonical until resolved |

### 6.4 Consumer obligations under UNKNOWN

Per [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md):

- Do not invent `ORG-unknown-*` as canonical.  
- Do not treat CRM-only ids as ATLAS **active**.  
- May continue **operational work** locally — ATLAS does not track work lifecycle.

---

## 7. Lifecycle document governance

| Change | Path |
|--------|------|
| Clarification in Phase 5 without contradiction | Minor amendment + REPORT |
| New lifecycle state code | Phase 5 v2 package + owner |
| Contradiction with Phase 1–4 | Crosswalk + owner decision: amend Phase 5 or escalate Phase 1–4 (rare) |

**Rule LG-DOC-01:** Implementation charters must cite approved lifecycle doc version.

---

## 8. Anti-patterns (lifecycle governance)

| Anti-pattern | Correct posture |
|--------------|-----------------|
| CRM stage drives ATLAS **active** | Import **proposed** + attest |
| “Mark done” sets project **completed** | **deprecated** with note |
| Delete canonical to “clean registry” | **deprecated** / **merged** / **archived** |
| Consumer redefines `active` as “billing active” | Consumer-local field; ATLAS **active** = structural attest |
| Auto-expire relationships by cron | Human or policy attest → **deprecated** |
| Agent promotes after confidence score | **Proposed** only |

---

## 9. Compliance checklist

- [ ] Transition has reviewer per §3?
- [ ] Attest note complete per §4.2?
- [ ] SAFE UNKNOWN not implemented as fake entity?
- [ ] Merge/split/archived correction has owner where required?
- [ ] No operational vocabulary as new state code?

---

*ATLAS Lifecycle Governance v1 — lifecycle authority. Documentation only.*
