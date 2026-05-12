# MARS Website Factory — First Operational Runbook v0

**Status:** **documentation only** — **human-driven** operational reference.  
**Not claimed:** a runnable workflow engine, autonomous agents, background orchestration, automatic stage routing, or deployment automation.

**Version:** v0.

**Related:** [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [reference-run-sequence-v0.md](reference-run-sequence-v0.md), [operator-lane-model-v0.md](operator-lane-model-v0.md), [human-supervision-model-v0.md](human-supervision-model-v0.md), [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md), [reference-run-artifact-flow-v0.md](reference-run-artifact-flow-v0.md), [reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md), [reference-run-reporting-v0.md](reference-run-reporting-v0.md), [`../../governance/execution-model.md`](../../governance/execution-model.md).

---

## 1. Purpose

This runbook is the **first practical execution layer** for Website Factory: it tells **humans** how a real project is expected to move through the factory **using documents, prompts, evidence, and explicit approvals** — without implying that MARS executes stages automatically.

Companion documents (same v0 bundle) spell out the **reference run sequence** (R01–R15), **operator lanes**, **supervision model**, **checkpoints**, **artifact flow**, **failure recovery prose**, and **reporting** aligned with [reporting-standard-v0.md](reporting-standard-v0.md).

---

## 2. Scope

**In scope**

- Operational vocabulary for a **single reference-style** project path from intake through delivery package.
- How this path **maps** to [website-factory-workflow-v0.md](website-factory-workflow-v0.md) stages `WF_V0_S01` … `WF_V0_S15` (narrative alignment; **no** persisted `stage_id` engine).
- Expectations for **Cursor-assisted** work per [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md) when an operator uses an IDE assistant — still **human-owned** execution.

**Out of scope**

- Code for schedulers, queues, daemons, or Control Plane dispatch.
- MetaBOT / n8n / external workflow ownership (see project packs; MARS does not claim those runtimes).
- Any statement that artifacts are **automatically** validated, routed, frozen, or delivered.

---

## 3. Operational philosophy

| Principle | Meaning |
|-----------|---------|
| **Document-first** | Contracts, registries, checklists, and REPORT prose are the **source of truth** for what happened; the assistant is a tool, not the authority. |
| **Human-owned transitions** | Moving from one reference step to the next requires a **human decision** (and usually a REPORT + checkpoint evidence). |
| **Explicit non-runtime** | There is **no** hidden orchestrator in this repository that advances Website Factory stages. |
| **SAFE UNKNOWN** | Unknown hosting, CI, storage, or Validator depth remains **SAFE UNKNOWN** until evidenced and documented per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md). |

---

## 4. What a “run” means

A **run** is one **bounded human execution** of a factory step (or a tightly coupled micro-batch of steps), typically:

1. **Prompt / task framing** — context, paths, constraints ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md)).
2. **Execution** — human performs work in Cursor or other tools; assistant output is **reviewed**, not blindly accepted.
3. **REPORT** — closing narrative per [reporting-standard-v0.md](reporting-standard-v0.md) for the applicable lane.
4. **Gate** — where HITL or QA applies, the run **does not** authorize the next step unless governance allows it.

A **reference project** may consist of **many runs** across R01–R15; sequencing is **documented intent**, not an enforced state machine ([stage-state-model-v0.md](stage-state-model-v0.md) semantics apply as **design vocabulary**).

---

## 5. Documentation-first execution

- **Inputs** and **outputs** of each step are **named artifacts** (see [artifact-types-v0.md](artifact-types-v0.md), [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md)) even when stored as files, tickets, or messages — storage format is **project-specific** (**SAFE UNKNOWN**).
- **Lineage** and **freeze** behavior follow [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), and [approval-semantics-v0.md](approval-semantics-v0.md) as **prose contracts**.
- **Invalidation** is acknowledged in REPORTs per [dependency-invalidation-v0.md](dependency-invalidation-v0.md); nothing is silently “healed.”

---

## 6. Relationship to Workflow v0

| Reference step | Workflow v0 `stage_id` (canonical) |
|----------------|-----------------------------------|
| R01 | `WF_V0_S01_INTAKE` |
| R02 | `WF_V0_S02_SITE_TYPE` |
| R03 | `WF_V0_S03_STRATEGY` |
| R04 | `WF_V0_S04_IA` |
| R05 | `WF_V0_S05_BLUEPRINT` |
| R06 | `WF_V0_S06_BLUEPRINT_QA` |
| R07 | `WF_V0_S07_DESIGN_HANDOFF` |
| R08 | `WF_V0_S08_DESIGN_PRODUCTION` |
| R09 | `WF_V0_S09_DESIGN_QA` |
| R10 | `WF_V0_S10_FRONTEND_HANDOFF` |
| R11 | `WF_V0_S11_FRONTEND_PRODUCTION` |
| R12 | `WF_V0_S12_FRONTEND_QA` |
| R13 | `WF_V0_S13_FINAL_VALIDATION` |
| R14 | `WF_V0_S14_HITL_APPROVAL` |
| R15 | `WF_V0_S15_DELIVERY` |

Details per step: [reference-run-sequence-v0.md](reference-run-sequence-v0.md).

---

## 7. Relationship to HITL

HITL is **mandatory** where workflow v0 and [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) require human authority. This runbook **does not** introduce autonomous approval. **G*** gate names follow [workflow-map.md](workflow-map.md) / workflow v0; checkpoint IDs **C01–C08** are operational shorthand — see [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md).

---

## 8. Relationship to Cursor

Today, many runs are executed in **Cursor** per [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md): explicit paths, git discipline, AGENT vs ASK posture, and REPORT closeout. Cursor is **not** a factory orchestrator; it is a **user-controlled** editing and assistance surface ([workflow-map.md](workflow-map.md)).

---

## 9. Relationship to artifacts

Artifact **movement**, **lineage**, **freeze**, **revision**, **invalidation**, and **QA propagation** are described in [reference-run-artifact-flow-v0.md](reference-run-artifact-flow-v0.md), aligned with the Artifact Bus and semantic layers (**documentation semantics**, not a message bus).

---

## 10. Relationship to Validator / QA

- **Stage QA** (blueprint, design, frontend) produces evidence and recommendations per [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), and [qa-validation-model.md](qa-validation-model.md).
- **Final Validation** (R13) aligns with workflow S13 and [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) — **methodology and vocabulary**, **not** an in-repo validator engine.

---

## 11. Explicit prohibitions (honesty boundary)

This runbook **must not** be read as claiming:

- **Autonomous execution** — no agent loop owns the factory line.
- **Hidden runtime** — no undisclosed code path advances stages.
- **Automatic routing** — “routing” is **which role reads next** ([validation-escalation-model-v0.md](validation-escalation-model-v0.md)); not a bus.
- **Background orchestration** — no daemon, queue, or n8n graph is implied by this pack.
- **Automatic deployment** — delivery is **human-packaged**; hosting/CDN is **SAFE UNKNOWN** unless evidenced.

---

## 12. Where to go next

| Need | Document |
|------|----------|
| Step-by-step R01–R15 | [reference-run-sequence-v0.md](reference-run-sequence-v0.md) |
| Roles and authority | [operator-lane-model-v0.md](operator-lane-model-v0.md) |
| Human supervision cadence | [human-supervision-model-v0.md](human-supervision-model-v0.md) |
| Checkpoints C01–C08 | [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md) |
| Artifact propagation | [reference-run-artifact-flow-v0.md](reference-run-artifact-flow-v0.md) |
| Failure / rollback prose | [reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md) |
| REPORT types and fields | [reference-run-reporting-v0.md](reference-run-reporting-v0.md) |

---

*End of First Operational Runbook v0.*
