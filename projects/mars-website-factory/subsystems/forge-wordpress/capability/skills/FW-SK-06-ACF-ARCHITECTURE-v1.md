# FW-SK-06 — ACF Architecture v1

**Skill ID:** FW-SK-06  
**Stage:** FW-04 capability

## Purpose
Design ACF field groups, location rules, and Local JSON strategy.

## When to use
- After approved content model
- Before ACF registration code

## Prerequisites
- Approved content model
- Editable regions map
- WAD (ACF confirmed as field layer)

## Inputs
- Content model
- Block-to-WP map
- Editable regions map

## Outputs
- ACF schema document (FW-T)
- Field group list with location rules
- Local JSON path plan

## Procedure
1. Group fields by screen: options page, page template, CPT, taxonomy.
2. Use semantic field names — stable, prefixed if project standard requires.
3. Define field types matching editor UX (FW-S-05 admin UX alignment).
4. Plan repeater/flexible content only where content model requires.
5. Set location rules per template/CPT.
6. Plan `acf-json/` sync directory in theme or plugin per WAD.
7. Avoid duplicating post title/content in ACF unnecessarily.

## Standards used
- FW-S-02 ACF Architecture
- FW-S-05 Admin UX
- FW-T ACF schema template

## Allowed tools
- Read artifacts; write schema doc

## Forbidden actions
- PHP registration without approved schema
- Hardcoded field keys in templates without JSON sync plan

## Validation
- Every editable region has field assignment or explicit exclusion
- Options page fields separated from page fields

## Human gate
Operator approval before FW-SK-10 ACF JSON generation.

## Stop conditions
- Content model not approved
- ACF not in WAD plugin register

## Report format
```text
# REPORT — Forge WordPress ACF Architecture
## Field groups
## Local JSON plan
```
