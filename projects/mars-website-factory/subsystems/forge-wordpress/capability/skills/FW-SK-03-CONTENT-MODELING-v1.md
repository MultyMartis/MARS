# FW-SK-03 — Content Modeling v1

**Skill ID:** FW-SK-03  
**Stage:** FW-04 capability

## Purpose
Define WordPress content model — types, relationships, editable regions, and IA alignment.

## When to use
- After approved WAD
- Before ACF, CPT, admin UX, or implementation spec

## Prerequisites
- Approved WAD
- Content evidence from client/operator
- Frontend page inventory

## Inputs
- WAD
- Frontend page list and sections
- Client content brief
- Editable region candidates from frontend

## Outputs
- Content model document (FW-T)
- Editable regions map (draft)
- CPT/taxonomy requirements list

## Procedure
1. Map each frontend page type to WordPress object (page, CPT archive, single).
2. Identify global vs per-page content (options vs fields).
3. List repeatable vs static regions.
4. Define minimum viable content types for pilot scope.
5. Mark operator-owned copy vs system defaults.
6. Cross-check with FW-S-01 content modeling standard.
7. Flag gaps as SAFE UNKNOWN.

## Standards used
- FW-S-01 Content Modeling
- FW-T content model template

## Allowed tools
- Read frontend and docs; write model artifacts

## Forbidden actions
- Registering CPT in code (use FW-SK-07)
- Inventing client copy

## Validation
- Every frontend page type has WordPress mapping or explicit exclusion
- Editable regions identified per block

## Human gate
**BLOCKING** — operator approval before ACF/CPT implementation.

## Stop conditions
- WAD not approved
- No content evidence for required pages

## Report format
```text
# REPORT — Forge WordPress Content Model Design
## Content types
## Editable regions summary
## CPT/taxonomy needs
```
