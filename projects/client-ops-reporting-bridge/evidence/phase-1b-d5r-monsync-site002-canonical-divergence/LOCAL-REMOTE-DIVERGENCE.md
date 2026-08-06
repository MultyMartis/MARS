# LOCAL-REMOTE-DIVERGENCE

## Snapshot (MONSYNC preflight)

| Ref | Full hash | Subject |
|-----|-----------|---------|
| Local `mars/canonical-post-recovery` HEAD | `a6802b1abd78af4128844d868227919a3b17b308` | docs(iseo-su): record glossary launch commit hash in REPORT |
| `origin/mars/canonical-post-recovery` | `dc1fa5c48255efd8819b1947408d82f67bf020ca` | ocpilot: apply SITE-002 electromechanical category image |

Ahead/behind (`origin...HEAD` left-right): **62 behind / 109 ahead**.

## SITE-002 runtime-relevant divergence only

MONSYNC does **not** reconcile the full 62/109 repository divergence.

| Path | Origin tip | Local HEAD | Meaning |
|------|------------|------------|---------|
| `.../monitor-02.py` | `9c0272f6` (baseline 1737) | `f2273b18` (regressive) | Origin GOOD / local MISSING |
| `.../monitor-runner.ps1` | `f699e5cc` (pre-repair) | `a96b7aef` (= `9a48e93b`) | Local GOOD / origin MISSING |
| finish-summary harness | absent on origin | `a125ce31` (= `9a48e93b`) | Local-only repair harness |

## Ancestry facts

| Fact | Result |
|------|--------|
| `9a48e93b` ancestor of local HEAD | YES |
| `9a48e93b` ancestor of origin tip | NO |
| `af5f3fca` ancestor of origin tip | YES |
| `af5f3fca` ancestor of local HEAD | NO |

## MAIN working tree

MAIN `monitor-02.py` WT blob `2de8773c` differs from both committed local and origin. Treated as **foreign WIP**, not source authority.
