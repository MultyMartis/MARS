# Cleanup Execution Feedback for Phase 03

**Source waves:** V9-06E64 Safe Cleanup → **V9-06E65 Manual-Review Cleanup**  
**Status:** Feedback only — Phase 3 polish **not** started

## Retention assumptions that were correct

- Four hard-protected freezes were sufficient rollback authority for deleting superseded E54–E62 tiny/full intermediates.
- Empty unregistered `git-sync-fp0002-*` directories were safe low-risk wins.
- Evidence `node_modules` under probe/closeout folders were regenerable and not cited by Experience Pack docs.
- `debug.log` was regenerable under `WP_DEBUG_LOG`; post-cleanup routes showed no PHP noise.
- Pre-E54 mass delete correctly deferred — naming alone is not supersession proof.
- E64 MANUAL_REVIEW gate on e29c was correct; E65 later proved removal only after bundle/patch preservation.

## Riskier than expected (E64) → resolved in E65 where proven

- **`git-sync-fp0002-e29c-e35-…`**: Phase 2 inventory marked DELETE, but live audit found **six unpushed commits** not ancestors of `origin/mars/canonical-post-recovery`. Gate correctly forced MANUAL_REVIEW. **E65:** commits inventoried; final product state superseded by Stable v1; unique history preserved as Git bundle + patches; worktree removed safely.
- Mid-size **E59 / E61** (~280 MB each): ambiguous in E64. **E65:** compact-preserved DB dumps + manifests/scoped/operator-edits, then deleted full trees — E63/Stable remain rollback authority.
- Source `.bak` video: **E65** proved identical copies already inside Stable + E63 freezes → safe source delete after hash match. Comfort pre-split JSON.bak compacted then deleted.

## Actual space reclaimed

**E64:** approximately **10.4 GB** logged OK deletions:

| Class | Approx |
|-------|--------|
| Git worktrees | ~8.29 GB |
| Backups (17 dirs) | ~2.06 GB |
| Evidence node_modules | ~44 MB |
| debug.log | ~3.7 MB |

**E65:** approximately **1.32 GB** additional exact-path reclaim (worktree e29c + E59/E61 + persistence export + source `.bak` + pre-E54 junk). Correctness prioritized over GB KPI in both waves.

## Worktree removal lessons

1. Use `git worktree list` + `git worktree remove` from the registering repo; then remove leftover parent only if under `git-sync-fp0002-*`.
2. Never delete foreign `git-sync-e01` / MetaBOT / OCPilot / SITE-002 trees.
3. Empty dirs may be unregistered — delete only after file-count **0**.
4. `git worktree prune` is safe metadata hygiene after removals.

## Backup naming problems

- Mix of “fullish” (~1 GB), mid (~280 MB), and tiny (&lt;15 MB) under the same `v9-06eNN-before-*` pattern — size class is a better first filter than wave ordinal alone.
- New E64 packs (`v9-06e64-cleanup-documentation-safety-*`, `v9-06e64-post-cleanup-state-*`) increase directory count after cleanup; reports must distinguish hygiene packs from product freezes.

## Evidence-reference problems

- HTML dumps are large and often unreferenced by Experience Pack prose, but may appear in allowlists/commit lists — keep unless reference search is clean.
- Probe folders mix valuable scripts with disposable `node_modules` — delete deps only, keep scripts/`package.json`.

## Future cleanup tooling improvements

- Automated inventory CSV with: ancestry-to-remote, file-count, unique-vs-protected-freeze hash sample, documentation reference hit count.
- Hard stop when `git log origin/..HEAD` is non-empty.
- Separate allowlists by class (worktree / backup / evidence / runtime) with mandatory dry-run artifact.
- Do not estimate reclaimed GB as a success KPI.

## Lessons for Phase 3 documentation polish

- Document the e29c unpushed-branch exception explicitly in operator runbooks — and the E65 resolution pattern (bundle/patches → worktree remove).
- Add a “post-cleanup remaining MANUAL_REVIEW queue” section to the master Experience Pack index (pre-E54 bulk still open after E65).
- Clarify that Stable v1 docs safety snapshots are documentation-only and must never be confused with the authoritative near-production freeze.
- Link E64/E65 cleanup results from Phase 2 inventory without rewriting historical pre-phase measurements.
- Teach **final-state equivalence vs ancestry equivalence** for unreachable commits.
- Prefer Storage `historical-packs/fp-0002/` compact packs over retaining full mid-size backups or sync worktrees.
- Keep preview deploy packages (`fp-0002-shpigovsky-preview`) until production — not the same class as reproducible persistence exports.

## E65 results (pointers)

- Report: `REPORTS/REPORT-FP-0002-V9-06E65-MANUAL-REVIEW-CLEANUP.md`
- Remaining queue: `REPORTS/CLEANUP/E65-REMAINING-MANUAL-REVIEW.txt`
- Historical packs: `X:\AI MARS STORAGE\historical-packs\fp-0002\e29c-e35\` and `…\manual-review-e65-20260718-015731\`
- Approx reclaimed in E65: **~1.32 GB** (exact-path allowlist)
