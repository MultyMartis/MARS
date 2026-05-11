# MARS Website Factory — Delivery Lifecycle v0

**Status:** **documentation only** — defines the **release-side lifecycle**: delivery candidate, pre-delivery validation, release approval, freeze, export package, deployment handoff, rollback, archive, post-delivery revision. **Not** deployment automation, **not** a CI/CD pipeline, **not** a release manager service.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [artifact-types-v0.md](artifact-types-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [frontend-production-model.md](frontend-production-model.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [`../../security/approval-gates.md`](../../security/approval-gates.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

[website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S13–S15 names Final Validation, Human Approval, and Delivery / Export. [artifact-types-v0.md](artifact-types-v0.md) names the Validation artifact, Approval artifact, and Delivery artifact.

This document adds **release-side lifecycle behavior**:

- when a **delivery candidate** is assembled;
- what **pre-delivery validation** includes;
- how **release approval** behaves at G7;
- what **freeze** means at delivery;
- what an **export package** contains;
- how **deployment handoff** works without claiming deployment automation;
- how **rollback** behaves;
- how **archive** behaves;
- how **post-delivery revisions** reopen the lifecycle.

Per [safe-unknown-boundary.md](safe-unknown-boundary.md), **no deployment automation** is claimed. Delivery is a **state**, not a deployment event.

---

## 2. Delivery candidate

A **delivery candidate** is the **assembled set** of artifact baselines proposed for release. It comprises:

| Component | Source |
|-----------|--------|
| Frontend production artifact | `frozen` at G6 ([artifact-state-model-v0.md](artifact-state-model-v0.md)). |
| Frozen design artifact | `frozen` at G5. |
| Approved blueprints | `frozen` at G3 (per affected pages / batch). |
| Approved strategy / SEO | `frozen` after G2. |
| Approved IA | `frozen` after G3. |
| QA reports (per lane) | `closed_pass` / `closed_conditional` / `closed_waived` per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md). |
| Validation artifact | Filed at S13 ([artifact-types-v0.md](artifact-types-v0.md) §Validation artifact). |
| Risk summary | Open SAFE UNKNOWN entries, open waivers, security notes. |
| Rollback notes | Prior release / baseline reference for rollback ([§9](#9-rollback-candidate)). |
| Delivery manifest | Per [§6](#6-export-package): artifact_ids + revisions + checksums (when defined). |

Candidate states:

| State | Meaning |
|-------|---------|
| **proposed** | Candidate has been assembled; Final Validation gate is `open` or `assessing`. |
| **validated** | Final Validation gate is `verdict_filed` with a go/no-go recommendation. |
| **release_pending** | Release approval (G7) is pending. |
| **approved_release** | G7 approved; candidate is the active release baseline. |
| **rejected** | G7 rejected; revision required ([revision-semantics-v0.md](revision-semantics-v0.md)). |
| **held** | G7 deferred (e.g. waiting on external signoff). |
| **released** | Release authorization recorded; handoff scheduled or completed ([§7](#7-deployment-handoff)). |
| **rolled_back** | A prior baseline is the active release; this candidate is no longer the baseline ([§9](#9-rollback-candidate)). |
| **archived** | Release cycle closed ([§10](#10-archive-philosophy)). |

A delivery candidate **does not** become a release until G7 ([approval-semantics-v0.md](approval-semantics-v0.md) §11).

---

## 3. Pre-delivery validation

Pre-delivery validation occurs at **S13 Final Validation** ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) §Stage 13). Lifecycle:

| Step | Detail |
|------|--------|
| **Assemble candidate** | Collect frozen artifacts + open issues + open waivers + risk summary. |
| **Run cross-lane QA** | SEO QA, Conversion QA, Frontend QA, Validator overlap on the candidate ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |
| **Check consistency** | End-to-end: links, metadata, legal pages, schema, asset paths. |
| **Check delivery manifest** | All referenced artifact_ids resolve to `frozen` revisions; no `draft` / `superseded` / `invalidated` references. |
| **Check open signals** | UNKNOWN bindings, SECURITY RISK findings, SAFE UNKNOWN entries — must be enumerated. |
| **Emit verdict** | `go` (safe to release) / `no-go` (release blocked) / `conditional` (release with bounded conditions) per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) §4. |
| **REPORT** | Validation REPORT enumerates verdict, evidence, open signals, recommendation. |

The Validation artifact ([artifact-types-v0.md](artifact-types-v0.md) §Validation artifact) is **immutable for that run id**; subsequent reruns produce **new** Validation artifact instances.

Pre-delivery validation **does not** grant release authority — it provides a **recommendation** ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §4). G7 is the release authority.

---

## 4. Release approval

Release approval (G7) follows [approval-semantics-v0.md](approval-semantics-v0.md) §11:

| Aspect | Detail |
|--------|--------|
| **Trigger** | Validation artifact filed at S13. |
| **Approver** | Ops / client per [workflow-map.md](workflow-map.md) §Artifact approval gates. |
| **Decision options** | `approve_release` / `reject` / `hold`. |
| **Scope** | Delivery package contents (artifact_ids + revisions + manifest); release cycle / time window. |
| **Recording** | Approval artifact with release tag intent + risk summary + rollback notes + expiration window (if applicable). |
| **Forbidden** | "Approved for deploy" without G7; "CI green" without evidence; deployment automation claims; release tagging by agents. |

Release approval **does not** trigger deployment. It **authorizes** subsequent deployment handoff ([§7](#7-deployment-handoff)) under whatever method the project uses (manual deploy, ops runbook, hosting handoff — all project-specific).

---

## 5. Freeze state

When G7 approves the release, the delivery candidate moves to **`approved_release`** and its component artifacts are **release-frozen**:

| Aspect | Detail |
|--------|--------|
| **Artifact state** | All component artifact baselines remain `frozen` ([artifact-state-model-v0.md](artifact-state-model-v0.md)). |
| **Stage state** | S13 (Final Validation) and S14 (Human Approval) move to `approved` / `frozen` ([stage-state-model-v0.md](stage-state-model-v0.md)). |
| **Mutation** | The release baseline is **immutable**; any change after G7 requires a **post-delivery revision** ([§11](#11-post-delivery-revision)). |
| **Reference** | Release tag intent (project-specific format; **SAFE UNKNOWN** for git tagging convention unless the project defines one). |
| **Audit** | Release baseline + Approval artifact + Validation artifact compose the release audit row. |

Release freeze **does not** automate any external system; it documents the immutability of the released set for the active scope.

---

## 6. Export package

The **export package** ([artifact-types-v0.md](artifact-types-v0.md) §Delivery artifact) is the **deliverable bundle** for release. Contents:

| Component | Notes |
|-----------|-------|
| **Frontend build output** | Static files (HTML / CSS / JS / assets) produced per [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [frontend-production-model.md](frontend-production-model.md). |
| **Documentation bundle** | Approved blueprints, strategy / SEO memos, design handoff, frontend handoff, QA reports, Validation report, Approval artifact reference. |
| **Manifest** | Enumerates artifact_ids + revisions + checksums (when defined). |
| **Runbook** | Project-specific deployment runbook (if any); otherwise **SAFE UNKNOWN**. |
| **Rollback notes** | Prior release baseline reference; pre-release / post-release state snapshot. |
| **Risk summary** | Open waivers, SAFE UNKNOWN entries, security notes. |

Format rules:

- The export package **format** is **project-specific**. v0 does **not** mandate a file layout, manifest schema, or checksum algorithm.
- Export **must** be assembled from frozen artifacts only; assembling from `draft` / `in_review` / `invalidated` is forbidden.
- Export **does not** include credentials, secrets, or deployment automation scripts unless the project explicitly defines an export-safe scope ([`../../security/approval-gates.md`](../../security/approval-gates.md), [`../../security/threat-model-v0.md`](../../security/threat-model-v0.md)).

---

## 7. Deployment handoff

Deployment handoff is **explicit and human-driven** in v0:

| Step | Detail |
|------|--------|
| **Approved release** | G7 recorded; export package assembled. |
| **Hand to ops / client** | Project-specific handoff method (email, secure file transfer, ops portal, vendor portal). |
| **Deployment execution** | Performed by ops / client per project runbook; **not** owned by the factory. |
| **Smoke test** | Performed on target environment **when known**; otherwise **SAFE UNKNOWN** in delivery notes ([safe-unknown-boundary.md](safe-unknown-boundary.md)). |
| **Confirmation** | Ops / client confirms deployment success / failure in the project record; factory REPORT references the confirmation. |

Forbidden:

- claiming the factory deployed the site;
- claiming "live on production" without ops confirmation;
- emitting deployment automation runs from the factory's prompts;
- assuming hosting / CDN / DNS details unless the project documents them.

Per [safe-unknown-boundary.md](safe-unknown-boundary.md) §Integrations, no direct integration with hosting / CI is assumed.

---

## 8. Post-deployment smoke

After deployment confirmation, the factory may perform a **post-deployment smoke** check:

| Scope | Detail |
|-------|--------|
| **Link integrity** | Spot-check internal / external links on the live URL. |
| **Metadata** | Spot-check title / description / canonical / schema. |
| **Visual fidelity** | Spot-check key pages against frozen design. |
| **a11y heuristic** | Spot-check critical paths. |
| **Performance heuristic** | Spot-check page load (where measurable). |
| **Security smoke** | Confirm no exposed secrets / debug pages. |

Smoke check rules:

- The smoke check is **heuristic** and **does not** replace Frontend QA (S12) or Final Validation (S13).
- Findings open as new QA findings against the delivered artifact and may trigger **post-delivery revisions** ([§11](#11-post-delivery-revision)).
- "Smoke passed" without evidence is forbidden.

Smoke check is **out of scope for v0** if the project does not include a live target. Most factory v0 projects treat smoke as a HITL-driven optional step.

---

## 9. Rollback candidate

A **rollback candidate** is a **prior release baseline** that may be re-selected as the active baseline if the current release fails post-deployment.

| Aspect | Detail |
|--------|--------|
| **Identification** | The most recent prior `approved_release` (or named earlier baseline). |
| **Trigger** | Post-deployment failure (smoke, monitoring, ops report) + HITL decision. |
| **Decision authority** | Ops / client (G7-level authority). |
| **Effect** | The current release moves to `rolled_back`; the prior baseline becomes the active release; downstream consumers (hosting, monitoring) are notified per project runbook. |
| **Recording** | New Approval artifact (decision = `rollback`) referencing prior Approval artifact id and current Approval artifact id. |
| **Forbidden** | Silent rollback; rollback without HITL; rollback that bypasses the prior baseline's freeze (the prior baseline remains immutable). |

Rollback **does not** mutate prior frozen artifacts; it **selects** them as the active baseline. The rolled-back release remains in audit as `rolled_back` for traceability.

A rollback **is not** a deployment automation; it is a HITL-driven re-selection of which release artifact is the active baseline. Whatever external system serves the live site is **out of scope** for the factory's lifecycle.

---

## 10. Archive philosophy

A release cycle is **archived** when:

- the release is **no longer active** (replaced by a new release cycle);
- the project scope is **closed** with HITL closure narrative.

Archive rules:

| Rule | Detail |
|------|--------|
| **Append-only audit** | Archived releases remain in the audit trail with their Approval artifact, Validation artifact, Delivery artifact, manifest, and component artifact references. |
| **Immutability preserved** | Archived artifacts stay `frozen` (or move to `archived` per [artifact-state-model-v0.md](artifact-state-model-v0.md)). |
| **Re-activation** | A new release cycle cannot re-activate an archived release without HITL approval + lineage acknowledgment. |
| **Retention** | Project-specific retention policy; v0 does not mandate a retention window. |

Archive **does not** delete; it closes for the active scope.

---

## 11. Post-delivery revision

A **post-delivery revision** reopens the lifecycle after a release.

| Trigger | Path |
|---------|------|
| Smoke / monitoring finding | New QA finding against the delivered artifact; if blocker → **DELIVERY BLOCKED** + revision request. |
| Customer / stakeholder feedback | New revision request through HITL. |
| Discovered SAFE UNKNOWN gap | Bounded revision under HITL. |
| Security finding | **SECURITY RISK** + emergency revision. |
| Legal / compliance change | **NEED HUMAN APPROVAL** + targeted revision. |

Post-delivery revision rules:

- A post-delivery revision **opens** as a normal revision ([revision-semantics-v0.md](revision-semantics-v0.md)) but starts from a **released baseline**, not a `draft` baseline.
- Freeze breaking on the released baseline **requires HITL**.
- The revision flows through the same stages (revised → QA → Final Validation → G7) but **does not** redo prior stages that are unaffected.
- A post-delivery revision **may** require rollback if the issue is urgent and the revision cannot be completed before the next release window.
- A post-delivery revision **always** produces a **new release cycle** (new Approval artifact at G7).

Forbidden:

- silent in-place edits to the released baseline;
- treating a post-delivery revision as a hotfix without lifecycle anchoring;
- emitting a "post-deploy patch" that bypasses HITL.

---

## 12. Tie to workflow v0

[website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S13–S15 anchors are realized here:

| Workflow stage | Lifecycle anchor |
|----------------|--------------------|
| S13 Final Validation | [§3](#3-pre-delivery-validation). |
| S14 Human Approval | [§4](#4-release-approval). |
| S15 Delivery / Export | [§5](#5-freeze-state) + [§6](#6-export-package) + [§7](#7-deployment-handoff). |
| (Post-delivery) | [§8](#8-post-deployment-smoke), [§9](#9-rollback-candidate), [§11](#11-post-delivery-revision). |

The workflow stages are **shape**; the lifecycle states here are **behavior over time**.

---

## 13. Tie to artifact-types-v0

Per [artifact-types-v0.md](artifact-types-v0.md):

| Artifact class | Delivery lifecycle role |
|----------------|--------------------------|
| **Validation artifact** | Filed at S13; informs G7 decision. |
| **Approval artifact** | Records G7 decision + release tag intent + rollback notes. |
| **Delivery artifact** | The export package; immutable per release cycle. |

Each instance of these artifacts has its own state per [artifact-state-model-v0.md](artifact-state-model-v0.md); release-side state changes flow through this document.

---

## 14. Tie to security and risk

Per [`../../security/approval-gates.md`](../../security/approval-gates.md), [`../../security/threat-model-v0.md`](../../security/threat-model-v0.md), and [`../../governance/risk-register.md`](../../governance/risk-register.md):

- A delivery candidate with an unwaived **SECURITY RISK** is **DELIVERY BLOCKED**.
- A waiver for security findings requires named approver per security policy (often higher authority than ordinary HITL).
- Risk-register rows ([`../../governance/risk-register.md`](../../governance/risk-register.md)) referenced when waivers create new exposure.
- Where MARS-wide security policy is stricter than factory gates, **MARS wins** per [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) §8.

---

## 15. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Auto-deployed after G7." | Deployment automation claim. | Manual handoff to ops / client. |
| "Released without rollback notes." | No safety net. | Rollback notes mandatory in release Approval artifact. |
| "Post-deploy hotfix applied silently." | Skips lifecycle. | Post-delivery revision per [§11](#11-post-delivery-revision). |
| "Delivery candidate assembled from draft artifacts." | Freeze bypassed. | Only frozen artifacts in candidate. |
| "Smoke check 'passed' without evidence." | Evidence-free claim. | Evidence per [§8](#8-post-deployment-smoke). |
| "Rollback executed without HITL." | Approval skipped. | HITL approval recorded for rollback. |
| "Validation 'go' overrides open SECURITY RISK." | Severity tuning. | DELIVERY BLOCKED until cleared. |
| "Release approved 'indefinitely'." | Expiration ignored. | Expiration window recorded per [approval-semantics-v0.md](approval-semantics-v0.md) §8. |

---

## 16. Non-claims

- This document does **not** ship a release manager or deployment pipeline.
- It does **not** assume any external system is integrated with the factory.
- It does **not** define wire formats for export manifests, runbooks, or rollback notes.
- It does **not** claim hosting, CDN, DNS, or CI control.
- It does **not** replace HITL judgment with predictable release behavior.

What it **does** do is define **the release-side lifecycle behavior** of factory output — candidate → validation → approval → freeze → export → handoff → smoke → rollback / archive / post-delivery revision — so factory delivery remains **honest, audit-bearing, and HITL-anchored**.

---

## 17. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial delivery lifecycle semantics (documentation only). |
