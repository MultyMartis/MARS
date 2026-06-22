# Корво Неро — Direct V2 Clean Room

**Project ID:** `corvonero-direct-v2-clean-room`  
**Status:** `DIAGNOSTIC FAILED — COMMERCIAL ADMISSION LOGIC NOT APPROVED`  
**Active line:** **YES** — canonical semantic rebuild locus (source corpus preserved; semantic decisions frozen)  
**Date established:** 2026-06-22  
**Diagnostic freeze recorded:** 2026-06-22 (operator decisions D2, D7; research intake v1)

---

## Diagnostic freeze declaration

Clean-room semantic pipeline v1 completed and exposed a **confirmed failure mode**: topical/service-scope relevance was treated as sufficient for commercial admission (~1892 accepts from ~2370 unique phrases). Per operator decision **D2**, this run is **frozen as diagnostic evidence**.

| Rule | Status |
|------|--------|
| Manual cleanup of 1892 accepted phrases | **PROHIBITED** |
| Reuse of v1 intent / eligibility / mapping / cluster / negative decisions | **FORBIDDEN** |
| Campaign production | **NOT STARTED — BLOCKED (D7)** |
| Advertising groups | **NOT STARTED — BLOCKED** |
| Ads / bids / URLs / UTM | **NOT STARTED — BLOCKED** |
| Final negatives | **NOT STARTED — BLOCKED** |
| Commander XLSX export | **NOT CREATED — BLOCKED** |
| Import / launch | **NOT AUTHORIZED** |

**Next gate:** ORCA Semantic Intelligence Architecture Decision Record → guideline + benchmark + pilot thresholds (promotion backlog P0-A through P0-G) → operator sign-off on approved Semantic Core (P0-H) → **then** new semantic admission rerun from preserved corpus only.

**Research reference:** `projects/orca/research/ppc-semantic-intelligence/world-practice-2026-06/`

---

## Reusable source layers (PRESERVED)

These layers remain valid inputs for a **future** semantic rerun with upgraded ORCA Semantic Intelligence. Do **not** delete.

| Layer | Locus |
|-------|-------|
| Operator business intake | `intake/CORVONERO-DIRECT-V2-BUSINESS-INTAKE-v1.md` |
| Service scope registry | `intake/CORVONERO-DIRECT-V2-SERVICE-SCOPE-v1.md` |
| Original MIG source ledger | `mig-source/MIG-WORDSTAT-SOURCE-LEDGER-v1.md` |
| Raw MIG corpus binding | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` |
| Normalized corpus | `semantic-core/CORVONERO-NORMALIZED-CORPUS-v1.md` |
| Deduplicated canonical phrases | `semantic-core/CORVONERO-CANONICAL-PHRASE-REGISTRY-v1.md` |
| Source authority manifest | `authority/CORVONERO-DIRECT-V2-SOURCE-AUTHORITY-MANIFEST-v1.md` |
| Provenance / pipeline summary | `artifacts/pipeline-run-summary-v1.json` |

---

## Invalid for semantic reuse — DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE

The following v1 outputs document **what went wrong**. They must **not** contaminate a new semantic run.

| Artifact | Marker |
|----------|--------|
| Intent screening decisions | `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE` |
| Commercial eligibility decisions | `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE` |
| Phrase-to-service mappings | `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE` |
| Cluster candidates | `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE` |
| Negative candidates | `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE` |
| Semantic Core Candidate v1 | `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE` |
| Operator review workbook decisions | `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE` |

Paths: `semantic-core/CORVONERO-INTENT-SCREENING-v1.md`, `CORVONERO-COMMERCIAL-ELIGIBILITY-v1.md`, `CORVONERO-PHRASE-TO-SERVICE-MAP-v1.md`, `CORVONERO-COMMERCIAL-CLUSTER-CANDIDATES-v1.md`, `CORVONERO-NEGATIVE-CANDIDATE-REGISTRY-v1.md`, `CORVONERO-DIRECT-SEMANTIC-CORE-CANDIDATE-v1.md`, review workbook under `artifacts/`.

**Next semantic run:** starts from preserved source/canonical corpus only; requires upgraded ORCA Semantic Intelligence (guideline, benchmark, pilot thresholds per D2/D5/D7).

---

## Clean-room declaration (historical)

This project is an **independent clean-room rebuild** of Corvonero Yandex Direct semantics.

| Rule | Status |
|------|--------|
| Old Corvonero v1–v7.1 production artefacts | **HISTORICAL ONLY** — not semantic authority |
| Semantic decision inheritance from old pipeline | **FORBIDDEN** |

---

## Allowed sources

| Class | Locus |
|-------|-------|
| Operator business inputs | `intake/`; `workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md` |
| Original MIG session | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` |
| Universal ORCA contract | `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` |
| Triumph-derived methodology | `projects/orca/knowledge/triumph-derived-orca-laws-v1.md` |
| PPC Semantic Intelligence research | `projects/orca/research/ppc-semantic-intelligence/world-practice-2026-06/` |

## Forbidden semantic sources

See `authority/CORVONERO-DIRECT-V2-SOURCE-AUTHORITY-MANIFEST-v1.md`

Historical branch: `projects/orca/projects/corvonero-yandex-direct/` — audit and anti-pattern reference only.

---

## Structure

```text
corvonero-direct-v2-clean-room/
├── PROJECT.md
├── authority/
├── intake/
├── mig-source/
├── semantic-core/
├── validation/
├── artifacts/
├── tools/
└── reports/
```

---

## MIG binding

| Artifact | Path |
|----------|------|
| MIG session | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` |
| Wordstat Pass A corpus | `evidence/wordstat/wordstat-pass-a-normalized.json` |
| Pass B | **NOT USED** (operator: not required) |

---

## Phase status

| Phase | Status |
|-------|--------|
| Source authority manifest | **COMPLETE** |
| Business intake | **COMPLETE** |
| Service scope registry | **COMPLETE** |
| MIG corpus ingest | **COMPLETE** |
| Normalization | **COMPLETE** |
| Deduplication | **COMPLETE** |
| Intent screening | **DIAGNOSTIC FAILED — DO NOT PROMOTE** |
| Commercial eligibility | **DIAGNOSTIC FAILED — DO NOT PROMOTE** |
| Service mapping | **DIAGNOSTIC FAILED — DO NOT PROMOTE** |
| Cluster discovery | **DIAGNOSTIC FAILED — DO NOT PROMOTE** |
| Negative candidate research | **DIAGNOSTIC FAILED — DO NOT PROMOTE** |
| Service demand coverage | **DIAGNOSTIC EVIDENCE ONLY** |
| Semantic core candidate v1 | **DIAGNOSTIC FAILED — NOT APPROVED** |
| Operator review workbook | **DIAGNOSTIC EVIDENCE ONLY** |
| Semantic core gate | **FAILED** — see `validation/direct-semantic-core-gate-v1.md` |
| Campaign production | **BLOCKED (D7)** |

---

*Corvonero Direct V2 Clean Room · documentation only · no runtime*
