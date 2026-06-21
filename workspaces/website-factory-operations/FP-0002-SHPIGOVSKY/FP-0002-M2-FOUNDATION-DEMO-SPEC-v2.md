# FP-0002 — M2 Foundation Demo Spec v2

**Document type:** Project implementation specification — M2 Foundation pass only  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-14  
**Status:** **ISSUED** — canonical M2 spec under post–RESET governance  

**Supersedes:** `FP-0002-M2-FOUNDATION-DEMO-SPEC-v1.md` — **INVALIDATED**; do not read, restore, or cite.

**Scope:** Specification only. **No** HTML, SCSS, JS, workspace edits, or QA REPORT filing in this document.

**Entry URL:** `workspaces/fp-0002-shpigovsky-frontend/` · foundation page **`ui-demo.html`** · build output **`dist/ui-demo.html`**

**Authority stack (read before implement):**

| Rank | Document |
|------|----------|
| 1 | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) |
| 2 | [frontend-production-authority-order-v1.md](../../../projects/mars-website-factory/frontend-production-authority-order-v1.md) OL-01–OL-07 |
| 3 | Factory gates — Shell-first, Visual Foundation, Calibration, Foundation QA, Enforcement |
| Project | [FP-0002-EXECUTION-BRAIN-v1.md](FP-0002-EXECUTION-BRAIN-v1.md) · [FP-0002-EXCEPTION-REGISTRY-v1.md](FP-0002-EXCEPTION-REGISTRY-v1.md) |
| Contract | [FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md](FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md) · [FP-0002-FRONTEND-START-SEQUENCE-v1.md](FP-0002-FRONTEND-START-SEQUENCE-v1.md) |

**Preconditions (operator — agent must not self-authorize):**

| ID | Requirement |
|----|-------------|
| PRE-01 | Production Standards v3 **APPROVED WITH ANDREY CORRECTIONS** |
| PRE-02 | Charter v1 **ISSUED** · Mapping QA **PASS WITH NOTES** |
| PRE-03 | PRE-M2 frontend restored — M1 scaffold only |
| PRE-04 | Operator **authorization** for new M2 pass received |
| PRE-05 | Agent read Execution Brain + this spec + Exception Registry |

---

## 1. Purpose

This spec defines **exactly** what M2 must deliver: shell + Visual Foundation demo + global tokens + desktop/mobile chrome — **nothing else**.

M2 **is not** Home production. M2 **is not** design exploration. Every block below is **prescriptive**; values come only from cited authority rows.

**Implementation rule:** If a value, component, or section is **not** listed as **FOUNDATION ENTITY** below → **do not implement**.

---

## 2. Foundation Demo Audit

Revision of Foundation Demo composition after FP-0002 RESET, Enforcement Pack, Compliance Decision Model, Failure Attribution Model, Exception Registry, and Execution Brain.

### 2.1 What must be in Foundation Demo?

| # | Obligation | Authority |
|---|------------|-----------|
| A-01 | Page entry **`ui-demo.html`** with `header` + `main` + `footer` — **not** `index.html` Home | Start Sequence Step 1 · Charter SC-02 |
| A-02 | **Shell chrome:** BLK-001, BLK-002, BLK-003, BLK-004 (mobile only) | Charter §6 · v3 §8.1/8.7–8.9 |
| A-03 | **All** Visual Foundation Contract §3 categories rendered inside `main` | [frontend-visual-foundation-contract-v1.md](../../../projects/mars-website-factory/frontend-visual-foundation-contract-v1.md) §3 |
| A-04 | **v3 tokens wired** in `src/scss` — container 1170, padding 40/20, Inter, colors, radius 30/10/999, spacing scale | v3 §2–§9 · Execution Brain §4 |
| A-05 | **Spacing demo labels:** same-bg **80px**, band **240px**, mobile inter-section **64px** | v3 §6.2 · Start Sequence Step 2 |
| A-06 | **Desktop-first** CSS — layout switch `@1024px` | v3 §9 · Charter §7 |
| A-07 | **WF-GRID** section ≠ container on every demo section and shell region | WF-GRID-DISCIPLINE-v1 |
| A-08 | **RU typography law** — typograph visible copy; forbidden break CSS absent | v3 §4.3 · OL-06/OL-07 |
| A-09 | **Exception Registry** cited for every v3 spacing token that appears in compiled CSS off OL-01 scale | Exception Registry §2 · Compliance CASE B→C |
| A-10 | **Design Calibration** + **Foundation QA** after Steps 1–6 — not part of coding scope but **blocks M2 close** | Shell-first Phase 4b–5 |

### 2.2 What must NOT be in Foundation Demo?

| # | Exclusion | Reason |
|---|-----------|--------|
| X-01 | **`index.html`** as Home | Charter SC-02 · Start Sequence Step 8 gate |
| X-02 | **PG-001** page production | Phase 8 only after Foundation QA PASS |
| X-03 | **BLK-007** Page Hero and any Home-marketing section | HEADER ≠ HERO · Charter G-04 |
| X-04 | **BLK-009, 010, 014, 015, 018, 019, 020, 021, 022, 023, 024, 026, 027, 034, 035** as page sections | Home / inner-page blocks — Block Inventory |
| X-05 | **BLK-005** Breadcrumbs, **BLK-006** Anchor nav, **BLK-017** Pagination as demo sections | Not in Visual Foundation §3; page-context chrome |
| X-06 | **G-SERVICE** template bodies (BLK-011/012/013) | Page-level — PG-002+ |
| X-07 | **Article TOC 280px** sidebar layout demo | PG-009 placeholder — v3 §3.6 page layout, not foundation |
| X-08 | **New components** not in v3 §8 or Visual Foundation §3 | Agent invention forbidden |
| X-09 | **Deprecated radius** 4/8/12/16/24 px scale | v3 §7 deprecated list |
| X-10 | **Mobile-first** base without Lead waiver | v3 §9 · Charter §7 |
| X-11 | **Design Completeness** full-page entity audit | Post–Home gate — [frontend-design-completeness-governance-v1.md](../../../projects/mars-website-factory/frontend-design-completeness-governance-v1.md) §11 |
| X-12 | Reuse of destroyed **M2 Spec v1** | Reset report · Execution Brain M-MUST-NOT-13 |

### 2.3 What must be combined?

| Combine | Rationale |
|---------|-----------|
| **Typography tiers H1–H4 + body-sm + caption** → **one** demo section `M2-B-010` | Single Visual Foundation §3.1 surface; avoids fragmenting QA |
| **Primary + header-callback + text/link buttons** → **one** button section `M2-B-012` | v3 §8.1 defines variants; one WF-GRID section |
| **Input + textarea + select + checkbox + radio + validation** → **one** form section `M2-B-013` | Visual Foundation §3.2 single form family |
| **Secondary + outline + disabled** button states → **inside** `M2-B-012` | Visual Foundation §3.3 — not separate sections |
| **Info + error alerts** → **one** alert strip `M2-B-018` | Visual Foundation §3.4 |
| **Image + video wrapper** → **one** media section `M2-B-019` | Visual Foundation §3.5 |
| **Global tokens + reset + default content styles** → **one** global pass `M2-B-005` | Start Sequence Step 5 — single token authority in `_variables.scss` + base SCSS |

### 2.4 What must be split?

| Split | Rationale |
|-------|-----------|
| **Shell chrome** (BLK-001/002/003/004) **vs** **`main` demo content** | Shell-first protocol · layout-shell-governance HEADER ≠ HERO |
| **Spacing demos:** same-bg **80px** · band **240px** · mobile **64px** → **three** labeled sections `M2-B-016a/b/c` | v3 §6.2 distinct tokens; Factory single-boundary rule per context |
| **Desktop shell** (Steps 3–4) **vs** **mobile shell** (Step 6) | Start Sequence order — do not defer mobile sticky to Home |
| **Design Calibration** **vs** **Foundation QA** | Separate gates — Calibration before QA REPORT |
| **DQ-02a** (SSOT token presence) **vs** **DQ-02b** (Operator Law / compiled CSS) | Execution Brain L-09 — independent checks |

### 2.5 What is Foundation?

**Foundation** = everything required to close Start Sequence Steps **1–7** without page-level production:

```text
Production SSOT (v3) frozen in SCSS
        ↓
Shell partials (header / main / footer) + BLK-004
        ↓
ui-demo.html — Visual Foundation Contract §3 inside main
        ↓
Global styles (Inter, colors, radius, spacing, content defaults)
        ↓
Desktop + mobile shell behavior
        ↓
Design Calibration → Foundation QA → ROOT COMPLIANCE PASS
```

**Foundation entities** are tagged **FOUNDATION ENTITY** in §4. **NOT FOUNDATION ENTITY** rows are **explicit bans** for M2 code.

### 2.6 What belongs to Home and is forbidden in M2?

| Home / page artifact | Block / Page ID | M2 status |
|----------------------|-----------------|-----------|
| Home page entry | **PG-001** / `index.html` | **FORBIDDEN** |
| Page Hero | **BLK-007** | **FORBIDDEN** |
| UTP Value Cards | **BLK-009** | **FORBIDDEN** |
| Home Services Preview | **BLK-010** | **FORBIDDEN** |
| Feature cards «Нас выбирают» | **BLK-014** | **FORBIDDEN** |
| Reviews preview | **BLK-015** | **FORBIDDEN** |
| Rehabilitation steps | **BLK-018** | **FORBIDDEN** |
| Guest Visit CTA section | **BLK-019** | **FORBIDDEN** |
| Program four directions | **BLK-020** | **FORBIDDEN** |
| Genotyping detail | **BLK-021** | **FORBIDDEN** |
| Expert opinion | **BLK-022** | **FORBIDDEN** |
| Comfort block | **BLK-023** | **FORBIDDEN** |
| Video section | **BLK-024** | **FORBIDDEN** |
| Home articles preview | **BLK-027** | **FORBIDDEN** |
| Home FAQ accordion **as page section** | **BLK-034** in Home scroll | **FORBIDDEN** — FAQ **demo sample** in `main` is allowed (Visual Foundation) |
| Contact form **as page section** | **BLK-035** in Home scroll | **FORBIDDEN** — form **demo fields** in `main` allowed |
| Any Home v2 scroll block order | Charter §13.3 | **FORBIDDEN** until Phase 8 |

**Allowed overlap:** BLK-001/002/003/004 are **shell** — shared with all pages, not Home-specific. FAQ/form **UI primitives** in foundation demo are **not** BLK-034/035 page sections.

---

## 3. M2 execution model

### 3.1 Start Sequence mapping

| Step | Spec blocks | Stop for Lead ack after |
|------|-------------|-------------------------|
| **1** Shell frame | M2-B-001, M2-B-002 | Step 1 complete |
| **2** Visual Foundation in `main` | M2-B-010 … M2-B-019 | Step 2 complete |
| **3** Desktop header | M2-B-020, M2-B-021 | Step 3 complete |
| **4** Desktop footer | M2-B-022 | Step 4 complete |
| **5** Global styles | M2-B-003, M2-B-005 | Step 5 complete |
| **6** Mobile shell | M2-B-026, M2-B-027, M2-B-028 | Step 6 complete |
| **7** QA gates | §5 Compliance Strategy · §6 Failure Traps | Foundation QA REPORT + Lead ack |

**Build rule:** `npm run build` after each step; edit **`src/` only**.

**Layout chain (every section):** Design Source (frozen v3) → **WF-GRID** → **WF-LAYOUT** → inferred LP from Normalization §6 + v3 §3 → HTML. **No Design→HTML shortcut.**

### 3.2 WF-GRID contract (all FOUNDATION sections)

| Rule | Implementation |
|------|----------------|
| WF-GRID-001 | Outer `<section class="…">` — background, vertical rhythm; inner `.container` — max-width **1170px**, padding-x **40px** desktop / **20px** mobile |
| WF-GRID-002 | One page grid contract — header, demo sections, footer share same container math |
| WF-GRID-004 | Wide/band sections: background **100vw**; inner content still in container **1170** |

### 3.3 WF-LAYOUT patterns (named — no eyeball %)

| Demo context | Pattern | v3 binding |
|--------------|---------|------------|
| Card sample grid | **LP-CARD-GRID-3** — `repeat(3, 1fr)` desktop · `1fr` mobile · **gap 24px** (`space-6`) | §3.6 · §8.3 |
| Form two-column | **LP-FORM-2COL** — `repeat(2, 1fr)` desktop · `1fr` mobile · **gap 16px** (`space-4`) | §3.6 · §8.2 |
| Footer desktop columns | **LP-FOOTER-MULTI** — `fr` columns per footer charter; **no** 65/35 % splits | §8.8 · OL-04 |
| Header rows | **LP-HEADER-DUAL-ROW** — BLK-001 stack above BLK-002 | §8.7 |
| Article TOC | **NOT IN M2** | §3.6 PG-009 only |

---

## 4. M2 blocks — canonical register

**Legend — relevance columns:**

| Column | Meaning |
|--------|---------|
| **DC** | Design Completeness — N/A at M2 (foundation slice only); full audit post–Home |
| **VF** | Visual Foundation Contract §3 |
| **GRID** | WF-GRID-DISCIPLINE-v1 |
| **LAY** | WF-LAYOUT-DISCIPLINE-v1 |
| **OL** | Operator Law — spacing/type; v3 tokens via Exception Registry |

---

### M2-B-001 — Foundation page entry

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Single non-Home Gulp entry compiling shell + demo sections |
| **Authority** | Start Sequence Step 1 · Charter §5.1 · Visual Foundation §1.1 |
| **Acceptance criteria** | `src/pages/ui-demo.html` exists; `@@include` layout partials; **`main` only** holds §4 demo blocks; **`dist/ui-demo.html`** builds; **no** `index.html` Home |
| **Non-goals** | Home routing; multi-page sitemap; PG-* sections |
| **DC** | N/A — foundation URL only |
| **VF** | Required — hosts §3 composition |
| **GRID** | Page obeys WF-GRID-002 one contract |
| **LAY** | N/A at entry |
| **OL** | N/A |

---

### M2-B-002 — Layout shell skeleton

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Semantic frame: `head`, `header`, `main`, `footer` partials wired before content |
| **Authority** | Shell-first Phase 1 · Charter §6.1 · layout-shell-governance |
| **Acceptance criteria** | Partials: `head.html`, `header.html`, `footer.html`; `main` landmark empty until Step 2; build green |
| **Non-goals** | BLK-007 hero inside header; page sections in shell partials |
| **DC** | N/A |
| **VF** | Prerequisite G-VF-02 |
| **GRID** | Header/footer use section+container pattern |
| **LAY** | LP-HEADER-DUAL-ROW placeholder structure |
| **OL** | N/A |

---

### M2-B-003 — Production token SCSS wiring

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Replace M1 placeholder with full v3 token map in `utils/_variables.scss` (or project-equivalent) |
| **Authority** | v3 §2–§9 · Execution Brain §4 · Charter §3.3 |
| **Acceptance criteria** | All tokens listed Execution Brain §4 present as SCSS variables; **no** deprecated radius scale; spacing tokens `space-0`…`space-16` per v3 §6.1 |
| **Non-goals** | New tokens; rem/em font-size stacks; agent-rounded values |
| **DC** | N/A |
| **VF** | Enables all §3 samples |
| **GRID** | `container-max: 1170px`; `page-padding-x` 40/20 |
| **LAY** | Grid gap tokens for LP patterns |
| **OL** | Values off OL-01 **only** via v3 token + Exception Registry EX-001…EX-010 |

**Mandatory token spot-check list:** 1170 · 40/20 padding · `#475371` · `#B3261E` · `rgba(218,229,240,0.7)` · Inter · 30/10/999 radius · H2 36/22 w500 · body 18/16 w300.

---

### M2-B-005 — Global reset and default content styles

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Desktop-first base: reset, box model, link defaults, list defaults, table defaults, quote defaults |
| **Authority** | Start Sequence Step 5 · v3 §4 · Shell-first Phase 2 |
| **Acceptance criteria** | `@1024px` desktop base; mobile overrides `max-width: 1023px`; **no** forbidden typography properties; min viewport **320px** |
| **Non-goals** | Page-specific block styles; Home hero styles |
| **DC** | N/A |
| **VF** | Supports §3.1 lists/links/blockquote/table |
| **GRID** | Body/page background layers per v3 §3.3 model |
| **LAY** | N/A |
| **OL** | OL-05: line-heights from v3 §4.1 tiers (**NEX-04** — no registry); OL-06 forbidden props absent |

---

### M2-B-010 — Typography scale demo

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Render v3 type tiers inside one labeled demo section |
| **Authority** | Visual Foundation §3.1 · v3 §4.1 |
| **Acceptance criteria** | Visible samples: **H1** 70/42 lh 84/50 w500 · **H2** 36/22 lh 44/28 w500 · **H3** 30/22 · **H4** 20/18 · **body** 18/16 w300 lh 28/24 · **body-sm** 16 · **caption** 12; Russian typographed copy in headings/body |
| **Non-goals** | H5/H6 unless added to demo — **optional** per VF «if in standards» — v3 §4.1 has no H5/H6 rows → **omit H5/H6**; agent-invented display sizes |
| **DC** | N/A at M2 |
| **VF** | **Required** §3.1 |
| **GRID** | Section + container |
| **LAY** | Single column content stack |
| **OL** | Line-heights = v3 named tiers (**PASS** OL-05); no `letter-spacing` |

---

### M2-B-011 — Lists, links, blockquote

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Prose patterns: `ul`, `ol`, nested list, inline link, blockquote |
| **Authority** | Visual Foundation §3.1 · v3 Quote tier §4.1 |
| **Acceptance criteria** | One `ul`, one `ol`, nested sample, inline text link with visible `:focus`/`:hover`, blockquote at quote tier 18/16 w300 |
| **Non-goals** | Nav menu samples (header handles nav); breadcrumb links |
| **DC** | N/A |
| **VF** | **Required** §3.1 |
| **GRID** | Inside container |
| **LAY** | Single column |
| **OL** | List spacing via `space-4` (16px) — cite **EX-004** in REPORT when compiled |

---

### M2-B-012 — Button family demo

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | All button variants needed before Home CTAs |
| **Authority** | Visual Foundation §3.3 · v3 §8.1 |
| **Acceptance criteria** | **Primary CTA:** h **44px**, px **32px** (`space-7`), min-width **280px**, radius **30px**, font 16/500 lh 20, fill `#B3261E`, text `#FFFFFF` · **Header callback sample:** h **40px**, px **24px** (`space-6`), radius **30px**, font 14/500, same fill as primary · **Text/link CTA:** 16/500 `#B3261E`, no fill · **Secondary:** fill `#F1F5F9` (`color-bg-elevated`), text `#475371`, border 1px `#CBD4E0`, radius **30px**, same h **44px** as primary · **Outline:** transparent fill, border 1px `#B3261E`, text `#B3261E`, radius **30px**, h **44px** · **Disabled:** primary variant at **50% opacity**, `pointer-events: none` · Hover primary only: darken **8%** on `#B3261E` (engineering) |
| **Non-goals** | Sticky mobile bar buttons (BLK-004 separate); invented pill sizes |
| **DC** | N/A |
| **VF** | **Required** §3.3 |
| **GRID** | Section + container |
| **LAY** | Inline flex row for variant row — gap per `space-4` |
| **OL** | Padding/gap 24/32px — **EX-005**, **EX-006** |

---

### M2-B-013 — Form family demo

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Form controls with validation state — not BLK-035 page section |
| **Authority** | Visual Foundation §3.2 · v3 §8.2 |
| **Acceptance criteria** | Text input h **48px**, padding **16px** x / **12px** y (`space-4`/`space-3`), radius **10px**, border 1px `#BCC6D5`, vertical gap **16px** · Textarea min-h **128px** · Select (native styled) · Checkbox labeled · Radio group ≥2 · One field `.has-error` (or equivalent) with error color `#B3261E` · Label gap **8px** below label (`space-2` — **EX-002**) · Optional success state `#2E7D52` placeholder |
| **Non-goals** | Full BLK-035 two-column contact section as page block; modal form; tel: submit wiring |
| **DC** | N/A |
| **VF** | **Required** §3.2 |
| **GRID** | Section + container |
| **LAY** | **LP-FORM-2COL** on desktop for field pairs |
| **OL** | 8/12/16px spacing — **EX-002**, **EX-003**, **EX-004** |

---

### M2-B-014 — Card surface sample

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | One card proving radius, border, padding, grid gap — not service catalog |
| **Authority** | Visual Foundation §3.4 · v3 §8.3 |
| **Acceptance criteria** | Min **one** card + **3-up grid** desktop / **1-col** mobile; padding **24px**; border 1px `#CBD4E0`; radius **30px**; gap **24px**; flat shadow none; placeholder 16:10 image area allowed |
| **Non-goals** | BLK-010/011 service cards content; specialist cards BLK-026 |
| **DC** | N/A |
| **VF** | **Required** §3.4 Cards |
| **GRID** | Section + container |
| **LAY** | **LP-CARD-GRID-3** |
| **OL** | gap/padding 24px — **EX-005** |

---

### M2-B-015 — FAQ accordion demo

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | FAQ UI primitive — not Home FAQ section scroll block |
| **Authority** | Visual Foundation §3.4 · v3 §8.4 · C-10 engineering default single-open |
| **Acceptance criteria** | ≥2 items; item gap **16px**; panel radius **30px**; chevron **16px**; single-open behavior; accordion or `<details>` |
| **Non-goals** | BLK-034 Home copy; coordinator-final accordion policy |
| **DC** | N/A |
| **VF** | **Required** §3.4 FAQ |
| **GRID** | Section + container |
| **LAY** | Single column stack |
| **OL** | gap 16px — **EX-004** |

---

### M2-B-016a — Spacing demo: same-background 80px

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Visible proof of `section-gap-same-bg` / `space-12` single-boundary rule |
| **Authority** | v3 §6.2 · section-spacing-rule · Start Sequence Step 2 |
| **Acceptance criteria** | Two adjacent sections **same** `bg-page` or `bg-base`; **one** boundary gap **80px** — **not** top+bottom double stack; **visible label** text: `same-bg gap: 80px (space-12)` |
| **Non-goals** | Inferring gap from PDF blocks |
| **DC** | N/A |
| **VF** | **Required** §3.4 Spacing examples |
| **GRID** | Two WF sections same role |
| **LAY** | N/A |
| **OL** | 80px — **EX-009** |

---

### M2-B-016b — Spacing demo: band transition 240px

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Major band transition token |
| **Authority** | v3 §6.2 `section-gap-band` · Execution Brain §4.3 |
| **Acceptance criteria** | Background role change (e.g. wash → footer-tone band); gap **240px**; label: `band transition: 240px (space-16)` |
| **Non-goals** | Hero exit bands (BLK-007) |
| **DC** | N/A |
| **VF** | **Required** §3.4 diff-bg / band |
| **GRID** | Full-bleed background allowed on outer section |
| **LAY** | N/A |
| **OL** | 240px — **EX-010** |

---

### M2-B-016c — Spacing demo: mobile inter-section 64px

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Mobile reduction token visible at ≤1023px |
| **Authority** | v3 §6.2 `section-gap-mobile` · Start Sequence Step 6 |
| **Acceptance criteria** | At `max-width: 1023px`, labeled demo shows **64px** inter-section gap; label: `mobile inter-section: 64px (space-11)` |
| **Non-goals** | Desktop 64px as default section rhythm |
| **DC** | N/A |
| **VF** | **Required** (mobile spacing sample) |
| **GRID** | Standard sections |
| **LAY** | N/A |
| **OL** | 64px — **EX-008** |

---

### M2-B-017 — Data table sample

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Simple table — project uses tables (blog/legal) |
| **Authority** | Visual Foundation §3.4 · v3 implied via blog/legal pages |
| **Acceptance criteria** | `<table>` with header row + body rows; readable at desktop; stacks or scroll policy at mobile — **engineering:** horizontal scroll wrapper allowed; typographed cell copy |
| **Non-goals** | Article complex tables BLK-030; pricing tables |
| **DC** | N/A — entity presence on foundation only |
| **VF** | **Required** (project uses tables) |
| **GRID** | Container-constrained |
| **LAY** | Single column |
| **OL** | Cell padding via approved tokens only |

---

### M2-B-018 — Alert samples

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Semantic info + error surfaces |
| **Authority** | Visual Foundation §3.4 · v3 §5.2 placeholders |
| **Acceptance criteria** | **Info** alert: background `#F1F5F9`, border 1px `#C6CEDA`, text `#475371` · **Error** alert: background `#FFFFFF`, border 1px `#B3261E`, text `#B3261E` · Both use radius **30px**, padding **24px** (`space-6`), typographed RU sample copy |
| **Non-goals** | Toast system; modal alerts |
| **DC** | N/A |
| **VF** | **Required** §3.4 Alerts |
| **GRID** | Section + container |
| **LAY** | Stack gap `space-4` |
| **OL** | Spacing via EX-004 |

---

### M2-B-019 — Media samples

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Image + video embed shell |
| **Authority** | Visual Foundation §3.5 |
| **Acceptance criteria** | One `<img>` with **alt** (placeholder policy OK) · One **16:9** video wrapper (empty iframe or `<video>` shell) · **no** autoplay violation |
| **Non-goals** | BLK-024 Home video section; real hosted video |
| **DC** | N/A |
| **VF** | **Required** §3.5 |
| **GRID** | Container; full-bleed image optional inside section |
| **LAY** | N/A |
| **OL** | N/A |

---

### M2-B-020 — BLK-001 Header Top Bar (desktop)

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Desktop top bar chrome |
| **Authority** | v3 §8.7 · Block Inventory BLK-001 · Charter §6 |
| **Acceptance criteria** | Row visible ≥1024px: region, генотипирование link stub, hours, specialists link stub, phones; container **1170**; padding-x **40px**; typographed RU labels; heights **SAFE UNKNOWN** — engineering placeholder OK (OQ-11) |
| **Non-goals** | Final copy; real URLs before IA charter; pixel-perfect logo |
| **DC** | N/A |
| **VF** | Shell integration Calibration §5.6 |
| **GRID** | Header section + container — not `header.container` |
| **LAY** | LP-HEADER-DUAL-ROW row 1 |
| **OL** | Internal gaps only approved tokens |

---

### M2-B-021 — BLK-002 Header Main Nav + callback (desktop)

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Primary IA row + callback CTA |
| **Authority** | v3 §8.1 header callback · §8.7 · BLK-002 |
| **Acceptance criteria** | Primary nav links stub per Page Inventory top IA; callback button per §8.1 header callback dims; logo placeholder; ≥1024px |
| **Non-goals** | Sticky header behavior TBD; hamburger (mobile step) |
| **DC** | N/A |
| **VF** | Shell §5.6 |
| **GRID** | Row 2 inside header container contract |
| **LAY** | Flex/grid with `fr` — **no** % column splits |
| **OL** | Callback padding-x 24px — **EX-005** |

---

### M2-B-022 — BLK-003 Site Footer (desktop)

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Multi-column footer desktop |
| **Authority** | v3 §8.8 · BLK-003 |
| **Acceptance criteria** | Background `#E2E8EF`; vertical padding **80px** (`space-12` — **EX-009**); multi-column desktop; stack deferred to mobile step; typographed links |
| **Non-goals** | Legal microcopy final; sitemap completeness |
| **DC** | N/A |
| **VF** | Shell §5.6 |
| **GRID** | Footer section + container |
| **LAY** | **LP-FOOTER-MULTI** with `fr` |
| **OL** | padding 80px — **EX-009** |

---

### M2-B-026 — Mobile header (≤1023px)

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Condensed header + menu pattern |
| **Authority** | Start Sequence Step 6 · v3 §3.5 |
| **Acceptance criteria** | Single-column compressed header; hamburger/menu per PDF pattern — exact control **SAFE UNKNOWN** allowed; padding-x **20px**; no desktop dual-row at mobile breakpoint |
| **Non-goals** | Full mobile nav drawer copy |
| **DC** | N/A |
| **VF** | §4 mobile shell |
| **GRID** | Same container contract 20px |
| **LAY** | Mobile stack |
| **OL** | padding 20px on OL scale — **PASS** without waiver |

---

### M2-B-027 — Mobile footer (≤1023px)

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Footer stack mobile |
| **Authority** | Start Sequence Step 6 · v3 §3.5 |
| **Acceptance criteria** | Columns stack; padding-x **20px**; readable tap targets |
| **Non-goals** | Duplicate footer content invention |
| **DC** | N/A |
| **VF** | §4 mobile |
| **GRID** | Footer section + container |
| **LAY** | Single column |
| **OL** | N/A |

---

### M2-B-028 — BLK-004 Mobile sticky CTA bar

| Field | Value |
|-------|-------|
| **Entity** | **FOUNDATION ENTITY** |
| **Purpose** | Fixed bottom bar mobile only |
| **Authority** | v3 §8.9 · BLK-004 |
| **Acceptance criteria** | Active **`max-width: 1023px` only**; bar h **56px**; 3 actions Phone · Callback · Appointment equal thirds; touch min **48px**; icon **24px** estimated; **`fixed` bottom**; **inactive** ≥1024px |
| **Non-goals** | Desktop sticky; real tel: analytics |
| **DC** | N/A |
| **VF** | Mobile shell |
| **GRID** | Full viewport width bar — inner flex thirds |
| **LAY** | Equal `flex: 1` columns |
| **OL** | Bar internal gap tokens only from v3/EX |

---

## 4.1 Explicit NOT FOUNDATION register (do not implement in M2)

| ID | Artifact | Entity tag | Reason |
|----|----------|------------|--------|
| NF-01 | `index.html` Home | **NOT FOUNDATION ENTITY** | Phase 8 |
| NF-02 | BLK-007 Page Hero | **NOT FOUNDATION ENTITY** | Home/inner hero |
| NF-03 | BLK-009 UTP Cards | **NOT FOUNDATION ENTITY** | PG-001 unique |
| NF-04 | BLK-010 Services Preview | **NOT FOUNDATION ENTITY** | PG-001 unique |
| NF-05 | BLK-005 Breadcrumbs demo | **NOT FOUNDATION ENTITY** | Not VF §3 |
| NF-06 | BLK-006 Anchor nav demo | **NOT FOUNDATION ENTITY** | Page context |
| NF-07 | BLK-017 Pagination demo | **NOT FOUNDATION ENTITY** | Not VF §3 — v3 §8.6 deferred to page QA |
| NF-08 | Article TOC 280px layout | **NOT FOUNDATION ENTITY** | PG-009 |
| NF-09 | BLK-011–013 G-SERVICE bodies | **NOT FOUNDATION ENTITY** | PG-002+ |
| NF-10 | Specialist avatar pill standalone section | **NOT FOUNDATION ENTITY** | Radius **999px** proven via buttons/cards if needed — no separate section required |
| NF-11 | Diff-bg **56px** spacing demo section | **NOT FOUNDATION ENTITY** | Token exists (EX-007) but **not** mandatory VF label — optional note in REPORT only; **do not** add fourth spacing section unless Lead requests |
| NF-12 | Design Completeness Audit execution | **NOT FOUNDATION ENTITY** | Post–Home |
| NF-13 | Pixel Fidelity full Home audit | **NOT FOUNDATION ENTITY** | Post–Home |
| NF-14 | New `fd-sec-*` naming from destroyed pass | **NOT FOUNDATION ENTITY** | Reset removed — use block IDs above |

---

## 5. M2 Compliance Strategy

Pre-declared verification route for M2 close — agent **must not** improvise QA methodology.

### 5.1 Spacing exceptions verification

| Step | Action |
|------|--------|
| S-01 | After `npm run build`, grep **`dist/*.css`** for `gap:`, `margin`, `padding` longhands and shorthands |
| S-02 | For each value **not** on OL-01 scale, lookup [FP-0002-EXCEPTION-REGISTRY-v1.md](FP-0002-EXCEPTION-REGISTRY-v1.md) §2 + §5 |
| S-03 | Run **Compliance Decision Model** per finding — **never FAIL at detection** |
| S-04 | Allowed v3 tokens: 8, 12, 16, 24, 32, 56, 64, 80, 240 px only with matching **EX-002…EX-010** + v3 cite |
| S-05 | Any unlisted px (e.g. `17px`, `12px` on non-input) → **CASE D → FAIL** — map to OL nearest or STOP HITL |
| S-06 | **Separate checks:** `gap` vs `margin` vs `padding` — Execution Brain L-03 |
| S-07 | Record each WAIVED row in Foundation QA REPORT with **decision id** (EX-00N) |

**PASS condition:** Every off-OL compiled value has complete Exception Registry row **or** value is on OL-01 (40/20 page padding = PASS).

### 5.2 Line-height verification

| Step | Action |
|------|--------|
| LH-01 | Extract computed line-heights for every v3 §4.1 tier on demo URL (DevTools) |
| LH-02 | Compare to v3 table — **exact px match** required |
| LH-03 | **OL-05:** v3 named tiers win — **NEX-04** — **no** Exception Registry for H1 84/50, H2 44/28, body 28/24, button 20 |
| LH-04 | **Forbidden:** unitless ratios (`1.5`) hiding cadence unless v3 names exception — none exist for FP-0002 |
| LH-05 | REPORT line: `TYPOGRAPHY PRECISION (line-height = font-size + 4px) — PASS` when all tiers match v3 |

**FAIL trigger:** Any tier uses agent-invented line-height not in v3 §4.1.

### 5.3 Compiled CSS inspection

| Step | Action |
|------|--------|
| C-01 | **Mandatory at Design Calibration** §5.7 — before Foundation QA |
| C-02 | Inspect **`dist/*.css`** primary — source SCSS secondary |
| C-03 | Scope: demo page selectors + global + layout partials CSS |
| C-04 | Categories: gap · margin · padding · OL-05 line-heights · OL-06 forbidden props |
| C-05 | Cross-check **`dist/**/*.html`** for inline `style=""` — EG-03 vs allowlist |
| C-06 | Emit: `COMPILED CSS SPOT-CHECK — …` and `COMPILED CSS COMPLIANCE — …` at Foundation QA |
| C-07 | **Never** claim PASS on source-only review — Execution Brain L-07 |

### 5.4 Mandatory checks before Foundation QA PASS

All **must PASS** (or WAIVED with registry) before `ROOT COMPLIANCE — PASS`:

| # | Gate / check | Authority |
|---|--------------|-----------|
| 1 | `npm run build` succeeds | Charter G-01 |
| 2 | `dist/ui-demo.html` exists; no Home in dist | C-03 Execution Brain |
| 3 | Visual Foundation Contract all §3 categories | Foundation QA 6.1 |
| 4 | Design Calibration PASS incl. §5.7 compiled spot-check | Calibration §5.7 |
| 5 | Token spot-check vs v3 | Calibration §5.1–5.4 |
| 6 | `SECTION SPACING — PASS` | section-spacing-rule |
| 7 | `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS` | v3 §4.3 |
| 8 | `WF GRID DISCIPLINE — PASS` | WF-GRID |
| 9 | `WF LAYOUT DISCIPLINE — PASS` | WF-LAYOUT · OL-04 |
| 10 | `OPERATOR LAW COMPLIANCE — …` EG-01 | Enforcement §3.1 |
| 11 | `COMPILED CSS COMPLIANCE — …` EG-02 | Enforcement §3.2 |
| 12 | `INLINE STYLE COMPLIANCE — …` EG-03 | allowlist |
| 13 | `AUTHORITY CONFLICT STATUS — …` EG-04 | Exception Registry complete |
| 14 | `ROOT COMPLIANCE — PASS` EG-05 | Enforcement §6 |
| 15 | Compliance Decision Model block in REPORT | compliance-decision-model |
| 16 | `# REPORT — FP-0002 foundation QA` filed | Charter §14 |
| 17 | Lead acknowledgment | Charter G-15 |
| 18 | **No** BLK-007 / PG-001 blocks in codebase | Charter G-04 |

**Hard rule:** Foundation QA PASS **impossible** without **ROOT COMPLIANCE — PASS**.

---

## 6. Known Failure Traps

From [FP-0002-EXECUTION-BRAIN-v1.md](FP-0002-EXECUTION-BRAIN-v1.md) Lessons Learned — agent **must** treat as stop signals.

| Trap ID | Trap | Correct behavior |
|---------|------|------------------|
| **T-01** | PASS on structure + token **presence** while compiled CSS violates OL | EG-02 on `dist/*.css` mandatory |
| **T-02** | **`gap: 16px`** in compiled output treated as implicit PASS | Cite **EX-004** or map to OL 20px — CASE B without registry = FAIL |
| **T-03** | **`margin-bottom: 24px`** / **`padding: 24px`** off OL margin scale | Separate margin/padding grep; **EX-005** |
| **T-04** | **`padding: 12px`**, **`gap: 8px`**, **`gap: 32px`** without v3 cite | 12/8 only in EX-002/003 contexts; 32 in EX-006 — else CASE D FAIL |
| **T-05** | Rank-1 permit = auto-WAIVED OL | Complete Exception Registry **before** WAIVED |
| **T-06** | Exception Registry absent at QA | EG-04 FAIL — use project registry §2 |
| **T-07** | Source-only SCSS review | Calibration §5.7 COMPILED CSS SPOT-CHECK |
| **T-08** | ROOT COMPLIANCE PASS without sub-gates | EG-05 blocks PASS |
| **T-09** | DQ-02a SSOT PASS implies DQ-02b OL PASS | Run **both** independently |
| **T-10** | Skip Design Calibration → Foundation QA | Shell-first Phase 4b mandatory |
| **T-11** | AUTHORITY CONFLICT not verified | EG-04 at Foundation QA |
| **T-12** | Start Home before Phase 7 | SC-01 stop |
| **T-13** | Reuse destroyed M2 Spec v1 | Use **this v2 spec only** |
| **T-14** | RAW VIOLATION emitted as FAIL at detection | Full 6-stage Compliance Decision route |
| **T-15** | Aesthetic spacing habits (16/24 as «nice numbers») | Every px cites v3 token + EX row |
| **T-16** | Same-bg **double stack** 80+80 | Factory single-boundary — M2-B-016a |
| **T-17** | BLK-007 inside header partial | HEADER ≠ HERO |
| **T-18** | Hand-edit `dist/` | src-only — Charter SC-05 |
| **T-19** | Invent hover/focus states beyond engineering fallback | v3 §5.3 placeholders only |
| **T-20** | `letter-spacing` / `word-break` / `overflow-wrap` / `hyphens` (any value) | Remove entirely — v3 §4.3 hard law; property presence = FAIL |

**Expected Capture Point (if trap escapes):** Design Calibration §5.7 for compiled spacing; Foundation QA §6.16 for registry gaps — per Failure Attribution Model.

---

## 7. Document control

| Field | Value |
|-------|-------|
| Version | **v2** |
| Created | 2026-06-14 |
| Invalidates | FP-0002-M2-FOUNDATION-DEMO-SPEC-v1.md |
| Modifies frontend workspace | **No** — spec only |
| Commit / push | Not performed |

---

*M2 Foundation Demo Spec v2 only. No code. No HTML. No SCSS. No JS.*
