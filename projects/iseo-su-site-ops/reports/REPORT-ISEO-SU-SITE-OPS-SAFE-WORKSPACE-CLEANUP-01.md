# REPORT — ISEO-SU SITE OPS SAFE WORKSPACE CLEANUP 01

**Task ID:** `ISEO-SU-SITE-OPS-SAFE-WORKSPACE-CLEANUP-01`  
**Date:** 2026-09-04  
**Mode:** Agent / project-scoped only (not general MARS Storage Hygiene)  
**Final status:** COMPLETE — ISEO-SU PROJECT-SCOPED WORKSPACE CLEANUP / SAFE TEMP CONTOURS REMOVED / EVIDENCE + ROLLBACK PRESERVED

---

## 1. Scope

Cleanup limited to:

- Contour: `X:\AI MARS\projects\iseo-su-site-ops\`
- Temp Storage: `X:\AI MARS STORAGE\git-sync-iseo-su-*` (and search for `git-reconcile-iseo-su-*` — **none found**)
- Related worktrees: `X:\AI MARS\worktrees\iseo-su-*`

Explicitly out of scope: other programmes, general Storage hygiene, production site tree, raw audit/evidence, rollback `_wave*` folders, archives.

---

## 2. Safety Model

Every candidate was classified individually before any delete. Deletion allowed only for:

- **A. SAFE_TEMP_SYNC_CLONE** — registered worktree, clean status, HEAD ancestor of `origin/mars/canonical-post-recovery`, unique commits ahead = 0, then removed via `git worktree remove`
- **B. SAFE_EMPTY_RESIDUAL** — empty / incomplete failed clone shells with no unique project state

Never deleted on name match alone (`git-sync-*`, `tmp-*`, etc.).

Retained classes used: **D** unpromoted, **E** rollback, **F** raw audit, **G** archive, **H** foreign, **I** unknown.

---

## 3. Preflight

| Check | Value |
|-------|-------|
| Volume | `X:` label **AI WS** |
| CWD | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD | `0477806f18e8181337af5c7c0a17c641d7f87e80` |
| Remote tip (verified) | `d2759f6aed738936d69db0a5f0637be16d817775` |
| Staged | empty |
| Local vs remote | local **ahead** (unpushed commits; treated as foreign / non-cleanup WIP) |
| Project-owned dirty (pre-existing) | ~168 status lines under `projects/iseo-su-site-ops/` — **not mutated** by cleanup FS deletes |
| Foreign WIP | large unrelated dirty tree — **preserved** |
| Mutations forbidden | no `git reset` / `clean` / `stash` / broad restore / `git add .` / force push |

---

## 4. Candidate Inventory

### Found and classified

| PATH | TYPE | REGISTERED? | BRANCH / HEAD | REMOTE CONTAINS HEAD? | DIRTY | CLASS | SAFE TO DELETE? |
|------|------|-------------|---------------|----------------------|-------|-------|-----------------|
| `...\git-sync-iseo-su-city-height-overlap-pilot-01\repo` | sync clone | YES | `3e9e065a…` | YES (ancestor) | clean | A | YES → deleted |
| `...\git-sync-iseo-su-city-pages-wave-02a-cross-linking\repo` | sync clone | YES | `99dd5f38…` | YES | clean | A | YES → deleted |
| `...\git-sync-iseo-su-niche-pages-wave-04\repo` | sync clone | YES | `61ada673…` | YES | clean | A | YES → deleted |
| `...\git-sync-iseo-su-tech-seo-reaudit-02\repo` | sync clone | YES | `d2759f6a…` | YES (= tip) | clean | A | YES → deleted |
| `...\git-sync-iseo-su-webinar-date-update-01\repo` | sync clone | YES | `adbdbe42…` | YES | clean | A | YES → deleted |
| `...\git-sync-iseo-su-webinar-landing-01\repo` | sync clone | YES | `45fb8d68…` | YES | clean | A | YES → deleted |
| `...\git-sync-iseo-su-webinar-rebuild-01\repo` | sync clone | YES | `98a51fda…` | YES | clean | A | YES → deleted |
| `X:\AI MARS\worktrees\iseo-su-static-sitemap-completeness-sync-01` | worktree | YES | `2f29aae0…` | YES | clean | A | YES → deleted |
| `...\git-sync-iseo-su-form-consent-wave-01\repo` | sync clone | YES | `8426ea81…` | YES | **dirty** untracked `archive-glossary.php` | D | **NO** |
| `...\git-sync-iseo-su-tech-repair-wave-01` | independent `.git` | NO | ancestor HEAD but mass checkout noise | YES (HEAD) | messy | I | **NO** |
| `...\git-sync-iseo-su-city-pages-wave-02` | empty residual | NO | n/a | n/a | empty | B | YES → deleted |
| `...\git-sync-iseo-su-new-seo-height-rollout-01` | empty residual | NO | n/a | n/a | empty shell | B | YES → deleted |
| `...\git-sync-iseo-su-usa-uae-wave-03-wt` | empty residual | NO | n/a | n/a | empty | B | YES → deleted |
| `...\git-sync-iseo-su-usa-uae-wave-03` | incomplete pack | NO | n/a | n/a | 1 file / ~13.7 MB | B | YES → deleted |
| `...\git-sync-iseo-su-usa-uae-wave-03-b` | failed shallow | NO | n/a | n/a | 20 files / ~51.5 MB | B | YES → deleted |

`git-reconcile-iseo-su-*`: **0** directories.

Named waves searched but not present as separate live temps (already gone or never materialised as folders): form-consent-01a, city-pages-wave-02 (empty only), usa-uae (residuals only), etc.

---

## 5. Git / Worktree Verification

For each deleted sync clone:

1. `git status --porcelain` → empty  
2. `git merge-base --is-ancestor HEAD origin/mars/canonical-post-recovery` → true  
3. `git rev-list --count remoteTip..HEAD` → **0**  
4. Removed with `git worktree remove <path>` then parent `git-sync-iseo-su-*` folder removed

Form-consent retained: untracked  
`projects/iseo-su-site-ops/production-source/theme/iseoblog/archive-glossary.php`  
(SHA256 `AE2BCFCB…` class evidence recorded during classification; also untracked on main; **not** in remote tip).

---

## 6. Deleted Paths

### SAFE_EMPTY_RESIDUAL

| ABSOLUTE PATH | SIZE BEFORE | FILES | WHY SAFE | DELETE RESULT |
|---------------|-------------|-------|----------|---------------|
| `X:\AI MARS STORAGE\git-sync-iseo-su-city-pages-wave-02` | 0 | 0 | empty residual | OK |
| `X:\AI MARS STORAGE\git-sync-iseo-su-new-seo-height-rollout-01` | 0 | 0 | empty shell | OK |
| `X:\AI MARS STORAGE\git-sync-iseo-su-usa-uae-wave-03-wt` | 0 | 0 | empty residual | OK |
| `X:\AI MARS STORAGE\git-sync-iseo-su-usa-uae-wave-03` | 13 762 571 | 1 | incomplete pack only | OK |
| `X:\AI MARS STORAGE\git-sync-iseo-su-usa-uae-wave-03-b` | 51 530 564 | 20 | failed shallow clone | OK |

### SAFE_TEMP_SYNC_CLONE (via `git worktree remove`)

| ABSOLUTE PATH | SIZE BEFORE | FILES | HEAD | REMOTE PROOF | DELETE RESULT |
|---------------|-------------|-------|------|--------------|---------------|
| `...\git-sync-iseo-su-city-height-overlap-pilot-01\repo` | 3 290 070 782 | 32 680 | `3e9e065a…` | ancestor; uniq=0 | REMOVED + parent gone |
| `...\git-sync-iseo-su-city-pages-wave-02a-cross-linking\repo` | 3 287 823 612 | 32 645 | `99dd5f38…` | ancestor; uniq=0 | REMOVED + parent gone |
| `...\git-sync-iseo-su-niche-pages-wave-04\repo` | 3 288 277 277 | 32 664 | `61ada673…` | ancestor; uniq=0 | REMOVED + parent gone |
| `...\git-sync-iseo-su-tech-seo-reaudit-02\repo` | 3 331 370 958 | 32 920 | `d2759f6a…` | = remote tip | REMOVED + parent gone |
| `...\git-sync-iseo-su-webinar-date-update-01\repo` | 3 331 072 553 | 32 909 | `adbdbe42…` | ancestor; uniq=0 | REMOVED + parent gone |
| `...\git-sync-iseo-su-webinar-landing-01\repo` | 3 327 347 460 | 32 886 | `45fb8d68…` | ancestor; uniq=0 | REMOVED + parent gone |
| `...\git-sync-iseo-su-webinar-rebuild-01\repo` | 3 331 061 826 | 32 906 | `98a51fda…` | ancestor; uniq=0 | REMOVED + parent gone |
| `X:\AI MARS\worktrees\iseo-su-static-sitemap-completeness-sync-01` | 3 274 532 459 | 31 023 | `2f29aae0…` | ancestor; uniq=0 | REMOVED |

**Paths deleted count:** 13 (5 empty residuals + 8 worktrees/parents).

---

## 7. Retained Paths

| Path | Reason |
|------|--------|
| `X:\AI MARS STORAGE\git-sync-iseo-su-form-consent-wave-01` | D — untracked unique file |
| `X:\AI MARS STORAGE\git-sync-iseo-su-tech-repair-wave-01` | I — unregistered independent clone / ambiguous WIP |
| `X:\AI MARS STORAGE\iseo-su-site-ops\` (entire tree) | F / evidence |
| `...\glossary-db-backups\` | F |
| `...\tech-seo-audit-01\` | F |
| `...\tech-seo-reaudit-02\` + `20260904-163451\` | F raw crawl |
| `X:\AI MARS STORAGE\archives\iseo-su-site-ops-scratch-stabilization-2026-08-20\` | G |
| `X:\AI MARS\local\sites\iseo-su-production\` + all `_wave*` / `_hmac*` / `_high-fix*` folders | E rollback |
| Historical pilot evidence docs under project | historical evidence (Part 10) |
| Foreign worktrees (fp0002, mars-data-layer, iseo-sm, etc.) | H |

Project hygiene: no disposable project file deletions this task (probe `_pilot01-*.txt` left — not proven disposable enough to delete).

---

## 8. Locked Residuals

During docs closeout, `git worktree remove --force` on `X:\AI MARS STORAGE\git-sync-iseo-su-workspace-cleanup-01\repo` briefly left an unregistered empty physical residual (`Permission denied`). Classified `SAFE_RESIDUAL_LOCKED`, then cleared on retry (`rmdir`); parent folder gone. **Final locked residuals: 0.**

---

## 9. Protected Raw / Backup / Evidence

Preserved and verified present after cleanup:

- Storage evidence root `X:\AI MARS STORAGE\iseo-su-site-ops\` (~123 161 907 bytes / 89 files including cleanup scratch logs)
- Archive `...\archives\iseo-su-site-ops-scratch-stabilization-2026-08-20\` (~16 265 784 bytes / 386 files)
- Local production + `_wave*` rollback contours — untouched

---

## 10. Worktree Metadata

| Metric | Value |
|--------|-------|
| ISEO registered worktrees before | 9 (8 deleted + form-consent retained) |
| ISEO registered worktrees after | 1 (`git-sync-iseo-su-form-consent-wave-01`) |
| `.git/worktrees` name `iseo-su-static-sitemap-completeness-sync-01` before | present |
| After | absent |
| `git worktree prune -v --dry-run` | empty (already cleaned by `worktree remove`) |
| `git worktree prune -v` | no-op |
| Active foreign worktrees | unchanged (39 worktrees remain registered overall) |

---

## 11. Disk Usage

| Metric | Bytes | Approx |
|--------|-------|--------|
| ISEO TEMP STORAGE SIZE BEFORE (`git-sync-iseo-su-*`) | 29 845 382 270 | ~27.80 GB |
| ISEO TEMP STORAGE SIZE AFTER | 6 593 064 667 | ~6.14 GB |
| SPACE RECLAIMED | 23 252 317 603 | ~21.66 GB |
| RETAINED RAW/EVIDENCE (`STORAGE\iseo-su-site-ops`) | 123 161 907 | ~0.11 GB |
| RETAINED ARCHIVE (scratch-stabilization) | 16 265 784 | ~0.02 GB |

Retained temp after: form-consent (~3.06 GB) + tech-repair (~3.08 GB).

---

## 12. Post-Cleanup Validation

| Check | Result |
|-------|--------|
| Canonical project path intact | YES |
| Remote tip before cleanup | `d2759f6aed738936d69db0a5f0637be16d817775` |
| Remote tip after docs FF push | `682ae690ebdf1b7b9b6bfe160d5ef0efc97efe42` |
| Form-consent still registered | YES |
| Tech-repair still on disk | YES |
| Evidence / archive / production rollback | YES |
| Active ISEO worktree accidentally removed | NO |
| Pre-existing project WIP / foreign WIP | untouched |

---

## 13. Git Integrity

`git fsck --connectivity-only`: no missing objects / no new integrity errors attributed to cleanup. Only pre-existing dangling blobs/commits/trees (normal for a busy repo). **PASS** for this task’s safety goal.

---

## 14. Foreign WIP Preservation

Main tree dirty state and non-ISEO worktrees were not reset, cleaned, stashed, restored, or force-pushed. **FOREIGN WIP PRESERVED: YES**.

---

## 15. Final Decision

Safe project-scoped temps removed; unpromoted form-consent clone and ambiguous tech-repair clone retained; raw crawl, glossary backups, archives, and local rollback contours preserved.

**FINAL STATUS:**  
COMPLETE — ISEO-SU PROJECT-SCOPED WORKSPACE CLEANUP / SAFE TEMP CONTOURS REMOVED / EVIDENCE + ROLLBACK PRESERVED

---

## Hard check block

```
PROJECT: ISEO-SU-SITE-OPS
CANONICAL PROJECT PATH: X:\AI MARS\projects\iseo-su-site-ops\
CANONICAL REMOTE TIP BEFORE: d2759f6aed738936d69db0a5f0637be16d817775
CANONICAL REMOTE TIP AFTER:  682ae690ebdf1b7b9b6bfe160d5ef0efc97efe42

ISEO CLEANUP CANDIDATES FOUND: 15
SAFE TEMP SYNC CLONES: 8
SAFE EMPTY RESIDUALS: 5
ACTIVE WORKTREES RETAINED: 1 (form-consent)
UNPROMOTED STATE RETAINED: 1 (form-consent dirty)
ROLLBACK CONTOURS RETAINED: YES (local\sites\iseo-su-production\_*)
RAW AUDIT CONTOURS RETAINED: YES (tech-seo-audit-01, tech-seo-reaudit-02\20260904-163451)
ARCHIVES RETAINED: YES
UNKNOWN/UNSAFE RETAINED: 1 (tech-repair-wave-01)

PATHS DELETED: 13
PATHS RETAINED: form-consent + tech-repair + STORAGE\iseo-su-site-ops + archive + local production
LOCKED RESIDUALS: 0

STALE ISEO WORKTREE METADATA BEFORE: 1 (iseo-su-static-sitemap-completeness-sync-01)
STALE ISEO WORKTREE METADATA AFTER: 0

UNPROMOTED PROJECT COMMITS LOST: 0
UNIQUE PROJECT FILES LOST: 0
ROLLBACK DATA LOST: 0
RAW AUDIT DATA LOST: 0
SECRET AUTHORITY LOST: 0

CANONICAL PROJECT COMPLETE: YES
PROJECT-OWNED UNCOMMITTED: PRE-EXISTING UNTOUCHED (~168 lines; cleanup docs committed via sync worktree)
FOREIGN WIP PRESERVED: YES
GIT INTEGRITY: PASS

TEMP STORAGE SIZE BEFORE: 29845382270 (~27.80 GB)
TEMP STORAGE SIZE AFTER:  6593064667 (~6.14 GB)
SPACE RECLAIMED:          23252317603 (~21.66 GB)

REMOTE SYNC: FF push OK — d2759f6a..682ae690 (docs(iseo-su): record safe workspace cleanup); cleanup sync worktree removed (no residual)
```
