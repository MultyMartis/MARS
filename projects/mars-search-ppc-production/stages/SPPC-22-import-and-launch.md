# SPPC-22 — Import and Launch

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-22-import-and-launch.md`

---

## Stage ID

SPPC-22

## Name

Import and Launch

## Purpose

Human operator imports Commander XLSX into Yandex Direct and activates campaigns per bidding branch — platform actions are never agent-automated.

## Owning system

Operator / Platform

## Participating systems

- Commander Export (support)
- QA (post-import smoke)

## Required inputs

- SPPC-21 import_authorized token
- Commander XLSX matching approved checksum
- Platform account access (out of repo)
- Bidding branch manifest from SPPC-18

## Optional inputs

- Import session notes
- Calibration bid sheet for manual branch

## Source-of-truth rules

- Platform campaign IDs after import are SoT for live state — recorded in launch log.
- Repo artifacts remain pre-launch SoT for intended structure until import confirms.
- Launch timestamps and operator identity required in launch log.

## Required processing

- Import XLSX via Commander with checksum verification.
- Calibrate bids if manual branch selected.
- Verify negatives live in platform.
- Activate campaigns per strategy schedule.
- Run post-import smoke checks.
- Record platform IDs and launch status.

## Required outputs

- Launch log with platform campaign IDs
- Post-import smoke report
- Import session record with operator identity

## Prohibited outputs

- Agent-automated platform API launch without operator
- Import of non-approved checksum
- Silent partial launch without log

## Validation rules

- import_authorized token present.
- Checksum matches SPPC-21 approval.
- Smoke checks PASS or waived.
- Manual branch calibration documented if applicable.

## Blocking conditions

- SPPC-21 incomplete
- Checksum mismatch
- Smoke FAIL on critical rules

## Completion status

COMPLETE when campaigns live (or staged per strategy) and `launch_recorded` token issued.

## Evidence requirements

- Launch log path
- Smoke report
- Screenshots or platform export reference (out of repo acceptable)

## Next allowed stages

- SPPC-23

## Rollback / reopen behavior

Pause or rollback in platform is operator action; repo launch log updated with status change — does not auto-regenerate export.

## Responsible role

Operator platform lead

## Operator approval required

yes
