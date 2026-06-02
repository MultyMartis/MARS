# D-02 Survivability Readiness Assessment (v1)

**Status:** Post-drill readiness assessment — documentation only  
**Drill id:** D-02  
**Date:** 2026-05-24  
**Baseline:** D-01 operational drill + D-02 manual restore drill

---

## Layer readiness table

| Layer | Status | Notes |
|-------|--------|-------|
| **G0** — Awareness & halt discipline | **READY (doc)** | Halt/quarantine protocols exist; drill exercised quarantine-first |
| **G1** — Snapshot discipline | **READY (drill)** | Manifest + partial mirror work; partial gap documented |
| **G2** — Pre-execution validation | **READY (drill)** | Validator not re-run in D-02; D-01 proved DENY path |
| **G3** — Drift detection | **READY (drill)** | diff-report-helper + hash compare; content scan gap remains |
| **G4** — Recovery & rollback | **READY (drill)** | First real manual restore + rollback map draft |
| **Rollback readiness** | **MODERATE** | Human-operated flow proven in sandbox; no automation |
| **Operational resilience** | **MODERATE** | Logging + tooling assist; operator load remains |
| **Human-operated safety** | **MODERATE-HIGH** | Quarantine + selective restore clear |
| **Production survivability** | **LOW-MODERATE** | Triumph/production not exercised; hooks absent |

**Legend:** READY (drill) = proven in sandbox drill only, not production.

---

## What is now significantly safer

1. **Quarantine-first workflow** — exercised, not theoretical
2. **Manual selective restore** — snapshot parity verified by hash
3. **Drift artifact exclusion** — suspicious-spread.md not carried to restored tree
4. **Rollback map schema** — first JSON draft with ordering + quarantine refs
5. **Audit trail** — rollback-history + survivability logs for D-02
6. **Restore-to-new-workspace pattern** — avoids repairing contaminated tree

---

## What remains dangerous

1. **No automated enforcement** — agent can still run destructive shell
2. **Partial snapshots** — unm mirrored files (index.html) require operator judgment
3. **Production workspaces** — Triumph v4/v5 not drill-tested
4. **Untracked files** — git diff unavailable for sandbox
5. **Zone label noise** — PROTECTED-ZONE-HIT on every sandbox path
6. **Incident-time operator stress** — drill ≠ real incident

---

## Remaining weaknesses

| Weakness | Severity | D-02 impact |
|----------|----------|-------------|
| Partial mirror gaps | Medium | index.html sourced from quarantine |
| Manifest path staleness | Low | workspace field not updated |
| No Cursor hooks | By design | Validator CLI-only |
| Registry RD-030 | Low | Pre-existing |
| Quarantine retention policy | Low | Drill artifacts retained |

---

## Recommended G5 (next phase)

| G5 focus | Action |
|----------|--------|
| **G5a — Production-scoped drill** | Tabletop only: Triumph path restore from real snapshot (HITL, no agent) |
| **G5b — Partial mirror checklist** | Add to snapshot-manifest-standard: unm mirrored file handling |
| **G5c — Restore runbook** | Single OPERATIONAL-INDEX entry linking D-01/D-02 flow |
| **G5d — Hook experiment** | Optional: pre-shell validator hook (charter required) |
| **G5e — Quarantine lifecycle** | Archive policy for `workspaces/_quarantine/` |

---

## Comparison to scorecard (2026-05-23)

| Domain | Pre-D-02 (scorecard) | Post-D-02 (drill evidence) |
|--------|----------------------|----------------------------|
| Snapshot discipline | HIGH RISK | **MEDIUM** in sandbox — manifest + mirror used |
| Rollback readiness | HIGH RISK | **MEDIUM** — manual flow proven |
| Recovery speed | MEDIUM RISK | **MEDIUM** — manual steps add time but safer |
| Agent safety | HIGH RISK | **HIGH** — unchanged (no hooks) |

---

## SAFE UNKNOWN

- Long-term retention of D-01/D-02 drill artifacts
- Operator sign-off on readiness table
- Whether rollback map JSON will be maintained in real incidents

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | D-02 post-restore readiness assessment |

---

*End of D-02 Survivability Readiness v1.*
