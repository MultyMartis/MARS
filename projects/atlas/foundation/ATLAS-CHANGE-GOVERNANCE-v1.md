# ATLAS Change Governance v1

**Status:** **documented** — Phase 4 normative governance for registry evolution.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) · [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)  
**Is not:** ticketing system, CI gate, automated policy engine, version control for data files.

**Phase 1–3 constraint:** No changes to approved Phase 1–3 documents unless contradictions are discovered. None identified at Phase 4 authoring.

---

## 1. Purpose

Define **how ATLAS evolves** after Phase 1–4 foundations — entity additions, relationship additions, aliases, identity changes, and registry-level amendments — with **review requirements**, **approval requirements**, **anti-chaos principles**, and **expansion discipline**.

This document is the **governance layer for future ATLAS growth**, complementing Phase 1 [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) with registry-system scope.

---

## 2. Change philosophy

### 2.1 Deliberate evolution

ATLAS changes **slowly** and **in writing**. Urgent consumer pressure does not bypass:

- boundary checks;
- expansion criteria;
- attestation rules;
- identity merge discipline.

### 2.2 Prefer amendment over sprawl

| Prefer | Over |
|--------|------|
| New relationship type | New entity |
| Alias on existing entity | Duplicate entity |
| Metadata on consumer | Canonical field |
| Deprecation + successor | Id recycle |

Reaffirms [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) §4.

---

## 3. Change categories

### 3.1 Entity additions

| Change | Governance path |
|--------|-----------------|
| New **instance** (another Organization) | Intake + attestation — no expansion review |
| New **entity class** (seventh MVP type) | **Full expansion review** — A-01–A-07 |
| New **canonical field class** on existing entity | Field expansion review (Phase 1 ER §6) |
| Reactivate deprecated entity | Attestation + evidence — treat as promotion |

### 3.2 Relationship additions

| Change | Governance path |
|--------|-----------------|
| New **instance** of approved type | Relationship attestation per Phase 2 |
| New **relationship type** in taxonomy | Expansion + taxonomy amendment ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md)) |
| Cardinality rule change | Written decision + consumer impact note |

### 3.3 Alias additions

| Change | Governance path |
|--------|-----------------|
| New alias on existing entity | Light review + attestation ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)) |
| Alias collision / dispute | Identity governance duplicate flow |
| Consumer-suggested alias | Propose → steward attest |

### 3.4 Identity changes

| Change | Governance path |
|--------|-----------------|
| Display name update | Light attest |
| Merge | Evidence + steward/owner ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) §4) |
| Split | **Owner only** |
| Identifier correction (rare) | Owner + audit trail |
| Deprecation without merge | Steward + owner policy |

### 3.5 Registry changes (architecture-level)

| Change | Governance path |
|--------|-----------------|
| New entity registry partition (new class) | Expansion + Phase 4 doc amendment |
| Consumer contract change | Update [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) + REPORT |
| Attestation tier policy change | Update [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) |
| Boundary shift | **BOUNDARIES before TAXONOMY** ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) G-05) |

---

## 4. Review requirements

### 4.1 Minimum review package (by severity)

| Severity | Examples | Required artifacts |
|----------|----------|-------------------|
| **S0 — Routine instance** | New website for known org | Intake form, E0–E1 evidence, attest note |
| **S1 — Alias / display** | Trade name alias | Alias proposal, collision check |
| **S2 — Structural identity** | Merge two orgs | Evidence E2, relationship impact, consumer mapping plan |
| **S3 — Taxonomy / type** | New relationship type `SUBSIDIARY_OF` | Expansion proposal §3.1 Phase 1 ER |
| **S4 — Boundary / architecture** | Store invoice id on Organization | Boundary review — expect **reject** |
| **S5 — Split / registry architecture** | Person split; new Phase doc | Owner approval + written decision record |

### 4.2 Review roles

| Severity | Steward | Owner |
|----------|---------|-------|
| S0–S1 | Review + attest (delegated) | Optional spot check |
| S2 | Review + propose decision | Approve merge |
| S3–S4 | Prepare package | Approve expansion |
| S5 | Prepare package | **Required approve** |

---

## 5. Approval requirements

### 5.1 Approval authority (consolidated)

| Decision | Approver |
|----------|----------|
| proposed → active (routine) | Steward (delegated) or Owner |
| Merge | Owner or delegated steward |
| Split | **Owner only** |
| New entity class | Owner + expansion record |
| New relationship type | Owner + taxonomy bump |
| Boundary exception | **No standing exception** — amend boundaries or reject |
| Phase document revision | Owner sign-off in REPORT |
| Consumer contract waiver | **Not permitted** for CC-P01–P07 |

### 5.2 Written decision record

Per [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) G-01:

| Field | Content |
|-------|---------|
| Date | ISO date |
| Change id | Human-readable reference |
| Category | §3 category |
| Rationale | Why needed, which consumers |
| Boundary check | Pass/fail explicit |
| Outcome | Approve / defer / reject |
| Approver | Role + name |

Chat-only approval is **insufficient** for S3–S5.

---

## 6. Anti-chaos principles

| Principle ID | Principle |
|--------------|-----------|
| **AC-01** | **No silent promotion** — every active record has attest trail |
| **AC-02** | **No id recycle** — deprecated ids point forward |
| **AC-03** | **No dual canonical** — duplicates merge, not coexist |
| **AC-04** | **No consumer veto** of steward boundary reject |
| **AC-05** | **No emergency bypass** of merge evidence for “deadline” |
| **AC-06** | **One taxonomy version** active per implementation charter |
| **AC-07** | **Cooling period** on rejected expansion — 30 days ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) §3.3) |
| **AC-08** | **UNKNOWN is valid** — better than wrong canonical |
| **AC-09** | **Imports are proposals** — not floods of active rows |
| **AC-10** | **Business Scope never gates** canonical existence |

---

## 7. Expansion discipline (registry-wide)

Phase 1 expansion rules apply unchanged. Phase 4 adds **registry-system checks**:

| Check | Question |
|-------|----------|
| **RG-01** | Does change require new entity class, or can Relationship express it? |
| **RG-02** | Does change push ATLAS toward operational authority? (If yes → reject) |
| **RG-03** | Do **two or more** consumers benefit, or one critical SoT gap? (A-05) |
| **RG-04** | Can consumer-local storage hold the data instead? |
| **RG-05** | Does change break consumer contracts without migration plan? |

---

## 8. Versioning and document amendments

| Artifact type | Version bump |
|---------------|--------------|
| Taxonomy entity set | v1 → v2 in filename or header |
| Relationship type enum | Taxonomy doc revision |
| Phase 4 architecture doc | Minor amendment with REPORT; major = new Phase package |
| Implementation charter | Must cite approved doc versions only ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) G-04) |

**Rule CG-V01:** Implementation **must not** ship features from **NOT APPROVED** expansion candidates.

---

## 9. Consumer-driven change pressure

Consumers often request “just add a field.” Governance response:

```text
Request → Classify (§3) → Boundary check → Severity (§4)
    → If S4 smell → Reject or consumer-local
    → If S0–S2 → Attestation path
    → If S3+ → Expansion package
```

**Rule CG-CDP-01:** High-frequency operational fields **never** become canonical via consumer lobbying alone.

---

## 10. Future imports and migrations

| Scenario | Governance |
|----------|------------|
| CRM org import | Proposed + mapping; steward promote |
| Legacy spreadsheet | Same; no bulk active |
| ATLAS merge | Consumer key migration plan required (CR-S02) |
| Two consumers disagree on org | Dispute → owner; not “first writer wins” |

---

## 11. Relationship to other Phase 4 docs

| Document | Role in change |
|----------|----------------|
| [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) | How instance changes become canonical |
| [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) | How consumers may request change |
| [ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md) | Which partition is affected |

---

## 12. Non-deliverables

No workflow engine, Git hooks, or automated expansion linter.

---

*ATLAS Change Governance v1 — Phase 4 Foundation. Documentation only.*
