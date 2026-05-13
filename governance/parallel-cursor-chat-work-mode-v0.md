# MARS — Parallel Cursor chat work mode (v0)

**Status:** **documented** — human operational discipline for **one** Cursor application, **one** repository root, **multiple** chats/tabs.  
**Version:** v0.

**Related:** [execution-model.md](execution-model.md), [../projects/mars-website-factory/first-operational-runbook-v0.md](../projects/mars-website-factory/first-operational-runbook-v0.md), [../agents/frontend-gulp-agent/workflow.md](../agents/frontend-gulp-agent/workflow.md).

---

## Purpose

Safe parallel work model for:

- **production execution** chats (frontend, delivery, workspaces), and  
- **MARS core** chats (governance, Website Factory, architecture, registries),

inside **one** Cursor application on the **same** working copy.

**Explicitly not in scope (this document does *not* define):**

- Runtime orchestration, process scheduling, or queue semantics.  
- Chat isolation, separate memory stores, or enforced separation of assistant context.  
- A scheduler or automatic lane routing.

**This *is*:** human operational discipline — naming chats, choosing paths, staging commits, and reporting in a way that **reduces accidental mixing** of lanes.

---

## Chat lanes

### Lane A — Production execution chat

**Purpose**

- Frontend implementation, landing pages, workspaces, build/debug, QA, project-specific delivery.

**Typical areas**

- `workspaces/*`  
- `projects/<client-project>/*` (delivery, handoffs, project-specific docs)  
- Design assets tied to implementation  
- Frontend source under an allowed project tree

**Forbidden (do not treat as in-lane without escalation)**

- Governance rewrites unrelated to the delivery slice.  
- MARS architecture refactors, registry-wide normalization, broad semantic contract edits.  
- Ad-hoc runtime experiments under `mars-runtime/` unless the task is explicitly a **runtime** task.  
- Broad semantic changes outside the scoped handoff.

**Examples**

- Triumph manipulator landing (or other client landing) implementation.  
- Responsive fixes, partials/SCSS/SVG work, gulp/build verification.  
- Delivery QA and REPORT for the factory frontend lane.

---

### Lane B — MARS core chat

**Purpose**

- Governance, Website Factory packs, registries, contracts, semantics, runbooks, agent packs, architecture documentation.

**Typical areas**

- `governance/*`  
- `registry/*`  
- `agents/*`  
- `projects/mars-website-factory/*`  
- Architecture and workflow documentation (`workflows/`, `interfaces/`, etc., per task scope)

**Forbidden (wrong lane)**

- Production source edits under `workspaces/*` for delivery.  
- Client landing implementation and design production files, except where a **governance** task explicitly updates a doc-only path.  
- Routine editing of design assets for pixel implementation (that belongs in Lane A).

**Examples**

- Execution semantics, artifact bus, validation runtime **models** (documentation).  
- Operational templates, agent normalization, registry maintenance.

---

## Chat switch rules

Before **changing** which chat you treat as authoritative for the next edit batch:

1. Run `git status --short` (or `-uall` when untracked trees matter).  
2. **Classify** each changed path by lane (use the template under *Status classification*).  
3. State the **active lane** for the upcoming work (A or B, or Runtime when explicitly scoped).  
4. List **forbidden paths** for that lane and keep them out of scope for this session.

**If a production (Lane A) chat modified governance or core contracts without a charter:**

- **STOP.**  
- Classify as **STRUCTURE CHANGE** (or equivalent escalation label in your REPORT).  
- Require an explicit **HITL** decision before continuing.

**If a MARS core (Lane B) chat modified production implementation paths:**

- **STOP.**  
- Classify as **wrong-lane modification**; revert or hand off to Lane A with a clean scope.

---

## Commit lane rules

### MARS core commit

**Allowed**

- Governance docs, Website Factory documentation, agent packs, registries, semantics, runbooks — paths consistent with Lane B scope.

**Forbidden (unless explicitly re-scoped and approved)**

- Production frontend source under `workspaces/*`.  
- `dist/*` and generated build outputs (regenerate via pipeline; do not “fix” in governance commits).  
- Client design production assets.  
- `mars-runtime/*` **leftovers** unless the commit is an explicit **runtime** commit (see below).

---

### Production commit

**Allowed**

- Frontend source, project assets, `workspaces/*` changes, frontend QA notes, project-specific documentation tied to delivery.

**Forbidden**

- Governance rewrites, unrelated registry churn, unrelated Website Factory doc edits.  
- Accidental `mars-runtime/*` changes mixed into the same commit.

---

### Runtime commit

**Allowed only** when the task is explicitly **runtime-scoped**:

- `mars-runtime/*`, adapters, runtime tests tied to that task.

**Forbidden in the same commit**

- Production frontend paths, unrelated Website Factory documentation, unrelated governance — split commits or defer.

---

## Git safety rules (strict)

- Always run `git status` (short) **before** starting a batch of edits and **before** switching mental “lane.”  
- **Never** use `git add .`  
- **Never** use `git add -A`  
- **Never** use `git commit -a`  
- **Stage explicit paths only** (path-by-path or a small, reviewed list).  
- Before every commit, run:  
  `git diff --cached --name-only`  
  and verify every path matches the intended **commit lane**.  
- **Never** commit mixed lanes in a single commit.  
- **Never** stage runtime leftovers “because they were dirty” — either revert, stash with a named message, or commit under an explicit **runtime** commit after classification.  
- If the active lane is **unclear**: **STOP**, classify, then proceed.  
- If **another chat** may have touched files: rerun `git status` and `git log --oneline -3` before staging.

---

## Status classification (template)

Copy into your session REPORT or notes and fill in.

### Production lane

- path:  
- action:

### MARS core lane

- path:  
- action:

### Runtime lane

- path:  
- action:

### Legacy / leftovers

- path:  
- action:

### Unknown

- path:  
- action:

---

## REPORT format — Parallel chat lane check

When the user (or runbook) asks for a lane check REPORT, use:

`# REPORT — Parallel chat lane check`

Include:

1. Current `git status` (short; add `-uall` if untracked matter).  
2. Active lane (A / B / Runtime / mixed — if mixed, STOP and split).  
3. Files touched (or intended) in this session.  
4. Forbidden paths for that lane — confirm avoided.  
5. Lane classification (use the template above).  
6. Intended **commit lane** for the next commit (if any).  
7. Push status (not pushed / pushed to `origin/main` / N/A).  
8. Final `git status` after the operation.  
9. **SAFE UNKNOWN** / risks (hosting, CI, ambiguous ownership, etc.).

---

## Changelog (documentation)

| Version | Date       | Notes |
|---------|------------|--------|
| v0      | 2026-05-13 | Initial parallel chat lane model for one Cursor instance. |
