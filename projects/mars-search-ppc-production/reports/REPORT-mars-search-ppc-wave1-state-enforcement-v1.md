# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 1 STATE ENFORCEMENT V1

**Date:** 2026-06-22  
**Branch:** `mars/post-cycle8-live-tests`  
**Lifecycle checkpoint commit:** `43c4271` — `docs(ppc): approve search production lifecycle v1`  
**Wave 1 runtime status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (uncommitted)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` ✓ |
| P0-I diagnostic checkpoint `a81cac2` | Present in history ✓ |
| Lifecycle package | Committed at `43c4271` ✓ |
| Cross-system references | Committed (orca OPERATIONAL-INDEX, mig README, mars-reality-index) ✓ |
| Corvonero | `FROZEN` — not resumed ✓ |
| Unrelated WIP staged | No — selective checkpoint only ✓ |
| HEAD before checkpoint | `66dacef`; after checkpoint `43c4271` |

---

## 2. Operator Decisions W1-D1–W1-D7

| ID | Decision | Record |
|----|----------|--------|
| W1-D1 | MARS SEARCH PPC PRODUCTION LIFECYCLE V1 — APPROVED | [decisions/WAVE-1-OPERATOR-APPROVAL-v1.md](../decisions/WAVE-1-OPERATOR-APPROVAL-v1.md) |
| W1-D2 | WAVE 1 — AUTHORIZED | Same |
| W1-D3 | Valid manifest required before lifecycle work | Manifest schema v2 + template |
| W1-D4 | Web-GPT/Cursor entry-point enforcement | Execution contracts updated |
| W1-D5 | `BLOCKED — LIFECYCLE REQUIREMENT NOT MET` on missing evidence | Runtime fail-closed |
| W1-D6 | Bulk manual phrase classification prohibited as default | `human-review-boundary.mjs` |
| W1-D7 | Corvonero read-only manifest; no production resume | [corvonero manifest](../../orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json) |

---

## 3. Lifecycle Approval

| From | To |
|------|-----|
| `PROPOSED — OPERATOR APPROVAL REQUIRED` | `APPROVED — IMPLEMENTATION AUTHORIZED` |

Updated: lifecycle README, primary lifecycle doc, machine contract, operator decision record, gap audit summary, integration map, repair roadmap header.

---

## 4. Selective Lifecycle Checkpoint

**Commit:** `43c4271` — pushed to `origin/mars/post-cycle8-live-tests`

**Included:** Full `projects/mars-search-ppc-production/` package (pre-runtime), cross-refs in orca/mig/governance.

**Excluded:** Wave 1 `runtime/`, Corvonero WIP, Website Factory, OCPilot, `.recovery-temp/`, P0-D benchmark WIP.

---

## 5. Runtime Locus

Created `projects/mars-search-ppc-production/runtime/`:

```text
runtime/
├── README.md
├── cli/search-ppc.mjs
├── src/ (constants, manifest-normalize, transition-engine, artifact-resolver,
│         corpus-enforcement, human-review-boundary, degraded-evidence,
│         blocker-report, validate-lifecycle)
├── config/lifecycle-defaults.json
├── schemas/ (manifest v2, blocker report, cursor task, degraded evidence)
├── fixtures/ (valid/invalid examples + synthetic cases)
├── tests/run-synthetic-matrix.mjs
└── reports/ (synthetic + corvonero validation outputs)
```

---

## 6. Project Manifest Implementation

| Artifact | Path |
|----------|------|
| Schema v2 | `runtime/schemas/project-ppc-state-manifest-v2.schema.json` |
| Template v2 | `state/project-ppc-state-manifest-template-v2.json` |
| Valid example | `runtime/fixtures/example-valid-manifest-v2.json` |
| Invalid example (pilot corpus) | `runtime/fixtures/example-invalid-pilot-corpus-v2.json` |
| Legacy v1 template | Preserved at `state/project-ppc-state-manifest-template-v1.json` |

Normalizer supports legacy v1 manifests (`stage_statuses`, `artifacts`).

---

## 7. Stage Transition Engine

`runtime/src/transition-engine.mjs`:

- Valid transitions: NOT STARTED → IN PROGRESS → READY FOR REVIEW → APPROVED → COMPLETED
- Supports BLOCKED, FAILED, FROZEN, COMPLETED WITH APPROVED DEGRADATION, SUPERSEDED, reopen trace warning
- Forbidden starts: SPPC-08 before admission/ownership, SPPC-13 before SPPC-12, SPPC-20 before SPPC-19, etc.
- CLI: `transition ... --dry-run` (never mutates manifest)

---

## 8. Artifact Resolution

`runtime/src/artifact-resolver.mjs` verifies:

- Path existence, project ownership, corpus mode, diagnostic-only flag, superseded status, approval, collection date, region metadata, downstream generation flags

Disk existence alone is insufficient when artifact is diagnostic, cross-project, or pilot-substituted.

---

## 9. Full-Corpus Enforcement

`runtime/src/corpus-enforcement.mjs`:

- Distinguishes PRODUCTION FULL CORPUS vs TECHNICAL PILOT / BENCHMARK / DIAGNOSTIC SAMPLE / RANDOM QA SAMPLE / HUMAN REVIEW SUBSET
- Blocks SPPC-03 completion when pilot substituted, counts mismatch, or exclusions undocumented
- Blocker: `BLOCKED — FULL PRODUCTION CORPUS NOT REGISTERED`

---

## 10. Human-Review Boundary

`runtime/src/human-review-boundary.mjs`:

- Detects whole-corpus manual classification, wholesale ABSTAIN routing, missing automation, automation claims with full manual review
- Blocker: `BLOCKED — HUMAN REVIEW HAS BECOME PRIMARY CLASSIFICATION ENGINE`
- Quantitative queue limits: **SAFE UNKNOWN** (policy-based only)

---

## 11. Web-GPT Entry Contract

Updated:

- [web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md](../web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md) — APPROVED status
- [web-gpt/WEB-GPT-OPENING-STATUS-BLOCK-v1.md](../web-gpt/WEB-GPT-OPENING-STATUS-BLOCK-v1.md) — full opening block + MARS sync instruction

---

## 12. Web-GPT Source/Sync Integration

Updated:

- [web-gpt-sources/WEB-GPT-CHAT-SYNC-PACK.md](../../../web-gpt-sources/WEB-GPT-CHAT-SYNC-PACK.md) — Search PPC sync block
- [web-gpt-sources/WEB-GPT-SOURCE-PACK-INDEX.md](../../../web-gpt-sources/WEB-GPT-SOURCE-PACK-INDEX.md) — lane add-on row

Concise references only — no duplication of 23 stage contracts.

---

## 13. Cursor Task Gate

Updated [cursor/CURSOR-SEARCH-PPC-TASK-STARTER-v1.md](../cursor/CURSOR-SEARCH-PPC-TASK-STARTER-v1.md):

- Required fields: manifest path, requested transition, validator before/after, git scope
- Machine-readable example: `cursor/cursor-search-ppc-task-contract-example-v1.json`
- Schema: `runtime/schemas/cursor-search-ppc-task-contract-v1.schema.json`

---

## 14. Validator CLI

| Command | Status |
|---------|--------|
| `validators/validate-search-ppc-lifecycle.mjs <manifest>` | ✓ delegates to runtime |
| `runtime/cli/search-ppc.mjs status <manifest>` | ✓ |
| `runtime/cli/search-ppc.mjs can-start <manifest> <stage-id>` | ✓ |
| `runtime/cli/search-ppc.mjs transition <manifest> <stage-id> <status> --dry-run` | ✓ |
| `runtime/cli/search-ppc.mjs report <manifest>` | ✓ |

Fail-closed; exit 2 on BLOCKED; JSON + Markdown output; dry-run preserves manifest.

---

## 15. Blocker Report Contract

`runtime/src/blocker-report.mjs` + schema `runtime/schemas/blocker-report-v1.schema.json`

Required fields implemented: STATUS, Project, Current stage, Requested action, Missing inputs, Invalid evidence, Required system/role, Allowed next action, Forbidden until resolved, Degraded mode YES/NO, Operator approval YES/NO.

---

## 16. Degraded-Evidence Enforcement

`runtime/src/degraded-evidence.mjs` + schema `runtime/schemas/degraded-evidence-record-v1.schema.json`

Validates required degraded record fields; blocks COMPLETED WITH APPROVED DEGRADATION without operator approval; paid SERP degradation path for SPPC-10.

Blocker: `BLOCKED — DEGRADED EVIDENCE MODE NOT APPROVED`

---

## 17. Corvonero Read-Only Manifest

**Path:** `projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json`

| Property | Value |
|----------|-------|
| lifecycle_status | FROZEN |
| current_lifecycle_stage | SPPC-05 (FAILED diagnostic admission) |
| SPPC-01–04 | COMPLETED with verified evidence paths |
| P0-I 200-phrase pilot | Classified DIAGNOSTIC SAMPLE |
| Paid SERP / analytical pack / strategy / campaign | Not claimed |
| Production resume | Forbidden |

---

## 18. Corvonero Validation Results

```bash
node validators/validate-search-ppc-lifecycle.mjs \
  projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json
# exit 2 — BLOCKED — PROJECT FROZEN
```

| Check | Result |
|-------|--------|
| can-start SPPC-14 (Campaign Production) | **blocked** — FROZEN |
| can-start SPPC-20 (Commander Export) | **blocked** — FROZEN |
| can-start SPPC-22 (Launch) | **blocked** — FROZEN |
| MIG evidence vs paid advertising | Distinguished — source/corpus registered; paid SERP absent |
| Diagnostic pilot vs full corpus | Distinguished — full corpus 2370 rows; P0-I diagnostic separate |
| Next actions | Await Wave 1 approval + Wave 2–3 charter |

Reports: `runtime/reports/corvonero-validation-v1.json`, `.md`

---

## 19. Synthetic Test Matrix

**Command:** `node runtime/tests/run-synthetic-matrix.mjs`  
**Result:** **20/20 PASS**

All 20 charter cases assert exit code, status, blocker codes, allowed/forbidden actions.

Output: `runtime/reports/synthetic-matrix-results-v1.json`

---

## 20. Bypass Re-Audit

Document: [MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-v1.md](./MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-v1.md)

| Disposition | Count |
|-------------|------:|
| CLOSED | 4 |
| PARTIALLY CLOSED | 8 |
| OPEN | 6 |
| NOT TESTED | 2 |

No bypass marked CLOSED on documentation alone.

---

## 21. Wave 1 Maturity Assessment

| Component | Status |
|-----------|--------|
| Lifecycle authority | **OPERATIONAL** (approved + checkpointed) |
| Project manifest | **IMPLEMENTED — TESTED** |
| Transition engine | **IMPLEMENTED — TESTED** |
| Artifact resolver | **IMPLEMENTED — PARTIALLY TESTED** |
| Full-corpus enforcement | **IMPLEMENTED — TESTED** |
| Human-review boundary | **IMPLEMENTED — TESTED** |
| Degraded mode | **IMPLEMENTED — PARTIALLY TESTED** |
| Web-GPT entry contract | **IMPLEMENTED — NOT VALIDATED AT SCALE** |
| Sync pack integration | **IMPLEMENTED — NOT VALIDATED AT SCALE** |
| Cursor task gate | **IMPLEMENTED — TESTED** (schema + example) |
| Validator CLI | **IMPLEMENTED — TESTED** |
| Blocker reports | **IMPLEMENTED — TESTED** |
| Corvonero read-only manifest | **IMPLEMENTED — TESTED** |

**Wave 1 overall:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED`  
**Not granted:** `OPERATIONAL` for Wave 1 enforcement at subsystem entry points.

---

## 22. Map and Roadmap Updates

| Item | Status |
|------|--------|
| Search PPC Lifecycle v1 | `APPROVED — CHECKPOINTED` |
| Wave 1 | `IMPLEMENTED — OPERATOR REVIEW REQUIRED` |
| Wave 2 | `BLOCKED UNTIL WAVE 1 APPROVAL` |
| Corvonero | `FROZEN` |
| P0-I pilot | `DIAGNOSTIC EVIDENCE` |
| P0-D | `ON HOLD` |
| Campaign Production | blocked (manifest/validator) |
| Commander | blocked (manifest/validator) |

Updated in roadmap v1 (uncommitted), orca OPERATIONAL-INDEX (checkpoint), mars-reality-index (checkpoint).

---

## 23. Files Created or Changed

**Checkpoint commit (`43c4271`):** 68 files — full lifecycle package + 3 cross-refs.

**Wave 1 uncommitted (operator review):**

- `projects/mars-search-ppc-production/runtime/**`
- `projects/mars-search-ppc-production/state/project-ppc-state-manifest-template-v2.json`
- `projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs` (rewired)
- `projects/mars-search-ppc-production/validators/README.md`
- `projects/mars-search-ppc-production/cursor/*` (updates)
- `projects/mars-search-ppc-production/web-gpt/*` (updates)
- `projects/mars-search-ppc-production/reports/MARS-SEARCH-PPC-BYPASS-RE-AUDIT-WAVE1-v1.md`
- `projects/mars-search-ppc-production/reports/REPORT-mars-search-ppc-wave1-state-enforcement-v1.md`
- `projects/mars-search-ppc-production/roadmap/*` (Wave 1 status)
- `projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json`
- `projects/orca/projects/corvonero-direct-v2-clean-room/PROJECT.md`
- `web-gpt-sources/WEB-GPT-CHAT-SYNC-PACK.md`
- `web-gpt-sources/WEB-GPT-SOURCE-PACK-INDEX.md`

---

## 24. Git Status

- **Committed + pushed:** lifecycle approval checkpoint `43c4271`
- **Uncommitted:** Wave 1 runtime and enforcement (by design — operator review gate)
- **Not started:** Wave 2; Corvonero production resume; MIG paid SERP collection

---

## 25. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Numeric human-review queue threshold | SAFE UNKNOWN — policy-based detection only; pending operator approval |
| Web-GPT technical enforcement | SAFE UNKNOWN — contract/sync only; no Web-GPT runtime hook |
| MIG/ORCA/Campaign CLI `--manifest` wiring | Not implemented — Wave 1 W1-04 partial |
| Subsystem-scale validator performance | NOT VALIDATED AT SCALE |

---

## 26. Operator Approval Items

1. Review Wave 1 runtime diff (uncommitted)
2. Approve or reject `IMPLEMENTED — OPERATOR REVIEW REQUIRED` for Wave 1
3. Authorize commit of Wave 1 runtime if approved
4. Authorize Wave 2 (MIG paid SERP mode) after Wave 1 approval
5. Do **not** unfreeze Corvonero until Wave 2–3 charter

---

## 27. Recommended Wave 2 Boundary

Wave 2 scope only:

- MIG `PAID SERP — BUSINESS HOURS` mode
- Source registry date passport enforcement
- Full-corpus intake producer aligned to SPPC-02/03
- Competitor audit pack schema v1
- **No** Corvonero paid SERP collection until explicit unfreeze charter

---

## 28. Stop Condition

**Stopped after:**

- ✓ Lifecycle checkpoint committed and pushed
- ✓ Wave 1 runtime implemented (uncommitted)
- ✓ Corvonero read-only manifest + validation
- ✓ Synthetic matrix 20/20
- ✓ Bypass re-audit complete

**Not done (by design):**

- Wave 1 self-approval as OPERATIONAL
- Wave 2 start
- Corvonero resume / MIG collection / strategy / campaigns / Commander / launch
- Commit of unapproved Wave 1 runtime

**Next gate:** OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 1
