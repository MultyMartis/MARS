# Wordstat Manual Export — Corvonero — Two-Pass Collection

**Session:** `mig-20260622-corv01`  
**Provider:** Yandex Wordstat  
**Capture method:** Manual operator collection (**Pass A COMPLETE — 2026-06-22 Storage correction**)  
**External evidence source:** `C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\`  
**Policy corrected:** 2026-06-22  

---

## Collection policy

| Pass | Status | Geography | Query entry | Progress |
|------|--------|-----------|-------------|----------|
| **A — Semantic Discovery** | **COMPLETE** | Все регионы / all Russia | Broad, **unquoted**, one seed at a time | **COMPLETE** — 18 Excel + 2 no-result |
| **B — Regional Demand Validation** | **PREPARED** | Новосибирск + Новосибирская область | Exact / quoted / operator variants on **bounded shortlist only** | **NOT STARTED** |

**af-006 scope:** Automated Cursor-agent Wordstat collection only — **does not block** manual operator Pass A/B.

---

## Pass A — Semantic Discovery (COMPLETE)

**Source of truth (immutable raw exports):** `C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\`  
**Normalized index:** `evidence/wordstat/wordstat-pass-a-file-index.json`  
**Ingestion command:** `node tools/ingest-wordstat-pass-a.mjs "C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06"`

| query_id | seed phrase (unquoted) | export file | rows | status |
|----------|------------------------|-------------|------|--------|
| ws-p1-001 | программист 1С | `ws-p1-001-programmist-1c.xlsx` | 589 | INGESTED |
| ws-p1-002 | программист 1С Новосибирск | `ws-p1-002-uslugi-programmista-1c.xlsx` | 5 | INGESTED |
| ws-p1-003 | сопровождение 1С | `ws-p1-003-soprovozhdenie-1c.xlsx` | 177 | INGESTED |
| ws-p1-004 | доработка 1С | `ws-p1-004-dorabotka-1c.xlsx` | 83 | INGESTED |
| ws-p1-005 | интеграция 1С с сайтом | `ws-p1-005-integraciya-s-saitom.xlsx` | 10 | INGESTED |
| ws-p1-006 | интеграция 1С Битрикс | `ws-p1-006-integraciya-bitrix.xlsx` | 28 | INGESTED |
| ws-p1-007 | маркировка в 1С | `ws-p1-007-markirovka-v-1c.xlsx` | 196 | INGESTED |
| ws-p1-008 | Честный знак 1С | `ws-p1-008-chestny-znak-1c.xlsx` | 250 | INGESTED |
| ws-p2-001 | доработка отчёта 1С | `ws-p2-001-otchet-1c.xlsx` | 2 | INGESTED |
| ws-p2-002 | доработка печатной формы 1С | `ws-p2-002-pechatnaya-forma.xlsx` | 542 | INGESTED |
| ws-p2-003 | доработка РМК 1С | — | — | **NO RESULT** (entered: `доработка РМК`) |
| ws-p2-004 | настройка синхронизации 1С | `ws-p2-004-sinhronizaciya.xlsx` | 384 | INGESTED |
| ws-p2-005 | обновление доработанной 1С | `ws-p2-005-obnovlenie-dorabotannoy.xlsx` | 1 | INGESTED |
| ws-p2-006 | срочно программист 1С | — | — | **NO RESULT** (entered: `срочно программист 1С`) |
| ws-p2-007 | 1С не работает | `ws-p2-007-1c-ne-rabotaet.xlsx` | 1 | INGESTED |
| ws-p3-001 | маркировка пива 1С | `ws-p3-001-pivo.xlsx` | 2 | INGESTED |
| ws-p3-002 | маркировка воды 1С | `ws-p3-002-voda.xlsx` | 1 | INGESTED |
| ws-p3-003 | маркировка лекарств 1С | `ws-p3-003-lekarstva.xlsx` | 1 | INGESTED |
| ws-p3-004 | ТС ПИОТ 1С | `ws-p3-004-avtozapchasti.xlsx` | 33 | INGESTED — slug/matrix mismatch flagged |
| ws-p3-005 | маркировка автозапчастей 1С | `ws-p3-005-ts-piot.xlsx` | 22 | INGESTED — slug/matrix mismatch flagged |

**Prior table (IN PROGRESS / NOT STARTED) superseded by Storage-path ingestion correction 2026-06-22.**

### Pass A operator notes (ws-p1-001)

- Query entered: `программист 1С` — **no quotation marks**
- Region: **all regions**
- Devices: desktop, smartphone, tablet selected
- Operator observed page total **19,682** for shown period — **semantic discovery signal only**; **not** recorded as frequency, regional demand, or traffic forecast
- Related/noise classes visible: vacancy, training, salary, remote work, services, informational
- Evidence ref: `evidence/wordstat/pass-a-ws-p1-001-evidence.json`
- Expected screenshot path: `evidence/wordstat/screenshots/ws-p1-001-programmist-1c.jpg` — **awaiting ingestion**

---

## Pass B — Regional Demand Validation (NOT STARTED)

Bounded shortlist — exact/quoted operator syntax — Novosibirsk + NSO only. **Does not replace Pass A.**

| query_id | exact phrase | operator syntax | region | frequency | status |
|----------|--------------|-----------------|--------|-----------|--------|
| ws-p1-001 | программист 1С | "программист 1С" | Новосибирск + НСО | — | NOT STARTED |
| ws-p1-002 | программист 1С Новосибирск | "программист 1С Новосибирск" | Новосибирск + НСО | — | NOT STARTED |
| ws-p1-003 | сопровождение 1С | "сопровождение 1С" | Новосибирск + НСО | — | NOT STARTED |
| ws-p1-004 | доработка 1С | "доработка 1С" | Новосибирск + НСО | — | NOT STARTED |
| ws-p1-005 | интеграция 1С с сайтом | "интеграция 1С с сайтом" | Новосибирск + НСО | — | NOT STARTED |
| ws-p1-006 | интеграция 1С Битрикс | "интеграция 1С Битрикс" | Новосибирск + НСО | — | NOT STARTED |
| ws-p1-007 | маркировка в 1С | "маркировка в 1С" | Новосибирск + НСО | — | NOT STARTED |
| ws-p1-008 | Честный знак 1С | "Честный знак 1С" | Новосибирск + НСО | — | NOT STARTED |

P2/P3 Pass B rows deferred until Pass A review identifies shortlist candidates.

---

## Interpretation rules

- Pass A nationwide broad totals → **semantic vocabulary and noise discovery only**
- Pass B regional quoted frequencies → **local demand validation** (when collected)
- Never merge Pass A nationwide display into Novosibirsk demand evidence
- Never present Wordstat UI totals as expected advertising traffic

---

## SAFE UNKNOWN

- All Pass B regional frequencies
- Pass A row-level related-query transcription (except ws-p1-001 noise classes)
- Broad vs exact comparison (Pass B)
- Seasonality
- Wordstat period label for ws-p1-001 screenshot
