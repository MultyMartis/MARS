# ATLAS Lifecycle Transitions v1

**Status:** **documented** — Phase 5 normative transition rules.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-LIFECYCLE-MODEL-v1.md](ATLAS-LIFECYCLE-MODEL-v1.md) · [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md)  
**Companion:** [ATLAS-LIFECYCLE-GOVERNANCE-v1.md](ATLAS-LIFECYCLE-GOVERNANCE-v1.md)  
**Is not:** workflow BPMN, state machine code, event bus schema.

---

## 1. Purpose

Define **valid and invalid state transitions**, **human review requirements**, **attestation requirements**, and **rollback principles** for all ATLAS registry records — unifying Phase 2 relationship transitions, Phase 3 identity events, and Phase 4 entity registry intake flows.

---

## 2. Transition philosophy

| Principle | Rule |
|-----------|------|
| **Forward promotion is attested** | proposed → active always requires human attestation |
| **Demotion is explicit** | active → * never silent; audit note required |
| **Dispute blocks** | No active in contested slot until resolution |
| **Supersession is additive** | New relationship id for **replaced**; no in-place canonical mutate |
| **Merge is terminal for loser** | merged id does not return to active |
| **Archive is structural lock** | archived → active forbidden except owner error path |

---

## 3. Core transition catalog

### 3.1 Intake and promotion

| Transition | Valid? | Human review | Attestation | Notes |
|------------|--------|--------------|-------------|-------|
| (create) → **proposed** | Yes | Steward intake | Optional E0 | Default intake |
| (create) → **active** | Yes* | Steward | **Required** | *Direct attested create only |
| **proposed** → **active** | Yes | Steward / owner | **Required** | Canonical promotion |
| **proposed** → **disputed** | Yes | Steward | Flag note | Competing proposals |
| **proposed** → **archived** | Yes | Steward | Reject note | Rejected candidate |
| **proposed** → (delete) | Yes† | Steward | — | †Never attested; non-canonical cleanup |
| **proposed** → **deprecated** | **No** | — | — | Must promote or reject |

### 3.2 Active maintenance

| Transition | Valid? | Human review | Attestation | Notes |
|------------|--------|--------------|-------------|-------|
| **active** → **active** | N/A | — | — | Metadata/alias amend — not a lifecycle transition |
| **active** → **disputed** | Yes | Steward / owner | Flag | Record or slot contest |
| **active** → **deprecated** | Yes | Steward | Required | Structural end |
| **active** → **archived** | Discouraged | Steward | Required | Prefer deprecated → archived |
| **active** → **proposed** | **No** | — | — | Demotion forbidden |
| **active** → **merged** | Yes | Owner / delegated | E1+ (E2 org) | Loser only; survivor stays active |
| **active** → **split_source** | Yes | **Owner only** | E2+ | Source id; children active |

### 3.3 Dispute resolution

| Transition | Valid? | Human review | Attestation | Notes |
|------------|--------|--------------|-------------|-------|
| **disputed** → **active** | Yes | Owner / steward | Resolution attest | Winner only |
| **disputed** → **deprecated** | Yes | Steward | Resolution | Losers / rejected |
| **disputed** → **merged** | Yes | Owner | Merge path | Duplicate resolution |
| **disputed** → **replaced** | Yes | Steward | Supersession | Relationship slot |
| **disputed** → **archived** | Yes | Steward | Reject path | Non-contenders |
| **disputed** → (SAFE UNKNOWN) | Yes | Owner / steward | Explicit declare | Neither affirmed |
| **disputed** → **disputed** | N/A | — | — | Await evidence |

**Rule LT-D01:** Resolution must not leave two **active** canonical records for same subject/slot.

### 3.4 Historical and terminal

| Transition | Valid? | Human review | Attestation | Notes |
|------------|--------|--------------|-------------|-------|
| **deprecated** → **archived** | Yes | Steward | Optional | Cooling policy |
| **deprecated** → **active** | Yes‡ | Owner / steward | **Required** | ‡Reactivation — wrongly ended |
| **replaced** → **archived** | Yes | Steward | Optional | Relationship history |
| **merged** → **active** | **No** | — | — | Use survivor id |
| **merged** → **deprecated** | Yes§ | **Owner only** | Audit | §Governance error correction |
| **split_source** → **active** | **No** | — | — | Use child ids |
| **archived** → **active** | **No** | — | — | Use § error path via deprecated |
| **archived** → **deprecated** | Yes§ | **Owner only** | Audit | Un-archive for correction |

---

## 4. Relationship-specific transitions

Aligned with [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md); Phase 5 names only.

### 4.1 Supersession path

```text
Relationship A [active]
    → create Relationship B [proposed]
    → attest B [active]
    → A [replaced], replaced_by = B
```

| Transition | Valid? | Attestation |
|------------|--------|-------------|
| **active** → **replaced** | Yes | Supersession attest |
| **replaced** → **active** | **No** | Create successor instead |
| **replaced** → **deprecated** | Discouraged | Pick one terminal pattern |
| **replaced** → **archived** | Yes | After cooling |

### 4.2 End without supersession

```text
active → deprecated (+ effective_to)
optional: type → FORMER_* per taxonomy
optional later: deprecated → archived
```

### 4.3 Disputed slot (relationship)

| Transition | Valid? |
|------------|--------|
| Two **proposed** → both **disputed** | Yes |
| One **active** + competitor **proposed** | Active → **disputed** or deprecate active pending review |
| Resolution → one **active**, others **replaced** / **deprecated** | Yes |

---

## 5. Entity-specific transitions

### 5.1 Merge path

```text
Org A [active] + Org B [active]  (duplicate — forbidden steady state)
  → dispute or freeze B
  → merge attest
  → A [active] survivor, B [merged] redirect_to=A
```

| Transition | Valid? |
|------------|--------|
| **active** + **active** same subject | **Forbidden** steady state — resolve to merge or separate |
| Loser **active** → **merged** | Yes |
| Survivor **active** → **merged** | **No** |

### 5.2 Split path

```text
Entity S [active]
  → owner-approved split
  → S [split_source]
  → new C1, C2 [active] with documented lineage
```

### 5.3 Project closure (not “Completed”)

| Consumer says | ATLAS transition |
|---------------|------------------|
| “Project completed” | **active** → **deprecated** (structural retire) |
| “Project cancelled before start” | **proposed** reject or **active** → **deprecated** |

**Rule LT-P01:** No `completed` lifecycle code.

---

## 6. Invalid transitions (global forbid list)

| From | To | Rule ID |
|------|-----|---------|
| **merged** | **active** | LT-X01 |
| **replaced** | **active** | LT-X02 |
| **archived** | **active** | LT-X03 |
| **archived** | **proposed** | LT-X04 |
| **proposed** | **deprecated** | LT-X05 |
| **proposed** | **merged** | LT-X06 |
| **proposed** | **replaced** | LT-X07 |
| **active** | **proposed** | LT-X08 |
| Any canonical | (hard delete) | LT-X09 |
| **disputed** | **active** (losers) | LT-X10 — only winner |

---

## 7. Human review requirements

| Transition class | Minimum reviewer | Owner required? |
|------------------|------------------|-----------------|
| proposed → active (routine) | Steward (delegated) | No |
| proposed → active (S2 identity) | Steward | Merge-adjacent: Yes |
| active → disputed | Steward | No (escalate if high impact) |
| disputed → active | Steward | If slot/systemic: Yes |
| active → deprecated (routine end) | Steward | No |
| Merge (→ merged) | Steward propose | **Yes** approve |
| Split (→ split_source) | Steward propose | **Yes** only |
| archived error correction | — | **Yes** |
| deprecated → active reactivation | Steward propose | **Yes** |
| Relationship supersession | Steward | Delegated OK |
| SAFE UNKNOWN declaration | Steward | Owner if ecosystem-wide |

Aligns with [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) §4 severity table.

---

## 8. Attestation requirements

| Transition | Evidence tier (minimum) | Attestation block |
|------------|-------------------------|-------------------|
| proposed → active | E0 routine; E1 org/person; E2 merge-adjacent | **Required** |
| direct create → active | Per entity rules | **Required** |
| active → deprecated | E0 + note | **Required** |
| active → disputed | E0 flag | Note required |
| disputed → active | E1+ | Resolution attest |
| merge → merged | E1; E2 legal org merge | **Required** |
| split → split_source | E2 | Owner attest |
| supersede → replaced | E1 | **Required** |
| → archived | E0 | Optional |
| import batch proposed | E3 import | **No** auto-active ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) AT-IMP-01) |

**Rule LT-AT-01:** Lifecycle transition without attest trail is **non-compliant**.

**Rule LT-AT-02:** Attestation records **why**; lifecycle records **what state**.

---

## 9. Rollback principles

### 9.1 What “rollback” means in ATLAS

ATLAS does **not** roll back business history. It **corrects registry posture** with audit.

| Situation | Allowed correction | Forbidden |
|-----------|-------------------|-----------|
| Wrong proposed promotion | Deprecate or dispute; never delete if attested | Silent delete |
| Wrong active canonical | Supersede (relationship) or merge fix (entity) | In-place id recycle |
| Wrong merge | Owner governance reversal — new attest; may re-split ids | merged → active on absorbed id |
| Wrong archive | archived → deprecated (owner) → re-attest → active | Direct archived → active |
| Consumer bad write | Reject; ATLAS wins on reconcile | Consumer overrides ATLAS state |

### 9.2 Rollback vs operational undo

| Operational undo | ATLAS response |
|------------------|----------------|
| “Undo deploy” | Consumer-local — Website entity stays **active** unless site retired |
| “Reopen ticket” | No ATLAS transition |
| “Restore CRM account” | Map to existing ATLAS id — no new canonical without attest |

### 9.3 Reconciliation order

1. Freeze conflicting **active** claims.  
2. Mark **disputed** or declare **SAFE UNKNOWN**.  
3. Apply supersession / merge with new ids as required.  
4. Publish attest notes + consumer redirect guidance.

---

## 10. Transition diagrams

### 10.1 Entity (core)

```text
                    ┌──────────┐
         create ──► │ proposed │
                    └────┬─────┘
                         │ attest
                         ▼
                    ┌──────────┐     dispute      ┌──────────┐
                    │  active  │ ─────────────► │ disputed │
                    └────┬─────┘                └────┬─────┘
           merge/split   │    deprecate            │ resolve
                         ▼                           │
              ┌──────────────────────┐               │
              │ deprecated / merged /│◄──────────────┘
              │ split_source         │
              └──────────┬───────────┘
                         │ archive
                         ▼
                    ┌──────────┐
                    │ archived │
                    └──────────┘
```

### 10.2 Relationship (core + replaced)

```text
proposed ──► active ──► deprecated ──► archived
              │              ▲
              │ supersede    │
              ▼              │
           replaced ─────────┘
              │
              └──► archived

active ──► disputed ──► (resolve) ──► active | replaced | SAFE UNKNOWN
```

---

## 11. Examples (illustrative)

### 11.1 PROPOSED → ACTIVE (new Organization)

1. Consumer import creates `ORG-*` **proposed** (E3).  
2. Steward verifies boundary + duplicate check.  
3. Attestation recorded (E1).  
4. Transition **proposed** → **active**.  
5. MIG/ORCA may use id for structural reference.

### 11.2 ACTIVE → DISPUTED → ACTIVE (ownership)

1. Two **proposed** OWNER edges for Domain D.  
2. Both → **disputed**; slot has no **active** OWNER → SAFE UNKNOWN for default join.  
3. Owner resolves: Org A edge → **active**; Org B → **replaced** or rejected **proposed**.

### 11.3 ACTIVE → DEPRECATED (project structural close)

1. Initiative ends — not a task board “Done”.  
2. **active** → **deprecated** with attest note.  
3. Websites and orgs remain **active** ([ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md) ER-LC-02).

### 11.4 MERGED → ? (absorbed org)

- **merged** is **terminal** for absorbed `ORG-B`.  
- Consumers use `ORG-A` **active**.  
- **merged** → **active** is **invalid** (LT-X01).

### 11.5 ARCHIVED → ? 

- **archived** → **active** **invalid** (LT-X03).  
- Error: **archived** → **deprecated** (owner) → re-attest → **active** if business subject truly still current.

---

## 12. Compliance checklist

- [ ] Transition listed in §3–§5?
- [ ] Not in forbidden §6 list?
- [ ] Attestation tier meets §8?
- [ ] Reviewer role meets §7?
- [ ] Rollback follows §9 (no merged→active)?

---

*ATLAS Lifecycle Transitions v1 — transition rules. Documentation only.*
