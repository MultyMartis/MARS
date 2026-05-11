# MARS Website Factory — QA Prompt Rules v0

**Status:** **documentation only** — how **QA prompts** are structured, executed, and reported in the factory. **Not** an automated QA engine, **not** evidence of a running Validator, **not** a test runner.

**Version:** v0.

**Related:** [qa-validation-model.md](qa-validation-model.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md).

---

## 1. Purpose

QA in the factory is **lane-based** ([qa-validation-model.md](qa-validation-model.md)) and is **never** produced by the same prompt that built the artifact. This document defines:

- **QA prompt structure**,
- **evidence-based** QA behavior,
- **no-fake-approval** rules,
- **blocker** semantics,
- **waiver** philosophy,
- **confidence** signaling,
- **escalation** behavior,
- relationship to **Validator** and **specialist QA** agents.

It applies to all QA lanes: Design QA, SEO QA, Conversion QA, Frontend QA, and Validator-overlapping checks.

---

## 2. QA prompt structure

A QA prompt extends [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §3.4. Required sections:

| Section | Content |
|---------|---------|
| `context` | Stage anchor (S06 / S09 / S12 / S13), lane (Design / SEO / Conversion / Frontend / Validator), project. |
| `subject artifact` | `artifact_id` + class + mutability + revision. |
| `checklist reference` | Specific checklist or rule set (e.g. [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md), Frontend lane in [qa-validation-model.md](qa-validation-model.md)). |
| `evidence expectations` | What counts as evidence per [qa-result-payloads-v0.md](qa-result-payloads-v0.md): URL, selector, screenshot ref, repro step. |
| `severity scale` | Project-normalized; e.g. `info` / `warn` / `blocker` ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)). |
| `confidence rules` | When to label `low` / `medium` / `high`. |
| `escalation rules` | When to emit **NEED HUMAN APPROVAL**, **STRUCTURE CHANGE**, **SECURITY RISK**, **UNKNOWN**, **SAFE UNKNOWN**. |
| `forbidden actions` | No artifact mutation; no auto-waiver; no production claims. |
| `reporting requirements` | QA REPORT per [reporting-standard-v0.md](reporting-standard-v0.md) §4.3. |

A QA prompt **does not** include a production objective. It cannot ask the agent to “fix” the artifact under test — only to **assess** it.

---

## 3. Evidence-based QA

Every finding **must** be supported by **evidence** ([qa-result-payloads-v0.md](qa-result-payloads-v0.md) §Core payload concepts):

- artifact reference (e.g. URL, file path, selector, blueprint section),
- reproduction step (how to observe the issue),
- viewport / breakpoint (for visual / responsive findings),
- screenshot reference (when available — never required unless the lane mandates).

Findings without evidence are **not findings**; at best they are **SAFE UNKNOWN** observations.

Evidence classes:

| Lane | Typical evidence |
|------|------------------|
| Design QA | Frame name, component reference, token name, design file pointer. |
| SEO QA | URL, head section snippet, heading outline, copy excerpt. |
| Conversion QA | CTA location, form field name, trust block reference. |
| Frontend QA | URL or file path, selector, viewport, build/lint output. |
| Validator | Cross-cutting reference: contract field name, policy rule. |

---

## 4. No fake approvals

A QA prompt **must not**:

- declare “pass” without enumerating verified categories;
- declare “pass” when blockers are open and not waived;
- generate an Approval artifact ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact);
- modify the subject artifact;
- write a final go/no-go on behalf of a HITL approver — that is **Final Validation** (S13) + **Human Approval** (S14).

QA verdicts are **recommendations** (pass / fail / conditional). Final authority over a gate is HITL ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)).

---

## 5. Blocker semantics

A **blocker** ([qa-result-payloads-v0.md](qa-result-payloads-v0.md) §`blocker`) is true when downstream stages **must not proceed** without a fix or an explicit waiver.

Blocker discipline:

- A blocker without evidence is **not** a blocker — emit SAFE UNKNOWN instead.
- A blocker fixed inline by the QA prompt is **not allowed** — QA does not produce production edits.
- A blocker cannot be **upgraded or downgraded** silently; severity changes require a new run or HITL.
- A blocker that exposes a **contract gap** must surface a **STRUCTURE CHANGE** signal upstream.
- Multiple blockers do not collapse into a single “overall blocker”; enumerate each.

---

## 6. Waiver philosophy

A **waiver** ([qa-result-payloads-v0.md](qa-result-payloads-v0.md) §`waiver`) accepts a finding **temporarily or permanently** under a named approver. Rules:

| Rule | Detail |
|------|--------|
| Waivers are **HITL**. | Only a named human approver can sign a waiver ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)). |
| Waivers are **named**. | Approver role + date + scope. |
| Waivers are **bounded**. | Scope of waiver (this revision / this run / permanent). |
| Waivers do **not delete findings**. | The finding remains attached to the artifact’s QA history. |
| Waivers require **evidence** of the trade-off. | Risk note + downstream impact must be recorded. |
| Waivers must **not** be self-approved by the agent. | The QA agent emits **NEED HUMAN APPROVAL**, then waits. |
| Waivers near **SECURITY RISK** require additional approval. | Per `../../security/approval-gates.md` alignment. |

---

## 7. Confidence signaling

QA findings carry **confidence** in addition to severity ([qa-result-payloads-v0.md](qa-result-payloads-v0.md) §`confidence`).

| Confidence | When to use |
|------------|-------------|
| **low** | Indirect inference; missing evidence; reviewer judgment uncertain. |
| **medium** | Some evidence; bounded ambiguity. |
| **high** | Direct evidence (URL, selector, log output). |

Use confidence to:

- avoid over-asserting findings,
- pair with **SAFE UNKNOWN** when evidence is partial,
- guide the HITL discussion when severity is contentious.

Confidence is **reviewer judgment in prose**, not an ML confidence score.

---

## 8. Escalation behavior

QA prompts use the same signal vocabulary as other prompts ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) §7):

| Trigger | Signal | Action |
|---------|--------|--------|
| Required field unverifiable | **SAFE UNKNOWN** | Continue with bounded assumption; do not assert pass. |
| Required binding missing | **UNKNOWN** | Hard stop the lane until resolved. |
| Blocker needs waiver | **NEED HUMAN APPROVAL** | Stop; HITL gate. |
| Contract gap exposed | **STRUCTURE CHANGE** | Propagate to upstream stage. |
| Security concern (assets, scripts, forms, secrets) | **SECURITY RISK** | Stop line; escalate per policy. |

Escalation appears in the QA REPORT ([reporting-standard-v0.md](reporting-standard-v0.md) §4.3) and triggers downstream HITL handling.

---

## 9. Validator relationship

**Validator Agent** ([agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md)) is **planned / legacy-bridge**. Validator integration depth vs specialist QA is **TBD** ([qa-validation-model.md](qa-validation-model.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md) §SAFE UNKNOWN boundaries).

QA prompts treat Validator as:

- **complementary**, not a substitute for specialist QA;
- **cross-cutting** (task fit, forbidden paths, structural / policy checks);
- **not** automated in this repo — Validator findings are only present if a Validator REPORT exists;
- a candidate for **STRUCTURE CHANGE** when contract-level concerns surface.

A QA prompt **does not** claim Validator approval. If Validator did not run, the prompt says so under **SAFE UNKNOWN**.

---

## 10. Specialist QA relationship

The lanes ([qa-validation-model.md](qa-validation-model.md), [agent-map.md](agent-map.md)):

| Lane | Specialist agent (planned) | Subject artifact |
|------|----------------------------|------------------|
| Design QA | Design QA Agent | Frozen / iterating design artifact |
| SEO QA | SEO QA Agent | Blueprint, on-page metadata, copy outline |
| Conversion QA | Conversion QA Agent | CTAs, trust blocks, form friction |
| Frontend QA | Frontend QA Agent | Built static pages, source files, accessibility, responsive |
| Validator overlap | Validator Agent (legacy-bridge) | Cross-lane structural / policy concerns |

Each lane:

- has its own QA prompt,
- emits its own QA REPORT,
- does **not** speak on behalf of other lanes,
- cross-references neighbors only as evidence (“see Design QA finding QA-DSGN-007 for context”).

---

## 11. Lane-specific guidance

### 11.1 Design QA prompt

- Subject: design artifact (wireframe or hi-fi), referenced by id.
- Compares against: [Design Handoff Contract v0](design-handoff-contract-v0.md), blueprint fields, brand tokens.
- Findings: fidelity, token drift, missing states, a11y intent ([qa-result-payloads-v0.md](qa-result-payloads-v0.md) §Lane relationships).
- Forbidden: editing the design; approving the freeze.

### 11.2 SEO QA prompt

- Subject: blueprint (S06) or built pages (S12, S13).
- Compares against: [seo-intent-model-v0.md](seo-intent-model-v0.md), heading hierarchy rules, metadata fields, link integrity.
- Findings: title/description integrity, heading outline, schema honesty, thin content risk.
- Forbidden: rank/traffic predictions; auto-tuning copy.

### 11.3 Conversion QA prompt

- Subject: blueprint or built pages.
- Compares against: [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md).
- Findings: CTA clarity, friction, trust honesty, form load.
- Forbidden: claiming conversion uplift numbers.

### 11.4 Frontend QA prompt

- Subject: frontend source + built static pages.
- Compares against: [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) (QA_requirements, accessibility, performance heuristic), [frontend-production-model.md](frontend-production-model.md), [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md).
- Findings: build outcome, markup semantics, viewport spot-check, link/asset paths, JS scope.
- Forbidden: hand-patching `dist/`; claiming CI green without evidence; claiming deploy.

---

## 12. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| QA prompt that also fixes the artifact | Mixes production and assessment. | Separate QA REPORT; raise fixes as findings, not edits. |
| Waiver inside QA REPORT without a named approver | Bypasses HITL. | Emit **NEED HUMAN APPROVAL**; wait. |
| Severity tuning to avoid blocker | Distorts QA history. | Keep severity; escalate honestly. |
| “Validator approved” without a Validator REPORT | Fabrication. | SAFE UNKNOWN on Validator unless evidenced. |
| Cross-lane verdict in one REPORT | Confuses lane responsibility. | One lane per REPORT; cross-reference neighbors. |
| Findings without evidence | Cannot be acted on. | Either gather evidence or label as SAFE UNKNOWN observation. |

---

## 13. Non-claims

- This document does **not** ship an automated QA runner.
- It does **not** assume Validator code paths exist.
- It does **not** replace human review at HITL gates.

What it **does** do is define **how a QA prompt is shaped, what counts as evidence, and how findings travel** so QA remains comparable and trustworthy across lanes and runs.

---

## 14. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial QA prompt rules (documentation only). |
