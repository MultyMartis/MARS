# MARS Website Factory — Semantic Freeze Semantics v0

**Status:** **documentation only** — how **semantic objects** participate in **freeze** and **reopen** lifecycles. Aligns with [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md); **not** a state machine implementation.

**Version:** v0.

**Related:** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [semantic-inheritance-v0.md](semantic-inheritance-v0.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md).

---

## 1. Frozen semantic objects

A **semantic freeze** attaches to:

- A **set of named semantic object instances** in a scope (page, cluster, site), and/or
- The **artifact revision** that currently **binds** them (Blueprint freeze implies semantic snapshot for objects declared there).

While frozen, **mutation** of those objects is **forbidden** except through **reopen** paths below.

---

## 2. Semantic approvals

**Semantic approval** is HITL acknowledgment that:

- Declared semantic objects **match** stakeholder intent, and
- Downstream artifacts **may rely** on them until invalidation.

Recorded in approval artifact / REPORT per [approval-semantics-v0.md](approval-semantics-v0.md). **No** self-approval or autonomous approval.

---

## 3. Inherited freezes

When a **parent** scope freezes shared defaults (site/cluster), **children** created **before** that freeze **inherit** the frozen values for inherited fields. Children created **after** parent freeze use the **current** parent snapshot at time of child creation — reconciliation is **manual** if policies shift.

---

## 4. Freeze invalidation

**Freeze invalidation** occurs when:

- A semantic object **must** change (legal, ops, factual error), or
- Downstream discovers an upstream semantic error (**upstream invalidation** per [dependency-invalidation-v0.md](dependency-invalidation-v0.md)).

Effects:

- Breaks **semantic freeze** for affected objects.
- **Inherited approvals** for dependent artifacts break for that scope ([approval-semantics-v0.md](approval-semantics-v0.md) §7).
- **QA verdicts** become stale ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)).

---

## 5. Semantic revisions

**Semantic revision** — controlled change while **unfrozen** or after **partial reopen**: new lineage id, explicit REPORT, re-bind downstream.

---

## 6. Semantic supersede

**Supersede** replaces a semantic object instance **for the same role** (e.g. new primary `cta_object`). Requires:

- Explicit supersede declaration,
- Invalidation of consumers,
- New QA pass on affected lanes.

---

## 7. Semantic rollback

**Rollback** restores a **prior approved** semantic snapshot for a scope. Treated as **another revision** with full invalidation semantics — **not** silent file revert without QA.

---

## 8. Partial semantic reopen

**Partial reopen** limits thawed objects to a **subset** (e.g. only `faq_entity` for legal edit). Downstream must declare whether they remain **frozen** relative to untouched objects.

---

## 9. Delivery implications

- Delivery packages **pin** semantic snapshot references ([reference-delivery-package-v0.md](reference-delivery-package-v0.md)).
- Post-delivery semantic change starts **new** revision / candidate flow — not hot patch without governance.

---

## 10. QA reset implications

Any freeze break that changes **S0–S1** semantic objects triggers **mandatory** rerun of named QA lanes per [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md); waivers need evidence + HITL.

---

## 11. HITL requirements

- Freeze break: **authorized role** per project policy ([reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md)).
- Waiver on semantic **C0–C1**: **forbidden** without explicit human acceptance of residual risk.

---

## 12. SAFE UNKNOWN

- Tooling support for **partial reopen UI** — **not** in MARS repo v0.
- Contractual **client freeze calendars** — external; reference in REPORT only.

---

*End of Semantic Freeze Semantics v0.*
