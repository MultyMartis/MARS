# ORCA Semantic Intelligence — Architecture Decision Record v1

**ADR ID:** `orca-semantic-intelligence-adr`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `APPROVED — IMPLEMENTATION NOT STARTED`

---

## 1. Context

ORCA requires a governed semantic intelligence layer separating **topical relevance** from **commercial intent** before Campaign Production. World-practice research (2026-06) was selectively adopted per operator decision **D1**. Corvonero clean-room v1 exposed systematic over-admission (~1892 accepts from ~2370 phrases) and is frozen per **D2**. Operator decisions **D3–D7** define thresholds, abstention, benchmark scope, canonical research locus, and production restart boundary.

This ADR defines the **target architecture** for ORCA Semantic Intelligence v1. It is **document-first** and **implementation-neutral**. No runtime, classifier, or benchmark is claimed.

---

## 2. Problem statement

ORCA lacks an approved multi-stage semantic authority chain. Diagnostic pipelines treated service-scope topical match as sufficient for commercial admission. Downstream campaign production, clustering, and negatives amplified these errors. A single «smart classifier» cannot safely own commercial eligibility without hierarchical gates, explicit abstention, human adjudication, semantic freeze, and export parity controls.

---

## 3. Confirmed failure mode

**Topic match mistaken for commercial intent.**

Evidence:

- Corvonero clean-room v1: career, educational, DIY, regulatory, and navigational strata admitted to commercial path.
- Diagnostic artifacts marked `DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE`.
- Research review and gap matrix align on Layer 6–8 maturity: screening and eligibility **DIAGNOSTIC FAILED** or **ABSENT** as validated capability.

---

## 4. Architecture goals

1. Separate business authority from market evidence and semantic decisions.
2. Enforce hierarchical gates SI-01 through SI-17.
3. Treat ACCEPT, REJECT, and ABSTAIN as distinct outcomes.
4. Route uncertainty to human review — ABSTAIN is controlled safety, not failure.
5. Run service mapping only after commercial eligibility.
6. Run clustering only after eligibility and ownership.
7. Form negatives only after ownership.
8. Freeze Semantic Core before Campaign Production.
9. Keep export as transport-only layer.
10. Confine post-launch learning to proposals without mutating pre-launch authority.
11. Meet D3 pilot thresholds before auto-admission at scale.
12. Preserve auditability and version discipline.

---

## 5. Non-goals

- Building or deploying a classifier in this ADR cycle.
- Creating annotation guideline, benchmark, or gold labels (P0-C/D).
- Rerunning Corvonero semantic admission.
- Authorizing Campaign Production, Commander export, import, or launch.
- Claiming ORCA runtime or orchestration product exists.
- Auto-promoting all research recommendations.
- Replacing operator business scope decisions with model output.

---

## 6. Authority model

Strict hierarchy (lower cannot override higher):

1. Explicit operator decisions (D1–D7 and future versioned decisions).
2. Approved business scope (SI-01).
3. Approved Semantic Core (SI-14, state `APPROVED` only).
4. Approved annotation guideline (future P0-C).
5. Benchmark / gold labels (future P0-D).
6. Versioned deterministic rules (SI-06 narrow exclusions).
7. Calibrated model output (advisory until P0-G pass).
8. LLM-assisted adjudication (SI-09, structured assistance only).
9. Clustering suggestions (SI-11, non-authoritative).
10. Campaign production (SI-15, consumer only).
11. Export formatting (SI-16, transport only).
12. Post-launch proposals (SI-17, non-mutating).

See `ORCA-SEMANTIC-INTELLIGENCE-AUTHORITY-MODEL-v1.md`.

---

## 7. Selected architecture

**ORCA Semantic Intelligence v1** — a managed multi-stage system documented as layers SI-01 through SI-17:

| Layer | Name |
|-------|------|
| SI-01 | Operator Authority |
| SI-02 | Market Evidence |
| SI-03 | Source Corpus |
| SI-04 | Normalization |
| SI-05 | Query Understanding |
| SI-06 | Hard Exclusion Screening |
| SI-07 | Intent Classification |
| SI-08 | Commercial Eligibility |
| SI-09 | Semantic Adjudication |
| SI-10 | Service Mapping |
| SI-11 | Cluster Discovery |
| SI-12 | Negative Intelligence |
| SI-13 | Human Review |
| SI-14 | Semantic Core Authority |
| SI-15 | Campaign Production Handoff |
| SI-16 | External Artifact QA |
| SI-17 | Post-Launch Learning |

**Not** a monolithic classifier. Hybrid components (rules, models, LLM, human) operate within layer boundaries and authority ranks.

---

## 8. Alternatives considered

| Alternative | Outcome |
|-------------|---------|
| Single supervised classifier end-to-end | **Rejected** — insufficient protected-strata control; Corvonero diagnostic evidence |
| Topical relevance + inline negatives only | **Rejected** — confirmed failure mode |
| Full LLM-as-judge for all phrases | **Rejected** — instability; no benchmark; violates authority model |
| Manual-only review without gates | **Rejected** — does not scale; no reproducible thresholds |
| Promote Corvonero v1 diagnostic decisions | **Rejected** per D2 |
| Defer architecture until benchmark built | **Rejected** — architecture must precede P0-B/C/D |

---

## 9. Decision rationale

Selective research promotion (see promotion matrix) plus operator decisions D1–D7 require a **documented layer model** before taxonomy, guideline, and benchmark work. Hierarchical gates isolate failure domains. ABSTAIN prevents forced commercial interpretation. Semantic freeze enforces Campaign Production separation already partially documented in Campaign Production Contract v1 and Triumph-derived laws.

---

## 10. Layer boundaries

Each layer owns defined inputs/outputs and **cannot** perform prohibited actions listed in architecture flow document. Key prohibitions:

- SI-02 cannot declare commercial eligibility.
- SI-03 cannot create semantic decisions.
- SI-06 cannot classify ambiguous problem queries as commercial.
- SI-08 cannot infer ACCEPT from service term presence alone.
- SI-10 cannot change eligibility.
- SI-11 cannot create campaign groups or merge conflicting primary intents.
- SI-12 cannot rescue bad base phrases via long negatives.
- SI-15 cannot alter approved semantic fields.
- SI-16 cannot silently repair semantics.
- SI-17 cannot mutate approved core without versioned review.

Full layer specs: `ORCA-SEMANTIC-INTELLIGENCE-FLOW-v1.md`.

---

## 11. Human review model

SI-13 owns queues: ABSTAIN, protected strata, high-risk ACCEPT, conflicts, random ACCEPT/REJECT audit, model disagreement, blind evaluation. Human reviewer and operator retain adjudication authority per governance. LLM may assist SI-09 with structured output — never final authority.

---

## 12. Admission policy

Three outcomes at SI-08: `ACCEPT`, `REJECT`, `ABSTAIN`. Policy detail: `ORCA-SEMANTIC-ADMISSION-POLICY-v1.md`. Corvonero initial risk mode: **CONSERVATIVE**.

---

## 13. Semantic freeze policy

Semantic Core (SI-14) states: `DRAFT` → `IN REVIEW` → `APPROVED` | `REJECTED` | `SUPERSEDED`. Only `APPROVED` unlocks SI-15 Campaign Production Handoff. Operator sign-off required per D7 and future P0-H contract.

---

## 14. Production separation

Campaign Production consumes approved Semantic Core only. No phrase restoration, intent change, eligibility override, or ownership change without return to Semantic Core gate. Aligns with `ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md`.

---

## 15. Quality gates

Operator-approved pilot thresholds (D3):

- Commercial Precision on auto-accept: **≥ 0.95**
- Protected-strata FPR: **≤ 0.01** per class (career, educational, DIY/how-to, regulatory, navigational)
- Explicit ABSTAIN: **mandatory**
- Campaign production before approved core: **prohibited**

Additional metrics: `PROPOSED — BENCHMARK VALIDATION REQUIRED`. See quality gates document.

---

## 16. Versioning

All layers, rules, models, guidelines, benchmarks, and Semantic Core artifacts are versioned. Supersede requires explicit gate — no silent overwrite. Diagnostic Corvonero v1 artifacts remain frozen at v1 diagnostic markers.

---

## 17. Auditability

Every semantic decision record must support: phrase ID, layer version, rule/model versions, confidence, outcome, evidence pointers, reviewer ID (if human), timestamp, and dependency on operator scope version. Export parity checks (SI-16) provide downstream audit trail.

---

## 18. Risks

See `ORCA-SEMANTIC-INTELLIGENCE-ARCHITECTURE-RISKS-v1.md`. Top risks: over-admission, excessive abstention, LLM instability, campaign-layer contamination, benchmark bias.

---

## 19. Deferred decisions

- Second-model review implementation timing.
- Active learning loop design.
- Optimal abstention rate in production (research suggests ≥ 0.15 early — not operator-validated).
- Specific classifier architecture selection.
- Full contract field schemas (P0-B onward).
- Commander template field binding updates.

---

## 20. Consequences

**Positive:** Clear promotion path P0-B through P0-H; Corvonero corpus reusable; failure mode bounded; export contamination prevented.

**Negative:** Higher initial abstention queue; annotation and benchmark investment required before rerun; longer time-to-campaign vs defective fast path.

---

## 21. Migration impact

Reusable: Corvonero intake, scope, MIG ledger, source/normalized/canonical corpus, research package, compatible Campaign Production Contract elements.

Diagnostic only: clean-room v1 intent, eligibility, mapping, clusters, negatives, review workbook, old v1–v7.1 production.

Must create later: taxonomy, guideline, benchmark, gold labels, pilot corpus, baselines, evaluation harness, approved Semantic Core.

No semantic decision migration from diagnostic layers. See migration boundary document.

---

## 22. Corvonero restart impact

Corvonero remains **FROZEN** until: ADR approved → P0-B/C/D/E/F/G → operator Semantic Core sign-off (P0-H) → new admission from preserved corpus only. Initial admission mode: **CONSERVATIVE**. v1 diagnostic decisions **must not** contaminate rerun.

---

## 23. Approval gate

| Requirement | Status |
|-------------|--------|
| ADR v1 operator review | **REQUIRED** |
| Architecture validation pass | See validation document |
| P0-A complete | **PENDING APPROVAL** |
| Next task | **P0-B — Semantic Taxonomy and Record Schema** |
| Classifier / benchmark / annotation | **NOT STARTED** |
| Campaign production / Commander | **BLOCKED** |

**Approver:** MARS operator  
**Maintainer:** ORCA Architecture Governance Maintainer

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-adr-v1.json` |
| Promotion matrix | `ORCA-SEMANTIC-INTELLIGENCE-RESEARCH-PROMOTION-MATRIX-v1.md` |
| Operator decisions | `research/ppc-semantic-intelligence/world-practice-2026-06/decisions/` |
| Corvonero freeze | `projects/corvonero-direct-v2-clean-room/PROJECT.md` |
