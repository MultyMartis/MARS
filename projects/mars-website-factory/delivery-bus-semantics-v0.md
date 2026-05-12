# MARS Website Factory — Delivery Bus Semantics v0

**Status:** **documentation only** — **delivery-side movement model** for release artifacts: how **candidates**, **packages**, and **authorities** relate. **Not** a CI/CD bus, **not** a deployment orchestrator, **not** artifact runtime transport.

**Version:** v0.

**Related:** [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md), [reference-delivery-package-v0.md](reference-delivery-package-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).

---

## 1. Terms

| Term | Meaning |
|------|---------|
| **Release candidate** | **Narrative label** for a build slice **proposed** for validation — may map to frontend production revision pending S12/S13. **Not** “RC” automation. |
| **Delivery candidate** | Assembled **frozen** baselines + QA + validation per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §2. |
| **Export package** | **Delivery artifact** bundle: static build + docs + manifest + rollback notes. |
| **QA package** | Logical grouping of **QA reports** + waivers referenced by the candidate (not a zip format mandate). |
| **Delivery freeze** | Post-G7 **release_frozen** posture on candidate components. |
| **Delivery invalidation** | Candidate **cannot** proceed to export because upstream invalidation or QA fail broke assembly preconditions. |
| **Release rollback** | HITL re-selection of **rollback candidate** baseline per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §9. |
| **Post-delivery revision** | Lifecycle after release per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §11 — new cycle, **no** silent hotfix. |

---

## 2. Movement model (conceptual)

```text
Lane QA verdicts (S06, S09, S12)
        ↓
Final Validation (S13) — QA package + cross-lane consistency
        ↓
Delivery candidate (assembled, validated, release_pending)
        ↓
G7 Approval artifact — approved_release
        ↓
Export package (immutable for cycle)
        ↓
Deployment handoff (human / project-specific)
        ↓
(post-deploy) smoke → optional post-delivery revision or rollback
```

**No** automatic arrows — each is **HITL- and REPORT-gated** per linked docs.

---

## 3. Authorities

| Role | Authority |
|------|-----------|
| **Delivery authority** | Assembles **candidate** and **export** contents per manifest rules; typically **ops / release lead** — **documentation role**, not a daemon. |
| **Release authority** | **G7** approver — **only** role that moves candidate to `approved_release` / `released`. |
| **Rollback authority** | **G7-level** (ops/client) per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md); **records** rollback Approval artifact. |

---

## 4. Delivery invalidation triggers

- Frontend or final QA **fail** on scope in candidate.  
- **SECURITY RISK** or unwaived **P0**.  
- Discovery that manifest lists **superseded** **artifact_id**.  
- **Semantic invalidation** affecting release claims (e.g. wrong legal region on live-bound pages).

Each trigger **routes** back through [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) invalidation patterns.

---

## 5. Relationship to “artifact bus”

The **delivery bus** is the **subset** of bus semantics applying to **S13–S15** and post-delivery. Same honesty rules: **no queue**, **no async** claims.

---

## 6. Non-claims

- **Not** Kubernetes rollout controller.  
- **Not** blue/green automation.  
- **Not** manifest JSON Schema in-repo unless added later (**SAFE UNKNOWN**).

---

## 7. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial delivery bus semantics (documentation only). |
