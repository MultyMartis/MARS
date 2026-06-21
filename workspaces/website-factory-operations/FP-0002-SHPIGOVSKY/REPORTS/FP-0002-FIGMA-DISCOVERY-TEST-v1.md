# REPORT — FP-0002 FIGMA DISCOVERY TEST v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-17  
**Task type:** Discovery test only (FIG → Home Page structure)  
**Primary authority:** `INCOMING/01_DESIGN/Шпиговский.fig`  
**Secondary (visual check only):** `INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
**Parser:** `openfig-core` 0.3.7 — offline decode of `.fig` (ZIP + `fig-kiwi`)  
**Figma MCP:** not used (server requires auth; offline FIG parse is sufficient for this test)  
**Scope:** Discovery only. No Layout Spec, Assembly Spec, HTML, SCSS, Build.

---

## 1. Home Frame Identification

| Field | Value |
|-------|-------|
| **FRAME NAME** | `Главная страница` |
| **FRAME SIZE** | **1437 × 16809** px |
| **FRAME ID** | **`1:875`** (`sessionID:localID` from decoded FIG tree) |
| **Parent canvas** | `Page 1` |
| **Direct children** | **15** section-level nodes (14 `FRAME` + 1 `INSTANCE` footer) |

### Why this frame is canonical Home Desktop

1. **Explicit Russian name** `Главная страница` — matches design naming on `Page 1`.
2. **Desktop width cluster** — **1437 px** (same band as all other desktop page templates on `Page 1`).
3. **Not mobile** — mobile variant is a separate sibling frame `Главная страница - моб` (380 × 22883).
4. **Full-page height** — **16809 px**; contains all home sections as direct children.
5. **FIG wins over JPG** — JPG is a single raster (~1398 × 16343); FIG gives exact frame bounds and named section children.

**JPG cross-check:** width/height delta ~3% vs FIG — consistent with raster export scaling, not a different page.

---

## 2. Section Discovery

Top-to-bottom list from **direct children** of `Главная страница` (`1:875`). Names are **verbatim from FIG** (including typos).

```
SECTION-01
1 - Главный экран

SECTION-02
2 - Дом - вступление

SECTION-03
3- Услуги

SECTION-04
Нас выбирают

SECTION-05
Отзывы

SECTION-06
С чего начать

SECTION-07
Программа центра

SECTION-08
Генотипирование

SECTION-09
преимущества

SECTION-10
Слово спецу

SECTION-11
Видео 

SECTION-12
Специаисты

SECTION-13
Статьи

SECTION-14
faq

SECTION-15
Подвал
```

**Notes:**

- **15 sections** in FIG vs **17 blocks** inferred from JPG (`FP-0002-FULL-jpg-ANALYSIS-TEST-v1.md`). FIG does not split header from hero at the section level — both live inside `1 - Главный экран`.
- Footer is a **component instance** `Подвал`, not a raw frame.
- Poor/generic names preserved as-is: `faq`, `преимущества`, `Специаисты`, `Group 6`, `Frame 4`, etc. (see Hero decomposition).

---

## 3. Section Register

| # | Название (FIG) | ID | Тип | ≈ Высота | Изображения | Текст | CTA | Повторяемые компоненты |
|---|----------------|-----|-----|----------|-------------|-------|-----|------------------------|
| 01 | `1 - Главный экран` | `1:876` | FRAME (hero+header) | 929 | YES | YES (15) | YES | `Кнопка`, `search` |
| 02 | `2 - Дом - вступление` | `1:927` | FRAME (intro) | 1260 | YES | YES (14) | NO | `Маркированный список`, `Ес` |
| 03 | `3- Услуги` | `1:958` | FRAME (services) | 1022 | YES | YES (3) | NO | `Раскрытие информации`, `Пункт услуги`, `Услуга` |
| 04 | `Нас выбирают` | `1:991` | FRAME | 2114 | YES | YES (19) | NO | `Пункт услуги`, `Стрелка` |
| 05 | `Отзывы` | `1:1050` | FRAME (reviews) | 429 | NO | YES (5) | YES | `отзыв` |
| 06 | `С чего начать` | `1:1079` | FRAME | 1781 | YES | YES (10) | YES | `Раскрытие информации`, `Маркированный список`, `Важно `, `Цифра`, `Запись маленькая` |
| 07 | `Программа центра` | `1:1115` | FRAME (program) | 1563 | YES | YES (4) | YES | `этап`, `Запись маленькая` |
| 08 | `Генотипирование` | `1:1136` | FRAME | 879 | YES | YES (6) | YES | `Маркированный список`, `Кнопка` |
| 09 | `преимущества` | `1:1164` | FRAME | 1294 | YES | YES (7) | YES | `этап` |
| 10 | `Слово спецу` | `1:1208` | FRAME | 511 | YES | YES (4) | YES | `Кнопка` |
| 11 | `Видео ` | `1:1224` | FRAME | 550 | YES | YES (1) | NO | — |
| 12 | `Специаисты` | `1:1231` | FRAME | 561 | YES | YES (5) | YES | `Врач`, `Услуга` |
| 13 | `Статьи` | `1:1268` | FRAME | 511 | NO | YES (3) | YES | `Статья` |
| 14 | `faq` | `1:1280` | FRAME | 1517 | YES | YES (4) | YES | `Расскрытие вопроса`, `Вопрос скрыт`, `Поле ввода`, `Кнопка` |
| 15 | `Подвал` | `1:1309` | INSTANCE (footer) | 488 | NO | NO* | NO | `Подвал` |

\*Footer text exists inside the `Подвал` symbol on `Internal Only Canvas`; this instance subtree did not surface text nodes in offline instance traversal (instance children not expanded in export).

**Section typing:** heuristic labels (`hero+header`, `intro`, `services`, …) added for Factory readability; FIG provides frame names only.

---

## 4. Content Extraction Test

First **5 sections** — heading / subheading / CTA only. Extracted from `textData.characters` via font-size heuristics + CTA pattern/`Кнопка` instance resolution.

| Section | Heading | Subheading | CTA | Quality |
|---------|---------|------------|-----|---------|
| **SECTION-01** `1 - Главный экран` | `Шпиговский дом` | `Центр профилактики и лечения зависимости` | `Записаться на консультацию` *(from `Кнопка` symbol default; hero instance `1:923`)* | **EXCELLENT** |
| **SECTION-02** `2 - Дом - вступление` | `Шпиговский дом — восстановление с уважением к личности` | `Реабилитация без изоляции` | — | **EXCELLENT** |
| **SECTION-03** `3- Услуги` | `Лечение и профилактика` | `смотреть все` | — | **GOOD** |
| **SECTION-04** `Нас выбирают` | `Нас выбирают за мультидисциплинарный подход к лечению` | `до 15 резидентов` | — | **EXCELLENT** |
| **SECTION-05** `Отзывы` | `Отзывы` | `смотреть отзывы` *(heuristic; alt node `отзыв клиентки на яндекс`)* | `Записаться на консультацию` | **GOOD** |

### Extraction quality notes

| Signal | Result |
|--------|--------|
| Hero copy vs JPG Content Lock v2 | **MATCH** — same strings as `FP-0002-HERO-GROUP-FORENSIC-v1.md` |
| CTA from component instance | **WORKS** when instance uses default symbol text; no per-instance override on hero CTA (`1:923`) |
| Heuristic heading picker | **FAILS** on decorative split text (`преимущества` section: `Шпиг` / `вскиЙ`) and can mis-rank CTA vs disclaimer copy |
| Header noise in SECTION-01 | Nav/phone strings pollute subtree; hero copy still recoverable by font size |

**Overall content extraction (first 5):** **GOOD → EXCELLENT** for headings; **PARTIAL** for automated CTA/subheading without component-aware rules.

---

## 5. Hero Group Discovery

Automatic decomposition of **`1 - Главный экран`** (`1:876`, 1440×929) — **FIG only**.  
Comparison reference (read-only): `FP-0002-HERO-GROUP-FORENSIC-v1.md` (JPG-derived Group Register v2).

### FIG top-level children

| FIG node | ID | Size | Role (inferred) |
|----------|-----|------|-----------------|
| `Хедер` | `1:877` | 1170×143 | Site chrome — **not** Factory Hero band per JPG boundary |
| `Group 6` | `1:912` | — | Hero content wrapper |
| `Frame 81513852` | `1:924` | 187×83 | Decorative vectors (brand mark fragment) |

### FIG `Group 6` decomposition

```
Group 6 (1:912)
├── банер (1:913)
│   ├── image 13030403 (1:916)          — background photo [IMAGE FILL]
│   ├── Rectangle 4245 (1:917)        — full-bleed overlay wash
│   └── Group 5 (1:918)               — frosted card band
│       ├── Rectangle 4246 (1:919)    — card surface
│       ├── TEXT «Шпиговский дом» (1:920)
│       └── TEXT «Центр профилактики и лечения зависимостей» (1:921)
└── Frame 4 (1:922)                     — CTA stack [VERTICAL auto-layout]
    └── INSTANCE «Кнопка» (1:923)       — «Записаться на консультацию»
```

### GROUP REGISTER (FIG auto-discovery)

| GROUP-ID | FIG source | Type | Size / text | Parent |
|----------|------------|------|-------------|--------|
| **FIG-G01** | `image 13030403` | Background image | 1523×863, image fill | `банер` |
| **FIG-G02** | `Rectangle 4245` | Background overlay | 1400×750 | `банер` |
| **FIG-G03** | `Group 5` | Overlay card (aggregated) | 1039×162 | `банер` |
| **FIG-G04** | `Rectangle 4246` | Card surface | 1039×162 | `Group 5` |
| **FIG-G05** | TEXT `Шпиговский дом` | Main heading | font ~70 | `Group 5` |
| **FIG-G06** | TEXT `Центр профилактики и лечения зависимостей` | Label / subheading | font ~36–42 | `Group 5` |
| **FIG-G07** | `Frame 4` → `Кнопка` `1:923` | CTA primary | 334×53 instance | `Group 6` (**sibling** of `банер`) |
| **FIG-G08** | `Хедер` | Header chrome | 1170×143 | `1 - Главный экран` |
| **FIG-G09** | `Frame 81513852` | Decorative vectors | 187×83 | `1 - Главный экран` |

**Total semantic groups auto-derived:** **9** (42 raw nodes in subtree including header/nav leaves).

### Comparison with existing Hero Group Register (JPG Forensic v2)

| Dimension | JPG Forensic v2 | FIG auto-discovery | Match? |
|-----------|-----------------|-------------------|--------|
| Hero label text | `Центр профилактики и лечения зависимостей` | Same (FIG-G06) | **YES** |
| Hero heading | `Шпиговский дом` | Same (FIG-G05) | **YES** |
| Hero CTA | `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ` | `Записаться на консультацию` (case differs) | **YES** |
| CTA placement | Sibling of overlay card | `Frame 4` sibling of `банер` / outside `Group 5` | **YES** |
| Card surface vs content stack | GROUP-02A + GROUP-02B split | `Rectangle 4246` + text children in `Group 5` | **PARTIAL** — structure visible, not auto-labeled |
| Background overlay (01B) | Explicit GROUP-01B | `Rectangle 4245` — detected, generic name | **PARTIAL** |
| Corner mask (01C) | GROUP-01C | Not auto-identified as semantic group; rounded rects exist on hero subtree | **POOR** |
| Header separation | Hero START below nav | Header **inside** same section frame `1 - Главный экран` | **NO** — FIG section model differs |
| Semantic group names | GROUP-01…05 | `Group 6`, `Group 5`, `Frame 4`, `банер` | **POOR** naming |

**Conclusion:** FIG **confirms** JPG Forensic **content** and **CTA sibling structure**, but **does not** auto-produce Factory-grade semantic group IDs without naming/heuristic rules. Header bundling is the main structural mismatch vs Factory Hero boundary.

---

## 6. Auto Discovery Score

| Capability | Score | Rationale |
|------------|-------|-----------|
| **TEXT EXTRACTION** | **EXCELLENT** | 1971/1983 TEXT nodes machine-readable; hero/home copy exact; no OCR |
| **SECTION EXTRACTION** | **EXCELLENT** | 15 named top-level home sections with exact heights and IDs |
| **GROUP EXTRACTION** | **MEDIUM** | Tree walk works; semantic groups need heuristics; generic `Group N` / `Frame N` names |
| **COMPONENT DETECTION** | **GOOD** | 954 instances, 76 symbols; `Кнопка`, `Подвал`, `отзыв`, etc. detectable per section |
| **PAGE DETECTION** | **GOOD** | Home found by name + width; templates are frames on one canvas, not separate Figma pages |

---

## 7. Factory Impact

**Question:** If Factory uses FIG Discovery instead of JPG Discovery, by how much does Discovery accelerate?

| Factor | JPG path | FIG path |
|--------|----------|----------|
| Home section list | Manual vision → 17 inferred blocks | Programmatic → 15 named frames + IDs |
| Text copy | OCR / partial reads / UNKNOWN strings | Direct `textData.characters` |
| Geometry | Approximate band heights | Exact `size.x` / `size.y` per frame |
| Hero groups | Manual visual entity scan | Tree walk + instance resolution |
| Setup cost | Low (open JPG) | Requires `openfig-core` pipeline (already proven in-repo) |
| Multi-page | Home JPG only | All 12 desktop + 11 mobile templates in one file |

**Honest estimate (Home Page Discovery only):** **~65–75% faster** end-to-end vs JPG-only discovery, assuming the `openfig-core` script is integrated into Factory ops (parse → section register → content extract in **minutes** vs **hours** of vision/manual decomposition).

**Caveats:**

- First-time parser integration and heuristic tuning are one-time costs not included above.
- Full-factory acceleration across all pages: **UNKNOWN** without timed runs on all 23 templates.
- FIG does not remove need for human visual sign-off (JPG/PDF still useful).

---

## 8. Final Verdict

| Gate | Answer |
|------|--------|
| **AUTO HOME DISCOVERY FROM FIG** | **SUCCESS** |
| **FIG DISCOVERY BETTER THAN JPG DISCOVERY** | **YES** |
| **CAN GENERATE GROUP REGISTERS FROM FIG** | **PARTIAL** |
| **CAN GENERATE SECTION REGISTERS FROM FIG** | **YES** |
| **RECOMMENDED FOR WEBSITE FACTORY** | **YES** |

### Rationale

- **SUCCESS:** Canonical home frame, 15 sections, text/geometry/components extracted automatically from `Шпиговский.fig`.
- **FIG > JPG:** Authoritative structure, names, sizes, and copy; JPG remains secondary visual QA only.
- **Section registers:** Ready now from direct children of `Главная страница`.
- **Group registers:** Tree + instances sufficient for Hero **content** and **CTA placement**; semantic IDs, header/hero split, and overlay/mask naming still need Factory rules.
- **Recommended workflow:** **FIG primary → Discovery registers → JPG cross-check** (aligns with `FP-0002-FIGMA-FORENSIC-TEST-v1.md`).

---

**STOP.** No Layout Spec, Assembly Spec, HTML, SCSS, or Build produced.

---

## Evidence artefacts (scratch, not deliverables)

| File | Role |
|------|------|
| `REPORTS/_fig_discovery_test_v1.json` | Machine output of this test |
| `REPORTS/_fig_parse_temp/discovery_test_v1.mjs` | Parser script used |

---

## Git status

| Item | Value |
|------|-------|
| **Created** | `REPORTS/FP-0002-FIGMA-DISCOVERY-TEST-v1.md` |
| **Commit / push** | Not performed |

## UNKNOWN / limits

- Footer instance text not expanded in offline parse.
- Figma live MCP (`use_figma`) not exercised — auth required; offline FIG parse used instead.
- Full-factory % speedup beyond home page: **UNKNOWN** without benchmark runs.
