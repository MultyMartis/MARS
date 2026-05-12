# Execution timeline — Triumph Manipulator Landing (v0)

**Nature:** Documented **operational sequence** for a reference run — **not** a Gantt with real dates, **not** automated scheduling.

**Lanes:** Strategy / SEO / UX / Design / Frontend / QA / HITL / PM (per [operator-lane-model-v0.md](../../operator-lane-model-v0.md)).

---

## Phase A — Intake & classification

| Step | Output | Checkpoint |
|------|--------|------------|
| A1 Intake workshop | [business-intake-v0.md](business-intake-v0.md) | **C01** evidence list complete |
| A2 Classify | [site-classification-v0.md](site-classification-v0.md) | **G1** gate review (simulated) |

**Invalidation example:** If business pivots to full **corporate_site**, site type reclassification → **restart** from A2.

---

## Phase B — Strategy & SEO

| Step | Output | Checkpoint |
|------|--------|------------|
| B1 Marketing strategy | [marketing-strategy-v0.md](marketing-strategy-v0.md) | **C02** stakeholder alignment |
| B2 SEO strategy | [seo-strategy-v0.md](seo-strategy-v0.md) | **G2** hypotheses approved (simulated) |

---

## Phase C — IA & blueprint

| Step | Output | Checkpoint |
|------|--------|------------|
| C1 IA | [information-architecture-v0.md](information-architecture-v0.md) | **C03** IA locked for blueprinting |
| C2 Blueprint draft | [page-blueprint-v0.md](page-blueprint-v0.md) | Internal peer review |
| C3 Blueprint QA | [blueprint-qa-v0.md](blueprint-qa-v0.md) | **R07**-class QA pass (per [reference-run-sequence-v0.md](../../reference-run-sequence-v0.md)) |
| C4 G3 | Conditional approval | **G3** PM + tech |

**Invalidation example:** **geo_trust** copy change after G3 → design + frontend marked **stale** until rerun.

---

## Phase D — Design

| Step | Output | Checkpoint |
|------|--------|------------|
| D1 Design handoff | [design-handoff-v0.md](design-handoff-v0.md) | Completeness vs blueprint |
| D2 Design direction | [design-direction-v0.md](design-direction-v0.md) | Creative review |
| D3 Comps | **SAFE UNKNOWN** — not in repo | **G5** intent |

---

## Phase E — Frontend

| Step | Output | Checkpoint |
|------|--------|------------|
| E1 Frontend handoff | [frontend-handoff-v0.md](frontend-handoff-v0.md) | Tech feasibility |
| E2 Production plan | [frontend-production-plan-v0.md](frontend-production-plan-v0.md) | **FE-Q1**… checkpoints |
| E3 Build | **Not executed** | **G6** intent |

---

## Phase F — QA & validation

| Step | Output | Checkpoint |
|------|--------|------------|
| F1 Frontend QA | [frontend-qa-v0.md](frontend-qa-v0.md) | Lane sign-off |
| F2 Aggregate validation | [validation-summary-v0.md](validation-summary-v0.md) | **C08**-class bundle |
| F3 Delivery readiness | [delivery-readiness-v0.md](delivery-readiness-v0.md) | **G7** blocked in this case |

---

## Phase G — HITL pauses

- **Pause 1:** Legal / insurance wording.
- **Pause 2:** Geo + schema.
- **Pause 3:** CRM + form.

---

## QA loops (explicit)

1. Blueprint QA loop: draft → findings → revision → re-QA.
2. Frontend QA loop: build → issues → fix → re-QA (**N/A** without build).

---

*Execution timeline v0 — reference execution only*
