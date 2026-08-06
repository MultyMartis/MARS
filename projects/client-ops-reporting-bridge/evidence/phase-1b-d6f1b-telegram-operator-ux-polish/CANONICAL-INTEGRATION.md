# Canonical Integration

| Item | Value |
|------|-------|
| Canonical remote tip before | `380cebd7ccc27e1d914daa55e2ab63317c647c09` |
| D6F1A source commit | `e5f34b8e76b5dd4740426d1cb0c736f173c46e3c` |
| D6F1B content commit | `2853b14f1adf412a17b69e37912e88e2203f9613` |
| Ancestry merge commit (final tip) | `edee6fec71c21e10023f0365db979decb059bb9f` |
| Canonical remote tip after | `edee6fec71c21e10023f0365db979decb059bb9f` |
| Branch pushed | `origin/mars/canonical-post-recovery` |

## Why Client Ops ancestry was missing

`origin/mars/canonical-post-recovery` had diverged onto unrelated iSEO sales-manager history and contained **0** `projects/client-ops-reporting-bridge/` paths. D6F1A lived on side branch `d6f1a-from-2145935c-20260806T182255` based on Client Ops-bearing history.

## Integration method

1. Clean worktree from `origin/mars/canonical-post-recovery`
2. Scoped `git checkout e5f34b8e -- projects/client-ops-reporting-bridge/`
3. Apply D6F1B UX formatter / runners / evidence
4. Commit content (`2853b14f`)
5. `git merge -s ours e5f34b8e` so D6F1A is a true ancestor without rewriting validated tree
6. Push to `origin/mars/canonical-post-recovery`

## Ancestry proof

- `git merge-base --is-ancestor e5f34b8e origin/mars/canonical-post-recovery` → 0
- `git merge-base --is-ancestor edee6fec origin/mars/canonical-post-recovery` → 0

## Conflicts

None (path checkout + ours merge). Unrelated canonical files preserved.

## MAIN / foreign WIP

Untouched (work performed only in `X:\AI MARS STORAGE\git-sync-d6f1b-20260806T185515\repo`).

Token: `D6F1B_CANONICAL_BRANCH_INTEGRATION_COMPLETE`
