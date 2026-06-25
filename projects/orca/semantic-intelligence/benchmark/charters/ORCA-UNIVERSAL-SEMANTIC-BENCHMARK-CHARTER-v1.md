# ORCA Universal Semantic Benchmark Charter v1

**Charter ID:** `orca-universal-semantic-benchmark-charter`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Gate:** P0-D

---

## Purpose

Define the **universal ORCA semantic benchmark program**: stratified gold-reference construction, governance, splits, leakage control, adjudication authority, and quality gates for evaluating semantic admission (ACCEPT / REJECT / ABSTAIN) per P0-B schema and P0-C annotation guideline.

This charter is **documentation only**. It authorizes **how** benchmark rows will be created after operator approval — it does **not** contain benchmark rows or gold labels.

---

## Non-goals

| Non-goal | Rationale |
|----------|-----------|
| Runtime or classifier implementation | P0-F/G scope |
| Campaign production authorization | D7 blocks until gates pass |
| Phrase registry or production core | Benchmark is evaluation reference only |
| Automatic promotion of research examples | Research is input, not gold |
| Relabelling Corvonero v1 accepted corpus | D2 freeze; old labels forbidden as ground truth |
| Weak-supervision label generation as gold | Human adjudicated gold only for benchmark splits marked frozen |

---

## Two-product model (D5)

### Universal ORCA benchmark

| Attribute | Value |
|-----------|-------|
| Target size (B2) | **1,200–2,000** phrases |
| Scope | Platform-wide B2B service PPC semantic admission |
| Stratification | Intent strata + domain coverage + difficulty strata |
| Blind test | ≥ 300–400 phrases (separate frozen pack) |
| Hard negatives | Separate fixed pack — not mixed into random sample |

### Corvonero pilot (bounded)

| Attribute | Value |
|-----------|-------|
| Target size | **300–500** phrases |
| Role | Go/no-go pilot within universal program before full corpus rerun |
| Relationship | Subset drawn from universal sampling frame where possible |
| Blind subset | ≥ 100 unseen phrases within pilot |
| Double annotation | **100%** on pilot set |
| Status | **FROZEN** — annotation blocked until P0-D approval and B0 pass |

> **Boundary:** Corvonero pilot metrics inform rerun permission; they do **not** supersede universal benchmark authority. See [`ORCA-CORVONERO-PILOT-BOUNDARY-v1.md`](ORCA-CORVONERO-PILOT-BOUNDARY-v1.md).

---

## Size phases

| Phase | ID | Size | Objective | Exit criteria |
|-------|-----|------|-----------|---------------|
| Qualification | **B0** | 60–100 | Validate annotation protocol, tooling, adjudication loop | B0 quality gates pass — see [`ORCA-BENCHMARK-B0-QUALIFICATION-CHARTER-v1.md`](ORCA-BENCHMARK-B0-QUALIFICATION-CHARTER-v1.md) |
| Expansion | **B1** | 300–500 | Corvonero pilot + partial universal strata fill | Pilot strata targets met; agreement metrics validated |
| Universal target | **B2** | 1,200–2,000 | Full D5 universal benchmark | Gold freeze; blind pack sealed |

Phases are **sequential**. B1 annotation scale-up requires B0 pass. B2 requires B1 pass and operator checkpoint.

---

## Release states

Controlled lifecycle for benchmark packages and split packs:

| State | Meaning |
|-------|---------|
| `DRAFT` | Charter or split design; no authoritative labels |
| `ANNOTATION IN PROGRESS` | Active human annotation under double-annotation policy |
| `ADJUDICATION IN PROGRESS` | Disagreements under adjudication |
| `FROZEN INTERNAL` | Gold labels frozen for internal dev/calibration only |
| `BLIND EVALUATION` | Blind pack sealed; no training or prompt tuning on blind |
| `RELEASED FOR DEVELOPMENT` | Dev/calibration splits released for P0-F baselines |
| `SUPERSEDED` | Replaced by newer versioned package |
| `CONTAMINATED` | Leakage or protocol breach — must not be used for evaluation |
| `WITHDRAWN` | Operator withdrawal — archived only |

Illegal transitions (e.g. `BLIND EVALUATION` → `ANNOTATION IN PROGRESS` without new version) require operator exception with audit trail.

---

## Operator-approved thresholds (D3)

| Metric | Threshold | Status |
|--------|-----------|--------|
| Commercial precision on auto-accept | **≥ 0.95** | **OPERATOR-APPROVED** (D3) |
| Protected-strata FPR per class | **≤ 0.01** | **OPERATOR-APPROVED** (D3) |

Protected classes: `career`, `educational`, `diy_how_to`, `regulatory`, `navigational`.

---

## Proposed thresholds (validate during B0/B1)

| Metric | Proposed direction | Status |
|--------|-------------------|--------|
| Overall auto-accept FPR | ≤ 0.03 | PROPOSED — VALIDATE DURING B0/B1 |
| Service mapping precision (accepted commercial) | ≥ 0.97 | PROPOSED — VALIDATE DURING B0/B1 |
| Ambiguity recall on blind hard set | ≥ 0.90 | PROPOSED — VALIDATE DURING B0/B1 |
| Abstention rate (initial releases) | ≥ 0.15 | PROPOSED — VALIDATE DURING B0/B1 |
| Annotator agreement κ (eligibility) | ≥ 0.75 target | PROPOSED — VALIDATE DURING B0/B1 |
| Long-term double-annotation sample rate (post-B0) | TBD | **OPERATOR DECISION REQUIRED AFTER B0** |

---

## Mandatory double annotation

**100% double annotation** required for:

- Entire **B0** qualification set
- Entire **Corvonero pilot** set
- Entire **blind test** pack (independent second pass before freeze)
- All **protected strata** records
- All **hard-negative** and **adversarial** packs
- All records flagged `DIFF_ADVERSARIAL`

Long-term universal benchmark double-annotation percentage beyond mandatory strata: **OPERATOR DECISION REQUIRED AFTER B0** (deferred from P0-C U-C02).

---

## Artifact map

| Topic | Document |
|-------|----------|
| B0 qualification | [`ORCA-BENCHMARK-B0-QUALIFICATION-CHARTER-v1.md`](ORCA-BENCHMARK-B0-QUALIFICATION-CHARTER-v1.md) |
| Corvonero boundary | [`ORCA-CORVONERO-PILOT-BOUNDARY-v1.md`](ORCA-CORVONERO-PILOT-BOUNDARY-v1.md) |
| Intent strata | [`../strata/ORCA-BENCHMARK-INTENT-STRATA-v1.md`](../strata/ORCA-BENCHMARK-INTENT-STRATA-v1.md) |
| Domain coverage | [`../strata/ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md`](../strata/ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md) |
| Sampling | [`../sampling/ORCA-UNIVERSAL-BENCHMARK-SAMPLING-PLAN-v1.md`](../sampling/ORCA-UNIVERSAL-BENCHMARK-SAMPLING-PLAN-v1.md) |
| Splits | [`../splits/ORCA-BENCHMARK-SPLIT-POLICY-v1.md`](../splits/ORCA-BENCHMARK-SPLIT-POLICY-v1.md) |
| Leakage | [`../leakage-control/`](../leakage-control/) |
| Annotation | [`../annotation/`](../annotation/) |
| Adjudication | [`../adjudication/ORCA-GOLD-LABEL-AUTHORITY-v1.md`](../adjudication/ORCA-GOLD-LABEL-AUTHORITY-v1.md) |
| Quality gates | [`../quality/ORCA-BENCHMARK-QUALITY-GATES-v1.md`](../quality/ORCA-BENCHMARK-QUALITY-GATES-v1.md) |

---

## Downstream consequences

| System | Status until charter approval + B0 |
|--------|-----------------------------------|
| Benchmark rows | NOT STARTED |
| Corvonero | FROZEN |
| Classifier | NOT STARTED |
| Campaign production | BLOCKED |
