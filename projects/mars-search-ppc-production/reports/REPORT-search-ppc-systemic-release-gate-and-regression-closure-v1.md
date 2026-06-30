# REPORT — Search PPC Systemic Release Gate and Regression Closure v1

**Date:** 2026-06-30  
**Branch:** `mars/canonical-post-recovery`  
**Verdict:** PASS — see §10

---

## 1. Audit findings

### Existing shared capabilities (pre-task)

| Capability | Location | Notes |
|------------|----------|-------|
| Filesystem guard (X: / AI WS) | `filesystem-guard.mjs` | Executable |
| Template SHA + structure validator | `template-validator.mjs` | Executable |
| Authority loader + SHA policy | `authority-loader.mjs` | Executable |
| Pre-generation transport validator | `transport-validator.mjs` | Validates JSON authority, not XLSX |
| Payload builder | `payload-builder.mjs` | Executable |
| Commander patcher adapter | `commander-patcher-adapter.mjs` | Triumph exporter-cli wrapper |
| Workbook forensic (callouts/URLs) | `workbook-forensic-verifier.mjs` | Partial — callouts + URLs only |
| Output verifier | `output-verifier.mjs` | Reopens XLSX but limited scope |
| Bid ladder (Triumph + Corvonero) | `bid-ladder.mjs` | Executable |
| E9 clear hotfix (V2.6.1) | `clearCampaignNegativesMetadataCell` | Post-patch only; truthiness bug in `translateMetadataPatches` |

### Documentation-only rules (pre-task)

- SPPC lifecycle stages SPPC-19..22 describe QA/import but no executable release gate
- Triumph survivability validation rules — human docs only
- Corvonero forensic validation reports — per-campaign scripts, not shared gate
- Operator approval implied by `operator_approval_state` in manifest — not receipt-based

### Project-specific rules

- Corvonero campaign generators (`pilots/corvonero/tools/execute-campaign-v*.mjs`)
- Corvonero bid policy `CORVONERO_BALANCED_CYCLIC_10_RUB_V1`
- Corvonero phrase authority V2.6 JSON artifacts
- Triumph S-tier draft instances (orca/ppc/triumph-manipulator)

### Bypass points (pre-task)

1. `translateMetadataPatches`: `value !== ''` filtered empty string → preserve template E9
2. No mandatory template sanitization before patch
3. `transport-validator` PASS did not reopen actual XLSX
4. Corvonero generators declared PASS without operator semantic receipt
5. No release state model — states conflated
6. Shared template is Triumph production template with client contamination

### Template contamination sources

- `triumph-manipulator-commander-template-v1.xlsx` E9: ремонт/запчасти/эвакуатор
- E11: `https://manipulator-triumph.ru/`
- E12 / col 50: organization ID `29500847237`
- Stale demo phrases/ads in template data rows

### Validation gaps (pre-task)

- No authority-to-artifact reconciliation
- No differential validator for hotfixes
- No checksum re-verification in gate
- No foreign-client contamination scan in shared tooling
- PASS status ambiguous (script vs semantic vs launch)

### PASS-status ambiguity (pre-task)

Scripts reported `PASS`/`FAIL` on authority JSON validation. Corvonero forensic reports used `PASS — FORENSIC VALIDATION COMPLETE` without distinguishing operator semantic approval or launch readiness.

---

## 2. Implemented systemic changes

| Component | Implementation |
|-----------|----------------|
| Metadata operation model | `src/metadata-operation-model.mjs` — MISSING/PRESERVE/EXPLICIT_CLEAR/SET_VALUE |
| Template sanitization | `src/template-sanitizer.mjs` + manifest JSON |
| Template contract | `contracts/commander-template-contract-v1.json` |
| Artifact XLSX validator | `src/artifact-xlsx-validator.mjs` — reopens actual files |
| Authority reconciliation | `src/authority-artifact-reconciler.mjs` |
| Differential validator | `src/differential-validator.mjs` — hotfix mode |
| Release state model | `src/release-state.mjs` + schema |
| Operator approval receipt | `src/operator-approval-receipt.mjs` + schema |
| Release gate | `src/release-gate.mjs` + CLI |
| Checksum manifest | `src/checksum-manifest.mjs` |
| Regression corpus | `contracts/search-ppc-regression-corpus-v1.json` |
| Commander adapter integration | Sanitization + typed metadata in `commander-patcher-adapter.mjs` |

### Documentation (11 specs)

`docs/release-gate/CAMPAIGN-RELEASE-STATE-MODEL-v1.md` through `SEARCH-PPC-OPERATOR-RELEASE-WORKFLOW-v1.md`

---

## 3. Triumph reconciliation

| Category | Items |
|----------|-------|
| **Reused executable** | exporter-cli patch, header map, bid ladder, callout serializer, URL policy, template SHA |
| **Was documented only** | Survivability rules, import observations, metadata block docs |
| **Was missing, now generalized** | Release gate, artifact validation, sanitization, metadata ops, differential validation |
| **Remains project-specific** | Triumph semantic prompts, S-tier draft JSON, Triumph promotion URL as template default |
| **Template reality** | No neutral template exists — Triumph template used with mandatory sanitization |

Full detail: `docs/release-gate/TRIUMPH-CORVONERO-SYSTEMIC-RECONCILIATION-v1.md`

---

## 4. Corvonero reconciliation

| Version | Status |
|---------|--------|
| **V2.6** | Semantic authority baseline — **unchanged** |
| **V2.6.1** | Generation hotfix (E9 clear) — registered as hotfix candidate |
| **V2.7** | **Not created** |
| **Semantic change** | **None** performed in this task |

Release state: `pilots/corvonero/CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json`

- `AUTHORITY_FROZEN`: true
- `OPERATOR_SEMANTIC_APPROVED`: false (no explicit prior receipt in repo)
- `GENERATION_COMPLETE`: true
- `ARTIFACT_VALIDATED`: true (per V2.6/V2.6.1 forensic reports; independent operator review may still be pending)
- `OPERATOR_IMPORT_READY`: false
- `COMMANDER_IMPORTED`: false
- `LAUNCH_APPROVED`: false

---

## 5. Test results

| Metric | Value |
|--------|-------|
| Total tests | 86 |
| Passed | 86 |
| Failed | 0 |
| Duration | ~14s |

### New test suites

- `metadata-operation-model.test.mjs` — 8 tests
- `template-sanitizer.test.mjs` — 3 tests
- `artifact-xlsx-validator.test.mjs` — 3 tests (includes actual XLSX patch + E9 verify)
- `differential-validator.test.mjs` — 4 tests
- `release-gate.test.mjs` — 3 tests

### Synthetic fixture validation

| Scenario | Result |
|----------|--------|
| Stale E9 in template detected | PASS |
| Sanitizer + explicit clear → E9 null in actual XLSX | PASS |
| Release gate fails without receipt | PASS |
| Release gate fails when E9 repopulated | PASS |
| Release gate passes clean fixture + approval | PASS |
| Hotfix differential allows E9-only change | PASS |
| Hotfix differential rejects phrase change | PASS |

Fixtures used: `fixtures/valid-synthetic/`, `.tools-test-output/` synthetic workbooks (not production Corvonero packages).

---

## 6. Remaining limitations

| Limitation | Notes |
|------------|-------|
| Semantic judgement | Requires operator — automation provides `SEMANTIC_AUDIT_READY_FOR_REVIEW` only |
| Commander import reconciliation | Not automated — operator task post-import |
| Direct launch | Operator-controlled — `LAUNCH_APPROVED` never set by automation |
| Neutral Commander template | **SAFE UNKNOWN** whether a clean template will be created separately; current path uses sanitization |
| Corvonero release gate on production package | Not run against Storage production paths in this task (read-only policy respected) |
| Full per-field metadata contract enforcement | Core fields implemented; extended contact/business-card fields classified in contract, partial validator coverage |

---

## 7. Scoped checkpoint file list (future git checkpoint)

### New files

```
projects/mars-search-ppc-production/docs/release-gate/*.md (12 files)
projects/mars-search-ppc-production/tools/commander-transport/contracts/*.json (6 files)
projects/mars-search-ppc-production/tools/commander-transport/src/metadata-operation-model.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/template-sanitizer.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/artifact-xlsx-validator.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/authority-artifact-reconciler.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/differential-validator.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/operator-approval-receipt.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/release-state.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/release-gate.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/release-gate-cli.mjs
projects/mars-search-ppc-production/tools/commander-transport/src/checksum-manifest.mjs
projects/mars-search-ppc-production/tools/commander-transport/tests/metadata-operation-model.test.mjs
projects/mars-search-ppc-production/tools/commander-transport/tests/template-sanitizer.test.mjs
projects/mars-search-ppc-production/tools/commander-transport/tests/artifact-xlsx-validator.test.mjs
projects/mars-search-ppc-production/tools/commander-transport/tests/differential-validator.test.mjs
projects/mars-search-ppc-production/tools/commander-transport/tests/release-gate.test.mjs
projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json
projects/mars-search-ppc-production/reports/REPORT-search-ppc-systemic-release-gate-and-regression-closure-v1.md
```

### Modified files

```
projects/mars-search-ppc-production/README.md
projects/mars-search-ppc-production/tools/commander-transport/README.md
projects/mars-search-ppc-production/tools/commander-transport/package.json
projects/mars-search-ppc-production/tools/commander-transport/src/commander-patcher-adapter.mjs
```

### Explicitly excluded from checkpoint scope

- Corvonero V2–V2.6 historical packages in Storage
- `.tools-test-output/` generated test artifacts
- Unrelated `.recovery-temp/` and foreign WIP
- FP-0002 or other pilot WIP

---

## 8. Git status

**No commit performed** per task policy.

---

## 9. Security / UNKNOWN

- **SECURITY RISK:** None introduced — read-only on production packages; writes limited to repo test output dirs.
- **UNKNOWN:** Whether operator will create a dedicated neutral Commander template vs continued sanitization of Triumph template.

---

## 10. Verdict

```
MARS SEARCH PPC SYSTEMIC CLOSURE:
PASS — SHARED CAMPAIGN RELEASE GATE AND REGRESSION PROTECTION IMPLEMENTED

Template contract:           IMPLEMENTED
Three-state metadata semantics: IMPLEMENTED
Template sanitization:       IMPLEMENTED
Actual XLSX artifact validation: IMPLEMENTED
Authority-to-artifact reconciliation: IMPLEMENTED
Differential validation:     IMPLEMENTED
Operator approval receipt:   IMPLEMENTED
Release state model:       IMPLEMENTED
Triumph regression corpus:   IMPLEMENTED
Corvonero regression corpus: IMPLEMENTED
Release gate tests:          PASS (86/86)

Production campaign changes: NONE
Commander import:            NOT PERFORMED
Git checkpoint:              NOT PERFORMED
```
