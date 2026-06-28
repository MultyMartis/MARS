# CORVONERO NEW CONTROLLED SEMANTIC RUN — NEXT TASK v1

**Task ID:** `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-0-1-EXECUTION`  
**Prerequisite:** Operator approval of `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-OPERATOR-CHARTER-v1`  
**Date:** 2026-06-26  
**Mode:** Agent — Run Everything  
**Explicitly forbidden in this task:** full-corpus processing, Wave 5, strategy, SERP/Wordstat collection

---

## Objective

After charter approval, execute **Phase 0 final authority check** and **Phase 1 immutable input registration** only. Optionally run **Phase 2 closed-dataset SPPC-05 validation** if operator authorizes model calls in the same task charter.

---

## Entry criteria

- Gate A = `APPROVE_CHARTER` recorded in charter JSON approval fields
- Git branch = `mars/canonical-post-recovery`
- No active lock on proposed STORAGE root
- Old run declared `OLD_CORVONERO_RUN_NON_RESUMABLE`

---

## Allowed actions

1. **Final authority check**
   - Re-verify HEAD, corpus SHA-256 prefixes, ORCA Wave 3.1F file hashes
   - Confirm old-run isolation (no forensic cache in new run root)

2. **Instantiate new run identity**
   - Format: `corv-semantic-v2-<YYYYMMDD>-<sequence>`
   - Create run manifest (Git) — not started in preflight

3. **Create STORAGE root** (first write to runtime area)
   - `C:\MARS Phenix\AI MARS STORAGE\orca\corvonero\semantic-runs\<run_id>\`
   - Subdirs: `lock/`, `checkpoints/`, `batches/`, `raw-responses/`, `receipts/`

4. **Immutable input registration**
   - Copy input manifest checksums into run manifest
   - Register exactly 2368 phrase IDs from canonical registry
   - Verify row count, ID uniqueness, lineage evidence

5. **Lock/checkpoint initialization**
   - Atomic lock file with owner, heartbeat schema, corpus checksum
   - Empty processed-ID registry

6. **Closed-dataset SPPC-05 validation** (optional sub-phase)
   - Use existing safe test commands only:
     - `node projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs`
     - `node projects/orca/semantic-intelligence/live-model/tests/run-under-admission-regression.mjs`
     - `node projects/orca/semantic-intelligence/live-model/tests/run-problem-query-policy-regression.mjs`
     - `node projects/orca/semantic-intelligence/live-model/tests/run-wave31f-bypass-audit.mjs`
   - **Do not** process project corpus
   - Stop if adversarial FPR > 0.01

---

## Outputs

| Output | Placement |
|--------|-----------|
| Run manifest v1 | Git: `projects/mars-search-ppc-production/pilots/corvonero/runs/<run_id>/` |
| Lock record | STORAGE: `.../lock/run.lock.json` |
| Input registration receipt | Git + STORAGE receipt copy |
| SPPC-05 report (if run) | Git: pilots/corvonero/runs/<run_id>/reports/ |
| Phase 0/1 execution report | `projects/mars-search-ppc-production/reports/` |

---

## Stop conditions (fail-closed)

- Corpus hash mismatch vs charter
- Record count ≠ 2368
- Duplicate or missing phrase IDs
- ORCA file hash mismatch vs charter
- SPPC-05 failure
- Lock ownership conflict
- Operator rejection

---

## Stop after

Phase 0/1 complete (and SPPC-05 if authorized). **Do not** start canary or production batches without Gate B/C approval.

**Next gate:** Gate B/C per gate matrix.
