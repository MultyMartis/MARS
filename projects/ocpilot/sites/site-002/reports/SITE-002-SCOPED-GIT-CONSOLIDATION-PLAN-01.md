# SITE-002-SCOPED-GIT-CONSOLIDATION-PLAN-01

**Verdict:** `SITE-002 SCOPED GIT CONSOLIDATION PLAN COMPLETE — WAITING OPERATOR GO`

**Mode:** PLAN-ONLY — no commit, no push, no production mutation, no mutating git on dirty main.

---

## 1. Scope

Plan safe Git consolidation of accepted SITE-002 M9/PDP production state via a future clean scoped worktree under `X:\AI MARS STORAGE\git-sync-*`.

## 2. Operator Git model

1. `X:\AI MARS` = one MARS monorepo (OCPilot, MetaBOT, WP Forge, iSEO, FP-0002, etc. are folders — not separate Git repos).
2. Canonical remote branch: `origin/mars/canonical-post-recovery`.
3. Safe Git ops: temporary clean worktrees `X:\AI MARS STORAGE\git-sync-*\repo`.
4. Scheduled jobs: `X:\AI MARS STORAGE\runtime-checkouts\` — SITE-002 monitor already fixed; **not changed by this task**.
5. Foreign WIP in dirty main is normal and out of scope.

## 3. No-mutation boundary

Forbidden on `X:\AI MARS` for SITE-002 chat: `git pull` / `reset` / `clean` / `stash` / `restore`; `git add .` / `-A`; `git commit -a`; commit; push; force push; production/DB/FTP write.

This task wrote only Storage evidence + this report.

## 4. Git read-only state (plan time)

| Item | Value |
|------|-------|
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8022a04854bf7affb619f12a9695329a59650182` |
| origin tip | `131882bdfdcfc4e11ad68b32f133201e66b17407` |
| Ahead / behind | **287 / 46** |
| Staged | empty |
| SITE-002 status | mix of `??` untracked accepted files + modified resolver; foreign WIP elsewhere |

Evidence: Storage `...\SITE-002-SCOPED-GIT-CONSOLIDATION-PLAN-01\git-readonly\`

## 5. Accepted SITE-002 state

Authority: `SITE-002-M9-PDP-CONSOLIDATION-CHECKPOINT-01`

- M9 filters: **86, 301, 331, 186** (+ 188/189 inherit)
- PDP hero specs: **86, 186**
- Live profiles byte-identical in repo WC for 86/301/331/186
- Live filter resolver SHA `0d994191…` (6321 B); WC `4c23c39a…` (5984 B)
- Live `product_hero_specs_resolver.php` SHA `19c9bc82…` — **absent from repo**

## 6. Candidate file inventory

See Storage `file-scope/site002-consolidation-candidates.csv`.

**Include later:** four profiles; filter resolver (after A/B); import hero resolver; listed reports.

**Include only after review:** `product.php` (STELLAZHI Storage payload; proposed patch path).

**Do not include:** foreign WIP, backups, unrelated tools, broad adds.

## 7. Resolver mismatch analysis

| Version | 86/301/331/186 regs? |
|---------|----------------------|
| HEAD / origin | **No** |
| Repo WC | **Yes** |
| Live | **Yes** |

Mismatch WC vs live = **CRLF + blank lines only**. Compact non-blank identity = **TRUE**.

Default recommendation: commit **LF compact WC** (option B) with note; or live bytes (option A) if operator requires production SHA.

## 8. Missing repo files

- `product_hero_specs_resolver.php` → recommended path under `m9-phase3-remaining-work/patch/system/library/zpm/`
- `product.php` → proposed `.../patch/catalog/controller/product/product.php` after path GO

## 9. Clean worktree future route

**Feasible: YES**

Create unique:

`X:\AI MARS STORAGE\git-sync-site002-m9-pdp-consolidation-<YYYYMMDD-HHMMSS>\repo`

from `origin/mars/canonical-post-recovery`, copy allowlist, exact `git add --`, commit/push only after GO. Leave dirty main and runtime-checkouts untouched.

## 10. Proposed commit groups

1. M9 profiles + filter resolver + M9 reports  
2. PDP hero resolver (+ optional product.php) + PDP reports  
3. Visual QA + checkpoint + this plan  

Exact adds: Storage `commit-plan/exact-file-add-list.txt`

## 11. Do-not-stage list

See Storage `commit-plan/do-not-stage-list.txt` — foreign WIP, backups, `git add .`, old HEAD resolver, blind 287-commit push.

## 12. Risk register

See Storage `risk-register/git-consolidation-risk-register.md` (dirty main, origin divergence, resolver SoT, missing hero mirror, product.php path, foreign WIP).

## 13. Operator GO checklist

Three gates: GO-1 worktree+import → GO-2 commit → GO-3 push. Storage `operator-go/operator-go-checklist.md`.

## 14. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-SCOPED-GIT-CONSOLIDATION-PLAN-01\`

Subfolders: `preflight`, `git-readonly`, `accepted-state`, `file-scope`, `resolver-analysis`, `missing-repo-files`, `commit-plan`, `worktree-plan`, `risk-register`, `operator-go`, `reports`, `logs`, `manifests`.

## 15. Final verdict

**`SITE-002 SCOPED GIT CONSOLIDATION PLAN COMPLETE — WAITING OPERATOR GO`**

Next action: operator reviews plan → GO-1 (create unique clean worktree + import allowlist) → then GO-2/GO-3 for commit/push. No consolidation commit until GO.
