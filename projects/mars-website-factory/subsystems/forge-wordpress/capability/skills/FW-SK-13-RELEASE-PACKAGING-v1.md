# FW-SK-13 — Release Packaging v1

**Skill ID:** FW-SK-13  
**Stage:** FW-04 capability

## Purpose
Build release candidate package and manifest from validated implementation.

## When to use
- After validation pass (blockers resolved or waived)
- Before WPilot handoff

## Prerequisites
- FW-SK-11 pass or documented waivers
- FW-V-07 release validator
- Packaging design doc

## Inputs
- Theme and plugin source directories
- Plugin register
- Validation reports
- Exclusion list per git workflow

## Outputs
- Release manifest (FW-T)
- Staged zip or directory package
- Checksum list if required

## Procedure
1. Verify validation evidence attached.
2. Collect theme + functionality plugin only — exclude core, vendor, uploads.
3. Include ACF JSON, README for deploy operator.
4. List third-party plugin dependencies in manifest.
5. Exclude secrets, `.env`, `wp-config` secrets.
6. Run FW-V-07 release checks.
7. Stage under `<project-artifacts>/release/`.
8. Do not deploy — package only.

## Standards used
- Packaging and release design
- FW-T release manifest
- Git workflow exclusions

## Allowed tools
- zip, file copy within scope

## Forbidden actions
- Including database dumps without charter
- Including production credentials
- Auto-tagging git

## Validation
- FW-V-07 PASS
- Manifest matches actual package contents

## Human gate
Operator approves release candidate.

## Stop conditions
- Blocking validation open
- Security validator fail

## Report format
```text
# REPORT — Forge WordPress Release Packaging
## Manifest summary
## Package path
## Exclusions verified
```
