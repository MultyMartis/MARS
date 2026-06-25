# REPORT — КОРВО НЕРО — V6 PRODUCTION SCOPE RECOVERY GATE

## 1. Preflight

| Field | Value |
|-------|-------|
| Branch | mars/post-cycle8-live-tests |
| HEAD | bf313e4 |
| v6 dataset | present — unchanged |
| Unrelated WIP | not modified |

## 2. V6 Rejection Registered

- Commander v6: **REJECTED BY OPERATOR — COMMERCIAL SCOPE LOSS**
- Review v6: **REJECTED BY OPERATOR — SEMANTIC AND CONTROLLED-TEST DEFECTS**
- Record: `production/audit/v6-operator-rejection-status.json`

## 3. Repair-Package Side Effects

- Commercial seed exclusions: **41**
- HOLD groups from empty-keyword rule: **8**
- Generic controlled-test hypotheses: **15**

## 4. Operator Service Scope

- Registry: `production/operator-service-scope-v1.json` — **31** service families
- All operator directions remain **MUST REPRESENT**; 8 groups flagged `recovery_required`

## 5. Commercial Phrase Recovery

- Phrases reviewed: **74**
- Restore ACTIVE: **41**
- Regression anchors: all **11** mapped to ACTIVE recovery

## 6. HOLD Group Review

- **CORV-G07-04** → ACTIVE NARROW (1 phrases)
- **CORV-G05-06** → ACTIVE NARROW (2 phrases)
- **CORV-G04-01** → ACTIVE NARROW (2 phrases)
- **CORV-G04-02** → ACTIVE NARROW (1 phrases)
- **CORV-G04-03** → ACTIVE NARROW (1 phrases)
- **CORV-G01-02** → ACTIVE NARROW (2 phrases)
- **CORV-G01-06** → ACTIVE (3 phrases)
- **CORV-G01-04** → ACTIVE NARROW (2 phrases)

## 7. Active Semantic Cleanup

- Informational/regulatory phrases flagged for v7 exclusion: **4**
- Anchors: `маркировка лекарств проверить`, `маркировка автозапчастей 2026`, `маркировка автозапчастей честный знак 2026`, `1с программист 2026`

## 8. Controlled-Test Rebuild

- Controlled tests in v6: **27**
- Generic hypotheses replaced: **15**

## 9. Status and Reason Consistency

- V6 contradictions: **59**
- Projected v7 after plan: **0**
- Gate: **PASS**

## 10. Negative Impact Plan

- Recovered groups mapped: **8**

## 11. Ad and Landing Impact

- CORV-G07-04: reuse v5 ad `ad-CORV-G07-04-a1`
- CORV-G05-06: reuse v5 ad `ad-CORV-G05-06-a1`
- CORV-G04-01: reuse v5 ad `ad-CORV-G04-01-a1`
- CORV-G04-02: reuse v5 ad `ad-CORV-G04-02-a1`
- CORV-G04-03: reuse v5 ad `ad-CORV-G04-03-a1`
- CORV-G01-02: reuse v5 ad `ad-CORV-G01-02-a1`
- CORV-G01-06: reuse v5 ad `ad-CORV-G01-06-a1`
- CORV-G01-04: reuse v5 ad `ad-CORV-G01-04-a1`

## 12. Production Scope Recovery Gate

**PASS — V7 PRODUCTION AUTHORIZED**

## 13. V7 Input Package or Blocker

Created `production/recovery/v7-production-input-package.json`

## 14. Evidence Workbook

`C:\AI MARS\projects\orca\projects\corvonero-yandex-direct\exports\CORVONERO-V6-SCOPE-RECOVERY-AUDIT.xlsx`

## 15. Files Created or Changed

- production/audit/v6-repair-package-side-effects.json/.md
- production/audit/v6-operator-rejection-status.json
- production/operator-service-scope-v1.json
- production/recovery/commercial-scope-recovery-registry.json/.md
- production/recovery/hold-group-review-v1.json/.md
- production/recovery/v6-active-semantic-cleanup.json/.md
- production/recovery/controlled-test-registry-v2.json/.md
- production/validation/status-reason-consistency-gate.json/.md
- production/recovery/negative-impact-plan-v7.json/.md
- production/recovery/ad-landing-impact-v7.json/.md
- production/validation/production-scope-recovery-gate.json/.md
- production/recovery/v7-production-input-package.json/.md
- exports/CORVONERO-V6-SCOPE-RECOVERY-AUDIT.xlsx
- artifacts/REPORT-orca-v6-production-scope-recovery.md

## 16. Git Status

No commit. No push. v6 production artefacts unchanged.

## 17. Remaining Issues

None blocking v7 production authorization.

## 18. Next Gate

**V7 PRODUCTION ONLY AFTER PRODUCTION SCOPE RECOVERY GATE PASSES** — gate passed; v7 dataset/XLSX generation authorized as separate task.

## 19. Stop Condition

Scope recovery audit complete. No dataset v7, Commander XLSX v7, import, split, or landing copy generated.
