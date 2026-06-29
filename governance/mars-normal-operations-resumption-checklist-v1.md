# MARS — Normal operations resumption checklist v1

**Status:** **documented** — operator checklist after disaster-recovery closure.  
**Authority:** [mars-disaster-recovery-2026-06-24-closure-v1.md](mars-disaster-recovery-2026-06-24-closure-v1.md)  
**Is not:** automated enforcement or CI gate.

---

## Before opening Cursor

- [ ] Open workspace root: `X:\AI MARS`
- [ ] Confirm volume label when checkable: `Get-Volume -DriveLetter X` → **AI WS**
- [ ] Confirm branch: `git branch --show-current` → `mars/canonical-post-recovery`
- [ ] Confirm clean tracked index or known local-only untracked only: `git status --short`
- [ ] Confirm HEAD matches expected canonical checkpoint when starting a major task: `git rev-parse HEAD`
- [ ] Do **not** open `C:\AI MARS`, `C:\MARS Phenix\_legacy-hold`, or `C:\this is backUP AI MARS 23.06.2026` as active development workspace

---

## Before project work

- [ ] Identify parent Web-GPT / project chat for the task (pack OPERATIONAL-INDEX or project README)
- [ ] Check [registry/project-registry.md](../registry/project-registry.md) for `project_id` and boundaries
- [ ] Check active roadmap/state (pack OPERATIONAL-INDEX, OCPILOT-STATE, or project STATE doc)
- [ ] Create task-specific Git checkpoint before large or risky work (scoped commit)
- [ ] Verify runtime boundary: brain at `X:\AI MARS`; execution at `X:\MARS-Localhost` when applicable

---

## Before filesystem commands

- [ ] Validate exact path — allowed roots: `X:\AI MARS` (tracked work), `X:\AI MARS STORAGE\`, `X:\MARS-Localhost\` (when chartered)
- [ ] Confirm operation is not delete, move, mirror, purge, or unrestricted copy without charter
- [ ] Run dry-run or list-only preview when tooling supports it
- [ ] No `insecure_none` or unrestricted sandbox bypass without explicit operator approval
- [ ] Legacy trees (`C:\AI MARS`, `C:\AI MARS STORAGE`, `_legacy-hold`, original backup) are **read-only** unless separately chartered

---

## Before commit

- [ ] Use exact allowlist staging — **never** `git add .`, `git add -A`, or `git commit -a`
- [ ] Review staged diff: `git diff --cached`
- [ ] No unrelated WIP in scope
- [ ] No secrets, tokens, or credentials
- [ ] No deletions unless separately approved and documented
- [ ] Report title format when applicable: `# REPORT — <task/stage name>`

---

## Before runtime

- [ ] Confirm correct runtime root (`X:\MARS-Localhost` for MLI consumers)
- [ ] No production target unless explicitly chartered
- [ ] Do not auto-start services in closure or routine doc tasks
- [ ] Backup/checkpoint for destructive or large runtime changes
- [ ] Operator-visible receipt for runtime mutations

---

## End of task

- [ ] Publish task report with changed files, summary, git status, UNKNOWN/SECURITY if any
- [ ] Update project map/registry/OPERATIONAL-INDEX when task changes project state
- [ ] Commit and push at major checkpoint (not required for every small doc tweak)
- [ ] Record next safe action in report or pack STATE doc

---

## Git workflow reminders

| Item | Rule |
|------|------|
| Canonical branch | `mars/canonical-post-recovery` |
| Recovery branch | `recovery/mars-phenix-2026-06-25` — immutable, no new development |
| Feature branches | Create from canonical branch only when needed |
| Legacy forward | `mars/post-cycle8-live-tests` — **DO NOT MERGE** |
| Force-push | **Prohibited** |

---

## Quick preflight (copy/paste)

```text
git branch --show-current
git status --short
git rev-parse HEAD
```

Expected branch: `mars/canonical-post-recovery`  
Expected workspace: `X:\AI MARS`

**X-drive authority:** [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md). Post–X9 closure (2026-06-29): canonical roots on volume **AI WS** (`X:`).

---

*Checklist v1 — post disaster-recovery closure 2026-06-25.*
