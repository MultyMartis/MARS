# ORCA Universal Benchmark — Charter Locus (P0-D)

**Locus:** `projects/orca/semantic-intelligence/benchmark/`  
**Status:** `P0-D — ON HOLD UNTIL P0-I PASS`  
**Date:** 2026-06-22  
**Package status:** `ON HOLD UNTIL P0-I PASS`. Hold record: [`../../audits/triumph-to-orca-capability-recovery-v1/decisions/ORCA-P0-D-BENCHMARK-CHARTER-HOLD-v1.md`](../../audits/triumph-to-orca-capability-recovery-v1/decisions/ORCA-P0-D-BENCHMARK-CHARTER-HOLD-v1.md). P0-I prerequisite: [`../integration/quality/P0-D-PREREQUISITE-AMENDMENT-v1.md`](../integration/quality/P0-D-PREREQUISITE-AMENDMENT-v1.md).

Implementation-neutral benchmark **program charter** for ORCA Semantic Intelligence v1. Not runtime. Not classifier. **No benchmark annotation rows** in this package.

## Authority

- P0-A ADR (`projects/orca/architecture/semantic-intelligence/`)
- P0-B taxonomy and semantic record schema (`../taxonomy/`, `../schemas/`)
- P0-C annotation guideline (`../annotation/`) — **APPROVED — IMPLEMENTATION NOT STARTED** (C1–C7)
- Operator decisions D1–D7 (D3 thresholds approved; D5 dual-scope sizing)
- Research strata table (`projects/orca/research/ppc-semantic-intelligence/world-practice-2026-06/`)

## Two-product model

| Product | Target size | Role |
|---------|-------------|------|
| **Universal ORCA benchmark** | 1,200–2,000 phrases (D5) | Platform-wide gold reference for semantic admission evaluation |
| **Corvonero pilot** | 300–500 phrases (D5) | Bounded pilot within universal program; go/no-go for v2 semantic rerun |

Corvonero pilot is **not** a separate truth source — it is a **bounded slice** with additional blind and hard-negative packs per [`charters/ORCA-CORVONERO-PILOT-BOUNDARY-v1.md`](charters/ORCA-CORVONERO-PILOT-BOUNDARY-v1.md).

## Size phases

| Phase | Purpose | Approximate size | Gate |
|-------|---------|------------------|------|
| **B0** | Qualification — protocol, annotator readiness, tooling | 60–100 phrases | Pass before B1 annotation scale-up |
| **B1** | Expansion — Corvonero pilot + partial universal strata | 300–500 phrases | Pass before B2 full universal target |
| **B2** | Universal target — full stratified benchmark per D5 | 1,200–2,000 phrases | Gold freeze before P0-F baselines |

## Structure

| Path | Role |
|------|------|
| `charters/` | Master charter, B0 qualification, Corvonero pilot boundary |
| `strata/` | Domain coverage, intent strata, difficulty strata |
| `sources/` | Source corpus policy and provenance classes |
| `sampling/` | Stratified sampling plan |
| `splits/` | Dev / calibration / blind split policy |
| `leakage-control/` | Blind test governance and leakage controls |
| `annotation/` | Double annotation policy and governance roles |
| `adjudication/` | Adjudication policy and gold label authority |
| `hard-negatives/` | Hard-negative and minimal-pair design |
| `regression/` | Regression anchor policy |
| `schemas/` | Benchmark record schema (wraps semantic record) |
| `quality/` | Metrics, agreement, versioning, quality gates |
| `validation/` | Charter validation checklist |
| `decisions/` | P0-D decision record — operator approval required |

## Release states

Controlled vocabulary for benchmark package lifecycle:

`DRAFT` → `ANNOTATION IN PROGRESS` → `ADJUDICATION IN PROGRESS` → `FROZEN INTERNAL` → `BLIND EVALUATION` → `RELEASED FOR DEVELOPMENT` → (`SUPERSEDED` | `CONTAMINATED` | `WITHDRAWN`)

## Hard prohibitions

- **No** real benchmark annotation rows in charter artifacts
- **No** gold labels derived from old Corvonero v1 admission decisions
- **No** classifier training or campaign production authorization from this package
- **No** use of P0-C training illustrations as benchmark ground truth

## Gates (downstream)

| Item | Status |
|------|--------|
| P0-D Charter | **PROPOSED — OPERATOR APPROVAL REQUIRED** |
| B0 qualification execution | BLOCKED until charter approval |
| Corvonero pilot annotation | BLOCKED — Corvonero **FROZEN** |
| Classifier | **NOT STARTED** |
| Campaign production | **BLOCKED** |

## Reading order

1. [`charters/ORCA-UNIVERSAL-SEMANTIC-BENCHMARK-CHARTER-v1.md`](charters/ORCA-UNIVERSAL-SEMANTIC-BENCHMARK-CHARTER-v1.md)
2. Strata (`strata/`)
3. Sources and sampling (`sources/`, `sampling/`)
4. Splits and leakage control (`splits/`, `leakage-control/`)
5. Annotation and adjudication (`annotation/`, `adjudication/`)
6. Hard negatives and regression (`hard-negatives/`, `regression/`)
7. Schemas and quality (`schemas/`, `quality/`)
8. Validation and decision (`validation/`, `decisions/`)
