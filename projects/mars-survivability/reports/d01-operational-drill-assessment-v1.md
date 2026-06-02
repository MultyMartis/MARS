# D-01 Operational Drill Assessment (v1)

**Status:** Human-reviewed drill assessment — documentation only  
**Drill id:** D-01  
**Date:** 2026-05-24  
**Lane:** B — Survivability / Recovery Drill / Sandbox Validation  
**Assessor:** cursor-agent-d01-drill (advisory — human sign-off pending)

---

## 1. Executive summary

The first sandbox survivability drill successfully validated the G0–G4 tooling stack in isolation. All core flows produce actionable advisory output. The stack is **fit for human-operated Lane B work** with known friction points around sandbox zone labeling and Windows path handling.

**Overall survivability confidence:** **Moderate-high** (documented flow) / **Low** (automation — intentionally absent)

---

## 2. Validator usefulness

| Criterion | Rating | Notes |
|-----------|--------|-------|
| DENY accuracy | Strong | Forbidden deletes, git clean, cleanup language all DENY |
| NEED_HUMAN accuracy | Good | Governance and parent zone escalation work |
| ALLOW accuracy | Good | Read-only git status passes cleanly |
| Operator clarity | Good | JSON output includes matched rule ids and explanations |
| False positives | Minor | Sandbox writes trigger PZ-14 NEED_HUMAN |

**Verdict:** Validator is the **most valuable gate** in the stack for pre-execution checks.

---

## 3. Helper usefulness

### snapshot-helper-v1.mjs

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Naming convention | Strong | Timestamped snap-* ids with workspace slug |
| Risk class mapping | Good | SAFE→optional, MEDIUM/HIGH→required |
| Manifest draft | Good | Reduces operator load; FILL placeholders clear |
| Disk safety | Strong | Does not write — human copy required |

**Gap:** HIGH risk does not elevate rollbackImportance above "medium".

### scope-analyzer-v1.mjs

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Cross-workspace detection | Strong | Correctly flags contamination |
| P0/P1 detection | Strong | Governance + mars-survivability hits |
| Sandbox labeling | Weak | Never emits SAFE for Q-tier sandbox |

**Verdict:** Helpers reduce manifest authoring friction and surface scope risk early.

---

## 4. False positives catalog

| ID | Component | Description | Impact |
|----|-----------|-------------|--------|
| FP-01 | Validator | Sandbox write → PZ-14 NEED_HUMAN | Operator friction in drills |
| FP-S01 | Scope analyzer | Sandbox-only → PROTECTED-ZONE-HIT | Label noise |
| FP-O01 | Integrity checker | Absolute Windows path breaks manifest lookup | Tool misuse risk |
| FP-O02 | Manifest validator | Future timestamp WARNING on same-day drill | Cosmetic |
| FP-O03 | Integrity checker | SI-050 workspace slug heuristic misfire | WARNING noise |

---

## 5. Missing protections

| Gap | Severity | Notes |
|-----|----------|-------|
| No Cursor hook integration | By design | Validator is CLI-only |
| No automated snapshot copy | By design | Human must mirror files |
| No automated rollback | By design | Manual restore only |
| Sandbox SAFE label absent | Low | Registry could add Q-tier override |
| Absolute path handling | Medium | snapshot-integrity-checker needs fix or docs |
| RD-030 registry drift | Low | Pre-existing doc/rule mismatch |

---

## 6. Usability

| Aspect | Assessment |
|--------|------------|
| CLI invocation | Straightforward with `--json` |
| Report discoverability | Good — reports under tools/*/reports/ |
| Log format | operational-log-format-v1.md is usable |
| Learning curve | Moderate — operator must know relative paths |
| PowerShell compatibility | Works; avoid `&&` chaining |

---

## 7. Operator friction

| Friction point | Mitigation |
|----------------|------------|
| Sandbox ops require NEED_HUMAN | Accept for safety or tune PZ-14 for _sandbox/ |
| Manual snapshot copy | Use checklist; helper provides draft |
| Multiple tool invocations | Preflight checklist bundles steps |
| Windows absolute paths | Document: always use repo-relative paths |

---

## 8. Survivability confidence

| Layer | Confidence | Rationale |
|-------|------------|-----------|
| Snapshot discipline | Moderate-high | Template + helper + integrity checker |
| Pre-execution gate | High | Validator DENY rules effective |
| Drift detection | Moderate-high | diff-report-helper + scope analyzer |
| Recovery clarity | Moderate | Manual restore guidance works; no automation |
| Production safety | High | No production touched in drill |

---

## 9. Drift detection quality

| Tool | Quality | Notes |
|------|---------|-------|
| diff-report-helper | Strong | Critical flag for governance + workspace mix |
| scope-analyzer | Good | Cross-workspace and P0 hits |
| registry-drift-linter | Good | Surfaces doc/rule gaps |
| manifest-cross-validator | Good | WARNING for incomplete manifests |

Recovery simulation confirmed diff-report-helper detects suspicious spread pattern.

---

## 10. Rollback clarity

| Aspect | Status |
|--------|--------|
| Manifest restore paths | Clear in SNAPSHOT-MANIFEST.md |
| Selective copy instructions | Documented in recovery log |
| Rollback map JSON | Not used in drill — optional future |
| Operator authority | Preserved — no auto-rollback |

**Assessment:** Rollback guidance is **sufficient for human-operated recovery** but requires operator discipline.

---

## 11. Most valuable systems

1. **scoped-operation-validator-v1.mjs** — deny-first for destructive patterns
2. **diff-report-helper-v1.mjs** — drift suspicion and zone classification
3. **snapshot-helper-v1.mjs** — manifest draft and naming
4. **snapshot-manifest-template.md** — structural consistency
5. **operational-log-format-v1.md** — audit trail standard

---

## 12. Remaining weaknesses

- Sandbox Q-tier treated like production workspace at label level
- Windows absolute path bug in integrity checker
- No single orchestrated preflight command (by design — human steps)
- Registry drift RD-030 unresolved
- Drill sandbox left in drifted state (intentional evidence)

---

## 13. SAFE UNKNOWN

- Human operator sign-off on this assessment not yet recorded
- Long-term retention of drill snapshot not verified
- Cross-session AGENT memory of drill state not tested

---

## 14. Recommended next phase

| Phase | Action |
|-------|--------|
| D-02 | Operator executes manual restore from snapshot; log in rollback-history |
| Registry | Reconcile RD-030 (F-10 recreate vs validator rules) |
| Tooling | Fix or document absolute-path handling in snapshot-integrity-checker |
| Registry proposal | Q-tier sandbox label exemption for scope-analyzer SAFE |
| Optional | Add rollback-map JSON for multi-file restore drill |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | D-01 first operational drill assessment |

---

*End of D-01 Operational Drill Assessment v1.*
