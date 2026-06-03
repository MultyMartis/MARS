# ORCA Triumph v6 Alignment v1 — Wave 1A Evidence

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 1A  
**Upstream:** [discoveries/triumph-version-map-v1.md](../discoveries/triumph-version-map-v1.md)

---

## Scope rule

- **Corrected:** Live ORCA calibration index paths that claimed **v5** as canonical as-built workspace.
- **Not corrected:** `projects/orca/archive/*`, content-pack as-built metadata, handoff filenames (`*-v5-*`), coordination docs already stating v6 baseline.

---

## Corrections log

| File | Before | After |
|------|--------|-------|
| `projects/orca/OPERATIONAL-INDEX.md` | Canonical case → v5 workspace | → **v6** |
| `projects/orca/calibration/OPERATIONAL-INDEX.md` | Evidence table v5 implementation | → **v6 canonical** + v5 reports historical |
| `projects/orca/calibration/OPERATIONAL-INDEX.md` | Boundary: do not edit v5 | → v6 (+ v5 historical) |
| `projects/orca/calibration/README.md` | Factory workspace v5 | → **v6** |
| `projects/orca/calibration/triumph-manipulator/README.md` | Factory workspace v5 | → **v6** (+ v5 historical) |
| `projects/orca/calibration/triumph-manipulator/calibration-loop-v1/README.md` | As-built paths v5 | → **v6** (QA reports note v5 era) |
| `projects/orca/calibration/triumph-manipulator/current-state/landing-state-summary-v1.md` | As-built v5 | → **v6** |
| `projects/orca/calibration/triumph-manipulator/current-state/current-hero-analysis-v1.md` | Partial paths v5 | → **v6** |
| `projects/orca/calibration/triumph-manipulator/current-state/frontend-structure-analysis-v1.md` | Workspace v5 | → **v6** |
| `projects/orca/calibration/triumph-manipulator/drift-analysis/orca-vs-frontend-drift-v1.md` | As-built v5 | → **v6** |
| `projects/orca/calibration/triumph-manipulator/implementation-findings/frontend-lessons-v1.md` | Source v5 only | → v5 lessons + **v6 canonical** note |
| `projects/orca/calibration/triumph-manipulator/implementation-findings/factory-implementation-observations-v1.md` | (implicit v5 path) | Header: **v6 canonical**; body = historical observation |

---

## Intentionally unchanged (safe-unknown / historical)

| Path | Reason |
|------|--------|
| `projects/orca/archive/stable-orca-after-triumph-battle-v1/**` | Frozen archive snapshot |
| `projects/orca/content-packs/examples/*` v5 paths | As-built pack metadata |
| `projects/orca/ppc/triumph-manipulator/handoff/*v5*` | Artifact filenames |
| `projects/orca/coordination/README.md` | Already lists v6 canonical |

---

*ORCA Triumph v6 alignment v1 — executed Wave 1A.*
