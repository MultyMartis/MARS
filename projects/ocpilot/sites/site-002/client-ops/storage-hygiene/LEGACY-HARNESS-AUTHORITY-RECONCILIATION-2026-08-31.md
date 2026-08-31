# SITE-002 / BZPM — Legacy Harness Authority Path Reconciliation Closeout

**Date:** 2026-08-31  
**Phase:** SITE-002 — Legacy Harness Authority Path Reconciliation  
**Source audit:** `POST-STORAGE-HYGIENE-LOSS-AUDIT-2026-08-31.md` @ canonical commit `6c2286d2`  
**Gate:** `SITE002_HARNESS_RECON_CLOSEOUT_DOCUMENTED`

## Purpose

Post–Storage-Hygiene audit proved no production/data loss from deleted `git-sync-*` / `git-reconcile-*` contours, but found **16** legacy Python harness files under `tools/` that still hardcoded deleted temporary worktree paths as `AUTHORITY_REPO` or equivalent. This phase reconciled those paths so ACTIVE/OCCASIONAL tooling and future Agents are not directed to disposable contours.

## Authority model (final)

| Role | Path | Usage |
|------|------|--------|
| Canonical source/docs | `X:\AI MARS` | Read-only inspection OK with foreign WIP |
| Git mutation | Fresh clean worktree via `--repo-root` | `X:\AI MARS STORAGE\git-sync-<label>\repo` — **never hardcode a named old contour** |
| Runtime scheduled jobs | `X:\AI MARS STORAGE\runtime-checkouts\...` | e.g. `site-002-monitor\repo` |
| Production deploy | Beget/server-side | Not local temp Git worktrees |

Shared helper: `tools/site002_harness_authority.py`

## Tools inspected

**Count:** 16 Python harness files with stale deleted `git-sync-*` authority paths (actual count verified; not assumed).

| File | Old authority | Classification | Authority requirement |
|------|---------------|----------------|----------------------|
| `site-002-prod-posuda-upakovochnoe-empty-category-check-01.py` | `git-sync-site002-offers-recovery-docs-03\repo` | **OCCASIONAL** | CANONICAL_READ_ONLY (+ optional `--repo-root`) |
| `site-002-prod-megamenu-leaf-root-info-panel-01.py` | `git-sync-site002-offers-recovery-docs-03\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-megamenu-leaf-info-minidescription-01.py` | `git-sync-site002-offers-recovery-docs-03\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-megamenu-and-posuda-plp-repair-01.py` | `git-sync-site002-offers-recovery-docs-03\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-catalog-normalization-ui-repair-01.py` | `git-sync-site002-offers-recovery-docs-03\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-catalog-normalization-apply-combined-01.py` | `git-sync-site002-offers-recovery-docs-03\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-first-level-block-hybrid-apply-01.py` | `git-sync-e01\repo` | HISTORICAL | RUNTIME_CHECKOUT_REQUIRED (monitor) when run |
| `site-002-prod-first-level-block-all15-correction-apply-01.py` | `git-sync-e01\repo` | HISTORICAL | RUNTIME_CHECKOUT_REQUIRED (monitor) when run |
| `site-002-prod-empty-category-copy-relocate-and-new-firstlevel-images-01.py` | `git-sync-e01\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-brand-caps-and-blog-slider-order-01.py` | `git-sync-e01\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-blog-publish-datetime-readtime-01.py` | `git-sync-e01\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-blog-literal-newline-cleanup-01.py` | `git-sync-e01\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-1c-category-mapping-backfill-01.py` | `git-sync-e01\repo` | HISTORICAL | NO_CURRENT_AUTHORITY_REQUIRED |
| `site-002-prod-d6g-event-driven-import-01.py` | `git-sync-d6g-event-driven\repo` | HISTORICAL/RETIRED | SERVER_RUNTIME_REQUIRED when run |
| `site-002-prod-d6g1-server-dispatch-01.py` | `git-sync-d6g1-20260807\repo` | HISTORICAL/RETIRED | SERVER_RUNTIME_REQUIRED when run |
| `site-002-prod-d6g1a-watchdog-kill-switch-01.py` | `git-sync-d6g1a-20260807T162210\repo` | HISTORICAL/RETIRED | SERVER_RUNTIME_REQUIRED when run |

**UNKNOWN_NEEDS_REVIEW:** none.

## Classification summary

| Class | Count |
|-------|-------|
| ACTIVE | 0 |
| OCCASIONAL | 1 |
| HISTORICAL | 12 |
| RETIRED | 3 (D6G family; merged/promoted) |
| UNKNOWN_NEEDS_REVIEW | 0 |

## Fixes applied

1. **Added** `tools/site002_harness_authority.py` — shared resolution for read-only canonical root, clean-worktree-required mutation, disposable-path detection, historical guard.
2. **OCCASIONAL** posuda check: defaults to `X:\AI MARS`; accepts `--repo-root`; no deleted contour.
3. **15 HISTORICAL/RETIRED** scripts: replaced stale `AUTHORITY_REPO`/`REPO`/`WT` with `CANONICAL_MONOREPO` + `site002_tools_dir()` / `site002_reports_dir()`; hybrid/all15 retain `DEFAULT_MONITOR_CHECKOUT` for monitor path; `guard_historical_harness()` fail-fast at `main()` unless `--allow-historical-run`.
4. **Report templates** in empty-category harness updated to canonical authority wording (no deleted named contour).

## Retired / historical handling

- HISTORICAL/RETIRED scripts **not deleted** — evidence preserved.
- Accidental execution blocked via `guard_historical_harness()` unless explicit override.
- D6G deploy/FTP logic unchanged; only local authority path resolution modernized.

## Documentation reconciliation

- `client-ops/AGENT-BRAIN.md` — harness authority bullets added (helper module, closeout reference).
- Historical audit docs under `storage-hygiene/` and `reports/` **unchanged** (HISTORICAL_EVIDENCE).

## Regression

- `python -m py_compile` on helper + all 16 patched files: **PASS**
- Helper smoke: `resolve_repo_root_for_read()` → canonical; `guard_historical_harness()` fail-fast: **PASS**
- Posuda `--help` exposes `--repo-root`: **PASS**
- Historical harnesses exit with HISTORICAL guard without override: **PASS**

## Post-fix stale reference search

Within `tools/*.py` executable authority logic:

- **Named deleted `git-sync-*` contours:** 0
- **Allowed remaining:** generic `git-sync-<label>` pattern in helper docstrings/messages only; `git-reconcile-` detection string in helper.

## Production mutation count

**0** — no Beget, OpenCart, 1C import, n8n, Data Table, Telegram, watchdog, kill-switch, cron, or Scheduled Task mutations.

## Git canonicalization

Performed from clean worktree:

`X:\AI MARS STORAGE\git-sync-site002-harness-authority-recon-20260831\repo`

Dirty MAIN (`X:\AI MARS`) untouched.

## Final authority rule for Agents

1. **`X:\AI MARS`** is canonical source/docs authority on `mars/canonical-post-recovery`.
2. **Old named `git-sync-*` / `git-reconcile-*` paths are disposable history** — do not use as authority.
3. **Git mutation** requires a **fresh clean worktree** via `--repo-root`; fail closed on dirty MAIN.
4. **Runtime jobs** use `runtime-checkouts\...` when applicable.
5. **Production operations** use server-side authority.
6. Import `site002_harness_authority` for new harness work instead of hardcoding paths.

## Readiness

`SITE002_LEGACY_HARNESS_AUTHORITY_RECONCILIATION_COMPLETE`
