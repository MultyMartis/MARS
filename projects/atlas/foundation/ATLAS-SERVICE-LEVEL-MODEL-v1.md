# ATLAS Service Level Model v1

**Status:** **documented** — Phase 8 stewardship expectations (normative guidance).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) · [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) · [ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md)  
**Is not:** runtime SLA, API latency SLO, ticketing SLA, automated enforcement, penalty contract.

**Important:** This document defines **governance expectations** for human stewards — **not** hard operational SLAs, uptime targets, or machine-measured deadlines.

---

## 1. Purpose

Define **stewardship expectations** for review timeliness, stale proposal handling, dispute resolution, registry health review, and capacity — so ATLAS operations remain accountable as the registry grows.

---

## 2. Service level philosophy

| Principle | Meaning |
|-----------|---------|
| **Expectations, not contracts** | Guidance for humans — not legal SLA |
| **Risk-proportional** | P0 disputes reviewed before P4 bulk import |
| **Quality trump** | Missing expectation is better than false active |
| **Transparency** | Backlog visible to Owner — not hidden |
| **Stop when exceeded** | STOP-03 when capacity unsustainable |

---

## 3. Review expectations

### 3.1 Triage windows (stewardship guidance)

| Queue class | Stewardship expectation | Notes |
|-------------|-------------------------|-------|
| **P0 — Blocker** | Same operational cycle (typically within 1–2 business days) | D1, disputed OWNER, STOP |
| **P1 — Dependency** | Within current population sprint window | Wave-critical |
| **P2 — Consumer blocker** | Within agreed population phase | Certified consumers |
| **P3 — Routine** | Within standard review window (e.g., 2–4 weeks) | Adjustable by Owner |
| **P4 — Bulk import** | Batch scheduled; spot-check same window as batch | No mass same-day attest |

**SLM-01:** These are **targets for stewards**, not machine timers.

**SLM-02:** Missing a target **triggers escalation**, not auto-outcome.

### 3.2 Review quality expectations

| Expectation | Standard |
|-------------|----------|
| Rationale recorded | Every attest, reject, defer |
| Evidence tier explicit | No implicit E0 for high-risk claims |
| Duplicate search | Pre-attest for org/person |
| Boundary smell check | CRM/PM fields rejected at intake |

---

## 4. Stale proposal handling

**Decision (Architectural Analysis #4):** Unresolved proposals **age** through tiers — they **never** auto-promote.

### 4.1 Aging tiers

| Tier | Condition (guidance) | Steward action | Owner action |
|------|----------------------|----------------|--------------|
| **Fresh** | Within standard P3 window | Normal review | — |
| **Aging** | Approaching window end | Document blocker; contact proposer | — |
| **Stale** | Beyond standard window | Health flag; prioritize or defer rationale | Review queue report |
| **Abandoned** | Proposer unresponsive, no evidence path | Recommend reject | Approve bulk reject or UNKNOWN |

### 4.2 Stale proposal rules

| Rule ID | Rule |
|---------|------|
| **STALE-01** | Stale **≠** active — timeout never promotes |
| **STALE-02** | Stale **disputes** escalate to Owner before stale routine proposals |
| **STALE-03** | Owner publishes **acceptance** of abandon/reject batch |
| **STALE-04** | Consumer-originated stale → notify consumer role — not silent drop |

### 4.3 Relationship to health review

Stale proposal count is a **health dimension** ([ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md) HD-06).

---

## 5. Dispute handling expectations

| Dispute class | Stewardship expectation |
|---------------|-------------------------|
| **Material structural** (OWNER, merge) | P0 — same operational cycle |
| **Evidence tier conflict** | Within P1 window |
| **Consumer challenge** | Acknowledge within 1 business day; resolve per class |
| **Owner escalated** | Owner decision within agreed arbitration window (e.g., 2 weeks) |

**SLM-D-01:** Unresolved dispute **> arbitration window** → registry health **red** flag; population may halt on affected subgraph (STOP-04).

**SLM-D-02:** Dispute resolution **documents outcome** — attest one, merge, separate, UNKNOWN.

---

## 6. Registry health review expectations

| Activity | Frequency (guidance) | Owner |
|----------|---------------------|-------|
| **Light health scan** | Monthly (steward) | Steward |
| **Full health review** | Quarterly | Steward + Owner |
| **Post-wave review** | After each population wave | Steward |
| **Post-incident review** | After STOP trigger | Owner |

**SLM-H-01:** Health review **produces written summary** — even if “green.”

**SLM-H-02:** Red health dimension **requires action plan** — not observation only.

Details: [ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md).

---

## 7. Capacity and STOP-03

### 7.1 Capacity signals

| Signal | Interpretation |
|--------|----------------|
| Queue depth growing > 2× standard window | Capacity stress |
| P0 items waiting > triage expectation | Critical gap |
| Steward unavailable > 1 week without interim | Continuity breach |
| Import batch > steward spot-check capacity | Defer batch attest |

### 7.2 STOP-03 expectation

When steward capacity **exceeded**:

1. **Pause new active promotions** ([ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) STOP-03).
2. Owner notified **same operational cycle**.
3. Owner assigns interim steward or reprioritizes queue.
4. **Proposed intake** may continue if queue hold discipline maintained.

**Decision (Architectural Analysis #5):** No steward → Owner assumes duties; same STOP behavior applies if Owner also unavailable → **global promotion pause** until coverage restored.

---

## 8. Population progression expectations

| Milestone | Expectation |
|-----------|-------------|
| Wave start | Owner confirms prerequisites |
| Wave complete | Health review before next wave |
| Wave skip exception | Owner written risk acceptance (POP-W-04) |
| Population freeze | Owner communicates to consumers |

---

## 9. Consumer-facing expectations

| Expectation | ATLAS side | Consumer side |
|-------------|------------|---------------|
| Proposal acknowledgment | Steward confirms queue entry | Consumer supplies evidence |
| Challenge response | Steward triage per dispute class | Consumer provides counter-evidence |
| UNKNOWN gaps | Documented — not hidden | Surface in UI (AT-UK-03) |
| Certification audit | Observer + Owner periodic | Mapping doc maintained |

**SLM-C-01:** ATLAS **does not** guarantee consumer operational deadlines — consumers plan around **UNKNOWN** and review windows.

---

## 10. Escalation expectations

| From | To | When |
|------|-----|------|
| Steward | Owner | Stale dispute, split, STOP, repeated violation |
| Owner | Architect (L3) | Expansion conflict, ecosystem drift |
| Health review | Owner | Any red dimension |

---

## 11. What this model does not define

| Excluded | Reason |
|----------|--------|
| API response time | Not Phase 8 |
| 99.9% uptime | Runtime concern |
| Ticket priority automation | Forbidden automation scope |
| Penalties for stewards | HR — out of scope |
| Legal deadlines | Consumer operational |

---

## 12. Non-deliverables

No SLA dashboard, alerting rules, or contractual SLA text.

---

*ATLAS Service Level Model v1 — Phase 8 Foundation. Documentation only.*
