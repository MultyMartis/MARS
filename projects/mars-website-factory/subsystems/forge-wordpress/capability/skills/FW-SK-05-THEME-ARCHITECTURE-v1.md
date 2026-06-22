# FW-SK-05 — Theme Architecture v1

**Skill ID:** FW-SK-05  
**Stage:** FW-04 capability

## Purpose
Define custom theme scaffold — hierarchy, partials, assets, bootstrap discipline.

## When to use
- After WAD and block mapping
- Before FW-SK-10 implementation

## Prerequisites
- Approved WAD
- Block-to-WP map
- FW-S-03 loaded

## Inputs
- WAD
- Block-to-WP map
- Template map requirements
- Gulp/asset integration model

## Outputs
- Theme architecture document
- Template hierarchy map (FW-T)
- Directory structure plan
- `functions.php` bootstrap outline (plan only)

## Procedure
1. Define theme directory tree (`inc/`, `template-parts/`, `assets/`).
2. Map WordPress template hierarchy to frontend pages.
3. Plan `functions.php` as thin bootstrap — logic in `inc/`.
4. Define enqueue strategy for CSS/JS/fonts.
5. Plan `header.php` / `footer.php` / `front-page.php` etc.
6. Specify template part naming convention.
7. Align with functionality plugin load order.
8. Document responsive/asset build approach.

## Standards used
- FW-S-03 Theme Architecture
- FW-S-07 Coding and Security (planning)
- FW-T template map

## Allowed tools
- Read docs and frontend; write architecture artifact

## Forbidden actions
- Writing production theme files (FW-SK-10)
- Loading business logic in `functions.php` beyond bootstrap

## Validation
- Every mapped page has template assignment
- Bootstrap-only `functions.php` discipline stated

## Human gate
Operator approval before implementation.

## Stop conditions
- WAD not approved
- Block map incomplete

## Report format
```text
# REPORT — Forge WordPress Theme Architecture
## Directory plan
## Template hierarchy
```
