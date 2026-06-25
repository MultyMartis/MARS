# Strategic Risk Register — Корво Неро v1

**Stage:** ORCA Stage 1  
**Scale:** probability H/M/L · impact H/M/L · status blocking / non-blocking

---

| ID | Risk | P | I | Evidence | Mitigation direction | Owner | Status |
|----|------|---|---|----------|-------------------|-------|--------|
| R-01 | No PPC history — blind optimization | H | H | Handoff `safe_unknown`; intake | Start with narrow model; define Metrika goals before scale | Андрей + operator | **non-blocking** (test charter) |
| R-02 | CPL unknown | H | H | No conversion data | Bounded test; qualify leads; no CPL targets in Stage 1 | Андрей | **non-blocking** |
| R-03 | Wide service portfolio vs small budget | H | H | 17 intake services; 100k budget | Select Model A/B/C; max 3–4 directions | Operator | **blocking** for architecture |
| R-04 | Budget 100k insufficient for multi-lane learning | M | H | Budget boundary notes | Sequential tests; defer specialist lanes | Operator | **non-blocking** if model narrow |
| R-05 | Single universal Tilda page | H | M | `website-corvonero-intelligence.json` | Minor edits (A/C) or dedicated page (B) | Роман | **blocking** for marking/integration lanes |
| R-06 | Weak proof package | H | H | No cases, certs, reviews | Proof readiness plan; forbid false claims | Роман / operator | **blocking** for scale; **non-blocking** for limited test |
| R-07 | Informational noise in marking | H | M | 539 regulatory_noise; r1q07 CAPTCHA | Isolate marking; heavy semantic clean (future) | Андрей | **non-blocking** if marking deferred |
| R-08 | Vacancy noise on programmer/troubleshooting | M | M | r1q01, r1q10 vacancy flags | Strategic exclude employment class | Андрей | **non-blocking** with cleaning |
| R-09 | Franchise competition in SERP | M | M | r1q01–r1q04 franchise/local mix | Differentiate on task/specificity not «we are 1C» | Андрей / Роман | **non-blocking** |
| R-10 | Integration queries — web-studio intent | M | H | r1q05 web studios; YAL in shortlist | Dedicated landing + isolation; defer Bitrix | Operator | **blocking** for integration launch |
| R-11 | ТС ПИОТ niche + no R1 | M | M | r1q09 not captured; defer verdict | Defer direction | Operator | **blocking** for TS PIOT spend |
| R-12 | Partner 1C status unconfirmed | M | M | SAFE UNKNOWN intake | Do not claim partner in ads | Роман | **blocking** for partner claims only |
| R-13 | VAT unknown | M | L | SAFE UNKNOWN | Clarify before B2B invoicing messaging | Роман | **non-blocking** for test |
| R-14 | Call tracking status unknown | M | M | Not in evidence | Implement if phone-led; else Metrika form goals | Андрей | **non-blocking** but affects attribution |
| R-15 | Metrika goals unknown | H | M | Not in evidence | Document goals before launch prep | Андрей / operator | **blocking** for optimization |
| R-16 | CRM / lead capture unknown | M | H | Form exists; routing unknown | Map lead path + SLA | Роман / Евгения | **blocking** for Model C |
| R-17 | Lead response SLA unknown | M | H | Not on site | Define before urgent/troubleshooting spend | Роман | **blocking** for Model C |
| R-18 | Min order not on site | M | M | intake vs site crosswalk | Operator decision on publication | Роман | **non-blocking** but affects lead quality |
| R-19 | Nationwide Wordstat misread as regional | M | H | Forbidden assumption in handoff | Train semantic-only use; Pass B not required | Андрей | **non-blocking** if discipline held |
| R-20 | CAPTCHA gaps r1q06/07 composition | M | M | Grade C only | Do not infer; defer or isolated test with caution | ORCA | **non-blocking** if directions deferred |
| R-21 | Price in ads not approved | M | M | intake note | Operator decision sheet #2 | Operator | **blocking** for price-forward ads |
| R-22 | Remote vs NSO geo targeting | M | M | intake remote; site office | Operator decision #14 | Operator | **non-blocking** for NSO-first |

---

## Risk summary

| Blocking count (launch prep) | Themes |
|------------------------------|--------|
| **Strategic** | Model selection (R-03), landing scope (R-05, R-10), Metrika (R-15), lead path (R-16, R-17) |
| **Claims** | Partner status (R-12), price in ads (R-21) |

*Mitigation directions are planned actions — not executed work.*
