# MARS-GIT-WORKTREE-PRUNE-APPLY-01

**Operation:** prune stale Git worktree metadata only  
**Date:** 2026-08-31  
**Repo:** `X:\AI MARS`  
**Evidence:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\MARS-GIT-WORKTREE-PRUNE-APPLY-01\`

## 1. Scope

Bounded Git hygiene: remove stale/orphaned **worktree metadata** under `.git/worktrees/` where checkout paths no longer exist.

Not in scope: Storage cleanup, filesystem directory deletes, ref deletes, `git gc`, production/runtime mutations.

## 2. Operator approval

Approved after `SITE-002-MARS-STORAGE-HYGIENE-STABILITY-AUDIT-01`  
Prior audit verdict: `CLEANUP_CANDIDATES_FOUND_DRY_RUN_ONLY`  
Approved action: run bounded `git worktree prune` for stale metadata only.

## 3. Boundary

| Flag | Value |
|------|-------|
| filesystem_delete_allowed | false |
| production_mutation_allowed | false |
| git_worktree_prune_allowed | true |
| git_gc_allowed | false |
| git_clean_allowed | false |
| ref_delete_allowed | false |

Manifest: `manifests/operation.json` in evidence root.

## 4. Preflight Git state

| Item | Value |
|------|-------|
| Volume | `AI WS` (`X:`) |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `3e1a76c356362479ee1f04495cddb5e5398292cd` |
| origin/mars/canonical-post-recovery | `ef662992ab3146abfcdb0c10e3a025720a597bbb` |
| Ahead/behind | behind by 3, ahead by 0 |
| Staged | 0 |
| Dirty status lines | 1114 (foreign WIP — untouched) |
| Registered worktrees | 109 (19 live / 90 missing on disk) |
| Filtered local refs | 8 |

## 5. Dry-run result

Command: `git worktree prune --dry-run --verbose`

- **90** lines, all: `Removing worktrees/<name>: gitdir file points to non-existent location`
- Checkout still exists for candidates: **0**
- Overlap with live worktree paths: **0**
- Sensitive path keywords (monitor / wpilot / production deployments / MARS-Localhost): **0**

Verdict: `DRY_RUN_SAFE_STALE_METADATA_ONLY`

## 6. Apply result

Command: `git worktree prune --verbose`

- Applied **90** stale metadata removals
- Output saved: `apply/worktree-prune-apply.txt`
- `git gc`: **not run**
- Refs: **not deleted**
- Filesystem project/Storage/runtime directories: **not deleted**

## 7. Post-check

| Metric | After |
|--------|-------|
| Registered worktrees | **20** |
| Missing on disk | **0** |
| Second dry-run lines | **0** |
| Filtered refs | **8 (unchanged)** |
| Dirty status lines | **1114 (unchanged)** |
| HEAD / branch | unchanged |

Remaining live worktrees include primary, `X:\AI MARS\worktrees\*`, selected Storage git-sync checkouts, and `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`.

## 8. Preserved refs / branches

Unchanged filtered heads (8), including:

- `closeout/site002-post-catalog-01` @ `17a6c5c0` (contains prior filter commits `6da95c5d`, `17a6c5c0`)
- `site002/workstation-cleanup-closeout-01`
- `docs/site002-final-knowledge-consolidation`
- `docs/site002-offers-recovery-healthcheck-03`
- `docs/site002-storage-hygiene-stability-audit-01`
- related iseo/mars closeout heads matched by filter

No refs deleted.

## 9. Production mutation count

| Kind | Count |
|------|-------|
| DB writes | 0 |
| FTP writes | 0 |
| deploys | 0 |
| cache clears | 0 |
| imports | 0 |
| baseline refresh | 0 |
| filesystem data deletes | 0 |
| git gc | 0 |
| refs deleted | 0 |
| stale worktree **metadata** pruned | **90** |

## 10. What was not touched

- Dirty primary WIP
- SITE-002 local refs / filter-architecture commits
- `site-002-monitor` runtime checkout (still registered and present)
- Storage evidence / production deployments data trees
- `wpilot-vc-raw-html-p06`
- Branches, stashes, resets, cleans
- Production DB / FTP / deploy / cache / 1C / n8n

## 11. SAFE UNKNOWN / blockers

- Primary HEAD remains **behind origin by 3** commits (`3e1a76c3` vs `ef662992`). Metadata prune did not require sync; optional docs commit/push must use a clean worktree and account for this mismatch.
- Exact historical reason each Storage `git-sync-*` checkout path disappeared is **SAFE UNKNOWN** (out of scope); prune only confirms paths were already missing.

## 12. Final verdict

**`MARS GIT WORKTREE PRUNE COMPLETE — STALE METADATA ONLY`**
