# CORVONERO — РСЯ budget and learning risk map v1.1

**Status:** PLANNING_RISK_MAP / NO_INVENTED_BUDGET_NUMBERS  
**Created:** 2026-08-19  
**Project:** CorvoNero / Корво Неро  

This map explains **why** v1’s LOCAL/REMOTE split must not be read as two independent auto-strategies by default. It does **not** set a live RSY budget.

Official learning/budget paraphrases: `CORVONERO-YANDEX-DIRECT-OFFICIAL-SOURCE-NOTES-v1.1.md`.  
Operator practice: `OPERATOR_INSIGHT / NOT_OFFICIAL_DOC_CONFIRMED`.

---

## Operator fill fields (required before import/generation)

| Field | Current value | Source | Notes |
|-------|---------------|--------|-------|
| Daily budget (RSY) | `[OPERATOR_TO_FILL]` | — | Direct currently emphasises **weekly** budgets in Help; keep daily as operator planning figure only. |
| Weekly budget (RSY) | `[OPERATOR_TO_FILL]` | — | If package is used, this is the **package** weekly budget covering all member campaigns. |
| Monthly budget (RSY) | `[OPERATOR_TO_FILL]` | — | Planning cap vs Search remainder. |
| Account balance / replenishment rhythm | `[OPERATOR_TO_FILL]` | Operator example 50 000 ₽ is **illustration only** | Empty balance / campaign stop degrades auto strategies (official Help). |
| Target CPA (RSY) | `[OPERATOR_TO_FILL]` | Do **not** copy Search CPA 4 516.67 ₽ | Search CPA is a different placement and n=6. |
| Acceptable test spend per weak direction | `[OPERATOR_TO_FILL]` | — | Доработка LOCAL, Интеграции LOCAL first; then other MEDIUM/TEST groups. |
| Minimum observation period | `[OPERATOR_TO_FILL]` | Official hint: 7–14 days; 1–2 weeks learning; change weekly budget ≤ every 2–3 weeks | Fill a CorvoNero period (e.g. 14 / 21 days). |
| Conversion goal to optimize for | `[OPERATOR_TO_FILL]` | Metrica goal name SAFE UNKNOWN | Must be a goal that can realistically accumulate volume. |
| Call tracking imported to Metrica/Direct | `[OPERATOR_TO_FILL]` | Phone leads ~3 are OPERATOR_REPORTED_APPROXIMATE | Not an official optimization signal until imported. |

Help sizing **formula** (not a CorvoNero number): Maximize conversions weekly budget **≥ 10 × conversion price**, and ≥10 conversions/week on the chosen goal (package = **sum** of member campaigns). Apply only after the operator fills CPA and goal.

---

## Risk register

| ID | Risk | Why it matters for CorvoNero now | Official vs operator | Mitigation |
|----|------|----------------------------------|----------------------|------------|
| R-01 | Too many independent campaigns | Search already has 10 campaigns. RSY v1 added 2 more as if they were extra learning pools. Search slice: 6 conversions / ~23 days — thin even **before** splitting RSY. | Operator insight + official 10 conv/week | Start with 1 campaign **or** 2 campaigns in **one package**. Do not launch 5 service campaigns on day one. |
| R-02 | Too many independent auto strategies | One campaign = one strategy. Two campaigns without a package = two learning pools. | Official (select-strategy; package Help) | Package LOCAL+REMOTE, or collapse to one campaign. |
| R-03 | Low conversion volume per campaign | Official guide ≥10 conversions/week **per strategy** (or per package sum). Current Search volume is below that at whole-Search level. RSY history: none. | Official | Fewer strategies; choose a frequent enough Metrica goal; consider pay-per-click Maximize conversions with weekly budget only until CPA is known (Help troubleshooting). |
| R-04 | Budget lower than combined campaign demand | Operator example: 50 000 ₽ balance vs several campaign budgets that sum higher. Help: insufficient funds / stop hurts algorithms; package weekly budget must cover **all** members. | Both | One RSY weekly budget (campaign or package). Confirm account weekly cap. Do not set two “full” conversion budgets that cannot both spend. |
| R-05 | Weak directions consume budget before winners scale | Доработка/Интеграции Search: little/no spend, 0 conversions. Operator rule: still **include**. Uncontrolled auto allocation may still spend on them. Package Help: weak campaigns are bid-down, not fully stopped. Groups cannot be assumed to have hard budget caps (SAFE UNKNOWN / cabinet). | Both | Keep on the map; HIGH/MEDIUM/TEST priority; group CPA adjustments; possible delayed **exposure** without deleting groups; operator test-spend cap. |
| R-06 | Search CPA copied blindly to RSY | Search CPA 4 516.67 ₽, n=6, 100% autotargeting, Search placement only. | Operator rule already in v1; restated | Separate RSY CPA field. If unknown, Help suggests budget-only Maximize conversions first. |
| R-07 | Conversion optimization without reliable goals | Exact Metrica goal names SAFE UNKNOWN. | Official (Metrica required) | Goal cleanup **before** launch. Do not generate import until OC-13 / OC-R07 closed. |
| R-08 | Unclear Metrica goals | Form vs call vs composite unknown. Help: pick a goal that can fire ≥10/week. | Official | Operator + Metrica audit. Prefer one primary goal for first RSY package/campaign. |
| R-09 | Phone calls outside Metrica not feeding optimization | ~3 approximate phone leads. Official path is call tracking / call goals. | Both | Do not use approximate phones as CPA. Confirm import. Optional click-to-call as weaker proxy (Help check-list). |
| R-10 | LOCAL and REMOTE mixed without geo/message clarity | LOCAL = Новосибирск / possible visit; REMOTE = Russia-wide, no visit promise. Mixing copy/images without group geo is a message risk, not a Help ban. | Operator / v1 architecture | If one campaign: **separate groups** (and ads) for LOCAL vs REMOTE, with group geo. If two campaigns: keep message isolation; still consider package for budget. |
| R-11 | Commander unlinks package | Help: strategy edit in Commander detaches the campaign. | Official | If packages are used, document a Commander SOP: do not edit strategy there; check weekly budget after any unlink. |
| R-12 | Packaging Search + RSY too early | 2023 news example mixed Search+RSY+retargeting; same article also reported better results with Search and RSY in **different** packages; current Help requires same **type**. | Official mixed signals | First evaluate an **RSY-only** package (LOCAL+REMOTE). Do not join live Search V2.6.2 until type compatibility is confirmed. |

---

## Mitigations — how they attach to structure

| Mitigation | Option A (1 campaign) | Option B (2 campaigns) | Option C (many + package) | Option D (hybrid) |
|------------|----------------------|------------------------|---------------------------|-------------------|
| Package strategy | Not needed for RSY-internal learning (already one pool) | **Evaluate / prefer** for LOCAL+REMOTE | Required for learning | Package the campaign family that exists |
| Fewer campaigns at launch | Yes | Only two | No — avoid at launch | Start A or B |
| Group-level service split | 10 groups | 5+5 | Campaigns instead of groups | Groups first, campaigns later for winners |
| Controlled testing priorities | HIGH/MEDIUM/TEST | Same | Harder | Same |
| Separate retargeting later | Yes | Yes | Yes | Yes |
| Manual caps / phased allocation | Operator process | Operator process | Operator process | Operator process |
| Goal cleanup before launch | Mandatory | Mandatory | Mandatory | Mandatory |
| Ignore approximate phones | Mandatory | Mandatory | Mandatory | Mandatory |
| Include all directions, manage exposure | Yes | Yes | Yes | Yes |

---

## Weak-direction budget-control logic (planning)

All five directions stay **included**. Weak/non-converting Search directions stay **included**.

Control order (later generation/launch, not this pack):

1. Architecture map includes all 10 groups.
2. Priority: HIGH (4) / MEDIUM (4) / TEST (2) from v1 group map — unchanged as planning ranks.
3. First-wave **exposure** may emphasise HIGH groups; TEST groups remain in the file.
4. If ЕПК group CPA/ДРР adjustments are available: lower TEST, protect HIGH.
5. Operator fills `acceptable test spend per weak direction`.
6. Do not create extra campaigns for TEST services at launch (that would add empty learning pools).

This is **not** equal first-wave budget. Inclusion ≠ equal spend.

---

## Search evidence reminder (not RSY proof)

| Slice | Spend | Conversions | Implication |
|-------|-------|-------------|-------------|
| Search official totals | 27 100 ₽ | 6 | Thin conversion history |
| LOCAL | 12 700 ₽ | 3 | Split already halves volume |
| REMOTE | 14 400 ₽ | 3 (all сопровождение) | REMOTE learning would be one-service-heavy if isolated |
| Phone outside Metrica | — | ~3 approx | Not strategy fuel |
| RSY | none | none | New learning from zero |

Do not treat these as RSY forecasts.
