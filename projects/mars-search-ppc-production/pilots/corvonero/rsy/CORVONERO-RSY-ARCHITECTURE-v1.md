# CORVONERO — РСЯ campaign architecture v1

**Status:** ARCHITECTURE_PACK / NOT_AN_IMPORT_PACKAGE / NOT_LAUNCH_APPROVED  
**Created:** 2026-08-18  
**Project:** CorvoNero / Корво Неро  
**Programme:** mars-search-ppc-production  
**Lane:** Search PPC production delivery → RSY planning  
**Current Search state:** OPERATIONAL / LAUNCHED / PERFORMANCE_OBSERVATION  
**Search authority (unchanged):** V2.6 / deployable V2.6.2  

This file is **planning architecture only**. It is not an РСЯ import package, not final ads, not image prompts, and not launch approval.

Operator decision already in force for this pack:

> Include ALL niches/directions that were advertised or are currently advertised in Search, including directions that did not perform on Search and including disabled/weak groups. Do not exclude a direction from РСЯ just because it did not “стрелять” on Search.

---

## 1. Purpose

Prepare the first CorvoNero Yandex Advertising Network / РСЯ campaign architecture pack from:

1. Final available Search statistics (processed 2026-08-18).
2. Existing CorvoNero Search PPC project base (V2.6 / V2.6.2).
3. Operator inclusion rule: all five advertised directions, LOCAL and REMOTE.

Next stage (not this pack): actual РСЯ campaign generation / import package after operator confirmations.

---

## 2. Search evidence used (read-only)

| Item | Value |
|------|--------|
| Report period in files | 21.05.2026 — 18.08.2026 |
| Days with data | 15.07.2026 — 18.08.2026 (23 days) |
| Placement official totals | 38 353 impressions / 358 clicks / CTR 0.93% / 27 100 ₽ / CPC 75.70 ₽ / 6 conversions / CR 1.68% / CPA 4 516.67 ₽ / avg. position 4.21 |
| Combined detailed grain | 38 238 / 354 / same spend and conversions / bounce 38.23% / depth 1.05 |
| Conversion grain | All 6 conversions and 100% spend in placement report sit on **автотаргетинг** |
| Phone leads outside Metrica | ≈3 / OPERATOR_REPORTED_APPROXIMATE |
| Deals | 2 / OPERATOR_REPORTED |
| Exact Metrica goal names | SAFE UNKNOWN |
| РСЯ historical performance | none in these files / SAFE UNKNOWN |

Search structure (unchanged): 10 campaigns / 71 groups / 926 keyword placements / 71 ads.

---

## 3. Recommended campaign structure

**Recommendation:** `LOCAL_REMOTE_SPLIT` (Option B).

| Option | Name | Verdict |
|--------|------|---------|
| A | One common РСЯ campaign | Not recommended as default |
| B | Two campaigns: `CORVONERO-RSY-LOCAL` + `CORVONERO-RSY-REMOTE` | **RECOMMENDED** |

### Why two campaigns

- Search V2.6 already used LOCAL / REMOTE as the primary control split (10 Search campaigns = 5 directions × 2 geo modes).
- Service promise differs: LOCAL = Новосибирск / possible on-site visit; REMOTE = удалённо по России, without a Novosibirsk visit promise.
- Geography, bidding, frequency, and creative messaging can be controlled separately.
- Future images may differ by local vs remote context.
- Weak Search directions can still be tested **inside** the correct LOCAL or REMOTE container instead of being mixed with converting geo-mode traffic.
- Evidence does **not** strongly support one campaign: LOCAL spend 12 700 ₽ / 3 conversions vs REMOTE spend 14 400 ₽ / 3 conversions, but REMOTE conversions are 100% from сопровождение; mixing geo modes would blur diagnosis.

Option A remains documented as a fallback if the operator later prefers fewer objects. This pack is built around Option B.

### Recommended campaigns

| Campaign code | Role | Geography (planning) | Groups |
|---------------|------|----------------------|--------|
| `CORVONERO-RSY-LOCAL` | Local / Novosibirsk / possible visit | Новосибирск (exact geo targeting TO_CONFIRM) | 5 |
| `CORVONERO-RSY-REMOTE` | Remote / Russia-wide, no local visit promise | Россия, remote proposition (exact geo TO_CONFIRM) | 5 |

**Logical groups:** 10 (5 directions × LOCAL/REMOTE).  
Search’s 71 groups collapse into these 10 РСЯ containers. Disabled or weak Search groups remain **candidates inside** the matching direction×geo group; they are not excluded.

---

## 4. Directions included (5/5)

| # | Direction | LOCAL | REMOTE | INCLUDED_IN_RSY | Primary reason | Search signal |
|---|-----------|-------|--------|-----------------|----------------|---------------|
| 1 | Программист 1С | YES | YES | YES | SEARCH_WORKING_SIGNAL (LOCAL); OPERATOR_REQUIRED_ALL_NICHES (REMOTE) | LOCAL 1 conv / 4 100 ₽; REMOTE 52 clicks / 0 ₽ / 0 conv |
| 2 | Сопровождение 1С / техподдержка / ошибки 1С | YES | YES | YES | SEARCH_WORKING_SIGNAL | 4 conv / 19 500 ₽ (LOCAL 1 + REMOTE 3) |
| 3 | Доработка / разработка 1С | YES | YES | YES | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + OPERATOR_REQUIRED_ALL_NICHES | 12 clicks / 0 ₽ / 0 conv |
| 4 | Интеграции 1С | YES | YES | YES | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + OPERATOR_REQUIRED_ALL_NICHES | 21 clicks / 0 ₽ / 0 conv; LOCAL INTEGRACII 0 clicks |
| 5 | Маркировка / Честный знак | YES | YES | YES | SEARCH_WORKING_SIGNAL (LOCAL); OPERATOR_REQUIRED_ALL_NICHES (REMOTE) | LOCAL 1 conv / 3 500 ₽; REMOTE 105 clicks / 0 ₽ / 0 conv |

Weak / non-converting Search directions **included:** YES.

No group in this pack is set to `EXCLUDE`. None of the five directions is outside CorvoNero services.

---

## 5. Group map (logical РСЯ groups)

### LOCAL — `CORVONERO-RSY-LOCAL`

| Group code | Direction | Priority | Include | Reason |
|------------|-----------|----------|---------|--------|
| `01-LOCAL-PROGRAMMIST-1S` | Программист 1С | HIGH | YES | SEARCH_WORKING_SIGNAL |
| `02-LOCAL-SOPROVOZHDENIE-1S` | Сопровождение 1С | HIGH | YES | SEARCH_WORKING_SIGNAL |
| `03-LOCAL-DORABOTKA-1S` | Доработка / разработка 1С | TEST | YES | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED |
| `04-LOCAL-INTEGRACII-1S` | Интеграции 1С | TEST | YES | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED |
| `05-LOCAL-MARKIROVKA-CHESTNY-ZNAK` | Маркировка / Честный знак | HIGH | YES | SEARCH_WORKING_SIGNAL |

### REMOTE — `CORVONERO-RSY-REMOTE`

| Group code | Direction | Priority | Include | Reason |
|------------|-----------|----------|---------|--------|
| `01-REMOTE-PROGRAMMIST-1S` | Программист 1С | MEDIUM | YES | OPERATOR_REQUIRED_ALL_NICHES + LANDING_AVAILABLE |
| `02-REMOTE-SOPROVOZHDENIE-1S` | Сопровождение 1С | HIGH | YES | SEARCH_WORKING_SIGNAL |
| `03-REMOTE-DORABOTKA-1S` | Доработка / разработка 1С | MEDIUM | YES | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + LANDING_AVAILABLE |
| `04-REMOTE-INTEGRACII-1S` | Интеграции 1С | MEDIUM | YES | DISABLED_OR_WEAK_SEARCH_BUT_INCLUDED + LANDING_AVAILABLE |
| `05-REMOTE-MARKIROVKA-CHESTNY-ZNAK` | Маркировка / Честный знак | MEDIUM | YES | OPERATOR_REQUIRED_ALL_NICHES + LANDING_AVAILABLE |

Priority rules applied:

- **HIGH** — Search working signal (conversions present, n=6, low-volume caution).
- **MEDIUM** — landing exists and Search produced traffic without conversions.
- **TEST** — very weak or zero Search clicks, still included by operator rule.

Full row-level map: `02-CORVONERO-RSY-GROUP-MAP-v1.xlsx` and repo `CORVONERO-RSY-GROUP-MAP-v1.md`.

---

## 6. Landing map

Landing split: **SAME_URL_FOR_LOCAL_AND_REMOTE**.

No separate LOCAL vs REMOTE landing URLs are defined in V2.6 materials. Live HTTP status was **not** rescanned in this task (SAFE UNKNOWN).

| ID | Direction | URL | LOCAL | REMOTE |
|----|-----------|-----|-------|--------|
| LP-01 | Программист 1С | https://lk.corvonero.ru/programmist-1s/ | same | same |
| LP-02 | Сопровождение 1С | https://lk.corvonero.ru/soprovozhdenie-1s/ | same | same |
| LP-03 | Доработка / разработка 1С | https://lk.corvonero.ru/dorabotka-razrabotka-1s/ | same | same |
| LP-04 | Интеграции 1С | https://lk.corvonero.ru/integracii-1s/ | same | same |
| LP-05 | Маркировка / Честный знак | https://lk.corvonero.ru/markirovka-chestny-znak/ | same | same |

LP-06 remains historical/deferred. Do not invent a sixth landing for РСЯ.

Whether to use all five landings in the first РСЯ launch is an **open confirmation**. Architecture includes all five.

---

## 7. Audience, message, images (pointers)

- Message map (conceptual angles, **not** final ads): `03-CORVONERO-RSY-MESSAGE-MAP-v1.md`
- Audience / intent / retargeting notes: `04-CORVONERO-RSY-AUDIENCE-AND-INTENT-MAP-v1.md`
- Landing detail: `05-CORVONERO-RSY-LANDING-MAP-v1.md`
- Image production brief **skeleton only**: `06-CORVONERO-RSY-IMAGE-PRODUCTION-BRIEF-SKELETON-v1.md`  
  Status for every group: `IMAGE_PROMPT_NOT_CREATED`. No prompts, no generated images.
- Open confirmations: `07-CORVONERO-RSY-OPEN-CONFIRMATIONS-v1.md`
- Not-for-generation guard: `08-CORVONERO-RSY-NOT-FOR-GENERATION-YET-v1.md`

---

## 8. Exclusions and cautions (planning, not import negatives)

Internal cautions from Search stats and existing Search negatives. **Not** a Commander negative list and **not** a Direct change.

**Audience / message cautions**

- Third-party vendor support identity (example from Search queries: Калуга Астрал).
- How-to / DIY 1C curiosity («как в 1с…») — weak commercial intent in the Search query export.
- ITS / личный кабинет curiosity with large impressions and almost no conversions.
- Job-seeker intent (vacancies, резюме) — already excluded in Search negatives; keep out of РСЯ messages.
- Training, licensing, franchising.

**Claims not to use** unless evidence later confirms them:

- official 1C partner / certified specialists
- guaranteed result
- 24/7 support
- fixed deadlines
- fixed price
- free audit

Search ads already use some commercial claims that still require client confirmation (выезд по Новосибирску, удалённо по России, от 3 000 ₽/час, минимальный заказ 2 часа). РСЯ copy must not treat those as proven until confirmed. See claims register: `projects/mars-search-ppc-production/pilots/corvonero/client-approval/CORVONERO-CLIENT-COMMERCIAL-CLAIMS-REGISTER-v1.json`.

Do not copy Search CPA (≈4 517 ₽) as an РСЯ bid. Search strategy text in the combined export was «Максимум конверсий с ограничением по цене»; РСЯ cost structure is a separate confirmation.

---

## 9. Search 71 groups → РСЯ 10 groups

V2.6.2 Search groups remain the source of **direction identity**, not the РСЯ group count.

| Search campaign family | Search groups (LOCAL+REMOTE) | РСЯ logical groups |
|------------------------|------------------------------|--------------------|
| CA-01 PROGRAMMIST | 4 LOCAL + 5 REMOTE | 01-LOCAL + 01-REMOTE |
| CA-02 SOPROVOZHDENIE | 10 LOCAL + 10 REMOTE | 02-LOCAL + 02-REMOTE |
| CA-03 DORABOTKA | 3 LOCAL + 3 REMOTE | 03-LOCAL + 03-REMOTE |
| CA-04 INTEGRACII | 4 LOCAL + 4 REMOTE | 04-LOCAL + 04-REMOTE |
| CA-05 MARKIROVKA | 14 LOCAL + 14 REMOTE | 05-LOCAL + 05-REMOTE |
| **Total** | **71** | **10** |

Live Direct enabled/disabled state of those 71 groups: **SAFE UNKNOWN** (no current Direct/Commander export in this task). Architecture treats disabled/weak Search groups as still in-scope for the matching РСЯ direction×geo container.

---

## 10. What this pack does not create

| Item | Status |
|------|--------|
| РСЯ import XLSX for Direct/Commander | NOT CREATED |
| Final РСЯ ad texts | NOT CREATED |
| Image prompts | NOT CREATED |
| Image files | NOT CREATED |
| Direct / Commander changes | NOT MODIFIED |
| Search campaign package V2.6.2 | UNCHANGED |
| Final stats intake source files | UNCHANGED (read-only) |
| Stable sheet package | UNCHANGED |
| Legal DOCX | UNCHANGED |
| Landing DOCX | UNCHANGED |
| Launch approval | NOT GRANTED |

---

## 11. Next stage (after operator approval)

1. Close open confirmations in `07-CORVONERO-RSY-OPEN-CONFIRMATIONS-v1.md`.
2. Separate image-production stage with the operator (manual upload).
3. Only then: РСЯ campaign generation / import package.

Until then this pack remains architecture only.

---

**Storage package:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-PACK-2026-08-18\`  
XLSX workbooks live in Storage only (not in Git).
