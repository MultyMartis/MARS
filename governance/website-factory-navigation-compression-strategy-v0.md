# Website Factory — navigation compression strategy v0

**Status:** **documented** — strategy only (Phase 2).  
**Date:** 2026-05-19.  
**Builds on:** [website-factory-compression-review-v0.md](website-factory-compression-review-v0.md) (Phase 1 signals).  
**Scope:** navigation simplification — **not** Factory rewrite, deletion, or repo restructure.

---

## 1. Audit summary (density)

| Signal | Observation |
|--------|-------------|
| Pack size | ~**258** markdown files under `projects/mars-website-factory/` |
| Entry surfaces | **3** competing maps: README Pack index (~200 lines), [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) (wide table), scattered `*-overview-v0.md` |
| Topology duplication | `system-overview.md` + `layer-map.md` + `workflow-map.md` + `website-factory-workflow-v0.md` — **four** workflow/topology entry points |
| Glossary semantics | Repeated in governance triads (`*-governance.md` + `*-model.md` + `*-taxonomy.md`) × ~30+ concerns |
| Forge repetition | Same concern linked from OPERATIONAL-INDEX **and** README **and** governance row — often **2–3×** per topic |
| Validation overload | `validation-runtime-overview-v0.md`, `validator-execution-model-v0.md`, `validation-escalation-model-v0.md`, execution semantics — **runtime-flavored filenames**, doc-only substance |
| Checklist overgrowth | ~38 Forge `*-checklist.md` + integrated blocks in `qa-checklist.md` |

---

## 2. Duplication classes (navigation-only)

| Class | Examples | Compression lever |
|-------|----------|-------------------|
| **A — Triplicate index** | README Pack index vs OPERATIONAL-INDEX vs concern-specific overviews | **One** operator entry + **one** architect entry |
| **B — Topology twins** | `layer-map` vs `system-overview` vs `workflow-map` | Role tags: **vision** / **layers** / **steps** — cross-link once |
| **C — Governance triads** | `foo-governance` + `foo-model` + `foo-taxonomy` | Index lists **governance only**; model/taxonomy = “deep dive” |
| **D — Forge mirror** | Factory governance + Forge checklist per concern | OPERATIONAL-INDEX: **one row** → governance + “Forge: checklist” sub-bullet |
| **E — Frontend block repeat** | “Semantics” and “Frontend discipline” rows duplicate source-interpretation / token blocks | **Merge** into single Frontend row (Phase 2 editorial) |
| **F — Validation vocabulary** | Multiple “runtime/validator” docs | Banner + link to [safe-unknown-boundary.md](../projects/mars-website-factory/safe-unknown-boundary.md) at top of validation cluster |

---

## 3. Compression strategy (phased, human-gated)

### Tier 0 — Zero file moves (immediate)

| Action | Owner | Outcome |
|--------|-------|---------|
| Adopt **read order** in [mars-reality-index-v0.md](mars-reality-index-v0.md) | All lanes | Fewer random `*-v0` opens |
| Use [operational-modes-model.md](../projects/mars-website-factory/operational-modes-model.md) (**light / standard / battle**) | Operator | Checklist scope without deleting files |
| Prefer **governance-minimalism.md** criteria before new triads | Authors | Stop index growth |

### Tier 1 — OPERATIONAL-INDEX editorial (recommended next)

Split **one file** into two sections (no new files):

```text
## Core run (≤12 rows)
  workflow, runbook, handoff, safe-unknown, agent-map, frontend discipline (merged), reference case

## Extended governance (collapsed)
  Single paragraph + link to README Pack index “governance triads” appendix
```

| Rule | Detail |
|------|--------|
| **Core run** | Only paths needed for first human-supervised Factory run |
| **Extended** | Link-out list; **no** inline duplication of Forge URLs |
| **Dedupe** | One Frontend discipline row; remove repeated token/cadence blocks from “Semantics” row |

### Tier 2 — README Pack index (later)

| Action | Detail |
|--------|--------|
| Add **“Governance triad index”** appendix | Alphabetical links to `*-governance.md` only |
| Mark README index **architect / inventory** | Banner: “Operators start at OPERATIONAL-INDEX Core run” |
| **Do not** shrink README until Tier 1 proves sufficient |

### Tier 3 — Taxonomy & checklist tiers (later)

| Action | Detail |
|--------|--------|
| README appendix: all `*-taxonomy.md` | Onboarding diagnosis only |
| Forge: tag checklists `battle-only` in checklist headers | Triumph V3 charter alignment |
| `qa-checklist.md` remains **integration** surface | Avoid fourth checklist per concern |

### Explicitly deferred

- Merging triad files into single files  
- Deleting governance docs  
- Autonomous compression scripts  
- New ontology / registry for Factory concepts  

---

## 4. Navigation decision tree (operator)

```text
Need to run a site pass?
  → website-factory-workflow-v0.md
  → first-operational-runbook-v0.md
  → OPERATIONAL-INDEX § Core run

Need layer/agent context?
  → system-overview.md OR layer-map.md (pick one; not both first)

Need QA for Triumph battle test?
  → agents/mars-forge/qa-checklist.md + operational-modes battle

Need deep drift diagnosis?
  → README taxonomy appendix OR specific *-taxonomy.md

Need validation semantics?
  → safe-unknown-boundary.md first
  → then execution-semantics-overview-v0.md (not validation-runtime-* first)
```

---

## 5. Success metrics (qualitative)

| Metric | Target |
|--------|--------|
| Operator paths to first run | ≤ **3** clicks from OPERATIONAL-INDEX |
| Duplicate Forge links per concern in index | ≤ **1** |
| New docs without OPERATIONAL-INDEX update | **Discouraged** (entropy rule) |
| README Pack index growth | **Flat** until Tier 2 |

---

## 6. SAFE UNKNOWN

- Which taxonomies are used in live runs — **usage survey** needed  
- Optimal **Core run** row count per site type — **charter-specific**  

---

*Navigation compression strategy — editorial discipline only; complements Phase 1 compression review.*
