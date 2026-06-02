# Validator Report Format (v1)

**Status:** **documented** — structure for human-written or CLI-generated validation reports.  
**Not:** automated report pipeline, telemetry store, or enforcement audit product.

**Output location (recommended):** `projects/mars-survivability/tools/validator/reports/`  
**Naming:** `validation-report-YYYYMMDD-HHMMSS-<slug>.md` or `.json`

---

## 1. Purpose

Capture a **point-in-time** record of validator input and outcome for incident review, operational drills, and future GitGuard manifest cross-checks.

---

## 2. Required fields

| Field | Type | Description |
|-------|------|-------------|
| **timestamp** | ISO-8601 UTC | When validation ran (`2026-05-24T12:00:00.000Z`) |
| **input.command** | string | Exact command string passed to `--command` |
| **input.scope** | string \| null | Scope path if provided |
| **input.riskClass** | string \| null | Declared risk class if provided |
| **riskScore** | number 0–100 | Heuristic score from validator (not authoritative policy) |
| **matchedRules** | array | Rule hits: `id`, `bucket`, `decision`, `reason` |
| **protectedZonesTriggered** | array | Prefixes or zone labels from protected_paths |
| **decision** | enum | `ALLOW` \| `DENY` \| `NEED_HUMAN` |
| **explanation** | array of strings | Human-readable reasoning lines |
| **SAFE UNKNOWN** | array of strings | Gaps, ambiguity, or missing evidence — **empty if none** |

---

## 3. Optional fields

| Field | Description |
|-------|-------------|
| `operator` | Who ran validator (initials or handle) |
| `sessionId` | Cursor chat / task id |
| `taskScopeLock` | Paste from safe-agent-task-template |
| `humanOverride` | `APPROVED: <op> @ <paths>` if operator proceeded despite NEED_HUMAN |
| `followUp` | Halt, redesign, snapshot taken, etc. |
| `validatorVersion` | `scoped-operation-validator-v1.mjs` |
| `registryVersion` | From `validator-rules-registry-v1.json` → `version` |

---

## 4. Markdown template

```markdown
# Validation Report — <short title>

**Timestamp:** 2026-05-24T12:00:00.000Z  
**Validator:** scoped-operation-validator-v1.mjs  
**Registry:** validator-rules-registry-v1.json v1.0.0

## Input

| Field | Value |
|-------|-------|
| Command | `<command>` |
| Scope | `<scope or —>` |
| Risk class | `<class or —>` |

## Outcome

| Field | Value |
|-------|-------|
| Decision | **DENY** |
| Risk score | 92/100 |

## Matched rules

| ID | Bucket | Decision | Reason |
|----|--------|----------|--------|
| FC-04 | forbidden_commands | DENY | git clean forbidden for AGENT (F-05) |

## Protected zones triggered

- `workspaces/triumph-manipulator-landing-v4/`

## Explanation

- 3 rule(s) matched (highest severity wins).
- [FC-04] git clean forbidden for AGENT (F-05) → DENY

## SAFE UNKNOWN

- (none)

## Operator notes

- Halted AGENT; redirected to quarantine protocol.

---
*Human-operated report — not automated enforcement.*
```

---

## 5. JSON template (CLI `--json`)

```json
{
  "timestamp": "2026-05-24T12:00:00.000Z",
  "input": {
    "command": "git clean -fdx",
    "scope": null,
    "riskClass": "FORBIDDEN"
  },
  "decision": "DENY",
  "riskScore": 90,
  "matchedRules": [],
  "protectedZonesTriggered": [],
  "explanation": [],
  "safeUnknown": [],
  "validator": "scoped-operation-validator-v1.mjs",
  "registry": "validator-rules-registry-v1.json"
}
```

---

## 6. Decision semantics in reports

| Decision | Report action |
|----------|----------------|
| ALLOW | May proceed **only if** scope lock + risk class agree; report still recommended for MEDIUM+ |
| NEED_HUMAN | Document required approval before execution |
| DENY | Document halt; link [operational-halt-protocol-v1.md](../../protocols/operational-halt-protocol-v1.md) if AGENT was stopped |

---

## 7. SAFE UNKNOWN usage

Record **SAFE UNKNOWN** when:

- Command is obfuscated or split across multiple steps
- Scope path is outside repo or not normalized
- Registry may be stale vs protected-zones doc
- Validator not run but operation proceeded (gap in process)

**Do not** use SAFE UNKNOWN to mean “allowed because unknown” — default is **deny / NEED_HUMAN**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G2 — report format v1 |

---

*End of Validator Report Format v1.*
