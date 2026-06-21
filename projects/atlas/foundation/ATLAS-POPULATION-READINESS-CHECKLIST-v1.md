# ATLAS Population Readiness Checklist v1

**Status:** **documented** — Phase 9 pre-wave readiness gates (normative checklist).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-POPULATION-EXECUTION-PLAN-v1.md](ATLAS-POPULATION-EXECUTION-PLAN-v1.md) · [ATLAS-POPULATION-ROADMAP-v1.md](ATLAS-POPULATION-ROADMAP-v1.md) · [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md)  
**Companion:** [ATLAS-WAVE-1-EXECUTION-v1.md](ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md)  
**Is not:** automated gate script, certification audit, implementation go-live checklist.

**Phase 1–8 constraint:** Checklist operationalizes existing Phase 7–8 gates — does not alter attestation or wave order.

---

## 1. Purpose

Define **readiness checks** that must pass before **Wave 1**, **Wave 2**, and **Wave 3** population execution begins — covering steward readiness, evidence readiness, duplicate risk, identity readiness, and relationship readiness.

**Normative statement:**

> No population wave **executes** until its readiness checklist reaches the required verdict — **NOT READY**, **PARTIALLY READY**, or **READY** — with Program Owner acknowledgment for **READY**.

---

## 2. Verdict definitions

| Verdict | Meaning | Wave execution |
|---------|---------|----------------|
| **NOT READY** | Blocking gaps — do not start wave attest | Halt |
| **PARTIALLY READY** | Dry-run, proposed intake, card collection OK — **no active attest** | Limited |
| **READY** | All blocking checks pass — active attest authorized | Full wave execution |

**PRC-01:** **READY FOR WAVE 1** (program-level) requires Wave 1 checklist **READY** + owner sign-off.

**PRC-02:** PARTIALLY READY is valid for preparation tranches — steward must not interpret as active attest permission.

---

## 3. Universal readiness dimensions

Every wave checklist evaluates five dimensions:

| Dimension | Question |
|-----------|----------|
| **Steward readiness** | Are qualified humans, delegation, and intake path in place? |
| **Evidence readiness** | Are required artifacts obtainable and tier rules understood? |
| **Duplicate risk** | Are homonym/alias signals identified and review planned? |
| **Identity readiness** | Are identifier, alias, and merge rules accessible to reviewers? |
| **Relationship readiness** | Are endpoint prerequisites and edge types for this wave understood? |

---

## 4. Wave 1 readiness — Organizations

### 4.1 Steward readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W1-S-01** | Registry Steward designated with written attest delegation (POP-GV-01) | ☐ |
| **W1-S-02** | Program Owner available for dispute/merge escalation | ☐ |
| **W1-S-03** | Steward completed onboarding path ([ATLAS-FOUNDATION-INDEX-v1.md](ATLAS-FOUNDATION-INDEX-v1.md) §4.2) | ☐ |
| **W1-S-04** | Intake/review playbook understood ([ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md)) | ☐ |
| **W1-S-05** | Execution log artifact defined (conceptual) | ☐ |
| **W1-S-06** | STOP trigger response understood | ☐ |

### 4.2 Evidence readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W1-E-01** | Counterparty Card model reviewed ([ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](ATLAS-COUNTERPARTY-CARD-MODEL-v1.md)) | ☐ |
| **W1-E-02** | Organization acquisition rules reviewed ([ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md)) | ☐ |
| **W1-E-03** | W1-A CC obtain/compile plan for Polygon, MetaCode, i-SEO | ☐ |
| **W1-E-04** | W1-B Triumph CC obtain plan (or E2 alternate rationale drafted) | ☐ |
| **W1-E-05** | Contract/invoice primary path prohibition acknowledged (OAR-BAN-01) | ☐ |
| **W1-E-06** | Evidence tier assignment cheat sheet accessible (E0 W1-A / E1 W1-B) | ☐ |

### 4.3 Duplicate risk

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W1-D-01** | Alias watchlist seeded: Polygon/Полигон/WSP | ☐ |
| **W1-D-02** | MetaCode/Метакод homonym note prepared | ☐ |
| **W1-D-03** | i-SEO vs client org boundary note prepared | ☐ |
| **W1-D-04** | Triumph name disambiguation note (org vs pilot) | ☐ |
| **W1-D-05** | Batch duplicate review scheduled before first active attest | ☐ |
| **W1-D-06** | Merge path escalation to owner understood (IGV) | ☐ |

### 4.4 Identity readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W1-I-01** | Identifier model reviewed — no premature id mint in planning docs | ☐ |
| **W1-I-02** | Alias vs canonical name rules accessible ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)) | ☐ |
| **W1-I-03** | SAFE UNKNOWN declaration process known | ☐ |
| **W1-I-04** | Optional requisites fields = UNKNOWN until expansion ([OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md)) | ☐ |
| **W1-I-05** | No `org-unknown-*` policy reaffirmed (GA-04) | ☐ |

### 4.5 Relationship readiness (Wave 1 perspective)

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W1-R-01** | Steward knows Wave 1 is **org-only** — no CLIENT_OF in Wave 1 | ☐ |
| **W1-R-02** | Wave 2B dependency noted — org endpoints before participation edges | ☐ |
| **W1-R-03** | Triumph org ≠ Triumph pilot project distinction documented | ☐ |

### 4.6 Wave 1 verdict matrix

| Blocking failures | Verdict |
|-------------------|---------|
| Any W1-S-01 through W1-S-04 fail | **NOT READY** |
| W1-S pass; W1-E-03/W1-E-04 not started | **PARTIALLY READY** (collection only) |
| All W1-S, W1-E, W1-D, W1-I, W1-R pass | **READY** |

**Owner sign-off required for READY.**

---

## 5. Wave 2 readiness — People

Wave 2 readiness is evaluated **before Person active attest** — may parallel Wave 1 **proposed** org intake when W1 duplicate batch is scheduled.

### 5.1 Steward readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W2-S-01** | Wave 1 duplicate batch complete or in final review | ☐ |
| **W2-S-02** | Steward capacity for Person homonym review | ☐ |
| **W2-S-03** | Person vs service account boundary understood | ☐ |

### 5.2 Evidence readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W2-E-01** | E0 path confirmed for Andrey, Sergey, Roman (operator-known) | ☐ |
| **W2-E-02** | Triumph contact extraction = proposed only (CC-PER-01) | ☐ |
| **W2-E-03** | Email-only Person creation prohibited | ☐ |

### 5.3 Duplicate risk

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W2-D-01** | Andrey homonym plan (U4 / D3) | ☐ |
| **W2-D-02** | Triumph contact names vs existing Person scan planned | ☐ |
| **W2-D-03** | Person vs Organization boundary (D5) reviewed | ☐ |

### 5.4 Identity readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W2-I-01** | Canonical name disambiguation rule for homonyms | ☐ |
| **W2-I-02** | Multi-org Person model understood — one PER, many REL | ☐ |
| **W2-I-03** | Wave 1 org endpoints at least **proposed** | ☐ |

### 5.5 Relationship readiness (Wave 2B prep)

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W2-R-01** | Andrey → Polygon/MetaCode/i-SEO edge types pre-identified (OWNER/MANAGER) | ☐ |
| **W2-R-02** | Sergey/Roman endpoint orgs identified or SAFE UNKNOWN declared | ☐ |
| **W2-R-03** | W2B-R01 endpoint rule understood | ☐ |
| **W2-R-04** | CLIENT_OF explicitly deferred to Wave 6 | ☐ |

### 5.6 Wave 2 verdict matrix

| Blocking failures | Verdict |
|-------------------|---------|
| W2-I-03 fail (no org proposals) | **NOT READY** |
| W2-S-01 in progress; W2-E/W2-D partial | **PARTIALLY READY** |
| All W2 checks pass + Wave 1 W1-A active or owner-approved defer | **READY** |

---

## 6. Wave 3 readiness — Projects

Wave 3 executes after Stage A anchor progress — typically post Wave 1–2B or with owner-documented defer per GA-03.

### 6.1 Steward readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W3-S-01** | Stage A GA-01 progress reviewed — org anchor stable | ☐ |
| **W3-S-02** | Project vs Organization boundary trained ([ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) §3) | ☐ |
| **W3-S-03** | MARS `project_id` disambiguation note prepared | ☐ |

### 6.2 Evidence readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W3-E-01** | E0–E1 structural attest path for operator pilots | ☐ |
| **W3-E-02** | Triumph pilot (gruzotaxi Krasnodar) evidence separate from Triumph org CC | ☐ |
| **W3-E-03** | MIG session artifacts = proposal support only (AT-E-03) | ☐ |
| **W3-E-04** | Sponsor org reference available (active/proposed/UNKNOWN) | ☐ |

### 6.3 Duplicate risk

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W3-D-01** | Project name collision with org names checked | ☐ |
| **W3-D-02** | Pilot vs production naming separated | ☐ |
| **W3-D-03** | MIG pack website ≠ auto Project | ☐ |

### 6.4 Identity readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W3-I-01** | Project identifier mint rules reviewed | ☐ |
| **W3-I-02** | Initiative container semantics — not Jira/PM ([ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md)) | ☐ |

### 6.5 Relationship readiness

| Check ID | Criterion | Pass? |
|----------|-----------|-------|
| **W3-R-01** | COMMISSIONED_BY / BELONGS_TO deferred to Wave 6B — noted | ☐ |
| **W3-R-02** | Sponsor org endpoint identified for each priority project | ☐ |
| **W3-R-03** | Website links deferred to Wave 4 | ☐ |

### 6.6 Wave 3 verdict matrix

| Blocking failures | Verdict |
|-------------------|---------|
| W3-S-01 fail (no org anchor) | **NOT READY** |
| W3-E-04 UNKNOWN sponsor without owner note | **PARTIALLY READY** (proposed projects only) |
| All W3 checks pass + GA-01 met or deferred | **READY** |

---

## 7. Cross-wave readiness summary

| Wave | Primary focus | Minimum prior wave | Owner sign-off |
|------|---------------|-------------------|----------------|
| **Wave 1** | Organizations | Phase 9 package complete | Required for READY |
| **Wave 2** | People | W1 proposed + dup batch | Required for READY |
| **Wave 3** | Projects | GA-01 progress | Required for READY |

---

## 8. Program-level execution readiness verdict

Aggregate checklist for Phase 9 kickoff:

| Condition | Program verdict |
|-----------|-----------------|
| Phase 1–8 foundations complete; Phase 9 docs published; Wave 1 checklist NOT READY | **NOT READY** |
| Wave 1 PARTIALLY READY — cards collecting, stewards onboarding | **PARTIALLY READY** |
| Wave 1 READY; owner sign-off; no STOP active | **READY FOR WAVE 1** |

**Current Phase 9 authoring verdict:** **READY FOR WAVE 1** at **documentation and methodology** level — pending operational sign-off (steward delegation, card collection, owner acknowledgment) at execution time.

---

## 9. Readiness review record (conceptual template)

| Field | Value |
|-------|-------|
| Wave | 1 / 2 / 3 |
| Review date | |
| Reviewer (Steward) | |
| Owner sign-off | |
| Verdict | NOT READY / PARTIALLY READY / READY |
| Blocking items | |
| Next review date | |

---

## 10. Non-deliverables

No automated scoring, ticketing integration, or registry implementation.

---

*ATLAS Population Readiness Checklist v1 — Phase 9 Foundation. Documentation only.*
