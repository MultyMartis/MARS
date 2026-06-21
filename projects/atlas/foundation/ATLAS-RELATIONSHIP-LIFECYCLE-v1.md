# ATLAS Relationship Lifecycle v1

**Status:** **documented** — Phase 2 normative lifecycle for Relationship records.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** workflow engine, state machine implementation, cron jobs, automated expiry.

---

## 1. Purpose

Define **how a Relationship comes into being, remains authoritative, changes, ends, or enters dispute** — with **effective dates**, **historical preservation**, and **supersession** — without CRM concepts (deals, stages, win/loss) or HR offboarding workflows.

---

## 2. Lifecycle states

### 2.1 State overview

| State | Canonical? | Meaning |
|-------|------------|---------|
| **proposed** | No | Candidate link awaiting human attestation |
| **active** | Yes | Current structural truth for its slot (subject to effective dates) |
| **deprecated** | Yes (historical) | Link ended or downgraded; retained for audit; not used for forward default |
| **replaced** | Yes (historical) | Superseded by another `relationship_id`; pointer required |
| **disputed** | No | Competing claims; blocks canonical promotion |
| **archived** | Yes (read-only) | Long-term storage; no edits except metadata correction |

```text
                    ┌──────────┐
         create ──► │ proposed │
                    └────┬─────┘
                         │ attest
                         ▼
                    ┌──────────┐     dispute      ┌──────────┐
                    │  active  │ ─────────────► │ disputed │
                    └────┬─────┘                └────┬─────┘
           end / supersede │                         │ resolve
                         ▼                           │
              ┌──────────────────────┐                 │
              │ deprecated /       │◄────────────────┘
              │ replaced / archived  │
              └──────────────────────┘
```

### 2.2 State definitions

#### proposed

| Attribute | Rule |
|-----------|------|
| **Entry** | Human or consumer creates candidate Relationship |
| **Canonical** | **Never** |
| **Editable** | Type, endpoints, dates, evidence notes |
| **Exit** | Attest → **active**; reject → delete proposal (non-canonical only) or **archived** stub |

#### active

| Attribute | Rule |
|-----------|------|
| **Entry** | Human attestation from **proposed**, or direct attested create |
| **Canonical** | **Yes** (subject to slot rules) |
| **Meaning** | “This is the business graph truth for this link now” |
| **Exit** | End date reached, supersession, dispute escalation, or explicit deprecate |

#### deprecated

| Attribute | Rule |
|-----------|------|
| **Entry** | Link no longer authoritative but **history required** |
| **Canonical** | **Yes** as historical fact |
| **Use** | Queries about past structure; not default forward joins |
| **Exit** | **archived** after cooling period (policy); or remain deprecated indefinitely |

#### replaced

| Attribute | Rule |
|-----------|------|
| **Entry** | New Relationship supersedes this one (type change, endpoint fix, ownership transfer) |
| **Required** | `replaced_by` → successor `relationship_id` |
| **Canonical** | Historical only |
| **Pairing** | Successor typically **active** |

#### disputed

| Attribute | Rule |
|-----------|------|
| **Entry** | Conflicting evidence or competing proposals |
| **Canonical** | **Never** |
| **Coexistence** | Multiple **disputed** rows may reference same slot |
| **Exit** | Human resolution → one **active**, others **replaced** or rejected |

#### archived

| Attribute | Rule |
|-----------|------|
| **Entry** | Deprecated/replaced records aged out of active review surfaces |
| **Canonical** | Read-only historical |
| **Edits** | Metadata correction only (typo in dates with audit note) — not type/endpoint change |

---

## 3. Creation

### 3.1 Creation paths

| Path | Initial state | Canonical |
|------|---------------|-----------|
| **Direct attested create** | active | Yes (if slot free) |
| **Propose then attest** | proposed → active | After attestation |
| **Consumer import proposal** | proposed | After human promotion (future) |
| **Uncertain intake** | proposed or no record | **SAFE UNKNOWN** if type/endpoints unknown |

### 3.2 Minimum creation fields (conceptual)

| Field | Required |
|-------|----------|
| `relationship_type` | Yes — from taxonomy |
| `subject_id` | Yes |
| `object_id` | Yes |
| `lifecycle_state` | Yes |
| `effective_from` | Yes for **active** canonical (may default to attestation date) |
| `effective_to` | No until end |
| `attested_by` | Yes for **active** (human reference) |
| `attested_at` | Yes for **active** |
| `evidence_ref` | Per governance tier |

### 3.3 Creation prohibitions

| Prohibition | Rule ID |
|-------------|---------|
| Auto-promote import to **active** without human | LC-P01 |
| Create canonical with unknown endpoints | LC-P02 |
| Create Organization to satisfy Relationship | LC-P03 (RR-07) |

---

## 4. Active phase

### 4.1 Authority

While **active** and within effective window, the Relationship is the **default structural truth** for consumers unless:

- governance marks **disputed** on parallel candidates,
- consumer cache is stale (reconcile to ATLAS),
- **SAFE UNKNOWN** declared for the slot (no active row).

### 4.2 Amendments while active

| Change kind | Treatment |
|-------------|-----------|
| Typo in notes | Light correction with audit |
| Wrong type | **Supersession** — new Relationship, old → **replaced** |
| Wrong endpoint | **Supersession** |
| Extend `effective_to` | Amend with attestation |
| “Upgrade” CLIENT_OF to deal won | **Forbidden** — CRM event, not lifecycle |

### 4.3 Parallel active multiplicity

Allowed **only** when taxonomy permits (e.g. multiple OWNER, multiple REPRESENTATIVE). **Forbidden** for singleton slots (PRIMARY_DOMAIN) unless dispute resolution pending.

---

## 5. Deprecation

### 5.1 When to deprecate

| Trigger | Example |
|---------|---------|
| Business link ended | Client engagement ended |
| Role ended | Contractor engagement complete |
| Domain parked | PRIMARY_DOMAIN removed; site inactive |
| Correction path | Wrong canonical promoted — deprecate after supersession |

### 5.2 Deprecation mechanics

1. Set `effective_to` (if not already set).
2. Transition state **active** → **deprecated**.
3. **Optional:** migrate type to **FORMER_*** (e.g. CLIENT_OF → FORMER_CLIENT_OF) per [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md).

**Rule LC-D01:** Deprecation **never** deletes the row.

### 5.3 Deprecated vs FORMER_* type

| Approach | When to use |
|----------|-------------|
| **deprecated** state only | Type unchanged; end visible via state + dates |
| **FORMER_* type** | Human clarity in exports (“former client”) |
| **Both** | Allowed if attested — avoid duplicate canonical slots |

---

## 6. Replacement and supersession

### 6.1 Supersession model

**Supersession** creates a **new** Relationship (`relationship_id` B) and marks predecessor A as **replaced**:

```text
A: OWNER, active, effective 2020-01 → 2025-12
   state → replaced, replaced_by = B

B: OWNER, active, effective 2026-01 → (open)
```

### 6.2 Type migration supersession

| From | To | Example |
|------|-----|---------|
| CLIENT_OF | FORMER_CLIENT_OF | A deprecated/migrated; B may be new CLIENT_OF for different org |
| OWNER | FORMER_OWNER | Ownership transfer |
| EMPLOYEE | FORMER_EMPLOYEE | Role ended |

**Rule LC-S01:** Do not mutate canonical **active** type in place when the **semantic role changed** — supersede.

### 6.3 Slot handoff

When two parties compete for singleton slot (PRIMARY_DOMAIN):

1. Winner → **active** (or remains).
2. Loser → **replaced** or **deprecated** with `effective_to`.
3. Disputed losers → remain **disputed**, not canonical.

---

## 7. Disputed phase

### 7.1 Entry conditions

| Condition | Example |
|-----------|---------|
| Dual canonical claim | Two imports assert CLIENT_OF same pair |
| Ownership unclear | Two orgs OWNS same domain |
| Representative overlap | Conflicting authority claims (not automatically dispute — human flag) |
| Consumer ≠ ATLAS | CRM client flag conflicts with registry |

### 7.2 Disputed handling

| Rule | Detail |
|------|--------|
| **LC-DP01** | **disputed** records are visible in review queues |
| **LC-DP02** | No **active** canonical in same slot until resolved |
| **LC-DP03** | Resolution documented in governance log |
| **LC-DP04** | Resolution is structural, not commercial adjudication |

### 7.3 Exit from disputed

| Outcome | Result |
|---------|--------|
| **Affirm A** | A → **active**; B → **replaced** or rejected proposal |
| **Affirm B** | B → **active**; A → **replaced** |
| **Neither** | Both remain deprecated/rejected; slot → **SAFE UNKNOWN** |
| **Split by time** | Sequential **active** windows if evidence supports non-overlap |

---

## 8. Archive

### 8.1 Purpose

Reduce operator noise while **preserving** legal and historical audit.

### 8.2 Archive rules

| Rule | Detail |
|------|--------|
| **LC-A01** | **archived** is terminal for structural edits |
| **LC-A02** | Archived rows participate in historical queries |
| **LC-A03** | Archive does not imply “never existed” — tombstone language forbidden |
| **LC-A04** | Minimum metadata: type, endpoints, effective range, attestation |

---

## 9. Effective dates

### 9.1 Definitions

| Field | Semantics |
|-------|-----------|
| **effective_from** | First instant the structural link is **true in business terms** |
| **effective_to** | Last instant the link is **true**; null = open-ended |
| **attested_at** | When a human confirmed the record (may differ from effective_from) |
| **record_updated_at** | System audit (implementation future) |

### 9.2 Rules

| Rule ID | Rule |
|---------|--------|
| **LC-E01** | `effective_to` ≥ `effective_from` when both set |
| **LC-E02** | Overlapping canonical slots must not violate RR-04 |
| **LC-E03** | Backdated `effective_from` allowed with evidence and attestation note |
| **LC-E04** | Future-dated `effective_from` allowed for known upcoming transfers |
| **LC-E05** | Open-ended past links use null `effective_to` until ended |

### 9.3 Historical queries (intent)

Consumers asking “who was CLIENT_OF B in 2023?” filter:

- `lifecycle_state` ∈ { active, deprecated, replaced, archived }
- `effective_from` ≤ 2023-12-31
- `effective_to` is null OR `effective_to` ≥ 2023-01-01

Exact query logic is implementation — semantics are normative here.

---

## 10. Historical preservation

### 10.1 Principles

| ID | Principle |
|----|-----------|
| **HP-01** | No silent delete of canonical Relationships |
| **HP-02** | Ended links remain addressable by `relationship_id` |
| **HP-03** | Supersession chain walkable via `replaced_by` |
| **HP-04** | FORMER_* types optional but encouraged for exports |
| **HP-05** | Merged entities retain Relationship history with redirect notes (Identity Foundation future) |

### 10.2 What “delete” means

| Action | Allowed? |
|--------|----------|
| Delete **proposed** never attested | Yes — non-canonical cleanup |
| Delete **active** canonical | **No** — deprecate/archive |
| Purge from backups | Out of scope — ops policy |

---

## 11. Lifecycle examples (illustrative)

### 11.1 Client relationship ends

```text
1. Organization(A) ──CLIENT_OF──► Organization(B)   [active, 2020–2025]
2. Set effective_to = 2025-12-31
3. State → deprecated OR type → FORMER_CLIENT_OF
4. No new CLIENT_OF unless re-engagement attested
```

### 11.2 Ownership transfer

```text
1. Person(P) ──OWNER──► Organization(X)   [active until 2025-06]
2. Supersede: new Person(Q) ──OWNER──► Organization(X)   [active from 2025-07]
3. Old row: replaced, replaced_by = new id
4. Optional: old type → FORMER_OWNER
```

### 11.3 Unknown ownership (no active row)

```text
1. Two proposed OWNS edges for Domain D → Org A, Org B
2. Mark both disputed OR leave proposed
3. Slot has no active canonical → SAFE UNKNOWN for consumers
4. Human attests Org A → one active; Org B proposal → replaced/rejected
```

---

## 12. CRM / HR concept ban in lifecycle

Lifecycle states **must not** include: Lead, Opportunity, Won, Lost, Onboarding, PerformanceReview, TerminationPayroll.

| CRM/HR term | ATLAS lifecycle equivalent |
|-------------|---------------------------|
| Deal closed-lost | CLIENT_OF ended → deprecated / FORMER_CLIENT_OF |
| Employee terminated | EMPLOYEE ended → FORMER_EMPLOYEE |
| Churn | No churn score — structural end only |

---

## 13. Compliance checklist

- [ ] State transition documented for package?
- [ ] Effective dates specified for active canonical?
- [ ] Supersession uses new `relationship_id`?
- [ ] Disputed rows blocked from canonical?
- [ ] FORMER_* or deprecated used instead of delete?
- [ ] No pipeline stage encoded in lifecycle?

---

*ATLAS Relationship Lifecycle v1 — states, dates, supersession. Documentation only.*
