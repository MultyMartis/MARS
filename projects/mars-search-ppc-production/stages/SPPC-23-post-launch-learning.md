# SPPC-23 — Post-Launch Learning

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-23-post-launch-learning.md`

---

## Stage ID

SPPC-23

## Name

Post-Launch Learning

## Purpose

Capture performance signals, search term insights, and semantic feedback loops after launch to inform future cycles without mutating frozen launch artifacts.

## Owning system

Post-Launch Learning

## Participating systems

- MIG
- ORCA
- Operator
- AI PPC Strategist

## Required inputs

- SPPC-22 launch_recorded token
- Launch log with platform IDs
- Performance export schedule
- Intake KPI definitions

## Optional inputs

- Search terms reports
- Conversion data SAFE UNKNOWN handling
- Operator qualitative notes

## Source-of-truth rules

- Post-launch learning pack is SoT for observations after launch — separate version line from pre-launch production artifacts.
- Learning outputs do not retroactively edit SPPC-03–20 committed artifacts.
- New cycle requires charter for reopen from appropriate stage.

## Required processing

- Collect scheduled performance and search term exports.
- Identify tier performance drift, negative gaps, and new query candidates.
- Propose learnings and reopen recommendations — not silent mutation.
- Feed insights to future SPPC-12 pack or operator review.
- Emit learning pack with dated observations.

## Required outputs

- Post-launch learning pack (dated)
- Reopen recommendations with target stage pointers
- KPI tracking sheet vs intake targets

## Prohibited outputs

- Retroactive edit of launch export manifests
- Automatic keyword admission without new SPPC-05 cycle
- Autonomous budget changes in platform

## Validation rules

- Launch log bound.
- Learning pack dated and versioned.
- Reopen recommendations cite target SPPC stage — no vague "fix in export".

## Blocking conditions

- SPPC-22 incomplete
- Learning pack without date

## Completion status

ONGOING — initial pack due per schedule; `learning_active` token after first pack.

## Evidence requirements

- Learning pack path
- Performance export references
- Reopen recommendation log

## Next allowed stages

- SPPC-12 (new cycle)
- SPPC-05 (new queries)
- SPPC-01 (scope change)

## Rollback / reopen behavior

Learning is append-only. Reopen of prior stages follows explicit operator charter — not automatic from learning pack.

## Responsible role

Post-launch analyst; Operator sponsor

## Operator approval required

yes — for reopen recommendations and new cycle charters
