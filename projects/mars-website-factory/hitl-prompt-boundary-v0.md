# MARS Website Factory — HITL Prompt Boundary v0

**Status:** **documentation only** — defines **where human-in-the-loop (HITL) approval is mandatory** in factory prompts, and how prompts cross (or stop at) those boundaries. **Not** an approval engine, **not** evidence of automated approval workflows, **not** a signing system.

**Version:** v0.

**Related:** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [artifact-types-v0.md](artifact-types-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [`../../security/approval-gates.md`](../../security/approval-gates.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

The factory has **mandatory HITL gates** at every stage that **freezes scope** or **approves release** ([workflow-map.md](workflow-map.md) §HITL checkpoints, §Artifact approval gates). This document defines:

- **where** HITL is mandatory,
- **what** an approval gate accepts as evidence,
- **how** a prompt expresses or escalates a HITL boundary,
- **what** an agent must **never** do at a HITL boundary.

It does **not** define a signing protocol, an identity provider, or a runtime approval store.

---

## 2. HITL is structural, not optional

HITL is **not** “a checkbox the agent can satisfy”. It is a **structural pause** in the workflow:

- the agent **stops**,
- a **human** issues the decision,
- the decision is recorded as an **Approval artifact** ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact),
- only then may the **next stage’s prompt** be issued.

Any prompt that asks the agent to “approve”, “sign off”, “waive”, “freeze”, or “release” is **mis-shaped** unless it is an explicit **HITL prompt** ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §3.3) targeted at a **named human approver**.

---

## 3. Mandatory HITL gates (factory map)

The factory inherits gates **G1–G7** from [workflow-map.md](workflow-map.md). For each gate, this section names the **trigger artifact**, the **typical approver**, and the **escalation signal** if HITL is missing.

| Gate | Stage(s) | Trigger artifact | Approver | Decision options | Default escalation |
|------|----------|------------------|----------|-------------------|---------------------|
| **G1** | S01 Intake / S02 Site Type Classification | Intake summary; `site_type_id` rationale | PM / lead | approve / reject / revise / park | **NEED HUMAN APPROVAL** |
| **G2** | S03 Strategic Layer | Strategy + SEO hypothesis memo | Marketing lead | approve / reject / revise / park | **NEED HUMAN APPROVAL** |
| **G3** | S04 IA + S05 Blueprint batch | IA pack; Blueprint set | PM + tech lead | approve / reject / revise / park | **NEED HUMAN APPROVAL** |
| **G4** | S08 Wireframes | Wireframe set | UX / client | approve / reject / revise | **NEED HUMAN APPROVAL** |
| **G5** | S09 Full design (design freeze) | Hi-fi design + Design QA report | Design lead / client | approve (freeze) / reject / revise | **NEED HUMAN APPROVAL** |
| **G6** | S11 Frontend + S12 Frontend QA | Frontend PR / file set + Frontend QA report | Tech + design | approve / reject / revise | **NEED HUMAN APPROVAL** |
| **G7** | S14 Human Approval + S15 Delivery | Final Validation report; risk summary | Ops / client | approve (release) / reject / hold | **NEED HUMAN APPROVAL** |

**Workflow alignment:** see [website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S01–S15 for the **stage-by-stage** `HITL requirements` rows.

---

## 4. Approval gates (per lane)

### 4.1 Design approval

- **Trigger:** design freeze proposal (S09 → frontend handoff).
- **Required evidence:** approved blueprint baseline, Design QA report, handoff pack.
- **Forbidden:** agent emitting “design approved” without a recorded G5 decision.
- **Frozen artifact rule:** post-approval design becomes an **immutable baseline** ([artifact-types-v0.md](artifact-types-v0.md) §Design artifact); changes require a re-gate.

### 4.2 SEO approval

- **Trigger:** SEO hypothesis sign-off (G2 extension for sensitive verticals).
- **Required evidence:** strategy memo + SEO hypothesis doc; competitive notes flagged honestly.
- **Forbidden:** rank claims without evidence ([safe-unknown-boundary.md](safe-unknown-boundary.md)); silent keyword pivots after G2.
- **SAFE UNKNOWN rule:** SERP/competitive facts that are not verified must be labeled.

### 4.3 Frontend approval

- **Trigger:** frontend PR / file set + Frontend QA outcome (G6).
- **Required evidence:** build outcome (or SAFE UNKNOWN), Frontend QA report, link/asset spot-check.
- **Forbidden:** “CI green” without evidence; auto-merge.
- **Source-first rule:** approval applies to **source files**, not to hand-patched `dist/`.

### 4.4 Commercial approval

- **Trigger:** commercial scope changes (e.g. CTA repositioning, pricing surface, lead-handling), legal copy, compliance impact.
- **Required evidence:** strategy memo + risk note; legal review where applicable.
- **Forbidden:** copy or pricing changes without HITL after G2.

### 4.5 Risk override

- **Trigger:** **NEED HUMAN APPROVAL** for a blocker waiver or for proceeding under **SAFE UNKNOWN**.
- **Required evidence:** named approver, named risk row ([`../../governance/risk-register.md`](../../governance/risk-register.md)), bounded continuation conditions.
- **Forbidden:** agent-side waiver; silent risk acceptance.

### 4.6 SAFE UNKNOWN escalation

- **Trigger:** evidence missing for a required field at a gate.
- **Required evidence:** explicit SAFE UNKNOWN entry ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).
- **Resolution paths:**
  - escalate to **UNKNOWN** (hard stop) if policy disallows continuation;
  - or accept **SAFE UNKNOWN** with bounded assumption and named approver.
- **Forbidden:** using SAFE UNKNOWN as a way to skip an avoidable check.

---

## 5. HITL prompt expression

Every HITL prompt ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §3.3) MUST contain:

1. **Gate identifier** (e.g. `G5`).
2. **Artifact under review** (`artifact_id` + class).
3. **Approver role** (named role, not “the team”).
4. **Decision options** (enumerated; the agent does not invent new ones).
5. **Evidence in** (artifacts and prior QA reports).
6. **Escalation rules** (what to do if a decision cannot be made now).
7. **Reporting requirements** — produce an **Approval artifact**:
   - decision,
   - approver,
   - date,
   - referenced artifact_id,
   - waivers (if any).

The agent does **not**:

- choose between the decision options on behalf of the human,
- soften or rephrase blockers to make approval easier,
- generate a “signed” approval artifact without a recorded human decision.

---

## 6. Escalation triggers (agent-side)

An agent must trigger HITL escalation (signal: **NEED HUMAN APPROVAL** or **UNKNOWN**) whenever any of the following are true:

- a required field cannot be evidenced;
- an upstream artifact is missing or contradicts the current one;
- a registry mismatch is detected (block / site type / contract);
- a waiver is needed for a blocker (QA lane);
- a security-sensitive surface is touched (assets, forms, scripts) → **SECURITY RISK** if applicable;
- a scope change is needed → **STRUCTURE CHANGE**;
- a runtime/automation assumption would otherwise be required.

Escalation appears in the **REPORT** ([reporting-standard-v0.md](reporting-standard-v0.md) §3 “HITL flags”).

---

## 7. Anti-patterns — “No fake autonomous approval”

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| “Design approved by AI Designer Agent.” | No agent can satisfy G5. | Issue a HITL prompt to a named design lead. |
| “Auto-waived warn-severity SEO findings.” | Waivers require HITL. | Emit **NEED HUMAN APPROVAL** with the finding intact. |
| “CI green, ready to deploy.” | Without evidence, this is a false runtime claim. | SAFE UNKNOWN on CI; deploy is HITL (G7). |
| “Approval recorded.” | Without an Approval artifact and named approver, this is fabrication. | Produce an Approval artifact only after recording a human decision. |
| “Continued under SAFE UNKNOWN.” (without approver) | Continuation requires policy or HITL agreement. | Name the approver and the bounded assumption. |
| “Re-approved with minor change.” | Frozen baselines do not “re-approve” silently. | Run the appropriate gate (G3 / G5 / G6) again. |

---

## 8. Relationship to MARS approval gates

The factory’s HITL gates are **project-scoped**. They align with — and **do not replace** — MARS-wide approval / security gates:

- [`../../security/approval-gates.md`](../../security/approval-gates.md) — system-level approval semantics.
- [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md) — signal vocabulary used in escalation.
- [`../../workflows/task-contract-v0.md`](../../workflows/task-contract-v0.md) — `hitl_gates` as a planned Task field (narrative alignment only).
- [`../../interfaces/recovery-playbooks-v0.md`](../../interfaces/recovery-playbooks-v0.md) — recovery / approval narrative where overlap exists.

Where MARS approval policy is stricter than the factory map, **MARS wins**. Where MARS is silent, factory gates apply as documented.

---

## 9. Non-claims

- This document does **not** ship an approval workflow engine.
- It does **not** imply approvers are notified automatically.
- It does **not** define cryptographic signing.
- It does **not** replace human judgment with predictable agent behavior.

What it **does** do is define **which prompts an agent must refuse to satisfy alone** and **how that refusal is worded**.

---

## 10. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial HITL prompt boundary for the Website Factory (documentation only). |
