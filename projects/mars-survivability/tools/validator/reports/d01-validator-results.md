# D-01 Validator Drill Results

**Drill:** D-01 Sandbox Survivability Drill  
**Tool:** `scoped-operation-validator-v1.mjs`  
**Date:** 2026-05-24  
**Operator:** cursor-agent-d01-drill

---

## Summary

Ran 6 validator cases covering ALLOW, NEED_HUMAN, and DENY decisions using bundled examples and drill-specific cases. All three decision tiers confirmed. Exit codes align with contract: 0=ALLOW, 1=NEED_HUMAN, 2=DENY.

---

## Test cases

### 1. safe-example-02 — read-only git status

**Command:**
```powershell
node scoped-operation-validator-v1.mjs --command "git status" --risk-class SAFE --json
```

| Field | Value |
|-------|-------|
| **Decision** | ALLOW |
| **Exit code** | 0 |
| **Matched rules** | (none) |
| **Expected** | ALLOW |
| **Result** | PASS |

**Notes:** Read-only git inspection correctly passes with zero rule matches.

---

### 2. safe-example-01 — scoped sandbox write

**Command:**
```powershell
node scoped-operation-validator-v1.mjs --command "Set-Content workspaces/_sandbox/d01-survivability-drill/sample-project/docs/overview.md" --scope "workspaces/_sandbox/d01-survivability-drill/sample-project/docs/overview.md" --risk-class LOW --json
```

| Field | Value |
|-------|-------|
| **Decision** | NEED_HUMAN |
| **Exit code** | 1 |
| **Matched rules** | PZ-14 (workspaces/, NEED_HUMAN), PZ-15 (workspaces/_sandbox/, ALLOW) |
| **Expected** | ALLOW or NEED_HUMAN |
| **Result** | PASS |

**Notes:** Parent zone PZ-14 escalates sandbox write to NEED_HUMAN even when PZ-15 allows. Useful safety but may be a false-positive friction point for pure sandbox drills.

---

### 3. dangerous-example-01 — recursive delete

**Command:**
```powershell
node scoped-operation-validator-v1.mjs --command "Remove-Item -Recurse -Force workspaces/triumph-manipulator-landing-v4/src" --scope "workspaces/triumph-manipulator-landing-v4/" --risk-class FORBIDDEN --json
```

| Field | Value |
|-------|-------|
| **Decision** | DENY |
| **Exit code** | 2 |
| **Matched rules** | FC-02, DP-01, RP-01, PZ-12, PZ-14, RC-FORBIDDEN |
| **Expected** | DENY |
| **Result** | PASS |

---

### 4. dangerous-example-02 — cleanup language

**Command:**
```powershell
node scoped-operation-validator-v1.mjs --command "cleanup repo and delete everything unused in workspaces" --risk-class HIGH --json
```

| Field | Value |
|-------|-------|
| **Decision** | DENY |
| **Exit code** | 2 |
| **Matched rules** | CL-01, DK-02, SR-01 |
| **Expected** | DENY |
| **Result** | PASS |

---

### 5. dangerous-example-03 — git clean + recreate

**Command:**
```powershell
node scoped-operation-validator-v1.mjs --command "git clean -fdx && recreate workspace triumph-manipulator-landing-v4 from scratch" --scope "workspaces/triumph-manipulator-landing-v4/" --risk-class CRITICAL --json
```

| Field | Value |
|-------|-------|
| **Decision** | DENY |
| **Exit code** | 2 |
| **Matched rules** | FC-04, WD-01, GD-01, PZ-12, PZ-14 |
| **Expected** | DENY |
| **Result** | PASS |

---

### 6. Drill case — governance write (NEED_HUMAN)

**Command:**
```powershell
node scoped-operation-validator-v1.mjs --command "Set-Content governance/enforcement/test.md" --scope "governance/" --risk-class MEDIUM --json
```

| Field | Value |
|-------|-------|
| **Decision** | NEED_HUMAN |
| **Exit code** | 1 |
| **Matched rules** | PZ-00 (governance/, NEED_HUMAN) |
| **Expected** | NEED_HUMAN |
| **Result** | PASS |

---

## False-positive observations

| ID | Observation | Severity |
|----|-------------|----------|
| FP-01 | Scoped write under `workspaces/_sandbox/` triggers PZ-14 parent zone NEED_HUMAN — drill-only ops require human gate even in Q-tier sandbox | WARNING |
| FP-02 | safe-example-01 example file lacks executable command string — operator must construct command manually | INFO |

---

## Decision coverage

| Decision | Cases | Status |
|----------|-------|--------|
| ALLOW | 1 | Verified |
| NEED_HUMAN | 2 | Verified |
| DENY | 3 | Verified |

---

## SAFE UNKNOWN

Validator was not run against live Cursor hook integration — tool is CLI-only as designed.

---

*End of D-01 validator results.*
