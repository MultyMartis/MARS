# Pre-Restore Analysis — D-02 Manual Restore Drill

**Log id:** `rollback-20260524-d02-pre-restore`  
**Timestamp:** `2026-05-24T19:10:00Z`  
**Severity:** WARNING  
**Operator:** cursor-agent-d02-drill  
**Lane:** B  
**Related task / chat:** D-02 Real Manual Restore Drill

---

## Summary

Pre-restore analysis of drifted D-01 sandbox against baseline snapshot `snap-20260524-012224-d01-drill`. Four drift signals identified in `sample-project/`; one suspicious spread file outside snapshot mirror. Quarantine-first restore recommended before any in-place repair.

---

## Evidence

| Artifact | Path |
|----------|------|
| Drifted sandbox (pre-quarantine) | `workspaces/_sandbox/d01-survivability-drill/` |
| Baseline snapshot | `workspaces/_snapshots/snap-20260524-012224-d01-drill/` |
| Manifest | `workspaces/_snapshots/snap-20260524-012224-d01-drill/SNAPSHOT-MANIFEST.md` |
| D-01 recovery log | `logs/survivability/d01-recovery-simulation-log.md` |

---

## Changed files (drift vs snapshot)

| File | Snapshot state | Drifted state | Restore action |
|------|----------------|---------------|----------------|
| `sample-project/src/app.js` | `pong — baseline` | `pong — DRIFTED (simulated agent error)` + `console.warn` | Copy from snapshot |
| `sample-project/src/styles.css` | color `#1a365d` | color `#e53e3e`, `text-transform: uppercase` | Copy from snapshot |
| `sample-project/config/settings.json` | v0.1.0-baseline, telemetry:false | v0.9.9-drift-sim, experimentalAutoDeploy:true | Copy from snapshot |
| `sample-project/docs/overview.md` | baseline doc | **unchanged** (hash match) | No action |
| `sample-project/docs/suspicious-spread.md` | **absent** | new file with governance/Triumph refs | **Do not restore** — omit in clean tree |
| `sample-project/src/index.html` | **not in snapshot mirror** | present, unchanged | SAFE UNKNOWN — carry from quarantine if needed |

**Unchanged (sandbox root):** `README.md` — drill metadata only; not mirrored in snapshot.

---

## Suspicious spread

| Signal | Detail |
|--------|--------|
| New file | `docs/suspicious-spread.md` — references `governance/enforcement/` and `workspaces/triumph-manipulator-landing-v4/` |
| Content drift | Simulates lane contamination without filesystem touch |
| diff-report-helper (D-01) | riskSummary: **critical**, signals: PROTECTED-ZONE-HIT, DANGEROUS-CLASS, GOVERNANCE-DRIFT |
| diff-report-helper (D-02 path-only) | riskSummary: **high**, PROTECTED-ZONE-HIT only — content references not scanned |

**Assessment:** Suspicious spread is a **drift artifact**, not production contamination. Quarantine preserves evidence; restore must exclude this file.

---

## Drift summary

| Metric | Value |
|--------|-------|
| Files in snapshot mirror | 4 |
| Files drifted | 3 |
| Files unchanged | 1 (`overview.md`) |
| Files added (not in snapshot) | 1 (`suspicious-spread.md`) |
| Files in workspace but not mirrored | 1 (`index.html`) |
| Partial mirror gap | **YES** — snapshot is partial by design (D-01) |

**Drift class:** Intentional D-01 simulation — context drift in config/handler/style + scope-spread doc.

---

## Restore candidates

| Priority | Source | Target (new workspace) | Method |
|----------|--------|------------------------|--------|
| 1 | `snap-.../sample-project/src/app.js` | `d01-survivability-drill-restored/.../app.js` | Manual copy |
| 2 | `snap-.../sample-project/src/styles.css` | `.../styles.css` | Manual copy |
| 3 | `snap-.../sample-project/config/settings.json` | `.../settings.json` | Manual copy |
| 4 | `snap-.../sample-project/docs/overview.md` | `.../overview.md` | Manual copy |
| 5 | Quarantine `index.html` (unchanged) | `.../index.html` | Manual copy — not in snapshot |

**Exclude from restore:** `suspicious-spread.md`

---

## Quarantine recommendation

| Field | Value |
|-------|-------|
| **Decision** | **QUARANTINE FIRST** — move drifted sandbox copy before restore |
| **Target path** | `workspaces/_quarantine/d01-survivability-drill-drifted/` |
| **Rationale** | Do not repair on contaminated tree; preserve drift evidence per `workspace-quarantine-protocol-v1.md` |
| **Snapshot** | Do **not** modify original snapshot |
| **Restore target** | New workspace `workspaces/_sandbox/d01-survivability-drill-restored/` |

---

## SAFE UNKNOWN

- Git baseline for sandbox files — untracked; no `git diff` available
- `index.html` provenance — not in snapshot; assumed unchanged from D-01 baseline
- Binary/hash verification — text-only drill; manual hash compare used

---

*End of D-02 pre-restore analysis.*
