# ORCA Semantic Duplication Reduction Plan v1

**Plan ID:** `orca-semantic-duplication-reduction-v1`  
**Date:** 2026-06-22

---

## Purpose

Reduce overlapping invariant/policy documents across P0-A–D without unsafe merges in this task.

---

## Overlap matrix

| Topic | Copies found | Canonical owner | Action |
|-------|--------------|-----------------|--------|
| ACCEPT requires commercial evidence | P0-C, invariants, ADR SI-07, Triumph SE | **P0-C COMMERCIAL-EVIDENCE** + **invariants #2** | Reference from ADR; do not restate in benchmark |
| ABSTAIN under ambiguity | P0-C, admission policy, invariants | **P0-C ABSTAIN standard** | Single consumer source |
| Career/edu/DIY blocklist | Triumph SE-03, P0-C protected intents, Corvonero regex | **P0-C PROTECTED-NONCOMMERCIAL** | Regex → signal only; merge Triumph lists into annotation consumer |
| Employment vs provider hire | P0-C, annotation examples, Triumph doctrine | **P0-C guideline** | Examples reference guideline IDs |
| Topic ≠ intent | Invariants #1, ADR, audit finding | **invariants #1** | ADR references invariant ID |
| Service ownership before negatives | ADR SI-10, Triumph workflow, contract INV | **ADR SI ordering** | Benchmark charter references — no third copy |
| Export validation rules | Triumph 345 rules, campaign contract | **Triumph export validators** | DOWNSTREAM — not admission |
| Benchmark quality gates (D3) | P0-D quality/, architecture quality gates | **architecture quality gates** for admission; **P0-D** for benchmark only | Keep distinct |
| Risk modes | ADR A4, admission policy, quality gates | **admission policy** | Risk consumer loads one JSON |
| Version authority | Schema versioning, ADR authority model, manifest | **loading manifest + authority model** | Version consumer owns |

---

## Recommend merge later (not this task)

| Documents | Merge target | Risk if merged now |
|-----------|--------------|-------------------|
| Triumph SE blocklists + P0-C protected intents | Annotation guideline JSON | Needs operator review |
| Enforcement gap matrix + invariant validator | Single machine registry | P0-I validator just defined |
| Benchmark admission strata + P0-C intent taxonomy | Reference links only | Benchmark on hold |

---

## Remain distinct

| Document set | Reason |
|--------------|--------|
| P0-B schema vs P0-D benchmark record schema | Different lifecycle — evaluation vs production record |
| P0-C annotation vs P0-D adjudication | Human annotation vs gold authority |
| Integration pilot vs B0 | Integration proof vs classifier quality |
| Legacy comparison vs benchmark metrics | Diagnostic vs gold evaluation |

---

## Reference-not-duplication rule

New documents must cite canonical owner by ID:

```text
See: orca-semantic-record-invariants #2 (ACCEPT requires commercial evidence)
```

Do not paste full invariant text into multiple charters.
