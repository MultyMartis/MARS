# ISBD Registration Repair v1 — Wave 1A Evidence

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 1A  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb`)  
**Upstream:** [reclassifications/isbd-classification-review-v1.md](../reclassifications/isbd-classification-review-v1.md)

---

## Action summary

| Field | Value |
|-------|-------|
| **Action** | **REGISTER** (Factory execution case — Option A) |
| **Classification** | Website Factory execution case + client delivery project |
| **Explicitly NOT** | Program · System · Initiative · `project_id` row |
| **Case id** | `isbd-care-landing` |

---

## Changes performed

| Surface | Change |
|---------|--------|
| `projects/mars-website-factory/execution-cases-registry-v1.md` | **Created** — execution cases SoT (Triumph + ISBD rows) |
| `projects/mars-website-factory/reference-cases/isbd-care-landing/reference-case-overview-v1.md` | **Created** — case overview |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | **Updated** — Core Run rows: execution cases registry + ISBD |
| `projects/mars-website-factory/workflow-map.md` | **Updated** — client delivery execution case #2 |
| `projects/mars-website-factory/wave1-operational-entity-map-v1.md` | **Updated** — `execution case` entity |
| `governance/ecosystem-topology-index.md` | **Updated** — Factory execution cases cross-link |
| `docs/visualization/obsidian-canvas/website-factory.canvas` | **Updated** — ISBD node (was SAFE UNKNOWN) |
| `docs/visualization/obsidian-canvas/_generate_pack.py` | **Updated** — generator text aligned |
| `docs/visualization/obsidian-canvas/README.md` | **Updated** — canvas description |

**Not changed (deferred):** `registry/project-registry.md` — no `project_id` row per review recommendation.

---

## Resulting state

- ISBD is **traceable** under Website Factory → Execution Cases.
- Canvas and Factory index **no longer contradict** `workspaces/isbd-care-landing/`.

---

## Deferred (Wave 2+)

| ID | Item |
|----|------|
| ISBD-D1 | Nested `.git` in workspace — policy |
| ISBD-D2 | WPilot insertion QA evidence |
| ISBD-D3 | Operator owner / client contract (external) |

---

*ISBD registration repair v1 — executed Wave 1A.*
