# REPORT — MIG Research Stage 1 — Корво Неро

**Session:** `mig-20260622-corv01`  
**Request:** `corvonero-yandex-direct-v1`  
**Date:** 2026-06-22  
**Lane:** A — Project Execution through MIG  
**Boundary:** Stage 1 only — no ORCA, no Wordstat, no full Website Intelligence  

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `main` |
| HEAD | *(see git status section)* |
| Prior Corvonero session | **None** — first session |
| Machine-readable request | **Created** — `incoming/mig/requests/request-corvonero-yandex-direct-v1.json` |
| Drop zone `incoming/mig/requests/` | **Active** per README |
| WIP conflict | **None** in `incoming/mig/pilots/corvonero/` |
| Research Request doc gate | Markdown artifact still marks **PENDING operator approval**; Cursor task treats intake as **approved for Stage 1 execution** via `operator_approval` in JSON |

---

## 2. MIG Execution Contract Review

| Contract | Application |
|----------|-------------|
| Research Request v0 | JSON normalized with `groundtruth_run`, RC-01 refs, capture_profile |
| Task File drop zone | Request placed in `incoming/mig/requests/` — **not** run through adapter (human Stage 1) |
| Session locus | Pilot folder: `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` (Triumph precedent) |
| Market Surface | Bounded multi-query SERP evidence in `serp_results/` |
| Competitor Discovery v0 | Preliminary candidates only — no confirmed competitors |
| Reality Acquisition R1–R4 | SERP grade **C**; website snapshot **B**; no R4 synthesis |
| Stage 1 exclusions | Wordstat, Landing Intelligence, full Website Intelligence, ORCA — **not executed** |

**Runtime helpers allowed (Core Run):** manual/bounded acquisition, session manifest, SERP normalization, competitor MVP derivation — **not** live SERP provider, approval automation, ORCA transport.

---

## 3. Machine Request

- **Path:** `incoming/mig/requests/request-corvonero-yandex-direct-v1.json`
- **request_id:** `corvonero-yandex-direct-v1`
- **ATLAS:** ORG-0009, LE-0006, PRJ-0013, WEB-CORV-01, DOM-CORV-01
- **JSON validity:** verified via `node -e JSON.parse` (see Validation)
- **No credentials** in file

---

## 4. Research Session

- **session_id:** `mig-20260622-corv01` (new; follows `mig-YYYYMMDD-suffix` Triumph pattern)
- **Manifest:** `session-mig-20260622-corv01/session_manifest.json`
- **Status:** `draft`
- **Queries executed:** 9 / 9 Stage 1 subset

---

## 5. Seed Query Matrix

- **Path:** `incoming/mig/pilots/corvonero/corvonero-seed-query-matrix-v1.json`
- **Clusters:** A (broad 1C), B (reports/forms), C (integrations), D (labeling/ЧЗ/ТС ПИОТ), E (product-specific — research only)
- **Stage 1 SERP subset:** q01–q09 documented in matrix
- **Not ad groups** — research seeds only

---

## 6. Market Surface Acquisition

| Query | Cluster | Commercial signal | Noise |
|-------|---------|-------------------|-------|
| программист 1С Новосибирск | A | **Strong** — local companies, franchisees, aggregators | Low |
| сопровождение 1С Новосибирск | A | **Strong** — dedicated support landings | Low |
| программа 1С не работает | A urgent | **Weak** — DIY blogs dominate | **High informational** |
| доработка отчёта 1С | B | **Moderate–strong** — modification landings | Low |
| интеграция 1С с сайтом Новосибирск | C | **Strong** — web studios | Low |
| интеграция 1С Битрикс | C | **Strong** — Bitrix integrators + aggregators | Moderate |
| Честный знак 1С настройка | D | **Moderate** — mix info + local vendor | **High informational** |
| маркировка в 1С Новосибирск | D | **Moderate** — local labeling vendor | Moderate info |
| ТС ПИОТ 1С настройка | D | **Weak** — how-to / regulatory content | **High informational** |

**Acquisition mode:** bounded web search (grade **C**). **Not** live Yandex mobile Playwright capture.

**Surfaces observed (types):** organic service pages, aggregators (Яндекс Услуги), informational blogs, regional support center (Мой бизнес), official partner directory reference.

**Ads / maps:** **SAFE UNKNOWN** — not isolated in this capture mode.

---

## 7. Initial Competitor Pool

| Class | Count (preliminary) | Examples |
|-------|---------------------|----------|
| 1 — Local companies NSO | 7+ | vigyana.ru, profinfoservice.ru, itsvsem.ru, shift-company |
| 2 — Freelancers / small teams | 2+ | Яндекс Услуги profiles |
| 3 — Federal / franchise 1C | 6+ | avanta-pro.ru, itllekt.ru, Первый Бит, somsk.ru |
| 4 — Labeling / ЧЗ specialists | 2 | ab-onlinekassa.ru (local), legasoft.ru (federal) |
| 5 — Integration / Bitrix web studios | 4 | yalstudio.ru, directline.pro, studio-expert.ru |
| 6 — Non-competitor reference | 3 | mbnso.ru, vendor blogs, v8.1c.ru |

**Total candidates:** 21 preliminary + 3 excluded references  
**Confirmed competitors:** **0** (by design — evidence insufficient for confirmation)

**Repeated domains across queries:** avanta-pro.ru (3), yalstudio.ru (2), studio-expert.ru (2), ab-onlinekassa.ru (2), uslugi.yandex.ru (2)

---

## 8. Corvonero Website Snapshot (WEB-CORV-01)

| Field | Observed |
|-------|----------|
| URL | http://lk.corvonero.ru/ |
| Availability | Available |
| Title | Корво Неро |
| Description | SAFE UNKNOWN |
| H1 / hero | «Корво Неро» — Внедрение и сопровождение 1С |
| Services | Внедрение, аудит, обновление, интеграция, отчёты/формы, маркировка/ЕГАИС, оборудование |
| CTA | Заявка, «Связаться с нами» |
| Form | Имя, email, телефон, описание задачи |
| Phone | +7 (383) 390-29-28 |
| Email | contact@corvonero.ru |
| Address | Новосибирск, Советская 64/1, оф. 804 |
| Pricing | 3000 ₽/час; от 2500 ₽ веб-публикация; от 7500 ₽ форма/отчёт |
| Trust | Process blocks only — **no cases/certs/partner badges on surface** |
| Tilda | Probable (form JSON structure) — not attested |
| Capture date | 2026-06-22 |

**Artifact:** `website-surface-snapshot.json`

---

## 9. Evidence and Acquisition Failures

| ID | Topic | Status |
|----|-------|--------|
| af-001 | Live Yandex SERP | **Failure** — synthesis only; operator manual SERP recommended |
| af-002 | Wordstat | **Excluded** Stage 1 |
| af-003 | Cluster E product SERP | **Deferred** |
| — | Target CPL / CPC | **SAFE UNKNOWN** — not fabricated |
| — | Ad block capture | **SAFE UNKNOWN** |

---

## 10. Stage 1 Findings (review questions)

### Q1 — Достаточен ли seed-query scope?

**Partially sufficient** for Stage 1 orientation. Clusters A–D covered in matrix; Stage 1 executed 9 representative queries. **Gaps:** Cluster E (product-specific labeling) not SERP-tested; geo variants for urgent queries; «Новосибирская область» as explicit modifier under-tested.

### Q2 — Какие запросы дали коммерческую выдачу?

**Strong commercial:** `программист 1С Новосибирск`, `сопровождение 1С Новосибирск`, `интеграция 1С с сайтом Новосибирск`, `интеграция 1С Битрикс`, `доработка отчёта 1С` (with local service pages).

### Q3 — Какие запросы дали информационный шум?

**High noise:** `программа 1С не работает`, `ТС ПИОТ 1С настройка`, `Честный знак 1С настройка` (without geo) — DIY guides, vendor blogs, accounting media.

### Q4 — Какие clusters требуют дополнительных формулировок?

- **Urgent help:** add geo + commercial modifiers (`вызов программиста 1С`, `срочно 1С Новосибирск`) — after operator review
- **Labeling:** product-level (Cluster E) + «маркировка под ключ» vs «настройка в 1С»
- **Integrations:** disambiguate «1С программист» vs «Bitrix integrator»
- **ТС ПИОТ:** may need paired commercial queries (`подключить ТС ПИОТ под ключ`, `ЕСМ настройка 1С`)

### Q5 — Разделение между general 1C / marking / integrations / urgent?

**Yes, observable in bounded capture:**

| Segment | SERP character |
|---------|----------------|
| General 1C / support | Local franchisees + companies; commercial landings |
| Integrations | **Different player set** — web studios dominate |
| Marking / ЧЗ | Mix of local vendor (ab-onlinekassa) + free regional center + blogs |
| Urgent troubleshooting | **Informational dominance** — commercial pages minority |

### Q6 — Достаточен ли candidate pool для следующего этапа?

**Sufficient for Stage 2 entry** as **preliminary** pool (21 candidates). **Insufficient** for final competitor registry — requires live SERP validation, recurrence scoring, website/landing passes, operator review.

### Q7 — Источники / запросы для ручной проверки оператором?

**Priority manual review:**

1. All q01–q09 on **live Yandex mobile** (Novosibirsk)
2. Aggregators: Profi.ru, 2GIS, Яндекс Карты for «программист 1С»
3. Ad/promo blocks on head terms
4. `ab-onlinekassa.ru` vs general 1C players for marking overlap
5. Cluster E product queries (11 products) — sample 3–4 first

### Q8 — Можно ли переходить к Website Intelligence и Wordstat?

**Conditionally yes — after OPERATOR REVIEW OF STAGE 1.**

Recommended gate conditions:

- Operator validates SERP grade C → upgrade to B with manual capture (Triumph checklist pattern)
- Approve seed matrix expansions for urgent + Cluster E
- Confirm competitor shortlist for website pass (5–8 local + 2 marking + 2 integration)

**Do not** proceed to ORCA or campaign architecture.

---

## 11. Files Created or Changed

### Created (Corvonero loci only)

| Path |
|------|
| `incoming/mig/pilots/corvonero/corvonero-seed-query-matrix-v1.json` |
| `incoming/mig/requests/request-corvonero-yandex-direct-v1.json` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/session_manifest.json` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/serp_index.json` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/serp_results/q01.json` … `q09.json` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/competitors.json` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/website-surface-snapshot.json` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/source-registry.json` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/review.md` |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/REPORT-mig-research-stage-1-v1.md` |

### Not modified

- `CORVONERO-MIG-RESEARCH-REQUEST-v1.md` (gate text unchanged)
- Triumph / Makita pilots
- ORCA / Website Factory / ATLAS

---

## 12. Validation

| Rule | Pass |
|------|------|
| Research Request exists | Yes |
| JSON valid | Yes |
| session_id unique | Yes (`mig-20260622-corv01`) |
| ATLAS IDs in request | Yes |
| Stage 1 boundary | Yes |
| Market Surface source-backed | Yes (grade C disclosed) |
| No confirmed competitors without evidence | Yes |
| Wordstat not performed | Yes |
| Full Website Intelligence not performed | Yes |
| ORCA absent | Yes |
| SAFE UNKNOWN not converted | Yes |
| Isolated to Corvonero loci | Yes |
| No commit / push | Yes |

---

## 13. Git Status

Run after task: `git status --short` — new untracked files under `incoming/mig/pilots/corvonero/` and `incoming/mig/requests/request-corvonero-yandex-direct-v1.json` only for this task scope.

---

## 14. Recommended Selective Git Scope

When operator chooses to commit (not in this task):

```
incoming/mig/pilots/corvonero/
incoming/mig/requests/request-corvonero-yandex-direct-v1.json
```

Exclude unrelated WIP across repo.

---

## 15. Next Gate

**OPERATOR REVIEW OF MIG RESEARCH STAGE 1**

Operator decisions:

- Approve / amend seed matrix
- Mandate live SERP re-capture (R1/R2)
- Authorize Stage 2: Website Intelligence + Wordstat Demand Surface
- Select competitor shortlist for deep capture

---

## 16. Stop Condition

**STOPPED** per Stage 1 charter.

**Not executed:** Website Intelligence (full), Landing Intelligence, Wordstat, Keyword Registry final, Research Pack approval, ORCA, Website Factory, commit, push.

---

*MIG acquires reality. ORCA interprets reality.*
