# FWS-0001 — Specialist Preflight v1

**Case:** FWS-0001  
**Date:** 2026-06-22  
**Specialist:** FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1

---

## Allowed write scope

```text
workspaces/forge-wordpress-synthetic/FWS-0001/FRONTEND/
workspaces/forge-wordpress-synthetic/FWS-0001/WORDPRESS/
workspaces/forge-wordpress-synthetic/FWS-0001/VALIDATION/
workspaces/forge-wordpress-synthetic/FWS-0001/RELEASE/
workspaces/forge-wordpress-synthetic/FWS-0001/TEMP/
```

## Read-only scope

```text
projects/mars-website-factory/subsystems/forge-wordpress/capability/
projects/mars-website-factory/subsystems/forge-wordpress/contracts/
projects/mars-website-factory/subsystems/forge-wordpress/standards/
```

## Forbidden scope

```text
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/
production hosts / credentials
WPilot runtime / plugin
agents/registry.md (AG-WP-001 global registration)
unrelated OCPilot / ORCA / BZPM WIP
```

## Input authority

| Source | Role |
|--------|------|
| `FRONTEND/dist/` | Visual + structural reference (post-build) |
| Architecture artifacts (this folder) | Implementation authority |
| FW-SK-01–14 skills | Procedure authority |
| FW-V-01–07 validators | Gate authority |

## Execution environment

**Profile B** — WordPress Playground CLI disposable runtime; static frontend reference via local HTTP.

## Selected implementation mode

**Mode A** — Custom theme `fws-synthetic` + functionality plugin `fws-synthetic-core` + ACF Free / Settings API fallback.

---

## Preflight gates (completed before WP code)

| Artifact | Status |
|----------|--------|
| WAD | FWS-0001-WORDPRESS-ARCHITECTURE-DECISION-v1.md |
| Content model | FWS-0001-CONTENT-MODEL-v1.md |
| Editable regions | FWS-0001-EDITABLE-REGIONS-MAP-v1.md |
| Template map | FWS-0001-TEMPLATE-MAP-v1.md |
| Block-to-WP map | FWS-0001-BLOCK-TO-WP-MAPPING-v1.md |
| ACF schema | FWS-0001-ACF-SCHEMA-v1.md |
| CPT map | FWS-0001-CPT-TAXONOMY-MAP-v1.md |
| Theme architecture | FWS-0001-THEME-ARCHITECTURE-v1.md |
| Functionality boundary | FWS-0001-FUNCTIONALITY-BOUNDARY-v1.md |
| Plugin register | FWS-0001-PLUGIN-REGISTER-v1.md |
| Implementation spec | FWS-0001-IMPLEMENTATION-SPEC-v1.md |
| Validation plan | FWS-0001-VALIDATION-PLAN-v1.md |

---

*Specialist preflight v1 — FWS-0001 FW-05.*
