# MARS Website Factory — Validation failure semantics v0

**Status:** **documentation only** — **failure taxonomy** for validation findings and gate outcomes. **Not** automated triage rules in code.

**Version:** v0.

**Related:** [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [validation-escalation-model-v0.md](validation-escalation-model-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md).

---

## 1. Failure kinds

| Kind | Meaning |
|------|---------|
| **hard fail** | Definitive violation of contract, policy, or mandatory checklist item — default **blocking** (**V2**/**V3**). |
| **soft fail** | Quality or consistency issue with acceptable workaround or deferrable fix — often **V1**; may become **hard** if gate policy elevates it. |
| **structural fail** | Shape/decomposition wrong — aligns with **STRUCTURE CHANGE** signal; replan may be required. |
| **semantic fail** | Meaning mismatch across artifacts or semantic objects (CTA, trust, SEO intent, nav) per [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md). |
| **delivery fail** | Release / export / handoff package incomplete or inconsistent with approved candidate per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md). |
| **trust fail** | Trust signals dishonest, unverifiable, or contradicting claims — often **critical** lane. |
| **SEO fail** | Metadata / heading / thin content / internal link issues per SEO QA lane; severity depends on site policy. |
| **conversion fail** | CTA friction, unclear offer, broken primary conversion path per [conversion-intent-model-v0.md](conversion-intent-model-v0.md). |
| **QA drift** | QA narrative drifts from artifact SoT (e.g. stale blueprint reference, wrong revision). |
| **stale validation** | Pass verdict no longer justified after lineage, approval, freeze, or dependency change — treat as **invalidated** outcome class per [validation-lifecycle-v0.md](validation-lifecycle-v0.md). |

---

## 2. Propagation rules (conceptual)

| Source failure | Typical propagation |
|----------------|---------------------|
| **structural fail** | Upstream **plan** / blueprint scope; may invalidate multiple downstream validations. |
| **semantic fail** | Along semantic dependency edges per [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md). |
| **trust fail** / **critical** security | Blocks delivery cluster-wide until resolved (**project policy**). |
| **SEO fail** on hub page | May trigger **cluster** or **site** revalidation per [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md). |

---

## 3. Invalidation rules

- **Hard fail** on a consumed artifact **invalidates** validations that assumed the prior good state of that artifact.
- **Approval revocation** **invalidates** gate results that depended on that approval.
- **Freeze break** without re-approval **invalidates** validations predicated on frozen SoT.

---

## 4. Downstream impact

- **Blocking** failures prevent **artifact bus** consumption for forward routes per [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md).
- **Non-blocking** failures may still require **conditional_pass** documentation before delivery per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).

---

## 5. Re-open logic

- After fix: new validation episode from **requested** — see [validation-lifecycle-v0.md](validation-lifecycle-v0.md).
- After **waiver**: recorded **waived** outcome; downstream must carry waiver scope in audit trail per [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md).
- After **replan** (**STRUCTURE CHANGE**): prior structural validations are **invalidated**; breadth of rerun is **plan-defined**, not “auto rerun everything” per [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md).

---

*Last updated: 2026-05-12.*
