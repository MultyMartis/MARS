# CURRENT CONTOUR INVENTORY v1 — i-SEO Sales Manager Bot

Date: 2026-08-31  
Authority tip (origin): `13b3830541f421a452b21bf08eea2e5963b1b23c`  
Closeout worktree: `X:\AI MARS STORAGE\git-sync-iseo-sm-final-hygiene-closeout-20260831-170501\repo`

## Disk-present Git / worktree contours (project-owned)

| Exact path | Type | Size (approx MB) | Exists | Git | Clean/dirty | HEAD | Canonical-covered | Sidecars/private | Current purpose | Decision |
|---|---|---:|---|---|---|---|---|---|---|---|
| `X:\AI MARS\worktrees\iseo-smb-card-status-sync` | registered worktree | ~3122 | YES | YES | CLEAN (0/0) | `9a69ef08` | YES (functionally; identical patch-id to promoted `5d08ed07`) | none | Historical card-status-sync tip checkout | `SAFE_CLOSED_REGENERABLE` |
| `X:\AI MARS\worktrees\iseo-smb-reminder-final-natural-01` | registered worktree | ~3125 | YES | YES | DIRTY (0 mod + 2 untracked) | `4af27901` | HEAD lineage partially historical; **untracked acceptance pack local-only** | none | Dirty WIP natural-acceptance stub | `DIRTY_WIP_DO_NOT_TOUCH` |
| `X:\AI MARS STORAGE\git-sync-iseo-sm-natural-reminder-action-card-20260831-141343` (+ `\repo`) | STORAGE git-sync wrapper | ~3133 | YES | YES (nested `\repo`) | CLEAN (0/0) | `13b38305` (= origin tip) | YES | none at wrapper or repo | Active natural-reminder action-card closeout contour | `ACTIVE_KEEP` |
| `X:\AI MARS STORAGE\git-sync-iseo-sm-final-hygiene-closeout-20260831-170501` (+ `\repo`) | STORAGE git-sync wrapper (this wave) | growing | YES | YES | working → clean after push | starts `13b38305` | YES after push | none | Final hygiene Git closeout | `ACTIVE_KEEP` during wave → `SAFE_CLOSED_REGENERABLE` after successful push |

## Incoming STORAGE (project-owned) — summary

Root: `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\`

| Class | Decision | Notes |
|---|---|---|
| `*\backups\*`, PRE/POST workflow JSON, `n8n-api.env` / private | `SECRET_OR_BACKUP_KEEP` | Credentials + rollback |
| Wave `*-local` forensic packs (incl. natural-reminder 20260831, reminder-live-accept probes, group-filter, keyboard, card packs) | `PRODUCTION_EVIDENCE_KEEP` | Current/historical deploy evidence |
| `raw\`, `sanitized\`, `analysis\` | `ARCHIVE_REVIEW_KEEP` / `SECRET_OR_BACKUP_KEEP` | Operator drop / sanitization staging |
| Nested `incoming\...\worktrees\phase3d7|phase3d71` | `ARCHIVE_REVIEW_KEEP` | Registered historical; not touched this wave |

**Incoming exact-path deletion this wave: none.**

## Stale git worktree registrations (disk ABSENT)

Multiple `git worktree list` entries for deleted `git-sync-iseo-sm-*` paths show `prunable` (gitdir points to non-existent location). Disk trees already gone (prior Storage Hygiene). **No global `git worktree prune` this wave.** Documented as non-blocking registry debt.

## Counts (disk-present project Git/STORAGE temp contours)

| Metric | Value |
|---:|---:|
| Remaining i-SEO Git/worktree contours before cleanup | **4** (3 pre-existing + 1 closeout) |
| Incoming KEEP roots (directory count under incoming project) | **~70** (not cleanup candidates) |
| SAFE_UNKNOWN contours | **0** |
