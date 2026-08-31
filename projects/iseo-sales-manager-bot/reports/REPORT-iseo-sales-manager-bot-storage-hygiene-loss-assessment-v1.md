# REPORT — i-SEO Sales Manager Bot Storage Hygiene Loss Assessment v1

Sanitized project-local summary of governance audit  
`X:\AI MARS\governance\audits\ISEO-SALES-MANAGER-BOT-storage-hygiene-loss-assessment-2026-08-31.md`

Date: 2026-08-31  
Mode: READ-ONLY assessment (no restore, no Git mutation, no production change)

---

## Final verdict

**`CONFIRMED LOSS`**

Temporary STORAGE `git-sync-iseo-sm-*` contours were removed after MASTER-19G. That wipe included paths previously marked **DIRTY_WIP / DO_NOT_TOUCH** and **PRODUCTION_EVIDENCE_KEEP**. At least one named unique local acceptance pack is gone with no surviving copy. Canonical promoted production fixes remain intact.

---

## Canonical / production

| Item | Result |
|------|--------|
| Current canonical tip | `13b38305` |
| Charter promoted SHAs reachable | **YES** (all listed) |
| Tracked project tree | **1454** files; disk matches tip top-level |
| Production depends only on deleted STORAGE? | **NO** |
| Rollback | **`ROLLBACK_DEGRADED`** — old sidecars gone; newer `incoming\iseo-sales-manager-bot\**` PRE/POST backups remain |
| Credential sole-copy lost? | **NO evidence** (alternate `n8n-api.env` exists under approved incoming private; values not read) |

---

## Contour counts (i-SEO Sales Manager Bot)

| Class | Count (approx) |
|-------|----------------:|
| Deleted i-SEO STORAGE/worktree contours identified | **30** (MASTER-19 set absences + post-19 temps; SMB-1 expected removes included) |
| Surviving related checkouts | **3** (reminder-final-natural worktree; card-status-sync worktree; natural-reminder-action-card STORAGE) |
| Per-path `SAFE_PROMOTED` / `SAFE_REDUNDANT` | **majority of clean/post-19 waves** |
| Per-path `POSSIBLE_*` | **dirty protected + KEEP sidecars + some soak/report gaps** |
| Per-path `CONFIRMED_LOCAL_FILE_LOSS` | **1 contour family** (`reminder-live-accept` untracked pack) |
| Per-path `NEEDS_FORENSICS` | **1** (`wrong-phase-rollback`, low urgency) |

Exact per-path matrix: see governance audit §15.

---

## What is confirmed lost

- `REPORT-iseo-sales-manager-bot-reminder-live-final-acceptance-v1.md` (was untracked only in deleted live-accept contour)  
- `evidence/current-stabilization/reminder-live-final-acceptance/` (same)  
- Disk trees of four KEEP sidecar wrappers (phase3h73 / 731 / 71 / 72)

## What is possible lost

- Uncommitted deltas from deleted DIRTY contours: current-stabilization, phase3h101, phase3f2, phase3h732, phase3h41  
- Extra phase3h732 untracked forensic dumps beyond tracked evidence  

## What is NOT lost (important)

- Canonical Git tip and promoted production commits  
- Unique tip **objects/refs** for card-status (`9a69ef08`) and phase3h7 (`5b479f6e`) — card-status patch functionally identical to `5d08ed07`  
- Reminder-final-natural untracked acceptance pack (**still in its worktree**)  
- Latest natural-reminder action-card STORAGE contour @ tip  
- Recent Admin.dev backups under incoming natural-reminder local  

---

## Restore

**`TARGETED FORENSICS REQUIRED BEFORE RESTORE`**

Do not mass-recreate STORAGE worktrees. Separate operator charter required.

---

## Safety (this task)

restored=0 · recreated worktrees=0 · deleted=0 · Git mutations=0 · production mutations=0 · Telegram=0 · ACCESS=0 · AI=0

---

## Next action (one)

Profile Curator loss verification → authorize or decline a **targeted forensic recovery charter** for the confirmed-missing live-final-acceptance pack (optionally other POSSIBLE dirty residuals).

`READY FOR PROFILE CURATOR LOSS VERIFICATION`
