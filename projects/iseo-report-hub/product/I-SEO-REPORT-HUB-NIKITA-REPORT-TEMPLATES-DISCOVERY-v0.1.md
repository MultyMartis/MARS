# I-SEO Report Hub — Nikita Report Templates Discovery v0.1

**Status:** DISCOVERY ONLY — no implementation / no DB migration in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-07  
**Wave:** UI Screenshot QA, Brand Style and Nikita Templates Discovery 01  
**Corpus root:** `X:\AI MARS STORAGE\incoming\iseo-report-hub\materials from Nikita\`

**Security:** Nikita XLSX **Лист2** contains access/credential-related material — **excluded** from product mapping and must not be copied into hub UI, fixtures, PDF, or prompts. Values are not reproduced here.

---

## 1. Candidates

| # | Path | Type | Why Nikita | Evidence | Confidence |
|---|------|------|------------|----------|------------|
| 1 | `…/materials from Nikita/Общий список работ.docx` | `.docx` | Folder + OPERATIONAL-INDEX (3 Nikita materials) | Work catalog: Старт проекта, Аналитика, Техмониторинг, Семантика, Ссылочное, SERM, … + «для чего / что выполнено» explanations | **HIGH** |
| 2 | `…/materials from Nikita/План работ по Интернет-магазину.xlsx` | `.xlsx` | Same folder | Sheets Лист1/Лист2; months 1–12; work blocks; «Ежемесячная отчетность»; ecommerce-oriented tasks | **HIGH** |
| 3 | `…/materials from Nikita/План работ по сайту услуг.xlsx` | `.xlsx` | Same folder | Parallel structure to #2 for services site profile | **HIGH** |

**Also related (not Nikita-authored templates, but field architecture):**

| Doc | Role | Confidence |
|-----|------|------------|
| `product/I-SEO-REPORT-HUB-REPORT-CONTENT-ARCHITECTURE-v0.1.md` | 13-block monthly + weekly flow (product architecture) | HIGH as architecture, not Nikita file |
| Denis / Ilya PDF reports under `incoming/iseo-report-hub/reports from *` | Real delivered report examples | HIGH as examples; separate from Nikita work plans |

No additional Nikita `.docx/.xlsx` matches found under `projects/iseo-report-hub/` beyond references to the STORAGE corpus.

---

## 2. Extraction method

| File | Method | Result |
|------|--------|--------|
| DOCX | Expand OOXML → `word/document.xml` → text | **OK** — 548 lines / ~47k chars UTF-8 |
| XLSX ×2 | Expand → `sharedStrings.xml` + sheet names | **OK** — structure + work strings; **Лист2 credentials present** (not exported) |

---

## 3. What these files are (important)

Nikita materials are primarily **SEO work catalogues / monthly work plans** (what specialists do over months 1–12), **not** a finished client-facing monthly report form with filled KPI tables.

They **do** define:

- Work categories and atomic tasks (source of truth for «что делали»).  
- Two site profiles: **интернет-магазин** vs **сайт услуг**.  
- An **«Отчеты / Ежемесячная отчетность»** heading (thin — no detailed client PDF field schema inside XLSX shared strings).  
- Quantitative planned works (content/links volumes).  
- Explicit **access** sheet (credentials) — operational, **not** report content.

They **do not** fully define (SAFE UNKNOWN / deferred):

- Exact client PDF section titles and layout.  
- Required KPI table columns for monthly client report.  
- AI vs manual fill split.  
- Weekly checkpoint form fields 1:1.

For client report **narrative structure**, continue using Report Content Architecture (13 blocks) + future Client Report Template wave + sample PDFs from Denis/Ilya — **triangulated** with Nikita work taxonomy.

---

## 4. Report types inferred

| Type | Present in Nikita files? | Notes |
|------|--------------------------|-------|
| Weekly checkpoint | Indirect | Plans are monthly/phase; weekly cadence not explicit form |
| Monthly internal work plan | **Yes** | Месяц 1–12 columns; work checklist |
| Monthly client-facing report | Partial | «Ежемесячная отчетность» named; field schema thin |
| Specialist workspace checklist | **Yes** | Core of DOCX/XLSX |
| Review/approval checklist | No | Not found |
| Access / credentials handoff | **Yes (Лист2)** | **Exclude from product corpus** |

---

## 5. Work taxonomy (section order from DOCX / XLSX)

Canonical work groups (order approximately as in materials):

1. **Старт проекта** — redirects map, counters (ЯМ/ЯВ/GSC/GA+goals), CMS admin, catalogs/geo, tech files, strategy, plan актуализация  
2. **Аналитика** — niche, traffic volume/quality, competitors, leaders, link profiles, site structure, commercial factors, hypotheses, media plan, conversion tools, strategy refresh  
3. **Техмониторинг** — basic/deep tech audit, webmaster monitoring, parser, indexing, robots/sitemap/URL/duplicates/404, forms/events, speed/AMP, TZ for fixes, indexing process  
4. **Ссылочное продвижение** — article/catalog/crowd/profile links, social signals, satellites/drops if needed, internal weight analysis  
5. **Семантика** — core collection, approval, position monitoring service, visibility, new landings, clustering, expansion, competitor semantics, scoring  
6. **Коммерческие факторы** — TZ from audit, page types, service pages, menu, 404  
7. **Текстовая оптимизация** — landings/solutions/catalog/articles; meta; alt; TZ for copywriters  
8. **Внешний ПФ** — CTR, snippets, microdata, metadata attractiveness  
9. **Внутренний ПФ** — usability, UX TZ, attention hypotheses  
10. **OnPage / точечная оптимизация** — meta, interlinking, page links, snippets, page content  
11. **SERM** — reputation / reviews / third-party mentions  
12. **Отчеты** — ежемесячная отчетность (named)  
13. **Количественные плановые работы** — categories/tags/articles/content/commercial+natural links/TZ batches  

Profile deltas (shop vs services) exist in the two XLSX files (e.g. catalog vs services page emphasis) — exact cell diffs **SAFE UNKNOWN** beyond shared-string overlap (very high overlap).

---

## 6. Field mapping vs current hub blocks

Current hub monthly content fields / block keys:

`executive_summary`, `work_completed`, `results_summary`, `key_findings`, `risks_and_blockers`, `next_month_plan`

| Current key | Nikita / architecture fit | Action |
|-------------|---------------------------|--------|
| `executive_summary` | Needed for client narrative; not in Nikita XLSX as named field | **Keep** + RU label; later enrich |
| `work_completed` | **Strong match** to work taxonomy | **Keep**; later **split** by Nikita categories / profile |
| `results_summary` | Maps to analytics/positions/traffic/leads outcomes | **Keep**; later **split** → positions / traffic / leads |
| `key_findings` | Partial overlap with «точки роста» / competitor insights | **Rename** toward «Что изменилось» / findings |
| `risks_and_blockers` | Tech/content/client blockers implied | **Keep** |
| `next_month_plan` | Matches plan актуализация + next month columns | **Keep** |
| *(missing)* KPI snapshot | Architecture Block 3; Nikita KPI mentioned at start | **Add** later |
| *(missing)* Technical SEO block | Techмониторинг group | **Add** later (or structured under work) |
| *(missing)* Semantic/content block | Семантика + тексты | **Add** later |
| *(missing)* Links/authority | Ссылочное | **Add** optional |
| *(missing)* Evidence/appendix | Not in Nikita plan files | **Add** later |
| *(missing)* Profile-specific blocks | Shop vs services XLSX | **Add** with project type |
| *(missing)* Manual vs AI flags | Not in files | **Add** in template charter |

**Verdict:** Current 6 keys are a **thin generic shell**. They are **not** sufficient for Nikita-faithful specialist entry. **DB/schema migration likely required** in a later template data-model wave — **not** in UI Impl 03.

---

## 7. Manual vs AI (planning only)

| Fill mode | Candidates |
|-----------|------------|
| Manual SEO specialist | Work completed (by category), blockers, plan, interpretation, client actions |
| Semi-auto / AI-assist later | Executive summary draft, results narrative from metrics, clustering notes |
| System / integration later | Positions, traffic, leads KPI tables (Topvisor/Metrika — out of scope now) |
| Never in report content | Credentials / access sheet |

---

## 8. Implications for next waves

1. **Impl 03:** RU labels for existing 6 fields only; do not migrate schema.  
2. **Nikita Report Template Data Model Charter 01:** map taxonomy → blocks/fields; shop vs services profiles; weekly vs monthly; client vs internal visibility.  
3. **Client Report Template Visual Alignment Charter 01:** PDF/HTML chrome to brand + Nikita/architecture sections.  
4. Keep Denis/Ilya PDFs as **examples**, Nikita XLSX/DOCX as **work SoT**, architecture doc as **narrative skeleton**.

---

## 9. SAFE UNKNOWN

- Full cell-level differences between shop vs services XLSX beyond shared strings.  
- Whether «Ежемесячная отчетность» has a hidden structured sheet beyond shared strings (payload may be formula-driven).  
- Exact client report layout Nikita expects visually (no Nikita PDF template found in folder).  
- Whether operator considers Denis/Ilya PDFs equal authority to Nikita for section titles.
