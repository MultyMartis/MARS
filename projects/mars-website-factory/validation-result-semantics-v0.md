# MARS Website Factory — Validation result semantics v0

**Status:** **documentation only** — **result shape vocabulary** aligned with [qa-result-payloads-v0.md](qa-result-payloads-v0.md). **Not** an API schema.

**Version:** v0.

**Related:** [validation-evidence-model-v0.md](validation-evidence-model-v0.md), [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md), [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md), [validation-escalation-model-v0.md](validation-escalation-model-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).

---

## 1. Validation result structure (conceptual)

| Field | Meaning |
|-------|---------|
| **verdict** | Outcome token aligned with lifecycle: e.g. pass, conditional_pass, fail, blocked, invalidated — see [validation-lifecycle-v0.md](validation-lifecycle-v0.md). |
| **severity** | Maximum severity across findings, mapped per §3. |
| **evidence** | Bundle per [validation-evidence-model-v0.md](validation-evidence-model-v0.md). |
| **affected_scope** | Stage, page, cluster, site slice, or semantic object set under review. |
| **impacted_artifacts** | Artifact types / envelopes whose consumption or publication is influenced by this result. |
| **escalation** | Optional escalation record per [validation-escalation-model-v0.md](validation-escalation-model-v0.md). |
| **waiver_eligibility** | Whether governance **allows** a waiver path for this finding class (**not** auto-waiver). |
| **confidence** | Overall confidence in the result aggregation (`low` \| `medium` \| `high`). |
| **blocking_status** | Whether downstream stage / delivery must halt per gate policy. |

---

## 2. Verdict vs blocking

- **Verdict** answers “what was concluded.”
- **blocking_status** answers “may the factory proceed regardless of narrative tone of non-blocker findings.”
- A **conditional_pass** may have **blocking_status** = false for stage advance but true for delivery until CRs close — project matrix decides (**SAFE UNKNOWN** default: treat unclear tables as **NEED HUMAN APPROVAL**).

---

## 3. Severity model — V0–V3

| Version token | Typical meaning | Maps to operational band |
|-----------------|-----------------|----------------------------|
| **V0** | Informational only — no gate impact unless policy says otherwise | **informational** |
| **V1** | Warning — proceed with documented risk; may require follow-up ticket | **warning** |
| **V2** | Blocking for next factory gate or handoff until resolved or waived | **blocking** |
| **V3** | Critical — security, legal exposure, catastrophic quality/trust break; halt and escalate | **critical** |

### 3.1 Band glossary

| Band | Gate impact (default) |
|------|------------------------|
| **informational** | Record only; does not block. |
| **warning** | Blocks only if gate policy binds warnings to HITL (common for brand-sensitive projects). |
| **blocking** | Standard stop for affected scope until fix, replan, or waiver. |
| **critical** | Stop + mandatory escalation path; may map to **SECURITY RISK** or **NEED HUMAN APPROVAL**. |

---

## 4. Alignment with QA payloads

[qa-result-payloads-v0.md](qa-result-payloads-v0.md) uses informal `info` \| `warn` \| `blocker`. Mapping guidance:

| qa-result-payloads hint | Suggested V-token |
|-------------------------|-------------------|
| `info` | **V0** |
| `warn` | **V1** (or **V2** if policy elevates warnings to blockers) |
| `blocker` | **V2** or **V3** depending on trust/security vs ordinary quality |

Exact enum unification remains **SAFE UNKNOWN** globally until a single registry row defines it.

---

*Last updated: 2026-05-12.*
