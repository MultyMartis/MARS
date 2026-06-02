# D-02 Human-Operated Restore Review (v1)

**Status:** Human-reviewed drill assessment — documentation only  
**Drill id:** D-02  
**Date:** 2026-05-24  
**Lane:** B — Survivability / Manual Restore / Rollback Discipline  
**Assessor:** cursor-agent-d02-drill (advisory — human sign-off pending)

---

## 1. Executive summary

First **real** human-operated restore drill completed: quarantine-first, manual selective copy from snapshot, diff validation, manifest validation, rollback map draft. Flow is **operationally clear** with moderate friction on partial mirrors and path labeling. No automation used; no production touched.

**Restore confidence after drill:** **Moderate-high** for sandbox drill / **Not proven** for production Triumph workspaces.

---

## 2. Restore clarity

| Aspect | Rating | Notes |
|--------|--------|-------|
| Pre-restore analysis template | Strong | Changed files table + restore candidates clear |
| Quarantine-first ordering | Strong | Move-before-restore prevents in-place repair mistake |
| Manifest restore paths | Good | SNAPSHOT-MANIFEST.md lists selective copy targets |
| New workspace vs in-place | Good | `d01-survivability-drill-restored` avoids overwriting quarantine |
| Exclude drift artifacts | Good | suspicious-spread.md omission explicit |

**Gap:** Manifest workspace field still points to original path after restore to new workspace — operator must mentally remap.

---

## 3. Operator friction

| Friction | Severity | Mitigation |
|----------|----------|------------|
| Manual copy per file | Medium | Rollback map restoreOrdering helps |
| Partial snapshot mirror | Medium | Document SAFE UNKNOWN; checklist for unm mirrored files |
| diff-report-helper zone noise | Low | Use hash compare for content; treat PROTECTED-ZONE-HIT as label |
| Multiple log files to write | Medium | Preflight checklist bundles steps |
| Quarantine naming vs protocol | Low | Drill slug acceptable; production should use `q-YYYYMMDD-...` |
| PowerShell Move-Item | Low | Works; document move-not-delete |

---

## 4. Rollback usability

| Criterion | Assessment |
|-----------|------------|
| Rollback map JSON | **Useful** — first drill using schema; ordering steps readable |
| Selective vs full restore | **Clear** — manifest + map both support selective |
| Quarantine references in map | **Useful** — links drift evidence to restore plan |
| Automation temptation | **Resisted** — no rsync/script; discipline held |

---

## 5. Quarantine usefulness

| Criterion | Assessment |
|-----------|------------|
| Evidence preservation | **Strong** — full drifted tree intact |
| Separation from clean restore | **Strong** — no repair on contaminated tree |
| QUARANTINE-MANIFEST.md | **Good** — links snapshot and recovery status |
| Operator confidence | **Improved** — knowing drift is isolated reduces panic |

---

## 6. Helper usefulness (D-02)

| Tool | Use in D-02 | Value |
|------|-------------|-------|
| diff-report-helper | Path advisory on restored files | Moderate — zone labels only |
| snapshot-integrity-checker | Pre/post restore snapshot check | Good — WARNING expected |
| manifest-cross-validator | Scope linkage for restored workspace | Good — catches SAFE UNKNOWN |
| snapshot-helper | Not re-run | N/A |
| scoped-operation-validator | Not re-run | N/A |

**Verdict:** Observability tools **support** restore verification but **do not replace** content-level diff/hash compare.

---

## 7. Validator usefulness (D-02)

Manifest and integrity validators returned WARNING (not INVALID) — correct for partial drill snapshot. Operators can proceed with documented gaps.

| Validator | D-02 outcome | Operator action |
|-----------|--------------|-----------------|
| snapshot-integrity-checker | WARNING | Review SI-031 partial mirror |
| manifest-cross-validator | WARNING | Review MC-070 SAFE UNKNOWN |

---

## 8. Missing guidance

| Gap | Priority |
|-----|----------|
| Explicit checklist: unm mirrored files after partial snapshot | High |
| When to use new workspace vs in-place restore | Medium |
| Updating manifest workspace field post-restore | Medium |
| Quarantine retention / archive policy for drills | Low |
| Single-page "restore drill runbook" linking all logs | Medium |

---

## 9. Operational confidence

| Dimension | Before D-02 | After D-02 |
|-----------|-------------|------------|
| Quarantine-first discipline | Documented only | **Exercised** |
| Manual restore | Simulated (D-01) | **Executed** |
| Rollback map | Not used | **Drafted** |
| Operator readiness | Theoretical | **Practiced** |

**Human-operated safety:** Improved for Lane B sandbox work. Production survivability still requires HITL and scope locks.

---

## 10. SAFE UNKNOWN

- Human sign-off on this review not recorded
- Whether operator can execute same flow under incident stress
- Cross-platform path handling in production restore

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | D-02 first human-operated restore review |

---

*End of D-02 Human-Operated Restore Review v1.*
