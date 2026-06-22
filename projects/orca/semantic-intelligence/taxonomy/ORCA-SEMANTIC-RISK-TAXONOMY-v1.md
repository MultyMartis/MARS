# ORCA Semantic Risk Taxonomy v1

**Taxonomy ID:** `orca-semantic-risk-taxonomy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-risk-taxonomy-v1.json`](orca-semantic-risk-taxonomy-v1.json)

---

## Purpose

Multi-dimensional **risk** assessment informs review priority and blocking. **High risk does not automatically mean REJECT** — it may require ABSTAIN and human review.

---

## Risk classes

| Class | Meaning |
|-------|---------|
| `LOW` | Automated path acceptable with standard gates |
| `MEDIUM` | Elevated review sampling |
| `HIGH` | Reviewer normally required; automated ACCEPT discouraged |
| `CRITICAL` | Blocking conditions may apply; no automated ACCEPT |

---

## Risk dimensions

| Dimension | Description |
|-----------|-------------|
| `FALSE_POSITIVE_SPEND` | Риск платного показа по нецелевому запросу. |
| `PROTECTED_STRATA` | Риск попадания career/educational/diy/regulatory в платный трафик. |
| `AMBIGUITY` | Риск решения при неразрешённой неоднозначности. |
| `SERVICE_MISMATCH` | Риск неверного service candidate. |
| `LANDING_MISMATCH` | Риск несоответствия посадочной странице. |
| `PRODUCT_SERVICE_MISMATCH` | Риск смешения продукта и услуги. |
| `NEGATIVE_OVERBLOCKING` | Риск излишнего REJECT целевых запросов. |
| `DOMAIN_KNOWLEDGE` | Риск ошибки из-за недостатка доменного контекста. |
| `MORPHOLOGY_OPERATOR` | Риск морфологии/операторов Яндекс. |
| `UNSUPPORTED_CLAIM` | Риск необоснованного утверждения в narrative. |
| `PROVENANCE` | Риск решения без полной provenance. |
| `MODEL_DISAGREEMENT` | Риск расхождения assessors. |

---

## Aggregation

**Rule:** `risk.overall_risk` = **maximum** of all assessed dimension risks, **unless** a blocking condition elevates or caps the outcome.

Example: dimensions `{PROTECTED_STRATA: MEDIUM, AMBIGUITY: HIGH}` → `overall_risk: HIGH`.

Populate `risk.dimensions` as object mapping dimension → risk class. List active conditions in `risk.blocking_conditions`.

### Blocking conditions (examples)

- `UNRESOLVED_MANDATORY_AMBIGUITY`
- `PROTECTED_STRATA_CONFLICT`
- `PROVENANCE_INCOMPLETE`
- `MODEL_DISAGREEMENT_UNRESOLVED`
- `SERVICE_CATALOG_MISS`

When blocking applies, automated ACCEPT is forbidden regardless of `may_support_accept` on intent.

---

## Human review conditions

Human review is **normally required** when:

1. `overall_risk` is HIGH or CRITICAL
2. `commercial_eligibility.reviewer_required` is true
3. `primary_intent.human_review_normally_required` is true for assigned intent
4. Any mandatory ambiguity type unresolved
5. `review.workflow_status` is `ABSTAIN_PENDING_REVIEW`

---

## Related documents

- [`ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md)
- [`ORCA-SEMANTIC-REVIEW-STATUS-v1.md`](ORCA-SEMANTIC-REVIEW-STATUS-v1.md)
