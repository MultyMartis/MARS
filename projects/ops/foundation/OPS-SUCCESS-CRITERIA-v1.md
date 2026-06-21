# OPS — Success Criteria v1

**Status:** **documented** — domain success and failure indicators (design).  
**Program:** OPS — Business Operations Domain  
**Phase:** 4 — Operational Mission & System Positioning  
**Date:** 2026-06-04  
**Parent:** [OPS-OPERATIONAL-MISSION-v1.md](OPS-OPERATIONAL-MISSION-v1.md) · [OPS-MVP-SCOPE-v1.md](OPS-MVP-SCOPE-v1.md)  
**Is not:** SLA dashboard, automated KPI system, or runtime metrics pipeline.

---

## 1. Purpose

Define **measurable operational outcomes** for OPS at the domain level — visibility and honesty criteria that a human can verify from documentation and artifacts — **without** KPIs that require runtime, telemetry, or registry automation.

---

## 2. Design constraint

| Constraint | Rule |
|------------|------|
| **No runtime KPIs** | Metrics are **observable by human review** of cases, records, and walkthroughs |
| **No false precision** | Percentages and dashboards are **examples only** until tooling exists |
| **MVP alignment** | WF-01 criteria extend [OPS-MVP-SCOPE-v1.md](OPS-MVP-SCOPE-v1.md) SC-01–SC-06 |

---

## 3. Success criteria (domain)

### 3.1 Visibility outcomes

| ID | Outcome | How to verify (human, v1) |
|----|---------|---------------------------|
| **VC-01** | **Reporting completion visibility** | For each active reporting period, operator can state stage (draft/review/sent/closed) per client or **explicitly** “no case opened” |
| **VC-02** | **Document tracking visibility** | Document ops cases show operational status (prep/review/routed/closed) — not confused with legal signed status |
| **VC-03** | **Approval visibility** | Before client send, an approval gate is **named** (who, when) or delivery is **blocked** with documented reason |
| **VC-04** | **Deadline visibility** | Due obligations for OPS workflows are **recorded** (DeadlineRecord or equivalent human log) — not only in private calendar |
| **VC-05** | **Escalation visibility** | Blockers beyond SLA tolerance have escalation path (WF-05) or explicit leadership attestation |
| **VC-06** | **Operational coordination visibility** | OpsCase has identifiable owner and next action — not only chat history |

### 3.2 Discipline outcomes

| ID | Outcome | How to verify (human, v1) |
|----|---------|---------------------------|
| **DC-01** | **ATLAS reference discipline** | Artifacts cite ATLAS refs or **SAFE UNKNOWN** — spot-check sample reports |
| **DC-02** | **No shadow SoT** | No OPS-only master client list presented as canonical |
| **DC-03** | **Documentation honesty** | No claims of automation, live integration, or registry authority in ops artifacts |
| **DC-04** | **Workflow coverage** | Approved MVP (WF-01) executable from docs; other WFs documented for expansion |

### 3.3 Pilot-ready outcomes (WF-01)

| ID | Outcome | How to verify (human, v1) |
|----|---------|---------------------------|
| **PR-01** | Ten-stage monthly workflow completable in walkthrough | Checklist against [OPS-WF-01-MONTHLY-REPORTING-v1.md](../workflows/OPS-WF-01-MONTHLY-REPORTING-v1.md) |
| **PR-02** | Missing data review blocks or qualifies delivery | Negative test scenario |
| **PR-03** | Completion record exists for closed month | Operational artifact present |

---

## 4. Failure indicators

| ID | Indicator | Severity |
|----|-----------|----------|
| **FI-01** | Monthly reports repeatedly sent with no completion record | High — operational truth lost |
| **FI-02** | Approvals skipped for “speed” with no documented exception | High — boundary violation |
| **FI-03** | Client/org data edited only in OPS sheets, not ATLAS path | High — shadow SoT (DF-02) |
| **FI-04** | Operators cannot answer “what stage is client X report?” | Medium — VC-01 failure |
| **FI-05** | Document routing status unknown for active closings | Medium — VC-02 failure |
| **FI-06** | Deadlines exist only in personal tools, not ops record | Medium — VC-04 failure |
| **FI-07** | Docs claim MetaBOT/MIG/ORCA “auto-sync” to OPS | High — honesty failure (DF-03) |
| **FI-08** | OPS presented as replacement for ATLAS in onboarding | High — positioning failure (DF-06) |

---

## 5. Non-goals

OPS **explicitly does not** pursue these as domain success measures:

| Non-goal | Rationale |
|----------|-----------|
| **Autonomous case resolution** | Human supervision is normative |
| **100% automation coverage** | No runtime claimed |
| **Real-time client portal** | Operator-centered; client portal is separate product decision |
| **Sub-minute alerting / paging** | No on-call product in OPS v1 |
| **Financial close automation** | Accounting authority outside OPS |
| **Legal document generation authority** | Legal process outside OPS |
| **Registry completeness score** | Registration is governance pass, not ops metric |
| **Agent fleet size** | Conceptual roles only in Phase 4 |

---

## 6. Relationship to MVP success criteria

[OPS-MVP-SCOPE-v1.md](OPS-MVP-SCOPE-v1.md) defines **SC-01–SC-06** for the Monthly Client Reporting Control MVP. This document **generalizes** visibility and discipline outcomes to the full OPS domain (WF-02–WF-06 and cross-cutting models).

| MVP criterion | Domain extension |
|---------------|------------------|
| SC-01 (10 stages) | PR-01 |
| SC-02 (ATLAS refs) | DC-01 |
| SC-03 (approval) | VC-03 |
| SC-04 (missing data) | PR-02 |
| SC-05 (completion) | PR-03, VC-01 |
| SC-06 (no false claims) | DC-03 |

---

## 7. Registration-readiness signals (documentation-only)

These inform governance **without** being runtime KPIs:

| Signal | Ready when | Phase 4 state |
|--------|------------|---------------|
| Mission and positioning docs exist | Phase 4 complete | **This pass** |
| Foundation + data model + workflows complete | Phases 1–3 | **Done** |
| Human pilot report for WF-01 | Operator walkthrough recorded | **Not started** |
| Registry row + topology pointer | Governance pass | **Deferred** |

See Phase 4 report for **OPS Registration Readiness** assessment.

---

## 8. SAFE UNKNOWN

| Topic | Unknown | Verification |
|-------|---------|--------------|
| Quantitative targets | e.g. “95% reports closed by day 5” | Operator policy after pilot — not domain v1 |
| Tooling-derived metrics | Dashboards from future OPS storage | Implementation charter |

---

*OPS Success Criteria v1 · Phase 4 · Business Operations Domain.*
