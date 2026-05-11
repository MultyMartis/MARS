# MARS Website Factory — Approval Semantics v0

**Status:** **documentation only** — defines the **meaning, scope, and lifecycle** of approvals across the factory. **Not** an approval engine, **not** a signing infrastructure, **not** an identity provider, **not** a runtime approval store.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [`../../security/approval-gates.md`](../../security/approval-gates.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

[hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) defines **where HITL approval is mandatory**. [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §5 defines **how approval inherits downstream**. [artifact-types-v0.md](artifact-types-v0.md) §Approval artifact defines **the record of an approval**.

This document adds the **temporal and scope semantics** that those documents assume:

- what an approval **means** vs what it **does not** mean;
- what **scope** an approval covers;
- when an approval is **partial** or **conditional**;
- when an approval **freezes** a baseline;
- when an approval **inherits** downstream;
- when an approval **expires**;
- when an approval is **revoked**;
- how QA-linked approvals differ from delivery approvals;
- how SAFE UNKNOWN and SECURITY RISK interact with approvals.

It does **not** ship a signing protocol or approval workflow engine.

---

## 2. Approval meaning

An **approval** is a **HITL-issued decision** that a specific artifact revision (or stage exit) is **good enough** to advance the workflow under a **bounded scope**. It is recorded as an **Approval artifact** ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact) with:

- decision (`approve` / `reject` / `revise` / `park`),
- approver role (named role, not "the team"),
- date,
- referenced artifact_id + revision,
- gate identifier (e.g. `G3`, `G5`, `G6`, `G7`),
- conditions (if conditional),
- waivers (if any),
- expiration window (if applicable).

What an approval **is not**:

| Approval is **not** | Honest alternative |
|----------------------|---------------------|
| A blanket release for the entire project. | Scope-bounded approval per gate. |
| A guarantee of downstream success. | Downstream still requires its own gate. |
| Permission to fabricate. | SAFE UNKNOWN gaps remain disclosed. |
| Permission to skip QA on later revisions. | Revisions reset QA per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md). |
| Self-renewing. | Renewal requires a new HITL pass. |
| Transferable to a different artifact_id. | New artifact_id starts at `draft` ([artifact-state-model-v0.md](artifact-state-model-v0.md) §9). |

**No fake autonomous approval.** Per [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) §2 + §7, **only HITL** can finalize approvals. An agent that emits an "Approval artifact" without a recorded HITL decision is **fabricating**.

---

## 3. Approval scope

Every approval has a **named scope**. Scope dimensions:

| Dimension | Examples |
|-----------|----------|
| **Artifact scope** | One artifact_id; one revision; a batch (e.g. a set of blueprint artifact_ids); a delivery package. |
| **Stage scope** | Approval anchors a specific stage's exit per gate (G1–G7 per [workflow-map.md](workflow-map.md)). |
| **Lane scope** | Design lane / SEO lane / Conversion lane / Frontend lane / Cross-cutting. |
| **Page scope** | Single page / template / batch / full site. |
| **Time scope** | Indefinite for the active execution scope; or bounded by an expiration window (e.g. "release approval valid for this release cycle only"). |
| **Decision scope** | Full approve / conditional / partial / waiver / park. |

Scope rules:

- An approval **only** covers what its scope names. Out-of-scope claims are **not** approved.
- A downstream prompt that needs approval outside the named scope **must** request a new approval.
- An approval for one page is **not** an approval for another page in the same batch unless the batch scope is explicit.

Forbidden:

- treating a single-page approval as a batch approval;
- treating a batch approval as a full-site approval;
- treating a stage approval as a delivery approval;
- treating a lane approval as a cross-lane approval.

---

## 4. Partial approval

A **partial approval** approves a **subset** of an artifact batch or scope while leaving other parts unapproved.

| Aspect | Detail |
|--------|--------|
| **Trigger** | HITL approves a subset (e.g. 8 of 12 blueprint pages) and defers the rest. |
| **Recording** | Approval artifact enumerates **which** artifact_ids + revisions are approved and **which** remain `in_review` / `draft`. |
| **Downstream effect** | Downstream stages may proceed **only** on the approved subset; the unapproved subset remains blocked. |
| **Forbidden** | "Partial approval interpreted as full approval" — the unapproved subset stays gated. |
| **HITL discipline** | Partial approval is a **single HITL event** with explicit enumeration, not a vague "most of it". |

A partial approval **does not** become full approval over time without a new HITL pass.

---

## 5. Conditional approval

A **conditional approval** approves an artifact revision **subject to bounded corrections** (CRs) that must be addressed before the next freeze or downstream consumption.

| Aspect | Detail |
|--------|--------|
| **Trigger** | QA emits `pass conditional` or HITL approves with a bounded CR list ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) §conditional pass). |
| **Recording** | Approval artifact enumerates each CR with severity, evidence reference, and resolution path. |
| **Downstream effect** | Downstream prompts must respect the CRs as **active obligations**; they are not optional. |
| **Resolution** | CRs are resolved within the **same revision id** (no new revision required) when scope allows; otherwise a new revision id is opened ([revision-semantics-v0.md](revision-semantics-v0.md)). |
| **Forbidden** | Treating a conditional approval as a full freeze; widening the CR list silently; closing CRs without evidence. |

A conditional approval is **not** a waiver. CRs **must** be resolved or explicitly waived under a named approver before freeze.

---

## 6. Approval freeze

An approval **freezes** an artifact baseline when the gate is anchored to the artifact's freeze transition ([artifact-state-model-v0.md](artifact-state-model-v0.md) §3, [stage-state-model-v0.md](stage-state-model-v0.md) §8).

| Approval | Freeze anchor |
|----------|----------------|
| G1 | Intake scope_in / scope_out frozen for downstream. |
| G2 | Strategy / SEO narrative frozen for blueprint stage. |
| G3 | IA + blueprint batch frozen for design handoff. |
| G5 | Design baseline frozen for frontend handoff. |
| G6 | Frontend release tag intent frozen for final validation. |
| G7 | Delivery package frozen for release. |

Rules:

- Freeze **does not** happen without an approval; freeze is **not implicit** ([artifact-state-model-v0.md](artifact-state-model-v0.md) §3.2).
- A frozen artifact is **immutable for the active scope** ([artifact-state-model-v0.md](artifact-state-model-v0.md) §7).
- Freeze does **not** prevent revision; freeze prevents **silent** mutation. A HITL-approved revision is the only path to break freeze.

---

## 7. Approval inheritance

Per [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §5:

| Upstream approval | Downstream effect |
|--------------------|--------------------|
| G1 (intake) | Strategy / SEO / IA may rely on `scope_in` / `scope_out` as immutable. |
| G2 (strategy / SEO) | Blueprint stage may rely on narrative + intent as immutable. |
| G3 (IA + blueprint batch) | Design handoff may rely on URLs, templates, block ordering as immutable. |
| G5 (design freeze) | Frontend handoff may rely on visual baseline as immutable. |
| G6 (frontend) | Final validation may rely on the file set as immutable. |
| G7 (release) | Delivery may package the approved baseline. |

Inheritance rules:

- Downstream **inherits scope**, not **authority** — downstream still requires its own gate.
- A **conditional** approval propagates **as a list of bounded CRs** that downstream must respect.
- A **partial** approval propagates **only for the approved subset**.
- Approval inheritance **breaks** when the upstream artifact moves to `invalidated`, `superseded`, or `deprecated` ([artifact-state-model-v0.md](artifact-state-model-v0.md) §5).

Forbidden:

- treating a partial / conditional approval as full upstream freeze;
- silently re-anchoring a downstream artifact from a `superseded` upstream to a new artifact_id without a new approval pass.

---

## 8. Approval expiration

An approval **may expire** if its time scope is bounded. Examples:

- A release approval (G7) is valid **for this release cycle only**; subsequent releases require a new G7 pass.
- A SAFE UNKNOWN-bounded continuation under a named approver may expire when the bounding condition is no longer met.
- A waiver may be **per-revision** (expires when a new revision opens) or **permanent** (until a new HITL pass revokes it).

Rules:

- Expiration is **recorded** on the Approval artifact ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact).
- An **expired** approval is **not** silently active. Downstream consumption of an expired approval is treated as `UNKNOWN` ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)) until a new approval is recorded.
- Expiration **does not** retroactively undo prior approved work; it gates **future** consumption.

Forbidden:

- silent renewal of expired approvals;
- treating "approval not explicitly expired" as "approval valid forever".

---

## 9. Approval revocation

An approval **may be revoked** by a HITL-issued decision that explicitly **undoes** a prior approval. Triggers:

- a `STRUCTURE CHANGE` invalidates the approved scope upstream;
- a `SECURITY RISK` finding requires reopening the approved baseline;
- a regulatory / legal finding requires reopening;
- a new HITL pass overrides a prior decision (with audit narrative).

Rules:

- Revocation is recorded as a **new** Approval artifact (decision = `revoke`) referencing the prior Approval artifact id.
- A revoked approval moves the affected artifact from `approved` / `frozen` → `in_review` (or `invalidated` if upstream propagation applies).
- Downstream artifacts that inherited the revoked approval move to `invalidated` per [dependency-invalidation-v0.md](dependency-invalidation-v0.md).
- Revocation requires the **same or higher-authority** approver as the original approval.

Forbidden:

- silent revocation (no Approval artifact);
- "revocation by inaction" — a stale approval is not revoked unless explicitly recorded.

---

## 10. QA-linked approvals

QA verdicts ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md)) are **recommendations**, not approvals. The relationship:

| QA verdict | HITL approval behavior |
|-------------|-------------------------|
| `pass` | HITL may approve without conditions. |
| `pass conditional` | HITL may approve with the QA-listed CRs as approval conditions ([§5](#5-conditional-approval)). |
| `fail` | HITL **must not** approve; either revise ([revision-semantics-v0.md](revision-semantics-v0.md)) or waive specific blockers under HITL. |
| `SAFE UNKNOWN` finding | HITL may approve with bounded continuation per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md). |
| `UNKNOWN` finding | HITL **must not** approve until resolved. |

A waiver-based approval ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §6) requires:

- a named approver;
- bounded scope (this revision / this run / permanent);
- risk note + downstream impact recorded;
- finding remains attached to the artifact's QA history (waiver does not delete findings).

QA cannot **self-approve** its own waiver; the QA agent emits `NEED HUMAN APPROVAL` and waits.

---

## 11. Delivery approvals

Delivery approvals (G7) follow [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md):

| Aspect | Detail |
|--------|--------|
| **Trigger** | Final Validation (S13) produces a go/no-go recommendation; delivery candidate is assembled ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §candidate). |
| **Approver** | Ops / client (per [workflow-map.md](workflow-map.md) §Artifact approval gates). |
| **Scope** | Delivery package contents (artifact_ids + revisions + manifest); release target (project-specific, **SAFE UNKNOWN** for hosting / CDN unless documented). |
| **Recording** | Approval artifact + release tag intent + rollback notes. |
| **Forbidden** | "Approved for deploy" without G7; "CI green" without evidence; deployment automation claims. |
| **Post-delivery** | Post-delivery revisions reopen the delivery lifecycle under HITL ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §post-delivery revision). |

A delivery approval is **not** a deployment; per [safe-unknown-boundary.md](safe-unknown-boundary.md), no deployment automation is claimed.

---

## 12. Tie to security and risk

Per [`../../security/approval-gates.md`](../../security/approval-gates.md) and [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) §8:

- **MARS-wide approval policy** takes precedence over factory gates where stricter.
- **SECURITY RISK** ([`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md)) findings **block** approval until cleared; a waiver requires additional named approval.
- **SAFE UNKNOWN** bounded continuations are HITL-anchored and require a named approver.
- Risk-register rows ([`../../governance/risk-register.md`](../../governance/risk-register.md)) are referenced when a waiver creates new risk exposure.

---

## 13. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Approved by AI Designer Agent." | No agent approves. | HITL approval at G5 with named approver. |
| "Conditional approval treated as freeze." | Approval scope exceeded. | Bounded CR list propagated downstream. |
| "Partial approval applied to the whole batch." | Scope drift. | Approval applies only to the named subset. |
| "Re-approved with minor change." | Silent re-approval. | New HITL pass + new revision id. |
| "Approval still valid (no expiration was noted)." | Stale approval not refreshed. | Treat as `UNKNOWN` until a new approval. |
| "Waiver self-approved by the QA agent." | Bypasses HITL. | `NEED HUMAN APPROVAL` + wait. |
| "Delivery approved by Final Validation." | S13 is recommendation, not authority. | G7 HITL approval. |
| "Approval re-used for a different artifact_id." | Scope mismatch. | New approval pass per artifact_id. |

---

## 14. Non-claims

- This document does **not** ship an approval workflow engine.
- It does **not** imply automated approver notifications.
- It does **not** define cryptographic signing.
- It does **not** assume approvers are notified or queried automatically.
- It does **not** replace human judgment with predictable agent behavior.

What it **does** do is define **how an approval behaves over time**, **what scope it covers**, and **what the prompt and report must say** when an approval is granted, conditional, partial, expired, revoked, or inherited.

---

## 15. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial approval semantics (documentation only). |
