# MARS Website Factory — Artifact Transfer Semantics v0

**Status:** **documentation only** — how **lifecycle attributes** move, inherit, degrade, or break across **declared transfers**. **Not** distributed transactions, **not** ACID middleware, **not** runtime replication.

**Version:** v0.

**Related:** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md).

---

## 1. What “transfers” in v0

Across a **prompt boundary**, these dimensions may **propagate** when explicitly declared:

| Dimension | Transfer behavior |
|-----------|-------------------|
| **Approvals** | **Downstream-only** inheritance for **same scope** per [approval-semantics-v0.md](approval-semantics-v0.md); never widen scope silently. |
| **Freezes** | Frozen upstream **constrains** downstream consumption; downstream may add **additional** freeze; cannot **remove** upstream freeze without HITL reopen. |
| **Semantic validity** | **Declared** in **semantic_state**; invalidation upstream **forces** downstream review or **stale** marking — not auto-healing. |
| **QA state** | Lane QA verdict is **per run**; new upstream revision **resets** applicable QA per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md). |
| **Lineage** | Child envelope **points to** parent revision; transfer **does not** fork lineage without documentation. |
| **Delivery eligibility** | **Derived**: only when upstream chain satisfies [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) assembly rules. |

---

## 2. Transfer inheritance

**Definition:** Downstream envelope **may assume** upstream **approval_state**, **freeze_state**, and **qa_state** **only** as encoded in the **immediate** parent artifacts listed in **dependencies**.

| Rule | Detail |
|------|--------|
| **Scope match** | Inherited approvals apply **only** to URLs/templates in **handoff_scope**. |
| **Conditional carry** | Conditional approvals transfer **with CR list attached**; downstream must cite CR ids. |
| **Expiration** | Expired upstream approval **does not** inherit — treat as **UNKNOWN** / re-gate. |

---

## 3. Transfer invalidation

**Triggers** (non-exhaustive): upstream **revision**, **semantic invalidation**, **registry STRUCTURE CHANGE**, **SECURITY RISK**, **QA fail** on dependent lane.

**Effects:**

- Downstream **envelopes** become **stale** or **invalidated** per scope.  
- **Delivery candidate** **cannot** advance until invalidation cleared or waived with HITL.  
- **Explicit REPORT** lists affected **artifact_id**s and **route** cancellations.

---

## 4. Transfer downgrade

**Downgrade** = moving publication class **backward** (e.g. approved → in_review) for a slice.

| Rule | Detail |
|------|--------|
| Requires **HITL** + reason (error discovered, scope shrink). |
| Downstream artifacts that consumed the downgraded slice become **stale** or require **re-consumption**. |
| **Forbidden:** downgrade to hide prior QA failures. |

---

## 5. Transfer freeze break

When HITL **reopens** a frozen baseline:

- Emit **new revision_id** policy per [revision-semantics-v0.md](revision-semantics-v0.md).  
- **All active forward routes** from that artifact **pause** until new approval path defined.  
- Semantic freeze break per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) **adds** semantic invalidation obligations.

---

## 6. Partial transfer

**Partial transfer** copies obligations for a **subset** of scope:

- **dependencies** must list only relevant parents.  
- **QA** and **approval** inheritance **trim** to subset.  
- **Risk:** split-brain between pages — mitigate with explicit **per-page envelope** or index artifact listing child ids.

---

## 7. Non-claims

- **Not** two-phase commit across repos.  
- **Not** automatic staleness detectors.  
- **Not** background sync of semantic objects.

---

## 8. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial transfer semantics (documentation only). |
