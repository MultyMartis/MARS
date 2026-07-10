# MARS Git / Runtime Brief for Project Chats

**Document role:** Short reference for OCPilot, MetaBOT, WP Forge, Website Factory, iSEO, FP-0002 and other MARS project chats — **not** automated enforcement.  
**Last updated:** 2026-07-10 (`MARS-INFRA-RUNTIME-SPLIT-SITE-002-SCHEDULED-SPOTCHECK-01`)  
**Audit basis:** [MARS-GIT-TOPOLOGY-AND-RUNTIME-SAFETY-AUDIT-01](https://github.com/MultyMartis/MARS) (storage mirror under `X:\AI MARS STORAGE\mars-infrastructure\git-hygiene\`)

---

## 1. Current Git Model

| Concept | Path / rule |
|---------|-------------|
| **Main monorepo / Active Brain** | `X:\AI MARS` |
| **Canonical remote branch** | `origin/mars/canonical-post-recovery` |
| **Systems inside monorepo** | OCPilot, MetaBOT, WP Forge, Website Factory, iSEO, FP-0002 — folders in the same repo unless explicitly documented otherwise |
| **Independent Git repos by default** | **No** — they are not separate repositories |
| **Clean Git sync worktrees** | `X:\AI MARS STORAGE\git-sync-*\repo` — temporary clean trees for safe commit/push when main is dirty |
| **Runtime checkouts** | `X:\AI MARS STORAGE\runtime-checkouts\...` — clean pinned trees for scheduled/local runtime jobs |
| **Bulk storage** | `X:\AI MARS STORAGE\` — artifacts, secrets, evidence; not a second repo root |

---

## 2. Why foreign WIP appears

When Cursor opens `X:\AI MARS`, root `git status` sees **all** systems in the monorepo:

- modified tracked files from unrelated projects;
- hundreds of untracked files (e.g. `workspaces/website-factory-operations`, `.recovery-temp`, local tools);
- changes in OCPilot, MetaBOT, FP-0002, etc. in one porcelain view.

Project chats scoped to one system still inherit this noise if the workspace root is the full monorepo. **This is expected monorepo behavior**, not proof that your task dirtied unrelated paths.

---

## 3. What is NOT the main problem

| Misconception | Reality (audit 2026-07-10) |
|---------------|----------------------------|
| "Nested Git repos absorbed everything" | **Secondary** — one known nested repo: `workspaces/isbd-care-landing` (gitignored). No `.gitmodules`, no submodules. |
| "WP Forge / OCPilot are separate repos" | **No** — monorepo folders only. |
| "Foreign WIP = my chat broke Git" | Usually **unrelated** paths; treat as out-of-scope unless your task charter touched them. |
| "Run scheduled jobs from main" | **Forbidden** when main carries foreign WIP — use runtime checkout. |

---

## 4. Runtime checkout policy

Scheduled and unattended local jobs **must not** execute from dirty `X:\AI MARS`.

| Job type | Pattern |
|----------|---------|
| SITE-002 post-1C monitor | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` |
| Task Scheduler action + WorkingDirectory | Both must point to runtime checkout, not main |
| Commits / doc updates | Authority worktree e.g. `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Artifacts | Under `X:\AI MARS STORAGE\ocpilot\...` (outside Git) |

**Update runtime checkout:** fetch in authority worktree → `git checkout <sha>` in runtime checkout → dry-run runner → optional manual verify → record infra report. See [runtime-checkouts.md](runtime-checkouts.md).

---

## 5. Rules for project chats

1. **Scope:** Only touch paths in the task charter. Ignore unrelated `M` / `??` in root status.
2. **Do not clean foreign WIP:** no `git stash`, `git restore`, `git clean`, `git reset` on main for "cleanup".
3. **Staging:** exact allowlist only — never `git add .` or `git add -A`.
4. **Commits:** prefer clean authority worktree when main is dirty.
5. **Runtime jobs:** if a new scheduled job is needed, create a **clean runtime checkout** — do not point Task Scheduler at `X:\AI MARS`.
6. **Truth:** distinguish documented architecture vs planned implementation vs legacy imported material.

---

## 6. SITE-002 current status

| Field | Value (2026-07-10 spotcheck) |
|-------|------------------------------|
| Scheduled task | `MARS_SITE_002_Post_1C_Catalog_Monitor` |
| Runtime checkout | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` @ `bd3021bf` |
| Scheduler points to main | **No** (detached in Run 4.257) |
| Latest run folder | `2026-07-10_20-17-16` (manual post-split verify) |
| Natural scheduled run after split | **Pending** — next `2026-07-11 12:30 +07` |
| onboarding_needs_count | **0** |
| classification | **HYGIENE_REVIEW_REQUIRED** |
| Production mutation | **0** |

Reports: [MARS-INFRA-RUNTIME-SPLIT-SITE-002-01](reports/MARS-INFRA-RUNTIME-SPLIT-SITE-002-01.md) · [scheduled spotcheck](reports/MARS-INFRA-RUNTIME-SPLIT-SITE-002-SCHEDULED-SPOTCHECK-01.md)

---

## 7. Forbidden broad Git operations

On `X:\AI MARS` (especially when dirty):

- `git add .` / `git add -A`
- `git clean` (any variant)
- `git reset --hard`
- `git stash` / `git restore` for foreign WIP
- `git pull` without explicit charter and preflight
- force push
- broad staging of unrelated paths

MARS selective staging contract overrides generic Cursor habits.

---

## 8. What to do when foreign WIP appears

1. **Read** `git status --short` but **filter** to your task paths only.
2. **Confirm** branch = `mars/canonical-post-recovery` (or task-authorized branch).
3. **Use** `X:\AI MARS STORAGE\git-sync-e01\repo` (or e01/e02 pattern) for docs-only commits when main is unsafe.
4. **Record** foreign WIP as out-of-scope in your report; do not delete or reset it.
5. **Escalate** only if your task paths are blocked by conflicts — not because unrelated workspaces show `??`.
6. **For runtime:** verify Task Scheduler uses `runtime-checkouts\...`, not main.

---

## Related documents

- [runtime-checkouts.md](runtime-checkouts.md)
- [governance/mars-x-drive-root-authority-v1.md](../../governance/mars-x-drive-root-authority-v1.md)
- Storage audit: `X:\AI MARS STORAGE\mars-infrastructure\git-hygiene\MARS-GIT-TOPOLOGY-AND-RUNTIME-SAFETY-AUDIT-01\`
