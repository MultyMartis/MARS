# 09 — Git and REPORT discipline (migration v0)

---

## Git safety (summary)

- Work only under agreed repo root (`C:\AI MARS` per project rules).  
- **Default:** no commit, no push (`AGENTS.md`).  
- **Never:** `git add .`, `git add -A`, `git commit -a` (`governance/parallel-cursor-chat-work-mode-v0.md`).  
- **Always:** explicit paths; `git diff --cached --name-only` before commit; **single lane** per commit.  
- **Runtime leftovers:** do not stage “because dirty” — revert, named stash, or **runtime-only** commit after explicit scope.

## Staging rules

1. `git status --short` (add `-uall` when untracked trees matter).  
2. Classify each path: Production / MARS core / Runtime / Legacy / Unknown.  
3. Stage **only** paths matching the active commit lane.  
4. Re-verify staged list.

## Commit lane rules (three buckets)

| Commit type | Allowed paths |
|-------------|----------------|
| **MARS core** | `governance/`, `registry/`, `agents/` (packs/cards), `projects/mars-website-factory/`, architecture docs per scope — **not** `workspaces/*`, **not** casual `mars-runtime/*` |
| **Production** | `workspaces/*`, project delivery docs, frontend sources — **not** broad governance rewrites, **not** `dist` as manual fix |
| **Runtime** | `mars-runtime/*` only when task is runtime-scoped |

## REPORT structure

**Required heading:** `# REPORT — <task/stage name>`

**Typical body (task closeout):**

1. **Changed files** (list).  
2. **Summary** (what / why, plain language).  
3. **`git status`** (short; `-uall` if untracked relevant).  
4. **UNKNOWN** / **SECURITY RISK** (if any).  
5. **GIT CHECKPOINT NEEDED** — only when `web-gpt-sources/04-workflows__git-rules.md` criteria met; else **omit**.

**Parallel lane check variant:** see `governance/parallel-cursor-chat-work-mode-v0.md` (active lane, forbidden paths, intended commit lane, push status).

## Push discipline

- Push only on **user request** or explicit milestone agreement — not agent default.

## Lane isolation

- Cross-lane edits → STOP, escalate, HITL (`parallel-cursor-chat-work-mode-v0.md`).

## Runtime exclusion discipline

- Production commits **must not** include `mars-runtime/*` noise.  
- Governance commits **must not** include `workspaces/*` implementation.

---

## Canonical REPORT skeleton (copyable)

```markdown
# REPORT — <task/stage name>

## Changed files
- path/to/file
- ...

## Summary
<complete sentences: what changed and why>

## Git status
<paste output of: git status --short -uall>

## UNKNOWN / SECURITY RISK
- <item or "None">

## GIT CHECKPOINT NEEDED
<Omit | YES with rationale per git-rules | NO GIT CHECKPOINT>
```

---

## References

- `AGENTS.md`  
- `web-gpt-sources/04-workflows__git-rules.md`  
- `governance/parallel-cursor-chat-work-mode-v0.md`
