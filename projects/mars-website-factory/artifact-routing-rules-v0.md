# MARS Website Factory — Artifact Routing Rules v0

**Status:** **documentation only** — **authoritative routing discipline** for which artifact transfers are **allowed**, **forbidden**, **conditional**, or **invalidation-driven** between factory stages and QA substages. **Not** a router implementation, **not** Control Plane code, **not** automatic stage advancement.

**Version:** v0.

**Related:** [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md).

---

## 1. Routing authority

| Action | Authority |
|--------|-----------|
| **Open a standard forward route** (e.g. Blueprint → Design Handoff) | Producing stage lead + **HITL** per workflow-map gate when required. |
| **Approve conditional route** | Named approver for the **conditional** artifact / QA lane ([approval-semantics-v0.md](approval-semantics-v0.md)). |
| **Declare invalidation route** | Upstream owner or QA with **STRUCTURE CHANGE** / invalidation narrative; downstream consumers **stop** until realigned. |
| **Freeze routes** | HITL at design freeze (G5), release freeze (G7), or semantic freeze per semantic freeze doc — **no** autonomous freeze. |
| **Emergency rollback route** | Ops / client **G7-level** authority per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). |

---

## 2. Allowed routes (primary chain)

Canonical **forward** paths (each assumes prior gate satisfied):

```text
Intake / classification
  → Strategy
  → IA
  → Blueprint (S05)
  → Blueprint QA (S06)
  → Design Handoff (S07)
  → Design Production (S08)
  → Design QA (S09)
  → Frontend Handoff (S10)
  → Frontend Production (S11)
  → Frontend QA (S12)
  → Final Validation (S13)
  → Human Approval (S14)
  → Delivery / Export (S15)
```

**Example (user-requested narrative):**

```text
Blueprint
  → Design Handoff
  → Design QA
  → Frontend Handoff
```

*Note:* “Design QA” in the shorthand maps to **S09**; **Frontend Handoff** is **S10** — only after **G5** frozen design baseline per workflow v0.

---

## 3. Forbidden routes

| Forbidden pattern | Why |
|-------------------|-----|
| **Blueprint → Frontend Handoff** skipping Design Handoff + Design Production + Design QA | Breaks design freeze and handoff contracts. |
| **Draft blueprint → Design Handoff** without G3 batch approval + S06 pass/waiver | Approval discipline violation. |
| **Superseded artifact_id → new consumer** without supersede acknowledgment | Orphan / stale consumption. |
| **Delivery candidate assembly** from non-frozen upstream baselines | [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). |
| **G7 release** without S13 validation artifact | Release authority chain broken. |

---

## 4. Partial routes

**Partial route** = transfer scoped to **subset** of pages/templates/cluster (not whole site).

| Rule | Detail |
|------|--------|
| **Allowed** when **handoff_scope** and **approval_state** explicitly name the subset. |
| **Downstream** stages may execute partial route **only** for that subset; other pages remain on prior revision until explicitly transferred. |
| **QA** partial routes must declare which URLs/templates are in/out of scope for the verdict. |

---

## 5. Revision routes

| Trigger | Route |
|---------|--------|
| **Bounded CR** after QA | Return to **nearest** owning stage (often S05/S08/S11) with same **artifact_id** lineage extended by **revision_id** suffix policy. |
| **Structure change** | Back to Strategy / IA / Blueprint as impact requires; emit **STRUCTURE CHANGE**; may require **new artifact_id**. |

Revision routes **always** emit a new or updated **envelope** and REPORT entry.

---

## 6. Rollback routes

| Context | Route |
|---------|--------|
| **Design rollback** (pre-freeze) | S08 → S07/S05 per revision semantics; G4/G5 reopened. |
| **Release rollback** | **G7** selects **rollback candidate** baseline per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) — **not** silent file revert. |

Rollback **does not** delete history; it **re-selects** active baseline.

---

## 7. Invalidation routes

When upstream **semantic** or **structural** change invalidates downstream:

| Example (user-requested) | Effect |
|--------------------------|--------|
| **Frontend QA fail** exposing blueprint contradiction | **Invalidates** trust in **Delivery Candidate** assembly for affected scope; route back to **S05–S11** minimum slice per [dependency-invalidation-v0.md](dependency-invalidation-v0.md); **Final Validation** and delivery **blocked** until new QA pass. |

**Canonical shorthand (same meaning as the row above):**

```text
Frontend QA fail
  → invalidates Delivery Candidate
```

Invalidation routes are **declared** in REPORT with **artifact_ids** + **revision_ids** affected.

---

## 8. QA routes

| Route | Meaning |
|-------|---------|
| **Stage → same-stage QA** | e.g. S05 output → S06 QA envelope; **qa_state** updated on lane artifact. |
| **QA fail → upstream fix** | Return route to owning production stage; **not** skip QA on re-entry. |
| **Conditional pass → bounded downstream** | Forward route allowed **only** with listed CRs in **approval_state** / QA artifact. |

---

## 9. Delivery routes

| Route | Gate |
|-------|------|
| **Frozen production set → Delivery candidate** | S13 assembly per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). |
| **Delivery candidate → Export package** | After G7 `approved_release`. |
| **Post-delivery revision → new cycle** | Re-enters revision route slice toward S13–S14–S15; **not** in-place export mutation. |

---

## 10. Route freeze

When **freeze_state** includes `stage_frozen` or `release_frozen`:

- **Forward routes** from that artifact are **blocked** except audit/history/read-only references.
- **Invalidation routes** may still **fire** (truth over convenience) — they **do not** “unfreeze” silently; they trigger **reopen** HITL per [revision-semantics-v0.md](revision-semantics-v0.md).

---

## 11. Blocked routes

Operational **blocked routes** (temporary):

- **NEED HUMAN APPROVAL** pending;
- **SECURITY RISK** open;
- **UNKNOWN** binding missing.

Blocked status must appear on **envelope** or REPORT; **no** implied block without signal.

---

## 12. Conditional routes

Allowed **only** when all hold:

1. **Conditional** QA or approval artifact lists **bounds** (scope + time + CR ids).  
2. Downstream **handoff_scope** ⊆ approved scope.  
3. Expiration or CR burn-down is **tracked** — expiry **blocks** route extension.

---

## 13. Non-claims

- **Not** dynamic routing code in-repo.  
- **Not** parallel multi-cast to all stages.  
- **Not** automatic invalidation propagation without human-authored declarations.

---

## 14. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial routing rules (documentation only). |
| 2026-05-12 | **v0** — explicit **Frontend QA fail → invalidates Delivery Candidate** shorthand block in §7. |
