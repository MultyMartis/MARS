# ORCA Semantic Intelligence — Component Responsibility Matrix v1

**Matrix ID:** `orca-semantic-intelligence-component-responsibility`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Components

| Component | Layers | Authority level |
|-----------|--------|-----------------|
| Deterministic rules | SI-06 | High-confidence narrow exclusions |
| Weak supervision | SI-06 hints, SI-07 features | Non-authoritative signals |
| Supervised classifier | SI-07, SI-08 | Advisory until P0-G |
| Embeddings / retrieval | SI-09 examples, SI-11 | Non-decision support |
| LLM | SI-09 structured assistance | Assistance only |
| Human reviewer | SI-09, SI-13 | Adjudication |
| Operator | SI-01, SI-14, gates | Policy and release |
| Validator | SI-16 | Parity check — fail closed |

---

## Deterministic rules

| Field | Value |
|-------|-------|
| Permitted | SI-06 hard exclusions; morphology-safe normalization rules in SI-04; operator-scope prohibitions |
| Prohibited | Commercial ACCEPT for ambiguous queries; service mapping; clustering; negative rescue |
| Required evidence | Rule ID, version, regression anchor pass |
| Output type | `EXCLUDED` \| `PASS` with rule citation |
| Authority level | Rank 6 — overrides models on narrow classes only |
| Versioning | Semantic version + changelog |
| Fallback | On rule conflict → ABSTAIN |

---

## Weak supervision

| Field | Value |
|-------|-------|
| Permitted | Pattern-based hints; heuristic features for SI-05/SI-07; training signal generation (future) |
| Prohibited | Direct ACCEPT/REJECT without SI-08 gate; overriding gold labels |
| Required evidence | Pattern source, coverage stats, error rate on dev set |
| Output type | Feature weights, weak labels (non-binding) |
| Authority level | Below benchmark and rules |
| Versioning | Pattern set version |
| Fallback | Ignore weak labels on disagreement with gold |

---

## Supervised classifier

| Field | Value |
|-------|-------|
| Permitted | Intent classification; eligibility probability; confidence scores |
| Prohibited | Final authority; protected-strata auto-ACCEPT without threshold; overriding operator scope |
| Required evidence | Model card, training data version, calibration report, P0-G pass |
| Output type | Intent distribution, eligibility probability, calibrated confidence |
| Authority level | Rank 7 — advisory until P0-G |
| Versioning | Model artifact hash + training snapshot |
| Fallback | ABSTAIN on low confidence or OOD detection |

---

## Embeddings / retrieval

| Field | Value |
|-------|-------|
| Permitted | Similar phrase retrieval for adjudication; cluster candidate suggestions |
| Prohibited | Commercial eligibility decision; merging conflicting intents |
| Required evidence | Embedding model version, neighbor audit sample |
| Output type | Neighbor lists, similarity scores |
| Authority level | Rank 8–9 support |
| Versioning | Embedding model version |
| Fallback | Disable retrieval on stale index |

---

## LLM

| Field | Value |
|-------|-------|
| Permitted | Structured adjudication drafts; feature extraction assistance; rationale generation |
| Prohibited | Sole authority; unversioned prompts; silent ACCEPT |
| Required evidence | Prompt version, model ID, structured output schema validation |
| Output type | JSON adjudication proposal with confidence |
| Authority level | Rank 8 — below human/operator |
| Versioning | Prompt template version + model ID |
| Fallback | Route to human on parse failure or low confidence |

**Decision:** Pure LLM is **not** the core authority.

---

## Human reviewer

| Field | Value |
|-------|-------|
| Permitted | Resolve ABSTAIN; override high-risk ACCEPT; adjudicate conflicts; blind evaluation |
| Prohibited | Bulk override without audit; changing operator scope; skipping protected-strata protocol |
| Required evidence | Reviewer ID, guideline version, decision rationale |
| Output type | Final ACCEPT/REJECT with audit trail |
| Authority level | Rank 8–9 adjudication; below operator sign-off |
| Versioning | Guideline version binding |
| Fallback | Escalate to operator |

---

## Operator

| Field | Value |
|-------|-------|
| Permitted | Business scope; risk mode; threshold governance; Semantic Core approval; policy overrides |
| Prohibited | Bypassing benchmark gate for auto-admission at scale |
| Required evidence | Versioned operator decisions |
| Output type | Scope manifest, approval records |
| Authority level | Rank 1–3 |
| Versioning | Decision registry |
| Fallback | SAFE UNKNOWN — halt production |

---

## Validator

| Field | Value |
|-------|-------|
| Permitted | Parity checks SI-16; schema validation; invariant checks |
| Prohibited | Semantic repair; silent field correction |
| Required evidence | Validator version, diff report |
| Output type | PASS/FAIL with field-level diffs |
| Authority level | Transport integrity only |
| Versioning | Validator script version |
| Fallback | Fail closed — block export |

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-component-responsibility-matrix-v1.json` |
