# REPORT — MARS Local Storage Cleanup Dry Run 01

**Operation:** `MARS-LOCAL-STORAGE-CLEANUP-DRY-RUN-01`  
**OCPilot run:** **4.323**  
**Date:** 2026-08-12  
**Worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo-site002-stable-checkpoint-01`  
**Verdict:** `MARS LOCAL STORAGE CLEANUP DRY RUN COMPLETE — ALLOWLIST READY, NO DELETE EXECUTED`

## 1. Scope

Local cleanup **dry-run only** after operator Beget backup confirmation. Reconfirm stable Git tag; re-read Run **4.322** inventory; re-scan MARS roots; prepare exact delete allowlist / keep / unknown lists and future apply plan. **No** delete, move, rename, archive, production mutation, dirty-main mutation, Client Ops / n8n / Telegram / secrets / 1C exchange mutation.

## 2. Operator backup confirmation

Operator message: **«я бэкап на бегете сделал»**

Recorded as: `operator_beget_backup_done: true` in Storage `manifests/operation.json`.

## 3. Stable checkpoint verification

| Field | Value |
|-------|-------|
| Prior operation | `SITE-002-PROD-STABLE-CHECKPOINT-AFTER-SPAM-GUARD-AND-CLEANUP-INVENTORY-01` (Run **4.322**) |
| Stable tag | `site-002/stable-prod-after-spam-guard-20260812` |
| Tag type | annotated |
| Tag object | `330425515a1da5a2a011e6514bd933bc5f929c4f` |
| Peeled commit | **`a14a97c9`** (matches expected) |
| Origin tip | `a14a97c9` = `origin/mars/canonical-post-recovery` |
| Tag on origin | **yes** (`git ls-remote --tags`) |
| Classification prior | `STABLE_FOR_SITE_OPS_WITH_1C_OFFERS_OPEN` |
| Baseline | **1879** |
| Open issue | 1C/offers — `offers0_*.xml` still expected |

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` label | **AI WS** |
| Clean worktree | clean; branch `site-002-stable-checkpoint-spam-guard-01`; HEAD `a14a97c9`; ahead/behind **+0 -0** |
| Dirty main `X:\AI MARS` | Read-only; foreign WIP present; **not mutated** |
| Named authority `git-sync-e01\repo` | HEAD `812d1515`; **dirty**; left untouched |
| Staged changes (clean WT) | empty |

Artifacts: Storage `preflight/git-state.txt`, `preflight/tag-verification.txt`, `preflight/dirty-main-readonly.txt`.

## 5. Previous inventory

Source: Run **4.322** Storage `cleanup-inventory/` + `cleanup-charter/`.

| Metric | Prior |
|--------|-------|
| Inventory rows | 304 |
| Delete candidates after backup | 202 |
| Keep | 43 |
| Unknown | 53 |
| Largest samples | worktrees ~64 GB; git-sync-e01 ~15 GB |

Charter precondition «Beget backup» now **satisfied**. Summary: Storage `previous-inventory/previous-inventory-summary.md`.

## 6. Filesystem scan

Structured top-level size scan (robocopy `/L`, locale-safe) of:

- `X:\AI MARS STORAGE\`
- `X:\MARS-Localhost\`
- `X:\AI MARS\`

Largest measured folders:

| Path | Size MB |
|------|---------|
| `STORAGE\worktrees` | **64441.6** |
| `STORAGE\website-factory` | **17782** |
| `STORAGE\git-sync-e01` | **15367** |
| `Localhost\backups` | **12388.8** |
| `AI MARS\workspaces` | **8488.7** |
| `STORAGE\runtime-checkouts` | **8397.5** |
| `STORAGE\incoming` | **6697.9** |
| `AI MARS\.recovery-temp` | ~451 |

Limits: Storage `filesystem-scan/scan-limits.md`. CSVs: `top-level-size-summary.csv` and per-root summaries.

## 7. Git repo scan

Scanned **118** git-related paths (read-only).

| Classification | Count |
|----------------|-------|
| DELETE_CANDIDATE_AFTER_OPERATOR_APPROVAL | 95 |
| REVIEW_REQUIRED | 10 |
| UNKNOWN_DO_NOT_TOUCH | 9 |
| KEEP_ACTIVE | 4 |

Critical:

- Active Brain — KEEP_ACTIVE (dirty WIP — do not git clean)
- `git-sync-e01\repo` — **UNKNOWN_DO_NOT_TOUCH** (WIP / behind)
- `repo-site002-stable-checkpoint-01` — KEEP_ACTIVE @ `a14a97c9`
- `runtime-checkouts\site-002-monitor\repo` — KEEP_RUNTIME

## 8. Size analysis

Estimated reclaimable **from HIGH-confidence allowlist only**: ~**245.2 GB** (~251109 MB).

Not counted as reclaimable: `website-factory`, `git-sync-e01`, `incoming`, runtime checkouts, Localhost backups, unknown/review paths.

## 9. Delete candidate allowlist

File: Storage `allowlist/delete-candidates-after-operator-approval.csv`

- **96** exact paths
- Confidence: **HIGH** only
- Includes: all `STORAGE\worktrees\*` children; obsolete `git-sync-*` (non-e01, **excluding** recent `phase3h7*`); `X:\AI MARS\.recovery-temp`
- Each row has: reason, precondition, exact future `Remove-Item` draft, risk, rollback source
- **No wildcards**; apply still requires separate operator approval

## 10. Keep list

File: Storage `keep-list/keep-active.csv` (**23** rows)

Includes: Active Brain / Storage / Localhost roots; `git-sync-e01` family; stable-checkpoint worktree; SITE-002 + Client Ops runtime checkouts; ocpilot evidence; incoming; secrets; recent e01 siblings pending retention; Localhost runtime/sites/DB.

## 11. Unknown do-not-touch list

File: Storage `unknown-list/unknown-do-not-touch.csv` (**51** rows)

Must not delete without separate review:

- `git-sync-e01\repo` (authority WIP)
- `website-factory` (~17.8 GB)
- Non-SITE-002 runtime checkouts
- Recent `phase3h7*` git-sync folders
- Dirty main WIP mass cleanup
- Secrets / unclear STORAGE tops / Localhost backups retention

## 12. Future apply plan

Storage:

- `future-apply-plan/cleanup-apply-plan.md`
- `future-apply-plan/cleanup-apply-prompt.md`
- `future-apply-plan/not-executed.md`

Future op: `MARS-LOCAL-STORAGE-CLEANUP-APPLY-01` — dry-run echo → before/after manifests → exact-path deletes only → verify active roots. **Not executed** here.

## 13. Mutation summary

| Item | Count |
|------|-------|
| local deletes | **0** |
| local moves | **0** |
| local archives | **0** |
| production DB writes | **0** |
| production FTP writes | **0** |
| source/code changes | **0** |
| cache clear | **0** |
| import runs | **0** |
| dirty main changes | **0** |
| Client Ops changes | **0** |
| docs/report changes | this report + OPERATIONAL-INDEX + OCPILOT-STATE |

## 14. Git/worktree summary

| Item | Value |
|------|-------|
| Commit worktree | `repo-site002-stable-checkpoint-01` |
| Branch | `site-002-stable-checkpoint-spam-guard-01` |
| Base HEAD | `a14a97c9` |
| Dirty main | untouched |
| Authority `repo` | untouched |

## 15. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\MARS-LOCAL-STORAGE-CLEANUP-DRY-RUN-01\`

Subfolders: `preflight`, `stable-checkpoint`, `previous-inventory`, `filesystem-scan`, `git-repo-scan`, `size-analysis`, `allowlist`, `keep-list`, `unknown-list`, `future-apply-plan`, `docs-update`, `decision`, `regression`, `reports`, `manifests`, `logs`.

## 16. SAFE UNKNOWN / blockers

- Unique unpushed content inside each obsolete git-sync clone: **not fully proven absent** for every path — allowlist requires operator spot-check before apply
- `website-factory` purpose/owner: **UNKNOWN**
- Authority `repo` WIP uniqueness: **UNKNOWN** — default keep
- Localhost `backups` retention policy: **not decided**
- 1C/offers production gap remains **OPEN** (unchanged; out of cleanup scope)

No blocker to dry-run completion. Apply blocked until operator allowlist approval.

## 17. Final verdict

**Classification:** `CLEANUP_DRY_RUN_COMPLETE_ALLOWLIST_READY`

**Verdict:** `MARS LOCAL STORAGE CLEANUP DRY RUN COMPLETE — ALLOWLIST READY, NO DELETE EXECUTED`

## 18. Next recommendation

1. **`OPERATOR_REVIEW_DELETE_ALLOWLIST`** — review Storage allowlist CSV  
2. After written approval: **`READY_FOR_CLEANUP_APPLY_AFTER_APPROVAL`** → run `MARS-LOCAL-STORAGE-CLEANUP-APPLY-01`  
3. **`DO_NOT_DELETE_UNKNOWN_ITEMS`** — keep authority repo, website-factory, runtimes, secrets, recent h7 syncs until reviewed  
4. Continue SITE-002 1C/offers track separately (production; not local cleanup)
