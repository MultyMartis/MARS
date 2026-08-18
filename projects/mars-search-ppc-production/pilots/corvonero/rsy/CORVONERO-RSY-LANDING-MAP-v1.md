# CORVONERO — РСЯ landing map v1

**Status:** SAME_URL_FOR_LOCAL_AND_REMOTE / LIVE_HTTP_NOT_RESCANNED  
**Created:** 2026-08-18  
**Project:** CorvoNero / Корво Неро  

Live scan of URLs was **not** performed in this task. Prelaunch (2026-07-10) recorded 5/5 `READY_WITH_WARNINGS`; current live status is **SAFE UNKNOWN**.

---

## Rule

For LOCAL and REMOTE РСЯ groups, use the **same landing URL** unless existing materials explicitly define separate URLs. No such split was found in V2.6 / V2.6.2 / stable sheet / landing packs.

Landing split: `SAME_URL_FOR_LOCAL_AND_REMOTE`.

Differentiation LOCAL vs REMOTE belongs in **ad/message/image**, not in a second URL — until the operator later commissions separate landings.

LP-06 (reports) is historical/deferred and is **not** part of this РСЯ architecture.

---

## Map

| LP | Direction | Group codes | URL | LOCAL uses | REMOTE uses | Use in architecture |
|----|-----------|-------------|-----|------------|-------------|---------------------|
| LP-01 | Программист 1С | 01-LOCAL-PROGRAMMIST-1S; 01-REMOTE-PROGRAMMIST-1S | https://lk.corvonero.ru/programmist-1s/ | YES | YES | YES |
| LP-02 | Сопровождение 1С | 02-LOCAL-SOPROVOZHDENIE-1S; 02-REMOTE-SOPROVOZHDENIE-1S | https://lk.corvonero.ru/soprovozhdenie-1s/ | YES | YES | YES |
| LP-03 | Доработка / разработка 1С | 03-LOCAL-DORABOTKA-1S; 03-REMOTE-DORABOTKA-1S | https://lk.corvonero.ru/dorabotka-razrabotka-1s/ | YES | YES | YES |
| LP-04 | Интеграции 1С | 04-LOCAL-INTEGRACII-1S; 04-REMOTE-INTEGRACII-1S | https://lk.corvonero.ru/integracii-1s/ | YES | YES | YES |
| LP-05 | Маркировка / Честный знак | 05-LOCAL-MARKIROVKA-CHESTNY-ZNAK; 05-REMOTE-MARKIROVKA-CHESTNY-ZNAK | https://lk.corvonero.ru/markirovka-chestny-znak/ | YES | YES | YES |

Open confirmation: whether the **first РСЯ launch** uses all five pages or a phased subset. Architecture includes all five because the operator required all Search directions.

---

## Source of URLs

- Search V2.6.2 groups CSV: `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30\CORVONERO-v2.6.2-FINAL-GROUPS.csv`
- РСЯ preparation basis: `projects/mars-search-ppc-production/pilots/corvonero/final-report/CORVONERO-RSY-PREPARATION-BASIS-v1.md`
- Stable sheet landing list (2026-08-12)

Landing DOCX packs were **not modified** and were not used as a rewrite source in this task.

---

**Storage package:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-ARCHITECTURE-PACK-2026-08-18\`  
XLSX workbooks live in Storage only (not in Git).
