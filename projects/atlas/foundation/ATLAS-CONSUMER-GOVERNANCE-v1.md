# ATLAS Consumer Governance v1

**Status:** **documented** — Phase 6 normative governance for consumer adoption (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-CONSUMER-ADOPTION-MODEL-v1.md](ATLAS-CONSUMER-ADOPTION-MODEL-v1.md)  
**Integrates:** [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) · [ATLAS-LIFECYCLE-GOVERNANCE-v1.md](ATLAS-LIFECYCLE-GOVERNANCE-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md)  
**Is not:** ticketing system, RBAC implementation, SLA tables, legal dispute process.

**Phase 1–5 constraint:** No changes to approved Phase 1–5 documents unless contradictions are discovered. None identified at Phase 6 authoring.

---

## 1. Purpose

Define **consumer obligations**, **when to defer to ATLAS**, **when to challenge ATLAS**, **dispute handling**, and **attestation interaction** — the governance layer for adoption without duplicating steward/owner matrices in Phases 2–5.

---

## 2. Governance philosophy

| Principle | Statement |
|-----------|-----------|
| **Defer by default** | Attested ATLAS structure wins over consumer belief |
| **Challenge openly** | Disagreement uses flag/propose/dispute — not fork |
| **UNKNOWN is honest** | Better than invented canonical |
| **Humans attest** | Consumers never promote to **active** alone |
| **Separation of domains** | Ops approval ≠ structural attestation |

---

## 3. Consumer obligations

### 3.1 Standing obligations

| Obl ID | Obligation | Source |
|--------|------------|--------|
| **CG-O01** | Maintain adoption owner contact | Adoption Model CA-R07 |
| **CG-O02** | Publish mapping table | Mapping Rules §2 |
| **CG-O03** | Comply with Semantic Contract SC-* | Semantic Contract |
| **CG-O04** | Honor Phase 4 interaction prohibitions | Consumer Contracts |
| **CG-O05** | Report suspected parallel registry | CG-O05 trigger → §6 |
| **CG-O06** | Remediate certified gap before production reliance (C2+) | Certification |

### 3.2 Event-triggered obligations

| Event | Consumer must |
|-------|---------------|
| ATLAS id **merged** | Remap foreign keys to survivor; stop using loser forward |
| Relationship **replaced** | Point to successor `relationship_id` |
| Slot → **disputed** | Halt forward structural automation |
| Attestation rejected | Remove canonical reliance; keep local ops if needed |
| Governance notifies vocabulary change | Update mapping + re-certify |

---

## 4. When consumers must defer to ATLAS

**Defer** = treat ATLAS as authoritative for the decision class; consumer updates local state or waits.

| Condition | Defer on | Consumer action |
|-----------|----------|-----------------|
| ATLAS **active** + C-01–C-06 | Entity existence, id, attested relationships | Use ATLAS id; align labels |
| **merged** with `redirect_to` | Identity pointer | Resolve survivor |
| **replaced** with `replaced_by` | Current structural edge | Use successor |
| Attested **OWNER** / **CLIENT_OF** | Structural role | Do not infer alternate type locally |
| Steward declares slot **SAFE UNKNOWN** | Whether canonical exists | Do not invent id |
| Post-dispute resolution | Winning record | Abandon loser canonical assumptions |

**Rule CG-D01:** Defer does **not** require deferring on operational facts (task status, spend, content).

**Rule CG-D02:** Defer applies even when consumer “has always used” a local name — governance may require remap.

---

## 5. When consumers may challenge ATLAS

**Challenge** = structured disagreement without creating parallel canonical truth.

| Challenge type | Who may initiate | Channel (conceptual) | ATLAS response |
|----------------|------------------|----------------------|----------------|
| **Dispute flag** | Consumer adoption owner | Intake / dispute flag | **disputed** on record or slot |
| **Correction proposal** | Any authorized proposer | Suggest / propose | **proposed** competitor or correction |
| **Evidence upgrade** | Consumer with new E-tier evidence | Proposal + evidence ref | Steward review |
| **Duplicate suspicion** | Consumer | Proposal; steward merge | **merged** workflow |
| **Boundary violation report** | Consumer | Governance incident | Reject or deprecate |

**Rule CG-C01:** Challenge **must include** evidence ref or reproducible rationale — not opinion alone.

**Rule CG-C02:** During challenge, consumer **must not** publish alternate canonical ids externally.

**Rule CG-C03:** Challenge authority for lifecycle transitions remains **owner/steward** ([ATLAS-LIFECYCLE-GOVERNANCE-v1.md](ATLAS-LIFECYCLE-GOVERNANCE-v1.md)); consumers have **flag** authority only.

### 5.1 Challenge vs operational disagreement

| Topic | Challenge ATLAS? |
|-------|------------------|
| Wrong **CLIENT_OF** direction | **Yes** |
| WPilot plugin version mismatch | **No** — ops |
| SERP ranking differs from expectation | **No** — market |
| Invoice amount wrong | **No** — finance consumer |
| Org merge should have happened | **Yes** — identity governance |

---

## 6. When consumers must remain SAFE UNKNOWN

| Situation | Required posture |
|-----------|------------------|
| No **active** canonical for required subject | **SAFE UNKNOWN** |
| **disputed** unresolved | UNKNOWN for slot — no forward canonical |
| Import ambiguous duplicate | UNKNOWN until steward decision |
| Market-only competitor identity | UNKNOWN for business existence |
| Consumer cache empty / error | UNKNOWN — not license to invent |
| Attestation pending (**proposed**) | UNKNOWN for forward canonical — optional risk flag |

**Rule CG-U01:** UNKNOWN must be **visible** in operator UX and export metadata.

**Rule CG-U02:** UNKNOWN duration does not justify **M-BAN** mapping violations (Mapping Rules).

---

## 7. Dispute handling

### 7.1 Dispute lifecycle (consumer view)

```text
Consumer detects conflict
  → Classify: structural (ATLAS) vs operational (local)
  → If structural: dispute flag OR proposal
  → ATLAS marks disputed / holds promotion
  → Steward/owner resolves (Lifecycle Governance)
  → Consumer receives outcome: active winner | deprecated | merged | UNKNOWN
  → Consumer remaps foreign keys / mapping table
```

### 7.2 Consumer dispute responsibilities

| Phase | Responsibility |
|-------|----------------|
| Detection | Log conflict source (cache, import, operator) |
| Flagging | Submit dispute within agreed intake (future) |
| Freeze | Stop auto-promotion scripts |
| Resolution support | Supply evidence; do not lobby by parallel registry |
| Post-resolution | Execute remap within consumer-defined SLA (local) |

### 7.3 Multi-consumer disputes

When Consumer A attested view conflicts with Consumer B local assumption:

- **ATLAS record state** is sole structural arbiter.
- Both consumers adjust to outcome; neither maintains “winning” canonical fork.

---

## 8. Attestation interaction

Consumers interact with attestation **only** at observation/proposal boundary:

| Consumer role | Attestation interaction |
|---------------|-------------------------|
| Observe | Import, SERP, CRM → evidence refs |
| Propose | Create **proposed** records |
| Review support | Supply notes — **not** attest |
| Attest | **Forbidden** for consumers |

**Rule CG-A01:** Consumer “approval” buttons (deal won, deploy approved) **must not** call ATLAS attest.

**Rule CG-A02:** Attestation outcomes consumers must interpret: §7 Semantic Contract SC-A*.

### 8.1 Evidence handoff

| Evidence source | Use in ATLAS |
|-----------------|--------------|
| Consumer foreign key | E3 corroboration — still needs human |
| MIG SERP pack | Market — proposal support only |
| Signed contract PDF | E2 — stored by doc consumer; ref in ATLAS |
| Operator knowledge | E0 — steward attest |

---

## 9. Escalation paths

| Severity | Example | Escalate to |
|----------|---------|-------------|
| **S0** | Display label mismatch | Consumer adoption owner |
| **S1** | Mapping table error | Consumer + steward notify |
| **S2** | Repeated UNKNOWN blocking production | Steward + program owner |
| **S3** | Suspected parallel registry | Program owner + change governance |
| **S4** | Semantic Contract violation in automation | Program owner; block integration |
| **S5** | Vocabulary / boundary change needed | Change governance S4–S5 |

Aligns with [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) severity classes where applicable.

### 9.1 Escalation diagram

```text
Consumer adoption owner
        │
        ▼
Registry steward ──► Program owner (ATLAS)
        │
        ▼
Change governance (vocabulary / expansion)
```

---

## 10. Conflict resolution (canonical vs local)

When consumer data conflicts with ATLAS ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) §8.3):

| Step | Action |
|------|--------|
| 1 | Identify conflict class (identity · relationship · lifecycle · name) |
| 2 | Fetch current ATLAS posture (not stale cache if avoidable) |
| 3 | If **active** attested → consumer corrects local |
| 4 | If **disputed** / UNKNOWN → consumer freezes forward use |
| 5 | If consumer has new evidence → proposal/challenge |
| 6 | Document incident if auto-sync caused user-visible error |

**Rule CG-R01:** No batch auto-merge across consumer and ATLAS datasets.

---

## 11. Violations and remediation

| Violation | Detection | Remediation |
|-----------|-----------|-------------|
| Parallel canonical registry | Audit / certification | Merge plan; block C2+ |
| Auto-attest | CI rule / audit | Disable path; S4 escalation |
| MAP-B01 completed→deprecated | Mapping audit | Fix table; replay proposals |
| Ignored **merged** redirect | Broken references | Remap keys |
| Business Scope partition | Schema/charter review | Remove partition key |

Certification downgrade: [ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md) §6.

---

## 12. Non-deliverables

No ticket queues, webhook specs, or steward SLA numbers.

---

*ATLAS Consumer Governance v1 — Phase 6 Foundation. Documentation only.*
