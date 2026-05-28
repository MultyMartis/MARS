# ORCA PROJECT.md Contract v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — navigation and status contract per ORCA-managed project.

**Not** a runtime state machine. **Not** auto-synced from platforms. Operator-maintained.

## Required File

```
projects/orca/projects/<project-id>/PROJECT.md
```

One `PROJECT.md` per canonical project root defined in [project-structure-contract-v0.md](project-structure-contract-v0.md).

## Purpose

Single operator-facing index for:

- Project identity and geo
- Active campaign modes
- Layer completion (raw → normalized → artifacts)
- Approval gate positions
- Website Factory handoff state
- Next actions and decision log pointers

## Template Structure

```markdown
# <project name>

## Project identity
- project_id: <slug>
- client / brand: <name>
- industry: <e.g. local equipment rental>
- geo: <city / region>
- primary service: <commercial focus>
- current status: <intake | research | strategy | factory | export | launch-prep | paused>

## Modes
- search: <inactive | draft | approved>
- rsya: <inactive | draft | approved>
- retarget: <inactive | draft | approved>
- brand: <inactive | draft | approved>
- local: <inactive | draft | approved>
- experimental: <inactive | draft | approved>

## Source state
- raw pack status: <not_received | inventoried | distributed>
- normalized intelligence status: <pending | partial | complete>
- evidence status: <ungraded | partial | graded>
- research status: <not_started | in_progress | snapshot_complete>

## Artifact state
- audit: <none | draft | approved>
- keyword pack: <none | draft | approved>
- strategy: <none | draft | approved>
- landing briefs: <none | draft | approved>
- campaign exports: <none | draft | production-ready>

## Approval gates
- approved_for_strategy: <no | yes | SAFE UNKNOWN>
- approved_for_keywords: <no | yes | SAFE UNKNOWN>
- approved_for_factory: <no | yes | SAFE UNKNOWN>
- approved_for_commander_import: <no | yes | SAFE UNKNOWN>
- approved_for_launch: <no | yes | SAFE UNKNOWN>

## Website Factory state
- landing routes: <link to landing-route-registry or list>
- handoff status: <none | draft | approved>
- semantic lock mode: <inactive | MODE 1>
- page implementation state: <not_started | in_progress | qa | approved_for_ads>

## SAFE UNKNOWN
- <list gaps that block decisions>

## Decision log links
- <paths to approvals/, logs/, run summaries>

## Next actions
- [ ] <operator-owned next step>
```

## Field Rules

| Rule | Detail |
|------|--------|
| Status values | Use labels from [orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md) where applicable |
| Gates | Mirror [approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md) — human sets `yes` |
| Modes | One row per mode from [orca-campaign-mode-architecture-v0.md](../campaign-modes/orca-campaign-mode-architecture-v0.md) |
| Factory | Cross-link [orca-factory-bridge-index-v0.md](../intelligence/orca-factory-bridge-index-v0.md) and handoff paths |
| Triumph legacy | Triumph pack may keep its own index until opt-in migration — see [TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md](../ppc/triumph-manipulator/TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md) |

## What PROJECT.md Is Not

- Not live bid or budget data
- Not Yandex.Direct API state
- Not proof that gates passed without human record in `approvals/`
- Not a substitute for artifact files in `strategy/`, `landing-briefs/`, `exports/`

## Update Discipline

- Update after intake distribution, research session, gate sign-off, Factory handoff, or export run.
- AI / Cursor may **propose** diffs; operator **commits** truth by saving the file.
- Stale `PROJECT.md` worse than SAFE UNKNOWN — mark outdated sections explicitly.

## Related Documents

- [project-structure-contract-v0.md](project-structure-contract-v0.md)
- [approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)
- [orca-factory-bridge-index-v0.md](../intelligence/orca-factory-bridge-index-v0.md)
- [project-memory-system-v0.md](../intelligence/project-memory-system-v0.md)

## Boundary

`PROJECT.md` is **navigation and status contract** documentation only. No runtime, no registry engine, no automated gate enforcement.
