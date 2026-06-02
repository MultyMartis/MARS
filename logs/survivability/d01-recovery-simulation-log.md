# Recovery Simulation — D-01 Drill Drift

**Log id:** `recovery-20260524-d01-drill-drift`  
**Timestamp:** `2026-05-24T01:30:00Z`  
**Severity:** WARNING  
**Operator:** cursor-agent-d01-drill  
**Lane:** B  
**Related task / chat:** D-01 Sandbox Survivability Drill

## Summary

Simulated agent context drift in drill sandbox after baseline snapshot. Three files mutated and one suspicious spread file created. No rollback script executed — manual restore guidance documented below.

## Evidence

**Snapshot baseline:** `snap-20260524-012224-d01-drill`  
**Drifted workspace:** `workspaces/_sandbox/d01-survivability-drill/sample-project/`

### Files changed (drift)

| File | Baseline | Drifted |
|------|----------|---------|
| `src/app.js` | `pong — baseline` | `pong — DRIFTED (simulated agent error)` + console.warn |
| `config/settings.json` | v0.1.0-baseline, telemetry:false | v0.9.9-drift-sim, experimentalAutoDeploy:true |
| `src/styles.css` | color #1a365d | color #e53e3e, uppercase |
| `docs/suspicious-spread.md` | (absent) | New file referencing governance + Triumph v4 |

### Diff signals (diff-report-helper)

- riskSummary: **critical**
- driftSuspicion: **true**
- signals: PROTECTED-ZONE-HIT, DANGEROUS-CLASS, GOVERNANCE-DRIFT

---

## Quarantine recommendation

**Status:** Simulation only — quarantine **not** applied to filesystem.

If this were a real incident:

1. Halt AGENT session per `operational-halt-protocol-v1.md`
2. Do **not** propagate changes outside `workspaces/_sandbox/d01-survivability-drill/`
3. Consider moving drifted tree to `workspaces/_quarantine/` only with explicit human charter
4. For drill: keep drift in place as evidence artifact

---

## Diff review (manual)

Compare workspace files against snapshot mirror:

```
workspaces/_snapshots/snap-20260524-012224-d01-drill/sample-project/
  vs
workspaces/_sandbox/d01-survivability-drill/sample-project/
```

**Expected diffs:**
- `src/app.js` — handler message and debug log
- `config/settings.json` — version bump, telemetry flags
- `src/styles.css` — visual style change
- `docs/suspicious-spread.md` — new untracked file (not in snapshot)

---

## Snapshot comparison

| Check | Result |
|-------|--------|
| Manifest id match | PASS — `snap-20260524-012224-d01-drill` |
| Partial mirror present | PASS — src, docs, config mirrored |
| Integrity checker | WARNING (SI-031, SI-041, SI-050) |
| New file outside snapshot | `docs/suspicious-spread.md` — restore = delete file |

---

## Restore guidance (manual — not executed)

**Do not run automated rollback.** Operator steps:

1. Stop AGENT on sandbox workspace
2. Verify snapshot manifest at `workspaces/_snapshots/snap-20260524-012224-d01-drill/SNAPSHOT-MANIFEST.md`
3. Selective copy from snapshot mirror:
   - `sample-project/src/app.js` → workspace
   - `sample-project/src/styles.css` → workspace
   - `sample-project/config/settings.json` → workspace
4. Delete unplanned file: `sample-project/docs/suspicious-spread.md`
5. Manual diff verification (visual or file compare)
6. Log actual restore in `logs/rollback-history/` if performed
7. Retire or retain drill snapshot per retention tier (Drill)

**Rollback map:** Not created as JSON — drill uses manifest restore paths only.

---

## Actions taken

- Created baseline snapshot (manual simulation)
- Introduced intentional drift in 3 files + 1 new file
- Ran observability tools on drift pattern
- Documented restore guidance without executing restore

## Follow-up

- Operator may execute manual restore to return sandbox to baseline
- Or retain drift as reference for D-02 drill
- No production workspaces touched

## SAFE UNKNOWN

- Git diff not captured (sandbox files untracked)
- Build/smoke test N/A for drill HTML sample

---

*End of recovery simulation log.*
