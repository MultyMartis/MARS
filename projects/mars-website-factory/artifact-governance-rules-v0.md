# MARS Website Factory — Artifact Governance Rules v0

**Status:** **documentation only** — **governance invariants** for artifact movement, publication, and lineage. **Not** legal advice, **not** automated policy enforcement.

**Version:** v0.

**Related:** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md), [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md), [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [`../../AGENTS.md`](../../AGENTS.md).

---

## 1. Immutable artifacts

Once **publication class** is **approved** or **frozen** for a **revision_id**:

| Rule | Detail |
|------|--------|
| **No in-place body rewrite** | Edits require **new revision** or **supersede** with lineage per [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md). |
| **Immutable approval record** | Approval artifacts remain **append-only** narrative per [approval-semantics-v0.md](approval-semantics-v0.md). |

---

## 2. Mutable drafts

**Draft** artifacts may change freely **within** authoring stage — but:

- **Must not** be cited as **approved** downstream.  
- Promotion to **review** requires explicit **publication** declaration.

---

## 3. Revision governance

| Requirement | Rationale |
|-------------|-----------|
| **Every revision** has owner, scope, trigger | Auditability ([revision-semantics-v0.md](revision-semantics-v0.md)). |
| **Revision_id** policy is project-defined — if undefined → **SAFE UNKNOWN** with bounded interim naming in REPORT. |
| **Cross-stage impact** enumerated before approval | Prevents silent partial site updates. |

---

## 4. Rollback governance

- **Rollback** requires **G7-level** (or delegated documented) authority per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md).  
- **Rollback** **records** prior and current **Approval artifact** ids.  
- **Forbidden:** “shadow rollback” (files reverted without approval record).

---

## 5. Stale artifacts

- **Stale** state must be **visible** in REPORT / envelope — not only tribal knowledge.  
- **Stale** **forbidden** as basis for new **approved** forward routes.

---

## 6. Orphan artifacts

- **Orphan** artifacts **blocked** from delivery and from **seeding** new child artifacts until resolved ([artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md)).

---

## 7. Freeze governance

- **Freeze** and **unfreeze** **HITL-only** per execution + semantic freeze docs.  
- **Forbidden:** “soft freeze” language without naming **freeze_state** and gate id.

---

## 8. Delivery governance

- **Delivery candidate** components must be **frozen** publication baselines per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md).  
- **Open SECURITY RISK** → **DELIVERY BLOCKED** until cleared or waived per security policy.

---

## 9. Explicit prohibitions (transfer layer)

| Forbidden pattern | Name |
|-------------------|------|
| Replace file/content while keeping same **revision_id** and claiming no change | **Silent replacement** |
| New **artifact_id** or revision hidden from downstream prompts | **Hidden revision** |
| Downstream **approval_state** `approved` without HITL because “upstream was approved” | **Fake approval inheritance** |
| Remove invalidation from narrative to avoid rework | **Hidden invalidation** |

Each violation is a **governance defect** — correct via **new REPORT**, **HITL**, and if recurring, **risk-register** row per project policy.

---

## 10. Non-claims

- **Not** automated governance bots.  
- **Not** cryptographic non-repudiation unless project adds tooling (**SAFE UNKNOWN**).

---

## 11. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial artifact governance rules (documentation only). |
