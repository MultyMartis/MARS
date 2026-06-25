# ORCA Benchmark Intent Strata v1

**Strata set ID:** `orca-benchmark-intent-strata`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-intent-strata-v1.json`](orca-benchmark-intent-strata-v1.json)

---

## Purpose

Define **intent strata** for stratified benchmark sampling and evaluation reporting. Each stratum links to P0-B primary-intent taxonomy values where applicable. Stratum assignment is benchmark metadata (`benchmark.stratum_id`), not a replacement for per-phrase `primary_intent`.

---

## Strata catalog

| stratum_id | Taxonomy link | Sampling purpose | Expected eligibility mix | Risk | Min rep (B2) | Protected | Hard-negative candidate |
|------------|---------------|------------------|--------------------------|------|-------------:|-----------|------------------------|
| `INTENT_EXPLICIT_SERVICE_HIRE` | `INTENT_HIRE_PROVIDER`, `INTENT_REQUEST_SERVICE` | Test clear commercial hire signals | Mostly ACCEPT | Low over-reject | 80 | No | No |
| `INTENT_IMPLICIT_SERVICE_HIRE` | `INTENT_HIRE_PROVIDER` (implicit) | Test weak but valid provider intent | ACCEPT / ABSTAIN | Over-reject if too strict | 60 | No | No |
| `INTENT_QUOTE_PRICE_CONTACT` | `INTENT_REQUEST_QUOTE`, `INTENT_CONTACT_PROVIDER` | Price/quote/contact commercial path | Mostly ACCEPT | False reject on price-only | 50 | No | No |
| `INTENT_IMPLEMENTATION_CONFIGURATION` | `INTENT_IMPLEMENTATION`, `INTENT_CONFIGURATION` | Implementation/setup service demand | ACCEPT / ABSTAIN | Product vs service confusion | 50 | No | No |
| `INTENT_MODIFICATION_INTEGRATION` | `INTENT_INTEGRATION`, `INTENT_CUSTOMIZATION` | Integration/customization services | ACCEPT / ABSTAIN | Product module confusion | 50 | No | No |
| `INTENT_SUPPORT_RECOVERY` | `INTENT_SUPPORT`, `INTENT_RECOVERY` | Paid support/recovery vs DIY troubleshoot | ACCEPT / REJECT / ABSTAIN | Support vs information overlap | 40 | No | Yes |
| `INTENT_UNRESOLVED_PROBLEM` | `INTENT_DIAGNOSE_PROBLEM` | Problem signal without clear hire | ABSTAIN / REJECT | **Over-accept** risk | 60 | No | Yes |
| `INTENT_DIY_HOW_TO` | `INTENT_DIY`, `INTENT_HOW_TO` | DIY/self-help — protected | Mostly REJECT | **FPR** risk | 70 | **Yes** | **Yes** |
| `INTENT_INFORMATIONAL` | `INTENT_INFORMATIONAL` | General information without hire | REJECT / ABSTAIN | Topical relevance trap | 50 | No | Yes |
| `INTENT_EDUCATIONAL` | `INTENT_EDUCATION`, `INTENT_COURSE` | Courses/training — protected | REJECT | **FPR** risk | 60 | **Yes** | **Yes** |
| `INTENT_CAREER_SEEKER` | `INTENT_CAREER` | Job seeker — protected | REJECT | **FPR** risk | 60 | **Yes** | **Yes** |
| `INTENT_EMPLOYEE_HIRING` | `INTENT_HIRE_EMPLOYEE` | Employer hiring ≠ service demand | REJECT | **FPR** risk | 40 | **Yes** | **Yes** |
| `INTENT_REGULATORY` | `INTENT_REGULATORY` | Rules/compliance without implementation hire | REJECT / ABSTAIN | Regulatory overlap | 50 | **Yes** | Yes |
| `INTENT_NAVIGATIONAL` | `INTENT_NAVIGATIONAL` | Brand/site navigation — protected | REJECT | **FPR** risk | 40 | **Yes** | **Yes** |
| `INTENT_LOGIN_ACCOUNT` | `INTENT_ACCOUNT_ACCESS` | Login/cabinet — protected | REJECT | **FPR** risk | 30 | **Yes** | **Yes** |
| `INTENT_DOCUMENTATION` | `INTENT_DOCUMENTATION` | Docs/manuals — protected | REJECT | **FPR** risk | 40 | **Yes** | **Yes** |
| `INTENT_DOWNLOAD_FREE` | `INTENT_FREE_DOWNLOAD` | Free/download — protected | REJECT | **FPR** risk | 30 | **Yes** | **Yes** |
| `INTENT_PRODUCT_MODULE` | `INTENT_PRODUCT_PURCHASE` | Product/module without service | REJECT / ABSTAIN | Product/service conversion | 50 | No | Yes |
| `AMBIG_PRODUCT_VS_SERVICE` | ambiguity: `AMBIG_PRODUCT_SERVICE` | Product/service boundary | ABSTAIN heavy | **Over-accept** | 40 | No | **Yes** |
| `AMBIG_PROVIDER_VS_DIY` | ambiguity: `AMBIG_PROVIDER_DIY` | Provider vs DIY boundary | ABSTAIN heavy | **Over-accept / FPR** | 40 | Partial | **Yes** |
| `AMBIG_SUPPORT_VS_INFORMATION` | ambiguity: `AMBIG_SUPPORT_INFO` | Support vs information | ABSTAIN | Misclassification | 30 | No | **Yes** |
| `AMBIG_CAREER_VS_PROVIDER` | ambiguity: `AMBIG_CAREER_PROVIDER` | Career vs customer hire | REJECT / ABSTAIN | **FPR** | 30 | **Yes** | **Yes** |
| `INTENT_SHORT_HEAD` | short-head policy | Generic nouns, roles, modules | ABSTAIN / REJECT | **Over-confidence** | 50 | No | **Yes** |
| `INTENT_MALFORMED` | malformed handling | Noise, typos, fragments | REJECT / ABSTAIN | Rewriting risk | 20 | No | No |
| `INTENT_IRRELEVANT` | `INTENT_IRRELEVANT` | Off-topic | REJECT | Noise | 20 | No | No |
| `INTENT_UNKNOWN` | `INTENT_UNKNOWN` | Insufficient evidence | ABSTAIN | Premature ACCEPT | 20 | No | No |

**Note:** Taxonomy link values are illustrative mappings to P0-B `primary_intent` enums; exact crosswalk maintained in sampling plan.

---

## Protected strata

Protected strata require D3 FPR cap **≤ 0.01** per protected class at P0-G evaluation. Mandatory double annotation.

---

## B0 minimum representation

Each stratum: **≥ 2 phrases** where feasible in B0 (60–100 total); operator may waive thin strata with documented rationale.

---

## Related documents

- [`ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md`](ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md)
- [`../sampling/ORCA-UNIVERSAL-BENCHMARK-SAMPLING-PLAN-v1.md`](../sampling/ORCA-UNIVERSAL-BENCHMARK-SAMPLING-PLAN-v1.md)
- [`../../taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](../../taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md)
