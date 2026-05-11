# MARS Website Factory — SAFE UNKNOWN Prompt Rules v0

**Status:** **documentation only** — how prompts, agents, and reports handle **unknowns** under MARS honesty rules. **Not** a runtime validator, **not** evidence of automated unknown-detection, **not** a substitute for human review.

**Version:** v0.

**Related:** [safe-unknown-boundary.md](safe-unknown-boundary.md), [`../../AGENTS.md`](../../AGENTS.md), [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

---

## 1. Purpose

The factory is **documentation-first** and **honesty-first**. Many fields in real projects are **not known** at prompt time: target stack, hosting, CI, exact registry rows, design freeze state, etc. Without discipline, agents fabricate. This document defines **SAFE UNKNOWN behavior** in prompts and reports so unknowns are **named, bounded, and resolvable** rather than guessed.

---

## 2. Unknown vs SAFE UNKNOWN

| Signal | When it applies | Behavior |
|--------|-----------------|----------|
| **UNKNOWN** | A **required binding** is missing (approver role, stack decision, registry row). | **Hard stop** for the affected branch. Do not produce the artifact; emit UNKNOWN in the REPORT. |
| **SAFE UNKNOWN** | A **non-blocking** unknown exists where **policy** allows bounded continuation with explicit assumption. | Continue **only** with a written assumption; escalate to UNKNOWN if the assumption proves false. |

Both signals are part of [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md) and used in [website-factory-workflow-v0.md](website-factory-workflow-v0.md) stage rows.

---

## 3. Assumption discipline

Every SAFE UNKNOWN entry **must** include:

| Field | Meaning |
|-------|---------|
| **scope** | What the assumption covers (one artifact field or area). |
| **assumption** | The bounded statement the agent is making. |
| **why** | Why the assumption is necessary right now. |
| **source missing** | The artifact, decision, or external fact that would resolve it. |
| **resolution path** | Who/what closes it (approver role, future stage, registry row). |
| **risk if wrong** | What downstream artifact or QA would be invalidated. |

A SAFE UNKNOWN entry **without** all six fields is **incomplete** and should be flagged as such.

---

## 4. Forbidden fabrication

The following are **never** acceptable in a factory prompt or report:

- inventing a `block_id`, `site_type_id`, `blueprint_id`, `design_handoff_id`, `frontend_handoff_id` not present in named artifacts or registries;
- claiming a value for a contract field without a source;
- claiming **CI passes** without a build run and named CI;
- claiming **deployed** / **live** without a deployment record;
- claiming **Validator approved** without a Validator report ([agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md));
- claiming **n8n bound**, **Cursor automated**, **runtime active** without in-repo evidence ([safe-unknown-boundary.md](safe-unknown-boundary.md));
- claiming **HITL approved** without an Approval artifact ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact);
- claiming **SEO performance** numbers (rank, traffic) — these are **never** factory outputs.

When fabrication is the only way to “complete” a field, the correct answer is **SAFE UNKNOWN** or **UNKNOWN**.

---

## 5. Evidence expectations

Evidence comes in three classes, all human-auditable:

| Class | Examples |
|-------|----------|
| **Artifact evidence** | A named upstream artifact, with `artifact_id` and contract anchor. |
| **Registry evidence** | A row in [site-type-registry-v0.md](site-type-registry-v0.md), [block-registry-v0.md](block-registry-v0.md), or [`../../agents/registry.md`](../../agents/registry.md). |
| **Execution evidence** | A local command output (build, lint, link check) captured in the REPORT. |

Anything else (recollection, paraphrase, “common sense”) is **not evidence** and must trigger SAFE UNKNOWN or UNKNOWN.

---

## 6. Confidence signaling

When an agent writes a finding, an assumption, or a recommendation, it should signal **confidence** using the QA payload convention ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)):

| Level | When to use |
|-------|-------------|
| **low** | Inference from indirect evidence; substantial unknowns. |
| **medium** | Some evidence; bounded gaps. |
| **high** | Direct artifact / registry / execution evidence. |

Confidence is **not ML confidence** — it is **reviewer judgment** in prose. Do not overstate confidence to make a report look stronger.

---

## 7. Escalation wording

Escalation phrasing matters. Use the canonical signal vocabulary.

| Situation | Correct wording |
|-----------|-----------------|
| Required field missing, no policy allows continuation. | `UNKNOWN — <field> not evidenced; halting <branch>.` |
| Required field missing, bounded continuation allowed. | `SAFE UNKNOWN — assuming <X> until <source> resolves; risk: <Y>.` |
| Decision required from a human. | `NEED HUMAN APPROVAL — <gate>, <approver role>, <decision options>.` |
| Contract/registry/scope shift needed. | `STRUCTURE CHANGE — <impacted artifact>, <reason>.` |
| Security-sensitive concern. | `SECURITY RISK — <concern>; stopping line per <policy>.` |

Avoid soft language (“probably”, “seems fine”, “maybe later”) when one of these signals applies.

---

## 8. Implementation honesty

For any prompt that touches **implementation**:

- Do not claim **Gulp build** ran unless it ran in this session — emit SAFE UNKNOWN otherwise.
- Do not claim **deploy** — that is HITL G7 territory.
- Do not claim **CI** unless an in-repo job name is referenced AND a recent run is cited.
- Do not claim **Cursor automation** — it does not exist beyond user discipline.
- Do not claim **Validator pass** — Validator integration depth is TBD.

Reference: [safe-unknown-boundary.md](safe-unknown-boundary.md) is the canonical honesty boundary.

---

## 9. Runtime honesty

For any prompt that touches **runtime**:

- The repo contains `mars-runtime/*` with **experimental** material per [`../../mars-runtime/README.md`](../../mars-runtime/README.md). This is **not** a full production runtime.
- A factory prompt **does not** assume:
  - the Control Plane is live,
  - the Execution Bridge dispatches work,
  - the State Store persists task state,
  - any factory agent is wired to a runner.
- Statements about future runtime appear as **planned** ([`../../governance/execution-model.md`](../../governance/execution-model.md), [`../../mars-runtime/execution-bridge-v0.md`](../../mars-runtime/execution-bridge-v0.md)).
- Statements about **today** default to **human-supervised Cursor**.

---

## 10. Examples — GOOD vs BAD

### 10.1 Missing CI evidence

GOOD:

```text
SAFE UNKNOWN
  scope:           build verification
  assumption:      none yet; build not run in this session
  why:             prompt did not include local build step
  source missing:  CI job name; build log
  resolution path: run `gulp build` locally OR run named CI job
  risk if wrong:   may claim green build that does not pass
```

BAD:

```text
"All tests pass; build is green."
```

Why bad: §4 (fabrication) and §8 (implementation honesty).

### 10.2 Missing registry row for a new site type

GOOD:

```text
STRUCTURE CHANGE
  context: site_type_id 'b2b-marketplace' not in site-type-registry-v0.md
  options:
    1) add row under registry governance, then proceed with classification
    2) reclassify to nearest existing site_type with rationale
  blocker: no silent best-guess classification
```

BAD:

```text
"Used site_type 'b2b-marketplace' (closest match)."
```

Why bad: invents a registry row; violates §4 and §6 (over-confident).

### 10.3 Missing approver role for design freeze

GOOD:

```text
UNKNOWN
  scope:           G5 design freeze
  reason:          no design lead role identified in project setup
  halting:         frontend handoff cannot start until approver is named
```

BAD:

```text
"Marked design as frozen for handoff."
```

Why bad: bypasses HITL ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) §3 G5); fabricates approval.

### 10.4 Frontend handoff with unspecified target_stack

GOOD:

```text
SAFE UNKNOWN
  scope:           target_stack
  assumption:      gulp-static (Gulp 4 + gulp-file-include + Dart Sass) per legacy profile
  why:             prompt did not name the stack; legacy profile is the closest reference
  source missing:  explicit project stack decision
  resolution path: tech lead names target_stack before S11 starts
  risk if wrong:   section_map and SCSS_mapping may need rework
```

BAD:

```text
"target_stack: Next.js with Tailwind."
```

Why bad: fabricates a stack outside the static factory model; would trigger STRUCTURE CHANGE per [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md).

### 10.5 SEO performance claim

GOOD:

```text
SAFE UNKNOWN
  scope:           SEO performance
  assumption:      none claimed
  why:             factory does not predict rank / traffic
  source missing:  out of scope; SEO QA reviews on-page, not ranking
  resolution path: post-launch monitoring outside factory v0 scope
```

BAD:

```text
"This page will rank top 3 within 2 months."
```

Why bad: forbidden fabrication; SEO performance is never a factory output.

---

## 11. Honesty checklist (one-line items)

- If you cannot cite an artifact, registry, or execution log — **SAFE UNKNOWN or UNKNOWN**.
- If a value would require a human decision — **NEED HUMAN APPROVAL**.
- If a runtime assumption would be needed — **SAFE UNKNOWN runtime + planned**.
- If a contract field shape would shift — **STRUCTURE CHANGE**.
- If assets / forms / scripts raise security concerns — **SECURITY RISK**.
- If unsure between UNKNOWN and SAFE UNKNOWN — default to **UNKNOWN** (stricter).

---

## 12. Non-claims

This document does **not**:

- ship a runtime unknown-detector,
- guarantee any LLM will follow these rules,
- replace human judgment.

It **does** define a shared vocabulary and behavior so the **same unknown** is described the **same way** across stages, lanes, and projects.

---

## 13. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial SAFE UNKNOWN prompt rules for the Website Factory (documentation only). |
