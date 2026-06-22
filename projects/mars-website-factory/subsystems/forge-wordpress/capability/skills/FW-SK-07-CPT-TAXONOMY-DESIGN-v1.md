# FW-SK-07 — CPT Taxonomy Design v1

**Skill ID:** FW-SK-07  
**Stage:** FW-04 capability

## Purpose
Design custom post types and taxonomies aligned with content model.

## When to use
- When content model requires CPT beyond native pages/posts
- Before registration code in functionality plugin

## Prerequisites
- Approved content model
- WAD

## Inputs
- Content model
- IA / URL structure requirements
- Frontend archive and single templates

## Outputs
- CPT/taxonomy map (FW-T)
- Rewrite slug plan
- Archive/single template assignments

## Procedure
1. List each CPT with singular/plural labels and slug.
2. Define supports: title, editor, thumbnail, etc.
3. Add taxonomies only if justified — avoid taxonomy sprawl.
4. Map archive and single templates in template hierarchy.
5. Plan admin menu position and icon.
6. Document relationship to ACF field groups.
7. Confirm no duplicate of native post types.

## Standards used
- FW-S-01 Content Modeling
- FW-T CPT taxonomy map

## Allowed tools
- Read artifacts; write map document

## Forbidden actions
- Registering CPT in code without approved map
- Creating taxonomies for single-use filters

## Validation
- Each CPT has archive/single strategy
- Slugs unique and URL-safe

## Human gate
Operator approval before registration code.

## Stop conditions
- Content model not approved

## Report format
```text
# REPORT — Forge WordPress CPT Taxonomy Design
## CPT table
## Taxonomies (if any)
```
