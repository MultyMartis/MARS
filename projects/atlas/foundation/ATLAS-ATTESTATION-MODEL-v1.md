# ATLAS Attestation Model v1

**Status:** **documented** — Phase 4 canonical trust model for business reality.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) · [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) · [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md)  
**Is not:** evidence storage system, document management, e-signature platform, ML confidence scorer, automated trust engine.

**Phase 1–3 constraint:** No changes to approved Phase 1–3 documents unless contradictions are discovered. None identified at Phase 4 authoring.

---

## 1. Purpose

Define **how business reality becomes canonical** in ATLAS — the trust model binding evidence, human roles, review, and uncertainty. This document is the **authoritative attestation contract** for all entity and relationship registries.

**Normative statement:**

> Nothing is **canonical business reality** in ATLAS until a **qualified human** attests it under **documented evidence discipline**; uncertainty remains **SAFE UNKNOWN**, never silent invention.

---

## 2. Attestation philosophy

### 2.1 Reality is claimed, then attested

| Stage | Meaning |
|-------|---------|
| **Observation** | Someone notices a fact (intake, import, consumer flag) |
| **Proposal** | Fact recorded as **non-canonical** proposed state |
| **Evidence** | Pointers and notes supporting the claim |
| **Review** | Steward or owner evaluates claim vs boundaries |
| **Attestation** | Human affirms canonical promotion |
| **Canonical** | Active record trusted for cross-consumer reference |

Machines and consumers may accelerate **observation** and **proposal**; they **cannot** replace **attestation**.

### 2.2 Attestation ≠ operational approval

Attesting “Organization X exists” is **not** approving a contract, invoice, or campaign. Operational approvals stay in consumer systems ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) RA-D08).

---

## 3. Evidence

### 3.1 What evidence is

**Evidence** is **information that supports a structural claim** — sufficient for a human to defend canonical promotion. Evidence is **referenced**, not necessarily **stored in full** in ATLAS.

### 3.2 Evidence tiers (unified)

Aligned with [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §3.1 — applied to **all** registry promotions:

| Tier | Description | Typical use |
|------|-------------|-------------|
| **E0 — Internal attestation** | Operator/steward already knows fact from trusted context | Direct owner attest (low-risk structural facts) |
| **E1 — Informal document** | Email, chat export, letter scan reference | CLIENT_OF, EMPLOYEE, many aliases |
| **E2 — Formal document** | Contract extract, registrar record, corporate registry | OWNER, OWNS, legal org merge |
| **E3 — System corroboration** | Consumer foreign key, API snapshot reference | Import triage — still requires human promote |

### 3.3 Evidence rules

| Rule ID | Rule |
|---------|------|
| **AT-E-01** | Higher-risk claims require **higher minimum tier** (see §4.3) |
| **AT-E-02** | Evidence may be `evidence_ref` + short note — not full contract body in ATLAS |
| **AT-E-03** | MIG SERP packs are **market evidence** — may support **proposal** but do not auto-attest org/site existence |
| **AT-E-04** | Absence of evidence blocks promotion → **SAFE UNKNOWN** or remain **proposed** |
| **AT-E-05** | Fabricated evidence tier is a **governance violation** |

### 3.4 What is not evidence for ATLAS

| Artifact | Treatment |
|----------|-----------|
| CRM pipeline stage | Consumer-local |
| Analytics traffic spike | Consumer-local |
| Agent hallucinated org name | Reject — not evidence |
| “Needed for export” urgency | Not evidence |

---

## 4. Attestation

### 4.1 Attestation act

**Attestation** is a **recorded human decision** that:

1. A proposed fact is **structurally true** within ATLAS boundaries;
2. The record may enter **active canonical** state;
3. Assigned evidence tier is **accepted**;
4. Identity and relationship impacts were **considered**.

Attestation should capture (conceptually): **attestor role**, **timestamp**, **evidence tier**, **short rationale**.

### 4.2 Minimum attestation for promotion

| Target | Minimum attestor | Notes |
|--------|------------------|-------|
| Entity → active | Steward (delegated) or Owner | Per [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) |
| Relationship → active | Steward or Owner | Per [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) GV-01 |
| Merge | Owner or delegated steward | Evidence reviewed |
| Split | **Owner only** | IGV-S01 |
| Alias → attested canonical use | Steward or Owner | [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md) |
| Expansion (new type/field) | Program owner | [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) |

### 4.3 Risk-based minimum evidence at attestation

| Claim category | Minimum tier at attest |
|----------------|------------------------|
| New Organization (unknown legal status) | E1 |
| Org merge (legal same subject) | E2 |
| OWNER / OWNS (domain, site) | E1–E2 |
| EMPLOYEE / CONTRACTOR (structural) | E1 |
| Website exists (internal pack) | E0–E1 |
| Relationship from import only | E1 or E3 + human review |

---

## 5. Stewardship

### 5.1 Steward role

The **registry steward** is the **day-to-day custodian** of attestation quality:

- intake and triage of proposals;
- evidence collection and tier assignment;
- duplicate and homonym routing;
- escalation to program owner.

Stewards **may attest** when **written delegation** exists ([ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) GV-02).

### 5.2 Stewardship principles

| Principle | Rule |
|-----------|------|
| **Quality over throughput** | Do not mass-promote imports without review |
| **Prefer UNKNOWN over wrong** | CR-10, AT-UK-01 |
| **One graph** | Duplicates merged, not ignored |
| **Traceability** | Every active record should have attest trail (future implementation) |

### 5.3 Stewardship boundaries

Stewards **cannot**: approve entity splits without owner; override boundary exclusions; designate consumer systems as co-owners of canonical truth.

---

## 6. Review

### 6.1 Review types

| Review type | Trigger | Outcome |
|-------------|---------|---------|
| **Intake review** | New proposal | Promote, hold proposed, or reject |
| **Evidence review** | Tier challenge | Upgrade tier, dispute, or UNKNOWN |
| **Duplicate review** | D1–D5 classes ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) §3) | Merge, separate, UNKNOWN |
| **Boundary review** | Field smells like CRM/finance | Reject or consumer-local |
| **Dispute review** | Conflicting claims | Resolve, deprecate one, or UNKNOWN |
| **Expansion review** | New taxonomy | Approve/defer per expansion rules |

### 6.2 Review outcomes (normative)

| Outcome | Effect |
|---------|--------|
| **Attest → active** | Canonical for consumers |
| **Remain proposed** | Not SoT |
| **Mark disputed** | Block new canonical dependencies |
| **Reject proposal** | No canonical record; log rationale |
| **SAFE UNKNOWN** | Explicit gap — no invention |

---

## 7. Uncertainty and SAFE UNKNOWN

### 7.1 When to declare SAFE UNKNOWN

| Situation | Required behavior |
|-----------|-------------------|
| Id referenced but not in canonical set | SAFE UNKNOWN — no attribute inference |
| Insufficient evidence for promotion | Remain proposed or UNKNOWN |
| Conflicting attestations unresolved | disputed or UNKNOWN |
| Consumer cache disagrees with ATLAS pre-reconciliation | UNKNOWN until human reconcile |
| Missing org for website | Flag gap — no auto-org |
| Business Scope classification only | Not attestation input for entity existence |

### 7.2 SAFE UNKNOWN rules (AT-UK-*)

| Rule ID | Rule |
|---------|------|
| **AT-UK-01** | UNKNOWN is **explicit state**, not empty string or placeholder id |
| **AT-UK-02** | No permanent `org-unknown-*` canonical ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-10) |
| **AT-UK-03** | Consumers must surface UNKNOWN to operators — not hide in UI defaults |
| **AT-UK-04** | UNKNOWN may drive **work queues**, not **automation that invents ids** |
| **AT-UK-05** | Resolving UNKNOWN requires **attestation**, not batch heuristic |

### 7.3 Uncertainty vs disputed

| State | Meaning |
|-------|---------|
| **SAFE UNKNOWN** | We do not know enough to assert the fact |
| **disputed** | Competing claims exist; evidence conflict |

Both block **new irreversible canonical dependencies** until review completes.

---

## 8. Roles — who may attest, challenge, approve

### 8.1 Authority matrix (attestation-focused)

| Action | Program owner | Steward | Consumer | Agent |
|--------|---------------|---------|----------|-------|
| **Attest → active (entity/rel)** | Yes | Delegated | **No** | **No** |
| **Challenge / flag dispute** | Yes | Yes | Yes | Yes (flag) |
| **Approve merge** | Yes | Delegated | No | No |
| **Approve split** | **Yes only** | No | No | No |
| **Declare SAFE UNKNOWN** | Yes | Yes | No | No |
| **Reject proposal** | Yes | Yes | No | No |
| **Override boundary violation** | **No** — fix proposal | | | |

### 8.2 Challenge process

1. Any qualified flagger opens **dispute** or comment with evidence.
2. Steward investigates within **evidence review**.
3. Owner resolves if escalation required.
4. Outcome: attest one side, merge, separate, or UNKNOWN.

**Rule AT-CH-01:** Challenge does **not** grant consumer rights to rewrite canonical records.

---

## 9. Attestation and imports

Future bulk imports ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) RA-D06):

| Step | Behavior |
|------|----------|
| 1 | Import creates **proposed** rows + `evidence_ref` (E3) |
| 2 | Mapping table: consumer key → proposed ATLAS id |
| 3 | Steward batch-review with spot checks |
| 4 | Promote subset to active; duplicates → merge workflow |
| 5 | Unresolved → SAFE UNKNOWN |

**Prohibition AT-IMP-01:** Import scripts **must not** set active canonical without human attestation record.

---

## 10. Trust model summary diagram

```text
  Evidence (E0–E3)          Proposal (non-canonical)
        │                            │
        └──────────┬─────────────────┘
                   ▼
            Steward / Owner REVIEW
                   │
         ┌─────────┼─────────┐
         ▼         ▼         ▼
      ACTIVE    DISPUTED   SAFE UNKNOWN
   (canonical)  (blocked)   (explicit gap)
```

---

## 11. Relationship to Phase 1–3 governance

| Topic | Phase source | Phase 4 role |
|-------|--------------|--------------|
| Relationship evidence tiers | Phase 2 RG §3 | Unified here as registry-wide |
| Identity merge/split | Phase 3 IGV | Attestation outcomes |
| Expansion | Phase 1 ER | Separate approval path — not entity attest |

Phase 4 **does not weaken** GV-01, IGV-01, or CR-02. It **generalizes** trust language for the whole registry system.

---

## 12. Non-deliverables

No evidence vault implementation, OCR pipeline, or automated tier classifier.

---

*ATLAS Attestation Model v1 — Phase 4 Foundation. Documentation only.*
