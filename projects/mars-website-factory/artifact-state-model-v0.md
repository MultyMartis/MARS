# MARS Website Factory — Artifact State Model v0

**Status:** **documentation only** — conceptual **lifecycle vocabulary** for logical artifacts in the Website Factory. **Not** a persisted state store, **not** a serialization contract, **not** an enforcement engine.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

[artifact-types-v0.md](artifact-types-v0.md) names artifact **classes** and **mutability spirit**. This document gives each artifact instance a **named lifecycle** so that:

- prompts ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md)) can declare which artifact state they consume and which they produce;
- transfers between stages ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md)) reference a stable state vocabulary;
- approval inheritance ([approval-semantics-v0.md](approval-semantics-v0.md)) is anchored to artifact states, not paraphrase;
- revisions and regenerations ([revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md)) operate on **explicit** state transitions;
- dependency invalidation ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)) has a **stable target**;
- QA findings ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)) attach to a **revision** and a **lifecycle state**.

This document **does not** redefine artifact classes, contract fields, or registry rows.

---

## 2. Artifact state vocabulary

| State | Meaning |
|-------|---------|
| **draft** | Artifact is **mutable**; authoring is in progress; no QA verdict; no approval. |
| **in_review** | Artifact is under **QA assessment** ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md)) and/or **HITL pre-approval** review. Authoring is **paused** during the review window. |
| **approved** | Artifact has **passed QA** for its revision and a **HITL approval** has been recorded ([approval-semantics-v0.md](approval-semantics-v0.md)). Downstream may consume the approved revision. |
| **frozen** | Approved artifact is **immutable** for the active execution scope. Frozen state is not terminal — it can be **broken** by a HITL-authorized revision. |
| **superseded** | A newer **artifact_id** (or a major revision bump) has **replaced** this one; the older artifact remains in audit but is **not** the source for downstream consumption. |
| **invalidated** | An upstream change ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)) has rendered the artifact **stale**; it must be revised or regenerated for the affected scope. |
| **deprecated** | The artifact class or contract on which this artifact was filed has been **retired** under governance; the artifact stays in audit but **must not** be used as a baseline for new work. |
| **archived** | The artifact is **closed** for the active execution scope (delivery finalized or scope abandoned). |

**Out of scope for v0:** internal sub-states (e.g. "draft.outline", "in_review.evidence_pending"). Prose annotations are allowed in REPORT bodies; new state tokens are not.

---

## 3. State transition rules

### 3.1 Allowed transitions

```text
   draft ─► in_review ─► approved ─► frozen
     │           │           │           │
     │           ▼           ▼           ▼
     │       (rejected) → revision    invalidated
     │           │           │           │
     ▼           ▼           ▼           ▼
   superseded ◄── revised / replaced ──┘
     │
     ▼
   deprecated / archived
```

| From → To | Trigger |
|-----------|---------|
| `draft → in_review` | Authoring closes; a QA prompt or HITL review begins ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §3). |
| `in_review → draft` | QA returns `fail` or `conditional` with revision scope **inside the same revision id**; or HITL requests revision. (Severity / verdict tuning forbidden — see [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §5.) |
| `in_review → approved` | QA verdict filed **and** HITL approval recorded ([approval-semantics-v0.md](approval-semantics-v0.md)). |
| `approved → frozen` | The stage's freeze anchor fires ([stage-state-model-v0.md](stage-state-model-v0.md) §8). |
| `approved → in_review` | A **revision** ([revision-semantics-v0.md](revision-semantics-v0.md)) is opened on the approved revision **before** freeze. New revision id required. |
| `frozen → in_review` | A **revision** is opened on a frozen baseline. **HITL-only** reopen ([§7](#7-mutable-vs-immutable-regions)). New revision id required. |
| `frozen → invalidated` | Upstream invalidation propagates ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)). |
| `approved → invalidated` | Upstream invalidation propagates before freeze. |
| `invalidated → in_review` | Artifact rerun (partial or full per [regeneration-semantics-v0.md](regeneration-semantics-v0.md)) closes; new revision is reviewed. |
| `any → superseded` | A new **artifact_id** (or a major version bump) **replaces** this artifact; the old artifact_id moves to `superseded` and is retained for audit. |
| `any non-archived → archived` | Execution scope closed with HITL closure narrative. |
| `any non-deprecated → deprecated` | Governance retires the artifact class or contract version on which this artifact was filed. |

### 3.2 Forbidden transitions

| From → To | Why forbidden |
|-----------|---------------|
| `draft → approved` | Skips QA + HITL. |
| `draft → frozen` | Skips QA + approval + freeze gate. |
| `in_review → frozen` | Freeze requires `approved`. |
| `approved → frozen` (silent / without freeze anchor) | Freeze is gate-driven, not implicit. |
| `frozen → approved` | Freeze is **post-approval**; reverting to "approved" hides freeze breaking. |
| `frozen → draft` (silent) | Freeze breaking is HITL-only. |
| `superseded → approved` | Resurrecting a superseded artifact requires a new `artifact_id`. |
| `archived → anything` | Archival is closure for the active scope. |
| `deprecated → approved` | Governance must revive the class before any artifact filed under it can become a baseline again. |

Any forbidden transition observed → emit **STRUCTURE CHANGE** or **NEED HUMAN APPROVAL** per [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 4. State per artifact class (overview)

The mutability rows of [artifact-types-v0.md](artifact-types-v0.md) map onto this state vocabulary as follows.

| Artifact class | Typical `draft` | Becomes `approved` | Becomes `frozen` | Typical `invalidated` causes | Typical `superseded` causes |
|----------------|------------------|--------------------|------------------|------------------------------|-----------------------------|
| Intake artifact | Discovery phase | G1 approval of scope_in/scope_out | Once scope is locked for downstream | Scope reopen | Project reset |
| Strategy / SEO strategy | Hypothesis drafting | G2 | After G2 narrative is referenced downstream | Conflicting funnel; major brand change | Brand pivot |
| IA artifact | Sitemap / templates drafting | G3 (partial) | After G3 | Stack change; site type pivot | Site relaunch |
| Blueprint artifact | Per-page drafting | G3 batch | G3 freeze | Block registry amendment; CTA model change | Page taxonomy redesign |
| Design handoff artifact | Pack assembly | Design lead sign-off | G5 | Blueprint revision; design-system change | New brand identity |
| Design artifact | Iteration | G4 / G5 | G5 | Blueprint revision; component-state addition | New visual direction |
| Frontend handoff artifact | Spec drafting | Tech lead approval | At S11 start | Design revision; framework decision change | Stack pivot |
| Frontend production artifact | Source under change control | G6 | Release tag intent | Design revision; structural CR | Project re-platform |
| QA artifact | Within a single run | Verdict filed | n/a (verdict per run) | Upstream artifact revised | New run on new revision |
| Validation artifact | Within S13 run | Go/no-go recorded | n/a | Cross-lane invalidation | New final-validation run |
| Approval artifact | n/a (never draft) | Recorded once | Always immutable post-record | n/a | Revoked → new approval cycle |
| Delivery artifact | Pack assembly | Pre-delivery validated | At release approval | Hotfix revision | Re-release |

This table is a **map**, not an enumeration of every transition; lifecycle rules in §3 govern actual transitions.

---

## 5. Approval inheritance

Approval ([approval-semantics-v0.md](approval-semantics-v0.md)) attaches to a **specific revision** of an artifact. Inheritance rules:

- A downstream artifact consumes an upstream artifact in **`approved`** or **`frozen`** state by referencing **artifact_id + revision** ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §2).
- The downstream artifact **inherits** approval **scope** (what was approved), **not** approval **authority**: downstream still requires its own gate.
- Conditional approvals ([approval-semantics-v0.md](approval-semantics-v0.md) §conditional) **must** be propagated downstream as bounded CRs; downstream prompts respect them.
- If the upstream artifact moves to `invalidated`, `superseded`, or `deprecated`, downstream **inherited** approval is **broken** for the affected scope ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)).

Forbidden:

- treating a `draft` upstream as `approved` for inheritance;
- treating a conditional approval as a full freeze;
- silently re-anchoring a downstream artifact from a superseded upstream to a new artifact_id without a new revision pass.

---

## 6. Artifact lineage

Every artifact instance has a **lineage**:

1. **artifact_id** (stable per project convention; see [artifact-types-v0.md](artifact-types-v0.md) §`artifact_id` philosophy);
2. **revision** (suffix or changelog row per project convention);
3. **upstream references** (artifact_id + revision for each upstream artifact this one depends on);
4. **downstream references** (which downstream artifact_ids consume this one; may be tracked in lineage notes or REPORT bodies);
5. **state history** (state transitions recorded in audit narrative or REPORT bodies);
6. **QA history** ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)) attached to revision;
7. **approval history** (Approval artifact references) attached to revision.

Lineage rules:

- **No silent re-parenting:** changing upstream references is itself a revision ([revision-semantics-v0.md](revision-semantics-v0.md)).
- **No paraphrase references:** lineage rows cite **artifact_id + revision**, not "the previous blueprint".
- **No orphan artifacts:** an artifact whose upstream references resolve to `superseded`, `invalidated`, or `deprecated` must be re-anchored explicitly.

Lineage is **prose discipline** in v0; no graph database is implied.

---

## 7. Mutable vs immutable regions

An artifact instance may have **both** mutable and immutable regions depending on its state and the **structural significance** of the field. Anchored to [artifact-types-v0.md](artifact-types-v0.md) and the relevant contracts ([page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)):

| Artifact state | Mutable regions | Immutable regions |
|----------------|------------------|-------------------|
| `draft` | All authoring fields. | `artifact_id`, lineage upstream references (changing upstream is a re-anchor, not a draft edit). |
| `in_review` | None (authoring paused for the review window). | All fields under review. |
| `approved` | Bounded CR fields only ([approval-semantics-v0.md](approval-semantics-v0.md) §conditional). | Structural fields (e.g. blueprint `site_type_id`, block ordering) unless reopened. |
| `frozen` | None. | Entire artifact body for the active scope. |
| `invalidated` | None until rerun. | Entire body; rerun produces a new revision. |
| `superseded` | None. | Entire body; reference only via the new artifact_id. |
| `deprecated` | None. | Entire body; do not use as baseline. |
| `archived` | None. | Entire body. |

**Freeze breaking** ([revision-semantics-v0.md](revision-semantics-v0.md)) is the **only** path to modify an immutable region; it requires HITL and creates a new revision id.

---

## 8. Artifact references

References between artifacts ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §2 + §8) must include:

| Field | Rule |
|-------|------|
| **artifact_id** | Stable string per project convention. |
| **revision** | The revision being referenced. |
| **state at time of reference** | `draft` / `in_review` / `approved` / `frozen` / `superseded` / `invalidated` / `deprecated` / `archived`. |
| **contract anchor** | The contract or registry field being relied on. |

A reference to a `superseded`, `invalidated`, `deprecated`, or `archived` artifact is **read-only audit**: it may appear in lineage notes, but **must not** be used as a downstream baseline.

If a referenced artifact's state at consumption time differs from the documented contract expectation (e.g. consuming `draft` where the workflow requires `approved`) → emit **UNKNOWN** or **NEED HUMAN APPROVAL** ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)).

---

## 9. Artifact replacement philosophy

There are **three** mechanisms by which an artifact's content is replaced:

| Mechanism | When to use | Result |
|-----------|--------------|--------|
| **Revision** ([revision-semantics-v0.md](revision-semantics-v0.md)) | Same artifact_id, bounded scope change. | New revision (e.g. `v1` → `v1.1`); QA reset per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md); downstream may be invalidated where it intersects the change. |
| **Regeneration** ([regeneration-semantics-v0.md](regeneration-semantics-v0.md)) | Same artifact_id, re-production of artifact content (partial or full) under existing scope. | New revision; QA reset; explicit boundary on what content was regenerated. |
| **Supersede** | New artifact_id replaces the old one entirely (e.g. blueprint pivot, brand redesign). | Old artifact → `superseded`; new artifact_id starts at `draft`; downstream consumers re-issued prompts against the new id. |

A **rollback** ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §rollback) is **not** a replacement of an artifact body; it is a **selection** of a prior approved revision as the active baseline. The prior revision moves back to `approved` / `frozen` under HITL while later revisions move to `superseded` for the active scope.

Forbidden:

- silent in-place edits to a frozen artifact body;
- replacing a superseded artifact's old content with new content under the same revision id;
- using "revision" terminology for a supersede (or vice versa) — the lifecycle effect differs.

---

## 10. QA relationship

Per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) and [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md):

- QA findings ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)) attach to **artifact_id + revision + state**.
- When an artifact moves from `approved` → `in_review` (revision opened), all open QA findings for the prior revision become **stale** for the new revision unless explicitly carried forward.
- When an artifact moves to `invalidated`, all QA verdicts for the affected scope are **stale**; re-QA required on the new revision.
- A `superseded` artifact's QA history is preserved as audit; new artifact_id starts QA fresh.
- A `deprecated` artifact's QA history is frozen; no new QA permitted.

QA never **promotes** an artifact from `in_review` to `approved`; HITL does ([approval-semantics-v0.md](approval-semantics-v0.md)).

---

## 11. SAFE UNKNOWN handling

Per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) and [safe-unknown-boundary.md](safe-unknown-boundary.md):

- When a required artifact field cannot be evidenced, the artifact remains in `draft` (or `in_review` if a HITL waiver is in scope) and the gap is labeled **SAFE UNKNOWN** in the artifact body.
- A SAFE UNKNOWN entry **does not** block transitioning to `approved` **if** policy allows bounded continuation with a named approver.
- An UNKNOWN entry (hard missing binding) **blocks** transitioning to `approved` until resolved or escalated to HITL.
- A `frozen` artifact that later reveals a SAFE UNKNOWN gap requires a **revision** to either resolve or formally record the gap with HITL acceptance; it cannot be silently amended.

SAFE UNKNOWN is not a state — it is a **content annotation** that may coexist with `draft`, `in_review`, `approved`, or (under bounded HITL acceptance) `frozen`.

---

## 12. Tie to artifact-types-v0

The lifecycle states defined here **realize** the prose mutability rows of [artifact-types-v0.md](artifact-types-v0.md):

| artifact-types-v0 prose | This document's state |
|--------------------------|------------------------|
| "Mutable during X" | `draft` |
| "Reviewed / under sign-off" | `in_review` |
| "Approved", "Approved memo", "Approved baseline" | `approved` |
| "Frozen", "Immutable baseline", "Frozen for downstream" | `frozen` |
| "Superseded" / "supersede" | `superseded` |
| "Stale" / "Re-run required" / "Invalidated by upstream" | `invalidated` |
| "Retired" / "Deprecated class" | `deprecated` |
| "Closed" / "End of scope" | `archived` |

No conflict is introduced; if a future doc edit produces a conflict, this state vocabulary is the **operational** truth and [artifact-types-v0.md](artifact-types-v0.md) is the **classification** truth — both should be aligned in the same revision pass.

---

## 13. Tie to handoff contracts

The two key handoff contracts use specific lifecycle anchors:

| Contract | Handoff lifecycle anchor |
|----------|---------------------------|
| [Design Handoff Contract v0](design-handoff-contract-v0.md) | The handoff pack is consumable when its referenced blueprint is `approved` (G3) and the design pack itself is at least `approved` (design lead sign-off); design production produces a design artifact that moves through `draft → in_review → approved → frozen` at G5. |
| [Frontend Handoff Contract v0](frontend-handoff-contract-v0.md) | The handoff spec is consumable when its referenced blueprint and design are `frozen` (G3 + G5) and the spec itself is `approved` (tech lead approval before S11); frontend production produces a frontend artifact that moves through `draft → in_review → approved → frozen` at G6. |

Consuming a handoff that depends on a `draft` upstream is a scope violation per [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §4.

---

## 14. Tie to workflow v0

[website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S01–S15 names input / output artifacts per stage. The state model adds:

| Workflow concept | State model anchor |
|------------------|--------------------|
| `input artifacts` row | Required state of upstream artifacts at consumption time. |
| `output artifacts` row | Initial state of produced artifact (`draft`). |
| `HITL requirements` row | Anchors `in_review → approved` and `approved → frozen` transitions. |
| `SAFE UNKNOWN escalation` row | Governs allowable bounded continuation while artifact gaps exist. |
| `downstream dependencies` row | Governs which downstream artifact transitions are gated by this stage's freeze. |

---

## 15. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Frozen artifact updated with minor copy fix." | Silent freeze breaking. | Revision request + new revision id + HITL. |
| "Superseded artifact reused for delivery." | Audit-only artifact promoted. | Reference the active artifact_id. |
| "Approved without QA verdict." | Skips lifecycle. | QA verdict filed before approval. |
| "Draft consumed by downstream." | Skips approval. | Wait for approval or document explicit allowed-mutable read. |
| "Invalidated downstream not acknowledged." | Silent staleness. | Explicit invalidation REPORT entry per [dependency-invalidation-v0.md](dependency-invalidation-v0.md). |
| "SAFE UNKNOWN gap added to a frozen artifact." | Freeze body mutated. | Revision request + HITL acceptance of the gap. |
| "Conditional approval treated as full freeze." | Approval scope exceeded. | Bounded CR list propagated downstream. |

---

## 16. Non-claims

- This document does **not** ship a state store, artifact bus, or persistence layer.
- It does **not** assume an LLM enforces these states.
- It does **not** define wire formats for artifact bodies.
- It does **not** replace human judgment with predictable agent behavior.

What it **does** do is define **a stable lifecycle vocabulary** for factory artifacts so transfers, revisions, regenerations, invalidations, and approvals operate on **explicit named states** rather than paraphrase.

---

## 17. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial artifact state model (documentation only). |
