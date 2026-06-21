# ATLAS Population Execution Plan v1

**Status:** **documented** — Phase 9 Population Execution Planning (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-POPULATION-STRATEGY-v1.md](ATLAS-POPULATION-STRATEGY-v1.md) · [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) · [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md)  
**Companion:** [ATLAS-WAVE-1-EXECUTION-v1.md](ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) · [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](ATLAS-POPULATION-READINESS-CHECKLIST-v1.md)  
**Is not:** runtime, APIs, databases, automation, import tooling, sprint calendar, steward roster assignment, canonical record creation.

**Phase 1–8 constraint:** Does not modify approved Phase 1–8 foundations. Introduces **Counterparty Card** as a dedicated acquisition source without contradicting evidence tiers E0–E3.

---

## 1. Purpose

Phase 7 defined **what** should be populated and in what wave order.  
Phase 8 defined **who** operates population and how intake/review flows.  
Phase 9 defines **how controlled population is actually executed** — human-supervised execution planning only.

**Normative statement:**

> **Population execution** is the governed, wave-ordered, evidence-backed sequence by which stewards move claims from **Counterparty Card and other approved sources** through **proposal → review → attestation** — without automation, bulk promotion, or canonical invention.

---

## 2. Execution philosophy

### 2.1 Documentation-first, human-supervised

| Principle | Application |
|-----------|-------------|
| **No runtime shortcut** | Execution is described as human process; tooling may support later — not define now |
| **One record, one attest path** | Each active promotion has traceable evidence + reviewer rationale |
| **Anchor before attach** | Wave order from [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md) is **execution order**, not suggestion |
| **Card-first for organizations** | Counterparty Card is **preferred** acquisition source ([ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md)) |
| **Contracts are not org sources** | Contracts, acts, invoices, specs, project reports belong to OPS and other systems — not primary ATLAS org intake |
| **Quality over throughput** | Stop conditions override wave momentum ([ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md)) |
| **SAFE UNKNOWN over invention** | Missing facts remain explicit gaps — never placeholder ids |

### 2.2 Counterparty Card execution chain

```text
Counterparty Card (or approved alternate evidence)
        │
        ▼
   Evidence package (tier assigned at review)
        │
        ▼
   Proposal (non-canonical)
        │
        ▼
   Review (duplicate · boundary · evidence · wave)
        │
        ├──► ATTEST ──► active canonical
        ├──► DEFER ───► proposed (held)
        ├──► REJECT ──► logged, no canonical
        └──► DISPUTED ► blocked dependencies
```

Reaffirms attestation chain from [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §2.1 with **Counterparty Card** as the primary organization intake artifact.

### 2.3 Execution vs operation vs strategy

| Layer | Question | Phase |
|-------|----------|-------|
| **Strategy** | What to populate, why, risks | Phase 7 |
| **Operation** | Who stewards, intake queues, health | Phase 8 |
| **Execution** | Step-by-step wave performance, gates, card discipline | **Phase 9** |

**PEX-01:** Execution plans **implement** strategy and operation — they do not replace attestation or identity governance.

---

## 3. Execution stages

Execution maps population waves to **operational stages** with entry/exit gates.

### Stage 0 — Pre-execution readiness

| Activity | Owner | Output |
|----------|-------|--------|
| Readiness checklist complete | Program Owner + Steward | Signed readiness per wave ([ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](ATLAS-POPULATION-READINESS-CHECKLIST-v1.md)) |
| Steward delegation confirmed | Program Owner | Written attest delegation (POP-GV-01) |
| Counterparty Card intake path defined | Steward | Card acceptance rules understood |
| Duplicate watchlist seeded | Steward | Known alias/homonym list from foundation exemplars |
| STOP triggers acknowledged | Steward | Halt rules from population governance |

**Exit gate EX-00:** Readiness verdict **PARTIALLY READY** minimum for Wave 1 dry-run; **READY FOR WAVE 1** for live attest.

### Stage 1 — Wave 1 execution (Organizations)

| Step | Action | Gate |
|------|--------|------|
| 1.1 | Collect Counterparty Cards for W1-A operator core | Card format valid per CC model |
| 1.2 | Intake proposals — one org per proposal package | INT-01 class/boundary check |
| 1.3 | Duplicate review (D1) before any active attest | No unresolved D1 |
| 1.4 | Evidence tier assignment | E0–E1 for operator core; E1+ for W1-B |
| 1.5 | Steward/owner attest → **active** | GA-01 trail |
| 1.6 | Document gaps as SAFE UNKNOWN on optional fields | No invented requisites |

**Exit gate EX-01:** Stage A GA-01 — core operator orgs **active** with evidence trail.

See [ATLAS-WAVE-1-EXECUTION-v1.md](ATLAS-WAVE-1-EXECUTION-v1.md).

### Stage 2 — Wave 2 execution (People)

| Step | Action | Gate |
|------|--------|------|
| 2.1 | Identify persons from cards, operator context, separate attest | Not card-only for external persons |
| 2.2 | Intake Person proposals | Homonym review (D3) |
| 2.3 | Attest operator-known persons | E0 acceptable with steward note |
| 2.4 | Defer external persons lacking E1 | No email-only active Person |

**Exit gate EX-02:** Key operator persons **active** or explicitly **proposed** with defer rationale.

### Stage 3 — Wave 2B execution (Participation edges)

| Step | Action | Gate |
|------|--------|------|
| 3.1 | Queue PERSON↔ORG relationships | W2B-R01 both endpoints ready |
| 3.2 | Evidence per relationship type | E1 for OWNER; E0 operator-direct allowed |
| 3.3 | Attest participation edges | No disputed active OWNER |

**Exit gate EX-03:** GA-03 — Wave 2B complete or owner-documented defer.

### Stage 4 — Waves 3–6 (deferred in Phase 9 detail)

Phase 9 **defines execution methodology** for Waves 3–6 by reference to Phase 7 priorities. Detailed wave execution charters are **future Phase 9+ companions** when Stage A exits.

| Wave | Execution trigger |
|------|-------------------|
| Wave 3 Project | EX-03 + readiness checklist Wave 3 |
| Wave 4 Website | Wave 3 started or scoped proposed |
| Wave 5 Domain | Wave 4 for typical case |
| Wave 6 Relationship bulk | Stage A–B entity anchors stable |

---

## 4. Execution responsibilities

### 4.1 RACI (execution context)

| Activity | Program Owner | Registry Steward | Consumer | Agent |
|----------|---------------|------------------|----------|-------|
| Wave kickoff / halt | **A** | R | I | I |
| Counterparty Card intake | A | **R** | C (propose card ref) | C (propose only) |
| Evidence tier assignment | A | **R** | — | — |
| Duplicate review | A | **R** | Flag | Flag |
| Active attest | **A** | R (delegated) | — | — |
| Readiness sign-off | **A** | R | — | — |
| STOP trigger response | **A** | R (escalate) | — | — |

**R** = responsible · **A** = accountable · **C** = consulted · **I** = informed

### 4.2 Steward execution duties (per wave)

1. Maintain **execution log** (conceptual — doc, spreadsheet, or future UI).
2. Ensure **one proposal package per entity** at intake.
3. Run **duplicate review before attest** — never attest-first-fix-later.
4. Assign evidence tier honestly — card quality does not auto-upgrade tier.
5. Enforce **wave prerequisites** for active promotion (POP-PROP-01).
6. Escalate boundary smell (contract-as-org-source, CRM Account) to owner.
7. Record **SAFE UNKNOWN** declarations with gap description (EV-UK-01).

### 4.3 Program Owner execution duties

1. Approve wave start after readiness checklist.
2. Resolve disputes and split/merge decisions.
3. Invoke population **halt/resume** when STOP triggers fire.
4. Accept Stage exit gates (GA-01 through GA-05).

---

## 5. Execution gates

### 5.1 Universal gates (every promotion)

| Gate ID | Criterion | Block if fail |
|---------|-----------|---------------|
| **EG-01** | Entity class valid (MVP six) | Reject at intake |
| **EG-02** | Boundary check passed | Reject at intake |
| **EG-03** | Minimum evidence tier for target state | Defer active |
| **EG-04** | Duplicate review complete | Defer active |
| **EG-05** | Wave prerequisite met for **active** | Defer or queue |
| **EG-06** | Human attestor qualified | Reject auto path |

### 5.2 Wave 1 specific gates

| Gate ID | Criterion |
|---------|-----------|
| **EW1-01** | Counterparty Card or approved alternate evidence on file |
| **EW1-02** | Legal name + disambiguation note if homonym |
| **EW1-03** | No active promotion from contract/invoice primary source |
| **EW1-04** | Import-only row not attested E0 |
| **EW1-05** | Owner sign-off if W1-B client org in same tranche as W1-A |

### 5.3 Stage A exit gates (from roadmap — execution binding)

| Gate ID | Execution evidence |
|---------|-------------------|
| **GA-01** | W1-A operator orgs active, E0–E1 trail |
| **GA-02** | No unresolved D1 in Organization/Person |
| **GA-03** | Wave 2B complete or owner defer document |
| **GA-04** | No `org-unknown-*` canonical |
| **GA-05** | No active population halt |

**PEX-02:** Stage exit requires **owner acknowledgment** — steward completion alone is insufficient for GA-05 clearance.

---

## 6. Execution risks

| Risk ID | Description | Likelihood | Impact | Mitigation |
|---------|-------------|------------|--------|------------|
| **ER-01** | Card OCR/extraction errors treated as fact | Medium | High | Human review all extracted fields; never auto-attest |
| **ER-02** | Contract used as org intake shortcut | Medium | High | OAR-03 prohibition; boundary review |
| **ER-03** | Duplicate org from trade name vs legal name | High | High | D1 review; alias model before second org |
| **ER-04** | Person minted from card contact line only | Medium | Medium | CC-PER-01 — proposed only until attest |
| **ER-05** | Incomplete card promoted to active | Medium | High | CC-INC rules; defer missing critical fields |
| **ER-06** | Multiple cards conflicting (INN mismatch) | Low | High | Disputed workflow; no active until resolved |
| **ER-07** | Wave skip (relationships before orgs) | Medium | High | POP-PROP-01 + execution halt |
| **ER-08** | OPS requisites copied as canonical without attest | Medium | Medium | OPS-ALN requisites = expansion/UNKNOWN |
| **ER-09** | Steward throughput pressure → batch attest | Medium | High | STOP triggers; quality over throughput |
| **ER-10** | Triumph client org conflated with pilot Project | Medium | Medium | Separate Organization vs Project intake |

---

## 7. Required architectural decisions (Phase 9)

Decisions are normative for execution. Detailed rationale in companion documents.

| # | Question | Decision |
|---|----------|----------|
| **A1** | Can an organization enter ATLAS from a Counterparty Card alone? | **Partially.** Card alone supports **proposed** Organization. **Active** attest requires human confirmation + tier meeting minimum (E0 operator-known with steward attest, or E1+ from card for external). Card alone never auto-promotes. |
| **A2** | Can contacts be extracted from a Counterparty Card? | **Yes as proposed claims only.** Phone/email/name on card → proposed Person or contact metadata pending review. **Active** Person requires homonym review and relationship context — not card line alone. |
| **A3** | Can EDO be considered business reality? | **Yes** as **attested optional identifier metadata** on Organization (EDO operator + participant id). It is structural identification — not OPS document workflow. |
| **A4** | Should contracts ever be primary acquisition evidence? | **No.** Contracts may **corroborate** (E2) in disputes; never primary org intake path. OAR-01. |
| **A5** | What fields are safe to trust? | Registrar-grade fields on verified card (INN, OGRN, KPP, legal name) after steward visual confirmation → safe for **proposed** extraction; **active** after tier + duplicate check. Operator-known display names: E0 context. |
| **A6** | What fields require human review? | Director→Person linkage, all contacts, trade vs legal name, EDO ids, addresses, CLIENT_OF/VENDOR_OF inference, multi-card conflicts. |
| **A7** | How should incomplete cards behave? | **Proposed** org with explicit gap list; **defer** active; SAFE UNKNOWN for missing optional fields; **never infer** missing INN/OGRN/legal name. |
| **A8** | How should multiple cards for one organization behave? | Evidence **bundle** under one org proposal; duplicate review; supersession note on newer card; conflicting critical fields → **disputed** until resolved. |

---

## 8. Execution artifacts (conceptual)

Phase 9 does not mandate tooling. Stewards maintain:

| Artifact | Purpose |
|----------|---------|
| **Wave execution log** | Proposal id, source card ref, reviewer, outcome, date |
| **Card evidence index** | Pointer to card file + format + intake date |
| **Duplicate watchlist** | Known alias pairs under monitoring |
| **Gap register** | SAFE UNKNOWN fields with owner |
| **Readiness checklist** | Per-wave sign-off |

---

## 9. Non-deliverables

No runtime, APIs, databases, OCR pipelines, automation scripts, canonical records, git commits, or implementation schedules.

---

*ATLAS Population Execution Plan v1 — Phase 9 Foundation. Documentation only.*
