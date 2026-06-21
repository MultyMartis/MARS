# MARS Website Factory - Workspace Reset Governance

**Status:** **documented** - Website Factory workspace reset governance, **Workspace Archive Rule**, and human-supervised residue discipline only.  
**Not:** automatic cleaner, git reset policy, destructive command approval, runtime workspace manager, or build artifact deletion engine.

**Core principle:** stale implementation state is not neutral.  
Residue from earlier attempts can silently become architecture.

**Related layers:** [initialization-governance.md](initialization-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [failure-recovery-governance.md](failure-recovery-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [knowledge-provenance-governance.md](knowledge-provenance-governance.md).  
**Forge findings category:** `WORKSPACE RESET FINDINGS`.

---

## 1. Purpose

Workspace Reset Governance defines how operators recognize, document, and contain stale implementation cleanup needs before reconstruction or scoped repair.

It covers:

- stale implementation cleanup;
- reconstruction residue;
- orphaned imports;
- deprecated partial cleanup;
- frozen-state reset;
- workspace survivability;
- reset traceability;
- implementation residue drift.

It does not authorize deletion or moving files by itself. Cleanup remains project-specific and must follow repo rules and explicit user instruction when destructive.

---

## 2. Reset Model

| Reset concern | Governance read |
|---------------|-----------------|
| **Stale implementation cleanup** | Old code paths are identified before they influence new work. |
| **Reconstruction residue** | Prior rebuild attempts are classified as active, deprecated, temporary, or unknown. |
| **Orphaned imports** | Includes, SCSS imports, JS hooks, and asset references are checked for abandoned ownership. |
| **Deprecated partial cleanup** | Removed or replaced sections are not left as hidden alternatives without traceability. |
| **Frozen-state reset** | Previously frozen claims are reopened only with explicit reason and affected scope. |
| **Reset traceability** | Operators can explain what was cleaned, what remains, and what is intentionally parked. |

---

## 3. Canonical Rules

- Audit before cleanup: name residue before removing, replacing, or ignoring it.
- Never delete or move files without explicit authority.
- Do not import deprecated partials “just in case.”
- Do not keep old hero/header/background logic as hidden fallback during a clean reconstruction.
- Treat orphaned imports and dead hooks as implementation reliability risks.
- Record reset findings when cleanup, residue, or frozen-state reopening affects confidence.

---

## 4. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Residue inheritance** | Old implementation quietly defines the new architecture. |
| **Zombie partials** | Deprecated includes remain reachable and confuse ownership. |
| **Orphaned import tolerance** | Unused imports hide stale CSS/JS behavior or future coupling. |
| **Destructive cleanup by impulse** | Files are removed before authority and rollback implications are understood. |
| **Frozen-state amnesia** | A reset invalidates freeze claims without recording scope. |
| **Cleanup theater** | Operators say “cleaned” without traceable evidence of what changed. |

---

## 5. Drift Patterns

- **Implementation residue drift** - stale code shapes current behavior without being active authority.
- **Reset opacity drift** - future operators cannot tell what was reset or why.
- **Orphan dependency drift** - abandoned imports, hooks, or assets remain coupled to active pages.
- **Deprecated partial drift** - old partials survive as misleading alternatives.

---

## 6. Triumph V3 Lesson

Triumph V3 exposed stale hero rebuild contamination: prior first-screen attempts and partial logic can distort a clean rebuild even when the operator intends to start fresh.

The governance lesson is to audit and classify residue before reconstruction. This is not an instruction to delete files automatically.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| A file appears unused but ownership is unclear | Cleanup may remove live behavior. |
| Prior implementation attempts are not documented | Cannot tell active baseline from rejected residue. |
| Import graph is unclear | Stale styles or hooks may still affect runtime output. |
| Frozen state predates reset | Cannot prove current freeze claims still apply. |
| Cleanup requires destructive file operations | Requires explicit user or project authority. |

**Action:** classify as active / deprecated / temporary / orphan / unknown, then request authority before destructive cleanup.

---

## 8. Workspace Archive Rule

When a **frontend production cycle is fully restarted** (not a scoped in-place repair), operators **must** follow this archive discipline instead of versioning active workspace folder names.

| # | Rule |
|---|------|
| **WA-01** | The **current active workspace** is **moved** to bulk storage archive — e.g. `C:\AI MARS STORAGE\website-factory\archive/<project-slug>-pre-<cycle-label>/`. |
| **WA-02** | The archived workspace receives lifecycle status: **ARCHIVED** · **READ ONLY** · **REFERENCE ONLY**. An `ARCHIVED.md` marker **should** record path, date, reason, and active replacement path. |
| **WA-03** | A **new workspace** is created at the **original canonical project name** (e.g. `workspaces/fp-0002-shpigovsky-frontend/`) from the current gulp-starter or approved Factory template. |
| **WA-04** | **Forbidden** as **active production** workspace names: `project-v2`, `project-v3`, `project-final-final`, `project-new`, or any parallel `-vN` slug that splits canonical identity. |
| **WA-05** | A project may have **only one ACTIVE** frontend workspace at a time. |
| **WA-06** | All prior workspace generations **must** remain in archive (or documented snapshot with equivalent read-only posture) — not deleted silently. |

**Distinction from §3 clone-first (R-WF-04 in safe-production-rules):** clone-first applies to **experiments**; Workspace Archive Rule applies when the **canonical production tree is replaced** for a new cycle.

**Storage boundary:** Archive lives under [mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md) bulk storage — **not** a second git workspace root.

**Evidence:** Project `<PROJECT>-WORKSPACE-STATUS-vN.md` + `# REPORT — <project> workspace reset` in operations `REPORTS/`.

**First Factory instance:** FP-0002 Shpigovsky — archive `fp-0002-shpigovsky-frontend-pre-v2` (2026-06-14).

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v1 | 2026-06-14 | **Workspace Archive Rule** §8 — canonical name preservation, single ACTIVE workspace, bulk-storage archive; FP-0002 pre-v2 instance. |
| v0 | 2026-05-18 | Initial Workspace Reset Governance layer from Triumph V3 battle-test lessons; documentation only. |
