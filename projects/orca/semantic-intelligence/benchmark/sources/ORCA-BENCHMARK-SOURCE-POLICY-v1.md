# ORCA Benchmark Source Policy v1

**Policy ID:** `orca-benchmark-source-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-source-policy-v1.json`](orca-benchmark-source-policy-v1.json)

---

## Purpose

Define **permitted phrase sources** and **forbidden ground-truth** for benchmark construction.

---

## Forbidden as ground truth

| Source | Rule |
|--------|------|
| Corvonero v1 admission labels | **FORBIDDEN** — D2 freeze; diagnostic failed |
| P0-C training illustrations | Design only — not gold |
| Classifier or LLM outputs | Never gold without full human adjudication |
| Campaign export phrases | Contamination risk — D7 |

---

## Permitted source classes

| class_id | Description | Requirements |
|----------|-------------|--------------|
| `SRC_HISTORICAL_SEARCH_TERMS` | Historical PPC/search extracts | Full provenance |
| `SRC_OPERATOR_SEED` | Operator seed list | Operator approval per insert |
| `SRC_SYNTHETIC_DESIGN` | Adversarial/minimal-pair design | Marked synthetic; design illustrations only |
| `SRC_PUBLIC_CORPUS` | Licensed public corpora | License audit |
| `SRC_DOMAIN_EXPERT_CURATED` | Expert-curated candidates | Expert attestation |

---

## Corvonero preserved corpus

- **Status:** FROZEN
- **Permitted use:** Candidate phrase **text** extraction for sampling frame
- **Forbidden:** Treating v1 ACCEPT/REJECT decisions as labels

---

## Provenance requirements

Every benchmark record must populate `source_type`, `source_ids`, and `benchmark.provenance` per record schema. `provenance_status` must not be `UNKNOWN` at gold freeze.
