# Agent Operation Risk Classes (v1)

**Status:** **documented** — classification contract for Cursor AGENT and human-operated work on MARS.  
**Not:** automated risk scorer, policy engine, or runtime enforcement.

**Implements:** [destructive-operations-policy-v1.md](destructive-operations-policy-v1.md), [safe-execution-layer-v1.md](../protocols/safe-execution-layer-v1.md)  
**Protected zones:** [../registries/protected-zones-registry-v1.md](../registries/protected-zones-registry-v1.md)

---

## 1. Purpose

Assign every filesystem, git, or workspace operation a **risk class** before execution. Default when uncertain: **HIGH RISK** or **FORBIDDEN** — never downgrade silently.

---

## 2. Class summary

| Class | AGENT allowed | Mode | Human confirmation | Snapshot | Rollback plan |
|-------|---------------|------|--------------------|----------|---------------|
| **SAFE** | Yes | AGENT | No | No | No |
| **LOW RISK** | Yes | AGENT | No | Recommended | Optional |
| **MEDIUM RISK** | Yes, scoped | AGENT | Yes — scope lock | **Required** | Recommended |
| **HIGH RISK** | Limited | ASK or AGENT read-only | **Required** | **Required** | **Required plan** |
| **CRITICAL** | **No** | ASK / Human | **Required** | **Required** | **Required plan** |
| **FORBIDDEN** | **No** | Human only (if ever) | **Explicit written** | N/A | N/A |

---

## 3. SAFE

**Definition:** Read-only or single-file doc edits in non-protected paths with no shell mutation.

**Examples:**

- Read files under scoped task path
- `git status`, `git diff`, `git log`
- Edit one markdown file in `projects/mars-survivability/` when task scope lock lists it
- Lint/read-only analysis

**Allowed modes:** AGENT, ASK  
**AGENT allowed:** Yes  
**ASK only:** No  
**Human confirmation:** Not required (scope lock still required for AGENT)  
**Snapshot requirement:** No  
**Rollback requirement:** No  

---

## 4. LOW RISK

**Definition:** Bounded writes — explicit file list, no directory recursion, no shell delete.

**Examples:**

- Edit 1–5 known files under one workspace subdirectory
- Add new file under scoped `projects/mars-survivability/` path
- Single-file `git checkout -- <tracked-path>` restore
- Regenerate one build output when task explicitly allows

**Allowed modes:** AGENT  
**AGENT allowed:** Yes  
**ASK only:** No  
**Human confirmation:** Not required if scope lock lists paths  
**Snapshot requirement:** Recommended for workspace `src/` edits  
**Rollback requirement:** Optional — git revert sufficient for tracked files  

---

## 5. MEDIUM RISK

**Definition:** Multi-file edits, structural changes, or shell commands with bounded blast radius.

**Examples:**

- Refactor across one workspace `src/` tree (many files)
- Add/move files within one workspace (no delete-recreate)
- npm/gulp run in one workspace (may rewrite dist/)
- Bulk doc creation under one `projects/` subtree

**Allowed modes:** AGENT with scope lock  
**AGENT allowed:** Yes — **only** with full scope lock + human confirmation in task header  
**ASK only:** No  
**Human confirmation:** **Required** — operator must acknowledge path list and risk class  
**Snapshot requirement:** **Required** before first mutation  
**Rollback requirement:** Recommended — document restore path in REPORT  

---

## 6. HIGH RISK

**Definition:** Wide blast radius, recovery operations, cross-zone touches, or irreversible-adjacent ops.

**Examples:**

- Touching CRITICAL zone paths ([protected-zones-registry-v1.md](../registries/protected-zones-registry-v1.md))
- Mass search-replace across workspace or project
- Moving quarantine / recovery / snapshot trees
- Git stash pop affecting many files
- Recovery planning after incident (read-only AGENT OK; mutations human-led)

**Allowed modes:** ASK default; AGENT **read-only audit only** unless human explicitly scopes write  
**AGENT allowed:** Limited — no autonomous mutation  
**ASK only:** Preferred for planning  
**Human confirmation:** **Required** before any mutation  
**Snapshot requirement:** **Required**  
**Rollback requirement:** **Required** — written plan before execution  

---

## 7. CRITICAL

**Definition:** Operations that can destroy ecosystem SoT, governance truth, or multi-workspace integrity.

**Examples:**

- Bulk edits across `governance/`, `registry/`, `web-gpt-sources/`
- Modifying `AGENTS.md`, `.cursorrules` without explicit charter
- Snapshot delete or `_snapshots/` tree mutation
- Cross-workspace mass move
- Post-incident filesystem repair without quarantine protocol

**Allowed modes:** **Human primary**; ASK for analysis  
**AGENT allowed:** **No** for mutations — read-only audit at most  
**ASK only:** Yes for planning and diff review  
**Human confirmation:** **Required** — named operator + documented reason  
**Snapshot requirement:** **Required**  
**Rollback requirement:** **Required** — manifest + rollback log entry  

---

## 8. FORBIDDEN (agent — absolute deny)

**Definition:** Operations that caused or amplify survivability incidents. **Agent must refuse** regardless of user phrasing unless human provides `APPROVED:` line with exact command **and** all policy conditions met (rare).

### Mandatory FORBIDDEN operations

| ID | Operation | Class |
|----|-----------|-------|
| X-01 | **Recursive delete** (`Remove-Item -Recurse`, `rm -rf`, `rd /s`, etc.) | **FORBIDDEN** |
| X-02 | **Workspace delete + recreate** as recovery | **FORBIDDEN** |
| X-03 | **`git clean`** (any flags) by AGENT | **FORBIDDEN** |
| X-04 | **`git reset --hard`** by AGENT | **FORBIDDEN** |
| X-05 | Delete at repo root or drive root | **FORBIDDEN** |
| X-06 | Wildcard mass delete | **FORBIDDEN** |
| X-07 | Move/rename top-level ecosystem folders | **FORBIDDEN** |
| X-08 | `git push --force` to main/master | **FORBIDDEN** |
| X-09 | Agent recovery loops (delete → retry → delete) | **FORBIDDEN** |
| X-10 | Rebuild workspace from model memory without snapshot/git source | **FORBIDDEN** |
| X-11 | Recursive delete outside `workspaces/_sandbox/` | **FORBIDDEN** |
| X-12 | Pruning governance without explicit charter | **FORBIDDEN** |

**Allowed modes:** Human only — and only with snapshot + explicit approval  
**AGENT allowed:** **No**  
**ASK only:** N/A — refuse and report  
**Human confirmation:** Explicit written approval; still discouraged for X-01–X-03  
**Snapshot requirement:** Required if human proceeds  
**Rollback requirement:** Required plan; prefer quarantine over delete  

---

## 9. Escalation rules

1. If requested operation matches any **FORBIDDEN** row → halt, output `SECURITY RISK` or `NEED HUMAN APPROVAL`.  
2. If risk class ambiguous → classify as **HIGH RISK** minimum.  
3. If path touches CRITICAL zone → minimum **HIGH RISK**; default **CRITICAL** for writes.  
4. Never chain FORBIDDEN ops as "cleanup" after a failed MEDIUM RISK task.

---

## 10. Cross-reference to lanes

| Lane | Typical max class without extra approval |
|------|------------------------------------------|
| **A** (implementation) | MEDIUM RISK in one workspace |
| **B** (governance / survivability) | LOW RISK writes; MEDIUM with snapshot for structural doc packs |

---

## 11. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G0 operationalization with mandatory FORBIDDEN classes |

---

*End of Agent Operation Risk Classes v1.*
