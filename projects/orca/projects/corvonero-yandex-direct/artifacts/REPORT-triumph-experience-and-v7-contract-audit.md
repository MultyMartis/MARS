# REPORT — ORCA — TRIUMPH EXPERIENCE RECOVERY AND CORVONERO V7 CONTRACT AUDIT

**Project:** `projects/orca/` + `projects/orca/projects/corvonero-yandex-direct/`  
**Branch:** `mars/post-cycle8-live-tests` @ `bf313e4`  
**Generated:** 2026-06-22

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` |
| HEAD | `bf313e4` |
| v7 artefacts | Present — dataset, registries, XLSX, validation suite |
| Triumph artefacts | Present — `ppc/triumph-manipulator/`, freezes, battle pilot |
| Import / moderation / launch / split / landing copy | **Not authorized** |
| Commander v8 | **Not created** |
| v7 production data | **Not modified** |
| Commit / push | **Not performed** |
| Unrelated WIP | Untouched (ocpilot, reports, `.recovery-temp/`, FP-0002) |

---

## 2. Triumph Evidence Located

Evidence inventory: `projects/orca/knowledge/triumph-manipulator-production-evidence-inventory.md`

**Key canonical sources:**

- Battle stable state: `freeze/battle-pilot-triumph-search-v1/TRIUMPH-SEARCH-RK-STABLE-STATE-v1.md`
- JSON instance: `ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json`
- Validation + export: `tools/validation-cli/`, `tools/exporter-cli/`, freezes under `freeze/ppc-exporter-production-baseline-v1/`
- Lessons: `freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md`

**SAFE UNKNOWN:** gitignored launch XLSX; operator-signed launch approval not in repo.

---

## 3. Canonical Triumph Production Process

Document: `projects/orca/knowledge/triumph-manipulator-production-process-v1.md`

16 stages reconstructed from evidence — scope freeze → JSON SoT → validation → cross-negatives → export → Commander dry-run → human post-import.

---

## 4. Reusable Laws Extracted

Document: `projects/orca/knowledge/triumph-derived-orca-laws-v1.md`  
Machine decisions: `projects/orca/knowledge/triumph-manipulator-production-decisions-v1.json`

15 ORCA laws formalized (ORCA-LAW-01 through ORCA-LAW-15).

---

## 5. Project-Specific Rules Excluded

Triumph-only: 5t/14m claims, Krasnodar geo, manipulator-triumph.ru URLs, 12-route slug taxonomy, Triumph fastlink pattern. Documented in laws file under project-specific section.

---

## 6. ORCA Campaign Production Contract

- `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md`
- `projects/orca/contracts/orca-campaign-production-contract-v1.json`

Authority order: operator decisions → scope → architecture → evidence → production rules → classifier (advisory) → QA → export.

---

## 7. Contract Invariants

`projects/orca/contracts/orca-campaign-production-invariants-v1.json` — 13 invariant classes including scope, seeds, HOLD, semantics, controlled tests, negatives, ads, inline-minus.

---

## 8. Pipeline Authority Defects

`projects/orca/architecture/orca-production-contract-integration-plan-v1.md`

Documents where Corvonero v1–v6 allowed classifier/repair/validator to override operator scope; integration plan defines contract gate above pipeline.

---

## 9. Contract Validator

- Tool: `projects/orca/tools/validate-campaign-production-contract.mjs`
- Tests: `projects/orca/tools/tests/validate-campaign-production-contract.test.mjs` — **all passed**
- Fixtures: Triumph success minimal + Corvonero v6 failure patterns

---

## 10. Corvonero V7 Operator Scope Audit

- 31/31 service families represented in export
- 41/41 protected seeds active
- 0 commercial seed loss
- 0 HOLD groups in dataset
- **6 high findings:** `operator-service-scope-v1.json` stale HOLD statuses for recovered services (authority file drift, not dataset defect)

---

## 11. Campaign Architecture Audit

- One unified campaign preserved (operator decision)
- 8 directions coherent
- 48 groups = distinct commercial intents
- No undetected hidden services

---

## 12. Group-by-Group Audit

48/48 groups PASS at contract level. Workbook sheet `Group-by-group audit` in `exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT.xlsx`.

---

## 13. Semantic Audit

- 283 contract-active phrases (ACTIVE + CONTROLLED TEST)
- 0 informational leakage in active set
- 0 duplicate ownership
- 0 long inline-minus repairs

---

## 14. Controlled-Test Audit

27/27 phrase-specific hypotheses; 0 generic templates.

---

## 15. Ads and Landing Audit

48/48 ads; base URL alignment PASS (UTM on ad URLs expected).

---

## 16. Negative Architecture Audit

Collision PASS; 0 blocking collisions; ownership-before-negatives discipline applied in v7 rebuild.

---

## 17. Contract Violations

| Severity | Count |
|----------|------:|
| Critical | 0 |
| High | 6 (scope registry sync only) |

---

## 18. Gate Decision

# PASS — V7 MAY PROCEED TO ACTUAL XLSX REVIEW AND COMMANDER DRY-RUN

Not operator-approved. Sync scope registry before sign-off.

---

## 19. ORCA/MARS Map Updates

- `projects/orca/OPERATIONAL-INDEX.md` — Campaign Production Contract section + Corvonero v7 gate
- `projects/orca/projects/corvonero-yandex-direct/OPERATIONAL-INDEX.md` — v7 contract audit gate

---

## 20. Files Created or Changed

**Created:**

- `projects/orca/knowledge/triumph-manipulator-production-evidence-inventory.md`
- `projects/orca/knowledge/triumph-manipulator-production-process-v1.md`
- `projects/orca/knowledge/triumph-manipulator-production-decisions-v1.json`
- `projects/orca/knowledge/triumph-derived-orca-laws-v1.md`
- `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md`
- `projects/orca/contracts/orca-campaign-production-contract-v1.json`
- `projects/orca/contracts/orca-campaign-production-invariants-v1.json`
- `projects/orca/architecture/orca-production-contract-integration-plan-v1.md`
- `projects/orca/tools/validate-campaign-production-contract.mjs`
- `projects/orca/tools/tests/validate-campaign-production-contract.test.mjs`
- `projects/orca/tools/fixtures/campaign-contract/triumph-success-minimal-v1.json`
- `projects/orca/tools/fixtures/campaign-contract/corvonero-v6-failure-patterns-v1.json`
- `projects/orca/projects/corvonero-yandex-direct/production/validation/orca-contract-audit-config-v7.json`
- `projects/orca/projects/corvonero-yandex-direct/production/validation/orca-production-contract-audit-v7.json`
- `projects/orca/projects/corvonero-yandex-direct/production/validation/orca-production-contract-audit-v7.md`
- `projects/orca/projects/corvonero-yandex-direct/tools/generate-triumph-contract-audit-v7.cjs`
- `projects/orca/projects/corvonero-yandex-direct/exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT.xlsx`
- `projects/orca/projects/corvonero-yandex-direct/artifacts/REPORT-triumph-experience-and-v7-contract-audit.md`

**Modified:**

- `projects/orca/OPERATIONAL-INDEX.md`
- `projects/orca/projects/corvonero-yandex-direct/OPERATIONAL-INDEX.md`

**Not modified:** v7 production JSON/XLSX data; unrelated WIP.

---

## 21. Git Status

Corvonero tree largely untracked (`??`). New ORCA contract/knowledge/tools files untracked. Unrelated modified: `projects/ocpilot/...`, pre-existing `projects/orca/OPERATIONAL-INDEX.md` modification.

**Selective commit scope (after operator approval):**

```
projects/orca/knowledge/
projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md
projects/orca/contracts/orca-campaign-production-contract-v1.json
projects/orca/contracts/orca-campaign-production-invariants-v1.json
projects/orca/architecture/orca-production-contract-integration-plan-v1.md
projects/orca/tools/validate-campaign-production-contract.mjs
projects/orca/tools/tests/
projects/orca/tools/fixtures/campaign-contract/
projects/orca/OPERATIONAL-INDEX.md
projects/orca/projects/corvonero-yandex-direct/production/validation/orca-contract-audit-config-v7.json
projects/orca/projects/corvonero-yandex-direct/production/validation/orca-production-contract-audit-v7.*
projects/orca/projects/corvonero-yandex-direct/tools/generate-triumph-contract-audit-v7.cjs
projects/orca/projects/corvonero-yandex-direct/exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT.xlsx
projects/orca/projects/corvonero-yandex-direct/artifacts/REPORT-triumph-experience-and-v7-contract-audit.md
projects/orca/projects/corvonero-yandex-direct/OPERATIONAL-INDEX.md
```

Exclude: ocpilot WIP, reports/FP-0002, `.recovery-temp/`, unrelated workspaces.

---

## 22. Remaining Manual Checks

1. Operator opens actual `CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx`
2. Commander desktop dry-run
3. Sync `operator-service-scope-v1.json` (6 HOLD → ACTIVE)
4. Operator commercial sign-off
5. Landing publication before launch

---

## 23. Next Gate

**IF PASS (current):** ACTUAL V7 XLSX REVIEW AND COMMANDER DRY-RUN

**IF scope sync deferred:** complete registry sync before operator approval

**IF future BLOCKED:** CONTRACT-GUIDED V7 CORRECTION PLAN → controlled v8 (not authorized now)

---

## 24. Stop Condition

Task complete. Stopped after:

- Triumph production experience recovered and documented
- ORCA Campaign Production Contract created with invariants and validator
- Corvonero v7 audited independently — **PASS**
- Maps updated
- No v8, no v7 data mutation, no import, no commit
