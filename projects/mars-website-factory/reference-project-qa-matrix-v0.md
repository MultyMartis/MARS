# MARS Website Factory — Reference Project QA Matrix v0

**Status:** **documentation only** — **stage × QA posture** matrix for runbooks; **not** an executing gate engine.

**Version:** v0.

**Related:** [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-validation-model.md](qa-validation-model.md), [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md).

---

## 1. Matrix (v0 defaults)

**Required QA** — must be satisfied or **explicitly waived** under **waiver authority** (see [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md)).  
**Blocking** — fail closes the stage gate for production unless waiver + scope documented.  
**Optional** — recommended; omission is **SAFE UNKNOWN** risk accepted by PM.  
**HITL** — human review required even if automated checks exist.

| Stage | Required QA | Blocking | Optional | HITL |
|-------|-------------|----------|----------|------|
| **Intake** | Completeness vs intake checklist | Missing goals / audience / constraints | Stakeholder map depth | Sponsor confirms scope_in/out |
| **Strategy** | Consistency vs intake + `site_type_id` | Contradictory hypotheses without resolution | Competitive scan quality | **G2** approval |
| **IA** | Orphan pages, nav depth, URL policy sanity | Cannibalization flags unresolved | Faceted nav edge cases | IA lead + PM for **G3** slice |
| **Blueprint** | [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) categories | Block/registry violations; missing page objectives | UX microcopy polish | **G3** |
| **Design** | Handoff contract compliance | Brand / accessibility **blockers** per charter | Motion specs | **G5** |
| **Frontend** | Build integrity, semantic HTML baseline, critical path assets | Security issues (dependencies, secrets) | Performance budget | **G6** |
| **Delivery** | Export manifest completeness, version pin, rollback notes | Missing release approver | Smoke in prod-like env | **Release** HITL |

**Validator:** may contribute **evidence** in any stage; never replaces **Blocking** / **HITL** columns by itself.

---

## 2. Waiver rules

- Waivers require **waiver authority**, **written scope**, and **expiry** where risk is time-bounded.
- **Waived** items **must** appear in **delivery** notes and **invalidate** “all clear” semantics for unrelated pages unless scope is explicit.
- **Self-waiver** by sole author — **forbidden** for production (same spirit as self-approval).

---

## 3. QA inheritance

- Downstream QA **assumes** upstream QA **passed for declared scope**; scope changes **reset** inherited posture per [dependency-invalidation-v0.md](dependency-invalidation-v0.md).
- **Conditional** upstream QA **propagates** conditions to downstream checklists.

---

## 4. Invalidation resets

| Trigger | Reset behavior |
|---------|----------------|
| Intake / strategy change | Re-run **Intake → Strategy** matrix rows; **IA+** rows **invalidated**. |
| IA / URL graph change | Re-run **IA** + **Blueprint** rows for affected pages; cascade **Design+** as per dependency doc. |
| Blueprint revision | Re-run **Blueprint** row for touched pages; **Design / Frontend / QA** rows for those pages. |
| Design change | **Design** + **Frontend** + **QA** for impacted surfaces. |
| Frontend change | **Frontend** + **QA**; **Delivery** blocked until fresh QA verdict. |

---

## 5. SAFE UNKNOWN handling

When evidence is missing (analytics, legal text, third-party behavior):

- Record **SAFE UNKNOWN** in QA payload; **do not** fabricate pass.
- **Blocking** vs **optional** escalation is **HITL** decision unless policy already classifies the gap.

---

## 6. Scope disambiguation (governance boundary)

**This document (Reference Project QA Matrix v0)** governs **which QA posture applies at each Factory lifecycle stage** (Intake through Delivery) for **reference-project runbooks** — Required / Blocking / Optional / HITL columns. It is **not** a design-to-implementation fidelity checklist.

| Question | Use this doc (v0) | Use instead |
|----------|-------------------|-------------|
| Must Strategy QA block IA if hypotheses contradict intake? | **Yes** — §1 matrix row | — |
| Does hero spacing match Figma within Factory precision law? | **No** | [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) |
| Is foundation demo page ready before Home? | **No** | [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) |
| Is page entity inventory complete before fidelity QA? | **No** | [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) |
| What REPORT shape closes Production PASS? | **No** | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) |

**Naming rule:** **«QA Matrix»** without qualifier in **frontend production** context means [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md). **«Reference Project QA Matrix»** means **this file**.

**Frontend fidelity peer:** [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) — **site-level** stage × lane matrix is **complementary**; do not substitute for DQ domains or Production PASS.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-12 | Initial **Reference Project QA Matrix v0**. |
| v0.1 | 2026-06-13 | §6 scope disambiguation — Foundation Finalization Pack. |
