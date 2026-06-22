# ORCA P0-I Implementation Backlog v1

**Backlog ID:** `orca-p0-i-implementation-backlog-v1`  
**Status:** `CORE IMPLEMENTATION APPROVED — I-08 PILOT AUTHORIZED`  
**Machine-readable:** [`orca-p0-i-implementation-backlog-v1.json`](orca-p0-i-implementation-backlog-v1.json)

---

## I-01 — Contract loader

| Attribute | Value |
|-----------|-------|
| **Purpose** | Load required contracts per manifest; verify version and checksum |
| **Inputs** | `orca-semantic-contract-loading-manifest-v1.json` |
| **Outputs** | In-memory contract bundle; load report |
| **Dependencies** | None |
| **Tests** | Missing file → FATAL; checksum fail → FATAL; load order respected |
| **Stop conditions** | All required contracts loaded or run halted |
| **Prohibited** | Partial silent load; skipping optional legacy regex |

---

## I-02 — Semantic record generator

| Attribute | Value |
|-----------|-------|
| **Purpose** | Build P0-B schema records from normalized phrases |
| **Inputs** | Normalized phrase, query understanding, consumer outputs |
| **Outputs** | Draft semantic record JSON |
| **Dependencies** | I-01, taxonomy consumer, schema consumer |
| **Tests** | Required fields populated; no forbidden downstream fields |
| **Stop conditions** | Record validates or returns structured errors |
| **Prohibited** | Legacy eligibility values; auto service ownership |

---

## I-03 — Admission orchestrator

| Attribute | Value |
|-----------|-------|
| **Purpose** | Execute SI-07/SI-08 flow; tri-state decision authority |
| **Inputs** | Record draft, annotation policy, risk mode, operator scope |
| **Outputs** | `commercial_eligibility.decision` ∈ {ACCEPT, REJECT, ABSTAIN} |
| **Dependencies** | I-01, I-02, all consumers |
| **Tests** | Three decisions reachable; legacy not authoritative |
| **Stop conditions** | Pre-ownership boundary enforced |
| **Prohibited** | Clustering, negatives, export, campaign fields |

---

## I-04 — Invariant validator

| Attribute | Value |
|-----------|-------|
| **Purpose** | Blocking enforcement of SI-INV-001–015 |
| **Inputs** | Complete semantic record, invariant registry |
| **Outputs** | Validation result per record |
| **Dependencies** | I-03 |
| **Tests** | Known Corvonero failure phrases blocked |
| **Stop conditions** | FATAL on contract version missing |
| **Prohibited** | Warning-only mode for BLOCKING rules |

---

## I-05 — Human review router

| Attribute | Value |
|-----------|-------|
| **Purpose** | Route ABSTAIN, high risk, conflicts to review queue |
| **Inputs** | Validated record, router rules |
| **Outputs** | `review.workflow_status`, queue entries |
| **Dependencies** | I-04 |
| **Tests** | ABSTAIN always routed; automated decision preserved |
| **Stop conditions** | Route record created or explicit no-route justification |
| **Prohibited** | Silent ACCEPT promotion |

---

## I-06 — Legacy comparison adapter

| Attribute | Value |
|-----------|-------|
| **Purpose** | Run regex baseline; emit diagnostic_comparison only |
| **Inputs** | Phrase, `run-clean-room-semantic-pipeline-v1.mjs` functions |
| **Outputs** | Legacy comparison fields; disagreement flags |
| **Dependencies** | I-03 (parallel) |
| **Tests** | Legacy never writes authority decision field |
| **Stop conditions** | Comparison report row per phrase |
| **Prohibited** | ELIGIBLE COMMERCIAL as final output |

---

## I-07 — Contract-consumption report

| Attribute | Value |
|-----------|-------|
| **Purpose** | Prove each required contract loaded and consumed |
| **Inputs** | Run audit traces, manifest |
| **Outputs** | `contract-consumption-report-v1.json` |
| **Dependencies** | I-01 through I-05 |
| **Tests** | REGISTERED — NOT INTEGRATED = FAIL for required |
| **Stop conditions** | 100% required INTEGRATED for PASS |
| **Prohibited** | Manual status without trace evidence |

---

## I-08 — Integration pilot runner

| Attribute | Value |
|-----------|-------|
| **Purpose** | Execute ~200 phrase pilot slice end-to-end |
| **Inputs** | Pilot phrase list (operator-approved), I-01–I-07 |
| **Outputs** | Pilot artifacts, pass/fail vs criteria |
| **Dependencies** | I-01–I-07 complete |
| **Tests** | P0-I pass criteria checklist |
| **Stop conditions** | No downstream clustering/export |
| **Prohibited** | B0 labels; Corvonero rerun; gold adjudication |

---

## I-09 — External artifact parity hook

| Attribute | Value |
|-----------|-------|
| **Purpose** | Optional Triumph export validator hook post-admission |
| **Inputs** | Admission-passed subset only |
| **Outputs** | Parity report (downstream) |
| **Dependencies** | I-03 PASS records |
| **Tests** | Does not run on blocked records |
| **Stop conditions** | Admission boundary respected |
| **Prohibited** | Using 345 rules as admission substitute |

---

## Implementation gate

Operator approved P0-I charter (`3a5ec5d`). Core I-01–I-07 implemented and fixture-validated — **uncommitted** pending operator review.

## Implementation status (2026-06-22)

| Item | Status |
|------|--------|
| I-01 – I-07 | IMPLEMENTED — FIXTURE VALIDATED |
| I-08 | READY FOR PHRASE-SELECTION GATE |
| I-09 | PLANNED — DEFERRED |
| P0-I overall | CORE INTEGRATION PASS — PILOT REQUIRED |
