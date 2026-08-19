# CORVONERO — РСЯ Import Candidate v0.2

**Status:** IMPORT_CANDIDATE / NOT_READY_TO_UPLOAD / NOT_LAUNCH_APPROVED  
**Created:** 2026-08-19T04:05:00+07:00  
**Project:** CorvoNero / Корво Неро  
**Programme:** mars-search-ppc-production  
**Search authority (unchanged):** V2.6 / deployable V2.6.2  

| Source pack | Checkpoint | This task |
|-------------|------------|-----------|
| RSY Architecture Pack v1 | `e89c9593d9dd70a8e12c81bbed0d470386bc51c6` | UNCHANGED / read-only |
| RSY Architecture Revision v1.1 | `70db414e542976f029579e61daaea1848086931d` | UNCHANGED / read-only |
| RSY Generation Draft Pack v0.1 | `fe32a30b1bbd8d707925cabb054f75f243044834` | UNCHANGED / read-only |

This pack converts Generation Draft v0.1 into a **one-campaign import candidate** for operator review.

It is **not** a final import package. It is **not** launch-ready. Do **not** upload to Yandex Direct.

| Guard | Value |
|-------|--------|
| IMPORT_CANDIDATE | **YES** (operator review) |
| UPLOAD_READY | **NO** |
| Launch | NOT GRANTED |
| Final Direct ads | NOT FINAL |
| Image prompts | NOT CREATED |
| Images | NOT CREATED |
| Direct / Commander | NOT MODIFIED |
| Search package V2.6.2 | UNCHANGED |
| Direct-like Commander XLSX | **NOT CREATED** — RSY/ЕПК import format not verified |

---

## 1. Operator decisions applied

| ID | Topic | Value | Status | Notes |
| --- | --- | --- | --- | --- |
| OD-01 | Structure | one-campaign fallback | APPROVED | Do not launch two independent RSY campaigns. |
| OD-02 | Campaign name | CORVONERO-RSY | APPROVED | Single learning/budget pool. |
| OD-03 | Groups inside campaign | LOCAL and REMOTE groups / messages | APPROVED | 10 groups, isolation by group. |
| OD-04 | Directions | all five included | APPROVED | Weak/non-converting/disabled Search directions included. |
| OD-05 | Budget | 50 000 ₽ | APPROVED_AS_WORKING_INPUT | Campaign-level. Exact Direct period field CHECK_REQUIRED. |
| OD-06 | Strategy intent | payment for leads / conversions | APPROVED_AS_INTENT | Exact Direct UI field names CHECK_REQUIRED. |
| OD-07 | Metrica goals available | form; calls | OPERATOR_CONFIRMED | Exact names/IDs CHECK_REQUIRED. |
| OD-08 | Portfolio/package at start | not relied on for v0.2 start | APPROVED | One campaign instead of package. |
| OD-09 | Status of this pack | approved for RSY import-candidate preparation | APPROVED | Not import/launch. |
| OD-10 | Final Direct import | NOT GRANTED | NOT_GRANTED | Do not upload. |
| OD-11 | Launch | NOT GRANTED | NOT_GRANTED | Do not launch. |
| OD-12 | Image generation / prompts | NOT GRANTED | NOT_GRANTED | Requirements only. |
| OD-13 | Direct / Commander changes | NOT GRANTED | NOT_GRANTED | This task does not touch cabinets. |

Strategy interpretation:

- Do not create two independent RSY campaigns at launch.
- Do not rely on portfolio/package strategy for v0.2 start.
- Use one campaign so budget and conversion learning are not fragmented.
- Keep LOCAL and REMOTE differences inside groups, copy, URLs/UTM, audience logic and geo notes.
- Budget 50 000 ₽ is campaign-level working budget. Exact Direct period field remains **CHECK_REQUIRED**.
- Strategy intent is lead/conversion payment. Exact Direct UI names remain **CHECK_REQUIRED**.
- Metrica goals **form** and **calls** are operator-confirmed as available. Exact names/IDs remain **CHECK_REQUIRED**.

---

## 2. Candidate structure

**Campaigns:** 1  
**Campaign name:** `CORVONERO-RSY`  
**Groups:** 10  
**Directions:** 5/5  
**LOCAL represented:** YES  
**REMOTE represented:** YES  
**Weak/non-converting included:** YES  
**EXCLUDE:** 0

All five directions included, including weak/non-converting/disabled Search directions. Priority controls review/budget attention only. No group EXCLUDED.

| group_code | campaign | direction | mode | priority | inclusion | status |
| --- | --- | --- | --- | --- | --- | --- |
| 01-LOCAL-PROGRAMMIST-1S | CORVONERO-RSY | Программист 1С | LOCAL | HIGH | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 02-LOCAL-SOPROVOZHDENIE-1S | CORVONERO-RSY | Сопровождение 1С / техподдержка / ошибки 1С | LOCAL | HIGH | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 03-LOCAL-DORABOTKA-1S | CORVONERO-RSY | Доработка / разработка 1С | LOCAL | TEST | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 04-LOCAL-INTEGRACII-1S | CORVONERO-RSY | Интеграции 1С | LOCAL | TEST | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 05-LOCAL-MARKIROVKA-CHESTNY-ZNAK | CORVONERO-RSY | Маркировка / Честный знак | LOCAL | HIGH | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 01-REMOTE-PROGRAMMIST-1S | CORVONERO-RSY | Программист 1С | REMOTE | MEDIUM | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 02-REMOTE-SOPROVOZHDENIE-1S | CORVONERO-RSY | Сопровождение 1С / техподдержка / ошибки 1С | REMOTE | HIGH | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 03-REMOTE-DORABOTKA-1S | CORVONERO-RSY | Доработка / разработка 1С | REMOTE | MEDIUM | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 04-REMOTE-INTEGRACII-1S | CORVONERO-RSY | Интеграции 1С | REMOTE | MEDIUM | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |
| 05-REMOTE-MARKIROVKA-CHESTNY-ZNAK | CORVONERO-RSY | Маркировка / Честный знак | REMOTE | MEDIUM | INCLUDED | INCLUDED / IMPORT_CANDIDATE / NOT_UPLOAD_READY |

Priority:

- **HIGH:** 01-LOCAL-PROGRAMMIST-1S, 02-LOCAL-SOPROVOZHDENIE-1S, 02-REMOTE-SOPROVOZHDENIE-1S, 05-LOCAL-MARKIROVKA-CHESTNY-ZNAK
- **MEDIUM:** 01-REMOTE-PROGRAMMIST-1S, 03-REMOTE-DORABOTKA-1S, 04-REMOTE-INTEGRACII-1S, 05-REMOTE-MARKIROVKA-CHESTNY-ZNAK
- **TEST:** 03-LOCAL-DORABOTKA-1S, 04-LOCAL-INTEGRACII-1S

---

## 3. Budget / strategy / goals (candidate)

| Field | Value | Status |
|-------|--------|--------|
| Working budget | 50 000 ₽ | OPERATOR_APPROVED_INPUT / campaign-level working budget / OPERATOR_APPROVED_INPUT |
| Daily / weekly / monthly mapping | not invented | CHECK_REQUIRED |
| Strategy intent | payment for leads / conversions | APPROVED_AS_INTENT |
| Exact Direct strategy field | not invented | CHECK_REQUIRED |
| Package/portfolio | not used at v0.2 start | APPROVED |
| Goals available (operator) | form; calls | OPERATOR_CONFIRMED |
| Exact goal names / IDs | unknown | CHECK_REQUIRED |
| GOAL_MAPPING_TO_DIRECT | CHECK_REQUIRED | CHECK_REQUIRED |
| Campaign type | not invented | CHECK_REQUIRED |

Do not copy Search CPA 4 516.67 ₽ as an RSY target.

---

## 4. Geo working assumptions

| Mode | Working assumption | Exact Direct geo |
|------|--------------------|------------------|
| LOCAL | Новосибирск / Новосибирская область candidate | CHECK_REQUIRED |
| REMOTE | Россия candidate; Новосибирск / область exclusion candidate | CHECK_REQUIRED |

Not import-ready until geo is operator-approved and mapped to the actual import format.

---

## 5. Materials in this pack

| Material | Status |
|----------|--------|
| Campaign/group candidates | CREATED |
| Ad candidates | CREATED / CANDIDATE_FOR_OPERATOR_REVIEW / NOT_FINAL_DIRECT_AD |
| URL/UTM candidates | CREATED / CANDIDATE_FOR_REVIEW / NOT_FINAL_IMPORT_URL |
| Targeting candidates | CREATED / cold RSY now |
| Image requirements | CREATED WITHOUT PROMPTS |
| Exclusions | CREATED / CANDIDATE_FOR_REVIEW / NOT_FINAL |
| Operator review checklist | CREATED |
| Not-upload-ready guard | CREATED |
| Direct upload XLSX | NOT CREATED |
| Optional Commander-like XLSX | NOT CREATED — format not verified; would risk being mistaken for upload |

---

## 6. What this pack does not create or modify

| Item | Status |
|------|--------|
| Final Direct import XLSX | NOT CREATED |
| Final Direct ads | NOT FINAL |
| Image prompts (no Midjourney / SD / DALL-E syntax) | NOT CREATED |
| Image files | NOT CREATED |
| Direct | NOT MODIFIED |
| Commander | NOT MODIFIED |
| Search campaign package V2.6.2 | UNCHANGED |
| Search UTM policy | UNCHANGED |
| Final stats source files | UNCHANGED |
| RSY v1 / v1.1 / generation v0.1 refs | UNCHANGED |
| Stable sheet / legal DOCX / landing DOCX | UNCHANGED |
| Launch approval | NOT GRANTED |

---

## 7. Next stage (separate charter)

1. Operator review of this import candidate (checklist OR-01…OR-22).
2. Close exact campaign type, Direct field names, goal IDs, geo, budget period mapping, UTM, ads, exclusions.
3. Separate image production with the operator (manual upload) — still no prompts here.
4. Landing/legal live-check.
5. Only then: import package v1 after explicit import and launch approval.

Until then: **not upload-ready**.

---

**Storage package:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-IMPORT-CANDIDATE-v0.2-2026-08-19`  
XLSX workbooks live in Storage only (not in Git).
