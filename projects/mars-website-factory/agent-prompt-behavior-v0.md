# MARS Website Factory — Agent Prompt Behavior v0

**Status:** **documentation only** — **behavioral rules** for any agent (planned, legacy-bridge, or a human acting as an agent) executing Website Factory prompts. **Not** a runtime policy engine, **not** a guarantee of LLM behavior, **not** evidence of automated enforcement.

**Version:** v0.

**Related:** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [agent-map.md](agent-map.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [`../../workflows/task-contract-v0.md`](../../workflows/task-contract-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

The factory’s **planned specialist agents** ([agent-map.md](agent-map.md)) and the **humans** acting as those agents today share a single behavioral contract: how to interpret and execute a structured factory prompt **honestly**. This document defines that contract in prose.

It does **not**:

- describe LLM provider routing (see `../../models/`),
- define a runtime policy engine,
- claim that any factory agent is implemented.

---

## 2. Core behavioral rules

### 2.1 Do not fabricate

- Never invent **artifact identifiers**, **registry rows**, **field values**, or **upstream approvals** that are not present in named artifacts.
- Never invent **performance numbers**, **SERP positions**, **build statuses**, or **runtime states**.
- If evidence is missing, the response is **SAFE UNKNOWN**, not a confident guess.

### 2.2 Escalate uncertainty

- Use the system signal vocabulary ([`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md)):
  - **UNKNOWN** — required binding missing; hard stop for the affected branch.
  - **SAFE UNKNOWN** — bounded continuation allowed only with explicit assumption.
  - **NEED HUMAN APPROVAL** — HITL is required before proceeding.
  - **STRUCTURE CHANGE** — scope or contract must shift before continuing.
  - **SECURITY RISK** — stop line until governance review.
- Escalation is **inside the report**, not in side-channels.

### 2.3 Respect upstream artifacts

- Upstream artifacts ([artifact-types-v0.md](artifact-types-v0.md)) carry **immutability rules** (e.g. approved blueprint baseline, frozen design baseline).
- Do **not** silently mutate, re-interpret, or contradict an upstream artifact.
- If a contradiction is discovered, emit **STRUCTURE CHANGE** and stop; do not “fix” it inline.

### 2.4 Preserve contracts

- The blueprint, design handoff, frontend handoff, QA payload, and artifact-architecture documents are **field vocabularies** ([page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md)).
- Do not introduce new fields without an explicit **contract amendment** request flagged as **STRUCTURE CHANGE**.

### 2.5 Avoid hidden assumptions

- Every assumption that influences the output **must appear** in the report under `allowed assumptions` or `SAFE UNKNOWN`.
- Hidden assumptions (about stack, hosting, CI, CMS, runtime, n8n, Cursor automation) are **forbidden** ([safe-unknown-boundary.md](safe-unknown-boundary.md)).

### 2.6 No fake completion claims

- “Done” is only valid when:
  - the produced artifact matches the named contract,
  - the report enumerates created/updated files,
  - SAFE UNKNOWN items are listed,
  - downstream QA / HITL is **not** preempted by the agent.
- Saying “shipped”, “live”, “deployed”, “tested in CI”, or “SEO-verified” without in-repo evidence is forbidden.

### 2.7 No fake QA approval

- An agent **does not** approve its own work or another agent’s artifact.
- A production agent **does not** emit a QA payload; QA is a separate prompt and a separate lane ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-validation-model.md](qa-validation-model.md)).
- A QA agent **does not** waive its own blockers; waivers are HITL ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)).

### 2.8 No fake runtime assumptions

- The agent must **not** assume:
  - a MARS daemon executes this prompt,
  - n8n is bound,
  - the Validator runs automatically,
  - Figma export pipelines fire,
  - Cursor enforces these standards beyond user/operator discipline.
- The default execution model is **human-supervised Cursor** ([`../../governance/execution-model.md`](../../governance/execution-model.md)).

### 2.9 No uncontrolled expansion

- The agent **must not** silently expand scope:
  - editing files outside the named `scope.in`,
  - touching neighboring stages,
  - producing artifact classes not requested,
  - committing or pushing when not asked,
  - “while we’re here” edits.
- Scope drift = **STRUCTURE CHANGE** request, not unilateral expansion.

---

## 3. Operating philosophies

### 3.1 Deterministic intent philosophy

Even though LLM outputs are probabilistic, the **intent** of a factory prompt is **deterministic**:

- the produced artifact class is fixed,
- the contract fields are fixed,
- the scope is fixed,
- the escalation paths are fixed.

The agent’s job is to **reduce variance** toward that intent: cite contracts, mirror upstream identifiers, prefer explicit reference over paraphrase, and surface gaps rather than smooth them over.

### 3.2 Bounded execution philosophy

Every prompt has a **boundary** (scope, artifacts in, artifacts out). The agent runs **inside** that boundary. Anything outside is either:

- another stage’s prompt (orchestrator’s job to issue), or
- HITL territory (human’s job to decide).

The agent **does not** route, **does not** schedule, **does not** chain prompts on its own behalf.

### 3.3 Artifact-first behavior

The agent thinks in **artifacts**:

- read upstream artifact → produce downstream artifact;
- name the artifact_id;
- reference contract fields by name;
- treat artifact mutability per [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md).

Outputs that are not anchored to a named artifact are **drafts**, not factory deliverables.

### 3.4 HITL escalation

- If a decision would alter scope, approve a freeze, waive a blocker, or release a deliverable, the agent **stops** and emits a HITL escalation.
- HITL is not negotiation inside the agent; it is the **next step outside** the agent ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)).

---

## 4. Relationship to SAFE UNKNOWN

The agent’s default response to missing evidence is **SAFE UNKNOWN** ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)):

- write the assumption explicitly,
- bound the assumption (what it covers, what it does not),
- name the artifact or fact that would resolve it,
- do not claim verification without evidence,
- never use SAFE UNKNOWN to hide an avoidable check.

---

## 5. Relationship to Validator

**Validator Agent** ([agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md)) is **planned / legacy-bridge** with depth **TBD**.

The factory agent must:

- treat Validator as **complementary**, not a substitute for specialist QA;
- not claim Validator has run unless a Validator report is present;
- not preempt Validator findings (do not waive cross-cutting concerns).

If Validator is not invoked, the agent says so — **SAFE UNKNOWN** on cross-cutting checks.

---

## 6. Relationship to Workflow v0

Each behavior above maps onto [website-factory-workflow-v0.md](website-factory-workflow-v0.md):

| Behavior rule | Workflow anchor |
|---------------|-----------------|
| Do not fabricate | Stage SAFE UNKNOWN escalation rows |
| Respect upstream artifacts | Stage `input artifacts` rows |
| Preserve contracts | Registries used / contracts cited |
| No fake QA approval | S06, S09, S12, S13 QA stages |
| No fake runtime assumptions | §“No runtime / autonomy claims” of workflow v0 |
| HITL escalation | Stage `HITL requirements` rows |
| No uncontrolled expansion | Stage `scope_in` / `scope_out` discipline |

---

## 7. Behavioral examples

### 7.1 GOOD — handling a missing CTA target

```text
Finding: blueprint references CTA target /contact, but IA pack has no /contact.
Action:
  - emit STRUCTURE CHANGE in REPORT
  - stop blueprint generation for this CTA
  - reference IA artifact_id and missing slug
  - propose two resolution paths (add IA slug; reuse /lead-form)
  - do not silently retarget the CTA
```

### 7.2 BAD — silently retargeting

```text
"I noticed there's no /contact, so I changed the CTA to /lead-form."
Why bad:
  - violates §2.3 (respect upstream artifacts)
  - violates §2.5 (hidden assumption)
  - violates §2.9 (uncontrolled scope expansion)
```

### 7.3 GOOD — frontend prompt with missing CI evidence

```text
SAFE UNKNOWN: CI job name not provided in handoff;
              cannot assert green build.
Action in REPORT:
  - list SAFE UNKNOWN: build verification
  - propose: run gulp build locally and record output
  - do not claim "green build"
```

### 7.4 BAD — asserting green build without evidence

```text
"All tests pass, build is green."
Why bad:
  - violates §2.1 (fabrication)
  - violates §2.6 (fake completion claim)
```

### 7.5 GOOD — QA prompt with ambiguous severity

```text
Finding: heading hierarchy unclear due to missing H1 in section.
Severity: warn (cannot confirm blocker without IA evidence).
Confidence: medium.
Escalation: NEED HUMAN APPROVAL only if SEO QA disagrees.
```

### 7.6 BAD — auto-waiving a blocker

```text
"This blocker is minor, marking it resolved."
Why bad:
  - violates §2.7 (fake QA approval / agent waiver)
  - waivers require HITL per hitl-prompt-boundary-v0.md
```

---

## 8. Non-claims

- This document does **not** guarantee any LLM will follow these rules.
- It does **not** ship a runtime that enforces them.
- It does **not** replace human review at HITL gates.

What it **does** do is provide a **shared behavioral language** so prompts, reports, and reviews use the same vocabulary across the factory.

---

## 9. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial agent prompt behavior (documentation only). |
