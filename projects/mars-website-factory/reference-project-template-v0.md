# Operational template — Reference project structure (v0)

**Status:** **documentation-only** reusable shell. **Not** a project database, **not** persisted state, **not** an orchestration daemon.

**Normative references:** [reference-project-model-v0.md](reference-project-model-v0.md), [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md), [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md), [reference-delivery-package-v0.md](reference-delivery-package-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md).

---

## 1. Project identity (fill-in)

| Field | Value / SAFE UNKNOWN |
|-------|----------------------|
| `project_id` | |
| `project_type` (reference / production / sandbox / migration / demo) | |
| Site type (`site_type_id` per [site-type-registry-v0.md](site-type-registry-v0.md)) | |
| Owner lane (per [operator-lane-model-v0.md](operator-lane-model-v0.md)) | |

---

## 2. Canonical phases (target chain)

Align stage names with [website-factory-workflow-v0.md](website-factory-workflow-v0.md) and operational sequence [reference-run-sequence-v0.md](reference-run-sequence-v0.md) where applicable.

1. **Intake** — business facts, constraints, SAFE UNKNOWN inventory.
2. **Classification** — site type, forbidden patterns, hybrid rationale.
3. **Strategy** — positioning, commercial hierarchy, trust posture.
4. **Information architecture** — page/section order, mobile scan path.
5. **Page blueprint** — contract fields + [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md).
6. **Blueprint QA** — [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) + project-specific findings.
7. **Design** — [design-handoff-contract-v0.md](design-handoff-contract-v0.md); design direction / visual production artifacts as scoped.
8. **Frontend production** — [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md); [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) (Gulp Frontend Agent alignment per [../../agents/cards/gulp-frontend-agent-v0.md](../../agents/cards/gulp-frontend-agent-v0.md)).
9. **QA** — lanes per [qa-validation-model.md](qa-validation-model.md); payloads per [qa-result-payloads-v0.md](qa-result-payloads-v0.md).
10. **Validation** — semantics per [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) (**not** an automated validator engine).
11. **Delivery readiness** — packages per [reference-delivery-package-v0.md](reference-delivery-package-v0.md); lifecycle per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md).

---

## 3. Artifacts (minimum set)

For each artifact class, record: **path**, **version / supersede id**, **owner lane**, **publication state** (draft → review → approved → frozen per [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md)).

| Stage | Typical artifact | Consumed by |
|-------|------------------|--------------|
| Intake | Intake memo | Strategy, PM |
| Strategy / SEO | Strategy + SEO strategy | IA, blueprint |
| IA | Sitemap / IA doc | Blueprint |
| Blueprint | Page blueprint | Design, frontend handoff |
| Design | Design handoff + direction | Frontend |
| Frontend | Source tree + build notes | QA |
| QA | QA report | Validation, HITL |
| Delivery | Readiness + export / RC narrative | HITL, ops |

**Artifact bus reminder:** movement follows [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md) and [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) — **documentation sense** only.

---

## 4. QA expectations

- Stage × QA obligations: [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md).
- Gate vocabulary: [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).
- Semantic cross-checks when objects drift: [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md).

---

## 5. Checkpoints and approvals

Map project checkpoints to [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md) **C01–C08** (adapt labels if fewer gates).

| Checkpoint | Evidence required | HITL / approver |
|------------|-------------------|-----------------|
| | | |

**Approval semantics:** [approval-semantics-v0.md](approval-semantics-v0.md) — partial, conditional, inheritance, expiration, revocation.

---

## 6. Freeze lifecycle

Per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) and [stage-state-model-v0.md](stage-state-model-v0.md):

- **What is frozen** (object / artifact scope):
- **Freeze breaker events** (revision class — see [revision-cycle-template-v0.md](revision-cycle-template-v0.md)):
- **Inherited freezes** (site → page → section):

---

## 7. Invalidation

Per [dependency-invalidation-v0.md](dependency-invalidation-v0.md) and [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md):

| Upstream change | Downstream invalidated | QA reset scope |
|-----------------|------------------------|----------------|
| | | |

---

## 8. Reporting expectations

- Stage reports per [reporting-standard-v0.md](reporting-standard-v0.md).
- Invalidation / freeze events per [orchestration-signals-v0.md](orchestration-signals-v0.md) tokens (**documentation** routing, not runtime).

---

## 9. Honesty boundary

- No fabricated client sign-off, analytics, SERP positions, or deploy URLs.
- Use **SAFE UNKNOWN** per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) when evidence is absent.

---

*Template v0 — Reference Project Layer alignment; not a state engine.*
