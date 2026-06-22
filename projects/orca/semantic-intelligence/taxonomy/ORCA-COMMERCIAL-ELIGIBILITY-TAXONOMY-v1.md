# ORCA Commercial Eligibility Taxonomy v1

**Taxonomy ID:** `orca-commercial-eligibility-taxonomy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-commercial-eligibility-taxonomy-v1.json`](orca-commercial-eligibility-taxonomy-v1.json)

---

## Purpose

`commercial_eligibility` is the **PPC gate output**: exactly one of `ACCEPT`, `REJECT`, or `ABSTAIN`. Distinct from `primary_intent` and from `review.workflow_status`.

---

## Decisions

| Decision | Meaning |
|----------|---------|
| `ACCEPT` | Positive commercial evidence; phrase may enter approved semantic core path (subject to review gates) |
| `REJECT` | Clear non-commercial or incompatible intent; exclude from paid acquisition |
| `ABSTAIN` | Insufficient or conflicting evidence; **valid terminal** for automation |

---

## Required fields on eligibility record

Object `commercial_eligibility`:

| Field | Required | Description |
|-------|----------|-------------|
| `decision` | **yes** | ACCEPT / REJECT / ABSTAIN |
| `reason_code` | **yes** | Family code from tables below (machine-stable) |
| `confidence` | **yes** | 0.0–1.0 assessor confidence |
| `reviewer_required` | **yes** | Whether human review is mandatory before core promotion |
| `phrase_explanation` | recommended | Short operator-readable rationale (no sentinels) |
| `supporting_evidence` | recommended | List of evidence strings or signal refs |
| `opposing_evidence` | recommended | Evidence against the decision |
| `threshold_profile` | optional | e.g. CONSERVATIVE, STANDARD |

**Conditional:** ABSTAIN records must have `ambiguity.unresolved_questions` with at least one item.

---

## ACCEPT reason families

| reason_code family | When to use |
|--------------------|-------------|
| `EXPLICIT_PROVIDER_REQUEST` | EXPLICIT PROVIDER_HIRE; clear hire-provider goal |
| `EXPLICIT_SERVICE_REQUEST` | Explicit commercial service verb + service object |
| `EXPLICIT_IMPLEMENTATION_CONFIGURATION_MODIFICATION` | Clear paid implementation/config/modification request |
| `EXPLICIT_SUPPORT_RECOVERY_REQUEST` | Explicit support/recovery engagement |
| `STRONG_PAID_SERVICE_PROBLEM_INTENT` | Problem + strong provider/support path (not DIY) |
| `STRONG_GEOGRAPHY_PLUS_SERVICE_INTENT` | GEOGRAPHY STRONG + commercial service signals |
| `VALIDATED_OPERATOR_SEED` | Operator-prevalidated seed (audit trail required) |

**Invariant:** Topic match alone cannot support ACCEPT.

---

## REJECT reason families

| reason_code family | When to use |
|--------------------|-------------|
| `CLEAR_EDUCATION` | EDUCATIONAL protected stratum |
| `CLEAR_CAREER_SEEKER` | SEEK_EMPLOYMENT / CAREER_SEEKER |
| `CLEAR_DIY_HOW_TO` | DIY_HOW_TO protected stratum |
| `CLEAR_REGULATORY_INFORMATION` | REGULATORY without implementation ask |
| `CLEAR_NAVIGATION_LOGIN` | NAVIGATIONAL / LOGIN_ACCOUNT_ACCESS |
| `FREE_DOWNLOAD_INTENT` | DOWNLOAD + FREE without commercial path |
| `INCOMPATIBLE_PRODUCT_ONLY_INTENT` | Product purchase outside campaign scope |
| `IRRELEVANT` | IRRELEVANT intent |
| `MALFORMED` | MALFORMED intent |
| `UNSUPPORTED_SERVICE` | Service not in catalog |
| `LANDING_MISMATCH` | Commercial intent incompatible with landing scope |

**Invariant:** REJECT always requires `reason_code`.

---

## ABSTAIN reason families

| reason_code family | When to use |
|--------------------|-------------|
| `INSUFFICIENT_EVIDENCE` | Signals too weak; UNKNOWN-like |
| `COMPETING_INTENTS` | Multiple intents without winner |
| `SHORT_AMBIGUOUS_PHRASE` | SHORT_HEAD_TERM |
| `PROVIDER_DIY_CONFLICT` | PROVIDER_VS_DIY unresolved |
| `PRODUCT_SERVICE_CONFLICT` | PRODUCT_VS_SERVICE unresolved |
| `SUPPORT_INFORMATION_CONFLICT` | SUPPORT_VS_INFORMATION unresolved |
| `RULE_MODEL_DISAGREEMENT` | Assessor disagreement |
| `LOW_CONFIDENCE` | Below threshold_profile |
| `PROTECTED_SIGNAL_CONFLICT` | Protected strata conflict |
| `SERVICE_OWNERSHIP_UNRESOLVED_AT_ELIGIBILITY_BOUNDARY` | Cannot assign service at this stage |

**Invariant:** ABSTAIN requires unresolved question or conflict.

---

## Examples (RU)

| Query | decision | reason_code |
|-------|----------|-------------|
| «заказать внедрение crm под ключ» | ACCEPT | EXPLICIT_PROVIDER_REQUEST |
| «курс 1с программирование» | REJECT | CLEAR_EDUCATION |
| «вакансия 1с москва» | REJECT | CLEAR_CAREER_SEEKER |
| «1с» | ABSTAIN | SHORT_AMBIGUOUS_PHRASE |
| «монтаж вентиляции» | ABSTAIN | PROVIDER_DIY_CONFLICT |

---

## Related documents

- [`ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](ORCA-PRIMARY-INTENT-TAXONOMY-v1.md)
- [`ORCA-AMBIGUITY-TAXONOMY-v1.md`](ORCA-AMBIGUITY-TAXONOMY-v1.md)
- [`ORCA-SEMANTIC-REVIEW-STATUS-v1.md`](ORCA-SEMANTIC-REVIEW-STATUS-v1.md)
