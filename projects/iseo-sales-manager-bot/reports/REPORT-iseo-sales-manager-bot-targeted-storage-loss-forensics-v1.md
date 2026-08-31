# REPORT — i-SEO Sales Manager Bot Targeted Storage Loss Forensics v1

Sanitized project-local companion of  
`X:\AI MARS\governance\audits\ISEO-SALES-MANAGER-BOT-targeted-storage-loss-forensics-2026-08-31.md`

Date: 2026-08-31  
Mode: READ-ONLY forensics (no restore, no Git mutation, no production change)

---

## 1. Final forensic verdict

**`CONFIRMED LOSS — NO RESTORE NEEDED`**

---

## 2. Production/canonical health

| Item | Result |
|------|--------|
| Origin tip (authority) | `13b38305` |
| Production depends on deleted STORAGE-only files? | **NO** → `CURRENT PRODUCTION SOURCE INTACT` |
| Recent critical waves on tip | **ALL present** (impl + REPORT + evidence + reachable commits) |
| Rollback | Historical KEEP degraded; **current-wave** Admin.dev PRE/POST under incoming natural-reminder local **intact** |
| Credentials | Alternate `n8n-api.env` exists under approved incoming (values not read) |

---

## 3. Confirmed reminder-live-accept loss

Contour deleted: `X:\AI MARS STORAGE\git-sync-iseo-sm-reminder-live-accept-20260821`  
HEAD was `76037630` (promoted). DIRTY(2) = **two untracked items only**:

1. `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-reminder-live-final-acceptance-v1.md`  
2. `projects/iseo-sales-manager-bot/evidence/current-stabilization/reminder-live-final-acceptance/`

| Distinction | Result |
|-------------|--------|
| Physical copy lost | **YES** |
| Unique information lost | **YES** for that pack’s text/artifacts only |
| Production/implementation lost | **NO** |
| Superseded later | **YES** (natural worktree pack + tip wave evidence) |

Incoming `reminder-live-accept-20260821-local` has readiness probes only — **not** the named pack.

**Recommendation:** `ACCEPT LOSS — NO RESTORE`

---

## 4. Dirty WIP contours

| Contour | Historical | Classification |
|---------|------------|----------------|
| current-stabilization | DIRTY(12) | `SAFE_SUPERSEDED` (CLEAN forensic promoted; residual interim edits LOW) |
| phase3h101 | DIRTY(5) | `SAFE_SUPERSEDED` / forensic loss of interim natural pack (LOW) |
| phase3f2 | DIRTY(3) | `SAFE_SUPERSEDED` |
| phase3h732 | DIRTY(29) | Extra dumps may be forensic-lost; product `SAFE_SUPERSEDED` |
| phase3h41 | DIRTY(1) | `SAFE_SUPERSEDED` |

Possible-loss contours cleared SAFE for operations: **5/5**. Materially concerning restore targets: **0**.

---

## 5. KEEP sidecars

Four historical KEEP wrappers deleted.  
Credential continuity: **YES** (alternate exists).  
Backup class: `REDUNDANT_BACKUP_LOSS` + `ROLLBACK_REDUNDANCY_DEGRADED` (current PRE/POST remain).

---

## 6. Wrong-phase-rollback

Path: `...\git-sync-iseo-sm-wrong-phase-rollback-20260825`  
HEAD `f7d3ad80` (revert of docs-only `08a9f568`) already on tip; full patch archive in incoming.  
Prior `NEEDS FORENSICS` → **`SAFE_PROMOTED` / `SAFE_SUPERSEDED`**.

---

## 7. Git object survival

| SHA | Survives | Notes |
|-----|----------|-------|
| `9a69ef08` | YES | Same patch-id as promoted `5d08ed07` |
| `5b479f6e` | YES | Refs + tip product coverage |

Unpromoted commit objects lost: **NO**.

---

## 8. Recent promoted-wave continuity

| Wave | Impl | REPORT | Evidence | Commits |
|------|------|--------|----------|---------|
| group-filter + test cleanup | YES | YES | YES | `12327f1d` |
| CLEAN duplicate fix | YES | YES | YES | `a6b3dceb` |
| keyboard duplicate-All | YES | YES | YES | `4daeb3b2` |
| canonical card reconcile | YES | YES | YES | `dc2509d4` / `41596231` |
| natural reminder action-card | YES | YES | YES | `13b38305` lineage |

---

## 9–10. Rollback / credentials

Rollback: degraded for **old** KEEP trees; **current** deploy backups present.  
Credentials: sole-copy loss **not** evidenced.

---

## 11–15. Matrix summary

- Restore recommended: **none**  
- Filesystem undelete justified: **no**  
- Confirmed lost but acceptable: live-final acceptance pack (+ low-value forensic residuals)  
- SAFE despite deletion: promoted clean waves, Git unique tips, wrong-phase (history+incoming), KEEP as sole current sources (not sole)

---

## 16. Project readiness

**Can normal stabilization continue without restore?** **YES**

---

## 17. Safety

restored=0 · recreated=0 · Git mutations=0 · production=0 · Telegram=0 · ACCESS=0 · AI=0

---

## 18. Next action (one)

Profile Curator records **`ACCEPT LOSS — NO RESTORE`** and resumes normal i-SEO Sales Manager Bot stabilization from tip `13b38305` / surviving worktrees.

`FORENSICS COMPLETE — NO RESTORE`
