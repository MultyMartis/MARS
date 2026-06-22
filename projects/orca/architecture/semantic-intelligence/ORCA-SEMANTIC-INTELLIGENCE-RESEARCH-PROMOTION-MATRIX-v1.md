# ORCA Semantic Intelligence — Research Promotion Matrix v1

**Matrix ID:** `orca-semantic-intelligence-research-promotion-matrix`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `APPROVED — ADR OPERATOR SIGNED`  
**Authority:** Selective promotion per operator decision D1 — not automatic adoption

---

## Purpose

Record promotion status for each major world-practice research recommendation into ORCA Semantic Intelligence v1 target architecture.

## Promotion statuses

| Status | Meaning |
|--------|---------|
| `PROMOTED` | Adopted into target architecture with minimal adaptation |
| `PROMOTED WITH ADAPTATION` | Adopted with ORCA-specific constraints |
| `DEFERRED` | Valid direction; blocked on prerequisites |
| `REJECTED` | Not adopted as architecture authority |
| `SAFE UNKNOWN` | Insufficient evidence for promotion decision |

---

## Promotion items

### 1. Hierarchical gates

| Field | Value |
|-------|-------|
| Research recommendation | Multi-stage pipeline: source → understanding → screening → intent → eligibility → adjudication → mapping → clusters → negatives → core freeze |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | 17 documented layers SI-01 through SI-17; hard exclusions separated from adjudication |
| Reason | Confirmed Corvonero failure: single topical gate caused over-admission |
| Dependency | P0-A ADR approval |
| Implementation phase | Architecture (P0-A); contracts P0-B+ |
| Risks | Layer sprawl without contracts |
| Operator approval status | **APPROVED (ADR v1)** |

### 2. Conservative auto-admission

| Field | Value |
|-------|-------|
| Research recommendation | Default conservative admission; high precision on auto-accept |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | Three risk modes; Corvonero initial mode `CONSERVATIVE`; D3 thresholds operator-approved |
| Reason | Cost-sensitive B2B leads; D3 commercial precision ≥ 0.95 |
| Dependency | D3; P0-G threshold gate |
| Implementation phase | P0-F/G baselines; pilot admission |
| Risks | Low recall if thresholds too strict |
| Operator approval status | **APPROVED (D3)** |

### 3. Explicit ABSTAIN

| Field | Value |
|-------|-------|
| Research recommendation | ABSTAIN as first-class outcome; not failure |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | Mandatory per D4; routed to SI-09 adjudication and SI-13 human review |
| Reason | Operator decision D4; prevents invented commercial interpretation |
| Dependency | D4; P0-B schema |
| Implementation phase | P0-B taxonomy; P0-C guideline |
| Risks | Excessive abstention queue load |
| Operator approval status | **APPROVED (D4)** |

### 4. Human-in-the-loop

| Field | Value |
|-------|-------|
| Research recommendation | Human review for ambiguity, protected strata, high-risk ACCEPT |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | SI-13 queues; operator retains final authority on Semantic Core |
| Reason | MARS human-operated principles; Triumph battle evidence |
| Dependency | P0-C guideline; P0-H Semantic Core contract |
| Implementation phase | P0-C onward |
| Risks | Reviewer fatigue; confirmation bias |
| Operator approval status | **APPROVED (ADR v1)** |

### 5. Gold dataset

| Field | Value |
|-------|-------|
| Research recommendation | Versioned gold benchmark with strata and regression anchors |
| Promotion decision | **PROMOTED WITH ADAPTATION** |
| ORCA adaptation | Dual scope per D5: universal 1200–2000 + Corvonero pilot 300–500 |
| Reason | D5 operator sizing; required before threshold validation |
| Dependency | P0-C guideline; P0-D charter |
| Implementation phase | P0-D/E |
| Risks | Benchmark bias; annotation inconsistency |
| Operator approval status | **PROPOSED — P0-D charter drafted** |

### 6. Double annotation

| Field | Value |
|-------|-------|
| Research recommendation | Independent double annotation with adjudication on disagreement |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | Required in P0-D benchmark charter; blind split mandatory |
| Reason | Research quality practice; reduces single-annotator bias |
| Dependency | P0-C guideline |
| Implementation phase | P0-D |
| Risks | Cost; inter-annotator disagreement volume |
| Operator approval status | **PROPOSED — P0-D charter drafted** |

### 7. Weak supervision

| Field | Value |
|-------|-------|
| Research recommendation | Rules + heuristics + pattern labels as weak signals |
| Promotion decision | **PROMOTED WITH ADAPTATION** |
| ORCA adaptation | Limited to SI-06 hard exclusions and feature hints for SI-07; cannot auto-ACCEPT |
| Reason | Useful for narrow high-confidence exclusions; dangerous for commercial admission |
| Dependency | P0-F baselines |
| Implementation phase | P0-F hybrid baseline |
| Risks | Weak labels propagate errors if promoted to authority |
| Operator approval status | **APPROVED (ADR v1)** |

### 8. Supervised classifier

| Field | Value |
|-------|-------|
| Research recommendation | Trained intent/eligibility classifier with calibration |
| Promotion decision | **PROMOTED WITH ADAPTATION** |
| ORCA adaptation | Advisory output only until P0-G pass; cannot override rules or operator |
| Reason | Research supports hybrid stack; no validated model exists |
| Dependency | P0-D gold; P0-F baselines; P0-G gate |
| Implementation phase | P0-F/G |
| Risks | False confidence; domain transfer failure |
| Operator approval status | **NOT STARTED** |

### 9. Embeddings

| Field | Value |
|-------|-------|
| Research recommendation | Embedding similarity for clustering and retrieval |
| Promotion decision | **PROMOTED WITH ADAPTATION** |
| ORCA adaptation | Retrieval and cluster candidate support only (SI-11); cannot decide commercial eligibility |
| Reason | Lexical similarity caused intent merge failures in diagnostic runs |
| Dependency | P0-B schema; approved eligibility layer |
| Implementation phase | Post P0-G |
| Risks | False clustering by surface similarity |
| Operator approval status | **APPROVED (ADR v1)** |

### 10. LLM adjudication

| Field | Value |
|-------|-------|
| Research recommendation | LLM for structured adjudication of ambiguous queries |
| Promotion decision | **PROMOTED WITH ADAPTATION** |
| ORCA adaptation | SI-09 assistance only; structured output; human/operator final authority |
| Reason | Useful for ABSTAIN queue; instability requires versioning and audit |
| Dependency | P0-C guideline; benchmark examples |
| Implementation phase | P0-F baseline; production path post P0-G |
| Risks | LLM instability; hallucinated commercial intent |
| Operator approval status | **APPROVED (ADR v1)** |

### 11. Second-model review

| Field | Value |
|-------|-------|
| Research recommendation | Independent model review on high-risk ACCEPT |
| Promotion decision | **DEFERRED** |
| ORCA adaptation | Optional audit queue in SI-13 after primary hybrid path validated |
| Reason | Valid safety pattern; premature before first baseline |
| Dependency | P0-F/G primary baselines |
| Implementation phase | Post P0-G optional enhancement |
| Risks | Cost duplication |
| Operator approval status | **DEFERRED** |

### 12. Commercial precision threshold

| Field | Value |
|-------|-------|
| Research recommendation | Commercial precision on auto-accept as primary blocker metric |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | ≥ 0.95 per D3 on auto-accept path |
| Reason | Operator decision D3 |
| Dependency | P0-G evaluation gate |
| Implementation phase | P0-G |
| Risks | Metric gaming via excessive ABSTAIN |
| Operator approval status | **APPROVED (D3)** |

### 13. Protected-strata FPR

| Field | Value |
|-------|-------|
| Research recommendation | Per-class FPR caps on career, educational, DIY, regulatory, navigational |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | ≤ 0.01 per protected class per D3 |
| Reason | Corvonero v1 leaked protected strata to ACCEPT |
| Dependency | P0-D strata design; P0-G measurement |
| Implementation phase | P0-G |
| Risks | Under-detection of edge cases within strata |
| Operator approval status | **APPROVED (D3)** |

### 14. Calibration

| Field | Value |
|-------|-------|
| Research recommendation | Probability calibration before threshold application |
| Promotion decision | **PROMOTED WITH ADAPTATION** |
| ORCA adaptation | Required for model-assisted paths; proposed metric in P0-G |
| Reason | Research + cost-sensitive classification literature |
| Dependency | P0-F baselines; blind test |
| Implementation phase | P0-G |
| Risks | Calibration drift over time |
| Operator approval status | **PROPOSED — BENCHMARK VALIDATION REQUIRED** |

### 15. Active learning

| Field | Value |
|-------|-------|
| Research recommendation | Prioritize annotation of uncertain/disagreement cases |
| Promotion decision | **DEFERRED** |
| ORCA adaptation | Post-launch and benchmark iteration only |
| Reason | Requires running annotation program first |
| Dependency | P0-D/E operational |
| Implementation phase | Post P0-G |
| Risks | Feedback leakage from production |
| Operator approval status | **DEFERRED** |

### 16. Semantic freeze

| Field | Value |
|-------|-------|
| Research recommendation | Freeze Semantic Core before Campaign Production |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | SI-14 states DRAFT → IN REVIEW → APPROVED; only APPROVED unlocks SI-15 |
| Reason | Operator D7; Triumph production laws |
| Dependency | P0-H contract |
| Implementation phase | P0-H |
| Risks | Stale core if market shifts — versioned supersede path required |
| Operator approval status | **APPROVED (D7)** |

### 17. Negatives after ownership

| Field | Value |
|-------|-------|
| Research recommendation | Negative intelligence only after service ownership and clusters |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | SI-12 runs after SI-10 and SI-11; cannot rescue bad base phrases |
| Reason | Research + Corvonero diagnostic; inline negatives masked admission errors |
| Dependency | P0-B schema |
| Implementation phase | Architecture now; implementation post eligibility |
| Risks | Negative overblocking |
| Operator approval status | **APPROVED (ADR v1)** |

### 18. Task-based clustering

| Field | Value |
|-------|-------|
| Research recommendation | Cluster by user task and landing compatibility, not lexical similarity alone |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | SI-11 cluster discovery; cannot merge different primary intents |
| Reason | Research failure mode: lexical clustering hides intent conflicts |
| Dependency | P0-B intent taxonomy |
| Implementation phase | Post eligibility + mapping |
| Risks | Subjective task boundaries |
| Operator approval status | **APPROVED (ADR v1)** |

### 19. External artifact QA

| Field | Value |
|-------|-------|
| Research recommendation | Parity validation across semantic core, XLSX, Commander import |
| Promotion decision | **PROMOTED** |
| ORCA adaptation | SI-16 transport-only export; no silent semantic repair |
| Reason | Triumph exporter baseline; campaign contract v1 |
| Dependency | P0-H; existing export contracts where compatible |
| Implementation phase | P0-H + campaign handoff |
| Risks | Format drift vs semantic truth |
| Operator approval status | **APPROVED (ADR v1)** |

### 20. Post-launch learning

| Field | Value |
|-------|-------|
| Research recommendation | Search terms and performance feed proposal loop |
| Promotion decision | **PROMOTED WITH ADAPTATION** |
| ORCA adaptation | SI-17 proposals only; cannot mutate approved core without versioned gate |
| Reason | Research best practice; prevents feedback leakage into pre-launch authority |
| Dependency | Approved Semantic Core; launch (out of scope) |
| Implementation phase | Post launch — documentation now |
| Risks | Post-launch feedback leakage |
| Operator approval status | **APPROVED (ADR v1)** |

---

## Summary counts

| Status | Count |
|--------|-------|
| PROMOTED | 10 |
| PROMOTED WITH ADAPTATION | 7 |
| DEFERRED | 2 |
| REJECTED | 0 |
| SAFE UNKNOWN | 0 |

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-research-promotion-matrix-v1.json` |
| Operator decisions | `research/ppc-semantic-intelligence/world-practice-2026-06/decisions/` |
| ADR | `ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md` |
