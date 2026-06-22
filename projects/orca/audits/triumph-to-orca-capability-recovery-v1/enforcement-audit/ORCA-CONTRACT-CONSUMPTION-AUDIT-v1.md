# ORCA Contract Consumption Audit v1

**Machine-readable:** [`orca-contract-consumption-audit-v1.json`](orca-contract-consumption-audit-v1.json)

| Contract / law | Corvonero clean-room read? | Documentation only? | Validator check? | Could violate and proceed? | Violation blocking? | Compliance assumed? | Enforcement class |
|----------------|---------------------------|---------------------|------------------|---------------------------|---------------------|---------------------|-------------------|
| ORCA-CAMPAIGN-PRODUCTION-CONTRACT v1 | **No** — not imported by pipeline | Listed AUTH-03 in manifest | Only if `validate-campaign-production-contract.mjs` run separately | **Yes** — 1892 accepts | N/A at admission | **Yes** — manifest implies authority | **NOT CONSUMED** |
| orca-campaign-production-invariants | **No** at semantic stage | Yes | Contract validator tests | Yes | Export-only if validator run | Manual | **NOT CONSUMED** |
| triumph-derived-orca-laws-v1 (15 laws) | **No** | AUTH-04 reference | No | Yes | No | Documentation | **DOCUMENTATION ONLY** |
| ORCA-LAW-01 scope lock | Partial — scope file exists | Yes | INV-SCOPE if validator run | **Yes** — eligibility ignored scope intent | Soft | Assumed from intake | **MANUAL EXPECTATION** |
| ORCA-LAW-02 protected seeds | **No** in clean-room | v7 recovery only | INV-SEED in contract tool | Yes | No | No seed registry in v2 | **NOT CONSUMED** |
| ORCA-LAW-03 one intent per group | **No** — groups not pre-frozen | Triumph SE-01 | Triumph validation-cli only | Yes | No | No | **NOT CONSUMED** |
| ORCA-LAW-06 no informational filler | Partial — regex excludes some | Yes | Regex only | **Yes** — many info/commercial blur accepted | No | Weak regex assumed sufficient | **SOFT WARNING** |
| ORCA-LAW-08 ownership before negatives | **No** | Yes | No | **Yes** — negatives after bulk accept | No | No | **NOT CONSUMED** |
| ORCA-LAW-13 classifier advisory | **Violated** — script is authority | Contract text | No | Yes | No | No | **NOT CONSUMED** |
| ORCA-LAW-15 technical ≠ commercial | **Violated** — gate failed after run | Yes | semantic-core-gate post-hoc | Stopped export only | Informational at end | No | **SOFT WARNING** |
| P0-A SI authority model | **No** | Approved ADR | No | Yes | No | Future | **DOCUMENTATION ONLY** |
| P0-B semantic record schema | **No** | Approved schema | No | Yes | No | No | **DOCUMENTATION ONLY** |
| P0-C annotation guideline | **No** | Approved C1–C7 | No | **Yes** — career/edu/DIY would be REJECT | No | Assumed future | **DOCUMENTATION ONLY** |
| P0-D benchmark charter | **No** | PROPOSED | No | N/A | N/A | N/A | **NOT CONSUMED** |
| Triumph semantic-validation SE-* | **No** | Triumph path only | validation-cli | N/A for Corvonero | N/A | N/A | **NOT CONSUMED** |
| approval-gates-contract-v0 | Partial — D7 blocks campaign | Yes | PROJECT.md gates | Export blocked | **HARD BLOCK** at production | Operator decision | **HARD BLOCK** (production only) |
| orca-production-contract-integration-plan | **No** — plan not executed | Yes | N/A | Yes | No | Known gap | **DOCUMENTATION ONLY** |

## Summary

**Central finding:** Authority artifacts were **registered** in clean-room manifest but **semantic pipeline did not load them**. Validators checked **structure** (integrity validation) not **P0-C semantics**. Operator review workbook came **after** automated bulk admission — too late.
