# Website Factory — Operational Templates Layer v0 (overview)

**Status:** **documentation-only** — reusable **Markdown shells** and **checklist semantics** for human-supervised work in Cursor (or any editor). **Not** a runtime, **not** orchestration, **not** generated code, **not** n8n/Cron/automation.

**Version:** v0.

---

## 1. What operational templates are

**Operational templates** are **normalized patterns** for how a Website Factory **project type** or **review gate** should be **framed**, **scoped**, and **closed out** in documentation: sections to fill, risks to name, QA focus, HITL expectations, and reporting hooks. They **reuse** vocabulary from existing layers without introducing new “engines.”

They are **instructions for humans and prompts**, not machine-executable workflow definitions.

---

## 2. Why they exist

The **reference execution case** ([reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md)) proves an end-to-end **documentation-first** chain. Operational templates **generalize** that shape so new cases can start from **known-good structure** (phases, artifacts, QA, HITL, freeze) instead of ad-hoc prose.

They reduce **contradiction risk** between workflow narrative, semantic rules, artifact bus movement, and validation vocabulary.

---

## 3. How they relate to adjacent layers

| Adjacent layer | Relationship |
|----------------|--------------|
| **[website-factory-workflow-v0.md](website-factory-workflow-v0.md)** (workflow) | Templates **mirror** stage order and handoffs as **human-facing** scaffolds; they do **not** add stages or autonomous routing. |
| **[artifact-bus-overview-v0.md](artifact-bus-overview-v0.md)** (artifact bus) | Templates remind authors **what moves**, **who consumes**, and **what invalidates** downstream; bus semantics remain **documentation-only** (no queue, no event transport). |
| **[execution-semantics-overview-v0.md](execution-semantics-overview-v0.md)** (execution semantics) | Templates encode **freeze**, **revision**, **invalidation**, and **approval inheritance** as **operational reminders**, not state-machine implementations. |
| **Reference runs** ([first-operational-runbook-v0.md](first-operational-runbook-v0.md), [reference-run-sequence-v0.md](reference-run-sequence-v0.md), Triumph case folder) | Templates are **distilled** from reference run semantics; a template is **not** a substitute for reading the runbook when sequencing R01–R15. |
| **[prompt-standards-overview-v0.md](prompt-standards-overview-v0.md)** / [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) | Templates align **prompt boundaries** (minimal / production / HITL / QA / frontend variants) with **what must be true** before closing a gate. |
| **[qa-prompt-rules-v0.md](qa-prompt-rules-v0.md)**, [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) | **[qa-review-template-v0.md](qa-review-template-v0.md)** and related templates inherit **evidence**, **severity**, **waivers**, and **SAFE UNKNOWN** discipline. |
| **[hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)**, [approval-semantics-v0.md](approval-semantics-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md) | **[hitl-review-template-v0.md](hitl-review-template-v0.md)** and delivery templates anchor **human authority** — no fabricated sign-off. |

---

## 4. Explicit non-equivalence

**Templates ≠ runtime automation.**

- There is **no** implied scheduler, queue, daemon, or background worker.
- There is **no** “run this template” button — execution remains **human-supervised** per [`../../governance/execution-model.md`](../../governance/execution-model.md) and [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md).
- Templates **do not** generate JSON Schemas, Task payloads, or CI pipelines unless a **separate** explicit deliverable says so (**SAFE UNKNOWN** for any future wire format).

---

## 5. Index of v0 operational templates

| Template | Purpose |
|----------|---------|
| [reference-project-template-v0.md](reference-project-template-v0.md) | Canonical reusable **project** structure: phases, artifacts, QA, checkpoints, approvals, freeze, invalidation, reporting. |
| [service-landing-template-v0.md](service-landing-template-v0.md) | **Service / commercial landing** pattern (Triumph-shaped); sections, CTA/trust, SEO intent, mobile, blockers, QA focus. |
| [geo-landing-template-v0.md](geo-landing-template-v0.md) | **Geo / local** landing semantics; duplication and cannibalization risks; **no** ranking guarantees. |
| [catalog-project-template-v0.md](catalog-project-template-v0.md) | **Catalog / PLP-scale** project: hierarchy, filters, internal linking, scalable frontend constraints. |
| [ai-visibility-template-v0.md](ai-visibility-template-v0.md) | **Entity authority**, structured trust, citations; **no** guarantee of LLM inclusion or placement. |
| [multi-page-site-template-v0.md](multi-page-site-template-v0.md) | **Site graph**: clusters, navigation, trust inheritance, invalidation propagation ([multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)). |
| [frontend-delivery-template-v0.md](frontend-delivery-template-v0.md) | **Source-first** frontend execution; Gulp-oriented discipline ([frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)), freeze, delivery candidate. |
| [design-review-template-v0.md](design-review-template-v0.md) | Standardized **design review** shell (hierarchy, typography, mobile, CTA rhythm, escalation). |
| [qa-review-template-v0.md](qa-review-template-v0.md) | Unified **QA review** shell (findings, severity, evidence, blockers, waivers, freeze impact). |
| [hitl-review-template-v0.md](hitl-review-template-v0.md) | **HITL** approvals, conditional paths, waivers, freeze — **no** fake signatures. |
| [revision-cycle-template-v0.md](revision-cycle-template-v0.md) | **Revision classes**, bounded vs structural change, QA reset, approval inheritance ([revision-semantics-v0.md](revision-semantics-v0.md)). |
| [delivery-readiness-template-v0.md](delivery-readiness-template-v0.md) | **Readiness gates** and handoff posture ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)); **no** deployment claims. |
| [project-bootstrap-template-v0.md](project-bootstrap-template-v0.md) | How a **new** factory project starts: intake minimums, artifacts, assumptions, escalations. |
| [operator-session-template-v0.md](operator-session-template-v0.md) | **Session** structure: REPORT discipline, checkpoints, git safety, artifact tracking ([reporting-standard-v0.md](reporting-standard-v0.md)). |

---

## 6. SAFE UNKNOWN

- Whether future tooling will **materialize** these templates into forms or databases — **unknown**; v0 remains Markdown-only.
- Exact **per-client** legal/compliance checklists — **unknown** until intake artifacts exist.

---

*Layer version: v0 — aligned with Website Factory workflow, execution semantics, artifact bus, semantic layer, validation runtime model, and reference case #1 (Triumph).*
