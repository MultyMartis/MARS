# CORVONERO — РСЯ Generation Draft Pack v0.1

**Status:** GENERATION_DRAFT / NOT_IMPORT_READY / NOT_LAUNCH_APPROVED  
**Created:** 2026-08-19T02:10:00+07:00  
**Project:** CorvoNero / Корво Неро  
**Programme:** mars-search-ppc-production  
**Search authority (unchanged):** V2.6 / deployable V2.6.2  
**Architecture refs:** v1 checkpoint `e89c9593d9dd70a8e12c81bbed0d470386bc51c6`; v1.1 checkpoint `70db414e542976f029579e61daaea1848086931d`

This pack prepares **draft** RSY campaign-build materials for operator review. It is **not** an import-ready Direct package.

| Guard | Value |
|-------|--------|
| IMPORT_READY | **NO** |
| GENERATION_DRAFT_READY | **YES** (for operator review) |
| Launch | NOT GRANTED |
| Final ads | NOT CREATED |
| Image prompts | NOT CREATED |
| Images | NOT CREATED |
| Direct / Commander | NOT MODIFIED |
| Search package V2.6.2 | UNCHANGED |

---

## 1. Purpose

Create the first CorvoNero RSY Generation Draft Pack v0.1 from approved architecture v1 and v1.1 revision:

1. Draft campaign/group structure (primary two campaigns + one-campaign fallback).
2. Draft service-group map (5/5 directions, 10 groups, weak directions included).
3. Draft RSY message variants by service and LOCAL/REMOTE.
4. Draft URL/UTM plan (does not overwrite Search UTM policy).
5. Draft audience/targeting logic (cold RSY now; retargeting later).
6. Draft minus/exclusion logic for RSY (not a blind copy of Search negatives).
7. Draft image requirements list **without prompts and without files**.
8. Draft import-readiness checklist with blockers.
9. Explicit not-import-ready guard until budget, strategy, geography, package support and launch approval are confirmed.

---

## 2. Working assumptions (draft only)

All of the following are **WORKING_ASSUMPTION / OPERATOR_APPROVAL_REQUIRED**. They are planning scaffolding, not cabinet settings.

1. **Structure:** prepare materials for `CORVONERO-RSY-LOCAL` + `CORVONERO-RSY-REMOTE`, 5 service groups each, **10 groups**.
2. **Portfolio/package:** those two campaigns should preferably attach to **one package/portfolio strategy** if Direct supports it for the selected type and this login.
3. **Fallback:** also preserve `CORVONERO-RSY` — 10 groups, or 5 service groups with LOCAL/REMOTE message variants.
4. **LOCAL geo candidate:** Новосибирск / Новосибирская область. Exact geography **OPEN**.
5. **REMOTE geo candidate:** Россия, with Новосибирск / область exclusion as a candidate. Exact geography **OPEN**.
6. **Budget:** OPEN. No invented daily/monthly/weekly numbers. Placeholders only: `[OPERATOR_TO_FILL]`.
7. **Strategy:** OPEN. Fields reserved for package strategy, maximum conversions, weekly budget, manual/limited test mode. **No final strategy selected.**
8. **Landings:** existing five URLs, `SAME_URL_FOR_LOCAL_AND_REMOTE` unless later changed.
9. **Images:** required later; no prompts; no files; manual upload with operator.
10. **Launch / import:** NOT approved.

`STRUCTURE_STATUS:` **DRAFT / APPROVAL_REQUIRED**

---

## 3. Draft structure

### Primary (prepared)

| Campaign | Role | Groups | Package note |
|----------|------|--------|--------------|
| `CORVONERO-RSY-LOCAL` | Local / Novosibirsk candidate / local discussion | 5 | Prefer one package with REMOTE |
| `CORVONERO-RSY-REMOTE` | Remote / Russia candidate / no office tie | 5 | Prefer one package with LOCAL |

Do **not** treat two campaigns as two independent conversion/budget pools unless package is unavailable **and** the operator explicitly accepts two learning pools (v1.1 correction).

### Fallback (documented, not chosen as import-ready)

| Variant | Campaign | Groups |
|---------|----------|--------|
| Preferred fallback | `CORVONERO-RSY` | same 10 group codes |
| Compact fallback | `CORVONERO-RSY` | 5 service groups with LOCAL/REMOTE geo + message variants |

Use fallback if package UI is missing or budget cannot support two realistic learning pools.

### Expansion (later, not this draft)

If budget and conversions grow: split HIGH-volume services into extra campaigns **inside the same package**, keep TEST/weak as groups. Not day-one.

### Directions and groups

Directions included: **5/5**. Weak/non-converting/disabled Search directions: **included**. EXCLUDE: **0**. Weak directions are **not** equal-budget winners.

| Group | Campaign candidate | Direction | Mode | Priority | Inclusion | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 01-LOCAL-PROGRAMMIST-1S | CORVONERO-RSY-LOCAL | Программист 1С | LOCAL | HIGH | SEARCH_WORKING_SIGNAL | DRAFT_NOT_IMPORT_READY |
| 02-LOCAL-SOPROVOZHDENIE-1S | CORVONERO-RSY-LOCAL | Сопровождение 1С / техподдержка / ошибки 1С | LOCAL | HIGH | SEARCH_WORKING_SIGNAL | DRAFT_NOT_IMPORT_READY |
| 03-LOCAL-DORABOTKA-1S | CORVONERO-RSY-LOCAL | Доработка / разработка 1С | LOCAL | TEST | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + OPERATOR_REQUIRED_ALL_NICHES | DRAFT_NOT_IMPORT_READY |
| 04-LOCAL-INTEGRACII-1S | CORVONERO-RSY-LOCAL | Интеграции 1С | LOCAL | TEST | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + OPERATOR_REQUIRED_ALL_NICHES | DRAFT_NOT_IMPORT_READY |
| 05-LOCAL-MARKIROVKA-CHESTNY-ZNAK | CORVONERO-RSY-LOCAL | Маркировка / Честный знак | LOCAL | HIGH | SEARCH_WORKING_SIGNAL | DRAFT_NOT_IMPORT_READY |
| 01-REMOTE-PROGRAMMIST-1S | CORVONERO-RSY-REMOTE | Программист 1С | REMOTE | MEDIUM | OPERATOR_REQUIRED_ALL_NICHES + LANDING_AVAILABLE | DRAFT_NOT_IMPORT_READY |
| 02-REMOTE-SOPROVOZHDENIE-1S | CORVONERO-RSY-REMOTE | Сопровождение 1С / техподдержка / ошибки 1С | REMOTE | HIGH | SEARCH_WORKING_SIGNAL | DRAFT_NOT_IMPORT_READY |
| 03-REMOTE-DORABOTKA-1S | CORVONERO-RSY-REMOTE | Доработка / разработка 1С | REMOTE | MEDIUM | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + LANDING_AVAILABLE | DRAFT_NOT_IMPORT_READY |
| 04-REMOTE-INTEGRACII-1S | CORVONERO-RSY-REMOTE | Интеграции 1С | REMOTE | MEDIUM | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + LANDING_AVAILABLE | DRAFT_NOT_IMPORT_READY |
| 05-REMOTE-MARKIROVKA-CHESTNY-ZNAK | CORVONERO-RSY-REMOTE | Маркировка / Честный знак | REMOTE | MEDIUM | OPERATOR_REQUIRED_ALL_NICHES + LANDING_AVAILABLE | DRAFT_NOT_IMPORT_READY |

Priority affects **control**, not inclusion:

- **HIGH (4):** LOCAL программист, LOCAL сопровождение, REMOTE сопровождение, LOCAL маркировка
- **MEDIUM (4):** REMOTE программист, REMOTE доработка, REMOTE интеграции, REMOTE маркировка
- **TEST (2):** LOCAL доработка, LOCAL интеграции

---

## 4. Draft materials in this pack

| Material | Status |
|----------|--------|
| Campaign/group draft | CREATED |
| Message draft (not final Direct ads) | CREATED |
| URL/UTM draft | CREATED / DRAFT_APPROVAL_REQUIRED |
| Targeting draft | CREATED / cold RSY now |
| Exclusions draft | CREATED / DRAFT_REVIEW_REQUIRED |
| Image requirements | CREATED WITHOUT PROMPTS |
| Import readiness checklist | CREATED / IMPORT_READY=NO |

Companion files (repo `rsy/generation/` and Storage numbered copies): campaign-group, messages, URL/UTM, targeting, exclusions, image requirements, import checklist, open confirmations, not-import-ready guard.

---

## 5. Budget and strategy placeholders

| Field | Value | Status |
|-------|--------|--------|
| Daily budget | `[OPERATOR_TO_FILL]` | OPEN |
| Weekly budget (campaign or package) | `[OPERATOR_TO_FILL]` | OPEN |
| Monthly budget | `[OPERATOR_TO_FILL]` | OPEN |
| Package / portfolio strategy | evaluate / bind LOCAL+REMOTE if supported | OPEN / CABINET |
| Maximize conversions | field reserved | NOT SELECTED |
| Weekly budget-only start | field reserved | NOT SELECTED |
| Manual / limited test mode | field reserved | NOT SELECTED |
| Target CPA | `[OPERATOR_TO_FILL]` — do not copy Search 4 516.67 ₽ | OPEN |
| Acceptable test spend per weak direction | `[OPERATOR_TO_FILL]` | OPEN |
| Conversion goal | `[OPERATOR_TO_FILL]` | SAFE UNKNOWN |

Help sizing formula remains architectural (weekly budget ≥ 10 × CPA; ~10 conversions/week, package = sum). It is **not** filled with CorvoNero numbers here.

---

## 6. What this pack does not create

| Item | Status |
|------|--------|
| RSY import XLSX for Direct/Commander | NOT CREATED |
| Final Direct ads | NOT CREATED |
| Image prompts (incl. Midjourney/SD/DALL-E syntax) | NOT CREATED |
| Image files | NOT CREATED |
| Direct / Commander changes | NOT MODIFIED |
| Search campaign package V2.6.2 | UNCHANGED |
| Search UTM policy | UNCHANGED |
| Final stats source files | UNCHANGED |
| RSY architecture v1 / v1.1 source files | UNCHANGED |
| Stable sheet / legal DOCX / landing DOCX | UNCHANGED |
| Launch approval | NOT GRANTED |

---

## 7. Next stage (separate charter)

1. Operator review of this draft.
2. Close budget, strategy, package UI, geo, goals (see open confirmations).
3. Separate image production with the operator (manual upload) — still no prompts here.
4. Only then: generation v1 / import package after explicit import and launch approval.

Until then: **not import-ready**.

---

**Storage package:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-GENERATION-DRAFT-PACK-2026-08-19\`  
XLSX workbooks live in Storage only (not in Git).
