# I-SEO Report Hub — Nikita Taxonomy v0.1

**Status:** CHARTER / EXTRACTION — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Nikita Report Template Data Model Charter 01  
**Corpus:** `X:\AI MARS STORAGE\incoming\iseo-report-hub\materials from Nikita\`

**Security:** Credential / access sheet content is **excluded**. Values from access sheets (passwords, logins, raw counters/tokens, mail-share instructions as credentials) are **not** reproduced. Category label «Доступы» is noted only as **non-report operational** material.

---

## 1. Source files

| # | Path (under corpus) | Type | Confidence | Extraction |
|---|---------------------|------|------------|------------|
| 1 | `Общий список работ.docx` | Work catalogue + «для чего / что выполнено» narratives | **HIGH** | OOXML `word/document.xml` → 548 non-empty text lines |
| 2 | `План работ по Интернет-магазину.xlsx` | 12-month ecommerce work plan | **HIGH** | `sharedStrings` + sheet names (Лист1/Лист2); Лист2 access **excluded** |
| 3 | `План работ по сайту услуг.xlsx` | 12-month services-site work plan | **HIGH** | Same method; access sheet **excluded** |

Evidence terms seen: «Старт проекта», «Аналитика», «Техмониторинг», «Ссылочное продвижение», «Семантика», «коммерческими факторами», «Текстовая оптимизация», «внешним ПФ», «внутренними ПФ», «OnPage», «SERM», «Отчеты», «Ежемесячная отчетность», «Количественные плановые работы», «Месяц 1…12», «Базовая оптимизация», «Внешняя и точечная оптимизация».

---

## 2. What these files are

| Claim | Evidence |
|-------|----------|
| SEO **work catalogue / 12-month plan** | Month columns; work checklists; quantity plans |
| **Not** finished client PDF form | No client section layout schema; «Ежемесячная отчетность» is a thin heading |
| Dual site profiles | Separate XLSX for shop vs services |
| Narrative templates for client-safe explanations | DOCX «Для чего выполняется» / «Что выполнено» per numbered work item |

---

## 3. Normalized top-level taxonomy

Order follows DOCX / XLSX category sequence. Cadence/visibility/fill modes are **inferred lightly**; marked where SAFE UNKNOWN.

| Code | Category (RU) | Cadence (inferred) | Site applicability | Visibility default | Fill mode default | Evidence required |
|------|---------------|--------------------|--------------------|--------------------|-------------------|-------------------|
| `project_start` | Старт проекта | one-time + refresh | both | internal + client-safe summaries | manual | often yes (access/config checks) |
| `analytics` | Аналитика | recurring / monthly | both | internal; client-safe findings | manual; later AI draft for narrative | yes for competitor claims |
| `tech_monitoring` | Техмониторинг | recurring / as-needed | both | internal; client-safe issues | manual | yes (audit artifacts) |
| `link_building` | Ссылочное продвижение | recurring | both | internal; optional client summary | manual | yes |
| `semantics` | Семантика | one-time + recurring | both | internal; client-safe plan notes | manual | yes for core approval |
| `commercial_factors` | Коммерческие факторы | as-needed / phased | both | internal; client-safe | manual | yes (TZ) |
| `text_optimization` | Текстовая оптимизация | recurring | both (item deltas by type) | internal; client-safe | manual | yes (TZ/pages) |
| `external_behavioral` | Внешний ПФ | recurring / as-needed | both | mostly internal | manual | optional |
| `internal_behavioral` | Внутренний ПФ | as-needed | both | mostly internal | manual | optional |
| `onpage` | OnPage / точечная оптимизация | recurring | both | internal; client-safe | manual | yes |
| `serm` | SERM | as-needed / recurring | both | internal; careful client wording | manual | yes |
| `reporting` | Отчеты / ежемесячная отчетность | monthly | both | client-facing process | manual (+ later AI draft) | n/a |
| `quantitative_plan` | Количественные плановые работы | monthly/quarterly quotas | **differs by site type** | internal planning; client volume summary optional | manual / planned counts | optional |
| `access_ops` | Доступы (operational) | onboarding | both | **internal only — never report content** | manual | n/a — **exclude from hub report model** |

---

## 4. Per-source detail

### 4.1 `Общий список работ.docx`

**Type:** master work list + explanation templates.  
**Categories:** all taxonomy rows above except quantitative quotas table (DOCX lists related content/link volume items in SERM/adjacent sections).  
**Work item examples (sample):** карта редиректов; счётчики ЯМ/ЯВ/GSC/GA; CMS admin check; tech files; strategy; niche study; tech audit; link types; semantic core; commercial factors TZ; text optimization for services/solutions/catalog/articles; CTR/snippets; usability; OnPage; SERM placements.  
**Cadence:** not week-structured; item-level one-time vs iterative language («Итерационный…», «Актуализация…»).  
**Client/internal:** «Для чего / Что выполнено» text is **client-safe narrative style**; technical depth may still need filtering.  
**Required vs optional:** not formally marked; satellites/drops marked «при необходимости».

### 4.2 `План работ по Интернет-магазину.xlsx`

**Type:** 12-month ecommerce plan (Лист1 works; Лист2 access excluded).  
**Phase bands:** «Базовая оптимизация» / «Внешняя и точечная оптимизация» + Месяц 1–12 + «Актуализация».  
**Quantitative examples (shop):** добавление категорий; добавление тегов; статьи **7000** символов*; контент в категории **3000** символов*; коммерческие/естественные ссылки; ТЗ на ком. факторы и техчасть.  
**Note:** `*` — со второго месяца (месяц 1 забирают техправки/настройки/robots-sitemap/семантика/аналитика).  
**Client/internal:** plan is specialist/planning; reporting named but thin.

### 4.3 `План работ по сайту услуг.xlsx`

**Type:** parallel 12-month services plan.  
**Overlap with shop:** category tree and most work items **very high overlap** in shared strings.  
**Documented deltas (safe strings):**  
- статьи **5000** символов* (vs 7000 shop);  
- «Добавление структурных страниц (контент 3000 символов)» (shop emphasizes categories/tags/category content);  
- «Внутренняя перелинковка (2-3 со страницы)» explicit in services strings;  
- monthly quantity phrases present (e.g. «20 в месяц», «7 в месяц», «7 страниц в месяц», «6 в месяц») — exact mapping of which row owns which count is **SAFE UNKNOWN** without cell-level OCR/formula walk;  
- example project label appears in plan subtitle (services file) — treat as **example**, not product fixture requirement.

---

## 5. Ecommerce vs service-site differences (evidence-based)

| Dimension | Ecommerce XLSX | Services XLSX | Confidence |
|-----------|----------------|---------------|------------|
| Category taxonomy | Same major categories | Same | HIGH |
| Catalog/category content volume | categories, tags, category texts 3000, articles 7000 | structural pages 3000, articles 5000 | HIGH |
| Interlinking string | present in OnPage group | explicit «2-3 со страницы» | MEDIUM–HIGH |
| Month 1–12 scaffolding | Yes | Yes | HIGH |
| Exact month×task matrix cell diffs | Not fully extracted | Not fully extracted | **SAFE UNKNOWN** |

Hub `project_type` mapping recommendation (charter, not impl):

- ecommerce plan → `ecommerce`  
- services plan → `service_corporate`  
- other enum values remain architecture-only until more Nikita evidence

---

## 6. Implications for Report Hub

1. Taxonomy is the SoT for **work items**, not for PDF chrome.  
2. «Отчеты / Ежемесячная отчетность» justifies a monthly **reporting** process entity already present — but not field schema.  
3. Quantitative quotas should be **optional planned targets**, not mandatory client PDF sections on day 1.  
4. Access sheet → **integration/secrets concern**, never report blocks.  
5. DOCX «Для чего / Что выполнено» is a strong pattern for future **client_summary** + **description** fields on work entries.

---

## 7. Normalized category codes (seed-ready keys)

Suggested stable codes for future seed (implementation wave):

`project_start`, `analytics`, `tech_monitoring`, `link_building`, `semantics`, `commercial_factors`, `text_optimization`, `external_behavioral`, `internal_behavioral`, `onpage`, `serm`, `reporting`, `quantitative_plan`

Do **not** seed `access_ops` into client-visible catalogue.

---

## 8. SAFE UNKNOWN

- Full cell-level month×task matrices and formulas.  
- Whether every DOCX numbered item is meant to appear monthly or only once per engagement.  
- Whether Nikita expects quantitative quotas on the client report face.  
- Authority weight of Denis/Ilya PDFs vs Nikita plans for **section titles** (prior discovery: triangulate later).  
- Exact meaning of «3 штуки» quantity string without sheet coordinates.
