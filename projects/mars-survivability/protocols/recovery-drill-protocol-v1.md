# Recovery Drill Protocol (v1)

**Status:** **documented** — human-operated drill procedure for survivability validation.  
**Not:** automated disaster recovery product, CI job, or scheduled backup service.

**Related:** [snapshot-manifest-standard-v1.md](snapshot-manifest-standard-v1.md), [workspace-quarantine-protocol-v1.md](workspace-quarantine-protocol-v1.md)

---

## 1. Purpose

Periodically **simulate** survivability failures and **validate** that snapshots, quarantine, and rollback procedures work — without touching production workspaces.

Drills produce evidence under `logs/survivability/` and optional drill REPORT in `projects/mars-survivability/reports/`.

---

## 2. Drill types

| Drill ID | Name | Simulates |
|----------|------|-----------|
| D-01 | Snapshot restore | Pre-op snapshot → fake failure → selective restore |
| D-02 | Quarantine flow | Move disposable copy → manifest → restore from snapshot |
| D-03 | Manifest validation | Audit existing snapshots for incomplete manifests |
| D-04 | Git rollback | Restore tracked file via `git checkout --` (human) |
| D-05 | Agent refusal | Prompt agent with FORBIDDEN op — expect halt |
| D-06 | Diff verification | Compare snapshot vs live after controlled edit in sandbox |

**Rule:** All destructive drill steps run only under `workspaces/_sandbox/` unless human explicitly scopes otherwise.

---

## 3. How to simulate disaster (D-01 / D-02)

### Prerequisites

- Disposable folder: `workspaces/_sandbox/exp-<date>-drill-<slug>/`
- Copy of small fixture tree (not production workspace)

### Steps

1. Create fixture copy in sandbox.  
2. Create snapshot per [snapshot-manifest-standard-v1.md](snapshot-manifest-standard-v1.md) — mark retention tier **Drill**.  
3. **Simulate failure:** delete or corrupt 1–3 files in sandbox fixture (human or scoped command).  
4. **Stop** — do not attempt agent "fix loop".  
5. Restore from snapshot using manifest restore instructions.  
6. Run integrity checks (section 6).  
7. Record timing (section 5).  
8. Write drill REPORT.

---

## 4. How to test restore

| Step | Action | Pass |
|------|--------|------|
| 1 | Locate `SNAPSHOT-MANIFEST.md` | All required fields present |
| 2 | Verify snapshot id = directory name | Match |
| 3 | Selective copy per manifest | Files restored |
| 4 | Diff restored vs pre-failure copy | Only intended delta |
| 5 | Optional build/smoke | No regression in fixture |

**Production restore:** same steps, but human executes all copies; AGENT read-only unless explicit scoped restore task.

---

## 5. Rollback timing (record in drill REPORT)

| Metric | Target (drill) | Notes |
|--------|----------------|-------|
| Time to locate manifest | < 2 min | Operator skill |
| Time to selective restore (small fixture) | < 10 min | Excludes full workspace |
| Time to quarantine move + manifest | < 15 min | Human-operated |
| Decision point: abort agent | Immediate | On FORBIDDEN op detection |

Production targets are **SAFE UNKNOWN** — establish baseline from drills.

---

## 6. Integrity checks

After any restore (drill or production):

| Check | Method |
|-------|--------|
| **File presence** | List critical paths from manifest / handoff |
| **Git state** | `git status` — understand dirty vs expected |
| **Diff verification** | `git diff` or file compare vs snapshot |
| **Build output** | Run gulp/npm only if task allows — in scoped path |
| **Scope lock audit** | Confirm no files outside ALLOWED PATHS changed |
| **Manifest SAFE UNKNOWN** | Review unknowns before sign-off |

Failed integrity → do **not** sign off; re-quarantine or new snapshot.

---

## 7. Snapshot validation drill (D-03)

1. List all directories under `workspaces/_snapshots/`.  
2. For each: verify `SNAPSHOT-MANIFEST.md` exists.  
3. Score required fields (see snapshot standard).  
4. Flag **INCOMPLETE SNAPSHOT** entries.  
5. Append summary to `logs/survivability/`.

---

## 8. When AGENT is forbidden

| Stage | AGENT |
|-------|-------|
| Disaster simulation delete | **Forbidden** on production; sandbox only with scope lock |
| Quarantine move | **Human only** (default) |
| Production restore copy | **Human executes**; AGENT read-only assist |
| Integrity sign-off | **Human only** |
| Post-failure cleanup | **Forbidden** — no delete-recreate loops |
| Drill REPORT write | AGENT allowed if scoped to reports path |

After **context drift** detected mid-recovery → **mandatory new chat**; AGENT forbidden on recovery until new scope lock.

---

## 9. Human-only recovery stages

1. Incident detection and AGENT stop  
2. Quarantine move (production paths)  
3. Snapshot selection and validation  
4. Physical copy restore to production or `_recovery/`  
5. Integrity sign-off  
6. `logs/rollback-history/` entry  
7. Quarantine archive/delete decision  

AGENT may support: read-only audit, manifest drafting, diff listing, REPORT drafting — never autonomous recovery mutations on production.

---

## 10. Drill frequency (recommended)

| Drill | Frequency |
|-------|-----------|
| D-03 manifest audit | Monthly |
| D-01 snapshot restore | Quarterly |
| D-05 agent refusal | After guardrails change |
| Full D-02 quarantine | After any survivability incident |

No automation — calendar reminder sufficient.

---

## 11. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G0 operationalization |

---

*End of Recovery Drill Protocol v1.*
