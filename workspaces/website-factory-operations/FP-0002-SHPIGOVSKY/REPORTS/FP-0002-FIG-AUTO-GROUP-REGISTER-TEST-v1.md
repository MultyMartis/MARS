# REPORT — FP-0002 FIG AUTO GROUP REGISTER TEST v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-17  
**Phase:** FIG-only auto Group Register test (SECTION-01 scope)  
**Primary SSOT:** `INCOMING/01_DESIGN/Шпиговский.fig` (`openfig-core` 0.3.7 offline decode)  
**Target:** `Главная страница` → SECTION-01 `1 - Главный экран` (`1:876`)  
**JPG (disputes only):** `INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` — **not used** in auto registers below  

**Constraints respected:** No HTML · SCSS · JS · Layout Spec · Assembly Spec · Build.  
**Not touched:** `workspaces/fp-0002-shpigovsky-frontend/*`, `dist/*`, header/hero/footer/ui-demo implementation.

**Factory comparison reference (read-only, not used to build auto registers):**

- Header: `FP-0002-HEADER-LAYOUT-SPEC-v2.md` (BLK-001/002, Groups 1–7)
- Hero: `FP-0002-HERO-GROUP-FORENSIC-v1.md` + `FP-0002-HERO-LAYOUT-SPEC-v1.md` (Group Register v2)

**Evidence artefact (scratch):** `REPORTS/_section01_full_decomp_v1.json` — full tree, 51 nodes.

---

## 1. Section-01 Decomposition

### 1.1 Section root

| Field | Value |
|-------|-------|
| **Name** | `1 - Главный экран` |
| **Frame ID** | `1:876` |
| **Type** | FRAME |
| **Bounds** | x=-1, y=0, w=1440, h=929 |
| **Direct children** | **3** (not 2 — header + hero + decorative vectors) |
| **Flat node count (full expand)** | **51** |

### 1.2 Top-level children (FIG layer order)

| # | FIG name | ID | Type | Size | Role (FIG-only) |
|---|----------|-----|------|------|-----------------|
| 1 | `Хедер` | `1:877` | FRAME | 1170×143 | Site chrome — VERTICAL auto-layout, 2 rows |
| 2 | `Group 6` | `1:912` | FRAME | 1400×750 | Hero band wrapper — absolute children |
| 3 | `Frame 81513852` | `1:924` | FRAME | 187×83 | Decorative brand vectors (sibling, overlaps header zone) |

### 1.3 Full tree (expanded — no stop at `Group 6`, `банер`, `Frame 4`)

```
1 - Главный экран (1:876) 1440×929
├── Хедер (1:877) 1170×143 [VERTICAL AL]
│   ├── Frame 18 (1:878) 1170×101 [VERTICAL AL]          ← band 1
│   │   └── Frame 17 (1:879) 1150×46 [HORIZONTAL AL]
│   │       ├── image 219 (1:880) 205×46 [IMAGE]           ← logo raster
│   │       ├── Frame 15 (1:881) [VERTICAL AL]           ← region cluster
│   │       │   ├── Frame 14 (1:882) [HORIZONTAL AL]
│   │       │   │   ├── TEXT «Москва, Московская область» (1:883)
│   │       │   │   └── chevron-down (1:884) → Vector (1:885)
│   │       │   └── TEXT «Московская область» (1:886) w=0  ← empty/hidden duplicate
│   │       ├── Frame 16 (1:887) [VERTICAL AL]            ← hours cluster
│   │       │   ├── TEXT «пн-пт: 08:00-18:00, сб-вс: 08:00-22:00» (1:888)
│   │       │   └── TEXT «режим работы» (1:889)
│   │       ├── TEXT «8 (925) 183-64-64 / 8 (995) 023-92-26» (1:890)
│   │       └── Frame 13 (1:891) [HORIZONTAL AL]         ← messengers + header CTA
│   │           ├── telegramm (1:892) → 2× Ellipse + Vector
│   │           ├── watsapp (1:896) → 2× Ellipse + Vector
│   │           └── INSTANCE «Кнопка» (1:900) → «Записаться на консультацию»
│   └── Frame 19 (1:901) 1170×22 [HORIZONTAL AL]         ← band 2
│       ├── Frame 10 (1:902) 1130×22 [HORIZONTAL AL]     ← nav + search
│       │   ├── TEXT «Лечение и профилактика» (1:903)
│       │   ├── TEXT «Генотипирование» (1:904)
│       │   ├── TEXT «Специалисты» (1:905)
│       │   ├── TEXT «О центре» (1:906)
│       │   ├── TEXT «Отзывы» (1:907)
│       │   ├── TEXT «Статьи» (1:908)
│       │   ├── TEXT «Контакты» (1:909)
│       │   └── INSTANCE search (1:910)
│       └── TEXT «8 (800) 777-02-05» (1:911)
├── Group 6 (1:912) 1400×750
│   ├── банер (1:913) 1400×750
│   │   ├── TEXT «Центр профилактики и лечения зависимости» (1:914)  ← orphan layer, outside Group 5
│   │   ├── Vector (1:915) 768×408                                    ← decorative mass
│   │   ├── image 13030403 (1:916) 1523×863 [IMAGE]                   ← hero photo
│   │   ├── Rectangle 4245 (1:917) 1400×750                           ← full-bleed wash overlay
│   │   └── Group 5 (1:918) 1039×162
│   │       ├── Rectangle 4246 (1:919) 1039×162                       ← card surface
│   │       ├── TEXT «Шпиговский дом» (1:920)                         ← heading (y=68)
│   │       └── TEXT «Центр профилактики и лечения зависимостей» (1:921) ← label (y=27)
│   └── Frame 4 (1:922) 334×113 [VERTICAL AL]                         ← CTA stack
│       └── INSTANCE «Кнопка» (1:923) → «Записаться на консультацию»
└── Frame 81513852 (1:924) 187×83
    ├── Vector (1:925)
    └── Vector (1:926)
```

### 1.4 Decomposition notes (FIG facts)

| Signal | Finding |
|--------|---------|
| Header row model in FIG | **2 bands** inside `Хедер`: `Frame 18` (101px) + `Frame 19` (22px) — not the Factory BLK-001/002 content split |
| Logo placement in FIG | `image 219` lives in **band 1** (`Frame 17`), not in nav band |
| Nav link count in FIG | **7** text links + **search** instance in `Frame 10` |
| Phones in FIG | **Two clusters**: dual-line 925/995 in band 1; single 800 line in band 2 |
| Hero CTA placement | `Frame 4` is **sibling** of `банер`, not child of `Group 5` — confirmed |
| Extra hero layers | Orphan TEXT `1:914`, decorative Vector `1:915` — present in FIG, not in Factory Hero v2 |
| Corner mask | No node named or typed as mask; `image 13030403` is `ROUNDED_RECTANGLE` — corner radius **exists on node**, not auto-labeled as GROUP-01C |

---

## 2. Header Group Register

**Source:** FIG tree only (`Хедер` subtree + decorative sibling `Frame 81513852`).  
**Method:** Parent-index order · expand all frames to leaves · verbatim FIG names.

```
HEADER (SECTION-01)
 ├ GROUP-01  Хедер                    (1:877)  FRAME   VERTICAL AL
 ├ GROUP-02  Frame 18                 (1:878)  FRAME   band-1 container
 ├ GROUP-03  Frame 17                 (1:879)  FRAME   HORIZONTAL AL — meta+logo+contact+CTA strip
 ├ GROUP-04  image 219                (1:880)  ROUNDED_RECTANGLE  logo/brand raster [IMAGE]
 ├ GROUP-05  Frame 15                 (1:881)  FRAME   region cluster
 ├ GROUP-06  Frame 14                 (1:882)  FRAME   region label + chevron
 ├ GROUP-07  TEXT Москва               (1:883)  TEXT    «Москва, Московская область»
 ├ GROUP-08  chevron-down              (1:884)  FRAME   dropdown icon
 ├ GROUP-09  Frame 16                 (1:887)  FRAME   hours cluster
 ├ GROUP-10  TEXT hours                (1:888)  TEXT    schedule string
 ├ GROUP-11  TEXT режим работы        (1:889)  TEXT    hours caption
 ├ GROUP-12  TEXT phones dual          (1:890)  TEXT    925 / 995 lines
 ├ GROUP-13  Frame 13                 (1:891)  FRAME   messengers + CTA row
 ├ GROUP-14  telegramm                (1:892)  FRAME   messenger icon
 ├ GROUP-15  watsapp                  (1:896)  FRAME   messenger icon
 ├ GROUP-16  INSTANCE Кнопка          (1:900)  INSTANCE  «Записаться на консультацию»
 ├ GROUP-17  Frame 19                 (1:901)  FRAME   band-2 container
 ├ GROUP-18  Frame 10                 (1:902)  FRAME   nav + search row
 ├ GROUP-19  NAV «Лечение и профилактика» (1:903) TEXT
 ├ GROUP-20  NAV «Генотипирование»    (1:904)  TEXT
 ├ GROUP-21  NAV «Специалисты»        (1:905)  TEXT
 ├ GROUP-22  NAV «О центре»           (1:906)  TEXT
 ├ GROUP-23  NAV «Отзывы»             (1:907)  TEXT
 ├ GROUP-24  NAV «Статьи»             (1:908)  TEXT
 ├ GROUP-25  NAV «Контакты»           (1:909)  TEXT
 ├ GROUP-26  INSTANCE search          (1:910)  INSTANCE
 ├ GROUP-27  TEXT phone 800           (1:911)  TEXT    «8 (800) 777-02-05»
 └ GROUP-28  Frame 81513852            (1:924)  FRAME   decorative brand vectors (section sibling)
     ├ GROUP-28A Vector (1:925)
     └ GROUP-28B Vector (1:926)
```

### Per-group detail (selected)

| GROUP | FIG source | Type | Children | Text / instance |
|-------|------------|------|----------|-----------------|
| GROUP-01 | `1:877` | FRAME | GROUP-02, GROUP-17 | — |
| GROUP-03 | `1:879` | FRAME | 04, 05, 09, 12, 13 | 5-column horizontal strip |
| GROUP-04 | `1:880` | IMAGE rect | — | Brand raster 205×46 |
| GROUP-16 | `1:900` | INSTANCE `Кнопка` | — | `Записаться на консультацию` |
| GROUP-18 | `1:902` | FRAME | GROUP-19…26 | 8 children horizontal AL |
| GROUP-28 | `1:924` | FRAME | 28A, 28B | Overlaps header visually at x=135,y=20 |

**Auto-derived header row hierarchy (FIG geometry, not Factory BLK labels):**

| FIG band | Frame | Height | Contains |
|----------|-------|--------|----------|
| Band 1 | `Frame 18` → `Frame 17` | 101px / 46px content | Logo + region + hours + phones + messengers + header CTA |
| Band 2 | `Frame 19` | 22px | 7 nav links + search + 800 phone |

---

## 3. Hero Group Register

**Source:** FIG `Group 6` subtree only (excludes `Хедер`, includes hero CTA sibling).

```
HERO (SECTION-01 / Group 6)
 ├ GROUP-01  Group 6                  (1:912)  FRAME   hero wrapper
 ├ GROUP-02  банер                    (1:913)  FRAME   hero visual stack
 ├ GROUP-03  TEXT orphan label        (1:914)  TEXT    duplicate label layer (outside card)
 ├ GROUP-04  Vector                   (1:915)  VECTOR  decorative mass 768×408
 ├ GROUP-05  image 13030403           (1:916)  ROUNDED_RECTANGLE  background photo [IMAGE]
 ├ GROUP-06  Rectangle 4245           (1:917)  ROUNDED_RECTANGLE  full-bleed overlay wash
 ├ GROUP-07  Group 5                  (1:918)  FRAME   frosted card band
 ├ GROUP-08  Rectangle 4246           (1:919)  ROUNDED_RECTANGLE  card surface
 ├ GROUP-09  TEXT heading             (1:920)  TEXT    «Шпиговский дом»
 ├ GROUP-10  TEXT label               (1:921)  TEXT    «Центр профилактики и лечения зависимостей»
 ├ GROUP-11  Frame 4                  (1:922)  FRAME   CTA stack [VERTICAL AL]
 └ GROUP-12  INSTANCE Кнопка          (1:923)  INSTANCE  «Записаться на консультацию»
```

### FIG-native role mapping (inference from structure only)

| AUTO GROUP | Inferred role | FIG evidence |
|------------|---------------|--------------|
| GROUP-05 | Background | IMAGE fill, largest layer under overlay |
| GROUP-06 | Overlay | Full-size rectangle sibling above image |
| GROUP-08 | Card surface | Rectangle inside `Group 5`, behind text |
| GROUP-10 | Label | Smaller text, higher y in card |
| GROUP-09 | Heading | Larger text block in card |
| GROUP-11–12 | CTA | `Frame 4` sibling of `банер`; instance resolves text |
| GROUP-03, GROUP-04 | **Unassigned** | Extra layers — not required for minimal hero model |

**Content lock from FIG (machine):**

| Entity | FIG text |
|--------|----------|
| Label | `Центр профилактики и лечения зависимостей` |
| Heading | `Шпиговский дом` |
| CTA | `Записаться на консультацию` |

---

## 4. Comparison

### 4.1 Header — AUTO FIG vs Factory (`HEADER-LAYOUT-SPEC-v2` Groups 1–7)

| ENTITY | FIG (auto) | FACTORY | MATCH? |
|--------|------------|---------|--------|
| Dual-row header (BLK-001 / BLK-002) | 2 FIG bands, **different content split** | Row1: meta+utility+phones; Row2: logo+5-nav+CTA | **NO** |
| Region Group | `Frame 15` / TEXT `1:883` | GROUP 1 — Zone A | **PARTIAL** — entity present, zone placement differs |
| Hours Group | `Frame 16` / TEXT `1:888–889` | GROUP 2 — Zone B | **YES** — content matches |
| Utility Links (Генотипирование, Специалисты) | In **nav band** `Frame 10` (`1:904–905`) | GROUP 3 — Row 1 Zone C | **NO** — row assignment inverted |
| Phone Group (925/995) | TEXT `1:890` in band 1 | GROUP 4 — Row 1 Zone D | **PARTIAL** — phones exist; extra 800 line in band 2 |
| Logo / Brand | `image 219` in **band 1** | GROUP 5 — Row 2 Zone E | **NO** — wrong row |
| Primary Nav (5 links) | **7** links in `Frame 10` | GROUP 6 — Услуги, О центре, Отзывы, Статьи, Контакты | **NO** — count + labels differ |
| Header CTA | INSTANCE `1:900` «Записаться на консультацию» in band 1 | GROUP 7 — «Заказать звонок» in Row 2 | **NO** — label + row |
| Search | INSTANCE `search` `1:910` | Not in SSOT (FD-15) | **NO** — FIG-only |
| Messengers (TG/WA) | `telegramm`, `watsapp` in band 1 | SAFE UNKNOWN / not in PDF SSOT | **FIG-only** |
| Decorative vectors | `Frame 81513852` | Not in Factory register | **FIG-only** |

**What matched:** hours strings · region text cluster · phone numbers (partial) · two-row **geometry** exists.  
**What did not match:** row content model · nav cardinality · CTA label/placement · logo row · utility vs nav split.  
**Human-invented in Factory (not in FIG as stated):** 5-link nav canon · «Заказать звонок» · logo-only-in-main-row · utility links only in top row · BLK-001/002 zone letters.  
**Real in FIG, absent from Factory register:** search · messengers · `Frame 81513852` · dual phone clusters · 7-link nav · header CTA in top band.

### 4.2 Hero — AUTO FIG vs Factory (Group Register v2)

| ENTITY | FIG (auto) | FACTORY v2 | MATCH? |
|--------|------------|------------|--------|
| Background media | `image 13030403` `1:916` | GROUP-01 | **YES** |
| Image overlay | `Rectangle 4245` `1:917` | GROUP-01B | **PARTIAL** — detected, generic name |
| Corner mask | Rounded rect on image node; no semantic group | GROUP-01C | **PARTIAL** — geometry hint only |
| Overlay card container | `Group 5` `1:918` | GROUP-02 | **YES** (aggregated) |
| Card surface | `Rectangle 4246` `1:919` | GROUP-02A | **YES** |
| Content stack | TEXT `1:921` + `1:920` inside Group 5 | GROUP-02B | **PARTIAL** — not auto-labeled |
| Label | `1:921` | GROUP-03 | **YES** — same copy |
| Heading | `1:920` | GROUP-04 | **YES** — same copy |
| CTA primary | `Frame 4` → `1:923` sibling of `банер` | GROUP-05 sibling of card | **YES** |
| CTA text | `Записаться на консультацию` | `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ` | **YES** (case) |
| Content wrapper | Not named in FIG | Structural layer in Factory | **NO** — human layout layer |
| Orphan label layer | TEXT `1:914` outside Group 5 | Not in register | **FIG-only** (stale/duplicate) |
| Decorative vector | `1:915` | Not in register | **FIG-only** |

**What matched:** hero copy · CTA sibling structure · card surface + text children · background + wash layers.  
**What did not match:** semantic IDs · content-wrapper layer · corner mask as named entity.  
**Human-invented in Factory:** GROUP-01C label · GROUP-02B split · content wrapper · exclusion of orphan FIG layers.  
**Real in FIG, not in Factory v2:** TEXT `1:914` · Vector `1:915`.

---

## 5. Auto Generation Score

### HEADER

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **Extractability** | **GOOD** | Full tree to 51 nodes; instances resolve CTA text; AL axes readable |
| **Accuracy** (vs Factory Layout Spec) | **POOR** | Row model and group boundaries **conflict** with PDF/JPG-derived Factory register |
| **Layout Spec readiness** | **POOR** | Cannot emit BLK-001/002 zones without **human reconciliation rules** + SSOT choice (FIG vs PDF) |

**Overall HEADER:** **POOR**

### HERO

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **Extractability** | **EXCELLENT** | Background, overlay, card, texts, CTA instance — all machine-located |
| **Accuracy** (vs Factory v2) | **GOOD** | Content + CTA placement match; sub-layer naming partial |
| **Layout Spec readiness** | **GOOD** | Sufficient for draft Layout Spec with **operator review** on mask + orphan layers |

**Overall HERO:** **GOOD**

---

## 6. Factory Impact

**Question:** If this test succeeds, can Factory run:

```text
FIG → AUTO GROUP REGISTER → OPERATOR REVIEW → LAYOUT SPEC
```

instead of:

```text
FIG → manual GROUP REGISTER
```

| Block | Answer | Notes |
|-------|--------|-------|
| **Hero** | **YES (with review)** | Auto register covers ~85% of Factory v2; operator confirms mask, drops orphan layers, names content wrapper |
| **Header** | **NO (not yet)** | Auto tree is **complete** but **not aligned** with Factory dual-row law without: (1) SSOT arbitration FIG↔PDF, (2) row-content heuristics, (3) nav cardinality rules, (4) CTA/label normalization |
| **SECTION-01 boundary** | **PARTIAL** | FIG bundles header+hero in one section frame; Factory splits by visual boundary — needs **boundary rule**, not manual re-draw |
| **End-to-end without human** | **NO** | Operator review remains **mandatory** for both blocks; header needs **structural** not just cosmetic review |

**Recommended pipeline (documentation):**

```text
FIG parse (openfig-core)
  → AUTO flat tree + instance text
  → AUTO semantic register (rules TBD for header)
  → OPERATOR REVIEW (SSOT conflicts, orphans, BLK mapping)
  → LAYOUT SPEC (Hero: experiment-ready; Header: after rules charter)
```

**Acceleration vs manual JPG path (SECTION-01 only):** **~70%** on Hero grouping; **~40%** on Header (extract fast, reconcile slow).

---

## 7. Final Verdict

| Gate | Answer |
|------|--------|
| **AUTO HEADER REGISTER** | **FAIL** |
| **AUTO HERO REGISTER** | **SUCCESS** |
| **GROUP DECOMPOSITION FROM FIG** | **PARTIAL** |
| **READY FOR AUTO LAYOUT SPEC EXPERIMENT** | **YES** (Hero only) |
| **RECOMMENDED FOR WEBSITE FACTORY** | **YES** |

### Rationale

- **HEADER FAIL:** FIG produces a complete register, but it **does not match** Factory Header Layout Spec v2 without human SSOT arbitration. Key conflicts: logo row, nav count, utility/nav row assignment, CTA label and placement, FIG-only search/messengers.
- **HERO SUCCESS:** Machine register recovers Factory v2 **content**, **card structure**, and **CTA sibling** relationship from FIG alone.
- **DECOMPOSITION PARTIAL:** Raw expansion to **51 nodes** works; semantic Factory-grade groups work for Hero, not Header.
- **LAYOUT SPEC experiment:** Safe to trial **FIG → auto Hero register → operator review → Hero Layout Spec**; **not** Header until header heuristics charter exists.
- **RECOMMENDED YES:** FIG remains primary discovery SSOT; auto registers are **inputs**, not approvals.

---

## UNKNOWN

| ID | Topic |
|----|-------|
| UNK-01 | Whether `Frame 81513852` is visible in production export or FIG editor-only overlap |
| UNK-02 | Whether TEXT `1:914` is hidden in Figma UI (zero-opacity) or true duplicate |
| UNK-03 | Which SSOT wins for header row model when FIG and PDF conflict — **requires operator charter** |

---

**STOP.** Discovery report only. No Layout Spec, Assembly Spec, HTML, SCSS, or Build.

**Parser:** `REPORTS/_fig_parse_temp/section01_full_decomp.mjs`  
**Evidence JSON:** `REPORTS/_section01_full_decomp_v1.json`
