# OPS MVP Scope v1

**Status:** **documented** — approved Foundation MVP declaration.  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Parent:** [../README.md](../README.md) · [OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](../workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md)

---

## Approved MVP

**Monthly Client Reporting Control MVP**

A **human-supervised** operational capability to run a **repeatable monthly client reporting cycle**: from period trigger through evidence collection, draft, review, approval, delivery preparation, and completion recording — **without** claiming automation, integrations, or runtime.

---

## In scope

| # | Item | Notes |
|---|------|-------|
| **S-01** | Monthly reporting **workflow** (10 stages) | Normative: [OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](../workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md) |
| **S-02** | ATLAS **reference model** for report context | Consumer rules in [OPS-ATLAS-RELATIONSHIP-v1.md](OPS-ATLAS-RELATIONSHIP-v1.md) |
| **S-03** | Missing data review stage | Block or qualify delivery when canonical refs absent |
| **S-04** | Operator review and approval gates | No client send without human approval |
| **S-05** | Completion recording and closing status | Operational metadata only — not ATLAS promotion |
| **S-06** | Conceptual **Client Reporting Agent** role | Decomposition doc — not implemented |
| **S-07** | Evidence collection from **human-attested** sources | MIG/ORCA/MetaBOT/WPilot/OCPilot cited as attachments only |

---

## Out of scope

| # | Item | Rationale |
|---|------|-----------|
| **O-01** | Runtime, CLI, services | Foundation pass — docs only |
| **O-02** | Autonomous agents | Conceptual roles only |
| **O-03** | n8n / MARS orchestration | No automation claims |
| **O-04** | Databases and persistence layout | Deferred to future infrastructure charter |
| **O-05** | CRM / ERP features | Boundary exclusion |
| **O-06** | Accounting postings and payment confirmation | Authority exclusion |
| **O-07** | Legal drafting and contract authority | Human/legal outside OPS |
| **O-08** | ATLAS write-back or entity promotion | ATLAS governance separate |
| **O-09** | Registry registration of OPS | Explicitly excluded in Foundation v1 |
| **O-10** | Live integrations (MetaBOT, MIG, ORCA APIs) | Not implemented — **forbidden to claim** |

---

## Deferred

| # | Item | Trigger for reconsideration |
|---|------|----------------------------|
| **D-01** | Document Operations workflows | Separate charter after reporting MVP pilot |
| **D-02** | Executive Assistant automation (reminders) | HomeGateway or ops tooling charter |
| **D-03** | Weekly / quarterly reporting cadences | Operator demand + charter |
| **D-04** | ATLAS machine-readable consumer contract | ATLAS implementation milestone |
| **D-05** | OPS `project_id` registry entry | Governance registration pass |
| **D-06** | Evidence storage standard path | EAR / infrastructure decision |
| **D-07** | Template library under `projects/ops/templates/` | Post-pilot documentation pass |

---

## Success criteria (MVP — human-operated)

| # | Criterion | Verification |
|---|-----------|--------------|
| **SC-01** | Operator can execute all **10 workflow stages** using documentation alone | Walkthrough checklist |
| **SC-02** | Draft report cites ATLAS refs **or** explicit **SAFE UNKNOWN** attestation | Sample report review |
| **SC-03** | No client delivery without recorded **Approval** stage | Process audit |
| **SC-04** | Missing canonical data triggers **Missing Data Review** — no silent invention | Negative test scenario |
| **SC-05** | Completion record exists for closed cycle | Operational artifact present |
| **SC-06** | No document claims runtime, automation, or live integration | Governance spot-check |

---

## Human approval requirements

| Gate | Requirement |
|------|-------------|
| **HA-01** | **Reporting Trigger** — operator confirms client and period |
| **HA-02** | **Draft Report Preparation** — operator owns narrative; AI assist optional, not authoritative |
| **HA-03** | **Operator Review** — explicit review pass before approval |
| **HA-04** | **Approval** — named human approves client delivery |
| **HA-05** | **Client Delivery Preparation** — human chooses channel and sends |
| **HA-06** | **Canonical corrections** — any identity/requisite fix goes to ATLAS path, not OPS-only edit |

---

## Risk boundaries

| Risk | Boundary / mitigation |
|------|----------------------|
| **R-01** Parallel client registry in OPS | Anti-duplication rules; ATLAS wins |
| **R-02** Report sent with invented requisites | Stage 5 + AD-06; omit or SAFE UNKNOWN |
| **R-03** Autonomy creep (“agent sent the report”) | Conceptual roles labeled not implemented |
| **R-04** False integration claims | Workflow states no automation; governance GC-OPS-008 alignment |
| **R-05** Legal/financial overreach | Boundaries X-04–X-06; human authority outside OPS |
| **R-06** Premature registry/topology edits | Foundation charter forbids — reduces ecosystem noise |

---

*OPS MVP Scope v1 · Monthly Client Reporting Control MVP.*
