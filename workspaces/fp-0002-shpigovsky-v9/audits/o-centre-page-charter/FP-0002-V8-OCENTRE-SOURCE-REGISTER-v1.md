# FP-0002 V8 O-Centre Source Register v1

**Date:** 2026-06-29
**Task:** FP-0002 V8 O-Centre page anatomy + reuse charter (read-only)
**HEAD reference:** `7f5d7f23` (branch `mars/canonical-post-recovery`)

| Source | Path/reference | Authority | Contains | Freshness | Use |
|---|---|---|---|---|---|
| Spig_v1.2.fig | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig` | **CANONICAL** | Page frames «О центре» / «О центре - моб»; component instances; text; image refs | Active V8 design authority per operational status | Primary design composition, dimensions, block order cross-check |
| Шпиговский.fig | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Шпиговский.fig` | **HISTORICAL** | Legacy forensic parse (same frame names) | Superseded by Spig_v1.2.fig | Do not use on conflict |
| Figma section audit JSON | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_audit_page_sections_v2.json` | **SUPPORTING** | Desktop/mobile direct-child section frames for «О центре» | Parsed from canonical fig | Block order evidence, section names, dimensions |
| Figma forensic report | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-FIGMA-FORENSIC-TEST-v1.md` | **SUPPORTING** | Frame sizes PG-04 / PG-15; page template table | 2026 ops pack | Desktop/mobile frame confirmation |
| О центре.pdf | `SOURCE-011` in design audit (client intake; path not in V8 tree) | **SUPPORTING** | PG-005 desktop PDF copy/layout | Design-ready per page inventory | Content authority when fig text unreadable |
| О центре - моб.pdf | `SOURCE-012` (390 px width artifact) | **SUPPORTING** | PG-005 mobile PDF | Normalize to 380 px per frontend normalization | Mobile layout cross-check |
| FP-0002 BLOCK Inventory | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md` | **CANONICAL** | BLK-036…038 unique About blocks; PG-005 scroll composition | Ops foundation | Canonical block IDs and reuse classification |
| FP-0002 Page Inventory | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PAGE-INVENTORY-v1.md` | **CANONICAL** | PG-005 status; PDF pairing | Ops foundation | Route, slug, design-ready flag |
| FP-0002 Design Audit | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-DESIGN-AUDIT-v1.md` | **SUPPORTING** | PG-005 block list; CF-006 About subpages conflict | Audit complete | IA conflicts, URL tree |
| V8 operational status | `workspaces/fp-0002-shpigovsky-v8/foundation/FP-0002-V8-OPERATIONAL-STATUS.md` | **CANONICAL** | CF-003–CF-012 complete; O-Centre deferred | 2026-06-29 | Protected components, consolidation state |
| V8 shared include registry | `workspaces/fp-0002-shpigovsky-v8/audits/shared-component-universalization/FP-0002-V8-SHARED-INCLUDE-REGISTRY-v1.md` | **CANONICAL** | Neutral partial paths; CF-015 home-gallery HOLD | Post-consolidation | Reuse targets |
| V8 component family registry | `workspaces/fp-0002-shpigovsky-v8/audits/component-family-audit-v8-bootstrap-01/FP-0002-V8-COMPONENT-FAMILY-REGISTRY-v1.md` | **CANONICAL** | CF families CF-003–CF-012 | Post-consolidation | Structural reuse proof |
| V8 next-page readiness | `workspaces/fp-0002-shpigovsky-v8/audits/final-consolidation-readiness/FP-0002-V8-NEXT-PAGE-READINESS-v1.md` | **SUPPORTING** | Gallery/staff-photo HOLD notes | 2026-06-29 | Charter trigger document |
| V8 home reuse map | `workspaces/fp-0002-shpigovsky-v8/audits/home-style-baseline-01/FP-0002-HOME-COMPONENT-REUSE-MAP-v1.md` | **SUPPORTING** | home-gallery / home-staff-photo forecasts | Home baseline | Gallery/staff similarity baseline |
| V8 URL map | `workspaces/fp-0002-shpigovsky-v8/foundation/FP-0002-V6-URL-MAP.md` | **CANONICAL** | `/o-centre/` production route; subpage slugs | Foundation | Filename and href conventions |
| V7 o-centre-v1.html (rejected) | `workspaces/fp-0002-shpigovsky-v7/src/pages/o-centre-v1.html` | **HISTORICAL** | Rejected WIP composition; partial copy | Not V8 authority | Content hints only; do not copy structure |
| V8 current HTML partials | `workspaces/fp-0002-shpigovsky-v8/src/partials/**` | **CANONICAL** | Production implementation patterns | Operator manual polish + CF-010 | Reuse implementation source |
| Gallery asset provenance | `workspaces/fp-0002-shpigovsky-v8/src/img/content/gallery/GALLERY-ASSET-PROVENANCE.md` | **SUPPORTING** | Home gallery Figma node IDs | Home-only export | Not O-Centre gallery authority |
| Operator manual polish checkpoint | `workspaces/fp-0002-shpigovsky-v8/audits/operator-manual-polish/` | **CANONICAL** | Protected shared block state @ `472be1ab` | Canonical | Protected source boundary |
| CF-010 clinic landscape | commit `7f5d7f23` | **CANONICAL** | Neutral `clinic-landscape` family | Latest HEAD | Optional reuse candidate (not on PG-005 inventory) |

**Limitation:** Spig_v1.2.fig is on disk under operations INCOMING; not opened or modified in this task. Frame/node IDs for «О центре» are taken from existing parse artifacts (`_fig_audit_page_sections_v2.json`, forensic report) — not a fresh MCP Figma read.
