# FW-SK-14 — WPilot Handoff v1

**Skill ID:** FW-SK-14  
**Stage:** FW-04 capability

## Purpose
Prepare WPilot handoff artifact per FW-C-03 — operational boundary, not live deployment.

## When to use
- After release package approved
- WPilot operations are next downstream step

## Prerequisites
- Release manifest complete
- FW-C-03 handoff contract
- Validation evidence bundle

## Inputs
- Release package
- Release manifest
- Plugin register
- Environment requirements doc
- Validation reports including WV6 operator approval

## Outputs
- WPilot handoff document (FW-T)
- Handoff checklist completed
- Deployment notes for WPilot operator (read-only instructions)

## Procedure
1. Load FW-C-03 and WPilot boundary docs.
2. Verify release package matches manifest.
3. Document install steps: theme, plugin, ACF sync, permalinks.
4. List required WP version, PHP version, plugins.
5. Attach validation summary — no false-green.
6. State explicit **non-goals**: Forge does not operate site.
7. Run FW-V-07 handoff section.
8. Submit for handoff reviewer acceptance.

## Standards used
- FW-C-03 Forge WordPress to WPilot Handoff
- FW-T WPilot handoff template
- WPilot operational index (read-only)

## Allowed tools
- Read package; write handoff artifact

## Forbidden actions
- WPilot operational commands
- Production deployment
- Claiming handoff ACCEPTED without reviewer

## Validation
- FW-C-03 mandatory fields complete
- FW-V-07 handoff checks PASS

## Human gate
**BLOCKING** — WPilot reviewer or operator handoff acceptance.

## Stop conditions
- Release not validated
- WV6 operator approval missing
- Contract gap unresolved

## Report format
```text
# REPORT — Forge WordPress WPilot Handoff Preparation
## Handoff checklist
## Reviewer acceptance: PENDING
```
