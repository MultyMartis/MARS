# Website Factory — Execution Cases Registry v1

**Status:** **operational** (documentation registry — not `project_id` SoT)  
**Date:** 2026-06-03 (MARS Cleanup Wave 1A)  
**Authority:** [registry/project-registry.md](../../registry/project-registry.md) remains SoT for **programs**; this file is SoT for **Factory execution cases** (client delivery workspaces under Factory production lane).

**Evidence:** [logs/cleanup/actions/isbd-registration-repair-v1.md](../../logs/cleanup/actions/isbd-registration-repair-v1.md)

---

## Vocabulary

| Term | Meaning |
|------|---------|
| **Execution case** | Bounded client landing delivery tracked under Website Factory methodology (Gulp workspace, freeze, handoff). |
| **Client delivery project** | Named product/client workspace with frozen content and external integration target (e.g. WordPress). |
| **Reference execution case** | Documentation-first simulated run (artifact chain only — **not** live workspace SoT). |

**Excluded labels for rows below:** Program · System · Initiative · default `project_id` row (unless operator explicitly charters otherwise).

---

## Registered execution cases

| Case id | Classification | Workspace | Factory overview | WPilot follow-on |
|---------|----------------|-----------|------------------|------------------|
| `triumph-manipulator-landing` | Reference execution case #1 (doc simulation) + active client program pack | `workspaces/triumph-manipulator-landing-v6/` (**canonical** — see [triumph-workspace-authority-map-v1.md](../triumph-manipulator-landing/triumph-workspace-authority-map-v1.md)) | [reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md) | SAFE UNKNOWN / external |
| `isbd-care-landing` | **Client delivery execution case #2** | `workspaces/isbd-care-landing/` | [reference-cases/isbd-care-landing/reference-case-overview-v1.md](reference-cases/isbd-care-landing/reference-case-overview-v1.md) | WordPress / The7 / WPBakery (planned) |

---

## Registration rules

1. New cases **append a row** here before canvas/topology references — no silent workspace-only delivery.
2. Do **not** add `project_id` rows for pure execution cases unless operator promotes to long-lived program (discouraged for single-client landings).
3. Cross-link from [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) and [workflow-map.md](workflow-map.md).

---

*Execution cases registry v1 — Wave 1A.*
