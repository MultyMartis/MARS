# MIG Research Pack — APPROVED

## Pack Metadata

| Field | Value |
|-------|-------|
| pack_schema_version | 0 |
| pack_id | mig-20260622-corv01 |
| session_id | mig-20260622-corv01 |
| request_id | corvonero-yandex-direct-v1 |
| mig_phase | 2 |
| pack_state | published |
| created_at | 2026-06-22T12:30:00.000Z |
| published_at | 2026-06-22 |
| operator_id | human-supervised |
| Approved By | operator-delegated-cursor-session |
| Approval date | 2026-06-22 |

**Contracts:** [mig-research-pack-contract-v0.md](../../../../projects/mig/contracts/mig-research-pack-contract-v0.md) · [research-pack-v1.md](../../../../projects/mig/contracts/research-pack-v1.md)

**Boundary:** MIG acquires reality. ORCA interprets reality. This pack contains **no** campaign structure, ad groups, budgets, or landing architecture.

---

## 1. Executive evidence summary

### Investigated

Commercial 1C services market in **Новосибирск / Новосибирская область**: broad programmer/support/modification, reports/forms, integrations, marking/Честный знак, product labeling, troubleshooting, RMK, TS PIOT — for **PRJ-0013 Корво Неро** Yandex Direct initiative.

### Scope

| Dimension | Value |
|-----------|-------|
| Niche | Коммерческие услуги 1С; маркировка; интеграции; доработки; сопровождение |
| Region | Новосибирск + Новосибирская область |
| Search engine | Yandex |
| Device | mobile (primary SERP) |
| Wordstat geography | **All Russia** (Pass A broad semantic — separate layer) |

### Source classes

| Class | Grade | Coverage |
|-------|-------|----------|
| Stage 1 SERP | C | 9 seed queries |
| Stage 2 live SERP | C | 27 queries |
| R1 priority SERP (zpm-workflow) | **B_partial** | **7/10** Grade B |
| Wordstat Pass A | B_semantic_discovery | 20 seeds → 18 Excel + 2 no-result → 2399 rows |
| Wordstat Pass B | N/A | **NOT REQUIRED BY OPERATOR** |
| Competitor shortlist | B | 9 objects |
| Website / Landing intelligence | B | 7 competitors + Corvonero site |
| Keyword Registry | reviewed rev 2 | 20 seeds + 2364 discovered phrases |

### Key limitations

- R1 SERP **7/10** — r1q06, r1q07 CAPTCHA Grade C; **r1q09 not captured**
- Nationwide Wordstat **≠** Novosibirsk regional demand volume
- CPC, CTR, conversion, CPL, lead quality — **SAFE UNKNOWN**
- No campaign or landing decisions in this pack

---

## 2. Business and project context

| Topic | Evidence |
|-------|----------|
| Client | Центр автоматизации «Корво Неро» (ORG-0009) |
| Legal entity | ИП Никифоров Роман Вадимович (LE-0006) — intake only; not on public site |
| Execution | i-SEO (ORG-0003) — CLIENT_OF relationship |
| Service direction | 1C implementation, support, modifications, integrations, marking, equipment |
| Budget context (intake) | ~100 000 ₽ test budget — **not** allocation in this pack |
| Commercial terms (intake) | 3000 ₽/hour; 6000 ₽ minimum (2h) — site shows hourly; minimum not explicit on site |
| Current site | Tilda single page — `http://lk.corvonero.ru/` (WEB-CORV-01) |
| Approval roles | Operator / i-SEO — human gates before ORCA |

**Intake ref:** `workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md`

---

## 3. Market Surface

Observed provider types in Novosibirsk SERP and shortlist (evidence only):

| Class | Examples |
|-------|----------|
| Local 1C companies | Shift Company, Vigyana, Profinfoservice |
| Franchisees / partners | Avanta Pro, ITLlekt |
| Integration web studios | YAL Studio |
| Labeling / kassa specialists | AB OnlineKassa |
| Aggregators / boards | hh.ru, zarplata.ru, gorodrabot.ru |
| Informational / regulatory | ITS, vendor docs, course providers |
| Vacancy noise | Head «программист 1С» queries |

**Artifact:** `competitors-shortlist-confirmed.json`, `website_intelligence.json`

---

## 4. Competitor shortlist

| Role | Count | Note |
|------|-------|------|
| Confirmed local/segment competitors | 7 | Bounded website intelligence performed |
| Pattern references | 2 | SERP recurrence patterns — not full fetch |
| Excluded | aggregators, job boards, pure courses | Documented in shortlist policy |

Competitor **claims** (partner status, SLA, prices) are **observed on pages** — **not verified** by MIG.

---

## 5. Website Intelligence (summary)

Observable patterns from fetched competitor pages:

- **Positioning:** mix of broad 1C hubs vs narrow modification/report/integration/marking pages
- **Prices:** hourly (1500–3000 ₽ range observed) and task tables on modification pages
- **SLA:** 24/7 claims on some support/marking pages — **unverified**
- **Trust:** reviews on some sites; cases/certificates often absent
- **Specialization:** marking specialists with explicit commercial landings vs generic 1C studios

**Artifact:** `website_intelligence.json`

---

## 6. Landing Intelligence (summary)

| Page role | Evidence |
|-----------|----------|
| Broad 1C service | Avanta Pro programmer hub — medium specificity |
| Modification/report | ITLlekt — high price table density |
| Integration | YAL Studio — web-studio framing |
| Marking | AB OnlineKassa — local marking landing with prices |
| Corvonero current | Single universal Tilda page — see §11 |

**Artifact:** `landing_intelligence_v2.json` — **evidence only**, not landing architecture.

---

## 7. Wordstat semantic evidence (Pass A)

| Metric | Value |
|--------|-------|
| Seeds attempted | 20 |
| Excel ingested | 18 |
| No-result seeds | 2 (`доработка РМК`, `срочно программист 1С`) — **not numeric zero** |
| Normalized rows | 2399 |
| Mode | broad unquoted, all Russia |
| Commercial vocabulary rows | ~2382 (classification in demand_surface) |
| Employment/training noise | present in head terms |
| RMK alternatives | documented in demand_surface (e.g. «1с рмк честный знак») |
| Urgent alternatives | «программа 1с не работает» supported; «срочно программист 1С» no-result |

**Full row dump:** `wordstat-collection-normalized.json` — **not reproduced here**.

**Limitation:** National broad counts **must not** be used as Novosibirsk traffic forecasts.

---

## 8. Regional SERP evidence (R1)

| r1_id | Query | Grade | Status |
|-------|-------|-------|--------|
| r1q01 | программист 1С Новосибирск | **B** | captured |
| r1q02 | сопровождение 1С Новосибирск | **B** | captured |
| r1q03 | доработка 1С Новосибирск | **B** | captured |
| r1q04 | доработка отчёта 1С Новосибирск | **B** | captured |
| r1q05 | интеграция 1С с сайтом Новосибирск | **B** | captured |
| r1q06 | интеграция 1С Битрикс Новосибирск | **C** | CAPTCHA |
| r1q07 | маркировка в 1С Новосибирск | **C** | CAPTCHA |
| r1q08 | Честный знак 1С Новосибирск | **B** | captured |
| r1q09 | настройка ТС ПИОТ | — | **not captured** |
| r1q10 | программа 1С не работает Новосибирск | **B** | captured |

**Captures:** `evidence/serp/zpm-workflow-corv01/capture-run/captures/{r1q}/` — PNG, HTML, JSON for attempted queries.

**Composition notes (Grade B):** commercial provider pages, franchise ads, vacancy blocks on head terms, course ads on programmer query.

---

## 9. Demand Surface — cluster verdicts

| Cluster | Verdict |
|---------|---------|
| Broad programmer / general 1C | conditionally_supported |
| Support | conditionally_supported |
| Modifications | supported |
| Reports and print forms | supported |
| Website integration | supported |
| Bitrix integration | mixed (R1 CAPTCHA) |
| Cash register / sync | conditionally_supported (no R1 query) |
| Generic labeling | mixed (R1 CAPTCHA) |
| Честный знак | supported |
| Product-specific labeling | conditionally_supported |
| Troubleshooting | mixed (vacancy noise) |
| RMK | weak (no-result seed) |
| TS PIOT | defer (r1q09 not captured) |

**Artifact:** `demand_surface.json` → `cluster_evidence_verdicts`

---

## 10. Keyword Registry summary

| Metric | Value |
|--------|-------|
| Seed entries | 20 |
| Discovered phrases | 2364 |
| Registry revision | 2 |
| Evidence classes | Wordstat-only, SERP-only, R1+Wordstat, cluster-supported, captcha-blocked, defer |

**ORCA-eligible candidates:** seed and discovered entries marked `eligible_with_volume_unknown` or `requires_orca_interpretation` — **not final ad keywords**.

**Artifact:** `keyword_registry.json`

---

## 11. Current Corvonero site — gap analysis (evidence-based)

| Gap | Evidence |
|-----|----------|
| Broad single page vs specialized market pages | One Tilda landing vs competitor narrow pages |
| Configurations not named on site | Intake lists five; site generic |
| Minimum order not visible | 6000 ₽/2h in intake; not on page |
| Weak proof package | No cases, certificates, reviews, partner badge |
| Marking breadth | Generic mention vs intake product list |
| Form present | Name, phone, task description required |

**Artifact:** `website-corvonero-intelligence.json`

---

## 12. ORCA handoff questions

1. Which service clusters deserve **separate PPC treatment** given 100k ₽ test budget?
2. Should **broad** and **specialized** campaigns be separated?
3. How does budget constrain **breadth vs depth**?
4. Should **integrations** (site/Bitrix) be isolated campaigns?
5. Should **labeling/Честный знак** be isolated from general 1C?
6. How to handle **troubleshooting** intent (vacancy noise, mixed commercial value)?
7. Should **TS PIOT** be deferred given missing R1 capture?
8. Which Wordstat phrases are **useful but too informational** for paid search?
9. What **site/landing changes** are required before paid traffic?
10. Can **current Tilda** support intended multi-cluster structure?
11. What **proof gaps** materially affect launch readiness?
12. Should **3000 ₽/hour and 6000 ₽ minimum** be shown in ads/landings (intake says prices not approved for ads)?

**These are questions for ORCA — not MIG decisions.**

---

## 13. SAFE UNKNOWN

- CPC, CTR, conversion rate, CPL, qualified-lead rate, sale conversion
- Average project revenue, profitability
- Exact regional search volume (Pass B not required)
- Competitor ad spend and lead quality
- Effectiveness of current Corvonero page
- Achievable lead count
- VAT status
- Verified cases, certificates, official partner status
- Shift Company website (fetch timeout — SERP-only)

---

## Artifact Registry

| Key | Path |
|-----|------|
| session_manifest | `session_manifest.json` |
| demand_surface | `demand_surface.json` |
| keyword_registry | `keyword_registry.json` |
| serp_r1_index | `serp_r1_index.json` |
| competitors_shortlist | `competitors-shortlist-confirmed.json` |
| website_intelligence | `website_intelligence.json` |
| landing_intelligence | `landing_intelligence_v2.json` |
| corvonero_site | `website-corvonero-intelligence.json` |
| wordstat_normalized | `wordstat-collection-normalized.json` |
| source_registry | `evidence/source-registry.json` |
| human_review_gate | `human_review_gate.approved.md` |
| orca_handoff | `handoff/orca-evidence-handoff-v1.json` |

---

## Evidence Grades (session)

| Layer | Grade |
|-------|-------|
| Session composite | B_partial |
| Wordstat Pass A | B_semantic_discovery |
| R1 SERP | B_partial (7/10) |
| Stage 1/2 SERP | C |
| Competitor / Website / Landing | B |

---

*Approved Research Pack — ready for human-delivered ORCA intake. ORCA strategy NOT STARTED.*
