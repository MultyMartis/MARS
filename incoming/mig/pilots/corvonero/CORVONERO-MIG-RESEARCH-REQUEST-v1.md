# MIG Research Request — Корво Неро (v1)

**Artifact type:** formal MIG Research Request (intake postanovka)  
**Status:** **COMPLETE** — MIG research acquisition **COMPLETE WITH ACCEPTED LIMITATIONS** — Research Pack **PUBLISHED** — ORCA handoff **READY FOR ORCA REVIEW** — ORCA strategy **NOT STARTED**  
**Date:** 2026-06-22  
**Lane:** A — Project Execution  
**Intake slug:** `corvonero`  
**Pilot locus:** `incoming/mig/pilots/corvonero/`  
**Canonical intake contract:** [projects/mig/contracts/mig-research-request-contract-v0.md](../../../projects/mig/contracts/mig-research-request-contract-v0.md)  
**Research Pack contract:** [projects/mig/contracts/mig-research-pack-contract-v0.md](../../../projects/mig/contracts/mig-research-pack-contract-v0.md)  
**Runtime assembly:** [projects/mig/contracts/mig-runtime-assembly-v1.md](../../../projects/mig/contracts/mig-runtime-assembly-v1.md)

**Is not:** Research Session, Research Pack, market findings, competitor registry, Wordstat data, SERP capture, ORCA strategy, campaign architecture, landing copy, commit, push.

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

---

## 1. Purpose

Подготовить **формальную постановку** исследования рынка коммерческих услуг 1С и смежных направлений (маркировка, интеграции, доработки, сопровождение) для проекта **Корво Неро — Яндекс Директ и посадочные страницы**.

Документ задаёт **что** MIG должен установить как groundtruth (R1), **в каких границах**, **какими модулями runtime**, и **какой Research Pack** ожидается на выходе — **без** выполнения исследования в этой задаче.

---

## 2. ATLAS context binding (RC-01)

Per [shared/contracts/atlas-context-binding-rule-v1.md](../../../shared/contracts/atlas-context-binding-rule-v1.md) — **references only**; no ownership transfer.

| RC-01 field | ATLAS ID | Value / note |
|-------------|----------|--------------|
| Client organization | **ORG-0009** | Центр автоматизации «Корво Неро» |
| Legal entity | **LE-0006** | ИП Никифоров Роман Вадимович |
| Project | **PRJ-0013** | Корво Неро — Яндекс Директ и посадочные страницы |
| Website | **WEB-CORV-01** | `http://lk.corvonero.ru/` (Tilda) |
| Domain | **DOM-CORV-01** | `corvonero.ru` |
| Vendor context | **ORG-0003** | i-SEO — execution relationship **CLIENT_OF** (REL-0042) |

### Execution relationship (documentation note)

| Topic | Value |
|-------|-------|
| Client of | ORG-0003 / i-SEO |
| PPC executor | Андрей — подрядчик i-SEO (**documentation note only**; no `EXECUTES_PPC_FOR` edge minted in ATLAS v1 taxonomy) |

### SAFE UNKNOWN (ATLAS-adjacent — do not convert in MIG)

| Topic | Status |
|-------|--------|
| Website owner | **SAFE UNKNOWN** |
| Domain registrant | **SAFE UNKNOWN** |
| Official 1C partner status | **SAFE UNKNOWN** |

**Upstream ATLAS report:** [projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md](../../../projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md)

---

## 3. Upstream inputs consumed

| # | Artifact | Role |
|---|----------|------|
| 1 | [workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md) | Operator-confirmed business context, services, commercial terms, constraints |
| 2 | [workspaces/corvonero-yandex-direct/CORVONERO-ATLAS-REGISTRATION-RECOMMENDATION-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-ATLAS-REGISTRATION-RECOMMENDATION-v1.md) | Procedural locus and relationship intent (pre-population) |
| 3 | [workspaces/corvonero-yandex-direct/CORVONERO-PHASE-1-STATUS-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-PHASE-1-STATUS-v1.md) | Phase gates and allowed downstream chain |
| 4 | [projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md](../../../projects/atlas/reports/CORVONERO-ATLAS-REGISTRATION-REPORT-v1.md) | Confirmed ATLAS IDs and relationship correction |
| 5 | [projects/mig/OPERATIONAL-INDEX.md](../../../projects/mig/OPERATIONAL-INDEX.md) | MIG module map and boundaries |
| 6 | Triumph pilot package | **Process precedent only** — [incoming/mig/pilots/triumph-gruzotaxi-krasnodar/](../triumph-gruzotaxi-krasnodar/) |
| 7 | Makita pilot folder | **Process precedent only** — Demand Surface seed discipline; **no** market transfer to 1C |

**Explicit exclusion:** Makita market findings, keywords, competitors, campaign structure, landing decisions **must not** be transferred into the 1C market.

---

## 4. Business context (research framing)

### 4.1 Identity and offer model

| Field | Value |
|-------|-------|
| Commercial name | Центр автоматизации «Корво Неро» |
| Website | `http://lk.corvonero.ru/` |
| Platform | Tilda |
| Audience | юридические лица; индивидуальные предприниматели |
| Operating model | удалённо по региону первого запуска; выезд **только** в Новосибирске |
| Future expansion | города-миллионники, затем вся РФ — **не** входят в приоритет первого исследования, кроме сравнительных выборок |

### 4.2 Geography — first launch vs expansion

| Scope | Geography | Research role |
|-------|-----------|---------------|
| **Primary (first launch)** | Новосибирск; Новосибирская область | **Обязательный** groundtruth для спроса, конкурентов, терминологии |
| **Future expansion** | Краснодар, Екатеринбург, Красноярск, другие миллионники, вся РФ | **Не** объединять с первичной оценкой спроса; только контекст для масштабирования после первого запуска |
| **Optional comparative** | Екатеринбург; Красноярск; Краснодар; nationwide Russia | **Только** при обосновании — pattern evidence; **не** merge в initial demand estimate |

### 4.3 Commercial terms (context — not for publication in research output as approved pricing)

| Topic | Value |
|-------|-------|
| Rate | 3 000 ₽ / час |
| Minimum | 2 часа; минимальный заказ 6 000 ₽ |
| Price on landing pages | **не утверждена** — MIG фиксирует **рыночные** паттерны раскрытия цены, не утверждает публикацию |
| Advertising budget | 100 000 ₽ / месяц |
| Historical ad data | **отсутствуют** |
| Target CPL | **SAFE UNKNOWN** |

### 4.4 Supported 1C configurations (commercial context)

Все перечисленные конфигурации **коммерчески релевантны**, но **ни одна** не должна автоматически стать отдельным рекламным сегментом без evidence:

- 1С:Управление торговлей
- 1С:Управление нашей фирмой
- 1С:Розница
- 1С:Комплексная автоматизация
- 1С:Бухгалтерия предприятия

### 4.5 Proof and trust posture

| Topic | Value |
|-------|-------|
| Systematic case/proof package | **отсутствует** |
| Fabrication prohibition | **Не выдумывать** клиентов, кейсы, сертификаты, результаты, сроки, гарантии |

### 4.6 Current client website

`WEB-CORV-01` (`lk.corvonero.ru`) — **evidence input** для Website / Landing Intelligence; **не** approved landing baseline для будущих кампаний.

---

## 5. Initial service hypotheses

**Governance (binding):** перечень ниже — **operator-confirmed research hypotheses**, **не** approved campaign architecture, **не** приоритет услуг, **не** структура групп объявлений.

MIG обязан проверить каждую гипотезу на спрос, коммерческий интент, конкуренцию и пригодность для первого запуска; слабые гипотезы — в **rejected or weak hypotheses** Research Pack.

### 5.1 Labeling and regulated product processes

- Настройка ТС ПИОТ
- Маркировка напитков
- Маркировка косметики
- Маркировка лекарств
- Маркировка бытовой химии
- Маркировка автозапчастей
- Маркировка масел
- Маркировка техники
- Маркировка пива
- Маркировка воды
- Маркировка строительных материалов
- Маркировка алкоголя
- Подключение маркировки в 1С
- Настройка маркировки в 1С
- Внедрение маркировки в 1С
- Интеграция маркировки с 1С

### 5.2 1C modification tasks

- Расчёт себестоимости в 1С
- Доработка печатной формы 1С
- Доработка отчёта 1С
- Настройка отчёта в 1С
- Доработка РМК в 1С
- Планирование закупок в 1С
- Платёжный календарь в 1С

### 5.3 Integrations

- Интеграция 1С с кассой
- Интеграция 1С с сайтом
- Интеграция 1С с Битрикс
- Настройка синхронизации 1С

### 5.4 Support and troubleshooting

- Сопровождение 1С
- Обновление доработанной 1С
- Программа 1С не работает

---

## 6. Research objectives

MIG **must** establish groundtruth for the following (evidence-backed; gaps → **SAFE UNKNOWN**):

1. **Market structure** for commercial 1C services in Novosibirsk / Novosibirsk Region.
2. **Actual terminology** used by customers (search and on-page language).
3. **Commercial demand** by service group (hypothesis clusters §5).
4. **Demand differences** between:
   - urgent troubleshooting;
   - one-time modification;
   - integration;
   - labeling implementation;
   - regular support.
5. **Search-demand volume and intent** (Demand Surface + Keyword Intelligence — captured, not interpreted).
6. **Service variants** with insufficient or informational-only demand.
7. **Competitive saturation** (supply-side density, ad pressure, aggregator presence).
8. **Competitor offer patterns** (scope, packaging, urgency signals).
9. **Competitor proof and trust patterns** (cases, certificates, reviews, partner badges — observed only).
10. **Price disclosure patterns** in market (not Corvonero approved pricing).
11. **Landing page structures** currently used in the market.
12. Whether **niche labeling pages** outperform **broad 1C programmer pages** conceptually (observation-only comparison — no strategic verdict in pack).
13. Which services **can share one landing page** (evidence-based grouping proposal for ORCA handoff questions — not ORCA decision).
14. Which services **require separate landing pages**.
15. Which services **should not be included in the first launch** (evidence-based exclusion candidates — not final ORCA exclusion).
16. **Risks** created by lack of cases and certificates (market expectation vs client proof gap).
17. **Market-specific terminology** around:
    - Честный знак;
    - ТС ПИОТ;
    - маркировка;
    - integration;
    - update of modified configurations;
    - РМК;
    - reports and print forms.
18. **Potential negative keyword and irrelevant-demand classes** — as **groundtruth only** (informational noise, DIY, vacancies, training, free downloads, etc.); **without** creating final ORCA minus-word lists.

---

## 7. Canonical Research Request parameters (execution-ready summary)

When operator approves execution, Task File Adapter intake **must** normalize to [mig-research-request-contract-v0.md](../../../projects/mig/contracts/mig-research-request-contract-v0.md).

| Field | Planned value |
|-------|---------------|
| `schema_version` | `"0"` |
| `request_id` | `corvonero-yandex-direct-v1` (recommended) |
| `request_type` | `groundtruth_run` |
| `scope.niche` | Коммерческие услуги 1С; маркировка; интеграции; доработки; сопровождение |
| `scope.region` | Новосибирск и Новосибирская область |
| `scope.city` | Новосибирск |
| `scope.business_type` | `b2b_service` (adapter may normalize; not `local_service` — remote-first B2B) |
| `scope.search_engine` | `yandex` |
| `scope.device` | `mobile` (primary SERP context; desktop comparative optional in Human Review Mode) |
| `operator_id` | `human-supervised` |
| `source.adapter` | `task_file` (production) or `cursor` (preparation pass) |

### 7.1 `capture_profile` (required passes for this research)

Per [mig-runtime-assembly-v1.md](../../../projects/mig/contracts/mig-runtime-assembly-v1.md) and pilot precedent [triumph-gruzotaxi-krasnodar](../triumph-gruzotaxi-krasnodar/request-triumph-gruzotaxi-krasnodar-v1-fields.md):

| Key | Value | Runtime phase |
|-----|-------|---------------|
| `multi_query` | `true` | P1 Multi-Query Discovery — service-group coverage |
| `website_pass` | `true` | P3 Website Acquisition |
| `landing_pass` | `true` | P4 Landing Analysis |
| `keyword_pass` | `true` | P-K Keyword Intelligence / Demand Surface |
| `deep_research_pass` | `false` | P5 Deep Research — **out of scope** unless operator charter extends |

**Note:** Runtime MVP may force certain passes off per [resolve-capture-profile.js](../../../projects/mig/lib/runtime/resolve-capture-profile.js) at execution time — operator must verify manifest against this request at session bind.

### 7.2 `queries.seed_queries`

**Not pre-optimized** in this request — MIG must derive seed set from §5 hypotheses + terminology discovery. Minimum expectation:

- mix of **broad** («программист 1с новосибирск», «сопровождение 1с») and **narrow** (маркировка / Честный знак / ТС ПИОТ / интеграция / РМК / отчёт / печатная форма) queries;
- geographic modifier **Новосибирск** or region-appropriate Yandex geo;
- **no** fabricated Wordstat volumes at request stage.

Seed list artifact (future): `corvonero-query-seed-set-v1.json` in this pilot folder — **not created in v1 request task**.

### 7.3 `downstream_context` (operator notes — not ORCA semantics)

```json
{
  "atlas_client_org_ref": "ORG-0009",
  "atlas_legal_entity_ref": "LE-0006",
  "atlas_project_ref": "PRJ-0013",
  "atlas_website_ref": "WEB-CORV-01",
  "atlas_domain_ref": "DOM-CORV-01",
  "vendor_org_ref": "ORG-0003",
  "pilot_label": "Corvonero — 1C services Novosibirsk",
  "service_hypotheses_ref": "CORVONERO-MIG-RESEARCH-REQUEST-v1.md §5",
  "budget_context_rub_month": 100000,
  "operator_mode": "human-supervised"
}
```

---

## 8. Required MIG modules and runtime phases

Use **exact repository terminology**. User-facing groupings map as follows:

| Research need | Canonical MIG module / layer | Primary contracts & artifacts |
|---------------|------------------------------|----------------------------|
| Market structure, SERP, ads, aggregators | **Market Surface** | P1 Search Acquisition → `serp_result.json`; Multi-Query Discovery [mig-multi-query-discovery-design-v0.md](../../../projects/mig/contracts/mig-multi-query-discovery-design-v0.md) |
| Competitor set from SERP | **Competitor Discovery** (not a separate «Competitor Intelligence» product) | P2 → `competitors.json`; [mig-competitor-discovery-contract-v0.md](../../../projects/mig/contracts/mig-competitor-discovery-contract-v0.md) |
| HTTP fetch competitor / client sites | **Website Acquisition** / **Website Intelligence** | P3 → `website_snapshots.json`; [mig-website-acquisition-architecture-v1.md](../../../projects/mig/contracts/mig-website-acquisition-architecture-v1.md) |
| Offer, CTA, trust, page structure | **Landing Analysis** / **Landing Intelligence v2** | P4 → `landing_observations.json`; [mig-landing-analysis-v2.md](../../../projects/mig/contracts/mig-landing-analysis-v2.md); observation families [mig-landing-observation-families-v2.md](../../../projects/mig/contracts/mig-landing-observation-families-v2.md) |
| Wordstat / phrase demand | **Demand Surface** | Manual Wordstat pass; [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](../../../projects/mig/contracts/MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) |
| Terminology and phrase registry | **Keyword Intelligence** → **Keyword Registry** | `keyword_registry.json`, `keyword_observations.json`; [mig-keyword-intelligence-architecture-v1.md](../../../projects/mig/contracts/mig-keyword-intelligence-architecture-v1.md) |
| Trust stack and capture discipline | **Reality Acquisition Model** R1–R4 | [MIG-REALITY-ACQUISITION-MODEL-v1.md](../../../projects/mig/contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md) |
| Per-section and session grades | **Evidence discipline** / **Evidence Grades** | Research Pack § Evidence Grades; session manifest grades |
| Operator sign-off package | **Human Review Mode** → **Human Review Gate** | `evidence/review.md`; pack **Approved By** mandatory before ORCA |
| Draft → approved product | **Research Pack assembly** | P6 → `research_pack.draft.md` → `approved`; [mig-research-pack-contract-v0.md](../../../projects/mig/contracts/mig-research-pack-contract-v0.md) |

**Explicitly excluded modules for this request:**

| Module | Reason |
|--------|--------|
| **Deep Research** (P5) | `deep_research_pass: false` — no LLM synthesis memo as primary groundtruth |
| ORCA interpretation | Downstream only — [mig-orca-handoff-contract-v0.md](../../../projects/mig/contracts/mig-orca-handoff-contract-v0.md) |
| Website Factory | Not in MIG scope |

---

## 9. Competitor scope

Future research **must** cover a **bounded, evidence-based sample** — **without** preselecting final competitor list in this request (no seed URLs unless discovered in SERP / operator charter).

| Segment | Inclusion rule |
|---------|------------------|
| Local Novosibirsk providers | Primary sample |
| Broad «1C programmer» advertisers | Primary sample |
| Labeling / Честный знак specialists | Primary sample |
| Integrations and modified-configuration support | Primary sample |
| Official 1C franchisees | **Only where commercially relevant** in SERP / ads |
| Strong landing pages from other Russian cities | **Secondary** — pattern evidence only; not merged into Novosibirsk demand |

**Do not** fabricate competitor names, domains, or rankings at request stage.

---

## 10. Website scope

Future Website / Landing Intelligence **must** include:

| Target class | Purpose |
|--------------|---------|
| Current Corvonero site (`WEB-CORV-01`) | Baseline observation — not approved template |
| Competitor service pages | Offer, segmentation, message patterns |
| Broad and narrow landing pages | Structure comparison (general 1C vs labeling niche) |
| Mobile commercial presentation | Primary device alignment |
| Offer, price presentation, forms, CTA | Pattern capture |
| Trust, cases, service segmentation | Proof gap analysis input |
| Message match | Query ↔ landing headline/body alignment (observed) |

---

## 11. Demand research boundaries

| Rule | Detail |
|------|--------|
| Initial geography | Новосибирск + Новосибирская область only for **primary** demand estimates |
| Comparative geography | Yekaterinburg, Krasnoyarsk, Krasnodar, nationwide — **optional**, labeled **comparative**; **must not merge** into initial demand estimate |
| Provider discipline | Manual Wordstat export per operator charter — no fabricated frequencies |
| Negative classes | Document **classes** of irrelevant demand as groundtruth; **no** final ORCA negative keyword lists |

---

## 12. Expected Research Pack output

Per [mig-research-pack-contract-v0.md](../../../projects/mig/contracts/mig-research-pack-contract-v0.md) and layer map [research-pack-v1.md](../../../projects/mig/contracts/research-pack-v1.md) (terminology reference — Corvonero pack, not Makita market).

### 12.1 Required sections

| Section | Minimum content |
|---------|-----------------|
| **Pack Metadata** | `pack_id`, `session_id`, `request_id`, dates, `mig_phase`, RC-01 refs |
| **Scope** | Niche, region, city, engine, device |
| **Query Set** | Seed + executed queries; coverage gaps |
| **Market Surface** | SERP summary; ads; aggregators; competitor domains; recurrence |
| **Evidence Grades** | Session + per-section where present |
| **SAFE UNKNOWN** | **Never empty** when gaps exist |
| **Artifact Registry** | Paths to manifest, SERP, competitors, snapshots, keyword files |
| **Human Review Gate** | **Approved By** + date before ORCA handoff |

### 12.2 Required for this project (capture profile)

| Section | Source module |
|---------|---------------|
| **Competitor Observations** | Competitor Discovery |
| **Website Intelligence** | Website Acquisition pass |
| **Landing Intelligence v2** | Landing Analysis pass |
| **Demand Surface** | Wordstat / manual provider snapshot |
| **Keyword Registry** | Keyword Intelligence pass |
| **Terminology findings** | Keyword Registry + Landing observations + SERP snippets |
| **Commercial service clusters** | Evidence-grouped hypothesis clusters — **observations**, not ORCA segments |
| **Rejected or weak hypotheses** | From §5 list |
| **Client site observation** | Landing card for `WEB-CORV-01` |

### 12.3 Each evidence item must record

- evidence sources;
- collection date;
- source URLs or source references;
- evidence grades;
- explicit **SAFE UNKNOWN** where proof is missing.

### 12.4 Boundary statement (mandatory in pack)

Research Pack **must** include explicit separation:

- **MIG groundtruth** — what was observed with evidence grades;
- **Future ORCA interpretation** — campaign architecture, clusters, negatives, bids, landing strategy — **out of pack**.

---

## 13. Research questions for ORCA handoff

MIG **answers with evidence only** — **without** producing strategy, campaign structure, or ads.

| # | Question |
|---|----------|
| Q1 | Which service clusters have **sufficient commercial demand**? |
| Q2 | Which clusters show **urgent intent**? |
| Q3 | Which clusters have **high informational noise**? |
| Q4 | Which can **reasonably support a dedicated landing page**? |
| Q5 | Which need **combined landing pages**? |
| Q6 | Which appear **economically incompatible** with the initial 100 000 ₽/month budget (evidence-based — no CPC/CPL fabrication)? |
| Q7 | Which require **exclusion from the first launch**? |
| Q8 | What market claims are **common** but **cannot be used** without proof (given §4.5)? |
| Q9 | What **terminology** should ORCA use when building campaign architecture? |

ORCA owns all interpretive answers — MIG supplies **observations that inform** these questions.

---

## 14. SAFE UNKNOWN (preserve — do not convert to fact)

MIG may **identify questions or evidence needs** but **must not** convert these into facts in Research Pack:

| Topic | Status |
|-------|--------|
| Target CPL | **SAFE UNKNOWN** |
| Conversion rate | **SAFE UNKNOWN** |
| Lead-to-sale rate | **SAFE UNKNOWN** |
| Average project value | **SAFE UNKNOWN** |
| Customer lifetime value | **SAFE UNKNOWN** |
| Work with VAT | **SAFE UNKNOWN** |
| Team size | **SAFE UNKNOWN** |
| Certificates | **SAFE UNKNOWN** |
| Official 1C partner status | **SAFE UNKNOWN** |
| Operating hours | **SAFE UNKNOWN** |
| Urgent support SLA | **SAFE UNKNOWN** |
| Undesirable lead types | **SAFE UNKNOWN** |
| CRM and call tracking | **SAFE UNKNOWN** |
| Website / domain ownership | **SAFE UNKNOWN** |
| Technical Tilda limitations | **SAFE UNKNOWN** |
| Target CPL (advertising) | **SAFE UNKNOWN** |
| Fabricated Wordstat / CPC / CPL | **PROHIBITED** |

---

## 15. Explicit prohibitions (this request and future session)

**Do not:**

- conduct research in the request-preparation task;
- fabricate demand volume, competitors, Wordstat, CPC, or CPL;
- create campaign structure, keyword groups for launch, or final negative keywords;
- write ads or landing copy;
- prioritize services without evidence;
- modify ORCA, Website Factory, ATLAS, or Business Intake;
- transfer Makita market content into 1C research;
- perform commit or push.

---

## 16. Process precedent (reference only)

Procedural chain validated on other pilots — **no market transfer**:

```text
Business Intake (approved)
  → ATLAS registration (approved)
  → MIG Research Request (this artifact)
  → [operator approval]
  → Research Session (groundtruth_run)
  → Research Pack (draft → review → approved)
  → ORCA strategy / campaign architecture
  → Tilda landing architecture / copy
```

| Pilot | Role |
|-------|------|
| Triumph / Грузотакси / Краснодар | Task File Adapter, `groundtruth_run`, manual SERP, website + landing passes |
| Makita | Demand Surface seed discipline, Keyword Registry — **process only** |

---

## 17. Execution entry point (future — not authorized by this document alone)

After **operator approval of this Research Request**:

1. Derive and operator-review seed query set for §5 hypotheses.
2. Complete manual SERP / Wordstat capture per MIG operator charters.
3. Produce machine-readable `request-corvonero-yandex-direct-v1.json` in this folder (mirror triumph JSON pattern).
4. Drop to production inbox: `incoming/mig/requests/request-corvonero-yandex-direct-v1.json`
5. Run (human-supervised): `.\projects\mig\tools\run-task-file-adapter.ps1`
6. Complete Human Review Mode → Research Pack approval gate.

**This task stops before step 1.**

---

## 18. Approval gates

| Gate | Status |
|------|--------|
| PHASE 0 Preflight | **COMPLETE** |
| PHASE 1 Business Intake | **APPROVED** |
| ATLAS Registration | **APPROVED** |
| **MIG Research Request (this artifact)** | **APPROVED FOR EXECUTION** |
| MIG Research Stage 1 | **COMPLETE** (`session-mig-20260622-corv01`) |
| MIG Research Stage 2 | **AUTHORIZED** — evidence acquisition in progress / operator review pending |
| Research Pack | **NOT APPROVED** |
| ORCA handoff | **BLOCKED** until Research Pack approval |

**Next gate:** **OPERATOR REVIEW OF MIG RESEARCH STAGE 2 AND WORDSTAT MATRIX**

---

## 19. Related paths

| Layer | Path |
|-------|------|
| MIG pilot locus | `incoming/mig/pilots/corvonero/` |
| MIG request inbox (execution) | `incoming/mig/requests/` |
| MIG sessions (output) | `projects/mig/sessions/` |
| ORCA project locus (future) | `projects/orca/projects/corvonero-yandex-direct/` |
| Workspace intake | `workspaces/corvonero-yandex-direct/` |

---

*CORVONERO MIG Research Request v1 · 2026-06-22 · intake postanovka only · no market findings*
