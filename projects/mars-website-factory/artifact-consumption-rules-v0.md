# MARS Website Factory — Artifact Consumption Rules v0

**Status:** **documentation only** — how **downstream stages** may **consume**, **reject**, **invalidate**, **reopen**, or **partially accept** upstream artifacts. **Not** an API consumer SDK, **not** automated subscription consumption.

**Version:** v0.

**Related:** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md), [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md), [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Consumption authority

| Action | Authority |
|--------|-----------|
| **Consume** (full acceptance) | Downstream stage lead within **approved** upstream scope. |
| **Reject** | Downstream lead + QA narrative; may **block** route. |
| **Invalidate** (upstream-driven) | Upstream owner / QA / Validator finding with **signal** per [dependency-invalidation-v0.md](dependency-invalidation-v0.md). |
| **Reopen** | **HITL** only for frozen or approved baselines. |
| **Partial acceptance** | HITL when **conditional** path per [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) §12. |

---

## 2. Consume (full)

**Preconditions:**

- **artifact_state** ∈ {`approved`, `frozen`} as required by route.  
- **qa_state** not `fail` / not stale for that lane.  
- **dependencies** resolve; **lineage** not orphan.  
- **semantic_state** not `invalidated` unless waived.

**Effect:** Downstream may **author** child artifacts citing upstream **revision_id**.

---

## 3. Reject

**Reject** = downstream refuses transfer **before** child artifact is approved.

| Requirement | Detail |
|-------------|--------|
| **Written reason** | Contract gap, scope mismatch, **UNKNOWN** stack. |
| **Signal** | Often **STRUCTURE CHANGE** or **UNKNOWN**. |
| **Route** | Return to upstream per [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md). |

---

## 4. Invalidate

Downstream (or cross-lane QA) may **invalidate** upstream **for cause**:

- Expose blueprint error from frontend QA → invalidation **route** per routing doc.  
- Must **not** silently patch upstream artifact.

---

## 5. Reopen

**Reopen** frozen consumption path:

- **HITL** mandatory.  
- Updates **freeze_state** + **approval_state** narrative.  
- Triggers **revision** / **regeneration** semantics downstream.

---

## 6. Partially consume

Allowed when:

1. **handoff_scope** explicitly lists in-scope pages.  
2. Out-of-scope pages **remain** on previous **revision_id** or **blocked** until transferred.  
3. REPORT lists **partial** acceptance and **risks** (split site).

---

## 7. Stale consumption

Consuming while knowing **stale transfer** conditions (expired approval, superseded parent, failed QA reset) is **forbidden**. If discovered post-hoc → **stop line** + invalidation REPORT.

---

## 8. Invalid consumption

Examples:

- Treating **draft** as **approved**.  
- Ignoring **conditional** CR list.  
- **Widening** handoff_scope beyond approval.

**Remediation:** **Delivery blocked**; may require **governance** escalation per [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md).

---

## 9. Orphan consumption

Consuming artifact whose **parent** missing → **orphan consumption** — **blocked** until lineage fixed.

---

## 10. Non-claims

- **Not** automated drift detection between design files and HTML.  
- **Not** IDE “import” without human review.

---

## 11. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial consumption rules (documentation only). |
