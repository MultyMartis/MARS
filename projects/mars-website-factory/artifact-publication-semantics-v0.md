# MARS Website Factory — Artifact Publication Semantics v0

**Status:** **documentation only** — **publication classes** and how artifacts become **visible and binding** for consumers. **Not** a CMS publish API, **not** CDN propagation, **not** package registry upload automation.

**Version:** v0.

**Related:** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md).

---

## 1. Publication model

**Publication** is the act of **declaring** an artifact’s **availability and binding strength** for downstream stages — via envelope + REPORT + (when used) handoff doc headers.

---

## 2. Publication classes

| Class | Meaning | Typical consumer rule |
|-------|---------|------------------------|
| **draft publication** | Work in progress; **not** binding for forward production routes. | Consumers may **preview** only with explicit “draft consumption” flag in prompt. |
| **review publication** | Ready for **internal** or **peer** review; not yet HITL-approved. | QA may **open** gates; **no** design freeze / **no** release. |
| **approved publication** | HITL gate satisfied for stated **handoff_scope**. | Forward routes **allowed** per [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md). |
| **frozen publication** | Baseline **immutable** for scope; matches G5/G6/G7 freeze postures. | **No** silent edits; revisions need reopen path. |
| **revoked publication** | Prior approval **withdrawn** per [approval-semantics-v0.md](approval-semantics-v0.md). | Consumers must **stop**; treat as **invalidation route**. |
| **deprecated publication** | Still readable for audit/migration but **must not** seed new forward routes. | Use only for rollback compare or legal retention. |
| **archived publication** | Lifecycle closed per [artifact-state-model-v0.md](artifact-state-model-v0.md) / delivery archive rules. | **No** new work without HITL reactivation narrative. |

---

## 3. Publication authority

| Class transition | Who may authorize |
|------------------|-------------------|
| draft → review | Authoring role (human / planned agent under supervision). |
| review → approved | **HITL** gate owner for that lane. |
| approved → frozen | **HITL** freeze gate (G5 design, G6 frontend, G7 release). |
| any → revoked | Original approver class or higher per security policy — **never** autonomous agent. |
| → deprecated / archived | PM / governance + HITL per project policy. |

---

## 4. Publication visibility

**Visibility** = who **may see** payload_reference (internal team, client, public leak risk).

- **Secrets / credentials** — **never** in publication payload (**forbidden**).  
- Narrow visibility **does not** relax **routing rules** — hidden routes are **forbidden** ([artifact-governance-rules-v0.md](artifact-governance-rules-v0.md)).

---

## 5. Publication freeze

Aligns **publication class** with **freeze_state**:

- **frozen publication** **implies** route freeze for that artifact scope.  
- Unfreeze **only** via documented reopen + revision per [revision-semantics-v0.md](revision-semantics-v0.md).

---

## 6. Publication rollback

**Rollback** at publication layer = **re-select** prior **frozen publication** baseline (especially delivery) per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md).

- **Does not** delete newer publication history.  
- New **Approval artifact** records the rollback decision.

---

## 7. Non-claims

- **Not** WordPress “Publish” button semantics as automation.  
- **Not** real-time subscriber notifications.

---

## 8. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial publication semantics (documentation only). |
