# MARS Website Factory — Validation lifecycle v0

**Status:** **documentation only** — **conceptual lifecycle tokens** for a validation episode (one gate review / one validation scope). **Not** a persisted state machine, **not** a runtime enum store.

**Version:** v0.

**Related:** [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md).

---

## 1. Validation stages (tokens)

| Stage | Meaning |
|-------|---------|
| **requested** | A validation scope is **asked for** (explicit request, gate entry, or reopen after change). |
| **prepared** | Inputs assembled per methodology: artifacts, semantic slice, QA payloads, approvals/freeze context — **may** still lack evidence (**SAFE UNKNOWN** allowed as label, not as pass). |
| **executing** | Review activity in progress (human and/or tool-assisted **where** used); **not** “worker executing” as infrastructure. |
| **evidence_collected** | Evidence bundle assembled per [validation-evidence-model-v0.md](validation-evidence-model-v0.md); gaps explicitly classified. |
| **review_ready** | Ready for verdict aggregation; blockers, escalations, and waiver needs are visible. |
| **passed** | Verdict allows forward movement per gate policy without conditions, or with only documented non-blocking notes. |
| **conditional_pass** | Forward movement allowed **only** under named conditions, CRs, or follow-up validations — see [validation-result-semantics-v0.md](validation-result-semantics-v0.md). |
| **failed** | Verdict blocks forward movement until fix, replan, or governed waiver. |
| **blocked** | External dependency (freeze, missing approval, missing SoT, policy halt) prevents completion — distinct from **failed** (which is a completed negative verdict). |
| **invalidated** | A previously accepted validation is **voided** by upstream change, lineage break, or governance action — not silently “still valid”. |
| **waived** | Risk accepted under explicit waiver record — see [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md). |
| **archived** | Historical record retained for audit; **not** active for gating. |

---

## 2. Allowed transitions (typical)

```text
requested → prepared → executing → evidence_collected → review_ready
  → passed | conditional_pass | failed | blocked
passed | conditional_pass → archived (when superseded or project archives)
failed → requested (revalidation after fix)
blocked → prepared | executing (when unblocked)
any terminal → invalidated (superseded by change/governance)
failed | conditional_pass → waived (only via explicit waiver path)
```

Exact transitions are **governance- and project-bound**; this table is **normative vocabulary**, not executable workflow.

---

## 3. Forbidden transitions (conceptual)

| From | To | Why forbidden |
|------|-----|----------------|
| **archived** | **passed** / **conditional_pass** | Reopen = new **requested** episode, not resurrection of archive row “as if fresh” without lineage |
| **invalidated** | **passed** without new **requested** | Would hide invalidation |
| **waived** | **passed** (silent) | Waiver **is** the governed outcome; do not erase waiver metadata |
| **review_ready** | **passed** with zero evidence for mandatory scope | Fabrication / false pass |
| **blocked** | **passed** by automation | Unblock requires explicit resolution (human or documented non-HITL path) |

---

## 4. Revalidation

- **Revalidation** starts a **new** episode at **requested** (may skip redundant **prepared** steps only if governance allows — **SAFE UNKNOWN** per org).
- Prior **passed** / **conditional_pass** does **not** auto-carry after **revision**, **regeneration**, or **dependency invalidation** — see [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md).

---

## 5. Invalidation

- **Invalidated** marks prior validation **not authoritative** for current lineage.
- Triggers align with: upstream artifact supersede, approval revocation, semantic freeze break, bus-layer stale/orphan consumption — cross-ref [artifact-consumption-rules-v0.md](artifact-consumption-rules-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md).

---

## 6. Freeze interaction

- While **freeze** applies to named scope, validation may **block** or **conditional_pass** with “no mutation beyond freeze” constraints per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md).
- **Breaking freeze** for validation fixes is a **HITL** decision, not an automated side effect.

---

## 7. Dependency invalidation

- Upstream invalidation **should** move dependent validations toward **invalidated** or **requested** (revalidation), not leave **passed** stale — aligned with [dependency-invalidation-v0.md](dependency-invalidation-v0.md) and [validation-consistency-model-v0.md](validation-consistency-model-v0.md).

---

## 8. HITL ownership

| Action | Owner |
|--------|--------|
| Closing **passed** / **conditional_pass** on HITL gates | Named human role per project matrix ([reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md)) |
| **waived** | Approver with waiver authority per [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md) |
| **invalidated** / reopen | Governance / lead per [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md) |
| Specialist QA narrative | Lane owner; Validator does **not** replace brand/legal HITL |

---

*Last updated: 2026-05-12.*
