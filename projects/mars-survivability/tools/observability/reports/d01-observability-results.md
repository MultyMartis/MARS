# D-01 Observability Drill Results

**Drill:** D-01 Sandbox Survivability Drill  
**Date:** 2026-05-24  
**Operator:** cursor-agent-d01-drill

---

## Summary

Ran four observability tools against drill snapshot, registry docs, and synthetic diff paths. Tools are read-only and advisory. One path-resolution quirk discovered in snapshot-integrity-checker when using absolute Windows paths.

---

## 1. manifest-cross-validator-v1.mjs

**Command:**
```powershell
node manifest-cross-validator-v1.mjs --manifest "workspaces/_snapshots/snap-20260524-012224-d01-drill/SNAPSHOT-MANIFEST.md" --scope "workspaces/_sandbox/d01-survivability-drill/sample-project/" --snapshot-dir "workspaces/_snapshots/snap-20260524-012224-d01-drill" --expected-snapshot-id "snap-20260524-012224-d01-drill" --json
```

| Field | Value |
|-------|-------|
| **status** | WARNING |
| **exit code** | 1 |
| **findings** | MC-032 (timestamp future), MC-070 (SAFE UNKNOWN in manifest) |
| **parsed.snapshotId** | snap-20260524-012224-d01-drill |
| **mirroredEntryCount** | 2 |

**Notes:** Manifest structurally valid. WARNING due to timezone/future timestamp heuristic and documented SAFE UNKNOWN fields — expected for drill.

---

## 2. registry-drift-linter-v1.mjs

**Command:**
```powershell
node registry-drift-linter-v1.mjs --json
```

| Field | Value |
|-------|-------|
| **status** | DRIFT |
| **exit code** | 1 |
| **findings** | RD-030 — Policy mentions "recreate" (F-10) but no obvious validator rule |
| **mdPathCount** | 40 |
| **jsonPrefixCount** | 18 |
| **enforcementForbiddenCount** | 14 |

**Notes:** Useful drift signal for human registry reconciliation. Not a drill failure.

---

## 3. snapshot-integrity-checker-v1.mjs

**Command (correct — relative path):**
```powershell
node snapshot-integrity-checker-v1.mjs --snapshot-dir "workspaces/_snapshots/snap-20260524-012224-d01-drill" --json
```

| Field | Value |
|-------|-------|
| **status** | WARNING |
| **exit code** | 1 |
| **findings** | SI-031 (single top-level folder), SI-041 (SAFE UNKNOWN), SI-050 (workspace mismatch heuristic) |

**Command (failed — absolute path):**
```powershell
node snapshot-integrity-checker-v1.mjs --snapshot-dir "c:\AI MARS\workspaces\_snapshots\snap-20260524-012224-d01-drill" --json
```

| Field | Value |
|-------|-------|
| **status** | INVALID |
| **finding** | SI-010 Missing SNAPSHOT-MANIFEST.md |

**Bug/limitation:** Absolute Windows paths are joined with REPO_ROOT, producing invalid path. **Use relative repo paths only.**

---

## 4. diff-report-helper-v1.mjs

### Case A — drill drift paths (mixed sandbox + governance)

**Command:**
```powershell
node diff-report-helper-v1.mjs --paths "workspaces/_sandbox/d01-survivability-drill/sample-project/src/app.js,workspaces/_sandbox/d01-survivability-drill/sample-project/config/settings.json,governance/enforcement/" --json
```

| Field | Value |
|-------|-------|
| **riskSummary** | critical |
| **driftSuspicion** | true |
| **signals** | PROTECTED-ZONE-HIT, DANGEROUS-CLASS, GOVERNANCE-DRIFT |
| **findings** | DR-040 — Governance/registry paths in diff — charter required |

**Assessment:** Correctly flags suspicious spread pattern used in recovery simulation.

### Case B — bundled example

**Command:**
```powershell
node diff-report-helper-v1.mjs --file "examples/diff-stat-example.txt" --json
```

| Field | Value |
|-------|-------|
| **riskSummary** | high |
| **driftSuspicion** | true |
| **signals** | PROTECTED-ZONE-HIT, DRIFT-SUSPICION |
| **findings** | DR-030 — Both projects/ and workspaces/ touched |

---

## False-positive observations

| ID | Tool | Observation |
|----|------|-------------|
| FP-O01 | snapshot-integrity-checker | Absolute path on Windows breaks manifest detection |
| FP-O02 | manifest-cross-validator | MC-032 future timestamp on same-day drill |
| FP-O03 | snapshot-integrity-checker | SI-050 heuristic misparses workspace slug from manifest path text |

---

## Observability confidence

| Tool | Useful | Actionable output |
|------|--------|-------------------|
| manifest-cross-validator | Yes | WARNING with specific finding ids |
| registry-drift-linter | Yes | DRIFT with reconciliation hint |
| snapshot-integrity-checker | Yes (with relative paths) | WARNING/INVALID with repair hints |
| diff-report-helper | Yes | Critical drift suspicion for mixed zones |

---

*End of D-01 observability results.*
