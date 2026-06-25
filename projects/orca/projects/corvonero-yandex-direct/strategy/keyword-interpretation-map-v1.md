# Keyword Interpretation Map — Корво Неро v1

**Source:** `keyword_registry.json` (rev 2, 20 seeds + 2364 discovered)  
**Boundary:** Interpretation classes for **future** campaign work — **not** final keywords or negatives

---

## Registry intent_class distribution (seed-level anchor)

| intent_class (registry field) | Approx. entries | ORCA interpretation |
|------------------------------|-----------------|---------------------|
| direct-commercial | 1854 | Core B2B service demand — **future campaign eligible with manual cleaning** |
| commercial-mixed | 510 | Requires noise disambiguation before spend |
| troubleshooting | 19 | Problem-led lane — **test-only** with vacancy controls |
| regulatory | 1 | Strategic exclude unless marking lane isolated |

---

## Semantic class map (ORCA layer)

| Class | Description | Future campaign use | Manual cleaning | Strategic exclude | Test-only |
|-------|-------------|---------------------|-----------------|-------------------|-----------|
| **direct commercial** | Hire/outsource 1C work | **Eligible** (core) | **Required** (head terms) | — | — |
| **problem-based** | «не работает», errors, post-update | Eligible Model C | **Required** | — | Recommended first |
| **service-based** | сопровождение, доработка, аудит | **Eligible** | Moderate | — | — |
| **integration-based** | сайт, обмен, синхронизация, API | Eligible isolated lane | **Required** | Studio-intent rows | Integration test |
| **labeling-based** | маркировка, коды, GIS | Isolated lane only | **Heavy** | Default broad mix | Marking test |
| **configuration-based** | УТ, УНФ, Розница, КА, БП | Eligible in ad extensions / page | Moderate | — | — |
| **informational** | how-to, что такое, инструкция | — | — | **Yes** (strategic) | — |
| **employment** | вакансии, работа, зарплата, резюме | — | — | **Yes** | — |
| **educational** | курсы, обучение, сертификация | — | — | **Yes** | — |
| **software/download** | скачать, torrent, бесплатно | — | — | **Yes** | — |
| **regulatory** | закон, постановление, регламент | — | Heavy | **Yes** unless marking lane | — |
| **ambiguous** | mixed intent, geo-only, brand noise | Case-by-case | **Required** | Partial | Small tests |

---

## Noise classes observed (registry `noise_classes`)

Common tags on seed and related phrases:

| noise_class | Strategic treatment |
|-------------|---------------------|
| job-seeking | **Exclude** at strategy level for B2B campaigns |
| training | **Exclude** |
| salary | **Exclude** |
| remote-work | Review — may be valid for remote service or vacancy |
| informational | **Exclude** or content-only |
| regulatory | Isolate to marking lane or exclude |

Pass A layer aggregates (demand_surface): vacancy_employment_noise 93; training_course_noise 64; regulatory_noise 539.

---

## Seed-level strategic notes (20 seeds — not final keys)

| Seed theme | Wordstat | SERP | ORCA class | Note |
|------------|----------|------|------------|------|
| программист 1С | ingested | r1q01 B | direct commercial + employment noise | Head term — high clean burden |
| услуги программista NSO | ingested | r1q01 | direct commercial | Geo variant |
| сопровождение | ingested | r1q02 B | service-based | Core candidate |
| доработка | ingested | r1q03 B | service-based | Core candidate |
| доработка отчёта | ingested | r1q04 B | service-based | Scoped — good specificity |
| интеграция сайт | ingested | r1q05 B | integration-based | Studio bleed |
| интеграция Битрикс | ingested | r1q06 C | integration-based | CAPTCHA — caution |
| маркировка | ingested | r1q07 C | labeling + regulatory | CAPTCHA — caution |
| Честный знак | ingested | r1q08 B | labeling-based | Specialist lane |
| доработка РМК | **no-result** | — | ambiguous | Use alternatives only after manual verify |
| доработка печатной формы | ingested | — | service-based | Scoped |
| синхронизация | ingested | — | integration-based | Strong semantic — not regional vol |
| программа 1с не работает | ingested | r1q10 B | problem-based | Vacancy noise on SERP |
| срочно программист 1С | **no-result** | — | — | Do not force — use supported alternatives |
| product marking seeds (P3) | ingested | Stage 2 C | labeling-based | Defer breadth |
| ТС ПИОТ | ingested | **no R1** | regulatory / ambiguous | **Defer** |

---

## Classes: campaign eligibility summary

| Eligibility | Classes |
|-------------|---------|
| **Future campaign eligible (with cleaning)** | direct commercial, service-based, scoped task phrases, configuration-based |
| **Requires heavy manual cleaning** | direct commercial head, integration-based, labeling-based, ambiguous |
| **Strategic exclude** | employment, educational, software/download, broad informational, most regulatory |
| **Test-only lanes** | problem-based urgent, labeling-based (Честный знак isolated), integration site |

---

## Explicit non-actions (Stage 1)

- No final keyword list exported
- No minus-word list
- No ad texts
- No Wordstat frequencies used as Novosibirsk forecasts

---

*Map for ORCA Stage 2+ semantic work only.*
