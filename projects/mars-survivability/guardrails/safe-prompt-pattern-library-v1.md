# Safe Prompt Pattern Library (v1)

**Status:** **documented** — operator reference for AGENT task phrasing.  
**Not:** NLP classifier, prompt firewall, or automated detection product.

**Halt on unsafe:** [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md)  
**Enforcement registry:** [enforcement-rules-registry-v1.md](../registries/enforcement-rules-registry-v1.md)

---

## 1. SAFE patterns

### 1.1 Scoped replace

| Field | Value |
|-------|-------|
| **Pattern** | "Replace `<exact string>` with `<exact string>` in `C:\AI MARS\<path>\file.ext` only" |
| **Risk** | LOW — bounded single file |
| **AGENT allowed?** | Yes — with scope lock |
| **Snapshot required?** | No (LOW); yes if part of MEDIUM+ batch |

**Safer alternative:** List every file path explicitly.

---

### 1.2 Additive changes

| Field | Value |
|-------|-------|
| **Pattern** | "Add new file `path/to/file.md` under ALLOWED PATHS; do not modify existing files" |
| **Risk** | LOW |
| **AGENT allowed?** | Yes |
| **Snapshot required?** | No |

**Safer alternative:** Specify exact content source (template, copy from).

---

### 1.3 Clone-first

| Field | Value |
|-------|-------|
| **Pattern** | "Copy `workspaces/foo-v4/` to `workspaces/_sandbox/exp-<date>-foo/`; experiment only in sandbox copy" |
| **Risk** | LOW in sandbox |
| **AGENT allowed?** | Yes — copy only; no delete source |
| **Snapshot required?** | Recommended before copy if source is production |

**Safer alternative:** Document source SHA in REPORT.

---

### 1.4 Snapshot-first

| Field | Value |
|-------|-------|
| **Pattern** | "Create snapshot per manifest standard, then refactor `src/scss/` under one workspace" |
| **Risk** | MEDIUM — controlled with snapshot |
| **AGENT allowed?** | Yes — after snapshot id recorded |
| **Snapshot required?** | **Yes** — mandatory |

**Safer alternative:** Human creates snapshot; AGENT references `snap-...` id in task.

---

### 1.5 Read-only audit

| Field | Value |
|-------|-------|
| **Pattern** | "Audit links in `projects/mars-survivability/` — read only, no writes" |
| **Risk** | SAFE |
| **AGENT allowed?** | Yes |
| **Snapshot required?** | No |

**Safer alternative:** Explicit FORBIDDEN OPERATIONS list in task block.

---

### 1.6 Sandbox experiments

| Field | Value |
|-------|-------|
| **Pattern** | "Run drill D-01 in `workspaces/_sandbox/exp-<date>-drill/` only" |
| **Risk** | LOW in sandbox |
| **AGENT allowed?** | Yes — scoped to sandbox |
| **Snapshot required?** | Yes before simulated failure step |

**Safer alternative:** Reference [recovery-drill-protocol-v1.md](../protocols/recovery-drill-protocol-v1.md).

---

## 2. UNSAFE patterns

### 2.1 Cleanup repo

| Field | Value |
|-------|-------|
| **Pattern** | "Clean up the repo" / "Clean everything" |
| **Risk** | **CRITICAL** — unbounded delete scope |
| **AGENT allowed?** | **No** — halt |
| **Snapshot required?** | N/A — refuse first |

**Safer alternative:** "List candidates in `<path>` for human review; do not delete."

---

### 2.2 Rebuild workspace

| Field | Value |
|-------|-------|
| **Pattern** | "Rebuild the workspace" / "Rebuild from scratch" |
| **Risk** | **FORBIDDEN** — F-10 delete-recreate |
| **AGENT allowed?** | **No** |
| **Snapshot required?** | N/A |

**Safer alternative:** Quarantine → restore from snapshot/git → parity diff.

---

### 2.3 Remove broken files

| Field | Value |
|-------|-------|
| **Pattern** | "Remove broken files" / "Delete unused files" |
| **Risk** | **HIGH** — heuristic deletion F-12 |
| **AGENT allowed?** | **No** without inventory |
| **Snapshot required?** | Yes if human proceeds |

**Safer alternative:** "Produce inventory manifest; human marks deletions."

---

### 2.4 Start from scratch

| Field | Value |
|-------|-------|
| **Pattern** | "Start from scratch" / "Start fresh" |
| **Risk** | **FORBIDDEN** — scope expansion to wipe |
| **AGENT allowed?** | **No** |
| **Snapshot required?** | N/A |

**Safer alternative:** Clone-first to new `-vN` or sandbox copy.

---

### 2.5 Recreate project

| Field | Value |
|-------|-------|
| **Pattern** | "Recreate the project" / "Recreate workspace" |
| **Risk** | **FORBIDDEN** — F-10 |
| **AGENT allowed?** | **No** |
| **Snapshot required?** | N/A |

**Safer alternative:** Template clone from `_template-client-v1` with documented lineage.

---

### 2.6 Wipe dist

| Field | Value |
|-------|-------|
| **Pattern** | "Wipe dist" / "Delete dist and rebuild" |
| **Risk** | MEDIUM–HIGH — may confuse dist vs src SoT |
| **AGENT allowed?** | Only with explicit path + gulp regen plan |
| **Snapshot required?** | Yes if deploy-critical dist |

**Safer alternative:** "Run gulp build in scoped workspace; do not delete `src/`."

---

### 2.7 Delete old versions

| Field | Value |
|-------|-------|
| **Pattern** | "Delete old versions" / "Remove v3/v4" |
| **Risk** | **HIGH** — unlisted paths |
| **AGENT allowed?** | **No** without explicit path list + human approval |
| **Snapshot required?** | Yes |

**Safer alternative:** "Move to `_quarantine/` with manifest" — human executes move.

---

### 2.8 Fresh rebuild

| Field | Value |
|-------|-------|
| **Pattern** | "Fresh rebuild" / "Rebuild from memory" |
| **Risk** | **FORBIDDEN** — X-10 rebuild-from-memory |
| **AGENT allowed?** | **No** |
| **Snapshot required?** | N/A |

**Safer alternative:** Restore from `src/` + handoff + design authority only.

---

### 2.9 Mass refactor without scope

| Field | Value |
|-------|-------|
| **Pattern** | "Refactor the codebase" / "Modernize everything" |
| **Risk** | **HIGH** — F-08 |
| **AGENT allowed?** | **No** without path glob + file list |
| **Snapshot required?** | Yes |

**Safer alternative:** One subdirectory per task; pilot file list in ALLOWED PATHS.

---

## 3. Quick reference matrix

| Pattern class | AGENT | Snapshot | Typical signal |
|---------------|-------|----------|----------------|
| SAFE (read-only audit) | Yes | No | — |
| SAFE (additive, scoped) | Yes | Optional | — |
| MEDIUM (multi-file, scoped) | Yes + lock | **Yes** | — |
| UNSAFE (cleanup/wipe/fresh) | **No** | N/A | HALT |
| UNSAFE (delete-recreate) | **No** | N/A | SECURITY RISK |
| UNSAFE (rebuild-from-memory) | **No** | N/A | SAFE UNKNOWN |

---

## 4. Task template integration

Paste [safe-agent-task-template-v1.md](../templates/safe-agent-task-template-v1.md) and map user intent to patterns above **before** starting AGENT.

---

## 5. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G1 safe/unsafe prompt library |

---

*End of Safe Prompt Pattern Library v1.*
