# ORCA Semantic Admission Integration Charter v1

**Charter ID:** `orca-semantic-admission-integration-charter`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `APPROVED — IMPLEMENTATION AUTHORIZED`  
**Gate:** P0-I

---

## Purpose

Define the **executable admission integration boundary** for ORCA Semantic Intelligence v1: how approved contracts become pipeline consumers, how decisions are enforced, and how integration is proven before benchmark construction (P0-D) or Corvonero rerun.

This charter is **approved for bounded integration core implementation** (I-01–I-07). It is **not** production runtime or semantic accuracy proof.

---

## Core principle

> Semantic contracts, taxonomy, annotation rules and invariants must have explicit consumers, blocking validators and auditable outputs. Merely registering documents in a manifest is insufficient.

A document listed in an authority manifest without a consumer is classified: **`REGISTERED — NOT INTEGRATED`**.

---

## Executable flow (P0-I scope)

```text
Source Corpus
  → Normalization (SI-04 technical only)
  → Query Understanding (literal interpretation, signals — no final authority)
  → Semantic Contract Consumer (load + version check — BLOCKING)
  → Intent Assessment (taxonomy-backed primary intent)
  → Commercial Eligibility (ACCEPT / REJECT / ABSTAIN only)
  → Invariant Validator (BLOCKING)
  → Human Review Router
  → Integration QA (contract-consumption report)
```

### Hard stop boundary

P0-I flow **must stop before**:

| Stage | Reason |
|-------|--------|
| Final service ownership (SI-10) | Ownership requires validated ACCEPT admission |
| Clustering (SI-11) | Clusters derived from broken admission caused Corvonero failure |
| Negative keyword discovery (SI-12) | Negatives after bad accepts cannot repair admission |
| Campaign production | D7 / contract gate |
| Export / Commander import | Downstream only after semantic core approval |

---

## Permitted automated admission values

Only three terminal automated values are permitted as **semantic authority**:

| Value | Meaning |
|-------|---------|
| `ACCEPT` | Positive commercial evidence; invariants pass |
| `REJECT` | Clear non-commercial or prohibited intent; reason code required |
| `ABSTAIN` | Unresolved ambiguity, conflict, or insufficient evidence |

### Forbidden as semantic authority

Legacy Corvonero pipeline values must **not** appear as final admission authority:

- `ELIGIBLE COMMERCIAL`
- `NOT ELIGIBLE — *`
- `HOLD — AMBIGUOUS`
- `NEEDS OPERATOR REVIEW` (as substitute for ABSTAIN authority)
- Provisional intent classes (`COMMERCIAL SERVICE`, `CAREER/EMPLOYMENT`, etc.) as final eligibility

These may exist only in `diagnostic_comparison.legacy_*` fields.

---

## Integration vs registration

| State | Definition |
|-------|------------|
| **REGISTERED** | Path listed in manifest or README |
| **LOADED** | Consumer read file; checksum/version verified |
| **CONSUMED** | Consumer applied rules to produce output field |
| **INTEGRATED** | Loaded + consumed + blocking on failure + audit trace |
| **REGISTERED — NOT INTEGRATED** | Manifest reference only — **BLOCKING DEFECT** for required contracts |

---

## Dependencies

| Upstream | Role |
|----------|------|
| P0-A ADR (`f17c270`) | Stage architecture SI-01–SI-17 |
| P0-B Taxonomy & Schema (`3151953`) | Record shape and controlled vocabularies |
| P0-C Annotation Guideline (`78b0557`) | ACCEPT/REJECT/ABSTAIN semantics |
| Capability recovery audit (`a09380d`) | Failure modes and enforcement gaps |

---

## Deliverables (this charter)

| Artifact | Path |
|----------|------|
| Consumer architecture | `../architecture/` |
| Seven consumer specs | `../consumers/` |
| Contract loading manifest | `../contracts/` |
| Invariant validator | `../validators/` |
| Human review router | `../enforcement/ORCA-SEMANTIC-HUMAN-REVIEW-ROUTER-v1.md` |
| Legacy migration | `../migration/` |
| Pilot slice design | `../pilot-slice/` |
| Integration pass criteria | `../quality/` |
| Implementation backlog | `../reports/ORCA-P0-I-IMPLEMENTATION-BACKLOG-v1.md` |

---

## P0-I PASS (summary)

P0-I proves **integration and enforcement**, not production classifier accuracy. See [`../quality/ORCA-P0-I-INTEGRATION-PASS-CRITERIA-v1.md`](../quality/ORCA-P0-I-INTEGRATION-PASS-CRITERIA-v1.md).

---

## Non-goals

- B0 benchmark construction
- Gold label adjudication
- Corvonero corpus rerun
- Campaign production authorization
- LLM classifier training

---

## Operator approval required

Approval of this charter authorizes **bounded implementation backlog I-01–I-09** and **integration pilot execution** — not P0-D, not Corvonero rerun, not production semantic core.
