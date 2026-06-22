# FW-SK-09 — WordPress Implementation Planning v1

**Skill ID:** FW-SK-09  
**Stage:** FW-04 capability

## Purpose
Consolidate approved artifacts into ordered implementation specification.

## When to use
- After architecture, modeling, and mapping artifacts approved
- **Immediately before** FW-SK-10 code work

## Prerequisites
- Approved WAD, content model, block map, theme architecture
- ACF/CPT/admin UX designs approved or waived with operator record

## Inputs
- All design artifacts listed above
- Validation plan template
- Tool registry for local commands

## Outputs
- Implementation spec (FW-T)
- Ordered task breakdown
- Validation plan (FW-T)
- Risk and dependency notes

## Procedure
1. Gather all approved artifacts — reject stale drafts.
2. Define implementation order per FW-SK-10 required order.
3. List files to create with paths under allowed scope.
4. Attach standards checklist per file type.
5. Define validation checkpoints after each major phase.
6. List dependencies: ACF plugin, local env, build commands.
7. Document rollback approach.
8. Mark human gates in plan timeline.

## Standards used
- FW-T implementation spec
- FW-T validation plan
- FW-S-08 Validation Standard

## Allowed tools
- Read all artifacts; write spec documents

## Forbidden actions
- Writing theme/plugin code
- Starting implementation without spec approval

## Validation
- Spec references every approved artifact by path
- No orphan implementation tasks

## Human gate
**BLOCKING** — no FW-SK-10 without approved implementation spec.

## Stop conditions
- Any prerequisite artifact not approved
- Scope undefined

## Report format
```text
# REPORT — Forge WordPress Implementation Specification
## Implementation order
## File manifest
## Validation checkpoints
## Gate: AWAITING APPROVAL
```
