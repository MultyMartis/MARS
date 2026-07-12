# REPORT — MARS Infra Runtime Split SITE-002 Natural Run Verify

**Operation ID:** `MARS-INFRA-RUNTIME-SPLIT-SITE-002-NATURAL-RUN-VERIFY-01`  
**MARS infra run:** `MARS-INFRA-RUNTIME-SPLIT-NATURAL-VERIFY-01`  
**OCPilot reference:** Run **4.259** (infra)  
**Date:** 2026-07-12

> Storage mirror: `X:\AI MARS STORAGE\mars-infrastructure\runtime-split\MARS-INFRA-RUNTIME-SPLIT-SITE-002-NATURAL-RUN-VERIFY-01\reports\MARS-INFRA-RUNTIME-SPLIT-SITE-002-NATURAL-RUN-VERIFY-01.md`

---

## 1. Scope

Read-only verification that natural scheduled SITE-002 post-1C monitor runs from the clean runtime checkout after the dirty-main detach. No production mutation. No scheduler mutation. No manual monitor trigger.

## 2. Operator context

~2 days after runtime split + scheduled spotcheck. Operator noted Saturday/Sunday likely had no 1C catalog changes. This verify is about scheduler/runtime wiring and natural run observation — not about forcing a 1C import.

## 3. Pre-flight

Authority worktree `X:\AI MARS STORAGE\git-sync-e01\repo`:

| Check | Result |
|-------|--------|
| Branch | `site-002-git-authority-realign-after-wave-e` |
| HEAD | `db1d04b1` |
| `origin/mars/canonical-post-recovery` | `db1d04b1` |
| Includes `db1d04b1` / `bd3021bf` | yes |
| Tracked dirty | none |
| Untracked | 3 verification `.py` (not committed) |

**PASS** — safe for docs/report commit.

## 4. Task Scheduler check

| Field | Value |
|-------|--------|
| Task | `MARS_SITE_002_Post_1C_Catalog_Monitor` |
| Exists / Enabled | yes / Ready |
| Action | `powershell.exe … -File "X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo\projects\ocpilot\sites\site-002\tools\site-002-post-1c-monitor-runner.ps1"` |
| WorkingDirectory | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` |
| Last run | **2026-07-12 12:30:30 +07** |
| LastTaskResult | **0** |
| Next run | 2026-07-13 12:30:30 +07 |
| Dirty main referenced | **no** |
| Runtime checkout referenced | **yes** |

**Natural run class:** `NATURAL_RUN_CONFIRMED`

## 5. Runtime checkout check

| Field | Value |
|-------|--------|
| Path | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` |
| Status | **clean** |
| HEAD | `bd3021bf` |
| Runner / monitor | present |
| Allowlist | nested Lari + `tehnologicheskoe-oborudovanie` + `shkafy-dlya-hleba` (362/363 paths) present |

Dirty `X:\AI MARS` is **not** the scheduler runtime source.

## 6. Latest monitor artifact check

| Field | Value |
|-------|--------|
| Latest folder | `2026-07-12_12-30-02` |
| Natural align | yes (starts 12:30:02) |
| `repo_root` | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` |
| Classification | **ONBOARDING_REQUIRED** |
| onboarding_needs_count | **2** |
| strict_garbage / hygiene / БЗПМ | **0 / 0 / 0** |
| added / removed | **167 / 14** |
| baseline → current | 1377 → 1530 (baseline still stale) |
| Old Lari FP needs returned | **no** |
| Production mutation | **0** |

Needs (new branches, not old Lari FPs):

1. `/katalog/tehnologicheskoe-oborudovanie/posuda-i-inventar`
2. `/katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-standart/stellazhi-standart-vysota-1600`

Also observed: `2026-07-11_14-07-39` with same runtime `repo_root` and same needs=2 (secondary/delayed run relative to 12:30).

Catalog delta is **not** “no change” vs Jul 10 manual (`1424` → `1530`); weekend “no 1C” expectation does not match sitemap growth / two new category URLs.

## 7. Site safety quick check

All sampled URLs PASS (no 500; sitemap 200; `/kontakty` 404 accepted; targets 200; public `БЗПМ` 0).

## 8. Final decision

| Axis | Class |
|------|--------|
| Scheduler source | `RUNTIME_CHECKOUT_CONFIRMED` |
| Natural run | `CONFIRMED` |
| Monitor result | `ONBOARDING_REGRESSION` |

Runtime split goal (natural run from clean checkout) **succeeded**. Success criterion `onboarding_needs_count = 0` **failed** — two new category branches flagged `ONBOARDING_REQUIRED`.

## 9. Production mutation summary

- FTP writes: 0
- DB writes: 0
- Admin saves: 0
- Import runs triggered: 0
- Production code changes: 0
- Production content changes: 0
- Form submits: 0
- Mail sends: 0

## 10. Scheduler mutation summary

- Task changes: 0
- Trigger changes: 0
- Settings changes: 0
- Manual monitor runs: 0

## 11. Git/worktree summary

Docs/report authored in authority `git-sync-e01`. Dirty main untouched. Runtime checkout inspected read-only (clean @ `bd3021bf`).

## 12. Storage artifacts

`X:\AI MARS STORAGE\mars-infrastructure\runtime-split\MARS-INFRA-RUNTIME-SPLIT-SITE-002-NATURAL-RUN-VERIFY-01\`

Subfolders: `preflight/`, `task-scheduler/`, `runtime-checkout/`, `monitor-artifacts/`, `http/`, `verification/`, `reports/`, `manifests/`, `logs/`

## 13. SAFE UNKNOWN / blockers

- Baseline sitemap selection remains stuck at **1377**, inflating added counts across runs; treat large delta as partly baseline hygiene debt.
- `run-summary.json` may show `NO_ACTION_REQUIRED` while `monitor-classification.json` shows `ONBOARDING_REQUIRED` — authoritative gate is **monitor-classification**.
- Two needs are **new** categories (not Lari allowlist regression); still fail the `needs=0` verify gate.

## 14. Final verdict

**MARS INFRA RUNTIME SPLIT SITE-002 NATURAL RUN VERIFY FAILED — ONBOARDING REGRESSION**

## 15. Next recommendation

1. Charter `SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-02` (or equivalent) for the two new category paths + allowlist update.
2. Optionally refresh monitor baseline after onboarding so scheduled deltas shrink.
3. No further runtime-split scheduler work required unless task drifts off runtime checkout.
