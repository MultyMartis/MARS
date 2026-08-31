# SITE-002 / BZPM — Post-Storage-Hygiene Loss Audit Closeout

**Date:** 2026-08-31  
**Phase:** SITE-002 / BZPM — Post-Storage-Hygiene Canonical MARS Loss Audit + Documentation Reconciliation  
**Gate:** `SITE002_STORAGE_HYGIENE_CLOSEOUT_DOCUMENTED`

## Incident summary

Broad MARS Storage Hygiene removed old temporary Git worktree contours under `X:\AI MARS STORAGE\`:

- `git-sync-*`
- `git-reconcile-*`

The canonical monorepository `X:\AI MARS` was **not** intentionally deleted. Canonical Git on `origin/mars/canonical-post-recovery` was **not** intentionally cleaned.

## What was deleted

Historical disposable STORAGE Git worktrees (filesystem gone; representative list from evidence):

| Contour | Role (historical) |
|---------|-------------------|
| `git-sync-e01` | Early SITE-002 / Wave E sync |
| `git-sync-site002-offers-recovery-docs-01/02/03` | Offers recovery documentation waves |
| `git-sync-d6g-event-driven` | D6G event-driven import work |
| `git-sync-d6g1-20260807` | D6G1 server-side dispatch |
| `git-sync-d6g1a-20260807T162210` | D6G1A watchdog / kill-switch |
| Various `git-reconcile-*` | Reconciliation / promotion helpers |

## What was NOT deleted

| Asset | Status |
|-------|--------|
| `X:\AI MARS` monorepo | Present; canonical Git authority |
| `origin/mars/canonical-post-recovery` | Intact; SITE-002 commits reachable |
| `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\` | Complete canonical knowledge pack |
| `X:\AI MARS\projects\ocpilot\sites\site-002\tools\` | Production PHP mirrors in Git |
| `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` | Present (`KEEP_ACTIVE` / optional hygiene monitor) |
| Beget / OpenCart / n8n production runtime | Out of scope; not mutated by this audit |

**Note:** `runtime-checkouts\client-ops-site-002-producer\repo` is absent (Windows producer era retired per Client Ops handoff). This is expected, not hygiene loss.

## Git reachability findings

- Known consolidation commit `f27ebe80a6ba8252a97fd9003da271a3c2a8551a` (`docs(site002): consolidate 1c client ops stable knowledge and cleanup readiness`) is **reachable** from `origin/mars/canonical-post-recovery`.
- Later promoted SITE-002 docs include `9fe14f75`, `3e1a76c3`, `1c693b0c` on origin canonical tip.
- D6G-era branches (`mars/d6g-event-driven-1c-import`, `mars/d6g1-server-side-dispatch`, `mars/d6g1a-watchdog-kill-switch-*`, `mars/d6g1b-watchdog-cron-verification-*`, `docs/site002-final-knowledge-consolidation`, `site002/workstation-cleanup-closeout-01`) are **merged ancestors** of origin canonical.
- `git fsck --no-reflogs --unreachable --full` found **no SITE-002-scoped dangling commits** requiring rescue.
- **Local-only unpromoted content:** branch `closeout/site002-post-catalog-01` @ `17a6c5c0` holds two **doc-only** filter research commits (`6da95c5d`, `17a6c5c0`). Still reachable via local ref; **not** on origin canonical. Prior stability audit classified these as non-critical filter research — **no promote / no restore** unless operator re-charters.

## Canonical artifact findings

All current authority documents present under `client-ops/` including `FINAL-HANDOFF.md`, `AGENT-BRAIN.md`, `MASTER-OVERVIEW.md`, contracts, runbooks, and workstation-cleanup notes. **Zero** `git-sync` / `git-reconcile` references inside `client-ops/` authority pack.

D6G phase evidence remains under `X:\AI MARS\projects\client-ops-reporting-bridge\` (PHASE-1B-D6G*).

## Runtime findings

Production Client Ops authority is **server-side** (Beget cron, wrapper, dispatcher, n8n, Telegram). Workstation and deleted STORAGE git-sync contours were **never** production runtime authority.

## Runtime checkout findings

- `site-002-monitor` checkout **exists** and remains registered — not removed by hygiene.
- Windows producer checkout path absent — **retired by design**, separate from git-sync hygiene.

## Stale-path reconciliation

| Location | Classification | Action |
|----------|----------------|--------|
| `client-ops/*` authority docs | Clean | None required |
| `reports/*.md` historical audits | `HISTORICAL_EVIDENCE` | **Do not rewrite** |
| `tools/*.py` harness `AUTHORITY_REPO` → deleted git-sync paths | `CURRENT_AUTHORITY_STALE` | Documented here; operators must use `X:\AI MARS` or fresh worktree — **not** deleted contours |
| This closeout | Canonical | Added |

## Final verdict

**SAFE** — deleted SITE-002 `git-sync-*` / `git-reconcile-*` STORAGE contours were disposable or fully promoted; no unique unpromoted commit/WIP/source/config/recovery authority was lost for Client Ops production; current canonical SITE-002 knowledge and production authority remain intact.

## Restore decision

**RESTORE_NOT_REQUIRED**

Filter research on `closeout/site002-post-catalog-01` remains optionally recoverable from local Git ref if operator later charters promotion; it is **not** Client Ops production loss.

## Related prior audits

- `projects/ocpilot/sites/site-002/reports/SITE-002-MARS-STORAGE-HYGIENE-STABILITY-AUDIT-01.md`
- `projects/ocpilot/sites/site-002/reports/MARS-GIT-WORKTREE-PRUNE-APPLY-01.md`
