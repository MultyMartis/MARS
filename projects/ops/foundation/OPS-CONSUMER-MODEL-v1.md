# OPS — Consumer Model v1

**Status:** **documented** — consumer and audience layer (design).  
**Program:** OPS — Business Operations Domain  
**Phase:** 4 — Operational Mission & System Positioning  
**Date:** 2026-06-04  
**Parent:** [OPS-OPERATIONAL-MISSION-v1.md](OPS-OPERATIONAL-MISSION-v1.md) · [OPS-AGENT-DECOMPOSITION-v1.md](OPS-AGENT-DECOMPOSITION-v1.md)  
**Is not:** IAM specification, RBAC implementation, or user database.

---

## 1. Purpose

Define **who consumes OPS** — workflows, status vocabulary, and operational artifacts — and state that OPS is **operator-centered**, not client-self-service or autonomous-agent-first.

---

## 2. Consumer overview

| Consumer type | Relationship to OPS | Consumption mode (v1) |
|---------------|----------------------|------------------------|
| **Operator** | Primary — executes workflows, owns cases, approves gates | Documentation + human-operated artifacts |
| **Executive assistant role** | Secondary — reminders, coordination, draft prep | Conceptual role in agent decomposition |
| **Reporting role** | Secondary — monthly/quarterly report assembly and delivery prep | WF-01 primary; overlaps Client Reporting role |
| **Document operations role** | Secondary — document closing and routing tracking | WF-02 documented; pilot deferred |
| **Future HomeGateway surface** | Future — read-only or action shortcuts for OPS status | **SAFE UNKNOWN** — no integration claimed |
| **Governance / registry reviewer** | Indirect — reads OPS pack for registration readiness | Reports and OPERATIONAL-INDEX |
| **ATLAS maintainers** | Indirect — receive intake from OPS discoveries (future) | No write-back in v1 |

**Normative constraint:**

> OPS is **operator-centered**. Clients, external auditors, and autonomous agents are **not** primary OPS consumers in Foundation or Phase 4.

---

## 3. Primary user

| Attribute | Definition |
|-----------|------------|
| **Who** | Studio **operator** — owner of back-office rhythm for the engagement portfolio |
| **Needs** | Know what is due, what stage, what is blocked, what needs approval before client send |
| **Authority** | Human approval for client-facing delivery; operational status updates |
| **Not granted** | Canonical edits to business identity (→ ATLAS), legal signing, payment confirmation |

The operator may wear multiple **hats** (reporting + document ops + EA functions) — still one primary human actor per case unless delegation is recorded (**SAFE UNKNOWN** for formal delegation model).

---

## 4. Secondary users

| Role | OPS artifacts consumed | Typical workflows |
|------|------------------------|-------------------|
| **Executive assistant (conceptual)** | Deadlines, reminders, follow-up cases, coordination notes | WF-03, WF-04 cross-cutting |
| **Reporting specialist (conceptual)** | ReportRecord status, WF-01 stages, approval gates | WF-01 MVP |
| **Document operations (conceptual)** | DocumentRecord status, approval before routing | WF-02 |
| **Reviewer / approver (human)** | ApprovalRequest — not a separate system | Any workflow with `PENDING_APPROVAL` |
| **Studio leadership (read-only)** | Completion visibility, escalation records | WF-05, closed case summaries |

Secondary users are **roles**, not separate product logins — authentication and RBAC are **SAFE UNKNOWN**.

---

## 5. Future consumers

| Future consumer | Intended relationship | Status |
|-----------------|----------------------|--------|
| **HomeGateway cockpit** | Display OPS case/report/deadline signals; optional quick links | **SAFE UNKNOWN** — charter required |
| **ATLAS read API** | Machine pull of C-01–C-09 for case context | **SAFE UNKNOWN** — ATLAS implementation |
| **Evidence / EAR storage** | Attach drafts and completion proofs | **SAFE UNKNOWN** — infrastructure |
| **MIG / ORCA / MetaBOT adapters** | Push evidence into report assembly | **Forbidden to assume** in v1 — human attestation only |

Future consumers **must not** bypass human approval gates or become shadow writers of canonical ATLAS fields.

---

## 6. Non-consumers (explicit)

| Actor | Why not a consumer |
|-------|-------------------|
| **End client** | Receives deliverables; does not operate OPS cases |
| **MetaBOT runtime** | Does not read OpsCase; external SEO lane |
| **ORCA / MIG runtimes** | Supply evidence only via human attachment to reports |
| **Autonomous MARS agents** | No OPS agent implementation in Phase 4 |
| **Registry automation** | OPS pack is not a registry router |

---

## 7. Consumer ↔ conceptual role map

From [OPS-AGENT-DECOMPOSITION-v1.md](OPS-AGENT-DECOMPOSITION-v1.md) — **roles only, not runtime agents**:

| Conceptual role | Primary consumer alignment | Workflow emphasis |
|-----------------|---------------------------|-------------------|
| **Client Reporting Agent** | Reporting role / operator | WF-01 |
| **Document Operations Agent** | Document operations role / operator | WF-02 |
| **Executive Assistant Agent** | EA role / operator | WF-03, WF-04, cross-cutting |

One operator may fulfill all three roles in small studio contexts.

---

## 8. Operator-centered principles

| Principle | Statement |
|-----------|-----------|
| **OC-01** | Workflow progression is **human-triggered** — no autonomous case closure |
| **OC-02** | Status vocabulary serves **operator clarity**, not client-facing branding |
| **OC-03** | Missing data is surfaced to the **operator**, not hidden for client polish |
| **OC-04** | Integrations, when they exist, **assist** the operator — they do not replace approval |

---

## 9. SAFE UNKNOWN

| Topic | Unknown | Verification |
|-------|---------|--------------|
| Multi-operator assignment | Whether cases support co-owners | Future ops tooling charter |
| External reviewer access | Client portal for report status | Out of MVP — explicit charter if ever |

---

*OPS Consumer Model v1 · Phase 4 · Business Operations Domain.*
