# REPORT — MARS Local Storage Cleanup Apply 01

**Operation:** `MARS-LOCAL-STORAGE-CLEANUP-APPLY-01`  
**Run:** 4.324  
**Date:** 2026-08-12  
**Worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo-site002-stable-checkpoint-01`  
**Environment:** `LOCAL_STORAGE_CLEANUP_APPLY_EXACT_ALLOWLIST`

## 1. Scope

Execute local storage cleanup using **only** the exact approved dry-run allowlist from `MARS-LOCAL-STORAGE-CLEANUP-DRY-RUN-01`. Delete validated paths one-by-one with `Remove-Item -LiteralPath`. Verify active MARS roots after cleanup. Update docs/report only. No production/FTP/DB/source/Client Ops mutation.

## 2. Operator approval

| Item | Value |
|------|--------|
| Beget backup confirmation | `я бэкап на бегете сделал` |
| Cleanup apply approval | `Ок, утверждаю. Жду промт.` |
| Approval status | `APPROVED_FOR_EXACT_ALLOWLIST_DELETE` |
| Storage record | `.../MARS-LOCAL-STORAGE-CLEANUP-APPLY-01/approval/operator-approval.md` |

## 3. Stable checkpoint verification

| Item | Value |
|------|--------|
| Tag | `site-002/stable-prod-after-spam-guard-20260812` |
| Tag object | `330425515a1da5a2a011e6514bd933bc5f929c4f` (annotated) |
| Peeled commit | `a14a97c9fbb797d01477b7b08a546380c71ef080` |
| Matches expected `a14a97c9` | **YES** |
| Remote tag present | **YES** |
| Open issue | 1C/offers still **OPEN** — not touched |

## 4. Dry-run source

| Item | Value |
|------|--------|
| Dry-run operation | `MARS-LOCAL-STORAGE-CLEANUP-DRY-RUN-01` |
| Dry-run docs commit | `8a7831f2` |
| Allowlist CSV | `.../DRY-RUN-01/allowlist/delete-candidates-after-operator-approval.csv` |
| Allowlist count | **96** |
| Keep list | **23** |
| Unknown / do-not-touch | **51** |
| Estimated reclaimable | **~245.22 GB** |

## 5. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` label | `AI WS` |
| Worktree branch | `site-002-stable-checkpoint-spam-guard-01` |
| Worktree HEAD | `8a7831f237cbd64a8392c72f1568b7c88e1a64bc` |
| Tracks | `origin/mars/canonical-post-recovery` (+0/-0) |
| Staged changes | none |
| Unpushed commits | none |
| Dirty main (`X:\AI MARS`) | read-only inspected; foreign WIP present; **not mutated** |
| Stable tag | verified (peeled `a14a97c9`) |

## 6. Allowlist validation

| Metric | Count |
|--------|-------|
| Allowlist total | 96 |
| Validated OK (scheduled) | **95** |
| Already missing | 0 |
| Blocked / skipped | **1** (1.04% — under 5% hard-stop) |
| Whole-apply stop | **NO** |

Blocked path (not deleted):

- `X:\AI MARS\.recovery-temp` — `OUTSIDE_ALLOWED_CLEANUP_ROOTS` / under Active Brain / keep / unknown overlap

No protected authority paths (`git-sync-e01\repo`, `repo-site002-stable-checkpoint-01`, monitor checkout, secrets, incoming) were scheduled.

## 7. Before delete manifest

- Paths scheduled: **95**
- Estimated size: **~244.78 GB**
- Manifest: `before-delete/before-delete-manifest.csv`
- Deep file counts skipped as impractical for large trees; top-level counts + CSV sizes recorded

## 8. Delete execution

| Metric | Value |
|--------|--------|
| Method | `Remove-Item -LiteralPath "<exact>" -Recurse -Force` |
| One path at a time | YES |
| Wildcards | NO |
| DELETED_OK | **95** |
| FAILED | **0** |
| ALREADY_MISSING | **0** |
| Elapsed | **~10.73 minutes** |

## 9. After delete verification

| Metric | Value |
|--------|--------|
| Confirmed gone | **95 / 95** |
| Still exists | **0** |
| Remaining paths | none |

## 10. Actual reclaim

| Metric | Value |
|--------|--------|
| Estimated reclaimed | **~244.78 GB** (sum of before-delete size estimates for DELETED_OK) |
| Dry-run expected | ~245 GB |
| Exact volume free-space delta | **SAFE UNKNOWN** (not measured as full volume audit) |
| Blocked path size | excluded (Active Brain path not deleted) |

## 11. Active roots verification

| Root | Status |
|------|--------|
| `X:\AI MARS` | INTACT / Git readable |
| `X:\AI MARS STORAGE\git-sync-e01\repo` | INTACT / Git readable |
| `X:\AI MARS STORAGE\git-sync-e01\repo-site002-stable-checkpoint-01` | INTACT / Git readable |
| `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` | INTACT / Git readable |
| Secrets folder | INTACT |
| Dry-run + apply artifact folders | INTACT |
| Stable tag | resolves to `a14a97c9…` |
| `origin/mars/canonical-post-recovery` | resolves |
| Production FTP/DB actions | **0** |

Verdict: **ACTIVE_ROOTS_VERIFIED**

## 12. Skipped / blocked paths

| Path | Reason |
|------|--------|
| `X:\AI MARS\.recovery-temp` | Under Active Brain / keep/unknown / outside STORAGE or Localhost cleanup roots |

Keep list (23) and unknown list (51) were **not** deleted.

## 13. Mutation summary

| Mutation | Count |
|----------|-------|
| local deletes | **95** (exact validated allowlist only) |
| local moves | **0** |
| local archives | **0** |
| production DB writes | **0** |
| production FTP writes | **0** |
| source/code changes | **0** |
| cache clear | **0** |
| import runs | **0** |
| monitor baseline changes | **0** |
| dirty main changes | **0** |
| Client Ops changes | **0** |
| docs/report changes | report + OPERATIONAL-INDEX + OCPILOT-STATE + runtime-checkouts note |

## 14. Git/worktree summary

| Item | Value |
|------|--------|
| Clean worktree used | `repo-site002-stable-checkpoint-01` |
| Branch | `site-002-stable-checkpoint-spam-guard-01` → `origin/mars/canonical-post-recovery` |
| Docs commit message (this wave) | `ocpilot: record MARS local cleanup apply` |
| Force push | **not used** |
| Dirty main | untouched |

## 15. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\MARS-LOCAL-STORAGE-CLEANUP-APPLY-01\`

Includes: `preflight/`, `approval/`, `dry-run-read/`, `allowlist-validation/`, `before-delete/`, `delete-execution/`, `after-delete/`, `active-roots-verification/`, `size-reclaim/`, `docs-update/`, `decision/`, `manifests/operation.json`, logs/reports.

## 16. SAFE UNKNOWN / blockers

- Exact Windows volume free-space delta not measured (reclaim is estimate from dry-run sizes).
- 1C/offers gap remains **OPEN** (out of cleanup scope).
- Unknown/do-not-touch list (51) intentionally retained — do not delete without a new dry-run.
- One dry-run allowlist entry under `X:\AI MARS` was correctly blocked by apply gate.

## 17. Final verdict

**MARS LOCAL STORAGE CLEANUP APPLY COMPLETE — EXACT ALLOWLIST DELETED, ACTIVE ROOTS VERIFIED**

| Classification | Value |
|----------------|--------|
| Decision | `CLEANUP_APPLY_PARTIAL_SKIPPED_PATHS` |
| Meaning | 95/95 validated deletes OK; 1 protected Active Brain path skipped |
| Next | `READY_FOR_NORMAL_WORK` + `DO_NOT_DELETE_UNKNOWN_ITEMS` + `WAIT_FOR_1C_OFFERS_FIX` |

## 18. Next recommendation

1. Resume normal SITE-002 ops on verified active roots.
2. Do **not** delete remaining unknown/keep items without a new dry-run + approval.
3. Keep waiting on 1C/offers fix (separate track).
4. Optional later: second cleanup dry-run for residual large items if disk pressure remains.
