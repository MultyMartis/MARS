# REPORT — SITE-002 Category Entrypoint Onboarding

**Operation:** `SITE-002-PROD-CATEGORY-ENTRYPOINT-ONBOARDING-01`  
**OCPilot run:** 4.255  
**Date:** 2026-07-10  
**Environment:** Local monitor code + verification (`https://bzpm.ru/` read-only)  
**Worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Baseline (unchanged):** `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01`  
**Source:** Run 4.253 review + Run 4.254 meta onboarding

---

## 1. Scope

Close monitor allowlist / entrypoint onboarding after nested Lari reparent and Run 4.254 meta wave:

- Update `ONBOARDED_CATEGORY_PATHS` from flat `/lari/*` to nested `/shkafy-i-lari/lari/*`
- Verify id **140** entrypoint path
- Verify ids **362/363** post-meta monitor status
- Manual monitor run with updated code from temp worktree
- No production mutation

---

## 2. Operator approval

Operator approved production step `SITE-002-PROD-CATEGORY-ENTRYPOINT-ONBOARDING-01` after Run 4.254.

---

## 3. Pre-flight

| Check | Result |
|-------|--------|
| Worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| HEAD | `7319f78b` (includes Run 4.254 commit) |
| Staged files | **none** |
| Untracked | 3 verification `.py` tools (not committed) |
| Main worktree `X:\AI MARS` | **not touched** |
| `origin/mars/canonical-post-recovery` | `996489e3` (merge ahead of local branch — merged before push) |

**Verdict:** Pre-flight **PASS**.

---

## 4. Monitor code discovery

| Item | Value |
|------|-------|
| Allowlist file | `projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py` |
| Constant | `ONBOARDED_CATEGORY_PATHS` |
| Logic | `phase5_category_onboarding()` — flags added CATEGORY_PLP when path not in allowlist |
| Runner | `site-002-post-1c-monitor-runner.ps1` → **`X:\AI MARS`** (scheduled; not used for this verification) |

**Before:** 5 allowlist entries — 3 flat Lari paths, no nested Lari, no 362/363.

Storage: `deployments/.../code-before/`

---

## 5. URL/entity verification before

### HTTP (all PASS)

| Label | id | Status | Meta | Sitemap | БЗПМ |
|-------|-----|--------|------|---------|------|
| 88 nested | 88 | 200 | 141 chars | yes | 0 |
| 88 flat | 88 | 200 → nested | 141 chars | yes | 0 |
| 140 nested | 140 | 200 | 129 chars | yes | 0 |
| 141 nested | 141 | 200 | 138 chars | yes | 0 |
| 362 | 362 | 200 | 140 chars | yes | 0 |
| 363 | 363 | 200 | 132 chars | yes | 0 |

### DB read-only

**SAFE UNKNOWN** — SSH to production DB host failed from this environment (`NoValidConnectionsError` port 22). HTTP verification confirms Run 4.254 meta live on all target PLPs. Prior DB snapshot from Run 4.254 storage remains authoritative for row-level proof.

Storage: `url-verification-before/category-url-verification-before.{json,csv}`

---

## 6. Allowlist patch plan

**Remove** flat legacy paths (no longer in sitemap):

- `katalog/nejtralnoe-oborudovanie/lari`
- `katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari`
- `katalog/nejtralnoe-oborudovanie/lari/skladskie-lari`

**Add** nested canonical + post-meta paths:

- `katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` (id **88**)
- `katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari` (id **140**)
- `katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari` (id **141**)
- `katalog/tehnologicheskoe-oborudovanie` (id **362**)
- `katalog/nejtralnoe-oborudovanie/shkafy-i-lari/shkafy-dlya-hleba` (id **363**)

**362/363 rationale:** Monitor path gate is independent of meta quality; without allowlist entries they would re-flag on every post-1C delta.

Storage: `verification/allowlist-patch-plan.{md,json}`

---

## 7. Monitor code patch

**File changed:** `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` — `ONBOARDED_CATEGORY_PATHS` only.

- `py_compile`: **PASS**
- `--fixture-garbage-test`: **PASS** (7/7)
- Flat paths removed from allowlist; retained in `SANITY_URLS` for regression

Storage: `code-after/`, `verification/code-patch-verification.{md,json}`

---

## 8. Local tests / manual monitor run

| Field | Value |
|-------|-------|
| Command | `python site-002-prod-post-1c-catalog-onboarding-monitor-02.py --skip-removed-crawl --scheduled-run-dir <timestamp>` |
| Source | **temp worktree** (`git-sync-e01`) — not Task Scheduler |
| Run folder | `scheduled-monitors/post-1c/2026-07-10_18-16-39` |
| Exit code | **0** |
| Duration | **~89s** |
| Baseline / current | 1377 / 1424 |
| Added / removed | 61 / 14 |

Storage: `manual-run/`, `monitor-after/`

---

## 9. Manual run classification

| Metric | Before (`13-27-20`) | After (`18-16-39`) |
|--------|---------------------|---------------------|
| Classification | `ONBOARDING_REQUIRED` | `HYGIENE_REVIEW_REQUIRED` |
| Onboarding needs | **5** | **0** |
| Hygiene flags | 0 | 0 |
| Strict garbage | 0 | 0 |

**Verdict:** **PASS_REDUCED_ONBOARDING** — all 5 prior needs cleared. `HYGIENE_REVIEW_REQUIRED` is correct while sitemap delta (61/14) persists; no onboarding charter required.

id **140:** nested path onboarded in allowlist; HTTP 200, meta present, sitemap present — **verified**.

---

## 10. Site safety after

All regression URLs **PASS**: no 500; `/kontakty` 404 accepted; flat `/lari` rewrites to nested; nested targets 200 + in sitemap; `БЗПМ` 0; sitemap **1424** URLs.

Storage: `url-verification-after/site-safety-after.{json,csv}`

---

## 11. Final decision

| Area | Decision |
|------|----------|
| Monitor allowlist | **UPDATED** |
| Manual monitor verification | **PASS_REDUCED_ONBOARDING** |
| Production mutation | **0** |
| Checkpoint | **unchanged** `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01` |

---

## 12. Production mutation summary

| Class | Count |
|-------|-------|
| FTP writes | 0 |
| DB writes | 0 |
| Admin saves | 0 |
| Import runs triggered | 0 |
| Monitor manual runs triggered | **1** (temp worktree direct Python) |
| Task Scheduler changes | 0 |
| Form submits | 0 |
| Mail sends | 0 |
| Production code changes | 0 |
| Local monitor code changes | **1** (`site-002-prod-post-1c-catalog-onboarding-monitor-02.py`) |

---

## 13. Git/worktree summary

- Changes from `X:\AI MARS STORAGE\git-sync-e01\repo` only
- Main worktree **not touched**
- Push target: `origin/mars/canonical-post-recovery`
- **Note:** Task Scheduler runner still references `X:\AI MARS` until operator syncs main worktree or updates runner path

---

## 14. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CATEGORY-ENTRYPOINT-ONBOARDING-01\`

- `manifests/operation.json`
- `code-before/`, `code-after/`
- `url-verification-before/`, `url-verification-after/`
- `monitor-before/`, `monitor-after/`
- `manual-run/`, `test-runs/`, `verification/`

---

## 15. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| DB read-only SELECT this run | **BLOCKED** — SSH unreachable from agent environment |
| Task Scheduler uses updated code | **NOT YET** — runner points to `X:\AI MARS`; temp worktree verified only |
| `NO_ACTION_REQUIRED` classification | **Not expected** while 61/14 sitemap delta unchanged — `HYGIENE_REVIEW_REQUIRED` is accurate |

---

## 16. Final verdict

**SITE-002 CATEGORY ENTRYPOINT ONBOARDING COMPLETE — FALSE POSITIVES REMOVED, VALID ONBOARDING REMAINS**

(Onboarding count **0**; classification reduced from `ONBOARDING_REQUIRED` to `HYGIENE_REVIEW_REQUIRED`.)

---

## 17. Next recommendation

1. **Sync monitor code to `X:\AI MARS`** (or update runner `$RepoRoot`) so scheduled Task uses nested allowlist.
2. Optional **`SITE-002-PROD-POST-ONBOARDING-SPOTCHECK-01`** after next 1C import — confirm scheduled run classification with synced code.
3. No new production checkpoint required for this monitor-only change.
