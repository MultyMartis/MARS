# LEGACY BACKUP VALIDATION v1 — Phase 3F.2

## Backup location

`X:\AI MARS STORAGE\backups\iseo-sales-manager-bot\2026-08-05-clean-ledger-baseline\`

This is the approved bulk-storage canonical root (`X:\AI MARS STORAGE`), not the git-tracked repository — consistent with the project's storage-layer rules.

## Contents observed

| Subfolder/file | Contents | Status |
|---|---|---|
| `git/GIT-BASELINE-v1.md` | Worktree, base commit (`origin/mars/canonical-post-recovery @ 28ebb27d`), branch (`mars/iseo-sm-phase3f2-clean-ledger`), required ancestor commit list | **PRESENT, readable, consistent** with the live repo's `git log`/`git branch` state independently checked in this task |
| `forensic/exec-23273-ops-evgeniy.{brief,raw}.json` | Operational execution forensic dump for the intake run | **PRESENT** — not opened (raw dump may carry lead-level detail; brief/raw distinguished by filename only) |
| `forensic/exec-23320-mops-callback.{brief,raw}.json` | Admin callback execution forensic dump | **PRESENT** — not opened, same reasoning |
| `private/ADMIN.pre-3f2.raw.json`, `OPS.pre-3f2.raw.json`, `SMV2.pre-3f2.raw.json` | Pre-patch full workflow exports for Admin.dev, Operational.dev, Sales-Manager-v2 | **PRESENT** |
| `private/ADMIN.post-callback-patch.raw.json`, `OPS.post-callback-patch.raw.json` | Post-patch workflow exports | **PRESENT** — **not yet covered by `SHA256SUMS.txt`** (see below) |
| `SHA256SUMS.txt` | Checksum manifest | **PRESENT** — 7 entries covering the three pre-patch workflow exports and the four forensic dump files |
| `manifests/`, `sanitized/`, `sheets/` | Planned sanitized-copy / manifest / sheet-snapshot artifacts | **EMPTY** — not yet populated |

## Validation performed

- Confirmed the backup root, all listed subfolders, and `SHA256SUMS.txt` exist and are **readable** (directory listing and checksum-manifest file read succeeded).
- Confirmed `GIT-BASELINE-v1.md`'s recorded branch/base/ancestor commits **match** the live repository's `git branch --show-current` and `git log` output at the time of this evidence pass.
- Did **not** open the raw workflow exports or raw forensic dumps as part of this sanitized evidence pass (avoids incidental PII exposure in this document's authoring trail); their presence and file sizes were confirmed via directory listing only.
- Checksum **values** are intentionally not reproduced here — this file only confirms the manifest **exists** and lists **which filenames** it covers.

## Gaps (honest)

| Gap | Status |
|---|---|
| Post-callback-patch workflow exports not yet checksummed | **PARTIAL** — files present, `SHA256SUMS.txt` predates them |
| `manifests/`, `sanitized/`, `sheets/` not yet populated | **PENDING OPERATOR** / next backup pass — no sanitized CLEAN/RAW sheet snapshot has been taken as part of this backup yet |

## Verdict

`PARTIAL — PRE-PATCH BASELINE AND FORENSIC EVIDENCE VALIDATED; POST-PATCH CHECKSUMS AND SHEET-LEVEL SANITIZED SNAPSHOTS PENDING`

*Related: [LEGACY-ARCHIVE-MAP-v1.md](LEGACY-ARCHIVE-MAP-v1.md).*
