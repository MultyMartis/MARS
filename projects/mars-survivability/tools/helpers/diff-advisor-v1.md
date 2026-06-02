# Diff Advisor (v1)

**Status:** **documented** — human-operated guidance for reviewing file changes before and after risky work.  
**Not:** automated diff scanner, CI gate, or enforcement product.

**Workflow:** [diff-advisor-workflow-v1.md](diff-advisor-workflow-v1.md)  
**Scope check:** [scope-analyzer-v1.mjs](scope-analyzer-v1.mjs)  
**Validator:** [../validator/scoped-operation-validator-v1.mjs](../validator/scoped-operation-validator-v1.mjs)

---

## 1. Purpose

Help operators detect **scope escape**, **workspace explosion**, and **protected-zone touches** by disciplined use of `git diff` and path review — without claiming an in-repo diff engine.

---

## 2. What diff advisor is

| Is | Is not |
|----|--------|
| Checklist + interpretation guide | Autonomous file watcher |
| Pre/post change human review | Auto-rollback trigger |
| Suspicious-pattern vocabulary | Hidden runtime monitor |

---

## 3. Pre-change diff review

**When:** Before first mutation on MEDIUM RISK+ or protected paths.

**Operator steps:**

1. `git status` — note branch, dirty/clean, untracked count.  
2. `git diff` — review **already staged/unstaged** changes; do not mix with planned AGENT work.  
3. `git diff --stat` — baseline file count for post-check comparison.  
4. Run [scope-analyzer-v1.mjs](scope-analyzer-v1.mjs) on **ALLOWED PATHS** from scope lock.  
5. If scope lock lists workspace `src/` — record top-level folders expected to change.

**Red flags (pre):**

- Existing dirty state not mentioned in task → halt, clean or document first.  
- Diff already touches paths **outside** scope lock.  
- Unexpected `governance/`, `registry/`, `.cursorrules`, `AGENTS.md` in diff.

---

## 4. Post-change diff review

**When:** After AGENT session or human edit batch, **before** commit or handoff.

**Operator steps:**

1. `git diff --stat` — compare to pre-change baseline.  
2. `git diff` per suspicious path (see §5).  
3. List **unexpected paths** — any file not in scope lock.  
4. If unexpected paths exist → halt per [operational-halt-protocol-v1.md](../../protocols/operational-halt-protocol-v1.md).  
5. Optional: save summary to `tools/helpers/reports/diff-review-YYYYMMDD.md`.

---

## 5. Suspicious file spread

| Signal | Interpretation |
|--------|----------------|
| >15 files changed without task authorization | **Workspace explosion** — likely scope escape |
| Changes in 2+ `workspaces/*/` roots | **Cross-workspace contamination** |
| Changes under `projects/` + `workspaces/` same session | **Lane violation risk** — split tasks |
| Mass rename/delete in diff | **Destructive** — verify FORBIDDEN list |
| Only `dist/` / `build/` changed | May be regen — confirm task allowed build outputs |

---

## 6. Dangerous file classes

Treat edits in these areas as **minimum HIGH RISK** review:

| Class | Paths (examples) |
|-------|------------------|
| Ecosystem SoT | `governance/`, `registry/`, `AGENTS.md`, `.cursorrules` |
| Legacy pack | `web-gpt-sources/` |
| Security | `security/` |
| Survivability | `projects/mars-survivability/` structural moves |
| Snapshot store | `workspaces/_snapshots/` |
| Campaign schema | `projects/orca/ppc/triumph-manipulator/schema/` |
| Shared assets | `shared/assets/` |
| Triumph production | `workspaces/triumph-manipulator-landing-v4/`, `v5/` |

---

## 7. Workspace explosion detection

**Definition:** File change count or path breadth grows far beyond scope lock without documented reason.

**Heuristics (human judgment):**

- `--stat` line count > 2× expected file list.  
- New directories appearing under workspace root.  
- Config files touched (`package.json`, `gulpfile.js`) when task was HTML/CSS only.

**Response:** halt → quarantine assessment → do not commit “to save progress” without review.

---

## 8. Unexpected protected-zone touches

If `git diff` shows paths matching [protected-zones-registry-v1.md](../../registries/protected-zones-registry-v1.md) tiers:

| Tier | Action |
|------|--------|
| P0 / CRITICAL | Halt — revert or isolate; new chat + Lane B |
| P1 | Human review mandatory; document in REPORT |
| P2 workspace | Snapshot restore path must be known |
| Q (`_snapshots`, `_quarantine`) | AGENT must not have mutated — incident class |

---

## 9. SAFE UNKNOWN

- Binary/asset diff interpretation — operator visual check.  
- Untracked files — `git status` may hide spread until add.  
- Automated diff scoring — **not implemented** (G4+ candidate).

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G3 — diff advisor v1 |

---

*End of Diff Advisor v1.*
