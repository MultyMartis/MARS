# ATLAS Role Model v1

**Status:** **documented** — Phase 8 operational roles (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md)  
**Is not:** RBAC implementation, org chart, named roster, HR roles, consumer job titles.

**Phase 1–7 constraint:** Operationalizes role matrices in Phase 4 attestation §8 and Phase 7 population §2–3 without weakening them.

---

## 1. Purpose

Define **operational roles** for human-supervised ATLAS governance — responsibilities, authority, limitations, escalation rights, and interaction patterns.

**Normative role set (MVP operations):**

```text
Program Owner · Registry Steward · Reviewer · Consumer · Observer
```

**Reviewer** is a **functional hat** worn by Steward or Owner during structured review — not a separate canonical authority tier unless explicitly delegated for audit.

---

## 2. Role evaluation summary

| Role | Verdict | Notes |
|------|---------|-------|
| **Program Owner** | **Required** | Ultimate accountability — already implied in Phases 3–7 |
| **Registry Steward** | **Required** | Day-to-day custodian — AT §5.1 |
| **Reviewer** | **Required (as function)** | Structured review duty; often same person as steward |
| **Consumer** | **Required** | Propose/challenge boundary — Phase 6 |
| **Observer** | **Added** | Read-only oversight for audit, architecture, certification — no attest |

**Not added as operational roles:** Agent (tool actor), Import pipeline (process), Helpdesk operator, CRM admin — these interact **through** Consumer or Steward paths.

---

## 3. Role definitions

### 3.1 Program Owner

**Purpose:** Ultimate human accountability for ATLAS program integrity and operational policy.

| Attribute | Definition |
|-----------|------------|
| **Responsibilities** | Foundation amendments; written steward delegation; split approval; population freeze/resume; dispute terminus; registry health sign-off; STOP trigger response; wave skip exceptions (POP-W-04) |
| **Authority** | Full attest; merge; split (**exclusive**); reject; defer; declare SAFE UNKNOWN; halt population; approve expansion |
| **Limitations** | Cannot override ATLAS boundaries; cannot attest without evidence discipline; cannot delegate split |
| **Escalation rights** | Terminus — receives escalations from stewards, consumers (via dispute), health reviews |

**Delegation:** Owner **may delegate** stewardship and most attestation to named stewards in **writing** (POP-GV-01).

**Continuity:** When stewards unavailable, Owner **must** assume interim stewardship or designate interim steward ([ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) §8.1).

---

### 3.2 Registry Steward

**Purpose:** Day-to-day custodian of intake, review, attestation quality, and routine dispute investigation.

| Attribute | Definition |
|-----------|------------|
| **Responsibilities** | Intake triage; evidence tier assignment; duplicate/homonym routing; boundary smell detection; routine attest (delegated); defer/reject; dispute first response; population queue management; health signal triage |
| **Authority** | Propose; review; attest → active (**if delegated**); merge (**if delegated**); reject; defer; declare SAFE UNKNOWN; mark disputed; escalate |
| **Limitations** | No split; no expansion approval; no boundary override; no wave skip without owner; no consumer attest on behalf |
| **Escalation rights** | To Program Owner: split candidates, legal merge ambiguity, STOP triggers, repeated consumer violation, unresolved dispute, stale queue breach |

**Stewardship delegation (Architectural Analysis #2):** **Yes** — multiple stewards allowed with scoped written delegation (e.g., relationship-only steward).

**Attestation delegation (Architectural Analysis #3):** **Yes** — entity/relationship active, merge, alias — **not** split or expansion.

---

### 3.3 Reviewer

**Purpose:** Execute **structured review** types per [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §6.1 — intake, evidence, duplicate, boundary, dispute, expansion.

| Attribute | Definition |
|-----------|------------|
| **Responsibilities** | Apply review outcomes; document rationale; route to attest/defer/reject/disputed/UNKNOWN |
| **Authority** | Same as acting steward **during assigned review**; spot-audit authority if owner-delegated |
| **Limitations** | Reviewer without steward delegation **cannot attest** — findings only |
| **Escalation rights** | To steward lead or owner when review exceeds scope |

**Typical assignment:**

| Review type | Default reviewer |
|-------------|------------------|
| Intake, evidence, duplicate | Registry Steward |
| Boundary, expansion overlap | Steward → Owner |
| Dispute (complex) | Owner |
| Certification audit | Observer + Owner |

---

### 3.4 Consumer

**Purpose:** Operational program or human operator acting **on behalf of** a declared ATLAS consumer (MIG, ORCA, OPS, Factory, WPilot, HomeGateway, etc.).

| Attribute | Definition |
|-----------|------------|
| **Responsibilities** | Maintain consumer mapping document; propose entities/relationships; flag errors; supply evidence refs; respect certification tier |
| **Authority** | Propose (proposed state only); challenge / open dispute; request review |
| **Limitations** | **No attest active**; no merge/split; no lifecycle overwrite; no shadow canonical store |
| **Escalation rights** | Challenge → dispute → steward → owner ([ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) §8) |

**Rule ROLE-C-01:** Consumer escalation is **dispute path**, not **rewrite path** (AT-CH-01).

---

### 3.5 Observer

**Purpose:** Read-only oversight for architecture audit, certification review, and training — **without** canonical write authority.

| Attribute | Definition |
|-----------|------------|
| **Responsibilities** | Review registry exports; audit semantic compliance; attend health reviews; document findings |
| **Authority** | Read canonical and proposed (when shared); comment; recommend |
| **Limitations** | No propose with binding effect unless also Consumer; no attest; no defer/reject |
| **Escalation rights** | Recommendations to Owner — not operational commands |

**Examples:** External auditor, architect, certification reviewer, new steward trainee.

---

## 4. Authority matrix (consolidated)

Consolidates [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §8.1 and [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) §2 for operational use.

| Action | Owner | Steward (delegated) | Reviewer | Consumer | Observer |
|--------|-------|---------------------|----------|----------|----------|
| Propose | Yes | Yes | — | Yes | No |
| Review (complete) | Yes | Yes | If steward | No | No |
| Attest → active | Yes | Yes | No* | **No** | No |
| Reject | Yes | Yes | No* | No | No |
| Defer | Yes | Yes | No* | No | No |
| SAFE UNKNOWN | Yes | Yes | No* | No | No |
| Mark disputed | Yes | Yes | No* | Flag | No |
| Resolve dispute | Yes | Delegated | No | No | No |
| Merge | Yes | Delegated | No | No | No |
| Split | **Yes only** | No | No | No | No |
| Halt population | Yes | Escalate | No | No | No |
| Expansion approve | Yes | No | No | No | No |

\*Reviewer may **recommend** outcome; attest requires steward/owner role.

---

## 5. Role interaction model

### 5.1 Primary flows

```text
Consumer / Agent / Steward
         │
         ▼ PROPOSE
    Intake queue ──► Steward REVIEW ──► Attest | Defer | Reject | Disputed | UNKNOWN
         │                    │
         │                    └──► Owner (escalation)
         │
Consumer CHALLENGE ──► Dispute review ──► Steward ──► Owner (if unresolved)
```

### 5.2 Interaction rules

| Rule ID | Interaction |
|---------|-------------|
| **RI-01** | Consumers **never** instruct stewards to attest — they **request review** with evidence |
| **RI-02** | Stewards **must** escalate split candidates to Owner — no steward-to-steward split |
| **RI-03** | Owner **may** override steward defer with attest/reject — with documented rationale |
| **RI-04** | Observers **do not** participate in attest decisions |
| **RI-05** | Agent proposals **always** enter as steward-reviewed — no agent-to-active path |
| **RI-06** | Multiple stewards **coordinate** via shared queue discipline — not independent canonical forks |
| **RI-07** | Consumer certification level **caps** reference behavior — not steward authority |

### 5.3 Escalation ladder

| Level | Role | Typical issues |
|-------|------|----------------|
| **L1** | Registry Steward | Routine intake, E0–E1, alias, single duplicate |
| **L2** | Program Owner | Split, legal merge, STOP, wave skip, stale dispute |
| **L3** | Program / MARS architect | Expansion conflict, cross-program ontology drift |

Reaffirms [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) §10.

### 5.4 Conflict of interest

| Situation | Rule |
|-----------|------|
| Steward proposes record they attest | **Allowed** with explicit rationale — spot audit recommended |
| Consumer attests own proposal | **Forbidden** |
| Owner attests without review | **Allowed** for emergency — health review must note |
| Observer was proposer | **Recuse** from review |

---

## 6. Role vs structural relationship

**Distinction (consistency with audit):**

| Concept | Meaning |
|---------|---------|
| **OWNER relationship type** | Structural edge in graph (Phase 2 taxonomy) |
| **Program Owner role** | Governance accountability for ATLAS program |
| **Registry Steward role** | Operational custodian |

Operational roles **do not** auto-create or replace **OWNER** / **CLIENT_OF** relationships.

---

## 7. Related documents

| Document | Link |
|----------|------|
| Operational model | [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) |
| Intake and review | [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) |
| Attestation roles | [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §8 |
| Population authority | [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) §2 |

---

## 8. Non-deliverables

No named individuals, RBAC tables, SSO groups, or org chart.

---

*ATLAS Role Model v1 — Phase 8 Foundation. Documentation only.*
