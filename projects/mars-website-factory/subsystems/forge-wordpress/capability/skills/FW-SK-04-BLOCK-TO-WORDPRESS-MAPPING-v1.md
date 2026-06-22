# FW-SK-04 — Block to WordPress Mapping v1

**Skill ID:** FW-SK-04  
**Stage:** FW-04 capability

## Purpose
Map each approved frontend block/section to WordPress rendering strategy.

## When to use
- After content model draft
- Before theme architecture and implementation spec

## Prerequisites
- Frontend block inventory (FW-SK-01)
- Approved content model
- WAD template strategy

## Inputs
- Block inventory
- Content model
- WAD
- Frontend HTML partial paths

## Outputs
- Block-to-WP mapping document (FW-T)
- Template part naming plan
- ACF field group hints per block

## Procedure
1. List every frontend section with stable ID (from inventory).
2. For each block assign: template part | page template section | reusable component.
3. Map data source: ACF fields | post content | options | CPT loop.
4. Note asset dependencies (CSS/JS) per block.
5. Flag blocks requiring interaction (JS) — defer to implementation spec.
6. Identify shared partials (header, footer, cards).
7. Document any HTML class preservation requirement from approved frontend.

## Standards used
- FW-S-03 Theme Architecture
- FW-T block-to-WP mapping template
- Gulp integration model (asset paths)

## Allowed tools
- Read frontend source; write mapping artifact

## Forbidden actions
- Renaming approved CSS classes without documented deviation
- Creating WordPress blocks (Gutenberg) unless WAD specifies

## Validation
- 100% of in-scope frontend blocks mapped or explicitly deferred
- No orphan blocks

## Human gate
Architect/operator review for complex mappings.

## Stop conditions
- Missing block inventory
- Content model not approved

## Report format
```text
# REPORT — Forge WordPress Block to WP Mapping
## Mapping table summary
## Unmapped / deferred blocks
```
