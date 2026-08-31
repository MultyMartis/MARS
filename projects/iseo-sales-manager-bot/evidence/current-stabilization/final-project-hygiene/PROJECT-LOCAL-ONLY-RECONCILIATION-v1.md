# PROJECT LOCAL-ONLY RECONCILIATION v1

Dirty main `X:\AI MARS` project locus reviewed (status scoped to `projects/iseo-sales-manager-bot` + two governance audits).

## Classification of local-only / dirty entries

| Item | Class | Action this wave |
|---|---|---|
| `reports/REPORT-...-storage-hygiene-loss-assessment-v1.md` | `CANONICALIZE_NOW` | Commit |
| `reports/REPORT-...-targeted-storage-loss-forensics-v1.md` | `CANONICALIZE_NOW` | Commit |
| `governance/audits/ISEO-SALES-MANAGER-BOT-storage-hygiene-loss-assessment-2026-08-31.md` | `CANONICALIZE_NOW` | Commit (charter-authorized) |
| `governance/audits/ISEO-SALES-MANAGER-BOT-targeted-storage-loss-forensics-2026-08-31.md` | `CANONICALIZE_NOW` | Commit (charter-authorized) |
| Final hygiene REPORT + `evidence/.../final-project-hygiene/**` | `CANONICALIZE_NOW` | Commit |
| Untracked soak packs (`final-48h-soak*`) + older 20260816/17 evidence/reports | `SUPERSEDED_DO_NOT_COMMIT` / historical local | Document only; PII/soak risk; not required for Stable Git of current production patches |
| Modified architecture/implementation/README/OPERATIONAL-INDEX (dirty main `M`) | Foreign/historical dirty on shared brain | **Do not stage** (foreign WIP preserve) |
| Worktree-only `reminder-final-natural-acceptance` pack | `DIRTY_WIP_DO_NOT_TOUCH` | Incomplete WAITING stub; keep local |

## Counts

| Metric | Value |
|---:|---:|
| Local-only project files/dirs reviewed (status groups) | **38+** status lines under project + 2 governance audits |
| Canonicalized this wave (planned) | storage-loss ×2 reports, governance ×2 audits, hygiene report+evidence |
| Left local intentionally | soak packs, historical untracked evidence, dirty `M` docs, natural WIP worktree |
