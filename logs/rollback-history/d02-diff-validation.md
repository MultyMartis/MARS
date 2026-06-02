# Diff Validation — D-02 Manual Restore Drill

**Log id:** `rollback-20260524-d02-diff-validation`  
**Timestamp:** `2026-05-24T19:15:00Z`  
**Severity:** INFO  
**Operator:** cursor-agent-d02-drill  
**Lane:** B  
**Related task / chat:** D-02 Real Manual Restore Drill

---

## Summary

Manual hash comparison and `diff-report-helper-v1.mjs` advisory run confirm restored workspace achieves snapshot parity on all mirrored files. Drift artifacts excluded. Quarantined copy retains expected drift deltas.

---

## Tool invocation

```powershell
node projects/mars-survivability/tools/observability/diff-report-helper-v1.mjs `
  --paths "workspaces/_sandbox/d01-survivability-drill-restored/sample-project/src/app.js,workspaces/_sandbox/d01-survivability-drill-restored/sample-project/src/styles.css,workspaces/_sandbox/d01-survivability-drill-restored/sample-project/config/settings.json,workspaces/_sandbox/d01-survivability-drill-restored/sample-project/docs/overview.md" `
  --json
```

**Tool result:** riskSummary `high` (PROTECTED-ZONE-HIT on sandbox paths — label noise, not restore failure)

---

## Restored vs snapshot (parity check)

| File | Hash match | Status |
|------|------------|--------|
| `src/app.js` | YES | **PARITY** |
| `src/styles.css` | YES | **PARITY** |
| `config/settings.json` | YES | **PARITY** |
| `docs/overview.md` | YES | **PARITY** |
| `docs/suspicious-spread.md` | N/A (absent) | **CORRECT — excluded** |

**Restored parity:** **PASS** on all snapshot-mirrored files.

---

## Restored vs quarantine (drift isolation)

| File | Match quarantine? | Expected |
|------|-------------------|----------|
| `src/app.js` | NO — baseline restored | PASS |
| `src/styles.css` | NO — baseline restored | PASS |
| `config/settings.json` | NO — baseline restored | PASS |
| `docs/suspicious-spread.md` | Absent in restored | PASS |
| `src/index.html` | YES — copied from quarantine unchanged | PASS |

**Drift isolation:** **PASS** — restored tree does not carry drift mutations.

---

## Suspicious leftovers

| Check | Result |
|-------|--------|
| `suspicious-spread.md` in restored | **Absent** — correct |
| Drift strings in `app.js` | **Absent** — shows `pong — baseline` |
| `experimentalAutoDeploy` in settings | **Absent** — telemetry false |
| Unexpected new files | **None** |

---

## Missing files

| File | Status | Notes |
|------|--------|-------|
| `src/index.html` | Present in restored | Not in snapshot mirror — sourced from quarantine (SAFE UNKNOWN) |
| Snapshot root `README.md` | Not copied | Drill metadata only; not required for sample-project restore |

**Partial mirror gap:** Documented in manifest SAFE UNKNOWN — operator must handle unm mirrored files explicitly.

---

## Unexpected drift

| Signal | Finding |
|--------|---------|
| Cross-workspace contamination | **None** |
| Governance path writes | **None** |
| New drift in restored tree | **None** |

---

## diff-report-helper — quarantine drift paths (reference)

D-01 pattern on original drift (4 paths): riskSummary **high**, PROTECTED-ZONE-HIT.

D-02 restored paths (4 mirrored files): same zone label noise — **not** a restore quality signal.

---

## Validation verdict

| Criterion | Result |
|-----------|--------|
| Restored parity with snapshot | **PASS** |
| Drift excluded | **PASS** |
| Quarantine preserves drift evidence | **PASS** |
| Helper usefulness for restore verification | **Moderate** — path-based only; hash compare required for content |

---

## SAFE UNKNOWN

- diff-report-helper does not compare file contents — operator hash/diff still required
- `index.html` not verified against independent baseline (only quarantine copy)

---

*End of D-02 diff validation.*
