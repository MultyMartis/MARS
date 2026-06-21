# Factory Implementation Observations v1

**Canonical workspace today:** `workspaces/triumph-manipulator-landing-v6/` — see [triumph-workspace-authority-map-v1.md](../../../../triumph-manipulator-landing/triumph-workspace-authority-map-v1.md). Body below describes **historical v4→v5 path** as observed during calibration authoring.

**Bridge doc:** `projects/orca/intelligence/orca-factory-bridge-index-v0.md`  
**Validated precedent cited there:** 5-ton handoff → v4 workspace — **zakaz actually on v5** (superseded by v6 for new work).

## Implementation path (as observed)

```text
incoming/orca-triumph-raw-pack
    → landing-pages/*.md (blueprints)
    → PPC instance JSON
    → workspaces/triumph-manipulator-landing-v4 (broad clone)
    → workspaces/triumph-manipulator-landing-v5 (index baseline / zakaz)
```

## Factory decisions visible in repo

| Decision | Observation |
|----------|-------------|
| v5 workspace for master hot | Index-only scope per baseline audit — PPC partials cloned |
| Reuse v5-page01 trust/footer | Faster consistency; risks copy skew |
| `hero--v5` SCSS scoped to `ppc-*` page types | Good isolation from legacy index |
| Gulp include graph | Many unused v4 partials remain — bundle weight |
| Reports in `workspaces/.../reports/` | Human QA knowledge **not** fed back to ORCA until this calibration layer |

## Calibration → Factory feedback loop (new)

```text
workspaces/.../reports  ──┐
workspaces/.../src      ──┼──► projects/orca/calibration/
ORCA packs/blueprints   ──┘         │
                                    ▼
                          pack template + handoff vNext
```

## Block effectiveness (implementation)

| Block | Implementation quality | Note |
|-------|------------------------|------|
| Hero | High structural investment | SCSS + partial complexity justified |
| Specs | Strong image + dl | Good second screen |
| Tasks | Reuses capability pattern | OK |
| Trust | Shared partial | Verify copy for master hot intent |
| FAQ | Route-specific partial | Good |

## Do not claim

- Factory auto-enforces semantic lock
- CI validates ORCA continuity (validation-cli is PPC export, not LP HTML)

## Next factory input

Handoff should list:

- Exact partial paths per section
- `data-page-type` value
- Accepted overrides with operator initials
- Build command + dist output path
