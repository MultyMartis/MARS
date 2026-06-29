# Website Factory — Execution Cases Registry v1

**Status:** **operational** (documentation registry — not `project_id` SoT)  
**Date:** 2026-06-03 (MARS Cleanup Wave 1A) · **Updated:** 2026-06-08 (`bzpm-catalog-redesign` registration)  
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
| `bzpm-catalog-redesign` | **Client delivery execution case #3** — research phase complete (audit consolidation) | **SAFE UNKNOWN** — no Factory workspace registered | [../website-factory/execution-cases/bzpm-catalog-redesign/README.md](../website-factory/execution-cases/bzpm-catalog-redesign/README.md) | Staging `zpm.new-site.space`; production `bzpm.ru` (WEB-ZPM-01); W3 blueprint pending |

### Factory project lane — FP-0002 (not an execution-case row)

| Field | Value |
|-------|-------|
| Factory Project ID | **FP-0002** — Shpigovsky.ru |
| Active workspace | `workspaces/fp-0002-shpigovsky-v8/` |
| Ops status | [PROJECT-STATUS.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md) |
| **Priority visual protocol (ACTIVE)** | [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md) — **read before any FP-0002 frontend task** |
| Visual PASS | OPERATOR ONLY |
| Commit before operator visual approval | PROHIBITED |

---

## Registration rules

1. New cases **append a row** here before canvas/topology references — no silent workspace-only delivery.
2. Do **not** add `project_id` rows for pure execution cases unless operator promotes to long-lived program (discouraged for single-client landings).
3. Cross-link from [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) and [workflow-map.md](workflow-map.md).

---

*Execution cases registry v1 — Wave 1A.*
