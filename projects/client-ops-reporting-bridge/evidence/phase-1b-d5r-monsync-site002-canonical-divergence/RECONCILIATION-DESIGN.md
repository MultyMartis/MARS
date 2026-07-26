# RECONCILIATION-DESIGN

## Classification selected

`MONITOR_BASELINE_DELTA_ISOLATABLE`

## Strategy

1. Detached clean git-sync worktree at current local canonical HEAD (`a6802b1a`).
2. Materialize **only** `monitor-02.py` from Git object at `af5f3fca` (blob `9c0272f6`).
3. Leave runner + harness untouched (repair preserved).
4. Add Client Ops MONSYNC phase/evidence docs.
5. Create one scoped commit on local history.
6. Advance `refs/heads/mars/canonical-post-recovery` only if parent still equals tip.
7. Never touch MAIN index; never push; never broad-merge origin.

## Rejected alternatives

| Alternative | Why rejected |
|-------------|--------------|
| `git pull` / merge origin into MAIN | Broad sync; foreign WIP risk; out of charter |
| Cherry-pick entire `af5f3fca` | Imports 9 non-runtime docs/index paths |
| Copy MAIN WT monitor | Foreign WIP; blob ≠ origin authority |
| Copy dirty runtime monitor | Not committed authority source |
| Merge commit with origin solely for monitor | Unnecessary once delta isolatable |

## Method used

`git checkout af5f3fca -- <monitor-02.py>` inside clean worktree → exact origin blob.
