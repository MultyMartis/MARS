# ORCA Semantic Intelligence — Quality Gates v1

**Gates ID:** `orca-semantic-intelligence-quality-gates`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Gate classes

| Class | Meaning |
|-------|---------|
| `OPERATOR-APPROVED` | Threshold fixed by operator decision — changes require new decision |
| `PROPOSED — BENCHMARK VALIDATION REQUIRED` | Metric defined; threshold not operator-approved |
| `ARCHITECTURE` | Structural gate — no metric |

---

## Operator-approved pilot thresholds (D3)

| Metric | Threshold | Class | Status |
|--------|-----------|-------|--------|
| Commercial Precision on auto-accept | **≥ 0.95** | OPERATOR-APPROVED | D3 |
| Protected-strata FPR (per class) | **≤ 0.01** | OPERATOR-APPROVED | D3 |
| Explicit ABSTAIN support | **Mandatory** | OPERATOR-APPROVED | D4 |
| Campaign production before approved Semantic Core | **Prohibited** | OPERATOR-APPROVED | D7 |

**Protected classes:** career; educational; DIY/how-to; regulatory; navigational.

---

## Proposed metrics — benchmark validation required

| Metric | Purpose | Proposed target | Status |
|--------|---------|-----------------|--------|
| Ambiguity recall | ABSTAIN captures true ambiguous cases | TBD on blind set | PROPOSED |
| Service-mapping precision | Correct primary ownership | ≥ 0.90 suggested | PROPOSED |
| Calibration error (ECE) | Model confidence reliability | ≤ 0.05 suggested | PROPOSED |
| Abstention rate | Queue sizing / operator load | Research suggests ≥ 0.15 early — **not operator-validated** | PROPOSED |
| Human disagreement rate | Annotation/adjudication quality | ≤ 0.10 suggested | PROPOSED |
| Per-intent precision/recall | Stratified performance | Per-intent TBD | PROPOSED |
| Cost-weighted error | Business impact weighting | Charter-defined | PROPOSED |

---

## Architecture gates (no metric)

| Gate | Requirement | Blocking |
|------|-------------|----------|
| G-ARCH-01 | ADR v1 operator approval | P0-B onward |
| G-ARCH-02 | Semantic taxonomy frozen (P0-B) | P0-C |
| G-ARCH-03 | Annotation guideline approved (P0-C) | P0-D annotation |
| G-ARCH-04 | Gold benchmark frozen (P0-D) | P0-F baselines |
| G-ARCH-05 | Baseline evaluation complete (P0-F) | P0-G |
| G-ARCH-06 | Threshold gate pass (P0-G) | Corvonero rerun |
| G-ARCH-07 | Semantic Core operator sign-off (P0-H) | Campaign production |
| G-ARCH-08 | Export parity pass (SI-16) | Commander handoff |

---

## Evaluation protocol (P0-G)

1. Measure on **blind test** split — never tune on blind.
2. Report commercial precision on **auto-accept path only** — human-resolved ACCEPT tracked separately.
3. Report protected-strata FPR **per class** — not aggregate only.
4. Report abstention rate and ambiguity recall jointly — detect metric gaming via excessive ABSTAIN.
5. Fail closed: any D3 threshold miss → no production authorization.

---

## Corvonero pilot gates

| Gate | Requirement |
|------|-------------|
| Pilot corpus | 300–500 phrases per D5 |
| Parent benchmark | Universal program 1200–2000 phrases |
| Initial risk mode | CONSERVATIVE |
| Diagnostic v1 reuse | **FORBIDDEN** for decisions |

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-quality-gates-v1.json` |
| Admission policy | `ORCA-SEMANTIC-ADMISSION-POLICY-v1.md` |
| Promotion backlog P0-G | `research/.../promotion/` |
