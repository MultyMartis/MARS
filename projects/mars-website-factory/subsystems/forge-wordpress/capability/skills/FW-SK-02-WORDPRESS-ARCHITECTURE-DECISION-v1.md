# FW-SK-02 — WordPress Architecture Decision v1

**Skill ID:** FW-SK-02  
**Stage:** FW-04 capability

## Purpose
Produce WordPress Architecture Decision (WAD) — authoritative technical direction before modeling and code.

## When to use
- After successful FW-SK-01 inspection
- Before content model, theme architecture, or implementation

## Prerequisites
- FW-SK-01 PASS or PARTIAL with operator waiver
- Project intake complete
- Implementation mode declared (FW-01 modes)

## Inputs
- Inspection report
- Project intake
- Implementation mode
- Frontend IA summary

## Outputs
- WAD document (FW-T architecture decision template)
- Theme vs functionality plugin boundary statement
- Template hierarchy strategy
- Plugin governance approach
- Validation strategy summary

## Procedure
1. Confirm implementation mode (e.g. classic theme + ACF, hybrid).
2. Decide theme slug and functionality plugin slug.
3. Define what lives in theme vs plugin (FW-S-03, FW-S-04).
4. Choose template hierarchy approach (page templates, CPT templates).
5. State asset integration strategy (enqueue, build pipeline).
6. Define ACF Local JSON location.
7. List approved third-party plugins or "none for MVP".
8. Document validation levels planned (WV0–WV9 mapping).
9. Record decisions with rationale — no silent defaults.

## Standards used
- FW-01 implementation modes
- FW-S-03 Theme Architecture
- FW-S-04 Functionality Plugin
- FW-S-06 Plugin Governance

## Allowed tools
- Read docs, write WAD artifact only

## Forbidden actions
- Code implementation
- Plugin installation
- Production URL references

## Validation
- WAD covers all template sections
- Boundary between theme and plugin explicit

## Human gate
**BLOCKING** — operator approval before content model or implementation.

## Stop conditions
- Inspection not complete
- Implementation mode undeclared
- Design authority conflict

## Report format
```text
# REPORT — Forge WordPress Architecture Decision
## WAD summary
## Key decisions
## Gate: AWAITING APPROVAL | APPROVED
```
