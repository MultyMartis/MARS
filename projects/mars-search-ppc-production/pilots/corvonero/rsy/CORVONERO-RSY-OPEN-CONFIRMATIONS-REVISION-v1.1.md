# CORVONERO — РСЯ open confirmations revision v1.1

**Status:** OPEN / ARCHITECTURE_NOT_LAUNCH_APPROVED  
**Created:** 2026-08-19  
**Replaces decisioning in:** `CORVONERO-RSY-OPEN-CONFIRMATIONS-v1.md` (v1 file preserved; do not treat v1 OC-01 as the last word)

Known planning decision (not launch):

> All Search directions, including weak/disabled, must be included in РСЯ **planning**.

v1.1 adds: separate campaigns are **not** automatically separate budgets/learning pools.

---

## New confirmations (revision)

| ID | Topic | Current mark | Notes |
|----|-------|--------------|-------|
| OC-R01 | Is пакетная стратегия available for the selected RSY campaign type in this Direct account? | TO_CONFIRM / CABINET | Help: ЕПК except messenger/app. This login not checked. |
| OC-R02 | Should RSY use a package from first launch? | RECOMMENDED_TO_EVALUATE / OPERATOR_TO_CONFIRM | Preferred if Scenario 1 (two campaigns) is chosen. |
| OC-R03 | If yes, which campaigns join the same package? | CANDIDATE: RSY-LOCAL + RSY-REMOTE / OPERATOR_TO_CONFIRM | Do not assume Search campaigns join. Same **type** only. |
| OC-R04 | If no package, should we reduce campaign count? | RECOMMENDED_YES_IF_BUDGET_LIMITED / OPERATOR_TO_CONFIRM | Fallback: one RSY campaign, 10 groups. |
| OC-R05 | Account balance and replenishment rhythm | TO_CONFIRM | Operator illustration 50 000 ₽ is not a filled value. Empty balance hurts auto strategies (Help). |
| OC-R06 | Daily / weekly / monthly budget safely allocated to RSY | TO_CONFIRM | Fill fields in the budget risk map. Package weekly budget must cover all members. |
| OC-R07 | Conversion goal reliable enough for strategy learning | SAFE UNKNOWN / TO_CONFIRM | Help: prefer a goal that can fire ≥10/week. Exact names not in Search exports. |
| OC-R08 | Are phone calls tracked and imported into Metrica/Direct? | TO_CONFIRM | ~3 phones are OPERATOR_REPORTED_APPROXIMATE. Not an optimization signal until imported. |
| OC-R09 | Weak directions: included at launch with controlled exposure, or delayed but prepared? | ARCHITECTURE_INCLUDE_ALL / EXPOSURE_TO_CONFIRM | Map keeps all 10 groups. Phased **spend** is allowed; dropping from the map is not. |
| OC-R10 | LOCAL and REMOTE: independent campaigns or groups inside one campaign? | PRIMARY_EVALUATE_TWO_CAMPAIGNS_PLUS_PACKAGE / FALLBACK_ONE_CAMPAIGN / OPERATOR_TO_CONFIRM | See recommended structure v1.1. |
| OC-R11 | Should retargeting be separate from cold RSY? | TO_CONFIRM | Suggestion: separate later; do not mix into first cold package by default. |
| OC-R12 | Final Direct import approval | NOT_GRANTED | No import package exists. |
| OC-R13 | Final launch approval | NOT_GRANTED | Same as v1 OC-16. |
| OC-R14 | If Commander is used for RSY, accept unlink risk of package strategy edits | TO_CONFIRM | Official Help warning. |

---

## Previous confirmations that remain relevant

| ID | Topic | Current mark | Notes |
|----|-------|--------------|-------|
| OC-01 | Final campaign structure one vs LOCAL/REMOTE | SUPERSEDED_BY_OC-R10 / v1.1 CONDITIONAL | v1 recommended split as default; v1.1 makes it conditional on package/budget. |
| OC-02 | Daily budget | TO_CONFIRM | Keep; add weekly (OC-R06). |
| OC-03 | Monthly budget | TO_CONFIRM | Keep. |
| OC-04 | Bidding strategy | TO_CONFIRM | Now also: package vs ordinary; Maximize conversions vs budget-only start; do not copy Search CPA. |
| OC-05 | Use all five landings in first launch | ARCHITECTURE_YES / LAUNCH_TO_CONFIRM | Keep. |
| OC-06 | LOCAL and REMOTE same landing URLs | RECOMMENDED_SAME_URL / OPERATOR_TO_CONFIRM | Keep. |
| OC-07 | Exact geography LOCAL | TO_CONFIRM | Keep. |
| OC-08 | Exact geography REMOTE | TO_CONFIRM | Keep. Whether to exclude Novosibirsk from REMOTE: TO_CONFIRM. |
| OC-09 | First launch: all weak directions vs phased | ARCHITECTURE_INCLUDE_ALL / LAUNCH_PHASE_TO_CONFIRM | Aligned with OC-R09. |
| OC-10 | Image style and production | TO_CONFIRM | `IMAGE_PROMPT_NOT_CREATED`. |
| OC-11 | Brand restrictions on creatives | TO_CONFIRM | Keep. |
| OC-12 | Legal / disclaimer on ads | TO_CONFIRM | Legal DOCX review still not completed in this programme slice. |
| OC-13 | Metrica goals / audiences | SAFE UNKNOWN / TO_CONFIRM | Tightened by OC-R07. |
| OC-14 | Retargeting audience availability | SAFE UNKNOWN / TO_CONFIRM | Keep. |
| OC-15 | Separate remarketing from cold RSY | TO_CONFIRM | See OC-R11. |
| OC-16 | Final launch approval | NOT_GRANTED | Duplicate of OC-R13; keep both for continuity. |
| OC-17 | Price/offer claims in RSY copy | TO_CONFIRM | Claims register still requires confirmation. |
| OC-18 | Whether disabled live Search groups still exist | SAFE UNKNOWN | No current Direct snapshot. |

---

## Already decided for planning (not launch)

| Topic | Decision |
|-------|----------|
| Include weak Search directions in the architecture | YES |
| Include disabled Search groups as candidates inside direction×geo | YES |
| Exclude a direction because Search did not convert | NO |
| Treat two RSY campaigns as two independent strategies by default | **NO** (v1.1 correction) |
| Generate import XLSX now | NO |
| Write final ads / image prompts now | NO |
| Modify Direct / Commander / V2.6.2 | NO |

---

## Key confirmations blocking generation/import

OC-R01, OC-R02, OC-R04, OC-R06, OC-R07, OC-R10, OC-R12, OC-04, OC-13, OC-10.
