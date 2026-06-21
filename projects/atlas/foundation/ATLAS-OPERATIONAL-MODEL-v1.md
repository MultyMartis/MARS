# ATLAS Operational Model v1

**Status:** **documented** — Phase 8 Operational Governance Foundation (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md)  
**Companion:** [ATLAS-ROLE-MODEL-v1.md](ATLAS-ROLE-MODEL-v1.md) · [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) · [ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md) · [ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md)  
**Is not:** runtime, software, APIs, databases, ticketing systems, workflow automation, helpdesk, CRM operations, project management, administrative execution.

**Phase 1–7 constraint:** Does not modify approved Phase 1–7 foundations. Consolidates operational governance deferred in Phase 4–7.

---

## 1. Purpose

Define **how ATLAS is operated** as a human-supervised Business Reality Registry — who governs reality, how proposals flow, how quality is stewarded, and how the registry scales without becoming an operational authority.

**Normative statement:**

> **Operating ATLAS** means supervising **canonical business reality** — intake, review, attestation, dispute resolution, registry health, and population progression — under documented human roles and boundaries.  
> **Operating ATLAS** does **not** mean executing business work, running consumer workflows, or replacing operational systems.

---

## 2. Operational philosophy

### 2.1 ATLAS as reality authority, not operational authority

| ATLAS operates | ATLAS does not operate |
|----------------|------------------------|
| Canonical identity and structure | Client reporting cycles |
| Attestation and dispute resolution | Invoice approval |
| Registry health stewardship | Task assignment |
| Population wave progression | CRM pipeline management |
| Boundary enforcement | Document filing workflows |
| Consumer semantic alignment | SEO or campaign execution |

Reaffirms [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §1 and [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) AD-01–AD-13.

### 2.2 Human-supervised governance only

All operational decisions that affect **canonical truth** require **qualified humans**. Agents, imports, and consumers may **propose** and **flag**; they **cannot** replace attestation ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §2.1).

### 2.3 Quality over throughput

Registry operation prioritizes **correct structural reality** over speed of population. Mass promotion without review is a **governance violation**, not an efficiency win (AT §5.2, POP-GV quality controls).

### 2.4 Explicit uncertainty

Operational posture prefers **SAFE UNKNOWN** and **proposed** over **active wrong** ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-10, AT-UK-01).

### 2.5 One graph, many consumers

Operational governance maintains **one canonical graph**. Consumer-local copies, shadow registries, and parallel ontologies are **operational failures** to be corrected — not alternate truths.

---

## 3. What operating ATLAS means

**Operating ATLAS** is the sustained human activity of:

| Activity | Description |
|----------|-------------|
| **Intake supervision** | Accepting, triaging, and queueing reality proposals from stewards, consumers, and agents |
| **Review execution** | Evidence, duplicate, boundary, and dispute reviews per attestation model |
| **Attestation governance** | Promoting records to **active** canonical state with traceable human decision |
| **Dispute arbitration** | Resolving conflicting claims without granting consumers rewrite rights |
| **Registry health stewardship** | Periodic assessment of duplicate pressure, orphans, stale proposals, population quality |
| **Population progression** | Advancing waves per [ATLAS-POPULATION-STRATEGY-v1.md](ATLAS-POPULATION-STRATEGY-v1.md) with stop/resume discipline |
| **Consumer alignment** | Ensuring consumers read ATLAS semantics without forking entity classes |
| **Change governance** | Routing expansion, taxonomy, and contract changes per [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) |
| **Escalation management** | Moving issues from steward → owner → program when thresholds or severity demand |

These activities are **documentation-first** and **human-process** in Phase 8. Implementation tooling may support them later; tooling does not define them.

---

## 4. What operating ATLAS does not mean

Operational drift into the following domains is **explicitly forbidden**:

| Drift vector | Why forbidden | Correct owner |
|--------------|---------------|---------------|
| **Helpdesk / ticket resolution** | Resolves operational incidents, not structural truth | Consumer or ops support |
| **CRM operations** | Pipeline, deals, account scoring | CRM / commercial consumers |
| **Project management** | Tasks, sprints, delivery status | PM tools / programs |
| **Administrative execution** | Invoicing, payroll, contract signing | Finance / legal / OPS workflows |
| **Document management** | Version control of contracts and reports | Secretary / DMS (future consumer) |
| **Marketing execution** | Campaigns, SERP, content | MIG / ORCA |
| **Runtime operations** | Deploy, monitor, incident response | Infrastructure / WPilot |
| **Auto-sync as truth** | Consumer cache overwriting ATLAS | Forbidden (POP-B-01, RA-D08) |

**Rule OP-BAN-01:** If an activity answers “**what work is happening now?**” it belongs in a **consumer system**, not ATLAS operations.

**Rule OP-BAN-02:** If an activity answers “**who exists and how are they structurally linked?**” it may belong in **ATLAS operations**.

---

## 5. Operational responsibilities

### 5.1 Ultimate ownership — Program Owner

**Decision (Architectural Analysis #1):** The **Program Owner** holds **ultimate accountability** for ATLAS as a MARS program — foundation integrity, operational policy, steward delegation, population freeze/resume, split approval, and escalation terminus.

The Program Owner is **not** a super-steward for every intake item; they **own the system**, not every record.

| Accountability | Scope |
|----------------|-------|
| Foundation amendments | Expansion, boundary shifts, consumer contract changes |
| Delegation policy | Written steward attestation delegation |
| Population authority | Wave exceptions, STOP triggers, freeze/resume |
| Dispute terminus | Unresolved disputes after steward investigation |
| Registry health sign-off | Accepts or acts on health review findings |
| Roster continuity | Ensures steward coverage or documented fallback |

See [ATLAS-ROLE-MODEL-v1.md](ATLAS-ROLE-MODEL-v1.md) §3.1.

### 5.2 Day-to-day operation — Registry Steward

The **Registry Steward** executes intake, review, attestation (when delegated), defer/reject, and routine dispute investigation.

**Decision (Architectural Analysis #2):** **Stewardship may be delegated** — one or more named stewards under **written delegation** from Program Owner (GV-02, POP-GV-01, AT §5.1).

### 5.3 Attestation delegation

**Decision (Architectural Analysis #3):** **Attestation may be delegated** to stewards for entity and relationship promotion to **active**, merge approval, and alias canonical use — **except**:

| Action | Delegation |
|--------|------------|
| Entity/relationship → active | Steward (written delegation) or Owner |
| Merge | Steward (delegated) or Owner |
| **Split** | **Owner only** (IGV-S01) |
| Expansion (new type/class) | **Owner only** |
| Boundary override | **Never** |

### 5.4 Review and quality — Reviewer role

**Reviewers** (typically stewards; Owner on escalation) perform structured reviews defined in [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md). Review is **not** a separate authority from stewardship in MVP operations — it is the **steward's operational duty**.

### 5.5 Population progression — shared stewardship

**Population progression** is owned **jointly**:

| Owner | Responsibility |
|-------|----------------|
| **Program Owner** | Wave strategy, exceptions, halt/resume |
| **Registry Steward** | Wave execution, queue discipline, quality gates |
| **Population governance docs** | Normative rules (Phase 7 — not redefined here) |

Stewards **do not** unilaterally skip waves (POP-W-04).

### 5.6 Consumer boundary — Consumer role

Consumers **propose** and **challenge**; they **never attest active** (POP-C-01, AT §8.1).

**Decision (Architectural Analysis #7):** Consumer disagreement escalates via **challenge → dispute → steward review → owner escalation** — never via local canonical overwrite. See [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) §8.

---

## 6. Operational boundaries

### 6.1 Inside operational scope

| Boundary | Operational touch |
|----------|-------------------|
| Proposal lifecycle | Intake → review → attest / defer / reject |
| Canonical state | active, proposed, disputed, deprecated, SAFE UNKNOWN |
| Evidence tier assignment | E0–E3 at review |
| Identity duplicate flows | D1–D5 triage |
| Relationship slot conflicts | disputed until resolved |
| Population waves | Order and stop/resume |
| Registry health reviews | Periodic human assessment |
| Consumer certification posture | Semantic compliance, not ops execution |

### 6.2 Outside operational scope

| Boundary | Treatment |
|----------|-----------|
| Consumer workflow status | Consumer-local only (MAP-01) |
| OPS report drafts | OPS operational artifacts |
| Financial facts | Not attested in ATLAS MVP |
| Legal interpretation | Human/legal process — ATLAS holds pointers only |
| Implementation uptime | Future runtime concern — not Phase 8 |

### 6.3 OPS coexistence

**Decision (Architectural Analysis #8):** OPS **Clients, Contacts, Services, Agreements, Requisites** are **logical OPS views**, not ATLAS entity classes. Canonical mapping is defined in [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md). ATLAS operations **must not** adopt OPS vocabulary as entity taxonomy.

---

## 7. Operating principles

| ID | Principle | Rule |
|----|-----------|------|
| **OP-P-01** | **Reality, not work** | Operate structural truth only |
| **OP-P-02** | **Attest, don't infer** | No active promotion without human attestation record |
| **OP-P-03** | **Written delegation** | Steward authority requires documented delegation |
| **OP-P-04** | **Traceability** | Every active record should have attest trail (conceptual until implementation) |
| **OP-P-05** | **Stop before harm** | STOP-01–STOP-07 trump throughput |
| **OP-P-06** | **Defer beats reject** | When evidence is pending, prefer **defer** over **reject** if claim may be valid |
| **OP-P-07** | **Reject beats wrong** | Boundary violations and fabricated evidence → **reject** |
| **OP-P-08** | **Dispute blocks dependency** | No new irreversible canonical dependencies on **disputed** nodes |
| **OP-P-09** | **Health is reviewed** | Registry health is stewarded, not only reacted to |
| **OP-P-10** | **Grow deliberately** | Expansion and population follow written governance — no urgency bypass |

---

## 8. Registry stewardship principles

Extends [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §5.2 for operational context:

| Principle | Operational expression |
|-----------|------------------------|
| **Quality over throughput** | Review queue may backlog; false active is worse |
| **Prefer UNKNOWN over wrong** | Explicit gaps over invented orgs or edges |
| **One graph** | Duplicates merged or disputed — not parallel active |
| **Traceability** | Attestor, tier, rationale captured conceptually |
| **Wave discipline** | Population order reduces chaos |
| **Consumer discipline** | No shadow canonical stores |
| **Periodic health** | Scheduled review per [ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md) |
| **Continuity** | Steward absence triggers owner fallback — not silent promotion |

### 8.1 Steward unavailability

**Decision (Architectural Analysis #5):** When **no steward is available**:

1. **Program Owner** assumes steward duties or designates interim steward in writing.
2. **New active promotions pause** until coverage restored (extends STOP-03).
3. **Proposed intake may continue** only if queue can be held without promotion.
4. **Disputes and D1 duplicates** require **owner action** — cannot age indefinitely.
5. **No agent or consumer** may attest during gap.

---

## 9. How ATLAS continues operating as it grows

### 9.1 Growth dimensions

| Dimension | Operational response |
|-----------|---------------------|
| **Record volume** | Additional stewards with delegation; batch review discipline |
| **Consumer count** | Certification checks; mapping document requirements |
| **Proposal rate** | Queue prioritization; stale proposal handling (SLM) |
| **Taxonomy expansion** | Owner-led expansion review — stewards do not invent types |
| **Dispute rate** | Health review trigger; owner arbitration capacity |
| **Geographic / org complexity** | Alias and homonym discipline — not new entity classes by default |

### 9.2 Scaling without authority drift

```text
                    Program Owner
                   (policy · split · freeze)
                          │
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
      Steward A     Steward B     Reviewer pool
      (intake)      (relationships) (spot audit)
            │             │             │
            └─────────────┴─────────────┘
                          │
              One canonical graph
                          │
            Consumers read · propose · challenge
            (never attest · never fork taxonomy)
```

**OP-SCALE-01:** Adding stewards **scales throughput**; it does **not** create regional canonical forks.

**OP-SCALE-02:** Consumer-specific “fast paths” that bypass attestation are **forbidden**.

---

## 10. Unresolved proposal aging

**Decision (Architectural Analysis #4):** Proposals age through **stewardship tiers**, not automatic promotion or silent expiry:

| Age tier | State | Steward expectation | Escalation |
|----------|-------|---------------------|------------|
| **Fresh** | proposed / queued | Triage within stewardship window | — |
| **Aging** | proposed, evidence partial | Steward documents blocker; consumer may be asked for evidence | — |
| **Stale** | proposed beyond stewardship window | Health flag; owner notified | Owner: defer rationale, reject, or prioritize |
| **Abandoned** | proposer silent, no evidence | **Reject** or **SAFE UNKNOWN** — never auto-active | Owner sign-off on bulk abandon |

**OP-AGE-01:** Stale proposals **do not** become active by timeout.

**OP-AGE-02:** Stale **disputes** escalate to owner faster than stale routine proposals.

Details: [ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md) §4.

---

## 11. What registry health means (summary)

**Decision (Architectural Analysis #6):** **Registry health** is the **assessed condition** of the canonical graph and its governance queues — not uptime or query latency.

Health dimensions are defined in [ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md). Operational model treats health review as **mandatory stewardship**, not optional analytics.

---

## 12. Operational package map

| Document | Role in operations |
|----------|-------------------|
| [ATLAS-ROLE-MODEL-v1.md](ATLAS-ROLE-MODEL-v1.md) | Who does what |
| [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) | How work flows |
| [ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md) | Stewardship expectations |
| [ATLAS-REGISTRY-HEALTH-MODEL-v1.md](ATLAS-REGISTRY-HEALTH-MODEL-v1.md) | Quality monitoring concept |
| [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md) | Ecosystem vocabulary alignment |
| [ATLAS-FOUNDATION-INDEX-v1.md](ATLAS-FOUNDATION-INDEX-v1.md) | Navigation and authority hierarchy |

Normative semantics remain in Phases 1–7; Phase 8 **consolidates operational playbook** without duplicating attestation rules (GAP-10 resolution).

---

## 13. Non-deliverables

No runtime, APIs, databases, steward roster names, ticketing integration, workflow engine, or OPS document amendments (alignment doc is ATLAS-side; OPS doc amendment remains optional follow-up).

---

*ATLAS Operational Model v1 — Phase 8 Foundation. Documentation only.*
