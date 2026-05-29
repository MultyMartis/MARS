# Triumph Manipulator — Relationship to ORCA Intelligence Foundation v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — relationship note, not migration plan.

## What Triumph Is (unchanged)

- Active **validated Search-pack** under `ppc/triumph-manipulator/`
- Doctrine, intent tiers, landing blueprints, validation CLI, exporter CLI, full-cycle runs
- Operational entry: [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

Triumph remains the **reference implementation** for Search export + landing continuity — not deprecated by v0 foundation.

## What v0 Foundation Adds

Generalizes patterns Triumph already proves:

| Pattern | Triumph evidence (repo) |
|---------|---------------------------|
| Raw pack intake | `incoming/orca-triumph-raw-pack/` precedent |
| Commander export transport | exporter-cli, full-cycle v1.1 runs |
| Validation before export | validation-cli reports |
| ORCA → Factory handoff | v5 page-01 handoff → `workspaces/triumph-manipulator-landing-v4/` |
| Semantic continuity | Implemented landing matches handoff intent |

v0 docs describe **how any project** can follow the same shape — without forcing Triumph relocation.

## Migration Policy

| Rule | Detail |
|------|--------|
| Auto-migration | **No** — Triumph does not move into `projects/orca/projects/<project-id>/` automatically |
| Canonical project tree | Opt-in when operator charters full intake for Triumph-as-project |
| Triumph JSON / XLSX | **Do not** change as part of Intelligence Foundation integration |
| Tools | validation-cli and exporter-cli **untouched** by v0 architecture docs |

## Reference Case Role

Triumph may serve as:

- Template for future `incoming/orca/<project-id>-raw-pack/` intake
- Example for [orca-factory-bridge-index-v0.md](../../intelligence/orca-factory-bridge-index-v0.md)
- Example for [landing-route-registry-contract-v0.md](../../intelligence/landing-route-registry-contract-v0.md) (when operator creates registry)
- Pilot for [project-md-contract-v0.md](../../projects/project-md-contract-v0.md) if duplicated as `triumph-manipulator-krasnodar`

Until opt-in: use Triumph pack paths in `PROJECT.md` equivalents (pack README, run folders).

## Intelligence Layer Links

| v0 doc | Triumph relevance |
|--------|-------------------|
| [orca-operational-principles-v0.md](../../orca-operational-principles-v0.md) | Layer principles; supplements live review v1 |
| [orca-campaign-mode-architecture-v0.md](../../campaign-modes/orca-campaign-mode-architecture-v0.md) | Triumph = Search mode pack today |
| [approval-gates-contract-v0.md](../../artifacts/approval-gates-contract-v0.md) | Human launch authority applies to Triumph exports |
| [moderation-incident-registry-v0.md](../../moderation/moderation-incident-registry-v0.md) | Optional pack-local log until migrated |

## SAFE UNKNOWN

- Date of opt-in migration to canonical `projects/orca/projects/` tree
- Whether RSYA mode will be added for Triumph
- Client-specific approval records outside repo

## Recommended Next Step (operator)

If unifying under Intelligence Foundation:

1. Create `projects/orca/projects/triumph-manipulator-krasnodar/PROJECT.md` from [project-md-contract-v0.md](../../projects/project-md-contract-v0.md).
2. Add `landing-route-registry.json` for v5 routes.
3. Link existing handoff paths — do not duplicate content without merge review.

## Boundary

Relationship documentation only. No migration automation, no Triumph pack rewrite.
