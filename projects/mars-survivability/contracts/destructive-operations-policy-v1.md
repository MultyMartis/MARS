# Destructive Operations Policy (v1)

**Status:** **documented** — normative contract for human and Cursor-agent work on MARS.  
**Enforcement:** **human-operated** + future GitGuard/helpers — **no** automated deny engine claimed in-repo.

**Supersedes nothing** — complements [AGENTS.md](../../../AGENTS.md), [.cursorrules](../../../.cursorrules), [tool-safety-model-v0.md](../../../tools/tool-safety-model-v0.md).

---

## 1. Scope

Applies to:

- Cursor **AGENT** mode sessions on MARS  
- Helper scripts under `tools/` invoked by humans or agents  
- Website Factory / ORCA / workspace maintenance  
- Git operations with irreversible or hard-to-reverse effects  

---

## 2. Definitions

| Term | Meaning |
|------|---------|
| **Destructive operation** | Any action that removes, irreversibly overwrites, or mass-moves data such that recovery requires backup, git object recovery, or cannot be guaranteed. |
| **Scope lock** | Explicit allowlist of absolute paths and operation types in the task header. |
| **Quarantined cleanup** | Deletes confined to a disposable directory (e.g. `workspaces/_sandbox/`, temp export dirs) with snapshot taken. |
| **Human-confirmed** | Operator types explicit approval **after** seeing path list and operation class — not implied by “fix it”. |

---

## 3. FORBIDDEN (agent — default deny)

Unless **all** of: (a) explicit human instruction naming paths, (b) scope lock in prompt, (c) snapshot plan executed — agent **must not**:

| ID | Operation |
|----|-----------|
| F-01 | Recursive directory delete via agent (Shell `Remove-Item -Recurse`, `rm -rf`, `rd /s`, etc.) |
| F-02 | Delete at **volume root** (`X:\`) or **canonical root directories** (`X:\AI MARS\`, `X:\AI MARS STORAGE\`, `X:\MARS-Localhost\`) wholesale |
| F-03 | Wildcard mass delete (`del *.*`, `Remove-Item * -Recurse`, `git clean -fdx` without human at keyboard) |
| F-04 | **Move/rename** top-level folders: `governance/`, `registry/`, `projects/`, `agents/`, `workspaces/`, `web-gpt-sources/` |
| F-05 | `git clean` (any flags) initiated by **AGENT** |
| F-06 | `git reset --hard` initiated by **AGENT** |
| F-07 | `git push --force` to `main`/`master` (already in user rules; restated) |
| F-08 | Mass search-replace across repo **without** path glob lock and dry-run review |
| F-09 | Auto-generated “cleanup” scripts executed without human review of script body |
| F-10 | **Delete workspace + recreate** as recovery strategy |
| F-11 | `Remove-Item -Recurse` (or equivalent) **outside** a declared sandbox path |
| F-12 | Deleting “unused” files by model heuristic without inventory manifest |
| F-13 | Deleting `node_modules/`, `dist/`, `build/` **when** task forbids touching build outputs — use regen pipeline instead |
| F-14 | Pruning governance or registry docs without explicit charter (aligns with maintenance mode) |

**Agent interpretation rule:** If unsure whether an operation is destructive → treat as **FORBIDDEN** and report **NEED HUMAN APPROVAL**.

---

## 4. ALLOWED (with conditions)

| ID | Operation | Conditions |
|----|-----------|------------|
| A-01 | Human-confirmed local delete | Human names file(s); agent may assist **single-file** delete only after confirmation |
| A-02 | Scoped file replacement | One file or explicit list; no directory recursion |
| A-03 | Quarantined cleanup | Under `workspaces/_sandbox/` or operator-created quarantine dir; snapshot first |
| A-04 | Sandbox workspaces | All destructive tests only inside sandbox; never default cwd = repo root |
| A-05 | Snapshot-first operations | Documented snapshot path + timestamp before any A-02/A-03 |
| A-06 | Git restore of **tracked** file | `git checkout -- <path>` for known tracked path — not mass |
| A-07 | Truncate/regen **generated** output | Only when task explicitly allows and path is under declared build output dir |
| A-08 | Doc-only deletion | Explicit user instruction + lifecycle note per [mars-lightweight-maintenance-mode-v0.md](../../../governance/mars-lightweight-maintenance-mode-v0.md) |

---

## 5. Git-specific rules (agent)

| Command | Agent |
|---------|-------|
| `git status`, `git diff`, `git log` | Allowed (read) |
| `git add` + `git commit` | Only when user **explicitly** requests commit |
| `git stash` | Allowed with scope; prefer human for pop |
| `git clean` | **FORBIDDEN** (F-05) |
| `git reset --hard` | **FORBIDDEN** (F-06) |
| `git push` | Only when user explicitly requests |
| `git push --force` | **FORBIDDEN** unless explicit user request + warning |

---

## 6. PowerShell / shell discipline

- **Prefer** `Get-ChildItem` / list before any mutation.  
- **Never** chain `cd` + recursive delete without echoing **full absolute path** in REPORT.  
- **Default cwd** for risky work: narrowest subdirectory, not repo root.  
- **Forbidden:** running cleanup one-liners from Web without pasting into review buffer first.

---

## 7. Website Factory cross-reference

Reconstruction/resets: [workspace-reset-governance.md](../../../projects/mars-website-factory/workspace-reset-governance.md) — audit before cleanup; this policy **forbids** agent-initiated destructive cleanup.

Emergency production rules: [../protocols/website-factory-safe-production-rules-v1.md](../protocols/website-factory-safe-production-rules-v1.md).

---

## 8. Signals

| Signal | When |
|--------|------|
| **NEED HUMAN APPROVAL** | Any operation in gray zone; path list longer than 3 items |
| **SECURITY RISK** | Suspected scope escape, root-level paths, or delete outside lock |
| **SAFE UNKNOWN** | Cannot verify path exists / is in scope — **do not act** |

---

## 9. Violation handling (operator)

1. Stop agent session.  
2. Assess git + filesystem recovery (do not run further agent cleanup).  
3. File incident note under `projects/mars-survivability/reports/`.  
4. Add scope lock to all future AGENT prompts for 48h minimum.

---

## 10. Changelog

| Date | Change |
|------|--------|
| 2026-05-23 | v1 — initial policy after context-drift incident audit |

---

*End of Destructive Operations Policy v1.*
