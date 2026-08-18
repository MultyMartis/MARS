# CORVONERO — РСЯ recommended structure v1.1

**Status:** REVISED_RECOMMENDATION / CONDITIONAL_ON_BUDGET_AND_DIRECT_SUPPORT / NOT_LAUNCH_APPROVED  
**Created:** 2026-08-19  
**Supersedes for decisioning:** v1 `LOCAL_REMOTE_SPLIT` as an **independent-strategy** default  
**Does not delete:** v1 group map, landings, message angles, inclusion of all five directions  

This is architecture revision only. Final choice still depends on budget, strategy, package support for the selected campaign type, Metrica goals/audiences, and operator approval.

---

## 1. Primary recommended architecture

**Code:** `TWO_RSY_CAMPAIGNS_LOCAL_REMOTE__EVALUATE_PACKAGE`  
**Task Scenario 1.**

| Item | Value |
|------|--------|
| Campaigns | `CORVONERO-RSY-LOCAL` + `CORVONERO-RSY-REMOTE` |
| Groups | 5 service groups in each = **10** logical groups (same codes as v1) |
| Directions | **5/5 included** |
| Weak/non-converting | **Included**, controlled (not equal spend) |
| Strategy layer | **Evaluate first:** one **пакетная стратегия** covering both RSY campaigns (Maximize conversions or budget-only Maximize conversions once the goal is confirmed) |
| If package is available and bound | LOCAL/REMOTE stay separate for geo/message/reporting; **learning and weekly budget are shared** |
| If package is not available | Do **not** silently run B1 (two independent conversion pools). Switch to fallback Scenario 2 unless the operator confirms each campaign can learn on its own |

This keeps v1’s useful LOCAL/REMOTE **control split** and removes v1’s unstated budget-pool split.

### Why not “always one campaign” as primary

- Search V2.6 already trained the client on LOCAL vs REMOTE as the main offer split.
- Visit vs remote must not blur in creatives.
- Group geo can implement the same split inside one campaign, but two named campaigns remain clearer **if** they share a package.

### Why not “always two independent strategies”

- Official Help: conversion strategies want ~10 conversions/week; package counts them **in sum**.
- Search evidence: 6 conversions in ~23 days; RSY has zero history.
- Operator insight: limited balance vs several independent budgets.
- Official Help: package budget is distributed by effectiveness; weekly budget must cover all members.

---

## 2. Fallback if budget is very small

**Code:** `ONE_RSY_CAMPAIGN_TEN_GROUPS`  
**Task Scenario 2.**

Use **one** RSY campaign with:

- **Preferred mapping:** 10 groups (5 services × LOCAL/REMOTE), same group codes as v1, geo and ads isolated per group; **or**
- **Compact mapping:** 5 service groups, LOCAL/REMOTE as geo + message variants (only if creatives cannot be confused).

Shared strategy and budget. Strongest consolidation. Use this when:

- package UI is missing for the chosen type, **or**
- account balance / RSY weekly budget cannot support two realistic learning pools, **or**
- Metrica goals are too rare to split.

Do not drop weak directions in the fallback. Keep TEST groups on the map with controlled exposure.

---

## 3. Expansion if budget and conversions grow

**Code:** `HYBRID_SPLIT_WINNERS_UNDER_PACKAGE`  
**Option D.**

After the primary or fallback is stable (operator observation period filled; Help hint 7–14 days / 1–2 weeks, not a promise):

1. Keep all five directions in the system.
2. Split **HIGH-volume working** services (Search signal points to сопровождение first) into their own campaigns **inside the same RSY package**.
3. Leave weak/TEST directions as groups in the parent campaign(s).
4. Consider a **separate retargeting** campaign later (not mixed into cold RSY on day one unless confirmed).
5. Still do not copy Search CPA as an RSY bid.

Option C (many service campaigns) is this expansion, **not** the launch shape.

---

## 4. Direction policy (unchanged inclusion, new control language)

| Direction | LOCAL | REMOTE | Included | Planning priority (from v1) |
|-----------|-------|--------|----------|-----------------------------|
| Программист 1С | YES | YES | YES | HIGH LOCAL / MEDIUM REMOTE |
| Сопровождение 1С | YES | YES | YES | HIGH / HIGH |
| Доработка / разработка 1С | YES | YES | YES | TEST / MEDIUM |
| Интеграции 1С | YES | YES | YES | TEST / MEDIUM |
| Маркировка / Честный знак | YES | YES | YES | HIGH LOCAL / MEDIUM REMOTE |

**All five directions included:** YES  
**Weak/non-converting included:** YES  
**EXCLUDE count:** 0  

**Weak-direction control:** inclusion in the architecture ≠ equal budget. Use HIGH/MEDIUM/TEST ranks, later group CPA adjustments if ЕПК allows, and operator `acceptable test spend per weak direction`. Do not spawn extra campaigns for TEST services at launch.

---

## 5. Campaign vs package vs groups

| Need | Use |
|------|-----|
| Geo / visit-promise / creative isolation | Campaigns (LOCAL/REMOTE) **or** groups with geo + distinct ads |
| Service landing / message / image | **Groups** (10 logical groups) |
| Shared learning + shared weekly budget across LOCAL and REMOTE | **Package strategy** (if same type and UI available) |
| Per-service campaign reporting | Later expansion campaigns under the **same package** |

---

## 6. Logical groups (unchanged IDs)

LOCAL: `01-LOCAL-PROGRAMMIST-1S` … `05-LOCAL-MARKIROVKA-CHESTNY-ZNAK`  
REMOTE: `01-REMOTE-PROGRAMMIST-1S` … `05-REMOTE-MARKIROVKA-CHESTNY-ZNAK`

Landings LP-01…LP-05 unchanged. Image status remains `IMAGE_PROMPT_NOT_CREATED`.

---

## 7. What is still not decided

- Numeric daily/weekly/monthly RSY budget  
- Target CPA  
- Package yes/no for this login  
- Conversion goal name  
- One campaign vs two (final operator pick after budget + UI)  
- Import and launch  

Until those are closed, v1.1 is a **conditional** recommendation, not a Direct build sheet.
