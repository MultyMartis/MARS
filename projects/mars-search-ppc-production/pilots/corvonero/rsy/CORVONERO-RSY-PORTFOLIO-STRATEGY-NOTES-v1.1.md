# CORVONERO — РСЯ portfolio / package strategy notes v1.1

**Status:** ARCHITECTURE_NOTES / NOT_A_CABINET_SETTING  
**Created:** 2026-08-19  
**Project:** CorvoNero / Корво Неро  

Official name in Yandex Direct Help: **пакетная стратегия** (English Help: portfolio strategy). This file separates:

1. **Official Help** — what Yandex documents.
2. **Operator insight** — Direct-management practice for limited balance.
3. **CorvoNero application** — what to confirm before RSY launch.

Do not treat these notes as a live Direct configuration.

---

## 1. Three different layers (do not collapse them)

| Layer | What it is | What it is not |
|-------|------------|----------------|
| **Campaign split** | Objects for geo/message/reporting/control (LOCAL vs REMOTE, later service split) | Not automatically a separate learning pool **if** campaigns share a package |
| **Package / portfolio strategy** | One strategy-indicator set + one shared budget logic across same-type campaigns; conversions train the package | Not a replacement for groups; not proven available in this login until cabinet check |
| **Groups** | Service / geo / audience / creative containers **inside** one campaign; share that campaign’s strategy | Not independent weekly budgets |

v1 recommended `LOCAL_REMOTE_SPLIT` without this distinction. v1.1 keeps the LOCAL/REMOTE **control** idea and **rejects** the silent assumption that two campaigns must run two independent conversion budgets.

---

## 2. Official Help (paraphrase)

Sources: `CORVONERO-YANDEX-DIRECT-OFFICIAL-SOURCE-NOTES-v1.1.md` (S1–S8).

- Package unites **same-type** campaigns (Help: ЕПК, except messenger and app campaigns).
- Purpose: more conversions for **learning**; **one budget** across campaigns with different tasks; budget **distributed by effectiveness**.
- Learning guide: **≥10 conversions per week in sum** across the package.
- Campaign settings: the stated weekly budget must cover **all** campaigns in the package.
- Up to 100 campaigns per package.
- Weak campaign in a package: bids decrease with poor efficiency; algorithm does **not** fully stop it.
- Commander: editing the strategy on a packaged campaign **unlinks** it; the weekly budget then applies to that campaign alone.

---

## 3. Operator insight

**SOURCE_STATUS:** `OPERATOR_INSIGHT / NOT_OFFICIAL_DOC_CONFIRMED`

Example given: account balance ~50 000 ₽ while several independent campaigns each carry their own strategy/budget and combined demand is higher. Automated strategies then under-learn and under-deliver.

For CorvoNero Search, LOCAL and REMOTE already work as two **logical package containers**. RSY may still use two campaigns, but they should be evaluated for **shared package logic** or collapsed to one campaign until conversion volume is stable.

---

## 4. How this maps to CorvoNero RSY

Search today (unchanged, not modified): 10 Search campaigns / LOCAL + REMOTE families / 5 services.

RSY planning (v1.1):

| Question | v1.1 note |
|----------|-----------|
| Must RSY copy 10 Search campaigns? | **No.** v1 already collapsed 71 Search groups → 10 RSY groups. |
| Must RSY be two independent conversion strategies? | **No.** Two campaigns are a **control** choice, not a budget-pool mandate. |
| Can five services live in one campaign via groups? | **Yes, officially supported** at Help level (many groups, category example, group CPA adjustments). Same site (`lk.corvonero.ru`). |
| Should RSY join the existing Search packages? | **TO_CONFIRM.** Help: same **type** only. Mixing Search-only and RSY-only may or may not be allowed depending on current campaign types. Do not assume. |
| Should cold RSY share a package with retargeting? | **Later.** Prefer stable cold RSY first. 2023 news used mixed retargeting as an *example*, not a CorvoNero rule. |

---

## 5. Decision tree (planning, not launch)

```
Budget and conversion volume limited?
├─ YES, and two independent learning pools are unrealistic
│   ├─ Prefer: ONE RSY campaign, 10 groups (or 5 services × LOCAL/REMOTE message/geo)
│   └─ Or: TWO campaigns LOCAL/REMOTE bound to ONE package (if cabinet supports ЕПК package for RSY-only)
└─ NO, budget can buy ~10 conversions/week per independent strategy
    └─ TWO campaigns may run separate strategies — still optional to package them for shared budget

Need more service reporting later, after volume exists?
└─ Split HIGH-volume services into extra campaigns under the SAME package (Option C as expansion, not day-one)
```

Official 10 conversions/week is a **Help guideline**, not a CorvoNero KPI. Search evidence in the last processed slice was **6 conversions in ~23 days** — below that guideline at account Search level. RSY starts from zero Networks history.

---

## 6. Package membership candidates (if used)

**Candidate set A (preferred to evaluate first):**

- `CORVONERO-RSY-LOCAL`
- `CORVONERO-RSY-REMOTE`

Shared: one site, close B2B 1C goals, complementary geo/offer. Different: geography and visit promise.

**Not in the first RSY package by default:**

- Live Search campaigns (type compatibility TO_CONFIRM; also different placement learning).
- Future retargeting campaign (separate confirmation OC-15 / OC-R11).
- Weak-direction “test” campaigns (do not create extra campaigns for TEST groups).

---

## 7. What must be confirmed in Direct

1. Package strategies visible for the chosen RSY campaign type.
2. Both RSY campaigns would be the same type (ЕПК, Networks placement).
3. Operator accepts one shared weekly budget covering both LOCAL and REMOTE.
4. Conversion goal used by the package is a real Metrica goal, not approximate phone counts.
5. If Commander will be used: operators know that strategy edits unlink the package.

Until those are confirmed, the architecture remains **conditional**: Scenario 1 (two campaigns + package evaluation) or Scenario 2 (one campaign).
