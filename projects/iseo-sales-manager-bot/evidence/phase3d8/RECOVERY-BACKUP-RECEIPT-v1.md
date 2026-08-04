# RECOVERY BACKUP RECEIPT v1

## Location

`X:\AI MARS STORAGE\backups\iseo-sales-manager-bot\2026-08-05-phase3d8-baseline\`

**Not committed to Git.**

## Contours

| Contour | Contents |
|---------|----------|
| private/ | Raw workflow exports (OPS/Admin/Sales-Manager-v2) — protected |
| sanitized/ | Secret-safe workflow snapshots suitable for evidence |
| manifests/ | Runtime deployment manifest + symbolic secret inventory |
| sheets/ | Workbook tab structure inferred from workflow nodes (no PII cell dump) |
| forensic/ | Button payload structural/execution traces |
| git/ | Canonical tip guidance |
| RECOVERY-README.md | Restore + validation checklist |
| SHA256SUMS.txt | Checksums for package files |

## Workflows packaged

- Operational.dev `xSnXPy8cEHoZw6xG` (post Format+Send repair)
- Admin.dev `wLrLp4WQHm1VJmxz` (post token sync)
- Sales-Manager-v2 `h8I2Tl2yl4uzhUnB` (inactive rollback reference)

## Deliberately excluded

- Secret values, bot tokens, OAuth secrets
- Real emails / phones / names / screenshots
- Full Sheets row dumps with PII
- Foreign MARS WIP

## Verification

- Package built by `phase3d8-local/run-08-build-backup-package.mjs`
- SHA256SUMS.txt generated for included files
- Sanitized snapshots re-derived from post-repair raw exports
- Required top-level contours are present: `private/`, `sanitized/`, `manifests/`, `sheets/`, `forensic/`, `git/`, `RECOVERY-README.md`, `SHA256SUMS.txt`.
- This receipt does **not** claim that full Sheets PII dumps were exported; `sheets/` contains structure inferred from workflows.
- A full restore rehearsal is not claimed by this receipt.
