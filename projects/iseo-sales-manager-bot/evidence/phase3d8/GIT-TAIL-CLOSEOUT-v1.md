# GIT TAIL CLOSEOUT v1

## Canonical

- Branch: `origin/mars/canonical-post-recovery`
- Tip at Phase 3D.8 start: `6351ce6c` (`fix(iseo-sales-manager-bot): stop repeated lead delivery`)
- Ancestry includes `ce06f240` (3D.7), `e78303e2` (3D.6 closeout)
- `phase3d71` worktree/branch already at canonical `6351ce6c`

## Main workspace (`X:\AI MARS`)

- On `mars/canonical-post-recovery` but **diverged** (ahead/behind vs origin) with large foreign WIP
- Staged unrelated `client-ops-reporting-bridge/**` present
- **Not used** for Phase 3D.8 commits (STOP — dirty/staged foreign WIP)

## Worktrees / branches related to iseo-sales-manager-bot

| Location / branch | Tip / note | Disposition |
|-------------------|------------|-------------|
| `incoming/.../worktrees/phase3d71` @ `mars/phase3d71-duplicate-delivery` | `6351ce6c` | Already canonical; retain |
| `incoming/.../worktrees/phase3d7` @ `agent/iseo-phase3d7-delivery` | Historical Phase 3D.7 tip | Retain |
| `git-sync-iseo-sm-phase3d61-closeout-*` | 3D.6 closeout | Historical; retain |
| Many `worktrees/iseo-sm-phase3b*` / `phase3c*` / `phase3d*` | Older phase tips | Retained; not deleted |
| `git-sync-iseo-sm-phase3d8-*` | This phase clean worktree | Active integration path |

## Integration policy this phase

- Clean worktree created from origin tip `6351ce6c`: `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3d8-20260805-032341\repo`
- Scope allowlist: `projects/iseo-sales-manager-bot/**` only
- No force push; no main-workspace reset/clean/stash
- Temporary branches/worktrees not deleted (not proven obsolete-and-safe)
- Phase 3D.8 commit/push operations used the isolated worktree, not the dirty main workspace.
- Push was non-force; at final validation clean-worktree HEAD equalled canonical origin.

## Intentionally retained

- All historical iseo-sm worktrees and private `phase3d*-local` tooling under Storage
- Private backups / operator telegram JSON (never staged)
