# ORCA PPC Semantic Intelligence — Promotion Backlog v1

**Backlog ID:** `orca-ppc-semantic-intelligence-promotion-backlog`  
**Version:** v1  
**Status:** P0-A `APPROVED — CHECKPOINTED`; P0-B `APPROVED — CHECKPOINTED` (`3151953`); P0-C `APPROVED — IMPLEMENTATION NOT STARTED` (C1–C7); P0-D `AUTHORIZED — NOT STARTED`  
**Authority:** Selective promotion only — no automatic adoption of research

---

## P0-A — Architecture Decision Record

| Field | Value |
|-------|-------|
| Purpose | Selectively promote research findings into versioned ORCA Semantic Intelligence architecture |
| Inputs | World-practice research v1; operator decisions D1–D7; gap matrix |
| Outputs | `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md` |
| Dependencies | Research intake complete |
| Authority | Operator + architecture maintainer |
| Gate | ADR approved before P0-B implementation drafting |
| Prohibited claims | Not runtime; not classifier; not auto-promoted research |
| Corvonero impact | Unblocks design path for v2 semantic rerun |
| Status | **APPROVED — CHECKPOINTED** (commit `f17c270`) |

---

## P0-B — Semantic Taxonomy and Record Schema

| Field | Value |
|-------|-------|
| Purpose | Define per-phrase semantic record schema |
| Inputs | Research adjudication table; D4 abstention policy |
| Outputs | `semantic-intelligence/` — taxonomy, schema, invariants, fixtures (MD + JSON) |
| Dependencies | P0-A |
| Authority | Architecture ADR |
| Gate | Schema version frozen before annotation guideline |
| Prohibited claims | Not phrase registry; not production decisions |
| Corvonero impact | Required before new admission run |
| Status | **APPROVED — CHECKPOINTED** (commit `3151953`, operator B1–B7) |

---

## P0-C — Annotation Guideline

| Field | Value |
|-------|-------|
| Purpose | Human-readable rules, examples, counterexamples, adjudication policy |
| Inputs | P0-B schema; research failure-mode catalogue; Corvonero diagnostic examples |
| Outputs | Annotation guideline MD + worked examples |
| Dependencies | P0-B |
| Authority | Operator authority |
| Gate | Guideline approved before benchmark annotation |
| Prohibited claims | Not benchmark data itself |
| Corvonero impact | Required per D2 before semantic rerun |
| Status | **APPROVED — IMPLEMENTATION NOT STARTED** (operator C1–C7) |

---

## P0-D — Benchmark Charter

| Field | Value |
|-------|-------|
| Purpose | Universal ORCA benchmark program charter |
| Inputs | D5 sizing (1200–2000 phrases); research strata table; approved P0-C guideline |
| Outputs | Charter: strata, double annotation, disagreements, adjudication, blind split, regression anchors, hard negatives, versioning |
| Dependencies | P0-C |
| Authority | Operator + QA owner |
| Gate | Gold freeze before baseline evaluation |
| Prohibited claims | Not trained model; not production core |
| Corvonero impact | Parent program for Corvonero pilot |
| Status | **AUTHORIZED — NOT STARTED** |

---

## P0-E — Corvonero Pilot Charter

| Field | Value |
|-------|-------|
| Purpose | Bounded Corvonero pilot within universal benchmark |
| Inputs | D5 (300–500 phrases); D3 thresholds; preserved corpus |
| Outputs | Pilot charter: balanced strata, blind subset, operator role, go/no-go thresholds, prohibited downstream work |
| Dependencies | P0-D |
| Authority | Operator authority |
| Gate | Pilot pass required before full corpus admission rerun |
| Prohibited claims | Not campaign production authorization |
| Corvonero impact | Direct go/no-go for v2 semantic line |
| Status | **NOT STARTED** |

---

## P0-F — Baseline Implementations

| Field | Value |
|-------|-------|
| Purpose | Compare admission baselines before hybrid production path |
| Inputs | P0-C guideline; benchmark dev split |
| Outputs | Evaluation reports for: deterministic rules baseline; structured LLM baseline; hybrid hierarchical baseline |
| Dependencies | P0-D partial dev set |
| Authority | Data/ML engineer + operator |
| Gate | Baselines measured before threshold tuning |
| Prohibited claims | Not validated production classifier |
| Corvonero impact | Informs upgraded admission for rerun |
| Status | **NOT STARTED** |

---

## P0-G — Evaluation and Threshold Gate

| Field | Value |
|-------|-------|
| Purpose | Measure production-blocker metrics and calibration |
| Inputs | P0-F baselines; blind test; D3 thresholds |
| Outputs | Gate report: commercial precision, protected-strata FPR, abstention, ambiguity recall, service-mapping precision, calibration, human disagreement |
| Dependencies | P0-F, P0-E blind set |
| Authority | Operator go/no-go |
| Gate | Pass required for full corpus rerun and P0-H |
| Prohibited claims | Not launch approval |
| Corvonero impact | Blocks or permits semantic rerun |
| Status | **NOT STARTED** |

---

## P0-H — Semantic Core Authority Contract

| Field | Value |
|-------|-------|
| Purpose | Block campaign production until approved Semantic Core exists |
| Inputs | D7; campaign production contract v1; gap layer 13 |
| Outputs | Semantic Core Authority Contract MD + JSON |
| Dependencies | P0-G pass |
| Authority | Operator sign-off |
| Gate | Explicit sign-off before any campaign architecture |
| Prohibited claims | Not Commander export authorization alone |
| Corvonero impact | **CRITICAL** — campaign production remains blocked until signed |
| Status | **NOT STARTED** |

---

## Ordering

```text
P0-A → P0-B → P0-C → P0-D → P0-E → P0-F → P0-G → P0-H
```

Parallel allowed only where dependencies explicitly permit (e.g. P0-E drafting after P0-D charter outline — not annotation execution).
