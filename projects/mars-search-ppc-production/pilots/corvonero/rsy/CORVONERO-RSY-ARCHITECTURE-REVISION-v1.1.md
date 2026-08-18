# CORVONERO — РСЯ architecture revision v1.1

**Status:** AMENDMENT_PACK / NOT_AN_IMPORT_PACKAGE / NOT_LAUNCH_APPROVED  
**Created:** 2026-08-19  
**Project:** CorvoNero / Корво Неро  
**Programme:** mars-search-ppc-production  
**Amends:** RSY Architecture Pack v1 (checkpoint `e89c9593d9dd70a8e12c81bbed0d470386bc51c6`)  
**Does not replace:** v1 group IDs, landings, message angles, inclusion of all five directions  
**Search authority (unchanged):** V2.6 / deployable V2.6.2  

This file is **planning architecture revision only**. It is not an РСЯ import package, not final ads, not image prompts, and not launch approval.

v1 files are preserved. Read this pack together with:

- `CORVONERO-RSY-ARCHITECTURE-v1.md` (base objects)
- `CORVONERO-RSY-STRUCTURE-OPTIONS-v1.1.md`
- `CORVONERO-RSY-PORTFOLIO-STRATEGY-NOTES-v1.1.md`
- `CORVONERO-RSY-BUDGET-LEARNING-RISK-MAP-v1.1.md`
- `CORVONERO-RSY-RECOMMENDED-STRUCTURE-v1.1.md`
- `CORVONERO-YANDEX-DIRECT-OFFICIAL-SOURCE-NOTES-v1.1.md`
- `CORVONERO-RSY-OPEN-CONFIRMATIONS-REVISION-v1.1.md`
- `CORVONERO-RSY-NOT-FOR-GENERATION-YET-v1.1.md`

Storage package: `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-REVISION-PACK-2026-08-19\`  
XLSX workbooks live in Storage only (not in Git).

---

## 1. Why v1 needed a revision

v1 recommended `LOCAL_REMOTE_SPLIT`: two campaigns `CORVONERO-RSY-LOCAL` + `CORVONERO-RSY-REMOTE`, 10 groups, all five directions included. That **control split** remains useful.

v1 did **not** state that two campaigns must each run an independent conversion strategy and weekly budget. In practice that is how Direct objects behave **unless** they share a **пакетная стратегия** or are collapsed into one campaign.

Operator insight (`OPERATOR_INSIGHT / NOT_OFFICIAL_DOC_CONFIRMED`): if account balance is limited (example 50 000 ₽) and several independent campaigns each have their own budget/strategy while combined demand is higher, automated strategies under-learn. Semantically compatible campaigns on one site with close goals can share package logic so budget and learning stay coherent.

Official Help independently supports: package pooling of conversions; shared budget distributed by effectiveness; ~10 conversions/week (package = **sum**); weekly budget ≥ 10 × CPA for Maximize conversions; empty account balance hurting algorithms.

Search evidence used in v1 (unchanged read-only): 6 conversions / 27 100 ₽ / ~23 days with data; phone leads ~3 approximate, not in Metrica. That volume is already below the Help learning guide **before** splitting RSY into extra independent pools.

**v1.1 correction:** do not treat “separate campaigns” as “separate budgets/learning pools” by default.

---

## 2. Answers to the revision questions

### 2.1 One campaign, two, or several under a package?

**Conditional.**

- **Primary to evaluate:** two campaigns LOCAL/REMOTE (v1 objects) **plus** one package strategy if the account’s ЕПК/RSY type supports it.
- **Fallback if budget/package cannot support two pools:** one campaign, 10 groups (or 5 services with LOCAL/REMOTE variants).
- **Several campaigns by service:** expansion only, after volume, still preferably under one package.
- **Do not finalize** until budget and Direct package support are confirmed.

### 2.2 If we split LOCAL/REMOTE and/or service, how do we avoid starving strategies?

1. Prefer **one learning pool**: one campaign **or** two campaigns in **one package**.
2. Size the **package/campaign weekly budget** for all members (Help: budget must cover all).
3. Keep account funded; stops from empty balance hurt algorithms.
4. Choose a Metrica goal that can actually fire; do not optimize to approximate phones.
5. Do not copy Search CPA ≈ 4 517 ₽.
6. Do not add service-level campaigns on day one.
7. Keep weak directions on the map but control exposure (priority, later group adjustments, test-spend cap).

### 2.3 Can different services be advertised in one campaign via groups?

**Yes at Help level.** ЕПК supports many groups with different targeting; official category example uses group CPA/ДРР adjustments; more groups → more learning data; same-domain ads do not compete on billed price. CorvoNero: one site, five related 1C services, close goals. No official ban found. Cabinet/moderation remain TO_CONFIRM.

### 2.4 Recommended structure after constraints

See `CORVONERO-RSY-RECOMMENDED-STRUCTURE-v1.1.md`.

| Horizon | Structure |
|---------|-----------|
| Primary | Two RSY campaigns LOCAL/REMOTE, 5 groups each, **evaluate package** |
| Fallback (limited budget / no package) | One RSY campaign, 10 groups |
| Expansion | Split HIGH-volume services into extra campaigns **in the same package**; weak stay as groups |

All five directions included. Weak/non-converting included, with controlled exposure.

Images later, manual. No RSY import in this pack.

---

## 3. What stays from v1

| Item | v1.1 |
|------|------|
| 10 logical group codes | Unchanged |
| 5 landings, same URL LOCAL/REMOTE | Unchanged |
| Inclusion 5/5, EXCLUDE 0 | Unchanged |
| HIGH/MEDIUM/TEST ranks | Unchanged as planning ranks |
| Message angles conceptual only | Unchanged |
| Image prompts | Still not created |
| Search package / V2.6 | Unchanged |

---

## 4. Official research vs operator insight

| Kind | Use |
|------|-----|
| Official Help / Yandex Advertising news / Direct API | Authority for product rules (package, 10 conv/week, budget sizing, ЕПК levels) |
| Operator insight | Practice for limited balance; labelled, not passed off as Help |
| Search stats | Evidence of thin conversion volume; not RSY proof |

Full source table: `CORVONERO-YANDEX-DIRECT-OFFICIAL-SOURCE-NOTES-v1.1.md`.

---

## 5. Not created / not modified

| Item | Status |
|------|--------|
| RSY import XLSX | NOT CREATED |
| Final ads | NOT CREATED |
| Image prompts / images | NOT CREATED |
| Direct / Commander | NOT MODIFIED |
| Search V2.6.2 package | UNCHANGED |
| Final stats sources / stable sheet / legal DOCX / landing DOCX | UNCHANGED |
| Launch approval | NOT GRANTED |

---

## 6. Next stage (after operator)

1. Fill budget/CPA/goal fields; confirm package UI (OC-R01–R10).
2. Pick Scenario 1 or 2 explicitly.
3. Image production (manual) — still a separate stage.
4. Only then: generation/import charter.

Until then this remains architecture only.
