# FP-0002 HEADER LAYOUT SPEC v1

**Block ID / scope:** `FP-0002-BLK-001 + FP-0002-BLK-002` — Desktop Header (shell chrome)  
**Document type:** Layout Spec (composition decomposition — **not** audit, **not** implementation)  
**Status:** **DRAFT** — awaiting operator decision **APPROVED | REVISE**  
**Date:** 2026-06-14  
**Viewport:** Desktop **≥ 1024px** (Phase C.1 default)  
**Layout Pattern:** **LP-HEADER-DUAL-ROW** (BLK-001 stacked above BLK-002)

**Authority applied:**

| Layer | Document | Role |
|-------|----------|------|
| A0 | [FP-0002-SOURCE-DISCOVERY-REPORT-v1.md](FP-0002-SOURCE-DISCOVERY-REPORT-v1.md) | SOURCE-ID register |
| A1 | [FP-0002-DESIGN-AUDIT-v1.md](FP-0002-DESIGN-AUDIT-v1.md) | Visual SSOT READ · header element inventory |
| Approval | [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md) | Operator decision matrix (D-001…D-022) |
| Mini-audit | [FP-0002-HEADER-MINI-AUDIT-v1.md](FP-0002-HEADER-MINI-AUDIT-v1.md) | Header-only composition cross-check |
| Blocks | [FP-0002-BLOCK-INVENTORY-v1.md](../FP-0002-BLOCK-INVENTORY-v1.md) | BLK-001 / BLK-002 scope |
| Engineering | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) §8.7 | Container model · dual-row law |
| Factory law | [layout-spec-law-v1.md](../../../../projects/mars-website-factory/layout-spec-law-v1.md) | Mandatory fields L-01…L-15 |
| Shell | [canonical-clean-shell-v1.md](../../../../projects/mars-website-factory/canonical-clean-shell-v1.md) | Pre-code gate |
| Visual gate | [operator-visual-approval-law-v1.md](../../../../projects/mars-website-factory/operator-visual-approval-law-v1.md) | Post-build gate (separate from this doc) |

**Evidence artefacts:** `REPORTS/_audit_extract_output.json` · `REPORTS/fp0002-component-extraction.json` (`top_bar_end_px: 180`)

**Honesty note:** Primary PDF files are **not present on disk** at `INCOMING/01_DESIGN/` in this session (README only). Composition below is derived from **A1 Design Audit (24/24 PDF READ)** and derived artefacts — **not** from a live PDF open in this task.

---

## 1. Scope

| In scope | Out of scope |
|----------|--------------|
| Desktop header composition for **PG-001…PG-010** standard templates | HTML · SCSS · JS · tokens · components · partials · build |
| Structural decomposition: rows · zones · groups · boundaries | Color · typography tokens · pixel-perfect measurements |
| Frozen vs SAFE UNKNOWN composition decisions | Mobile condensed header / hamburger overlay (separate future spec) |
| Header vs next-block separation | BLK-004 Mobile Sticky CTA Bar (separate block, not header stack) |
| Container / row model for assembly | Modal «Заказать звонок» layout (M-06) |
| Operator gate input before Phase C HTML | Operator Visual Acceptance of built HTML |

**Shell SSOT reference:** SOURCE-001 (`Главная страница (v2).pdf`) — canonical desktop header; identical chrome on SOURCE-005…021 desktop templates per Mini-Audit §2. **404 (SOURCE-023) is not shell SSOT.**

---

## 2. Visual Sources Used

| SOURCE-ID | File | Role in this spec |
|-----------|------|-------------------|
| **SOURCE-001** | `2026-06-11-home-v2/Главная страница (v2).pdf` | **Primary** — dual-row header composition SSOT |
| SOURCE-005…021 | Service · About · Contacts · Reviews · Blog · Article · Legal desktop PDFs | **Confirm** — same BLK-001+002 chrome (Mini-Audit §2) |
| SOURCE-025 | `Предварит структура и спрос.xlsx` | URL targets for nav / top-bar links |
| SOURCE-034 | Block Inventory v1 | BLK-001 / BLK-002 block boundaries |
| SOURCE-036 | Numeric Design Rules v2 | Header heights SAFE UNKNOWN register |
| SOURCE-041 | Production Standards v3 §8.7 | Container model · dual-row behavior |
| `_audit_extract_output.json` | PDF text/metrics extraction | Phone numbers · partial label decode · `top_bar_end_px` proxy |
| `fp0002-component-extraction.json` | Component scan | `top_bar_end_px: 180` (top row band boundary — **ESTIMATED**, not layout law) |

**Not used as composition SSOT:** SOURCE-003/004 (Home v1 superseded) · SOURCE-023/024 (404 minimal chrome) · mobile PDF pairs (Phase C.1 desktop-only scope).

---

## 3. Header Boundary Definition

### 3.1 Where Header **starts**

Header begins at the **top edge of the first horizontal band (TOP ROW / BLK-001)** — the utility top bar containing region labels, hours, utility links, and phones.

There is **no** content above BLK-001 on standard desktop templates (PG-001…PG-010).

### 3.2 Where Header **ends**

Header ends at the **bottom edge of the second horizontal band (MAIN ROW / BLK-002)** — below the primary navigation row and the «Заказать звонок» CTA button.

**Immediately below header (first pixel outside header):**

| Page context | Next block | Block ID |
|--------------|------------|----------|
| Home (PG-001) | Page Hero | BLK-007 |
| Inner pages (PG-002…010) | Breadcrumbs | BLK-005 |
| 404 (PG-011) | 404 Error Content | BLK-008 — **different chrome; not governed by this spec** |

### 3.3 Vertical envelope

| Boundary | Row | Block |
|----------|-----|-------|
| Top | TOP ROW top | BLK-001 |
| Row split | TOP ROW bottom → MAIN ROW top | BLK-001 → BLK-002 |
| Bottom | MAIN ROW bottom | BLK-002 |

**Two-row stack is mandatory on desktop.** Collapsing BLK-001 into BLK-002 as a single row is **forbidden**.

### 3.4 Horizontal envelope

| Layer | Model |
|-------|-------|
| Header `<header>` shell | **Full viewport width** — background band may extend edge-to-edge |
| Inner layout | **Shared page container** — max **1170px**, centered, horizontal padding **40px** desktop (Production Standards v3 · WF-GRID-001) |
| Rule | **Section + inner container** — not `header.container` as sole element (M2-B-020 GRID note) |

Both TOP ROW and MAIN ROW share the **same inner container width and horizontal alignment**.

---

## 4. Row Model

### 4.1 Row count

**2 rows** on desktop ≥ 1024px.

| Row | Name | Block ID | Exists |
|-----|------|----------|--------|
| **Row 1** | **TOP ROW** | FP-0002-BLK-001 | **YES** |
| **Row 2** | **MAIN ROW** | FP-0002-BLK-002 | **YES** |

No third row inside header. No sub-row nesting confirmed.

### 4.2 TOP ROW (BLK-001)

**Role:** Utility / contact / secondary IA band — visually **lighter** than MAIN ROW.

**Reading-order composition (left → right):**

```text
[Region Group] — [Hours Group] — [Utility Links Group] — [Phone Group]
```

| Segment | Content |
|---------|---------|
| Region Group | «Москва,» · «Московская область» |
| Hours Group | «пн-пт: 08:00-18:00, сб-вс 08:00-22:00» (single hours cluster — see §10) |
| Utility Links Group | «Генотипирование» · «Специалисты» |
| Phone Group | +7 (925) 183-64-64 · +7 (995) 023-92-26 |

**Row layout intent:** single horizontal band; groups separated by whitespace — **not** merged into one typographic line; **not** wrapped into MAIN ROW.

### 4.3 MAIN ROW (BLK-002)

**Role:** Primary brand + site IA + conversion CTA — visually **dominant** header band.

**Reading-order composition (left → right):**

```text
[Logo Group] — [Primary Nav Group] — [CTA Group]
```

| Segment | Content |
|---------|---------|
| Logo Group | Brand mark + brand text stack (see Group Model) |
| Primary Nav Group | 5 text links (horizontal list) |
| CTA Group | «Заказать звонок» button (single control) |

**Row layout intent:** logo group **anchors left**; nav occupies **central horizontal band**; CTA **isolated at right** — not inline inside nav list.

---

## 5. Zone Model

Zones are **composition territories** inside the header stack, top-to-bottom then left-to-right within each row.

| Zone | Row | Name | Groups contained | Visual weight |
|------|-----|------|------------------|---------------|
| **ZONE A** | TOP ROW | Utility Left | Region Group | Secondary |
| **ZONE B** | TOP ROW | Utility Center | Hours Group | Tertiary / meta |
| **ZONE C** | TOP ROW | Utility Right-Inner | Utility Links Group | Secondary links |
| **ZONE D** | TOP ROW | Utility Right-Outer | Phone Group | **Stronger than Zone B** — contact prominence |
| **ZONE E** | MAIN ROW | Brand Anchor | Logo Group | Primary anchor (left) |
| **ZONE F** | MAIN ROW | Primary IA | Primary Nav Group | Primary navigation |
| **ZONE G** | MAIN ROW | Conversion | CTA Group | Primary action (right) |

### Zone order (strict)

```text
ROW 1:  ZONE A → ZONE B → ZONE C → ZONE D
ROW 2:  ZONE E → ZONE F → ZONE G
```

**Forbidden zone moves:** placing CTA in TOP ROW · placing phones in MAIN ROW · placing Primary Nav in TOP ROW · placing Region/Hours in MAIN ROW · placing «Генотипирование» / «Специалисты» in Primary Nav Group.

---

## 6. Group Model

### GROUP 1 — Region Group (ZONE A)

**Состав:**

- region label «Москва,»
- region label «Московская область»

**Grouping logic:** Two region labels read as **one location-selector cluster** — visually paired, separated from hours and phones.

**Merged vs separate:** Stay **one group** — do **not** distribute regions to opposite ends of TOP ROW.

**Interaction:** Link vs static text — **SAFE UNKNOWN** (see §10).

---

### GROUP 2 — Hours Group (ZONE B)

**Состав:**

- hours string «пн-пт: 08:00-18:00, сб-вс 08:00-22:00» (machine-confirmed fragments)

**Grouping logic:** Single meta block — **visually subordinate** to Phone Group (Zone D).

**Merged vs separate:** **Separate** from Region Group and Phone Group — do **not** embed hours inside phone links.

**Note:** Footer uses different hours fragment (пн-pt 09:00–19:00) — **outside header scope**; do not merge footer hours into header composition.

---

### GROUP 3 — Utility Links Group (ZONE C)

**Состав:**

- link «Генотипирование» → `/uslugi/genotipirovanie/`
- link «Специалисты» → `/specyalisty/`

**Grouping logic:** Pair of **secondary utility links** — same band as top bar, **not** primary nav.

**Merged vs separate:** **One group** — keep adjacent; do **not** move either item to MAIN ROW nav.

**Visual separation from Group 4:** Whitespace gap before Phone Group — phones are **not** part of this group.

---

### GROUP 4 — Phone Group (ZONE D)

**Состав:**

- phone 1: +7 (925) 183-64-64
- phone 2: +7 (995) 023-92-26

**Grouping logic:** Two tel links as **one contact cluster** at the **outer right** of TOP ROW.

**Merged vs separate:** **One group** — stacked or inline pair **within the group** (exact inline vs stacked — **SAFE UNKNOWN**); do **not** split one number to MAIN ROW.

**Hierarchy:** Group is **visually stronger** than Hours Group (Zone B) and Region Group (Zone A).

---

### GROUP 5 — Logo Group (ZONE E)

**Состав:**

- logo mark (graphic — asset **PARTIAL**)
- brand title: «Центр профилактики и лечения зависимостей»
- brand subtitle: «(Шпиговский дом)»
- tagline candidate: «Лечение и профилактика» — **placement SAFE UNKNOWN**

**Grouping logic:** Mark + text stack = **one brand home unit** — links to `/`.

**Merged vs separate:** Logo mark and text **must stay one visual object** — do **not** detach title to nav row center.

**Vertical stack intent:** Mark left of text **or** mark above text — exact stack axis **SAFE UNKNOWN**; both belong to **same group**.

---

### GROUP 6 — Primary Nav Group (ZONE F)

**Состав (exactly 5 items, fixed order):**

1. «Услуги» → `/uslugi/`
2. «О центре» → `/o-centre/`
3. «Отзывы» → `/otzyvy/`
4. «Статьи» → `/blog/`
5. «Контакты» → `/kontakty/`

**Grouping logic:** Single **horizontal nav list** — equal-weight text links, **excluding** logo/home, **excluding** CTA button.

**Merged vs separate:** **One list group** — do **not** break into multiple nav clusters; do **not** add «Генотипирование» or «Специалисты» here.

**Items explicitly NOT in this group:** «Генотипирование» · «Специалисты» · «Заказать звонок» · logo/brand · phones · hours · regions.

---

### GROUP 7 — CTA Group (ZONE G)

**Состав:**

- button «Заказать звонок» (single control)

**Grouping logic:** **Isolated conversion control** — visually separated from nav text links.

**Merged vs separate:** **Separate** from Primary Nav Group — do **not** render as 6th nav link; do **not** move to TOP ROW.

**Behavior:** Modal / tel / external — **SAFE UNKNOWN** (M-06 · D-015) — **does not change composition placement**.

---

## 7. Visual Hierarchy

| Level | Elements | Dominance |
|-------|----------|-----------|
| **1 — Primary** | MAIN ROW overall · Logo Group · Primary Nav Group · CTA button | Largest band; drives page IA |
| **2 — Secondary** | TOP ROW overall · Phone Group · Utility Links Group | Smaller type band; contact + utility |
| **3 — Tertiary** | Region Group · Hours Group | Meta / locale context |

**Within MAIN ROW:**

1. CTA button — strongest **action** accent (right)
2. Logo Group — strongest **brand** anchor (left)
3. Primary Nav — horizontal link band (center) — **between** brand and CTA

**Within TOP ROW:**

1. Phone Group — strongest (contact)
2. Utility Links Group — secondary links
3. Region Group — locale context
4. Hours Group — weakest meta text

**Cross-row rule:** MAIN ROW **must visually dominate** TOP ROW (taller band, larger logo/nav scale). Agent **must not** invert hierarchy (e.g. equal-height rows, phones larger than logo).

---

## 8. Header vs Non-Header Separation

### 8.1 Inside Header (must be assembled in `<header>` stack)

| Element | Row | Group |
|---------|-----|-------|
| Region labels | TOP | Region Group |
| Hours | TOP | Hours Group |
| Генотипирование · Специалисты | TOP | Utility Links Group |
| Two phones | TOP | Phone Group |
| Logo + brand text | MAIN | Logo Group |
| Five primary nav links | MAIN | Primary Nav Group |
| «Заказать звонок» button | MAIN | CTA Group |

### 8.2 Outside Header — **NEXT BLOCK** (must **not** be placed inside header)

| Element | Block ID | Relationship to header |
|---------|----------|------------------------|
| **Breadcrumbs** | BLK-005 | **Immediately below** header on PG-002…010 — **not** part of header |
| **Page Hero** | BLK-007 | **Below** header on Home — **not** part of header (**HEADER ≠ HERO**) |
| **In-page anchor navigation** | BLK-006 | Below hero/breadcrumbs on service/about pages |
| **Search** | — | **Not in design** — do not add to header |
| **Mobile Sticky CTA Bar** | BLK-004 | **Separate fixed bottom chrome** — not header stack |
| **Footer** | BLK-003 | Page bottom — separate block |
| **Service navigation / hub cards** | BLK-011 etc. | Page body |
| **Legal utility in footer** | BLK-003 | «Правовая информация» — footer, **not** header nav |

### 8.3 Common FP-0002 Header Failure guards

| Failure mode | Prevention rule |
|--------------|-----------------|
| Breadcrumb inside header | BLK-005 starts **after** BLK-002 bottom edge |
| Hero merged into header | BLK-007 starts **after** header boundary on PG-001 |
| Single-row collapse | BLK-001 and BLK-002 remain **two rows** |
| Specialists in main nav | «Специалисты» stays TOP ROW only |
| CTA as nav link | CTA stays GROUP 7 — separate from GROUP 6 |
| Phones in main row | Phones stay TOP ROW GROUP 4 only |

---

## 9. Frozen Decisions

These composition choices **must not be changed** by implementation agent without Layout Spec **REVISE**:

| ID | Decision |
|----|----------|
| FD-01 | **Dual-row header** — exactly **2 rows** on desktop; BLK-001 above BLK-002 |
| FD-02 | **TOP ROW contains only** Region · Hours · Utility links · Phones — nothing from MAIN ROW |
| FD-03 | **MAIN ROW contains only** Logo group · 5 nav links · CTA — nothing from TOP ROW |
| FD-04 | **Five primary nav labels** — Услуги · О центре · Отзывы · Статьи · Контакты — fixed set and order |
| FD-05 | **«Генотипирование» and «Специалисты»** — TOP ROW utility links only — **not** in primary nav |
| FD-06 | **Two phone numbers** — both in TOP ROW Phone Group |
| FD-07 | **«Заказать звонок»** — MAIN ROW CTA Group only — **not** in TOP ROW |
| FD-08 | **Logo + brand text** — single Logo Group at MAIN ROW left — home link to `/` |
| FD-09 | **Breadcrumbs (BLK-005)** — **outside** header — below BLK-002 |
| FD-10 | **Hero (BLK-007)** — **outside** header on Home |
| FD-11 | **Same header chrome** on PG-001…PG-010 desktop templates |
| FD-12 | **Shared 1170px inner container** for both rows |
| FD-13 | **404 page** — not used as header composition SSOT |
| FD-14 | **No hamburger / mobile menu** in desktop ≥1024px composition |
| FD-15 | **No search field** in header — not in Visual SSOT |

---

## 10. SAFE UNKNOWN

Composition gaps — agent **must not silently invent structure** to fill:

| ID | Topic | Impact |
|----|-------|--------|
| SU-01 | Exact **pixel heights** of TOP ROW / MAIN ROW / total stack | Cannot lock hero offset; use engineering placeholder only after APPROVED |
| SU-02 | **Sticky header** on scroll (yes/no/shrink) | Does not change row model; behavior deferred |
| SU-03 | **«Лечение и профилактика»** — inside Logo Group vs omitted vs TOP ROW | Brand stack assembly |
| SU-04 | Logo **graphic asset** (SVG/PNG) — SOURCE-026 empty | Placeholder policy at implementation — not composition |
| SU-05 | Region labels — **links vs static text** | TOP ROW interaction |
| SU-06 | Hours — **one shared string vs per-region pairs** | Mini-Audit: text layer suggests **once** — operator confirm |
| SU-07 | Phone pair — **inline horizontal vs stacked** within Phone Group | TOP ROW micro-layout |
| SU-08 | Exact **horizontal gaps** between zones A–D and E–G | Spacing tokens deferred |
| SU-09 | Logo Group — mark **left of** vs **above** text stack | MAIN ROW micro-layout |
| SU-10 | Primary Nav — exact **center alignment math** (flex center vs space-between) | MAIN ROW micro-layout — groups fixed, math open |
| SU-11 | CTA button exact dimensions | CTA presence and zone fixed; size deferred |
| SU-12 | «Заказать звонок» **click behavior** (M-06 · D-015) | Does not move CTA zone |
| SU-13 | **Mobile / ≤1023px** header composition (condensed · hamburger) | Separate Layout Spec scope |
| SU-14 | **Hover / focus / active** nav visual states | Interaction styling deferred |
| SU-15 | PDF files **not on disk** for operator re-open in this session | Operator visual compare should use archived PDFs or re-intake |
| SU-16 | TOP ROW micro-order when viewport narrows (1024–1199) | Wrap/truncate strategy deferred — **rows must not collapse** |

---

## 11. Layout Diagram

### 11.1 Desktop composition (≥ 1024px) — ASCII

```text
┌────────────────────────────────── HEADER (BLK-001 + BLK-002) ──────────────────────────────────┐
│  full-bleed background band (viewport width)                                                    │
│  ┌──────────────────────────── inner container max 1170 · pad-x 40 ────────────────────────────┐│
│  │                                                                                              ││
│  │  ROW 1 — TOP ROW (BLK-001) · utility band · secondary visual weight                          ││
│  │  ┌──────────────┐  ┌─────────────────────────┐  ┌──────────────────┐  ┌───────────────────┐ ││
│  │  │ ZONE A       │  │ ZONE B                  │  │ ZONE C           │  │ ZONE D            │ ││
│  │  │ Region Group │  │ Hours Group             │  │ Utility Links    │  │ Phone Group       │ ││
│  │  │              │  │                         │  │ Group            │  │                   │ ││
│  │  │ Москва,      │  │ пн-пт 08:00-18:00       │  │ Генотипирование  │  │ +7 925 183-64-64  │ ││
│  │  │ Московская   │  │ сб-вс 08:00-22:00       │  │ Специалисты      │  │ +7 995 023-92-26  │ ││
│  │  │ область      │  │                         │  │                  │  │                   │ ││
│  │  └──────────────┘  └─────────────────────────┘  └──────────────────┘  └───────────────────┘ ││
│  │                                                                                              ││
│  │  ROW 2 — MAIN ROW (BLK-002) · primary band · dominant visual weight                          ││
│  │  ┌────────────────────────────┐  ┌────────────────────────────────────┐  ┌───────────────┐ ││
│  │  │ ZONE E                     │  │ ZONE F                             │  │ ZONE G        │ ││
│  │  │ Logo Group                 │  │ Primary Nav Group                  │  │ CTA Group     │ ││
│  │  │                            │  │                                    │  │               │ ││
│  │  │ [mark] Центр профилактики  │  │ Услуги · О центре · Отзывы ·       │  │ [ Заказать    │ ││
│  │  │        и лечения           │  │ Статьи · Контакты                  │  │   звонок ]    │ ││
│  │  │        зависимостей        │  │                                    │  │               │ ││
│  │  │        (Шпиговский дом)    │  │                                    │  │               │ ││
│  │  └────────────────────────────┘  └────────────────────────────────────┘  └───────────────┘ ││
│  │                                                                                              ││
│  └──────────────────────────────────────────────────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
         │ header ends here │
         ▼
┌──────────────── NEXT BLOCK (NOT HEADER) ────────────────┐
│  PG-001 Home:        BLK-007 Page Hero                  │
│  PG-002…010 Inner:   BLK-005 Breadcrumbs                │
└─────────────────────────────────────────────────────────┘
```

### 11.2 Row summary strip

```text
ROW 1 (TOP ROW)
[Москва, Московская область] [hours] [Генотипирование · Специалисты] [phone 1 · phone 2]

ROW 2 (MAIN ROW)
[[mark] Brand title + subtitle] [Услуги · О центре · Отзывы · Статьи · Контакты] [Заказать звонок]
```

---

## 12. Implementation Readiness

| Gate | Verdict | Notes |
|------|---------|-------|
| Layout Spec filed | **YES** | This document |
| Operator APPROVED | **NO** | **STOP** — awaiting APPROVED \| REVISE |
| Composition sufficient for assembly | **YES WITH UNKNOWN** | Row/zone/group model locked; SU-01…SU-16 open |
| HTML/CSS permitted | **NO** | Forbidden until operator **APPROVED** per Layout Spec Law §3 |
| Operator Visual Review | **N/A** | Runs **after** implementation — separate gate |
| Logo asset ready | **NO** | SU-04 — non-blocking for spec gate |
| PDF on disk re-verify | **NO** | SU-15 — operator should compare against SOURCE-001 PDF |

**Post-approval implementation must cite:**

```text
LAYOUT SPEC REF — FP-0002-HEADER-LAYOUT-SPEC-v1.md — APPROVED <date>
LAYOUT SPEC GATE — PASS (APPROVED)
```

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Status | **DRAFT** |
| Supersedes | — (first Header Layout Spec) |
| Related | FP-0002-HEADER-MINI-AUDIT-v1.md (content audit — **not** substitute) |
| Commit / push | Not performed |

---

**Operator gate request:**

Layout Spec готов для **Header (BLK-001 + BLK-002, desktop ≥1024px)**.  
Проверьте декомпозицию против Visual SSOT (SOURCE-001 + matching templates).  
Требуется решение: **APPROVED** или **REVISE**.  
Верстка запрещена до **APPROVED**.
