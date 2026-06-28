# REPORT — CORVONERO NEW CONTROLLED SEMANTIC RUN PREFLIGHT V1

**Date:** 2026-06-26  
**Repository:** `C:\MARS Phenix\AI MARS`  
**Branch:** `mars/canonical-post-recovery` @ `ebc65acd4087fa9d180bb2a50921027fde51e3b7`  
**Task:** Preflight + authority verification + operator charter preparation  
**Preliminary verdict:** **`READY_FOR_OPERATOR_CHARTER_APPROVAL`**

---

## 1. Safety and Scope

This task performed **read-only** authority verification and created **documentation only**. Explicitly **not** executed:

- Semantic run / model calls on project corpus
- Runtime lock or checkpoint creation
- ORCA/MIG code changes
- Wordstat/SERP collection
- Wave 5 / strategy / campaign work
- Git commit or push

Destructive operations guard observed.

---

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` ✓ |
| HEAD | `ebc65acd4087fa9d180bb2a50921027fde51e3b7` ✓ **exact match** |
| Recovery branch | `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e` ✓ |
| Corvonero-scoped dirty paths | **None** |
| Unrelated WIP | Untracked only (ocpilot backups, recovery-temp, etc.) — untouched |

---

## 3. Canonical Project Locus

| Role | Path | Notes |
|------|------|-------|
| **Preflight/charter (new)** | `projects/mars-search-ppc-production/pilots/corvonero/` | Created this task — preferred locus did not exist |
| Operational freeze/state | `projects/orca/projects/corvonero-direct-v2-clean-room/` | Lifecycle manifest, diagnostic freeze |
| MIG session | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` | Complete handoff pack |
| ATLAS | `projects/atlas/population/` + reports | Entity registration |
| Search PPC lifecycle | `projects/mars-search-ppc-production/` | Wave block, Corvonero FROZEN |

---

## 4. ATLAS Authority

| Entity | Present | Current state | Authority file | Notes |
|--------|--------:|---------------|----------------|-------|
| ORG-0009 | Yes | Registered | `ATLAS-CORVONERO-*-REGISTER-v1.md` | Центр автоматизации «Корво Неро» |
| LE-0006 | Yes | Registered | same | ИП Никифоров Р.В. |
| PRJ-0013 | Yes | Registered | same | Corvonero Yandex Direct project |
| WEB-CORV-01 | Yes | Registered | `ATLAS-CORVONERO-WEBSITE-*` | **Ownership SAFE UNKNOWN** |
| DOM-CORV-01 | Yes | Registered | `ATLAS-CORVONERO-DOMAIN-*` | `corvonero.ru` secondary/Tilda |
| REL-0042 | Yes | Active | `ATLAS-CORVONERO-RELATIONSHIP-*` | Commercial relationship |
| Incorrect OWNS | No | **Deprecated** | `CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md` | Variant B — not recreated |

Last relevant ATLAS commit context: recovery reconstruction @ `eb2ca922`.

---

## 5. Business Authority

Source: `projects/orca/projects/corvonero-direct-v2-clean-room/intake/corvonero-direct-v2-business-intake-v1.json`

| Field | Classification |
|-------|----------------|
| Service scope (34 CR2-SVC) | CONFIRMED |
| Geography (NSO primary; expansion noted in task) | OPERATOR_APPROVED |
| Customer type (ЮЛ, ИП) | CONFIRMED |
| Remote RF / on-site NSO | CONFIRMED |
| Contract + cashless | CONFIRMED |
| Conversion goals | SAFE_UNKNOWN |
| Exclusions / prohibited claims | CONFIRMED |
| NDS | SAFE_UNKNOWN |
| Operating hours | SAFE_UNKNOWN |
| Budget 100k RUB/mo | CONFIRMED |
| Acceptable lead cost / CPL | SAFE_UNKNOWN |
| Landing pages (Tilda) | CONFIRMED |
| Measurement (Metrika) | CONFIRMED |
| Service priority | DECISION_REQUIRED — «Без приоритета» |

**No new Business Intake** warranted for semantic admission.

---

## 6. Raw Wordstat Verification

**`RAW_WORDSTAT_AUTHORITY = VERIFIED`**

| Check | Result |
|-------|--------|
| Directory exists | ✓ `C:\MARS Phenix\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\` |
| XLSX count | **18** |
| Manifest cross-check | SHA-256 prefixes match `keyword_registry.json` per-file `source_hash` |
| Missing/duplicate files | **None** |
| No-result seeds | ws-p2-003, ws-p2-006 documented |

Sample verified hash: `ws-p1-001-programmist-1c.xlsx` → `84464761e9b8d591...`

---

## 7. Dataset Authority

| Dataset | Path | Format | Count | SHA-256 prefix | Mutability |
|---------|------|--------|------:|----------------|------------|
| Normalized corpus | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/wordstat/wordstat-pass-a-normalized.json` | JSON | 2399 | `fbeb1b65d4a90cb0` | READ_ONLY |
| Normalized mirror | `projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-normalized-corpus-v1.json` | JSON | 2399 | `998422df6892d4cd` | READ_ONLY |
| Canonical semantic input | `projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json` | JSON | 2368 | `eaa09b8450f82738` | READ_ONLY |

Consumer: new controlled semantic run (2368 canonical registry).

---

## 8. 2399→2368 Lineage

**Lineage PROVEN** — not a silent rebuild gap.

| Stage | Count | Authority |
|-------|------:|-----------|
| Raw XLSX rows ingested | 2399 | MIG Pass A ingestion report |
| Duplicate clusters | 31 | Clean-room report §10 |
| Unique normalized phrases | 2368 | `CORVONERO-CANONICAL-PHRASE-REGISTRY-v1.md` |
| Dedup rule | Deterministic key (trim, lowercase, ё→е, punctuation, tokens) | `normalize-mig-corpus.mjs` |
| Stable IDs | CR2-PHR / CR2-LED | ✓ proven in registry |

Note: manifest uses 2370 unique raw phrases in one metric — canonical semantic input for new run is **2368** per registry stats (authoritative for ORCA admission).

---

## 9. MIG Session and Handoff

Session: **`session-mig-20260622-corv01`** — **COMPLETE**  
Handoff: **READY FOR ORCA REVIEW**

| Artefact | Path | Present | Ready |
|----------|------|--------:|------:|
| Session manifest | `session_manifest.json` | ✓ | ✓ |
| Normalized corpus | `evidence/wordstat/wordstat-pass-a-normalized.json` | ✓ 2399 | ✓ |
| Canonical registry | clean-room `corvonero-canonical-phrase-registry-v1.json` | ✓ 2368 | ✓ |
| Demand surface | `demand_surface.json` | ✓ | ✓ |
| Keyword registry | `keyword_registry.json` | ✓ | ✓ |
| Research Pack | `research_pack.approved.md` | ✓ | ✓ |
| Wordstat manifests | keyword_registry + source-registry | ✓ | ✓ |
| SERP indexes | `serp_r1_index.json` + stage indexes | ✓ | ✓ |
| ORCA handoff | `handoff/orca-evidence-handoff-v1.json` | ✓ | ✓ |

---

## 10. SERP Authority

**Classification: `SERP_PARTIAL_BUT_NON_BLOCKING`**

Latest canonical index: `serp_r1_index.json` (zpm-workflow-corv01, updated 2026-06-22)

| Query ID | Query | Latest grade | Evidence | Needed for new run |
|----------|-------|--------------|----------|-------------------:|
| r1q01 | программист 1С Новосибирск | B | zpm capture | Supporting |
| r1q02 | сопровождение 1С Новосибирск | B | zpm capture | Supporting |
| r1q03 | доработка 1С Новосибирск | B | zpm capture | Supporting |
| r1q04 | интеграция 1С с сайтом Новосибирск | B | zpm capture | Supporting |
| r1q05 | интеграция 1С Битрикс | B | zpm capture | Supporting |
| r1q06 | маркировка 1С | C (CAPTCHA) | zpm blocked | Non-blocking |
| r1q07 | маркировка в 1С Новосибирск | C (CAPTCHA) | zpm blocked | Non-blocking |
| r1q08 | Честный знак 1С Новосибирск | **B** | throttled resume | Supporting |
| r1q09 | настройка ТС ПИОТ | C / not captured | — | Non-blocking |
| r1q10 | программа 1С не работает Новосибирск | **B** | throttled resume | Supporting |

**7 Grade B** supersedes older 5-item summary. q08/q10 completed; q09 not completed — operator-accepted limitation per final evidence audit.

---

## 11. ORCA Wave 3.1F Authority

**`ORCA_WAVE_3_1F_AUTHORITY_VERIFIED`**

| File | Path | SHA-256 prefix | Wave |
|------|------|----------------|------|
| semantic-adjudicator.mjs | `live-model/adjudication/` | `4e197d816cfd1389` | 3.1F |
| prompt-contract.mjs | `live-model/contracts/` | `0fbe20bfef33d2e6` | v1.3 |
| hard-rules.mjs | `production/assessors/` | `aed6d1078aa87833` | 3.1F |
| run-problem-query-policy-regression.mjs | `live-model/tests/` | `7d84258a23c1a405` | — |
| run-under-admission-regression.mjs | `live-model/tests/` | `c7c0e805a78d5ee8` | 3.1F |
| run-wave31e-bypass-audit.mjs | `live-model/tests/` | `244da6802bf746e5` | 3.1E audit |
| run-wave31f-bypass-audit.mjs | `live-model/tests/` | `2c8da2b6cf103b5f` | 3.1F |
| run-confirmation-validation.mjs | `live-model/tests/` | `1a9664baf25a0f0b` | — |

Wave 3.1F > 3.1E confirmed. No regression tests executed in this preflight (documentation-only task).

---

## 12. Deep Research Authority

**`DEEP_RESEARCH_AUTHORITY_VERIFIED`**

| Check | Result |
|-------|--------|
| Path | `projects/orca/research/ppc-semantic-intelligence/world-practice-2026-06/ORCA-PPC-SEMANTIC-CORE-WORLD-PRACTICE-RESEARCH-v1.md` |
| SHA-256 prefix | `984192DA` ✓ |
| Status | PRESERVED — CANONICAL — READY |
| Superseding version | **None found** |

---

## 13. Old Run Forensic Boundary

**`OLD_CORVONERO_RUN_NON_RESUMABLE`**

| Field | Value |
|-------|-------|
| Run | clean-room v1 diagnostic |
| Failed stage | SPPC-05 |
| False accepts | ~1892 |
| Freeze | 2026-06-22 |
| Authority | `project-ppc-state-manifest-v1.json`, `PROJECT.md` |

Declaration: `pilots/corvonero/CORVONERO-OLD-RUN-NON-RESUMABLE-v1.md` + `.json`

---

## 14. Project Lifecycle State

| Dimension | State |
|-----------|-------|
| Corvonero project | **FROZEN** |
| Resume readiness | **READY_AFTER_OPERATOR_CHARTER** |
| MIG | COMPLETE |
| ORCA brain | Wave 3.1F READY |
| Search PPC | Corvonero FROZEN; Wave 5 BLOCKED |
| Next permitted phase | Operator charter approval → Phase 0/1 execution |

---

## 15. Proposed New Run Identity

Format: **`corv-semantic-v2-<YYYYMMDD>-<sequence>`**  
Example: `corv-semantic-v2-20260626-001`

| Binding | Value |
|---------|-------|
| Project | PRJ-0013 |
| MIG session | session-mig-20260622-corv01 |
| Corpus | corvonero-canonical-phrase-registry-v1 (2368) |
| Corpus checksum prefix | eaa09b8450f82738 |
| ORCA wave | 3.1F |
| Prompt contract | orca-semantic-assessment-prompt-v1.3 |

**Not instantiated** in preflight.

---

## 16. Model and Runtime Policy

| Parameter | Value | Notes |
|-----------|-------|-------|
| Provider | OPERATOR_DECISION_REQUIRED | Validation used openrouter |
| Model | OPERATOR_DECISION_REQUIRED | Validation: openai/gpt-5-mini; default: gpt-4o-mini |
| Temperature | 0.1 | From adapter |
| Structured output | JSON required | response_format json_object |
| Retry | 3 | cost-rate-controls.mjs |
| Timeout | 30000 ms | env override |
| Batch size | 25 default | confirmation used 10 |
| Cost cap | $50 default | OPERATOR_DECISION_REQUIRED for 2368 run |
| Secrets | Environment | Never Git |
| Fallback | MODEL-FALLBACK-POLICY-v1 | Fail-closed |

---

## 17. SPPC-05 Charter

New run SPPC-05 must use **closed datasets** before canary:

- Adversarial false-accept rate **≤ 0.01** (canonical: `run-confirmation-validation.mjs`)
- Commercial false-reject threshold: **OPERATOR_APPROVAL_REQUIRED**
- High-risk classes: product/service, problem queries, career, info, geo-commercial, marking, TS PIOT
- Fail-closed — stop before full corpus on failure

---

## 18. Canary Design

- Size: **120** phrases
- Seed: deterministic from phrase_id + class
- Balanced strata (commercial, problem, ambiguity, license, career, info, integration, marking, TS PIOT, geo, 1C terms)
- Review sample: 30
- **Not started**

---

## 19. Batch and Checkpoint Design

- STORAGE root (proposed): `C:\MARS Phenix\AI MARS STORAGE\orca\corvonero\semantic-runs\<run_id>\`
- Batch size: 25 (bounded)
- Lock: atomic, owner, heartbeat, corpus checksum
- Processed-ID registry, duplicate prevention, orphan detection
- **Not created** in preflight

---

## 20. Human Review Gates

Gates A–F documented in `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-GATE-MATRIX-v1.md`

---

## 21. Output Schemas

Future run outputs: input manifest, run manifest, lock, checkpoints, batch receipts, assessments, adjudication, ACCEPT/REJECT/ABSTAIN registries, SPPC-05/canary/cost reports, reconciliation receipt, semantic registry, operator review package, handoff manifest. Raw provider content → STORAGE only.

---

## 22. Git and STORAGE Boundaries

**Git:** manifests, schemas, sanitized registries, reports, decisions  
**STORAGE:** raw Wordstat, raw model responses, cache, checkpoints, locks, batch working data  
**Separate** new-run STORAGE root from old forensic runtime.

---

## 23. Stop Conditions

Fail-closed on: hash/count/ID mismatch, ORCA authority mismatch, SPPC-05 failure, canary failure, excessive false accepts/rejects, ABSTAIN spike, model drift, structured-output failure, retry storm, cost-cap risk, stale heartbeat, lock conflict, checkpoint corruption, orphan records, operator rejection, privacy violation.

---

## 24. Test Plan

Future execution must validate: input hashes, row counts, ID uniqueness, 2399→2368 lineage, old-run isolation, lock atomicity, checkpoint integrity, SPPC-05 closed dataset, Wave 3.1F regressions, cost cap, final receipt, no Wave 5 uplift. Safe commands listed in `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-NEXT-TASK-v1.md`.

---

## 25. Documents Created

All under `projects/mars-search-ppc-production/pilots/corvonero/`:

1. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PREFLIGHT-v1.md`
2. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PREFLIGHT-v1.json`
3. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-OPERATOR-CHARTER-v1.md`
4. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-OPERATOR-CHARTER-v1.json`
5. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-INPUT-MANIFEST-v1.json`
6. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-GATE-MATRIX-v1.md`
7. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-GATE-MATRIX-v1.json`
8. `CORVONERO-OLD-RUN-NON-RESUMABLE-v1.md`
9. `CORVONERO-OLD-RUN-NON-RESUMABLE-v1.json`
10. `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-NEXT-TASK-v1.md`

Plus this report at `projects/mars-search-ppc-production/reports/REPORT-corvonero-new-controlled-semantic-run-preflight-v1.md`

---

## 26. Files Changed

**Created (11 files)** — see §25. **No modifications** to canonical data, ORCA/MIG code, or runtime artefacts.

---

## 27. Git Status

Branch: `mars/canonical-post-recovery`  
New pilot/charter files: **untracked** (intentionally uncommitted for operator review)  
No staging performed.

---

## 28. SAFE UNKNOWN

| Item | Status |
|------|--------|
| WEB-CORV-01 ownership | SAFE UNKNOWN (by design) |
| NDS | SAFE UNKNOWN |
| Target CPL / acceptable lead cost | SAFE UNKNOWN |
| Production model/provider for new run | OPERATOR_DECISION_REQUIRED |
| Full-run cost cap authorization | OPERATOR_DECISION_REQUIRED |
| Immutable backup SHA manifest file on STORAGE | Not located as standalone file — hashes verified via keyword_registry cross-check |

---

## 29. Operator Decisions Required

1. **Approve operator charter v1** (Gate A)
2. **Confirm production model/provider** (openrouter + gpt-5-mini vs alternative)
3. **Confirm cost cap** for 2368-phrase run
4. **Authorize Phase 0/1 execution task** after charter approval
5. **Service priority** remains unset («Без приоритета») — acceptable unless strategy phase starts later

---

## 30. Preliminary Readiness Verdict

# **`READY_FOR_OPERATOR_CHARTER_APPROVAL`**

Not authorized: SEMANTIC RUN STARTED · SEMANTIC RUN AUTHORIZED · PROJECT ACTIVE · WAVE 5 READY

---

## 31. Exact Next Execution Task

See: `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-NEXT-TASK-v1.md`

**CORVONERO NEW CONTROLLED SEMANTIC RUN — PHASE 0/1 EXECUTION**  
After Gate A: authority re-check, immutable input registration, run manifest, STORAGE root, run ID, lock init, optional closed-dataset SPPC-05 only.

---

## 32. Stop Condition

**Task complete.** Preflight and charter draft delivered.  
**Next gate:** `OPERATOR REVIEW AND APPROVAL OF CORVONERO NEW CONTROLLED SEMANTIC RUN CHARTER`

No semantic execution. No runtime artefacts. No commit/push.
