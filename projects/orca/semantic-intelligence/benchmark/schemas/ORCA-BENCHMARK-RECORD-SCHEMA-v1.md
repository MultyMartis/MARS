# ORCA Benchmark Record Schema v1

**Schema ID:** `orca-benchmark-record-schema`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**JSON Schema:** [`orca-benchmark-record-schema-v1.schema.json`](orca-benchmark-record-schema-v1.schema.json)  
**Template:** [`orca-benchmark-record-template-v1.json`](orca-benchmark-record-template-v1.json)

---

## Purpose

Wrap the P0-B **semantic record** with benchmark-specific metadata for gold construction, splits, and governance.

---

## Structure

```text
BenchmarkRecord
├── semantic_record  → $ref ../../schemas/orca-semantic-record-schema-v1.schema.json
└── benchmark        → strata, split, gold status, double annotation, adjudication
```

---

## Benchmark block (required)

| Field | Description |
|-------|-------------|
| `benchmark_version` | Benchmark package semver |
| `phase` | B0 / B1 / B2 |
| `stratum_id` | Intent stratum ID |
| `domain_id` | Domain coverage ID |
| `difficulty_id` | Difficulty stratum ID |
| `split_id` | Dev / calibration / blind / anchor / hard-negative |
| `gold_status` | DRAFT → PROVISIONAL → AUTHORITATIVE |
| `release_state` | Package lifecycle state |
| `double_annotation` | Required flag, pass count, disagreement types |
| `adjudication` | Adjudicator metadata when resolved |
| `provenance` | Sampling frame and source class |
| `minimal_pair_id` | Optional pair linkage |
| `corvonero_pilot` | Pilot slice flag |

---

## Template

Empty template provided — **no real phrases**. Use only after charter approval for operational row creation.

---

## Invariants

1. `gold_status: AUTHORITATIVE` requires completed double annotation where mandatory
2. `split_id: SPLIT_BLIND` forbids export to dev tooling before seal
3. Old Corvonero labels must appear in `forbidden_source_flags` if phrase originated from frozen corpus — never as gold evidence
