# MARS runtime checkouts

**Document role:** Human-operated registry of clean Git checkouts used for scheduled/local runtime — **not** a runtime product.

**Last updated:** 2026-07-10 (`MARS-INFRA-RUNTIME-SPLIT-SITE-002-01`)

---

## Purpose

Scheduled and unattended local jobs must **not** execute from the dirty development worktree `X:\AI MARS` when foreign WIP is present. Runtime checkouts provide pinned, clean trees under `X:\AI MARS STORAGE\runtime-checkouts\`.

---

## SITE-002 post-1C monitor

| Field | Value |
|-------|--------|
| Site | SITE-002 |
| Job | `MARS_SITE_002_Post_1C_Catalog_Monitor` |
| Path | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` |
| Source ref | `origin/mars/canonical-post-recovery` |
| Pinned commit (2026-07-10) | `56f9bae7` |
| Checkout method | Sparse clone — cone `projects/ocpilot` |
| Runner | `projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner.ps1` |
| WorkingDirectory | Same as repo root above |
| Artifacts | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\` |

### Update policy

1. Fetch in authority worktree; note new `origin/mars/canonical-post-recovery` SHA when monitor/runner/allowlist changes.
2. In runtime checkout: `git fetch origin && git checkout <sha>` (sparse cone unchanged).
3. Re-run `site-002-post-1c-monitor-runner.ps1 -DryRun`.
4. Optional manual `Start-ScheduledTask` verification.
5. Record infra report under `projects/mars-infrastructure/reports/`.

If full checkout fails on Windows long paths, prefer **sparse clone/worktree** limited to `projects/ocpilot` (or narrower) rather than running from dirty main.

### Rules

- **Do not** point Windows Scheduled Tasks at `X:\AI MARS` for SITE-002 monitor while main worktree carries foreign WIP.
- **Do not** commit from runtime checkouts (detached HEAD); commit in authority worktree only.
- Production mutation from monitor: **forbidden** (read-only monitor).

---

## Related reports

- [MARS-INFRA-RUNTIME-SPLIT-SITE-002-01.md](reports/MARS-INFRA-RUNTIME-SPLIT-SITE-002-01.md)
- Audit: `X:\AI MARS STORAGE\mars-infrastructure\git-hygiene\MARS-GIT-TOPOLOGY-AND-RUNTIME-SAFETY-AUDIT-01\`
