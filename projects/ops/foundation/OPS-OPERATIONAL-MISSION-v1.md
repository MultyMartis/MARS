# OPS — Operational Mission v1

**Status:** **documented** — operational identity layer (design).  
**Program:** OPS — Business Operations Domain  
**Phase:** 4 — Operational Mission & System Positioning  
**Date:** 2026-06-04  
**Parent:** [OPS-BOUNDARIES-v1.md](OPS-BOUNDARIES-v1.md) · [../README.md](../README.md)  
**Is not:** implementation charter, registry entry, runtime mission statement, or authority grant.

---

## 1. Purpose

State **why OPS exists** in MARS: the operational problems it addresses, what success and failure mean at the domain level, and the non-negotiable stance that OPS is **operational support**, not **ecosystem or business authority**.

---

## 2. Mission

### 2.1 One-sentence mission

**OPS gives studio operators a documented, human-supervised way to see and complete recurring back-office work — reporting, documents, follow-ups, approvals, and deadlines — without duplicating business identity or pretending to be a product runtime.**

### 2.2 One-paragraph mission

OPS exists because back-office operational rhythm — monthly client reports, document closing steps, follow-up chains, approval gates, and deadline visibility — routinely fails in ad-hoc spreadsheets, chat threads, and memory. OPS defines **how that work is structured, tracked, and closed** using ATLAS-backed context where available, with explicit human approval before client-facing delivery. OPS does not decide who the client is, what is legally true, or what money moved; it makes **operational completion and visibility** honest and repeatable for the operator.

### 2.3 Operational purpose

| Dimension | Purpose |
|-----------|---------|
| **Visibility** | Operators can answer: what is due, what stage is it in, who approved, what is blocked |
| **Structure** | Recurring work follows normative workflows (WF-01–WF-06) instead of one-off habits |
| **Accountability** | Completion, approval, and escalation states are recordable — human-attested |
| **Separation** | Business reality stays in ATLAS; operational artifacts stay in OPS |
| **Honesty** | Documentation does not claim runtime, automation, or integration that does not exist |

---

## 3. Problems OPS exists to solve

| Problem class | Symptom | OPS response (documented) |
|---------------|---------|---------------------------|
| **Missed reporting** | Monthly reports slip or repeat without closure record | WF-01 cycle, ReportRecord status, completion recording |
| **Missing follow-ups** | Post-delivery actions lost after meetings or sends | WF-03 follow-up case type, TaskRecord attachment |
| **Document tracking gaps** | Contracts/acts prepared but routing status unknown | WF-02 document operational status (not legal status) |
| **Approval visibility gaps** | Client send happens without recorded reviewer | Approval model + `PENDING_APPROVAL` gates |
| **Operational coordination gaps** | Multiple people unclear on who owns next step | OpsCase owner, workflow stages, escalation visibility |
| **Deadline blindness** | Due dates live only in calendars or heads | Deadline model cross-cutting WF-04 (tracking, not calendar product) |
| **Identity drift in ops docs** | Spreadsheets become shadow CRM | ATLAS consumer rules — OPS references, does not fork SoT |

**Examples are illustrative** of problem classes; OPS does not guarantee automatic detection until a future implementation charter exists.

---

## 4. What success means (domain level)

Success for OPS **as a domain** means:

| # | Success signal | Notes |
|---|----------------|-------|
| **DS-01** | Operators can run approved workflows from documentation with clear stages | MVP: WF-01 monthly reporting |
| **DS-02** | Operational status is visible per case: open, blocked, pending approval, closed | Status model + case model |
| **DS-03** | Client-facing delivery requires recorded human approval | No silent send |
| **DS-04** | Canonical client/org/project context is referenced from ATLAS or explicit **SAFE UNKNOWN** | No silent invention |
| **DS-05** | Completion of a cycle is recordable without implying ATLAS promotion | Operational metadata only |
| **DS-06** | Boundaries hold: OPS docs are not read as CRM, ledger, legal, or runtime | Creep resistance rules BR-01–BR-05 |

Success is **operational honesty and repeatability**, not feature count or automation coverage.

---

## 5. What failure means (domain level)

| # | Failure mode | Indicator |
|---|--------------|-----------|
| **DF-01** | **Authority creep** | OPS treated as canonical client registry or legal/accounting SoT |
| **DF-02** | **Shadow SoT** | Master lists maintained only in OPS spreadsheets with no ATLAS path |
| **DF-03** | **False automation claims** | Docs or operators imply n8n/agents/runtime exist for OPS when they do not |
| **DF-04** | **Invisible delivery** | Reports or documents sent without approval or completion record |
| **DF-05** | **Permanent blocked state** | Cases stuck with no escalation or human resolution path documented |
| **DF-06** | **Ecosystem confusion** | OPS positioned as ATLAS replacement, HomeGateway owner, or MetaBOT executor |

Failure is **loss of boundary discipline** or **loss of operational visibility**, not “missing a dashboard.”

---

## 6. Authority stance (normative)

| Statement | Status |
|-----------|--------|
| **OPS is an operational support domain** | **Accepted** — structures and tracks back-office work |
| **OPS is not an authority domain** | **Accepted** — does not own business identity, legal truth, money, or ecosystem registry |
| **OPS is documentation-first in Phase 4** | **Accepted** — no runtime or registry authority implied |
| **Human supervision is mandatory** | **Accepted** — aligned with [OPS-WORKFLOW-ARCHITECTURE-v1.md](OPS-WORKFLOW-ARCHITECTURE-v1.md) |

**Normative constraint:**

> OPS may **require** human approval for operational gates; OPS may **never** assert canonical business, legal, financial, or ecosystem authority.

---

## 7. Relationship to other Phase 4 artifacts

| Document | Role |
|----------|------|
| [OPS-SYSTEM-POSITIONING-v1.md](OPS-SYSTEM-POSITIONING-v1.md) | Why OPS is a separate system vs ATLAS, HomeGateway, MetaBOT, etc. |
| [OPS-CONSUMER-MODEL-v1.md](OPS-CONSUMER-MODEL-v1.md) | Who uses OPS outputs and workflows |
| [OPS-SUCCESS-CRITERIA-v1.md](OPS-SUCCESS-CRITERIA-v1.md) | Measurable operational outcomes (no runtime KPIs) |
| [OPS-ECOSYSTEM-RELATIONSHIPS-v1.md](OPS-ECOSYSTEM-RELATIONSHIPS-v1.md) | Per-system relationship map |

---

## 8. SAFE UNKNOWN

| Topic | Unknown | Verification |
|-------|---------|--------------|
| Pilot metrics | Whether first WF-01 walkthrough met DS-01–DS-06 | Human pilot report under `projects/ops/reports/` |
| Tooling for mission enforcement | Any linter or cockpit enforcement | Separate implementation charter |

---

*OPS Operational Mission v1 · Phase 4 · Business Operations Domain.*
