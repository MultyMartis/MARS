# REPORT — FP-0002 V9-06E36-E37 SELECTIVE PERSISTENCE

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` (main worktree) |
| HEAD | `af3062646e6696e4fbe67f0ee2c272a7153ba5fe` |
| Upstream relation | ahead 18, behind 17 vs `origin/mars/canonical-post-recovery` |
| Main worktree staged files before | 0 |
| Main worktree WIP count only | ~708 (foreign monorepo WIP ignored) |
| FP-0002 changed/untracked count | ~402 |
| Merge/rebase state | NONE |
| Result | PASS |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e36-e37-persistence-before-20260713-042025` |
| Runtime theme backup/hash | `theme/assets/css/v9-style.css` + `theme-sha256.txt` (631 files) |
| v9-style.css source/runtime hash | SHA256 `F62B294755482F0E381824A891F1625F2A8693E492FE9C2B52B7BC577FC07817` (MATCH) |
| Home snapshot | `snapshots/home.html` |
| Section extracts | `section-home-recovery-life.html`, `section-home-rehabilitation-program.html` |
| DB dump | skipped with reason: CSS-only persistence |
| Result | PASS |

## 3. Runtime accepted-state evidence

| Evidence | Path | Rows/items | Result |
|---|---|---:|---|
| Route smoke | `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-persistence\v9-06e36-e37-20260713-042025\route-smoke.csv` | 7/7 | PASS |
| Mobile evidence | `…/home-mobile-evidence.md` + `mobile-metrics.json` + screenshots 360/390/430 | 3 viewports | PASS |
| Accepted-state manifest | `…/accepted-state-manifest.md` | 1 | PASS |

## 4. Source authority audit

| Class | Count | Notes |
|---|---:|---|
| Include candidates | 6 | CSS + E36/E37 reports + persistence report + PROJECT-STATUS + SOURCE-AUTHORITY |
| Excluded backup/runtime files | many | Localhost backups, STORAGE dumps, `_probe/node_modules`, DB skipped |
| Foreign files ignored | ~306+ | MetaBOT / OCPilot / other MARS WIP outside FP-0002 allowlist |
| Large/binary files reviewed | yes | Screenshots only in STORAGE export (not committed) |
| Secrets detected | 0 | No `.env` / `wp-config` / credentials |

## 5. Included files

| File | Status | Reason |
|---|---|---|
| `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css` | included | E36+E37 CSS-only (+72 vs prior tip) |
| `REPORTS/REPORT-FP-0002-V9-06E36-home-recovery-life-mobile.md` | included | E36 stage report |
| `REPORTS/REPORT-FP-0002-V9-06E37-home-rehabilitation-program-direction-mobile.md` | included | E37 stage report |
| `REPORTS/REPORT-FP-0002-V9-06E36-E37-selective-persistence.md` | included | this persistence report |
| `PROJECT-STATUS.md` | included | exact-scope status update |
| `WORDPRESS/SOURCE-AUTHORITY.md` | included | exact-scope authority note |

## 6. Excluded files

| File/pattern | Reason |
|---|---|
| Other FP-0002 modified theme/plugin/ACF files | Already on prior tip `f77ee7eb` or unrelated to E36/E37 |
| `X:\MARS-Localhost\backups\…` | runtime backup only |
| STORAGE export screenshots / `_probe/` | external evidence tooling; not source authority |
| MetaBOT / OCPilot / iSEO / other workspaces | foreign WIP |
| DB dumps | none created; CSS-only |

## 7. Temp worktree / commit path

| Item | Value |
|---|---|
| Temp worktree used | YES |
| Temp worktree path | `X:\AI MARS STORAGE\git-sync-fp0002-e29c-e35-20260713-032549\repo` (reused; new worktree add failed on Windows MAX_PATH) |
| Temp branch | `fp0002/v9-06e36-e37-mobile-polish-persistence-20260713-042025` |
| Base HEAD | `f77ee7ebde7e597107d3bdb20aa0215a20268cce` (prior E29C–E35 tip; incremental chain — not main HEAD `af306264` which would re-diff 294 CSS lines) |
| Clean before copy | YES |
| Copy method | Exact allowlist `Copy-Item` from main worktree source authority → temp worktree |
| Staged files count | 6 |
| Staged files scope valid | YES |
| Commit attempted | YES |
| Commit hash | product `e8dc63da15cddd970a17b9c37f0c163274e630bc`; branch tip `e93a4ca3859dbce1cdf69ebc6885a3780fa1a96f` |
| Commit message | `FP-0002: persist v9 e36-e37 mobile polish` (+ annotate/finalize tip hashes) |
| Push attempted | NO |

## 8. Patch fallback

| Item | Value |
|---|---|
| Patch bundle created | NO |
| Patch bundle path | n/a |
| Patch file | n/a |
| Commit skipped reason | n/a (commit path used) |

## 9. Route smoke validation

| Route | Expected | HTTP | Result | Notes |
|---|---|---:|---|---|
| `/` | 200 | 200 | PASS | no fatal |
| `/uslugi/` | 200 | 200 | PASS | no fatal |
| `/blog/` | 200 | 200 | PASS | no fatal |
| `/specyalisty/` | 200 | 200 | PASS | no fatal |
| `/o-centre/` | 200 | 200 | PASS | no fatal |
| `/o-centre/programma-lecheniya/` | 200 | 200 | PASS | no fatal |
| `/kontakty/` | 200 | 200 | PASS | no fatal |

## 10. Main worktree preservation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Main worktree staged files after | 0 | 0 | PASS |
| Foreign WIP untouched | yes | yes | PASS |
| No reset/rebase/stash/clean | yes | yes | PASS |
| No push | yes | yes | PASS |

## 11. Documentation updates

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E36-E37-selective-persistence.md | created | PASS | source authority + STORAGE copy |
| PROJECT-STATUS.md | updated | PASS | E36/E37 local accepted; not production |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | PASS | E36/E37 + persistence notes |

## 12. Git result

COMMIT_CREATED

| Item | Value |
|---|---|
| Commit hash | product `e8dc63da15cddd970a17b9c37f0c163274e630bc`; tip `e93a4ca3859dbce1cdf69ebc6885a3780fa1a96f` |
| Temp branch | `fp0002/v9-06e36-e37-mobile-polish-persistence-20260713-042025` |
| Patch bundle | n/a |
| Commit skipped reason | n/a |
| Push | NO |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Main worktree dirty + ahead/behind origin | medium | accepted | Keep selective temp-branch persistence; no merge/push |
| New worktree add fails on Windows MAX_PATH | medium | mitigated | Reused prior persistence worktree path |
| CSS in main WIP still dirty vs main HEAD | low | expected | Main worktree intentionally not cleaned; tip branch holds truth |
| Screenshots not in git | low | accepted | Evidence lives under STORAGE export only |

## 14. Final verdict

PASS

Then state:

V9-06E36-E37 selective persistence:
COMPLETE

Runtime accepted state evidenced:
PASS

Source authority audited:
PASS

Selective commit:
PASS

Patch fallback:
SKIPPED

Foreign WIP preserved:
PASS

Main worktree preserved:
PASS

No push:
PASS

No destructive Git:
PASS

Recommended next phase:
OPERATOR_REVIEW_PERSISTENCE_RESULT

## 15. Recommended next action

OPERATOR_REVIEW_PERSISTENCE_RESULT

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E36-E37 selective persistence performed:
YES

Backup created:
YES

Runtime DB writes:
0

Source changes in main worktree:
YES

Temp worktree used:
YES

Git mutation:
YES

Git commit:
e8dc63da15cddd970a17b9c37f0c163274e630bc (product); tip e93a4ca3859dbce1cdf69ebc6885a3780fa1a96f

Git branch:
fp0002/v9-06e36-e37-mobile-polish-persistence-20260713-042025

Git push:
NO

Reset:
NO

Rebase:
NO

Stash:
NO

Cleanup:
NO

Foreign project work:
NO

Main worktree staged files:
0

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0
