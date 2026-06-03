# HomeGateway Classification Cleanup v1 — Wave 1A Evidence

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 1A  
**project_id:** `homegateway-v4-ai`  
**Upstream:** [reclassifications/homegateway-classification-review-v1.md](../reclassifications/homegateway-classification-review-v1.md)

---

## Target classification (applied)

| Layer | Label |
|-------|-------|
| **Program (registry)** | **`planned`** — PLANNED / DRAFT |
| **Workspace** | **UI Prototype** — `workspaces/homegateway-v4-ai/v1/` |
| **Documentation** | **Operational Documentation Pack** (doc discipline; ≠ product operational) |

**Honesty rule:** No inflation to active product / shippable MVP; no downgrade of doc-pack or prototype existence.

---

## Changes performed

| File | Change |
|------|--------|
| `registry/project-registry.md` | Boundaries § — disambiguate `planned` vs «operational documentation» |
| `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md` | Classification header; Phase 2 exit note; **Workspace (UI prototype)** section |
| `projects/homegateway-v4-ai/README.md` | Program / workspace / documentation status lines |
| `governance/ecosystem-topology-index.md` | HomeGateway operational status prose aligned |

**Kept unchanged:** Registry `status: planned`; maturity map `planned / draft` (per review KEEP).

---

## Inconsistencies resolved

1. **OPERATIONAL prose overload** — clarified in registry + index.
2. **«HTML not started» vs MVP v1** — index now states wireframe docs complete; static HTML in workspace; Phase 4 gate open.

---

## Deferred

| ID | Item |
|----|------|
| HG-D1 | Lifecycle log backfill for 2026-06-02 registry touch |
| HG-D2 | Roadmap Phase 4 gate vs v1 workspace scope alignment |
| HG-D3 | Whether v1 workspace is operator-canonical vs throwaway |

---

*HomeGateway classification cleanup v1 — executed Wave 1A.*
