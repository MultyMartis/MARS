# REPORT — FP-0002 FIGMA FORENSIC TEST v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-17  
**Task type:** Forensic analysis only (structure / extractability / Factory fitness)  
**Source file:** `INCOMING/01_DESIGN/Шпиговский.fig`  
**Comparison file:** `INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
**Parser used:** `openfig-core` (Node.js) — offline decode of `fig-kiwi` binary inside ZIP  
**Scope:** No design/UX/visual quality judgment. No HTML/SCSS/build output.

---

## 1. File Forensic

| Field | Value |
|-------|-------|
| **FILE EXISTS** | **YES** |
| **Path** | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Шпиговский.fig` |
| **FILE SIZE** | **148 210 516 bytes** (~141.3 MB) |
| **FILE TYPE** | **ZIP archive** (magic `PK\x03\x04`) — Figma offline export (`.fig`) |
| **Exported at** | `2026-06-15T14:51:27.003Z` (from embedded `meta.json`) |
| **Embedded file name** | `Шпиговский` |

### Main internal files (ZIP entries: 170)

| Entry | Role | Size (approx.) |
|-------|------|----------------|
| `canvas.fig` | Main document binary (`fig-kiwi` format, schema + zstd data chunks) | ~2.9 MB compressed |
| `meta.json` | Export metadata, thumbnail coords, background color | 333 B |
| `thumbnail.png` | File preview | ~82 KB |
| `images/*` | Embedded raster assets (SHA-1 hashed filenames) | 166 files |

### Aggregate counts

| Metric | Value |
|--------|-------|
| **IMAGES COUNT** (in ZIP) | **166** |
| **Image fill references** (in document tree) | **562** |
| **PAGES COUNT** (Figma `CANVAS` nodes) | **2** |
| **FRAME COUNT** (all `FRAME` nodes) | **3172** |
| **Node changes** (flat node array) | **7953** |
| **TEXT nodes** | **1983** |
| **TEXT with extractable `textData.characters`** | **1971** |
| **SYMBOL** (components) | **76** |
| **INSTANCE** | **954** |
| **VARIABLE / VARIABLE_SET** | **16 / 7** |

### Binary format notes

- Outer container: standard ZIP.
- Inner `canvas.fig`: `fig-kiwi` prelude + version `0x6A` + deflate schema chunk + **zstd** data chunk.
- Plain unzip + string grep **insufficient**; requires kiwi decoder (e.g. `openfig-core`, `fig-kiwi`).
- ASCII node-type tokens (`FRAME`, `TEXT`, …) **not present** in raw binary — types exist only after decode.

---

## 2. Page Discovery

Figma has **2 canvas pages**. All site mockups live on **`Page 1`** as top-level frames (not as separate Figma pages).

### Figma canvas level

| ID | Name | Role |
|----|------|------|
| **PAGE-01** | `Page 1` | All page mockups (desktop + mobile) |
| **PAGE-02** | `Internal Only Canvas` | Design system: symbols, color/type variables, component source frames |

### Logical page templates (top-level frames on `Page 1`)

Desktop width cluster: **1437×…** (one frame **1440×929** for hero slice).

| ID | Frame name | Size (W×H) | Viewport signal |
|----|------------|------------|-----------------|
| **PG-01** | Главная страница | 1437 × 16809 | desktop |
| **PG-02** | Услуги хаб | 1437 × 11999 | desktop |
| **PG-03** | Услуга конечная | 1437 × 13313 | desktop |
| **PG-04** | О центре | 1437 × 12830 | desktop |
| **PG-05** | Блог хаб | 1437 × 5031 | desktop |
| **PG-06** | Правовая инфа | 1437 × 3151 | desktop |
| **PG-07** | Отзывы | 1437 × 5155 | desktop |
| **PG-08** | Контакты | 1437 × 4505 | desktop |
| **PG-09** | 404 | 1437 × 1900 | desktop |
| **PG-10** | Статья | 1437 × 11861 | desktop |
| **PG-11** | Услуга подраздел | 1437 × 13675 | desktop |
| **PG-12** | Главная страница - моб | 380 × 22883 | mobile (name + width) |
| **PG-13** | Услуги хаб - моб | 380 × 17611 | mobile |
| **PG-14** | Услуга конечная - моб | 380 × 18136 | mobile |
| **PG-15** | О центре - моб | 390 × 16586 | mobile |
| **PG-16** | Блог хаб - моб | 380 × 8678 | mobile |
| **PG-17** | Правовая инфа - моб | 380 × 5035 | mobile |
| **PG-18** | Отзывы - моб | 380 × 6902 | mobile |
| **PG-19** | Контакты - моб | 380 × 4827 | mobile |
| **PG-20** | 404 - моб | 380 × 1734 | mobile |
| **PG-21** | Статья - моб | 380 × 17833 | mobile |
| **PG-22** | Услуга подраздел - моб | 380 × 18101 | mobile |

### Extra top-level frames (not full pages)

| Name | Size | Note |
|------|------|------|
| `1 - Главный экран` | 1440 × 929 | Hero slice only (desktop) |
| `2 - Дом - вступление` | 1437 × 1262 | Home intro section slice (desktop) |
| `Дом вступление` | 380 × 4429 | Home intro slice (mobile) |

**Total top-level frames on Page 1:** 25  
**Coverage vs PDF intake (12 templates × desktop/mobile):** **complete** — all expected templates present with `- моб` pairs.

---

## 3. Frame Discovery

### 3.1 Per Figma canvas

| Canvas | Top-level children | Nested `FRAME` count (descendants) |
|--------|-------------------|-----------------------------------|
| `Page 1` | 25 (all `FRAME`) | 2901 |
| `Internal Only Canvas` | 106 (mixed types) | (component library; not page layout) |

### 3.2 Desktop / mobile / tablet signals

Heuristic: frame **name** (`- моб`) + width bands (≤480 mobile, ≤900 tablet, ≥1200 desktop).

| Viewport band | Frames with H > 800px (page-like) |
|---------------|-----------------------------------|
| desktop | 68 |
| mobile | 162 |
| tablet | 3 |
| unknown | 33 |

**Tablet:** no dedicated `- tablet` frames; only 3 mid-width frames detected by size alone.

### 3.3 Page template table (primary discovery set)

| Page frame | W | H | Viewport | Nested frames (incl. self) |
|------------|---|---|----------|----------------------------|
| Главная страница | 1437 | 16809 | desktop | 245 |
| Услуги хаб | 1437 | 11999 | desktop | 178 |
| Услуга конечная | 1437 | 13313 | desktop | 214 |
| О центре | 1437 | 12830 | desktop | 198 |
| Блог хаб | 1437 | 5031 | desktop | 89 |
| Правовая инфа | 1437 | 3151 | desktop | 52 |
| Отзывы | 1437 | 5155 | desktop | 94 |
| Контакты | 1437 | 4505 | desktop | 78 |
| 404 | 1437 | 1900 | desktop | 31 |
| Статья | 1437 | 11861 | desktop | 186 |
| Услуга подраздел | 1437 | 13675 | desktop | 205 |
| Главная страница - моб | 380 | 22883 | mobile | 312 |
| … (other `- моб` pairs) | 380–390 | varies | mobile | 31–312 |

### 3.4 Home page section frames (inside `Главная страница`)

Direct children — **15** section-level nodes (14 `FRAME` + 1 `INSTANCE` footer):

| # | Block frame name | W×H | Auto-layout (`stackMode`) |
|---|------------------|-----|---------------------------|
| 1 | 1 - Главный экран | 1440×929 | — |
| 2 | 2 - Дом - вступление | 1437×1260 | — |
| 3 | 3- Услуги | 1437×1022 | VERTICAL |
| 4 | Нас выбирают | 1437×2114 | — |
| 5 | Отзывы | 1435×429 | — |
| 6 | С чего начать | 1441×1781 | — |
| 7 | Программа центра | 1437×1563 | — |
| 8 | Генотипирование | 1440×879 | — |
| 9 | преимущества | 1437×1294 | VERTICAL |
| 10 | Слово спецу | 1440×511 | — |
| 11 | Видео | 1437×550 | VERTICAL |
| 12 | Специаисты | 1437×561 | VERTICAL |
| 13 | Статьи | 1440×511 | VERTICAL |
| 14 | faq | 1440×1517 | — |
| 15 | Подвал (`INSTANCE`) | 1440×488 | VERTICAL |

**JPG cross-check:** prior JPG analysis inferred **17** blocks for home; FIG shows **15** top-level section frames on home (header likely inside `1 - Главный экран`, not a separate named sibling).

---

## 4. Structure Quality Audit

| Criterion | Rating | Explanation |
|-----------|--------|-------------|
| **A. Отдельные страницы** | **MEDIUM** | 12 full templates exist as **named top-level frames** on one Figma canvas — not as separate Figma pages. Machine-discoverable by frame name, but not by native page list alone. |
| **B. Отдельные блоки** | **GOOD** | Home and inner pages use **semantically named section frames** (`faq`, `Статьи`, `Программа центра`, …). Footer is component instance `Подвал`. |
| **C. Логическая группировка** | **GOOD** | Deep `FRAME` nesting (3172 frames); section boundaries mostly explicit. Some generic names remain (`Frame 3600`, `Property 1=…`). |
| **D. Auto Layout** | **GOOD** | **3179** nodes with `stackMode`: HORIZONTAL **1647**, VERTICAL **1532**. (`layoutMode` field empty — layout expressed via `stackMode` in this export.) |
| **E. Повторно используемые компоненты** | **GOOD** | **76** `SYMBOL` + **954** `INSTANCE` (`Кнопка`, `Пункт`, `Подвал`, `Поле ввода`, pagination variants, etc.). |
| **F. Design system** | **GOOD** | `Internal Only Canvas` holds color variables (`Colors`, `Typography`, primitives), text style specimens, and master symbols. |
| **G. Текстовые слои** | **GOOD** | **1983** TEXT nodes; **1971** with `textData.characters` (UTF-8, including long medical copy). Home page: **100** text strings (**85** unique). |
| **H. Изображения** | **GOOD** | **166** files in ZIP `images/`; **562** image fill references in tree. Assets extractable by hash filename. |

**Overall structure grade for automation:** **GOOD** (with **MEDIUM** on native page separation).

---

## 5. Website Factory Value

Can Factory **automatically** obtain each artifact class?

| Capability | Rating | Notes |
|------------|--------|-------|
| **Список страниц** | **YES** | Top-level frame names on `Page 1` map 1:1 to site templates (desktop + `- моб`). |
| **Список блоков** | **PARTIAL** | Reliable on home (15 named sections). Other pages need per-template traversal rules; depth and naming not fully uniform. |
| **Размеры блоков** | **YES** | `size.x` / `size.y` on frames (e.g. home hero 1440×929, page 1437×16809). |
| **Тексты** | **YES** | `textData.characters` — 1971/1983 nodes; no OCR required. |
| **Изображения** | **YES** | Bundled `images/<sha1>` + fill paint hashes; resolvable offline. |
| **Структура секций** | **PARTIAL** | Tree walk yields sections, but **no single stable “section” node type** — heuristics on frame depth/name required; `GROUP` nodes = **0** (grouping done via nested frames). |

**Factory prerequisite:** integrate a **fig-kiwi decoder** pipeline (`openfig-core` or equivalent). Raw ZIP inspection alone is **not** enough.

---

## 6. JPG vs FIG Comparison

| Dimension | `HOME-PAGE-FULL-MOCKUP.jpg` | `Шпиговский.fig` | Winner for Factory |
|-----------|----------------------------|------------------|-------------------|
| **GEOMETRY** | Raster only; ~1398×16343 px; block heights **approximate** | Exact frame `size` per section; home **1437×16809** | **FIG** |
| **TEXTS** | Vision/OCR; prior test: many **UNKNOWN** partial strings | **1971** machine-readable text nodes; phones, headings, body copy | **FIG** |
| **GROUPS** | Inferred visually; no object tree | **7953** nodes, parentIndex tree, 3172 frames | **FIG** |
| **BLOCKS** | 17 blocks inferred (JPG test v1) | 15 named home sections + nested subframes | **FIG** |
| **SECTIONS** | Manual band decomposition | Named frames (`faq`, `Статьи`, …) + y-order from tree | **FIG** |
| **AUTO DISCOVERY** | Human/vision heuristics | Programmatic: pages, sizes, texts, components, variables | **FIG** |

**JPG strengths (non-Factory):** quick human visual QA; single-file preview; no parser dependency.  
**JPG limits:** one page only (home desktop); no mobile; no other templates; no component/variable layer.

**Size alignment (home desktop):**

| Source | Width | Height |
|--------|-------|--------|
| JPG mockup | 1398 | 16343 |
| FIG `Главная страница` | 1437 | 16809 |

~3% width delta — consistent with export/raster scaling, not a different layout.

---

## 7. Final Verdict

| Question | Answer |
|----------|--------|
| **FIG USABLE FOR WEBSITE FACTORY** | **YES** |
| **BETTER THAN JPG** | **YES** (for automated discovery / extraction) |
| **GOOD ENOUGH AS VISUAL SSOT** | **YES** — structurally complete SSOT for all 12 templates + mobile pairs; still needs human sign-off for visual parity |
| **CAN REPLACE JPG** | **NO** — keep JPG (or PDF) as fast human visual reference and cross-check raster |
| **RECOMMENDED WORKFLOW** | **B) FIG + JPG → Discovery → Build** |

### Rationale

- **FIG** is the **primary machine source**: pages, blocks, geometry, texts, images, components, variables.
- **JPG** remains a **secondary human visual anchor** (home desktop only; no structural data).
- **PDF intake** (24 files) still valuable for client-approved visual SSOT per Factory charter — FIG does not obsolete PDF authority without an explicit governance decision.

### Risks / gaps (forensic only)

1. **Parser dependency** — Factory must standardize on `openfig-core`/`fig-kiwi`; not built-in today.
2. **Page model** — templates are frames on one canvas, not Figma pages; discovery rules must target top-level frame names.
3. **Block discovery** — section naming is strong on home, **PARTIAL** globally; generic frame names exist.
4. **Header** — not a separate top-level home section; nested inside `1 - Главный экран` (differs from JPG’s explicit BLOCK-01 header band).
5. **Tablet** — no explicit tablet artboards detected.
6. **Temp artefacts** — forensic parse outputs under `REPORTS/_fig_*` are agent-generated scratch; not product deliverables.

---

**STOP.** No Layout Spec, Assembly Spec, HTML, SCSS, or Build produced in this task.
