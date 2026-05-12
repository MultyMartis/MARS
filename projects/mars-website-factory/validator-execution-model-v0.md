# MARS Website Factory — Validator execution model v0

**Status:** **documentation only** — **conceptual I/O** for how validation activity is framed **in the abstract**. **Not** an execution bridge, **not** a process supervisor, **not** a service contract.

**Version:** v0.

**Related:** [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md), [validation-lifecycle-v0.md](validation-lifecycle-v0.md), [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [validation-evidence-model-v0.md](validation-evidence-model-v0.md), [qa-validation-model.md](qa-validation-model.md), [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md), [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 1. Conceptual execution shape

Validation is modeled as **bounded reasoning** over explicit inputs, producing explicit outputs. **Who** performs it (human, specialist agent prompt, Validator prompt, external tool) is **environment-specific** and often **SAFE UNKNOWN** per [qa-validation-model.md](qa-validation-model.md).

---

## 2. Inputs (conceptual)

| Input class | Description |
|-------------|-------------|
| **artifacts** | Blueprint, design, frontend, QA payloads, delivery packages — per [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md) |
| **semantic graph** | Documented relationships / objects / dependencies — per [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md) (**not** a graph DB snapshot) |
| **QA payloads** | Lane outputs per [qa-result-payloads-v0.md](qa-result-payloads-v0.md) |
| **approvals** | HITL decisions per [approval-semantics-v0.md](approval-semantics-v0.md) |
| **freezes** | Frozen scopes per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) |
| **revisions** | Revision records per [revision-semantics-v0.md](revision-semantics-v0.md) |
| **signals** | Governance tokens per [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md) and [orchestration-signals-v0.md](orchestration-signals-v0.md) |

---

## 3. Outputs (conceptual)

| Output class | Description |
|--------------|-------------|
| **findings** | Atomic issues / observations with severity |
| **evidence** | Proof bundle per [validation-evidence-model-v0.md](validation-evidence-model-v0.md) |
| **verdicts** | Gate outcome per [validation-result-semantics-v0.md](validation-result-semantics-v0.md) |
| **escalations** | Routed human/policy actions per [validation-escalation-model-v0.md](validation-escalation-model-v0.md) |
| **waivers** | Explicit risk acceptance per [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md) |
| **invalidation notices** | Statements that prior validation no longer applies (lineage / dependency driven) |

---

## 4. Explicit non-properties

This model **does not** assume or require:

| Absent property | Note |
|-----------------|------|
| **Scheduler** | No timed validation jobs implied |
| **Queue** | No FIFO work queue for validators |
| **Distributed runtime** | No cluster of validation workers |
| **Background workers** | No daemon continuously validating |
| **Deterministic LLM validation** | LLM-assisted review is **non-deterministic**; human and tool evidence still required for HITL-grade claims |

---

## 5. Orchestration semantics (documentation-only)

“Orchestration” here means **ordering and responsibility** described in [website-factory-workflow-v0.md](website-factory-workflow-v0.md) and [workflow-map.md](workflow-map.md): which stage **may** request validation, which signals **may** fire. It **does not** mean an invisible automation layer running validations.

---

*Last updated: 2026-05-12.*
