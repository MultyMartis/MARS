# ATLAS Registration v1

**Date:** 2026-06-04  
**Lane:** MARS entity registration (documentation only)  
**Upstream:** Phase 1 foundation complete under `projects/atlas/foundation/`  
**Architect decision:** ATLAS = **official MARS entity** with `project_id` `atlas`

---

## Registration posture

| Field | Value |
|-------|-------|
| **Entity** | ATLAS |
| **`project_id`** | `atlas` |
| **Classification** | **Cross-Cutting Registry Infrastructure** |
| **Purpose** | **Business Reality Registry** |
| **Registry `status`** | `planned` |
| **Phase label (registry)** | **FOUNDATION** — Phase 1 complete |
| **Implementation home** | `projects/atlas/foundation/` (normative docs only) |
| **Runtime** | **Not created** (explicit non-goal) |

---

## Foundation evidence (unchanged by this registration)

| Artifact | Role |
|----------|------|
| `ATLAS-REALITY-MODEL-v1.md` | Core reality model |
| `ATLAS-ENTITY-TAXONOMY-v1.md` | MVP entity taxonomy |
| `ATLAS-BOUNDARIES-v1.md` | Inclusions / exclusions |
| `ATLAS-EXPANSION-RULES-v1.md` | Governed expansion rules |

**Not done:** new phases, architecture edits, README/OPERATIONAL-INDEX pack, persistence, APIs, agent cards.

---

## Actions taken

| Surface | Change |
|---------|--------|
| `registry/project-registry.md` | `atlas` row + ATLAS boundaries note |
| `governance/ecosystem-topology-index.md` | ATLAS § — registered cross-cutting registry |
| `docs/visualization/obsidian-canvas/programs.canvas` | ATLAS node + hub edge (via generator regen) |
| `docs/visualization/obsidian-canvas/_generate_pack.py` | `build_programs` + ATLAS |
| `docs/visualization/obsidian-canvas/README.md` | programs.canvas purpose line |

---

## Files changed

- `registry/project-registry.md`
- `governance/ecosystem-topology-index.md`
- `docs/visualization/obsidian-canvas/_generate_pack.py`
- `docs/visualization/obsidian-canvas/programs.canvas` (regenerated)
- `docs/visualization/obsidian-canvas/README.md`
- `logs/atlas/atlas-registration-v1.md` (this file)

**Not changed:** `projects/atlas/foundation/*`, `mars-runtime/`, lifecycle phases, `mars-reality-index-v0.md` (out of scope).

---

*ATLAS registration v1 — documentation only; no runtime; no commit in this task.*
