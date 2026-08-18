# CORVONERO — РСЯ open confirmations v1

**Status:** OPEN / ARCHITECTURE_NOT_LAUNCH_APPROVED  
**Created:** 2026-08-18  
**Project:** CorvoNero / Корво Неро  

Known operator decision (already recorded, do not re-open as a blocker for architecture):

> All Search directions, including weak/disabled, must be included in РСЯ **planning**.

That decision is **not** launch approval.

---

## Confirmations

| ID | Topic | Current mark | Notes |
|----|-------|--------------|-------|
| OC-01 | Final campaign structure: one common vs LOCAL/REMOTE split | RECOMMENDED_LOCAL_REMOTE_SPLIT / OPERATOR_TO_CONFIRM | Pack is built on Option B: `CORVONERO-RSY-LOCAL` + `CORVONERO-RSY-REMOTE`. Option A remains a documented fallback. |
| OC-02 | Daily budget | TO_CONFIRM | Not in Search exports as an РСЯ budget. Do not copy Search spend rate blindly. |
| OC-03 | Monthly budget | TO_CONFIRM | Same. |
| OC-04 | Bidding strategy | TO_CONFIRM | Search combined report strategy text: «Максимум конверсий с ограничением по цене». РСЯ strategy is a separate decision. Do not copy Search CPA ≈ 4 517 ₽ as a Networks bid. |
| OC-05 | Use all five landing pages in first launch | ARCHITECTURE_YES / LAUNCH_TO_CONFIRM | Architecture maps all five. Phased launch is still an operator choice. |
| OC-06 | LOCAL and REMOTE use same landing URLs | RECOMMENDED_SAME_URL / OPERATOR_TO_CONFIRM | No separate URLs found in V2.6 materials. |
| OC-07 | Exact geography for LOCAL | TO_CONFIRM | Planning: Новосибирск / local scenario. City vs oblast vs radius: SAFE UNKNOWN. |
| OC-08 | Exact geography for REMOTE | TO_CONFIRM | Planning: Russia-wide remote, without Novosibirsk visit promise. Whether to exclude Novosibirsk from REMOTE: TO_CONFIRM. |
| OC-09 | First launch: all weak Search directions vs phased | ARCHITECTURE_INCLUDE_ALL / LAUNCH_PHASE_TO_CONFIRM | Planning includes weak/disabled. Operator may still phase **budget** without dropping them from the map. |
| OC-10 | Image style and production | TO_CONFIRM | Separate future stage. Skeleton only. `IMAGE_PROMPT_NOT_CREATED`. |
| OC-11 | Brand restrictions on creatives | TO_CONFIRM | Logo, colors, 1C UI depiction, partner marks. Forbidden claims listed in architecture. |
| OC-12 | Legal / disclaimer requirements on ads | TO_CONFIRM | Legal DOCX review was NOT COMPLETED (stable sheet 2026-08-12). Publication SAFE UNKNOWN. |
| OC-13 | Metrica goals / audiences availability | SAFE UNKNOWN / TO_CONFIRM | Exact goal names not in Search exports. |
| OC-14 | Retargeting audience availability | SAFE UNKNOWN / TO_CONFIRM | Site, LP, form, messenger, goal audiences not proven. |
| OC-15 | Separate remarketing from cold РСЯ | TO_CONFIRM | Suggestion only: cold groups as mapped; remarketing later if audiences exist. |
| OC-16 | Final launch approval | NOT_GRANTED | This pack must not be treated as permission to upload. |
| OC-17 | Price/offer claims in РСЯ copy | TO_CONFIRM | Search claims register still «ТРЕБУЕТ ПОДТВЕРЖДЕНИЯ» (выезд, удалённо, от 3 000 ₽/час, минимум 2 часа, перечень конфигураций). |
| OC-18 | Whether disabled live Search groups still exist | SAFE UNKNOWN | No current Direct/Commander snapshot. Architecture still maps all five directions. |

---

## Already decided for planning (not launch)

| Topic | Decision |
|-------|----------|
| Include weak Search directions in the architecture | YES |
| Include disabled Search groups as candidates inside direction×geo | YES (as planning rule) |
| Exclude a direction because Search did not convert | NO |
| Generate import XLSX now | NO |
| Write final ads now | NO |
| Write image prompts now | NO |
| Modify Direct / Commander / V2.6.2 | NO |

---

## What “include in planning” does not mean

It does not force equal first-wave budget. HIGH / MEDIUM / TEST priorities exist so the operator can later phase spend while keeping all ten groups on the map.

---

**Storage package:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-PACK-2026-08-18\`  
XLSX workbooks live in Storage only (not in Git).
