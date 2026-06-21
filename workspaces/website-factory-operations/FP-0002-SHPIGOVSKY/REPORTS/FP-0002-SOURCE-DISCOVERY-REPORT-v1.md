# REPORT — FP-0002 SOURCE DISCOVERY

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Document type:** A0 Source Discovery Report (Full Project Intake)  
**Date:** 2026-06-14  
**Authority:** [website-factory-source-discovery-v1.md](../../../../projects/mars-website-factory/website-factory-source-discovery-v1.md)  
**Scope:** Inventory and registration only — **not** Design Audit, **not** workspace creation, **not** layout analysis.

---

## Scan scope (A0.1)

Paths scanned on disk:

```text
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/          (full tree)
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/
  01_DESIGN/
  02_CONTENT/
  03_BRANDING/
  04_ACCESS/
  05_HOSTING/
  06_WORDPRESS/
  07_NOTES/
  08_CLIENT_MATERIALS/
  09_ARCHIVE/
workspaces/fp-0002-shpigovsky-frontend/                             (adjacent workspace — no design intake)
```

**Scan method:** filesystem walk (`os.walk`), file size verification, XLSX parse (`openpyxl` + `zipfile` XML fallback). PDF binary files **not** opened for visual analysis (out of scope).

**Intake summary:**

| Zone | Files found | Notes |
|------|-------------|-------|
| `INCOMING/01_DESIGN/` | **24 PDF** | Desktop + mobile pairs; Home v2 subfolder; Home v1 superseded |
| `INCOMING/02_CONTENT/` | **1 XLSX** | `Предварит структура и спрос.xlsx` (14 102 bytes) |
| `INCOMING/03_BRANDING/` … `09_ARCHIVE/` | README only | Empty intake — awaiting drop |
| Project root + `REPORTS/` | **33 MD + 4 JSON** | Derived / process artefacts (post-intake) |
| `KNOWLEDGE-EXTRACTION/` | 7 README | Placeholder containers |
| Frontend workspace | 51 files | M1 shell only — **no** `src/assets/design/` intake |

---

## PHASE 1 — SOURCE INVENTORY

### 1.1 Primary intake — design PDFs (Critical)

Visual filenames confirmed via [FP-0002-PAGE-INVENTORY-v1.md](../FP-0002-PAGE-INVENTORY-v1.md) cross-reference and byte-size mapping.

| SOURCE-ID | FILE | LOCATION | TYPE | AUTHORITY | STATUS | PURPOSE |
|-----------|------|----------|------|-----------|--------|---------|
| SOURCE-001 | `2026-06-11-home-v2/Главная страница (v2).pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Home desktop (canonical v2) |
| SOURCE-002 | `2026-06-11-home-v2/Главная страница - моб (v2).pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Home mobile (canonical v2) |
| SOURCE-003 | `Главная стр.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Home desktop v1 (**superseded** by SOURCE-001) |
| SOURCE-004 | `Главная стр - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Home mobile v1 (**superseded** by SOURCE-002) |
| SOURCE-005 | `Услуги хаб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Service hub desktop |
| SOURCE-006 | `Услуги хаб - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Service hub mobile |
| SOURCE-007 | `Услуга подраздел.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Service section template desktop |
| SOURCE-008 | `Услуга подраздел - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Service section template mobile |
| SOURCE-009 | `Услуга конечная.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Service leaf template desktop |
| SOURCE-010 | `Услуга конечная - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Service leaf template mobile |
| SOURCE-011 | `О центре.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — About desktop |
| SOURCE-012 | `О центре - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — About mobile |
| SOURCE-013 | `Контакты.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Contacts desktop |
| SOURCE-014 | `Контакты - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Contacts mobile |
| SOURCE-015 | `Отзывы.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Reviews archive desktop |
| SOURCE-016 | `Отзывы - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Reviews archive mobile |
| SOURCE-017 | `Блог хаб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Blog archive desktop |
| SOURCE-018 | `Блог конечная - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — **misnamed file**; content = blog hub mobile per Page Inventory |
| SOURCE-019 | `Статья.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Blog single desktop |
| SOURCE-020 | `Статья - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — mobile file present; Page Inventory marked PG-009 mobile **Partial** — reconcile at audit |
| SOURCE-021 | `Правовая инфа.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Legal hub desktop |
| SOURCE-022 | `Правовая инфа - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Legal hub mobile |
| SOURCE-023 | `404.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Error page desktop |
| SOURCE-024 | `404 - моб.pdf` | `INCOMING/01_DESIGN/` | PDF | Critical | NOT READ | Visual SSOT — Error page mobile |

**Not on disk (do not register):** `Блог хаб - моб.pdf`, `Блог конечная.pdf` — referenced in Page Inventory ambiguity notes only; **24 PDF files verified**.

### 1.2 Primary intake — structure / content (High)

| SOURCE-ID | FILE | LOCATION | TYPE | AUTHORITY | STATUS | PURPOSE |
|-----------|------|----------|------|-----------|--------|---------|
| SOURCE-025 | `Предварит структура и спрос.xlsx` | `INCOMING/02_CONTENT/` | XLSX | High | **READ** | IA / URL tree / menu levels / search-demand clusters |

### 1.3 Intake placeholders — empty folders (Low)

| SOURCE-ID | FILE | LOCATION | TYPE | AUTHORITY | STATUS | PURPOSE |
|-----------|------|----------|------|-----------|--------|---------|
| SOURCE-026 | `README.md` | `INCOMING/03_BRANDING/` | MD | Low | PARTIALLY READ | Brand assets intake — **empty** |
| SOURCE-027 | `README.md` | `INCOMING/04_ACCESS/` | MD | Low | PARTIALLY READ | Access references intake — **empty** (no secrets) |
| SOURCE-028 | `README.md` | `INCOMING/05_HOSTING/` | MD | Low | PARTIALLY READ | Hosting docs intake — **empty** |
| SOURCE-029 | `README.md` | `INCOMING/06_WORDPRESS/` | MD | Low | PARTIALLY READ | WordPress incoming — **empty** |
| SOURCE-030 | `README.md` | `INCOMING/07_NOTES/` | MD | Low | PARTIALLY READ | Operator notes — **empty** |
| SOURCE-031 | `README.md` | `INCOMING/08_CLIENT_MATERIALS/` | MD | Low | PARTIALLY READ | General client materials — **empty** |
| SOURCE-032 | `README.md` | `INCOMING/09_ARCHIVE/` | MD | Low | PARTIALLY READ | Superseded intake archive — **empty** |

### 1.4 Derived project artefacts — inventories & standards (Medium–High)

Created **after** initial PDF-centric path; **not** substitutes for reading primary intake.

| SOURCE-ID | FILE | LOCATION | TYPE | AUTHORITY | STATUS | PURPOSE |
|-----------|------|----------|------|-----------|--------|---------|
| SOURCE-033 | `FP-0002-PAGE-INVENTORY-v1.md` | project root | MD | Medium | PARTIALLY READ | Page list derived from PDFs; **pre-XLSX** IA gaps |
| SOURCE-034 | `FP-0002-BLOCK-INVENTORY-v1.md` | project root | MD | Medium | NOT READ | Block inventory from design audit path |
| SOURCE-035 | `FP-0002-NUMERIC-DESIGN-RULES-v1.md` | project root | MD | Medium | NOT READ | Numeric extraction v1 |
| SOURCE-036 | `FP-0002-NUMERIC-DESIGN-RULES-v2.md` | project root | MD | Medium | PARTIALLY READ | Numeric rules from 24 PDF (metadata only this session) |
| SOURCE-037 | `FP-0002-DESIGN-APPROVAL-SHEET-v1.md` | project root | MD | Medium | NOT READ | Coordinator approval gate v1 |
| SOURCE-038 | `FP-0002-DESIGN-APPROVAL-SHEET-v2.md` | project root | MD | Medium | NOT READ | Coordinator approval gate v2 |
| SOURCE-039 | `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md` | project root | MD | High | PARTIALLY READ | Production SSOT v1 — Excel **SAFE UNKNOWN** |
| SOURCE-040 | `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v2.md` | project root | MD | High | PARTIALLY READ | Production SSOT v2 — Excel integrated |
| SOURCE-041 | `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` | project root | MD | High | PARTIALLY READ | Production SSOT v3 (**APPROVED**); §10–11 Excel intake read this session |
| SOURCE-042 | `FP-0002-DESIGN-FRONTEND-MAPPING-QA-RECORD-v1.md` | project root | MD | Medium | PARTIALLY READ | Mapping QA; cites XLSX as S4 |
| SOURCE-043 | `FP-0002-FRONTEND-NORMALIZATION-v1.md` | project root | MD | Medium | NOT READ | Normalization pass |
| SOURCE-044 | `FP-0002-FRONTEND-FOUNDATION-v1.md` | project root | MD | Medium | NOT READ | Frontend foundation doc |
| SOURCE-045 | `FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md` | project root | MD | Medium | NOT READ | Production charter |
| SOURCE-046 | `FP-0002-FRONTEND-START-SEQUENCE-v1.md` | project root | MD | Medium | NOT READ | M2 start sequence |
| SOURCE-047 | `FP-0002-M2-FOUNDATION-DEMO-SPEC-v2.md` | project root | MD | Medium | NOT READ | M2 spec (post-reset reference) |
| SOURCE-048 | `FP-0002-EXECUTION-BRAIN-v1.md` | project root | MD | Medium | PARTIALLY READ | Agent execution context |
| SOURCE-049 | `FP-0002-EXCEPTION-REGISTRY-v1.md` | project root | MD | Medium | NOT READ | OL exception registry |
| SOURCE-050 | `FP-0002-PROJECT-PASSPORT.md` | project root | MD | Low | PARTIALLY READ | Project passport |
| SOURCE-051 | `FP-0002-ONBOARDING-READINESS.md` | project root | MD | Low | NOT READ | Onboarding playbook map |
| SOURCE-052 | `WORDPRESS-PRODUCTION-LEARNING-CHARTER.md` | project root | MD | Low | NOT READ | WP learning charter |
| SOURCE-053 | `README.md` | project root | MD | Low | PARTIALLY READ | Project index |
| SOURCE-054 | `PROJECT-STATUS.md` | project root | MD | Low | PARTIALLY READ | Status register |
| SOURCE-055 | `DECISIONS.md` | project root | MD | Low | NOT READ | ADR journal |
| SOURCE-056 | `CHANGELOG.md` | project root | MD | Low | NOT READ | Changelog |

### 1.5 Derived artefacts — REPORTS & extraction JSON (Low–Medium)

| SOURCE-ID | FILE | LOCATION | TYPE | AUTHORITY | STATUS | PURPOSE |
|-----------|------|----------|------|-----------|--------|---------|
| SOURCE-057 | `FP-0002-FOUNDATION-INITIALIZATION-REPORT.md` | `REPORTS/` | MD | Low | PARTIALLY READ | Foundation init 2026-06-11 |
| SOURCE-058 | `FP-0002-RESET-EXECUTION.md` | `REPORTS/` | MD | Low | NOT READ | Reset execution log |
| SOURCE-059 | `FP-0002-RESET-COMPLETE.md` | `REPORTS/` | MD | Low | PARTIALLY READ | PRE-M2 restore evidence |
| SOURCE-060 | `fp0002-numeric-extraction-v2.json` | `REPORTS/` | JSON | Medium | NOT READ | Automated numeric extraction from PDFs |
| SOURCE-061 | `fp0002-numeric-extraction-v2b.json` | `REPORTS/` | JSON | Medium | NOT READ | Numeric extraction iteration |
| SOURCE-062 | `fp0002-numeric-extraction-v2c.json` | `REPORTS/` | JSON | Medium | NOT READ | Numeric extraction iteration |
| SOURCE-063 | `fp0002-component-extraction.json` | `REPORTS/` | JSON | Medium | NOT READ | Component extraction snapshot |

### 1.6 Stale intake READMEs (Low — documentation drift)

| SOURCE-ID | FILE | LOCATION | TYPE | AUTHORITY | STATUS | PURPOSE |
|-----------|------|----------|------|-----------|--------|---------|
| SOURCE-064 | `README.md` | `INCOMING/` | MD | Low | PARTIALLY READ | Intake index — accurate structure |
| SOURCE-065 | `README.md` | `INCOMING/01_DESIGN/` | MD | Low | PARTIALLY READ | **Stale:** states «Empty — Awaiting Intake» while 24 PDF present |
| SOURCE-066 | `README.md` | `INCOMING/02_CONTENT/` | MD | Low | PARTIALLY READ | **Stale:** states «Empty — Awaiting Intake» while XLSX present |

**Total registered sources:** **66** (24 Critical PDF + 1 High XLSX + 41 derived / placeholder / stale docs)

---

## PHASE 2 — AUTHORITY CLASSIFICATION

Classification per [website-factory-source-discovery-v1.md](../../../../projects/mars-website-factory/website-factory-source-discovery-v1.md) §7.

| Authority | Count | SOURCE-IDs |
|-----------|-------|------------|
| **Critical** | 24 | SOURCE-001 … SOURCE-024 (all design PDFs) |
| **High** | 4 | SOURCE-025 (XLSX); SOURCE-039 … SOURCE-041 (Production Standards v1–v3) |
| **Medium** | 17 | SOURCE-033 … SOURCE-038, SOURCE-042, SOURCE-043 … SOURCE-049, SOURCE-060 … SOURCE-063 |
| **Low** | 21 | SOURCE-026 … SOURCE-032, SOURCE-050 … SOURCE-059, SOURCE-064 … SOURCE-066 |

**Rules applied:**

- PDF desktop/mobile = **Critical** (visual SSOT, PDF-only project decision).
- Site structure XLSX = **High** (IA, URLs, menu depth, search demand — not optional).
- Production Standards approvals = **High** as **derived** engineering SSOT (downstream of intake).
- Inventories / extraction JSON = **Medium** (derived; do not override unread Critical/High intake).
- Empty intake READMEs = **Low** (placeholders until material arrives).

---

## PHASE 3 — CONTENT VALIDATION (XLSX)

### SOURCE-025 — `Предварит структура и спрос.xlsx`

**File facts:** 14 102 bytes · modified 2026-06-13 03:34:52 · location confirmed on disk.

**Sheets (2):**

| Sheet | Rows (non-empty) | Columns | Content summary |
|-------|------------------|---------|-----------------|
| **`Структура`** | 53 | URL + 4 hierarchy levels (`1 уровень` … `4 уровень`) | Full site URL tree under `https://shpigovsky.ru/` — services (up to **4 URL levels**), `/specyalisty/` hub + profile slugs, `/o-centre/` + 6 subpages, blog placeholder, contacts, legal hub |
| **`Спрос набросок`** | 53 | Query + `Частотность МСК` | Moscow search-volume clusters for addiction treatment, alcohol, narcotic/substance, behavioral addictions, mental health, RPP, genotyping-related queries |

**Sample `Структура` evidence (parsed this session):**

- L0: `/` — Главная
- L1: `/uslugi/` — Услуги
- L2–L4 service examples: `zavisimosti` → `lechenie-alkogolnoy-zavisimosti`; `lechenie-narkoticheskoy-zavisimosti` → leaf slugs (`soli`, `matadon`, `geroin`, `lek`…); behavioral addiction leaves (`ludomaniya`, `internet-zavisimost`, …)
- Parallel section: `/uslugi/genotipirovanie/`
- `/specyalisty/` + profiles (`shipovsky`, `kazakov`, `kostyuk`, placeholders)
- `/o-centre/` children: `o-nas`, `programma-lecheniya`, `galereya-o-dome`, `specialistam`, `rodstvennikam`, `intervyu-i-smi`
- `/blog/nazvanie-stati/`, `/kontakty/`, `/pravovaya-informaciya-pilzovatelyu//` (typo/double-slash noted)

**Sample `Спрос набросок` evidence:**

- Top volumes: «лечение зависимости» (2666), «лечение алкогольной зависимости» (567), «центр лечения зависимостей» (266), …
- Long-tail substance queries align with L4 service leaves in `Структура`.

**Project impact — decisions that depend on this file:**

| Decision domain | Dependency |
|-----------------|------------|
| **Page inventory completeness** | Full service leaf count, about subpages, specialists section — **beyond 11 PDF templates** |
| **URL / slug SSOT** | Confirmed slugs for nav, breadcrumbs, internal linking, future sitemap |
| **Menu / header targets** | «Специалисты», «Генотипирование» destination URLs |
| **Service IA depth** | Up to **4 levels** under dependencies — deeper than PDF 3-level template assumption |
| **SEO prioritization** | Demand clusters inform content priority (intake only — not SEO implementation here) |
| **Missing pages register** | Confirms M-01 specialists URLs; expands M-05 genotyping URL; reveals about hub children without PDF |

**Why this file must not be skipped:**

- Governs **structural truth** (page graph, URLs) orthogonal to visual PDFs.
- PDF pack shows **templates + examples**, not exhaustive production page set.
- Early PDF-only path produced Page Inventory with «SAFE UNKNOWN» for full service count (§4.2 Page Inventory).

**Risks if absent or unread:**

| Risk | Consequence |
|------|-------------|
| PDF-only IA inference | Under-scoped page inventory; wrong service tree depth |
| Shell / header nav errors | Links to unconfirmed slugs; missing «Специалисты» / genotyping targets |
| Breadcrumb under-spec | 3-level template applied where 4-level paths exist |
| Production Standards gap | v1 marked §10–11 **SAFE UNKNOWN** when file not found |
| Late rework | Foundation / mapping validated without structural SSOT |

**Cross-check:** Detailed intake already captured in SOURCE-041 §10–11 (2026-06-13). This A0 report **independently verifies** file presence and sheet structure.

---

## PHASE 4 — READ STATUS AUDIT

| Status | Count | SOURCE-IDs |
|--------|-------|------------|
| **READ** | 1 | SOURCE-025 (XLSX — both sheets reviewed) |
| **PARTIALLY READ** | 18 | SOURCE-026 … SOURCE-032, SOURCE-033, SOURCE-036, SOURCE-039 … SOURCE-042, SOURCE-048, SOURCE-050, SOURCE-051, SOURCE-053, SOURCE-054, SOURCE-057, SOURCE-059, SOURCE-064 … SOURCE-066 |
| **NOT READ** | 47 | SOURCE-001 … SOURCE-024 (all PDFs); SOURCE-034, SOURCE-035, SOURCE-037, SOURCE-038, SOURCE-043 … SOURCE-047, SOURCE-049, SOURCE-052, SOURCE-055, SOURCE-056, SOURCE-058, SOURCE-060 … SOURCE-063 |

**Honesty notes:**

- **No PDF marked READ** — binary PDFs were not opened for visual/block analysis in this A0 task (explicit restriction: no Design Audit).
- Prior agent sessions may have analyzed PDFs (Page Inventory, numeric JSON), but that work is **not** committed as separate audit REPORT files in-repo (Page Inventory U-10). Status reflects **this register’s evidence rule**, not assumed session memory.
- SOURCE-041 §10–11 content was read **via document cross-reference** → SOURCE-041 = PARTIALLY READ, not full document READ.

**A0 gate per Source Discovery §4–§5:**

| Condition | Verdict |
|-----------|---------|
| Any NOT READ registered source | **FAIL** — 47 sources NOT READ |
| Critical sources all READ | **FAIL** — 24/24 PDFs NOT READ |
| High SOURCE-025 READ | **PASS** |
| High Production Standards docs READ | **FAIL** — PARTIALLY READ only |

---

## PHASE 5 — LOST OR LATE DISCOVERED SOURCES

### SOURCE-025 — `Предварит структура и спрос.xlsx`

| Field | Finding |
|-------|---------|
| **Was absent in early process?** | **YES** — [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md](../FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md) (2026-06-13): file **not found** in workspace; §10–11 **SAFE UNKNOWN** |
| **When found** | File on disk 2026-06-13 03:34:52; integrated in v2/v3 Production Standards same day |
| **Impact** | Page inventory, menu, URL strategy, service depth, specialists section, SEO demand intake |
| **Consequences** | Page Inventory v1 (2026-06-11) built **PDF-only**; full service leaf list and 4-level paths **not** in official page inventory; genotyping URL explicit only after Excel; about subpages absent from inventory |
| **Decisions taken without it** | 11-page PDF inventory; 3-level service tree in Page Inventory §4.1; «количество leaf-услуг — SAFE UNKNOWN»; Production Standards v1 without structural §10–11; Mapping QA initially incomplete for S4 |

### Other late / drift items

| SOURCE-ID | Issue | Impact |
|-----------|-------|--------|
| SOURCE-065, SOURCE-066 | README still «Empty» after intake drop | Operator confusion; false negative in manual intake checks |
| SOURCE-033 | Page Inventory created before SOURCE-025 placement | Structural gaps N-01…N-09 logged only in v2/v3 standards, not Page Inventory amendment |
| Design Intake Audit reports (Page Inventory U-10) | Session artefacts **not** in repo | Lost traceability for early audit scope (likely PDF-only) |

**LOST SOURCES FOUND — YES** (at minimum SOURCE-025 in early v1 path)

---

## PHASE 6 — SOURCE DISCOVERY LAW VALIDATION

Could Phase A0 ([website-factory-source-discovery-v1.md](../../../../projects/mars-website-factory/website-factory-source-discovery-v1.md)) have prevented each loss?

| Case | A0 would prevent? | Explanation |
|------|-------------------|-------------|
| **SOURCE-025 missed in PDF-centric audit** | **YES** | A0.1 mandates `INCOMING/02_CONTENT/` scan; A0.2 registers XLSX as High; SD-06 forbids PDF subsume; gate blocks Design Audit until High source READ |
| **Page Inventory before structural intake** | **YES** | Phase order: A0 → A; Page Inventory is Phase A output consuming register — cannot pass gate with NOT READ SOURCE-025 |
| **Production Standards v1 SAFE UNKNOWN §10–11** | **YES** | A0 completes before Production Standards Draft (Phase B per roadmap); Excel would be READ in A0 |
| **Stale INCOMING READMEs (SOURCE-065/066)** | **PARTIAL** | A0 REPORT lists scanned paths and file counts — exposes README drift; does not auto-fix docs |
| **Uncommitted Design Intake Audit sessions** | **NO** | A0 registers **files**, not chat logs; operator must still commit REPORT artefacts |
| **24 PDFs never individually registered before** | **YES** | SD-02 requires SOURCE-NNN per file; prevents «24 PDF pack» anonymous treatment |

---

## PHASE 7 — PROJECT READINESS

### DESIGN AUDIT READY — **NO**

**Blocking reasons:**

1. **SD-03 / SD-04:** All **Critical** sources (SOURCE-001 … SOURCE-024) are **NOT READ**.
2. **SD-03:** 47 additional sources **NOT READ** (including derived docs — gate requires zero NOT READ on register).
3. Page Inventory (SOURCE-033) predates full structural intake — Design Audit must reconcile PDF + XLSX, not reuse PDF-only inventory alone.

**SOURCE-IDs that must reach READ before Design Audit (minimum set):**

| Priority | SOURCE-IDs | Reason |
|----------|------------|--------|
| **Mandatory Critical** | SOURCE-001 … SOURCE-024 | Visual SSOT — full PDF review |
| **Mandatory High** | SOURCE-025 | IA / URL / demand — already **READ** ✓ |
| **Recommended High** | SOURCE-041 | Current approved Production Standards — full READ for conflict check |
| **Mandatory reconciliation** | SOURCE-033 vs SOURCE-025 | Amend page inventory after both fully consumed |

Empty Low intake folders (SOURCE-026 … SOURCE-032) may proceed with operator waiver for Phase A if no material expected.

---

## PHASE 8 — OPERATOR SOURCE CONFIRMATION

### Complete source list (66 entries)

**INCOMING/01_DESIGN/ — PDF (24):**  
SOURCE-001 … SOURCE-024 — see §1.1 table.

**INCOMING/02_CONTENT/ — XLSX (1):**  
SOURCE-025 — `Предварит структура и спрос.xlsx`

**INCOMING/ — empty zones (7):**  
SOURCE-026 … SOURCE-032 — README placeholders only.

**Project root — derived MD (24):**  
SOURCE-033 … SOURCE-056

**REPORTS/ (7):**  
SOURCE-057 … SOURCE-063 · **this report** (not a registered intake source)

**Stale / index READMEs (3):**  
SOURCE-064 … SOURCE-066

---

Обнаружены следующие материалы проекта.

Подтвердите, что кроме перечисленных источников дополнительных материалов не существует.

Если существуют дополнительные материалы, они должны быть зарегистрированы как новые SOURCE-ID до начала Design Audit.

---

## Scan anomalies & UNKNOWN

| Item | Note |
|------|------|
| `Статья - моб.pdf` (SOURCE-020) | File exists; Page Inventory marks PG-009 mobile partial — reconcile at audit |
| `Блог конечная - моб.pdf` (SOURCE-018) | Known misname — blog hub mobile; `Блог хаб - моб.pdf` **absent** on disk |
| Figma / PNG design exports | **None** in intake — PDF-only project decision |
| `src/assets/design/` in frontend workspace | **Absent** — no exported design folder |
| Coordinator oral facts (Olga 2026-06-13) | Cited in Production Standards — **not** a registered file; SAFE UNKNOWN as standalone SOURCE until documented |

---

## Git status (this task)

- **Created:** `REPORTS/FP-0002-SOURCE-DISCOVERY-REPORT-v1.md`
- **Modified:** none else
- **Commit / push:** not performed

---

SOURCE DISCOVERY COMPLETE — **YES**

DESIGN AUDIT READY — **NO**

LOST SOURCES FOUND — **YES**

UNKNOWN ITEMS:

- Coordinator-provided design facts (colors, Inter, 1170px container) — referenced in SOURCE-039…041 but **no dedicated intake file** registered
- Original «FP-0002 DESIGN INTAKE AUDIT» and «HOME V2 INTAKE UPDATE» session reports — **not** found as files in project tree (Page Inventory U-10)
- Final client branding assets (logos, fonts beyond Inter CDN decision) — folders empty (SOURCE-026)
- Whether `Статья - моб.pdf` is valid mobile SSOT or misfiled — requires PDF READ at Design Audit
