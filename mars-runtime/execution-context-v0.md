# MARS — Execution Context Model v0

**Status:** documented — contract only. This file defines the run-carried execution context shape. No runtime context engine is implemented in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

Define what context each run carries while progressing through orchestration and execution, with explicit bounded-context discipline.

---

## 2. Execution context fields (v0)

| Field | Meaning |
|-------|---------|
| `run_id` | Run correlation identifier. |
| `task_id` | Task binding for task-level semantics and traceability. |
| `project_id` | Project scope ownership and policy context. |
| `current_step` | Current workflow/execution step pointer. |
| `accumulated_results` | Aggregated intermediate outputs from prior steps. |
| `artifacts_refs` | References to produced artifacts (not embedded binaries). |
| `memory_refs` | References to memory slices selected for this run context. |
| `budget_state` | Current budget posture (tokens/cost/context quotas). |
| `signals` | Canonical signal set active for this run slice. |

---

## 3. Relations to other artefacts

| Artefact | Relation |
|----------|----------|
| [../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md) | Governs bounded context assembly and prioritization rules. |
| [../memory/memory-retrieval-v0.md](../memory/memory-retrieval-v0.md) | Defines retrieval and filtering constraints for `memory_refs`. |
| [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) | Provides durable state persistence mapping for context snapshots/updates. |

---

## 4. Bounded context rule (normative v0)

- Execution context **must be bounded** and must not grow without limits during a run.
- Context expansion should be constrained by budget policy and relevance rules.
- Oversized context conditions should trigger explicit deny/truncate/escalation behavior per applicable policies.

---

## 5. Explicit non-claims

- No context builder, truncation engine, or automatic summarizer is implemented in-repo.
- No claim is made that bounded-context enforcement exists at runtime in Phase 1.

---

## 6. SAFE UNKNOWN

- Concrete size limits and token thresholds are not fixed in this document.
- Serialization format and checkpoint granularity for context snapshots are not specified.
- Conflict resolution for concurrent context updates is unspecified in v0.

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Execution Context Model v0 authored (documentation-only contract, bounded context rule added). |

---

*End of Execution Context Model v0.*
