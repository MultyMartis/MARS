# D-01 Scope Analyzer Drill Results

**Drill:** D-01 Sandbox Survivability Drill  
**Tool:** `scope-analyzer-v1.mjs`  
**Date:** 2026-05-24  
**Operator:** cursor-agent-d01-drill

---

## Summary

Ran four scope analysis cases: sandbox-only, sandbox+governance, multi-workspace, and protected-zone hit. Tool surfaces advisory labels and recommendations without blocking.

---

## Test cases

### 1. Sandbox-only

**Command:**
```powershell
node scope-analyzer-v1.mjs --paths "workspaces/_sandbox/d01-survivability-drill/sample-project/src/app.js" --json
```

| Field | Value |
|-------|-------|
| **primary** | PROTECTED-ZONE-HIT |
| **labels** | PROTECTED-ZONE-HIT |
| **workspaceRoots** | workspaces/_sandbox |
| **protectedHits** | PZ-15 (Q/LOW), PZ-14 (P2/MEDIUM) |

**Expected:** SAFE or low-friction label for drill sandbox  
**Actual:** PROTECTED-ZONE-HIT  
**Assessment:** False-positive friction — sandbox paths inherit parent `workspaces/` zone

---

### 2. Sandbox + governance

**Command:**
```powershell
node scope-analyzer-v1.mjs --paths "workspaces/_sandbox/d01-survivability-drill/sample-project/src/app.js,governance/enforcement/" --json
```

| Field | Value |
|-------|-------|
| **primary** | PROTECTED-ZONE-HIT |
| **labels** | PROTECTED-ZONE-HIT |
| **protectedHits** | PZ-15, PZ-14, PZ-00 (governance/, P0/CRITICAL) |

**Assessment:** Correctly flags P0 governance alongside sandbox. Recommendations include validator pre-check.

---

### 3. Multi-workspace

**Command:**
```powershell
node scope-analyzer-v1.mjs --paths "workspaces/_sandbox/d01-survivability-drill/,workspaces/triumph-manipulator-landing-v4/src/" --json
```

| Field | Value |
|-------|-------|
| **primary** | PROTECTED-ZONE-HIT |
| **labels** | PROTECTED-ZONE-HIT, RISKY, CROSS-WORKSPACE |
| **workspaceRoots** | workspaces/_sandbox, workspaces/triumph-manipulator-landing-v4 |
| **details** | "Multiple workspace roots — contamination risk" |

**Assessment:** PASS — correctly detects cross-workspace contamination and production workspace marker.

---

### 4. Protected-zone hit (governance + mars-survivability)

**Command:**
```powershell
node scope-analyzer-v1.mjs --paths "governance/registry-architecture.md,projects/mars-survivability/README.md" --json
```

| Field | Value |
|-------|-------|
| **primary** | PROTECTED-ZONE-HIT |
| **labels** | PROTECTED-ZONE-HIT |
| **protectedHits** | PZ-00 (governance/), PZ-07, PZ-08 (projects/) |

**Assessment:** PASS — dual P0/P1 hits correctly identified.

---

## False-positive observations

| ID | Case | Observation |
|----|------|-------------|
| FP-S01 | Sandbox-only | Never emits SAFE label for paths under `workspaces/_sandbox/` due to parent zone inheritance |
| FP-S02 | Sandbox-only | Drill Q-tier sandbox treated same as production workspace paths at label level |

---

## Recommendations surfaced by tool

- Narrow scope or explicit path allowlist (Lane B)
- Run scoped-operation-validator on planned commands
- Split multi-workspace tasks
- Run snapshot-helper before MEDIUM+ mutation

All recommendations are actionable and align with survivability protocols.

---

*End of D-01 scope analyzer results.*
