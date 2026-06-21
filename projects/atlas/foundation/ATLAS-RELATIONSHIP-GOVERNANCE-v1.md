# ATLAS Relationship Governance v1

**Status:** **documented** — Phase 2 normative governance for Relationship records.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md)  
**Is not:** RBAC implementation, ticketing integration, automated conflict bots, approval UI.

---

## 1. Purpose

Define **who may assert relationships**, **what evidence is required**, **how ambiguity and SAFE UNKNOWN are handled**, and **how conflicts are resolved** — governance only, no implementation.

Aligned with Phase 1: human-supervised, documentation-first, no silent invention.

---

## 2. Governance roles

### 2.1 Role definitions (conceptual)

| Role | Authority |
|------|-----------|
| **Program owner / operator** | Final canonical attestation; dispute resolution; expansion approval |
| **Registry steward** | Day-to-day intake, evidence review, propose → attest workflow |
| **Consumer proposer** | Submit **proposed** relationships (future); cannot set **active** canonical alone |
| **Agent proposer** | Same as consumer — **proposal only**, never canonical without human |
| **Auditor (read-only)** | Query graph; flag disputes; no attestation |

### 2.2 Who may create relationships

| Action | Program owner | Steward | Consumer | Agent |
|--------|---------------|---------|----------|-------|
| Create **proposed** | Yes | Yes | Yes (future) | Yes (proposal) |
| Promote to **active** canonical | Yes | Yes (if delegated) | **No** | **No** |
| Mark **disputed** | Yes | Yes | Yes (flag) | Yes (flag) |
| Resolve dispute | Yes | With delegation | No | **No** |
| Deprecate / supersede | Yes | Yes | No | No |
| Archive | Yes | Yes | No | No |
| Declare **SAFE UNKNOWN** | Yes | Yes | No | No |

**Rule GV-01:** No autonomous promotion to canonical.

**Rule GV-02:** Delegation to stewards must be **written** (operator note), not assumed.

---

## 3. Evidence requirements

### 3.1 Evidence tiers

| Tier | Description | Minimum evidence |
|------|-------------|------------------|
| **E0 — Internal attestation** | Operator already knows structural fact | Steward/owner attestation note |
| **E1 — Informal document** | Chat export, email, signed letter scan reference | Citation + date |
| **E2 — Formal document** | Contract, registrar record, corporate registry extract | Document reference id (not full text in ATLAS) |
| **E3 — System corroboration** | Consumer-held foreign key (CRM id, registrar API snapshot) | Import reference; still human promote |

**Rule GV-E01:** Higher-risk types require higher tier:

| Type category | Minimum tier |
|---------------|--------------|
| OWNER, OWNS (domain/site) | E1 or E2 |
| CLIENT_OF | E1 |
| REPRESENTATIVE | E1 |
| PRIMARY_DOMAIN | E1 (registrar / DNS intent) |
| EMPLOYEE / CONTRACTOR | E1 (structural, not payroll) |
| proposed → active (any) | E0 allowed **only** for operator direct attest |

### 3.2 Evidence storage

| Allowed in ATLAS (future) | Forbidden in ATLAS |
|---------------------------|-------------------|
| `evidence_ref` pointer | Full contract body |
| Short attestation note | Salary, deal value |
| Link to external doc store | CRM pipeline history |

Contracts and invoices remain **external**; ATLAS holds **pointers** only.

### 3.3 Evidence insufficient

| Situation | Action |
|-----------|--------|
| Evidence below tier | Remain **proposed** or **disputed** |
| No evidence at all | **SAFE UNKNOWN** — no canonical |
| Fabricated placeholder ref | Reject proposal; log incident |

---

## 4. Ambiguity handling

### 4.1 Ambiguity classes

| Class | Example | Default action |
|-------|---------|----------------|
| **A1 — Unknown type** | “Works with” without OWNER/CONTRACTOR | **SAFE UNKNOWN** or **proposed** without type lock |
| **A2 — Unknown endpoint** | Website exists; org unclear | No BELONGS_TO/OWNS canonical |
| **A3 — Overlapping dates** | Two owners same period | **disputed** until resolved |
| **A4 — Naming collision** | Two “Polygon” orgs | Entity identity resolution (Identity Foundation) before Relationship |
| **A5 — Import mismatch** | CRM ACCOUNT maps to multiple orgs | Steward review; no auto-merge |

### 4.2 Ambiguity workflow

```text
Detect → Classify (A1–A5) → Block canonical promotion
       → Document in intake log
       → Gather evidence OR declare SAFE UNKNOWN
       → Human resolve → active / supersede / UNKNOWN
```

### 4.3 Prohibition

**GV-A01:** Do not resolve ambiguity by inventing entities or default types to unblock consumers ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-10).

---

## 5. SAFE UNKNOWN handling

### 5.1 When SAFE UNKNOWN is required

| Situation | UNKNOWN scope |
|-----------|---------------|
| Ownership of domain unknown | Slot (OWNS / OWNER) for that Domain |
| Client relationship unclear | CLIENT_OF between specific org pair |
| Representative authority unclear | REPRESENTATIVE for Person → Org |
| Relationship type not in taxonomy | Whole proposal |
| Endpoints not in canonical entity set | Whole proposal |

### 5.2 SAFE UNKNOWN representation (conceptual)

| Mechanism | Purpose |
|-----------|---------|
| **No canonical row** in slot | Default — absence is explicit in consumer contract |
| **UNKNOWN flag on slot** (metadata) | Operator-declared gap with reason |
| **proposed** candidates listed | Shows work-in-progress without canonical lie |

**Rule GV-U01:** SAFE UNKNOWN is **preferable** to a false canonical Relationship.

**Rule GV-U02:** Consumers must treat UNKNOWN as **first-class** — not as error to auto-heal.

### 5.3 UNKNOWN clearance

UNKNOWN clears only when:

1. Human attests **active** Relationship with evidence, **or**
2. Human confirms **no relationship** exists (document negative attestation), **or**
3. Entity merge/clarification completes (Identity Foundation).

---

## 6. Conflict resolution

### 6.1 Conflict types and playbooks

#### Unknown ownership

| Step | Action |
|------|--------|
| 1 | List **proposed** OWNS/OWNER candidates with evidence tier |
| 2 | Declare slot **SAFE UNKNOWN** for consumers |
| 3 | No **active** canonical until E1+ satisfied |
| 4 | On decision: one **active**, others **replaced** or rejected |

#### Conflicting client claims

| Step | Action |
|------|--------|
| 1 | Identify org pair and direction (A CLIENT_OF B vs B CLIENT_OF A) |
| 2 | Mark conflicting rows **disputed** |
| 3 | Verify commercial direction with evidence — not deal stage |
| 4 | Affirm one canonical CLIENT_OF; end other via supersession or reject |
| 5 | If relationship never existed → no canonical; archive proposals |

#### Multiple representatives

| Step | Action |
|------|--------|
| 1 | **Allowed:** multiple canonical REPRESENTATIVE if attested |
| 2 | **Dispute only when** authority claims are mutually exclusive (exclusive signatory) |
| 3 | Resolve with effective dates or scope notes — not “primary rep” CRM field |
| 4 | Do not collapse to single Person without evidence |

#### Disputed relationships (general)

| Step | Action |
|------|--------|
| 1 | Freeze canonical slot (no active) |
| 2 | Operator documents resolution outcome |
| 3 | Winner → **active**; losers → **replaced** / deprecated |
| 4 | Unresolvable → maintain **SAFE UNKNOWN** |

### 6.2 Escalation

| Level | Handler |
|-------|---------|
| L1 | Registry steward |
| L2 | Program owner |
| L3 | Amendment to governance doc / expansion rules — not silent override |

**Rule GV-C01:** Agents **must not** auto-resolve disputes.

### 6.3 Conflict resolution record (template)

```markdown
## Relationship conflict resolution
- **Date:**
- **Slot:** (type, subject_id, object_id)
- **Parties:** relationship_ids
- **Evidence reviewed:** E0/E1/E2/E3 refs
- **Decision:** affirm | reject | sequential | UNKNOWN
- **Outcome ids:**
- **Operator:**
```

---

## 7. Attestation and audit

### 7.1 Required attestation metadata (active canonical)

| Field | Required |
|-------|----------|
| `attested_by` | Yes — human identity reference |
| `attested_at` | Yes |
| `evidence_tier` | Yes |
| `evidence_ref` | If tier > E0 |
| `resolution_note` | If emerged from dispute |

### 7.2 Audit principles

| ID | Principle |
|----|-----------|
| **GA-01** | Every canonical state change traceable to human |
| **GA-02** | Supersession chain preserved |
| **GA-03** | UNKNOWN declarations logged with reason |
| **GA-04** | Consumer proposals never overwrite without review |

---

## 8. Consumer interaction governance

### 8.1 Read contract

Consumers **may read** canonical and deprecated/archived Relationships for historical joins.

Consumers **must**:

- Respect **SAFE UNKNOWN** slots.
- Not treat **proposed** / **disputed** as canonical.
- Reconcile cache after operator resolution.

### 8.2 Write contract (future)

| Allowed | Forbidden |
|---------|-----------|
| POST proposal | PUT active canonical |
| Flag dispute | Delete canonical history |
| Attach evidence_ref to proposal | Import CRM stage as type |

### 8.3 Consumer-specific notes

| Consumer | Typical proposals | ATLAS must not absorb |
|----------|-------------------|------------------------|
| **MIG** | Project/site/org links for session | SERP ownership |
| **ORCA** | Site ↔ project ↔ org | Campaign membership edges |
| **Website Factory** | BELONGS_TO, OWNS | Build state |
| **WPilot / OCPilot** | Domain ↔ website | CMS user roles |
| **HomeGateway** | Navigation labels only | Personal UX state |

---

## 9. Type and expansion governance

### 9.1 New relationship types

Follow [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md):

- Prefer new **type** over new **entity**.
- Boundary check against [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md).
- Taxonomy version bump (v1 → v2).

### 9.2 Forbidden governance shortcuts

| Shortcut | Why forbidden |
|----------|---------------|
| Map CRM stage → CLIENT_OF | Pipeline ≠ structure |
| Map WP user → EMPLOYEE | Ops account ≠ business Person |
| Auto-create CLIENT_OF from invoice | Accounting ≠ ATLAS |
| n8n unattended attest | Violates GV-01 |

---

## 10. PII and sensitivity

| Data | Governance |
|------|------------|
| Person name on Relationship | Inherited from entity — minimize duplication |
| Contact email in evidence | External reference preferred |
| Government ids in notes | **Forbidden** — boundary / security |
| Political / personal attributes | Out of scope |

---

## 11. Governance compliance checklist

- [ ] Creator role authorized for action?
- [ ] Evidence tier met for type?
- [ ] Canonical slot free or multiplicity allowed?
- [ ] Dispute resolved before active?
- [ ] UNKNOWN documented instead of guess?
- [ ] No CRM/HR/finance encoded?
- [ ] Resolution record filed for disputes?

---

## 12. Phase 2 governance deliverables

| Delivered | Not delivered |
|-----------|---------------|
| Roles and attestation rules | IAM / RBAC code |
| Evidence tiers | Document vault implementation |
| Conflict playbooks | Automated mediator |
| SAFE UNKNOWN policy | Consumer SDK |
| Escalation path | Ticketing integration |

---

*ATLAS Relationship Governance v1 — human supervision, evidence, conflict, UNKNOWN. Documentation only.*
