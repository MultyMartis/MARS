# Backup, Evidence, and Cleanup Policy (Pre-Cleanup)

**Status:** POLICY ONLY — **no deletions authorized by this document**  
**Applies to:** FP-0002 Shpigovsky WordPress artifacts on approved roots  
**Next execution:** requires separate destructive charter after Experience Pack Phase 2 review

---

## 1. Artifact classes

| Class | Description | Example (FP-0002) |
|-------|-------------|-------------------|
| Authoritative stable freeze | Named near-production / Stable freeze | `v9-stable-v1-near-production-freeze-20260718-004137` |
| Major accepted milestone freeze | Operator-accepted page-type or audit freeze | E53 admin UX freeze; E58 visual-audit freeze |
| Rollback backup before risky wave | Pre-mutation checkpoint | `v9-06e63-before-stable-v1-closeout-…` |
| Small intermediate backup | Tiny pre-FIX folders | Many `v9-06e5x-fix*-before-*` ~0–10 MB |
| Duplicate backup | Same content superseded by later full freeze | Early full wave backups after Stable exists |
| Evidence screenshot pack | Report evidence trees | `REPORTS/evidence/v9-06e6*` |
| Temporary evidence | HTML dumps, one-off probes | Ad-hoc under evidence/temp |
| Clean Git worktree | Storage git-sync used for push | `git-sync-fp0002-e63-stable-v1-…` |
| Stale worktree | Empty or superseded sync trees | `git-sync-fp0002-e38-e51-…` (0 files) |
| Generated report artifact | Diffs/csv already in Git | Committed evidence OK to keep in repo |
| Current source authority | `WORDPRESS/` in Git project | Never delete as “cleanup” |
| Runtime authority | Local site tree | Not a disposable backup |
| Incoming operator asset | `INCOMING/OPERATOR-ASSETS` | Retain until promoted+verified |
| Obsolete generated asset | Replaced decor/fonts copies | Candidate after verify |
| Demo content | DB posts/options rows | Cleanup via content charter, not file delete |
| Cache/log/temp files | `debug.log`, caches | Low-risk candidates with gates |

---

## 2. Retention rules (defaults)

| Class | Default retention | Min count | Deletion gate | Proof before delete | Reversible? | Inventory required? |
|-------|-------------------|-----------|---------------|---------------------|-------------|---------------------|
| Authoritative Stable freeze | KEEP until superseded Stable v2 **and** production proven | 1 | Explicit operator approve | Hash verify freeze still intact | Restore from freeze only if kept | Yes |
| Pre-Stable closeout backup | KEEP_UNTIL_PRODUCTION or cleanup confirmed | 1 | Operator + doc gate | Stable freeze verified | Yes if Stable exists | Yes |
| Major milestone freeze (E53/E58) | KEEP if historically valuable / style authority | ≥1 of each named | Operator | Path still referenced by docs | Partial | Yes |
| Rollback-critical pre-wave | KEEP until next major freeze supersedes + 1 successful restore drill optional | case-by-case | Operator | Supersession map | Yes if later freeze | Yes |
| Small intermediate backup | DELETE_IN_CLEANUP_PHASE after inventory | 0 required | Doc Phase 2 + Stable verify | Listed in inventory; not sole copy of unique DB | Usually yes | Yes |
| Duplicate full backup | DELETE_IN_CLEANUP_PHASE if byte-covered by later freeze | 0 | Hash/size compare | Covered-by path | Yes if freeze kept | Yes |
| Evidence for accepted baseline | KEEP (in Git or archive) | n/a | Rare | Unique screenshots check | Low | Yes |
| Temporary evidence | DELETE_IN_CLEANUP_PHASE | 0 | Inventory | Not cited by Stable docs | Yes | Yes |
| Clean worktree (verified push) | DELETE_IN_CLEANUP after remote verify | 0 | Remote SHA match | `git ls-remote` proof | Re-clone possible | Yes |
| Stale/empty worktree | DELETE_IN_CLEANUP | 0 | Confirm empty/unused | file count 0 or superseded | Yes | Yes |
| Source / runtime | KEEP forever (not cleanup targets) | n/a | Forbidden | — | — | — |
| Incoming operator assets | KEEP until promoted+hashed | — | Operator | Asset in theme/uploads | Copy may exist | Yes |
| Cache/log/temp | DELETE_IN_CLEANUP | 0 | Runtime smoke after | Size list | Regenerable | Yes |
| Demo content (DB) | KEEP_UNTIL_PRODUCTION cleanup charter | — | Content charter | Backlog doc | DB backup | Yes |

### Must retain (minimum)

- Stable v1 authoritative freeze
- Pre-Stable v1 closeout backup until cleanup confirmed
- E53 accepted admin baseline freeze (historical + UX milestone)
- E58 visual-audit freeze while still cited as style authority / history
- Release documentation (`REPORTS/STABLE-V1/`, freeze markers)
- Rollback-critical backups named in active runbooks
- Operator source assets still referenced
- Evidence supporting accepted Stable baseline (Git-tracked packs)
- Current clean canonical source + runtime (not deleted)

### Deletion candidates (advisory)

- Superseded small per-wave backups (E54–E62 FIX checkpoints)
- Duplicated full copies covered by Stable freeze
- Abandoned screenshots / temp HTML dumps
- Stale local clean worktrees after remote verification
- Generated diffs with no continuing value outside Git
- Old extracted asset copies superseded by theme assets
- Caches and logs
- Temporary test exports under Storage exports if superseded

---

## 3. Deletion gates (all must pass)

1. Experience Pack Phase 2 reviewed by operator  
2. Stable v1 freeze re-verified (path + DB hash)  
3. Candidate on exact inventory with sizes  
4. Ownership unambiguous (FP-0002 only)  
5. Not the sole copy of unique evidence  
6. Not authoritative freeze  
7. Stop conditions in cleanup plan not triggered  

**Forbidden without charter:** recursive delete, `git clean`, MIR/PURGE, deleting freeze roots.

---

## 4. Relationship to inventory / plan

- Inventory: [CLEANUP-CANDIDATE-INVENTORY-PRE-PHASE.md](./CLEANUP-CANDIDATE-INVENTORY-PRE-PHASE.md)  
- Plan: [CLEANUP-PLAN-AFTER-EXPERIENCE-PHASE-02.md](./CLEANUP-PLAN-AFTER-EXPERIENCE-PHASE-02.md)

## 5. Execution results (links only — policy text above unchanged)

- E64 safe cleanup: [`../../../REPORTS/REPORT-FP-0002-V9-06E64-SAFE-CLEANUP.md`](../../../REPORTS/REPORT-FP-0002-V9-06E64-SAFE-CLEANUP.md)
- E65 manual-review cleanup: [`../../../REPORTS/REPORT-FP-0002-V9-06E65-MANUAL-REVIEW-CLEANUP.md`](../../../REPORTS/REPORT-FP-0002-V9-06E65-MANUAL-REVIEW-CLEANUP.md)
- Feedback for Phase 3: [CLEANUP-EXECUTION-FEEDBACK-FOR-PHASE-03.md](./CLEANUP-EXECUTION-FEEDBACK-FOR-PHASE-03.md)
