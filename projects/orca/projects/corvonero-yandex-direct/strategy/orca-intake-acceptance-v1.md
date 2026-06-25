# ORCA Intake Acceptance — Корво Неро v1

**Date:** 2026-06-22  
**Session:** `mig-20260622-corv01`  
**Handoff:** `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/handoff/orca-evidence-handoff-v1.json`

---

## Intake state

**ACCEPTED FOR STRATEGIC INTERPRETATION**

Not set: `campaign ready`, `launch ready`, `strategy approved`.

---

## Validation checklist

| Check | Result | Evidence |
|-------|--------|----------|
| MIG groundtruth complete for approved scope | **PASS** | Human Review Gate APPROVED; Research Pack `published` |
| Evidence limitations explicit | **PASS** | Handoff `accepted_limitations`, Research Pack §Key limitations |
| Wordstat and SERP layers separated | **PASS** | Pass A = all Russia semantic; R1 = Novosibirsk mobile; Pass B not required |
| Keyword Registry ≠ final ad semantics | **PASS** | `registry_state: reviewed_for_research_pack`; eligibility flags require ORCA interpretation |
| Research Pack ≠ ad strategy | **PASS** | Boundary statement; ORCA questions only in §12 |
| SAFE UNKNOWN preserved | **PASS** | Handoff, demand_surface, Research Pack §13 |
| Corvonero site intelligence present | **PASS** | `website-corvonero-intelligence.json` grade B |
| Competitor claims not verified as facts | **PASS** | Forbidden assumptions in handoff |
| Operator closed further MIG acquisition | **PASS** | `operator_decisions` in handoff |

---

## Approved evidence layers (summary)

| Layer | Grade | ORCA use |
|-------|-------|----------|
| Wordstat Pass A | B_semantic_discovery | Semantic class map only — **not** regional volume |
| SERP Stage 1/2 | C | Breadth / noise patterns |
| SERP R1 (zpm) | B_partial (7/10) | Regional commercial composition for captured queries |
| Competitors / website / landing | B | Positioning and landing patterns |
| Demand Surface | finalized | Cluster verdicts for segmentation |
| Keyword Registry | reviewed rev 2 | Interpretation map input — **not** export keywords |

---

## Accepted limitations (non-blocking for Stage 1)

- R1: r1q06, r1q07 — CAPTCHA Grade C; composition not inferred from captures
- R1: r1q09 (ТС ПИОТ) — not captured
- Nationwide Wordstat ≠ Novosibirsk demand volume
- No CPC / CPL / conversion history
- Shift Company website timeout — SERP-only

---

## Forbidden at this intake boundary

Per handoff `forbidden_assumptions` — ORCA Stage 1 did **not**:

- Treat Wordstat counts as Novosibirsk forecasts
- Treat registry phrases as final keywords
- Infer campaign structure from MIG
- Mark strategy or launch approved

---

## Outcome

ORCA Stage 1 strategic interpretation **authorized**. Campaign architecture remains **BLOCKED** pending operator model selection and downstream gates.
