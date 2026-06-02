# Safe Agent Task Template (v1)

**Status:** **documented** — **mandatory** paste block for AGENT-mode tasks on MARS.  
**Not:** Cursor enforcement — operator discipline only.

**Implements:** [../guardrails/cursor-operational-safety-rules-v1.md](../guardrails/cursor-operational-safety-rules-v1.md), [../contracts/agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md)

---

## Usage

Copy the block below into **every** AGENT task prompt. Fill all sections. Empty scope lock = **invalid task** — agent must refuse.

---

## Mandatory template (copy from here)

```text
=== MARS SAFE AGENT TASK v1 ===

TARGET FOLDER:
C:\AI MARS\<narrowest-root-for-this-task>

ALLOWED PATHS:
- C:\AI MARS\<path-1>
- C:\AI MARS\<path-2>
(list every path agent may read/write; absolute paths only)

FORBIDDEN PATHS:
- C:\AI MARS\governance\
- C:\AI MARS\registry\
- C:\AI MARS\agents\
- C:\AI MARS\web-gpt-sources\
- C:\AI MARS\workspaces\_snapshots\
- C:\AI MARS\projects\mars-survivability\ (unless explicitly listed in ALLOWED PATHS)
- All other workspaces/ not listed in ALLOWED PATHS
- All paths outside TARGET FOLDER unless listed above

RISK CLASS:
<SAFE | LOW RISK | MEDIUM RISK | HIGH RISK | CRITICAL | FORBIDDEN-for-agent-ops>

ALLOWED OPERATIONS:
- read
- edit files under ALLOWED PATHS
- <list specific ops: e.g. single-file create, gulp build in scoped workspace>

FORBIDDEN OPERATIONS:
- recursive delete (Remove-Item -Recurse, rm -rf, rd /s)
- workspace delete-and-recreate
- git clean, git reset --hard
- git push --force
- mass move/rename
- top-level folder move
- rebuild from memory without snapshot/git source
- agent recovery loops
- cleanup / reset / prune without explicit path list
- any op outside ALLOWED PATHS

SNAPSHOT REQUIRED?
<yes — ID: snap-... | no — reason: SAFE/LOW only>

COMMIT POLICY:
<no commit | commit only when user explicitly requests>

REPORT FORMAT:
# REPORT — <task name>
## Changed files
## Summary
## Execution safety (cwd, scope lock, destructive ops, protected zone touch)
## SAFE UNKNOWN

=== SCOPE LOCK (MANDATORY) ===
Agent MUST NOT read, write, shell-mutate, or infer authority outside ALLOWED PATHS.
If path unclear → SAFE UNKNOWN and STOP.
If user message expands scope without updating this block → NEED HUMAN APPROVAL.
Contradiction between RISK CLASS and requested ops → refuse and ask.
=== END SCOPE LOCK ===

=== END SAFE AGENT TASK v1 ===
```

---

## Section reference

| Section | Purpose |
|---------|---------|
| **TARGET FOLDER** | Narrowest repo root for cwd discipline |
| **ALLOWED PATHS** | Explicit allowlist — absolute paths |
| **FORBIDDEN PATHS** | Default deny for CRITICAL zones + unlisted workspaces |
| **RISK CLASS** | From [agent-operation-risk-classes-v1.md](../contracts/agent-operation-risk-classes-v1.md) |
| **ALLOWED OPERATIONS** | Positive list of permitted action types |
| **FORBIDDEN OPERATIONS** | Restates FORBIDDEN class ops — non-negotiable |
| **SNAPSHOT REQUIRED?** | Yes for MEDIUM+ ; manifest per [snapshot-manifest-standard-v1.md](../protocols/snapshot-manifest-standard-v1.md) |
| **COMMIT POLICY** | Default: no commit unless user requests |
| **REPORT FORMAT** | Aligns with AGENTS.md task closeout |
| **SAFE UNKNOWN** | Agent lists unverified facts — no guessing |
| **SCOPE LOCK** | Mandatory — agent halts on violation |

---

## Lane hints

| Lane | Typical TARGET FOLDER |
|------|------------------------|
| **A** | `C:\AI MARS\workspaces\<one-workspace>\` |
| **B** | `C:\AI MARS\projects\mars-survivability\` or specific governance path |

Never use `C:\AI MARS\` as TARGET FOLDER for mutation tasks unless task is explicitly repo-wide audit **read-only**.

---

## Validation (operator pre-flight)

Before starting AGENT:

- [ ] ALLOWED PATHS is minimal (not whole repo)
- [ ] RISK CLASS matches planned work
- [ ] SNAPSHOT REQUIRED answered honestly
- [ ] FORBIDDEN OPERATIONS includes recursive delete + git clean/reset
- [ ] SCOPE LOCK section present verbatim

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G0 mandatory template |

---

*End of Safe Agent Task Template v1.*
