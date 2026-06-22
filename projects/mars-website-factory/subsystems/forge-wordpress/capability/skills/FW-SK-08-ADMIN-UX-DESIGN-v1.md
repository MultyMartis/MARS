# FW-SK-08 — Admin UX Design v1

**Skill ID:** FW-SK-08  
**Stage:** FW-04 capability

## Purpose
Plan WordPress admin experience — editor clarity, options pages, field labels, workflows.

## When to use
- After content model and ACF schema draft
- Before admin-facing configuration code

## Prerequisites
- Content model
- ACF schema draft
- FW-S-05 loaded

## Inputs
- Editable regions map
- ACF schema
- CPT map
- Operator/editor persona notes

## Outputs
- Admin UX map (FW-T)
- Options page structure
- Field label and instruction text plan
- Menu organization plan

## Procedure
1. Map editor tasks: edit homepage, edit service, global settings.
2. Design options page tabs/sections if needed.
3. Write human-readable field labels and instructions (RU if project requires).
4. Hide unnecessary WordPress UI noise where safe (document only).
5. Plan featured image and excerpt usage.
6. Define preview/workflow notes for operator.
7. Align field order with visual top-to-bottom on frontend.

## Standards used
- FW-S-05 Admin UX
- FW-T admin UX map

## Allowed tools
- Read artifacts; write admin UX map

## Forbidden actions
- Implementing admin PHP without approved map
- Removing core admin capabilities without operator approval

## Validation
- Every editable region reachable by non-developer editor path
- No developer jargon in labels

## Human gate
Operator review — editor must understand map.

## Stop conditions
- ACF schema missing for field-driven regions

## Report format
```text
# REPORT — Forge WordPress Admin UX Design
## Editor workflows
## Options structure
```
