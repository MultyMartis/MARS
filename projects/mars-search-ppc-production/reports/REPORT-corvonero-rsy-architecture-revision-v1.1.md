# REPORT — Corvonero RSY architecture revision v1.1

**Date:** 2026-08-19  
**Programme:** mars-search-ppc-production  
**Project:** CorvoNero / Корво Неро  
**Operator mode:** human-operated Cursor charter  
**Git checkpoint this task:** **NO / NOT PERFORMED**

---

## Verdict

CORVONERO RSY ARCHITECTURE REVISION:
PASS

```
CORVONERO RSY ARCHITECTURE REVISION:
PASS — PORTFOLIO/PACKAGE STRATEGY AND BUDGET LEARNING LOGIC INTEGRATED; ALL DIRECTIONS REMAIN INCLUDED; NO RSY IMPORT OR IMAGE PROMPTS CREATED
```

---

## Environment

| Check | Result |
|-------|--------|
| Drive | `X:` |
| Volume | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| This task pull/reset/clean/stash/restore | **NOT RUN** |
| Stage / commit / push | **NOT PERFORMED** |

Foreign WIP preserved. No volume/branch STOP.

---

## Revision reason

v1 recommended two RSY campaigns (`LOCAL_REMOTE_SPLIT`) as the default. That split remains useful for geo and message control, but v1 did not say that two campaigns must each run an independent conversion strategy and weekly budget. Operator Direct practice: limited account balance (example 50 000 ₽) plus several independent auto-strategies can starve learning. Official Help independently documents пакетные стратегии (shared learning + budget distributed by effectiveness) and a ~10 conversions/week learning guide. v1.1 amends the architecture so campaign objects, package strategy, and groups are three distinct layers.

---

## Official Yandex research

Official sources used:

- https://yandex.ru/support/direct/ru/strategies/portfolio-strategy — Пакетная стратегия
- https://yandex.ru/adv/news/paketnie-strategii — новость Яндекс Рекламы (2023-03-23)
- https://yandex.ru/support/direct/ru/unified-performance-campaign/about — Единая перфоманс-кампания
- https://yandex.ru/support/direct/ru/unified-performance-campaign/create-campaign
- https://yandex.ru/support/direct/ru/unified-performance-campaign/create-group
- https://yandex.ru/support/direct/ru/strategies/select-strategy
- https://yandex.ru/support/direct/ru/strategies/average-cpa — Максимум конверсий
- https://yandex.ru/support/direct/ru/strategies/week-budget
- https://yandex.ru/support/direct/ru/troubleshooting/conversions
- https://yandex.ru/support/direct/ru/technologies-and-services/compete
- https://yandex.ru/support/direct/ru/statistics/metrika
- https://yandex.ru/support/direct/ru/strategies/priority-goals
- https://yandex.ru/support/direct/ru/efficiency/check-list
- https://yandex.ru/support/direct/ru/strategies/call-conversions
- https://yandex.ru/dev/direct/doc/ru/objects/strategy

Official support found for:

- Package/portfolio strategies on ЕПК (except messenger and app campaigns); same type only; up to 100 campaigns
- Package purpose: conversion pooling for learning; one budget across campaigns; distribution by effectiveness
- ≥10 conversions/week for package **in sum**; Maximize conversions ≥10/week (70 for apps); evaluate 7–14 days
- Weekly budget ≥ 10 × conversion price for Maximize conversions; min weekly 300 ₽; empty balance hurts algorithms
- Campaign vs group levels; many groups in one campaign; group CPA/ДРР adjustments; geo at group
- No Help ban found on several related services of one site via groups
- Same-domain ads do not compete on billed price
- Call goals only train strategies if tracked into Metrica/Direct

Still SAFE UNKNOWN:

- Whether **this** login currently shows packages for RSY-only ЕПК
- Live type of Search V2.6.2 campaigns (legacy vs ЕПК)
- Whether Search packages may legally join an RSY package (same-type rule)
- Numeric RSY budgets, CPA, replenishment
- Exact Metrica goal names and fire rate
- Whether phones are imported
- Commander-vs-web process for packages

Operator 50 000 ₽ example remains `OPERATOR_INSIGHT / NOT_OFFICIAL_DOC_CONFIRMED`.

---

## Revised structure recommendation

**Primary:** two RSY campaigns `CORVONERO-RSY-LOCAL` + `CORVONERO-RSY-REMOTE`, five service groups each (10 groups), **evaluate and prefer one пакетная стратегия** so LOCAL/REMOTE stay control objects without becoming two independent learning pools.

**Fallback for limited budget:** one RSY campaign with 10 groups (or five services with LOCAL/REMOTE geo/message variants) until conversion volume is stable or package UI is missing.

**Expansion if budget/conversions grow:** hybrid — split HIGH-volume working services into extra campaigns **under the same package**; keep weak/TEST directions as groups; retargeting later, separate confirmation.

Do not finalize until budget, strategy, and Direct package support are confirmed.

---

## Direction policy

All five directions included: **YES**

Weak/non-converting directions included: **YES**

Weak direction budget-control logic: stay on the map (EXCLUDE = 0); HIGH/MEDIUM/TEST ranks from v1; later group CPA adjustments if ЕПК allows; operator fills acceptable test spend; do not create extra campaigns for TEST services at launch. Inclusion ≠ equal first-wave budget.

---

## Package

**Storage:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-REVISION-PACK-2026-08-19\`

**Repo refs:** `projects/mars-search-ppc-production/pilots/corvonero/rsy/`

**Report:** `projects/mars-search-ppc-production/reports/REPORT-corvonero-rsy-architecture-revision-v1.1.md`

---

## Created

**Storage** (`X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-REVISION-PACK-2026-08-19\`):

- `01-CORVONERO-RSY-ARCHITECTURE-REVISION-v1.1.md`
- `01-CORVONERO-RSY-ARCHITECTURE-REVISION-v1.1.xlsx` (12 sheets)
- `02-CORVONERO-RSY-STRUCTURE-OPTIONS-v1.1.xlsx`
- `03-CORVONERO-RSY-PORTFOLIO-STRATEGY-NOTES-v1.1.md`
- `04-CORVONERO-RSY-BUDGET-LEARNING-RISK-MAP-v1.1.md`
- `05-CORVONERO-RSY-RECOMMENDED-STRUCTURE-v1.1.md`
- `06-CORVONERO-YANDEX-DIRECT-OFFICIAL-SOURCE-NOTES-v1.1.md`
- `07-CORVONERO-RSY-OPEN-CONFIRMATIONS-REVISION-v1.1.md`
- `08-CORVONERO-RSY-NOT-FOR-GENERATION-YET-v1.1.md`
- `CORVONERO-RSY-ARCHITECTURE-REVISION-MANIFEST-v1.1.json`
- `CORVONERO-RSY-ARCHITECTURE-REVISION-SHA256SUMS-v1.1.txt`

**Repo refs:**

- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-ARCHITECTURE-REVISION-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-ARCHITECTURE-REVISION-v1.1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-STRUCTURE-OPTIONS-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-PORTFOLIO-STRATEGY-NOTES-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-BUDGET-LEARNING-RISK-MAP-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-RECOMMENDED-STRUCTURE-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-YANDEX-DIRECT-OFFICIAL-SOURCE-NOTES-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-OPEN-CONFIRMATIONS-REVISION-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-NOT-FOR-GENERATION-YET-v1.1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/rsy/CORVONERO-RSY-ORKA-KNOWLEDGE-FOLLOWUP-v1.md`
- `projects/mars-search-ppc-production/reports/REPORT-corvonero-rsy-architecture-revision-v1.1.md`

XLSX not placed in Git. v1 RSY architecture files preserved.

## Not created

| Item | Status |
|------|--------|
| RSY import | NOT CREATED |
| Final ads | NOT CREATED |
| Image prompts | NOT CREATED |
| Images | NOT CREATED |
| Direct | NOT MODIFIED |
| Commander | NOT MODIFIED |

---

## Validation

| Check | Result |
|-------|--------|
| XLSX sheets | 12/12 |
| Structure options | A/B/C/D evaluated (B split into B1 independent vs B2 package) |
| Portfolio/package strategy | CONSIDERED |
| Budget learning risk map | CREATED |
| Open confirmations | UPDATED (OC-R01–R14 + remaining v1 items) |
| Not-for-generation guard | CREATED |
| ORKA follow-up note | CREATED (ingestion not executed) |
| Campaign package | UNCHANGED |
| Final stats source XLSX | UNCHANGED |
| Stable sheet | UNCHANGED |
| Legal DOCX | UNCHANGED |
| Landing DOCX | UNCHANGED |
| Cleanup | NOT EXECUTED |
| Git checkpoint | NOT PERFORMED |
| Foreign WIP | PRESERVED |
| v1 files | PRESERVED |

---

## Remaining open confirmations

Key blockers before generation/import: OC-R01 package UI; OC-R02 use package at launch; OC-R04 reduce campaign count if no package; OC-R06 RSY budget; OC-R07 conversion goal; OC-R08 call import; OC-R10 one vs two campaigns; OC-R12 import approval; OC-04 strategy; OC-13 Metrica; OC-10 images.

---

## Required final line

CORVONERO RSY ARCHITECTURE REVISION:
PASS — PORTFOLIO/PACKAGE STRATEGY AND BUDGET LEARNING LOGIC INTEGRATED; ALL DIRECTIONS REMAIN INCLUDED; NO RSY IMPORT OR IMAGE PROMPTS CREATED
