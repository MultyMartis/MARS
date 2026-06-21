# FP-0002 HEADER LAYOUT SPEC v2

**Block ID / scope:** `FP-0002-BLK-001 + FP-0002-BLK-002` — Desktop Header (shell chrome)  
**Document type:** Layout Spec (composition decomposition — **not** audit, **not** implementation)  
**Status:** **DRAFT** — awaiting operator decision **APPROVED | REVISE**  
**Date:** 2026-06-14  
**Viewport:** Desktop **≥ 1024px** (Phase C.1 default)  
**Layout Pattern:** **LP-HEADER-DUAL-ROW** (BLK-001 stacked above BLK-002)

**Revision note:** v2 extends v1 with **Visual Weight Model**, **Left/Center/Right Alignment Model**, **Row 1/2 Composition Models**, and **Layout Risk Assessment** per operator REVISE request. v1 remains on file — **not superseded** until operator APPROVED on v2.

**Authority applied:**

| Layer | Document | Role |
|-------|----------|------|
| A0 | [FP-0002-SOURCE-DISCOVERY-REPORT-v1.md](FP-0002-SOURCE-DISCOVERY-REPORT-v1.md) | SOURCE-ID register |
| A1 | [FP-0002-DESIGN-AUDIT-v1.md](FP-0002-DESIGN-AUDIT-v1.md) | Visual SSOT READ · header element inventory |
| Approval | [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md) | Operator decision matrix (D-001…D-022) |
| Mini-audit | [FP-0002-HEADER-MINI-AUDIT-v1.md](FP-0002-HEADER-MINI-AUDIT-v1.md) | Header-only composition cross-check |
| Prior spec | [FP-0002-HEADER-LAYOUT-SPEC-v1.md](FP-0002-HEADER-LAYOUT-SPEC-v1.md) | Structural baseline preserved in v2 |
| Blocks | [FP-0002-BLOCK-INVENTORY-v1.md](../FP-0002-BLOCK-INVENTORY-v1.md) | BLK-001 / BLK-002 scope |
| Engineering | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) §8.7 | Container model · dual-row law — **not** visual composition SSOT |
| Factory law | [layout-spec-law-v1.md](../../../../projects/mars-website-factory/layout-spec-law-v1.md) | Mandatory fields L-01…L-15 |
| Lesson | [FP-0002-layout-spec-lesson-v1.md](../../../../projects/mars-website-factory/FP-0002-layout-spec-lesson-v1.md) | SaaS-header failure provenance |
| Shell | [canonical-clean-shell-v1.md](../../../../projects/mars-website-factory/canonical-clean-shell-v1.md) | Pre-code gate |
| Visual gate | [operator-visual-approval-law-v1.md](../../../../projects/mars-website-factory/operator-visual-approval-law-v1.md) | Post-build gate (separate from this doc) |

**Evidence artefacts:** `REPORTS/_audit_extract_output.json` · `REPORTS/fp0002-component-extraction.json` (`top_bar_end_px: 180`)

**Honesty note:** Primary PDF files are **not present on disk** at `INCOMING/01_DESIGN/` in this session (README only). Composition below is derived from **A1 Design Audit (24/24 PDF READ)** and derived artefacts — **not** from a live PDF open in this task.

---

## 1. Scope

| In scope | Out of scope |
|----------|--------------|
| Desktop header **composition and visual hierarchy** for **PG-001…PG-010** standard templates | HTML · SCSS · JS · tokens · components · partials · build |
| Structural decomposition: rows · zones · groups · boundaries · **visual weight · alignment · composition models** | Color · typography tokens · pixel-perfect measurements |
| Frozen vs SAFE UNKNOWN composition decisions | Mobile condensed header / hamburger overlay (separate future spec) |
| Header vs next-block separation | BLK-004 Mobile Sticky CTA Bar (separate block, not header stack) |
| Container / row model for assembly | Modal «Заказать звонок» layout (M-06) |
| Layout Risk Assessment for implementation agents | Operator Visual Acceptance of built HTML |

**Shell SSOT reference:** SOURCE-001 (`Главная страница (v2).pdf`) — canonical desktop header; identical chrome on SOURCE-005…021 desktop templates per Mini-Audit §2. **404 (SOURCE-023) is not shell SSOT.**

**v2 delta:** Scope unchanged; explicitly includes **visual composition models** as first-class spec content — not optional commentary.

---

## 2. Visual Sources Used

| SOURCE-ID | File | Role in this spec |
|-----------|------|-------------------|
| **SOURCE-001** | `2026-06-11-home-v2/Главная страница (v2).pdf` | **Primary** — dual-row header composition SSOT |
| SOURCE-005…021 | Service · About · Contacts · Reviews · Blog · Article · Legal desktop PDFs | **Confirm** — same BLK-001+002 chrome (Mini-Audit §2) |
| SOURCE-025 | `Предварит структура и спрос.xlsx` | URL targets for nav / top-bar links |
| SOURCE-034 | Block Inventory v1 | BLK-001 / BLK-002 block boundaries |
| SOURCE-036 | Numeric Design Rules v2 | Header heights SAFE UNKNOWN register · CTA radius est. 6 px (PDF) vs Production 30 px (**CONFLICT CF-010**) |
| SOURCE-041 | Production Standards v3 §8.7 | Container model · dual-row behavior — **engineering only** |
| `_audit_extract_output.json` | PDF text/metrics extraction | Phone numbers · partial label decode · `top_bar_end_px` proxy |
| `fp0002-component-extraction.json` | Component scan | `top_bar_end_px: 180` (top row band boundary — **ESTIMATED**, not layout law) |

**Not used as composition SSOT:** SOURCE-003/004 (Home v1 superseded) · SOURCE-023/024 (404 minimal chrome) · mobile PDF pairs (Phase C.1 desktop-only scope) · **Production Standards v3 styling tokens** (accent, radius, padding) — see §17 Layout Risk Assessment **LR-007**.

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

**Visual composition rule (v2):** MAIN ROW must read as the **dominant visual band** — taller, larger type/mark scale — so the eye lands on brand + nav + CTA before re-reading TOP ROW contact meta. Inverting this (equal-height rows, TOP ROW visually louder than MAIN ROW) is a **composition failure**, not a styling tweak.

### 3.4 Horizontal envelope

| Layer | Model |
|-------|-------|
| Header `<header>` shell | **Full viewport width** — background band may extend edge-to-edge |
| Inner layout | **Shared page container** — max **1170px**, centered, horizontal padding **40px** desktop (Production Standards v3 · WF-GRID-001) |
| Rule | **Section + inner container** — not `header.container` as sole element (M2-B-020 GRID note) |

Both TOP ROW and MAIN ROW share the **same inner container width and horizontal alignment**. Left/right alignment anchors (Region + Logo on left; Phones + CTA on right) must share the **same container edges** — not drift to viewport edge on one row and container edge on the other.

---

## 4. Row Model

### 4.1 Row count

**2 rows** on desktop ≥ 1024px.

| Row | Name | Block ID | Exists | Band visual role |
|-----|------|----------|--------|------------------|
| **Row 1** | **TOP ROW** | FP-0002-BLK-001 | **YES** | **Secondary band** — contact + utility meta; must not overpower Row 2 |
| **Row 2** | **MAIN ROW** | FP-0002-BLK-002 | **YES** | **Primary band** — brand + IA + conversion |

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

**Composition intent (v2):** TOP ROW is a **supporting contact strip**, not a second navigation bar. Phones are the **visual climax** of this strip; hours and region provide context but must not steal attention from phones or from MAIN ROW below.

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

**Composition intent (v2):** MAIN ROW is the **identity + wayfinding + conversion** row. Logo and nav share primary visual weight; CTA is the **isolated action object** at the right edge — not a nav item, not a top-bar utility link.

---

## 5. Zone Model

Zones are **composition territories** inside the header stack, top-to-bottom then left-to-right within each row.

| Zone | Row | Name | Groups contained | Visual weight tier (see §6) |
|------|-----|------|------------------|----------------------------|
| **ZONE A** | TOP ROW | Utility Left | Region Group | **UTILITY** |
| **ZONE B** | TOP ROW | Utility Center | Hours Group | **SUPPORTING** |
| **ZONE C** | TOP ROW | Utility Right-Inner | Utility Links Group | **SECONDARY** (within TOP ROW) |
| **ZONE D** | TOP ROW | Utility Right-Outer | Phone Group | **SECONDARY** (strongest within TOP ROW) |
| **ZONE E** | MAIN ROW | Brand Anchor | Logo Group | **PRIMARY** |
| **ZONE F** | MAIN ROW | Primary IA | Primary Nav Group | **PRIMARY** |
| **ZONE G** | MAIN ROW | Conversion | CTA Group | **PRIMARY** (action accent) |

### Zone order (strict)

```text
ROW 1:  ZONE A → ZONE B → ZONE C → ZONE D
ROW 2:  ZONE E → ZONE F → ZONE G
```

**Forbidden zone moves:** placing CTA in TOP ROW · placing phones in MAIN ROW · placing Primary Nav in TOP ROW · placing Region/Hours in MAIN ROW · placing «Генотипирование» / «Специалисты» in Primary Nav Group · centering Logo in MAIN ROW (SaaS pattern) · moving Phone Group to left or center of TOP ROW.

---

## 6. Visual Weight Model

**Purpose:** Lock **visual force** of each header group so implementation agents cannot demote contact phones to meta text, inflate utility links to nav parity, or treat logo as a disposable placeholder.

**Tier definitions (header-scoped):**

| Tier | Meaning | Agent rule |
|------|---------|------------|
| **PRIMARY** | Defines page identity, main IA, or primary conversion — **must dominate** viewer attention within its row and (for MAIN ROW groups) across the full header stack | Must not shrink, mute, or hide behind SECONDARY/UTILITY elements |
| **SECONDARY** | Important but **subordinate** to PRIMARY band; may include links or contact clusters with real presence | Must remain **readable and intentional** — not collapsed to caption/utility styling |
| **UTILITY** | Context/meta labels — present but **must not compete** with PRIMARY or strong SECONDARY | Smaller/lighter than phones and MAIN ROW; never styled as nav or CTA |
| **SUPPORTING** | Lowest meta — **must not draw the eye** before phones or MAIN ROW | Never equal or stronger than Phone Group or any MAIN ROW group |

### 6.1 Cross-row hierarchy

| Band | Overall tier | Composition statement |
|------|--------------|----------------------|
| **MAIN ROW (Row 2)** | **PRIMARY** | The header's visual **main stage** — brand, site navigation, and callback CTA live here. An agent must not make TOP ROW equally tall, equally saturated, or equally typographically loud. |
| **TOP ROW (Row 1)** | **SECONDARY** (band) | A **contact + utility strip** above the main stage. It is real chrome, not optional — but it **supports** conversion and locale context; it does **not** replace MAIN ROW navigation or CTA. |

### 6.2 Group weight register

| Group | Zone | Tier | Visual force statement |
|-------|------|------|------------------------|
| **Logo / Brand Group** | E | **PRIMARY** | Brand mark + title stack is the **left anchor** of the entire site chrome — a **visual brand object**, not a favicon-sized decoration or text-only wordmark fallback. Must read as **home** and **institution identity** at MAIN ROW scale. |
| **Primary Nav Group** | F | **PRIMARY** | Five equal-weight **text links** forming the **horizontal IA spine** between brand and CTA. Nav is **site wayfinding** — not utility links, not phone numbers, not button labels. |
| **CTA Group** | G | **PRIMARY** | «Заказать звонок» is the **isolated conversion control** — visually separated from nav links. It is the **strongest action accent** in MAIN ROW (right edge). Must not be demoted to a text link or merged into nav. **Styling** (fill, radius, color) follows Visual SSOT — **not** generic Production Standards pill defaults (see LR-002). |
| **Phone Group** | D | **SECONDARY** | **Phone Group is visually stronger than Hours Group, Region Group, and Utility Links Group** within TOP ROW. Two numbers form **one contact cluster** at the **outer right** — they are **clickable contact objects**, not fine-print footer text. Agent **must not** render phones as muted utility captions. |
| **Utility Links Group** | C | **SECONDARY** (weak) | «Генотипирование» · «Специалисты» are **secondary top-bar links** — more present than hours/region meta, **less** than phones and **far less** than PRIMARY nav. They are **not** primary nav items. |
| **Region Group** | A | **UTILITY** | Locale labels («Москва,» · «Московская область») — **context**, not navigation. Paired cluster on the **left** of TOP ROW. Must not be styled with nav/CTA weight. |
| **Hours Group** | B | **SUPPORTING** | Operating hours are **meta text** — subordinate to Phone Group. Must not be styled equal to phones or utility links. Single cluster — not repeated per region unless operator decides otherwise (SU-06). |

### 6.3 Weight relationships (mandatory)

```text
MAIN ROW (PRIMARY band)  >>>  TOP ROW (SECONDARY band)

Within MAIN ROW:
  Logo Group ≈ Primary Nav Group  (co-primary identity + IA)
  CTA Group  >  Nav link text     (action accent — isolated control)

Within TOP ROW:
  Phone Group  >  Utility Links  >  Region Group  >  Hours Group

Cross-row (contact):
  Phone Group (TOP ROW)  <  Logo / Nav / CTA (MAIN ROW)   — phones prominent in strip, not louder than main band
  Phone Group (TOP ROW)  >  Hours / Region (TOP ROW)       — phones must not become meta footnotes
```

### 6.4 Explicit non-competition rules

| Element | Must NOT compete with |
|---------|----------------------|
| Hours Group | Phone Group · Primary Nav · CTA |
| Region Group | Phone Group · Logo · CTA |
| Utility Links | Primary Nav (same visual tier or placement) |
| Phone Group | Logo · CTA (must not jump to MAIN ROW or match MAIN ROW scale) |
| TOP ROW band | MAIN ROW band (must not equalize row height/visual dominance) |

---

## 7. Left / Center / Right Alignment Model

**Purpose:** Prevent **SaaS header re-layout** (centered logo, right-clustered nav+CTA, phones demoted to corner microtext) that contradicts SOURCE-001 dual-row composition.

**Alignment applies inside the shared 1170px inner container** (both rows). Full-bleed background may extend viewport-wide; **content anchors** align to container edges.

### 7.1 Row 1 — TOP ROW alignment

| Alignment zone | Groups | Position intent | Visual linkage |
|----------------|--------|---------------|----------------|
| **LEFT** | Region Group | Anchored **left** within container — first content in reading order | Region labels **paired** — stay adjacent; **linked visually** as one locale cluster |
| **CENTER-LEFT** | Hours Group | **Between** Region and Utility Links — **not** flush right, **not** centered alone in row | **Linked to meta context** (locale/time) — **not** linked to Phone Group as one typographic sentence |
| **CENTER-RIGHT** | Utility Links Group | **Right of center**, **left of phones** — secondary links band | **Paired links** — «Генотипирование» + «Специалисты» stay adjacent as one utility cluster |
| **RIGHT** | Phone Group | Anchored **outer right** of TOP ROW — **strongest right-side element** in Row 1 | Two phone numbers **one cluster** — **linked visually**; whitespace separates from Utility Links |

**Row 1 alignment diagram (intent):**

```text
|← LEFT          CENTER-LEFT    CENTER-RIGHT →|        RIGHT →|
 [Region cluster] [Hours meta]  [Util links]              [Phones]
```

### 7.2 Row 2 — MAIN ROW alignment

| Alignment zone | Groups | Position intent | Visual linkage |
|----------------|--------|---------------|----------------|
| **LEFT** | Logo Group | **Brand anchor left** — mark + text stack as **one unit** | Mark + title + subtitle **must not split** across zones |
| **CENTER** | Primary Nav Group | **Horizontal link band** occupying central territory between brand and CTA | Five links **one list** — equal spacing intent; **not** split to far left/right edges |
| **RIGHT** | CTA Group | **Isolated button** at outer right — separated from last nav link | CTA **not** part of nav list flex group |

**Row 2 alignment diagram (intent):**

```text
|← LEFT                    CENTER                      RIGHT →|
 [Logo + brand stack]   [Nav · Nav · Nav · Nav · Nav]   [CTA btn]
```

### 7.3 Vertical alignment between rows

| Left anchor | Right anchor | Rule |
|-------------|--------------|------|
| Region Group (Row 1) | — | Left edge aligns with Logo Group left edge **within container** (same container padding) |
| — | Phone Group (Row 1) | Right cluster aligns with CTA right edge **within container** — both rows share right-side conversion/contact column intent |
| Logo Group (Row 2) | CTA Group (Row 2) | Define MAIN ROW **visual width** — nav lives **between** these anchors |

### 7.4 Forbidden alignment moves

| Forbidden move | Why |
|----------------|-----|
| Logo centered in MAIN ROW (SaaS pattern) | Contradicts SOURCE-001 left brand anchor |
| Primary Nav flush-right next to CTA only | Collapses center IA band; mimics app header |
| Phones centered or left-aligned in TOP ROW | Contradicts confirmed outer-right phone cluster |
| Region labels split to far left + far right | Breaks locale cluster pairing |
| Hours moved to RIGHT zone replacing phones | Inverts contact hierarchy |
| CTA placed LEFT of logo or inside nav list | Breaks conversion isolation |
| Utility links moved to MAIN ROW center | Confuses secondary vs primary IA |
| Single-row flex: `[Logo][phones][nav][CTA]` | Collapses dual-row law (FD-01) |

### 7.5 Groups that must stay visually linked

| Linked set | Row | Must read as |
|------------|-----|--------------|
| «Москва,» + «Московская область» | 1 | One locale selector cluster |
| «Генотипирование» + «Специалисты» | 1 | One utility-links pair |
| +7 (925)… + +7 (995)… | 1 | One phone contact cluster |
| Mark + brand title + subtitle | 2 | One brand/home unit |
| Five nav labels (fixed order) | 2 | One primary navigation list |
| «Заказать звонок» button | 2 | Standalone — **not** linked into nav list |

---

## 8. Row 1 Composition Model

**Row 1 is not a element list.** It is a **horizontal meta-and-contact strip** with **four visual zones** inside one band (BLK-001).

### 8.1 Zone count and force

| Property | Value |
|----------|-------|
| Visual zones in Row 1 | **4** — ZONE A · B · C · D |
| Strongest zone in Row 1 | **ZONE D (Phone Group)** — contact climax of the strip |
| Weakest zone in Row 1 | **ZONE B (Hours Group)** — supporting meta |
| Row 1 vs Row 2 | Row 1 **visually subordinate** to Row 2 — shorter/lighter typographic band per Visual SSOT intent |

### 8.2 Compositional narrative (left → right)

The eye should move: **locale context** (where) → **availability meta** (when) → **secondary shortcuts** (what else) → **direct contact** (call now).

**ZONE A (left):** Region Group establishes **geography** — quiet UTILITY tier. It **opens** the strip but does not close the composition.

**ZONE B (center-left):** Hours Group provides **schedule meta** — SUPPORTING tier. It supports Phone Group contextually but **must not** match phone visual weight.

**ZONE C (center-right):** Utility Links Group offers **secondary IA shortcuts** — stronger than meta, weaker than phones. These are **not** primary nav; they **bridge** meta and contact zones.

**ZONE D (right):** Phone Group **closes** the strip with **contact urgency** — SECONDARY tier, strongest in Row 1. This zone **pairs visually with the right edge of Row 2 CTA** as the header's contact/conversion column — without moving phones to Row 2.

### 8.3 Row 1 content placement (confirmed)

| Element | In Row 1? | Zone |
|---------|-----------|------|
| Region labels | **YES** | A |
| Hours | **YES** | B |
| «Генотипирование» · «Специалисты» | **YES** | C |
| Two phone numbers | **YES** | D |
| Logo / brand | **NO** — Row 2 only | — |
| Primary nav (5 links) | **NO** — Row 2 only | — |
| «Заказать звонок» CTA | **NO** — Row 2 only | — |
| Search | **NO** — not in Visual SSOT | — |
| Messengers / social icons | **NO** — **SAFE UNKNOWN** in desktop header; **not confirmed** in SOURCE-001 extraction | — |

### 8.4 Forbidden in Row 1

| Forbidden | Reason |
|-----------|--------|
| Logo / brand mark | FD-03 · MAIN ROW identity |
| Primary navigation links | FD-02 · would create double-nav SaaS pattern |
| CTA button | FD-07 · conversion belongs MAIN ROW right |
| Breadcrumbs | BLK-005 · below header |
| Search field | FD-15 · not in SSOT |
| Collapsing Row 1 into Row 2 | FD-01 |
| Rendering phones as smallest text in strip | Visual Weight Model §6.2 |

---

## 9. Row 2 Composition Model

**Row 2 is the header's main stage** — brand recognition, site wayfinding, and callback conversion in one **dominant horizontal band** (BLK-002).

### 9.1 Zone count and force

| Property | Value |
|----------|-------|
| Visual zones in Row 2 | **3** — ZONE E · F · G |
| Strongest zones in Row 2 | **ZONE E (Logo)** and **ZONE F (Nav)** — co-primary identity + IA |
| Action accent | **ZONE G (CTA)** — isolated **PRIMARY** conversion control |
| Row 2 vs Row 1 | Row 2 **must visually dominate** entire header stack |

### 9.2 Compositional narrative (left → right)

**ZONE E (left):** Logo Group is the **brand anchor** — mark + institutional title + «(Шпиговский дом)» as **one visual object** linking to `/`. This is **not** a placeholder square + generic text; it is the **primary identity block** of the site chrome.

**ZONE F (center):** Primary Nav Group is the **horizontal IA spine** — five text links of **equal nav weight** between brand and CTA. This is **the** site menu — not utility links from Row 1, not service hub cards, not in-page anchors (BLK-006).

**ZONE G (right):** CTA Group is **one button** — «Заказать звонок» — visually **separated** from the last nav link. It is the **conversion punctuation** at the right margin.

### 9.3 Row 2 content placement (confirmed)

| Element | In Row 2? | Zone | Notes |
|---------|-----------|------|-------|
| Logo / brand mark + text | **YES** | E | Mark asset PARTIAL (SU-04) — composition still requires **brand object**, not placeholder policy at layout level |
| Primary nav — 5 links | **YES** | F | Fixed set/order FD-04 |
| «Заказать звонок» | **YES** | G | Label CONFIRMED; behavior SU-12 |
| Phones | **NO** — Row 1 only | — | FD-06 |
| Hours / region | **NO** — Row 1 only | — | FD-02 |
| Utility links | **NO** — Row 1 only | — | FD-05 |
| Search | **NO** | — | FD-15 |
| Service links / hub cards | **NO** — page body | — | Not header chrome |
| Breadcrumbs | **NO** — immediately below header | — | FD-09 |
| Hamburger / mobile menu control | **NO** at desktop ≥1024 | — | FD-14 |

### 9.4 What **is** nav vs **is not** nav (Row 2)

| IS Primary Nav (ZONE F) | IS NOT Primary Nav |
|-------------------------|-------------------|
| Услуги | Генотипирование (Row 1 utility) |
| О центре | Специалисты (Row 1 utility) |
| Отзывы | Заказать звонок (CTA button) |
| Статьи | Logo / brand home link |
| Контакты | Phones · hours · region |
| | In-page anchor chips (BLK-006) |
| | Footer links (BLK-003) |

### 9.5 Forbidden in Row 2

| Forbidden | Reason |
|-----------|--------|
| Phone numbers | FD-06 · breaks dual-row contact model |
| Top-bar utility links | FD-05 |
| Region / hours meta | FD-02 |
| Extra nav items beyond fixed five | FD-04 |
| CTA rendered as 6th inline nav link | Group 7 isolation |
| Search / language switcher | Not in SSOT |
| Breadcrumbs / hero content | §8 Header vs Non-Header |
| Centered logo with split nav to edges | SaaS misalignment (§7.4) |

---

## 10. Group Model

*(Preserved from v1 — cross-referenced to §6 Visual Weight and §7 Alignment.)*

### GROUP 1 — Region Group (ZONE A)

**Состав:**

- region label «Москва,»
- region label «Московская область»

**Grouping logic:** Two region labels read as **one location-selector cluster** — visually paired, separated from hours and phones.

**Visual weight:** **UTILITY** (§6.2)

**Alignment:** **LEFT** anchor of Row 1 (§7.1)

**Merged vs separate:** Stay **one group** — do **not** distribute regions to opposite ends of TOP ROW.

**Interaction:** Link vs static text — **SAFE UNKNOWN** (see §14 SU-05).

---

### GROUP 2 — Hours Group (ZONE B)

**Состав:**

- hours string «пн-пт: 08:00-18:00, сб-вс 08:00-22:00» (machine-confirmed fragments)

**Grouping logic:** Single meta block — **visually subordinate** to Phone Group (Zone D).

**Visual weight:** **SUPPORTING** (§6.2) — must not match Phone Group prominence.

**Alignment:** **CENTER-LEFT** of Row 1 (§7.1)

**Merged vs separate:** **Separate** from Region Group and Phone Group — do **not** embed hours inside phone links.

**Note:** Footer uses different hours fragment (пн-pt 09:00–19:00) — **outside header scope**; do not merge footer hours into header composition.

---

### GROUP 3 — Utility Links Group (ZONE C)

**Состав:**

- link «Генотипирование» → `/uslugi/genotipirovanie/`
- link «Специалисты» → `/specyalisty/`

**Grouping logic:** Pair of **secondary utility links** — same band as top bar, **not** primary nav.

**Visual weight:** **SECONDARY (weak)** within TOP ROW (§6.2)

**Alignment:** **CENTER-RIGHT** of Row 1 (§7.1)

**Merged vs separate:** **One group** — keep adjacent; do **not** move either item to MAIN ROW nav.

**Visual separation from Group 4:** Whitespace gap before Phone Group — phones are **not** part of this group.

---

### GROUP 4 — Phone Group (ZONE D)

**Состав:**

- phone 1: +7 (925) 183-64-64
- phone 2: +7 (995) 023-92-26

**Grouping logic:** Two tel links as **one contact cluster** at the **outer right** of TOP ROW.

**Visual weight:** **SECONDARY** — **strongest group in Row 1** (§6.2). Phone Group is **visually stronger than Hours Group and Region Group**. At implementation, phones **must not** be demoted to utility caption styling.

**Alignment:** **RIGHT** anchor of Row 1 (§7.1)

**Merged vs separate:** **One group** — stacked or inline pair **within the group** (exact inline vs stacked — **SAFE UNKNOWN** SU-07); do **not** split one number to MAIN ROW.

---

### GROUP 5 — Logo Group (ZONE E)

**Состав:**

- logo mark (graphic — asset **PARTIAL**)
- brand title: «Центр профилактики и лечения зависимостей»
- brand subtitle: «(Шпиговский дом)»
- tagline candidate: «Лечение и профилактика» — **placement SAFE UNKNOWN** (SU-03)

**Grouping logic:** Mark + text stack = **one brand home unit** — links to `/`.

**Visual weight:** **PRIMARY** (§6.2) — **visual brand object**, not placeholder block.

**Alignment:** **LEFT** anchor of Row 2 (§7.2)

**Merged vs separate:** Logo mark and text **must stay one visual object** — do **not** detach title to nav row center.

**Vertical stack intent:** Mark left of text **or** mark above text — exact stack axis **SAFE UNKNOWN** (SU-09); both belong to **same group**.

---

### GROUP 6 — Primary Nav Group (ZONE F)

**Состав (exactly 5 items, fixed order):**

1. «Услуги» → `/uslugi/`
2. «О центре» → `/o-centre/`
3. «Отзывы» → `/otzyvy/`
4. «Статьи» → `/blog/`
5. «Контакты» → `/kontakty/`

**Grouping logic:** Single **horizontal nav list** — equal-weight text links, **excluding** logo/home, **excluding** CTA button.

**Visual weight:** **PRIMARY** (§6.2)

**Alignment:** **CENTER** band of Row 2 (§7.2)

**Merged vs separate:** **One list group** — do **not** break into multiple nav clusters; do **not** add «Генотипирование» or «Специалисты» here.

**Items explicitly NOT in this group:** «Генотипирование» · «Специалисты» · «Заказать звонок» · logo/brand · phones · hours · regions.

---

### GROUP 7 — CTA Group (ZONE G)

**Состав:**

- button «Заказать звонок» (single control)

**Grouping logic:** **Isolated conversion control** — visually separated from nav text links.

**Visual weight:** **PRIMARY** — **strongest action accent** in MAIN ROW (§6.2)

**Alignment:** **RIGHT** anchor of Row 2 (§7.2)

**Merged vs separate:** **Separate** from Primary Nav Group — do **not** render as 6th nav link; do **not** move to TOP ROW.

**Styling note:** PDF samples accent **#B3261D**, CTA radius est. **~6 px** (SOURCE-036) — **conflicts** with Production Standards 30 px radius (CF-010). **Visual SSOT wins for composition styling intent** at implementation — agent must **not** substitute generic red pill from Production Standards without operator decision (LR-002, LR-007).

**Behavior:** Modal / tel / external — **SAFE UNKNOWN** (M-06 · D-015 · SU-12) — **does not change composition placement**.

---

## 11. Visual Hierarchy

*(Updated to reference Visual Weight Model §6.)*

| Level | Elements | Dominance | Weight tier |
|-------|----------|-----------|-------------|
| **1 — Primary band** | MAIN ROW overall · Logo Group · Primary Nav Group · CTA button | Largest band; drives page IA | **PRIMARY** |
| **2 — Secondary band** | TOP ROW overall · Phone Group · Utility Links Group | Smaller type band; contact + utility | **SECONDARY** |
| **3 — Meta** | Region Group | Locale context | **UTILITY** |
| **4 — Supporting meta** | Hours Group | Schedule footnote within strip | **SUPPORTING** |

**Within MAIN ROW:**

1. CTA button — strongest **action** accent (right) — **PRIMARY**
2. Logo Group — strongest **brand** anchor (left) — **PRIMARY**
3. Primary Nav — horizontal link band (center) — **PRIMARY**, between brand and CTA

**Within TOP ROW:**

1. Phone Group — strongest (contact) — **SECONDARY**
2. Utility Links Group — secondary links — **SECONDARY (weak)**
3. Region Group — locale context — **UTILITY**
4. Hours Group — weakest meta text — **SUPPORTING**

**Cross-row rule:** MAIN ROW **must visually dominate** TOP ROW (taller band, larger logo/nav scale). Agent **must not** invert hierarchy (e.g. equal-height rows, phones larger than logo, TOP ROW typographically equal to MAIN ROW).

---

## 12. Header vs Non-Header Separation

### 12.1 Inside Header (must be assembled in `<header>` stack)

| Element | Row | Group | Weight |
|---------|-----|-------|--------|
| Region labels | TOP | Region Group | UTILITY |
| Hours | TOP | Hours Group | SUPPORTING |
| Генотипирование · Специалисты | TOP | Utility Links Group | SECONDARY |
| Two phones | TOP | Phone Group | SECONDARY |
| Logo + brand text | MAIN | Logo Group | PRIMARY |
| Five primary nav links | MAIN | Primary Nav Group | PRIMARY |
| «Заказать звонок» button | MAIN | CTA Group | PRIMARY |

### 12.2 Outside Header — **NEXT BLOCK** (must **not** be placed inside header)

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

### 12.3 Common FP-0002 Header Failure guards

| Failure mode | Prevention rule |
|--------------|-----------------|
| Breadcrumb inside header | BLK-005 starts **after** BLK-002 bottom edge |
| Hero merged into header | BLK-007 starts **after** header boundary on PG-001 |
| Single-row collapse | BLK-001 and BLK-002 remain **two rows** |
| Specialists in main nav | «Специалисты» stays TOP ROW only |
| CTA as nav link | CTA stays GROUP 7 — separate from GROUP 6 |
| Phones in main row | Phones stay TOP ROW GROUP 4 only |
| SaaS centered-logo header | Logo stays LEFT ZONE E — §7.4 |
| Phones as utility microtext | Phone Group weight SECONDARY — §6.2 · LR-001 |

---

## 13. Frozen Decisions

These composition choices **must not be changed** by implementation agent without Layout Spec **REVISE**:

| ID | Decision |
|----|----------|
| FD-01 | **Dual-row header** — exactly **2 rows** on desktop; BLK-001 above BLK-002 |
| FD-02 | **TOP ROW contains only** Region · Hours · Utility links · Phones — nothing from MAIN ROW |
| FD-03 | **MAIN ROW contains only** Logo group · 5 nav links · CTA — nothing from TOP ROW |
| FD-04 | **Five primary nav labels** — Услуги · О центре · Отзывы · Статьи · Контакты — fixed set and order |
| FD-05 | **«Генотипирование» and «Специалисты»** — TOP ROW utility links only — **not** in primary nav |
| FD-06 | **Two phone numbers** — both in TOP ROW Phone Group — **outer right** |
| FD-07 | **«Заказать звонок»** — MAIN ROW CTA Group only — **not** in TOP ROW |
| FD-08 | **Logo + brand text** — single Logo Group at MAIN ROW **left** — home link to `/` |
| FD-09 | **Breadcrumbs (BLK-005)** — **outside** header — below BLK-002 |
| FD-10 | **Hero (BLK-007)** — **outside** header on Home |
| FD-11 | **Same header chrome** on PG-001…PG-010 desktop templates |
| FD-12 | **Shared 1170px inner container** for both rows — aligned left/right anchors |
| FD-13 | **404 page** — not used as header composition SSOT |
| FD-14 | **No hamburger / mobile menu** in desktop ≥1024px composition |
| FD-15 | **No search field** in header — not in Visual SSOT |
| FD-16 | **Phone Group visual weight** — SECONDARY, stronger than Hours/Region within TOP ROW — **not** utility microtext (v2) |
| FD-17 | **Logo Group** — PRIMARY brand object at MAIN ROW left — **not** centered SaaS layout (v2) |
| FD-18 | **Visual Weight Model tiers** — §6 are binding for composition — agent cannot re-tier groups (v2) |

---

## 14. SAFE UNKNOWN

Composition gaps — agent **must not silently invent structure** to fill:

| ID | Topic | Impact |
|----|-------|--------|
| SU-01 | Exact **pixel heights** of TOP ROW / MAIN ROW / total stack | Cannot lock hero offset; use engineering placeholder only after APPROVED |
| SU-02 | **Sticky header** on scroll (yes/no/shrink) | Does not change row model; behavior deferred |
| SU-03 | **«Лечение и профилактика»** — inside Logo Group vs omitted vs TOP ROW | Brand stack assembly |
| SU-04 | Logo **graphic asset** (SVG/PNG) — SOURCE-026 empty | Asset delivery — **composition still requires brand object placement** at ZONE E |
| SU-05 | Region labels — **links vs static text** | TOP ROW interaction |
| SU-06 | Hours — **one shared string vs per-region pairs** | Mini-Audit: text layer suggests **once** — **OPERATOR DECISION REQUIRED** |
| SU-07 | Phone pair — **inline horizontal vs stacked** within Phone Group | TOP ROW micro-layout within ZONE D |
| SU-08 | Exact **horizontal gaps** between zones A–D and E–G | Spacing tokens deferred |
| SU-09 | Logo Group — mark **left of** vs **above** text stack | MAIN ROW micro-layout within ZONE E |
| SU-10 | Primary Nav — exact **center alignment math** (flex center vs space-between) | MAIN ROW micro-layout — groups fixed, math open |
| SU-11 | CTA button exact dimensions | CTA presence and zone fixed; size deferred |
| SU-12 | «Заказать звонок» **click behavior** (M-06 · D-015) | Does not move CTA zone |
| SU-13 | **Mobile / ≤1023px** header composition (condensed · hamburger) | Separate Layout Spec scope |
| SU-14 | **Hover / focus / active** nav visual states | Interaction styling deferred |
| SU-15 | PDF files **not on disk** for operator re-open in this session | Operator visual compare should use archived PDFs or re-intake |
| SU-16 | TOP ROW micro-order when viewport narrows (1024–1199) | Wrap/truncate strategy deferred — **rows must not collapse** |
| SU-17 | **Messengers / social icons** in desktop header | **Not confirmed** in audit extraction — do not add without SSOT |
| SU-18 | CTA **fill vs outline** variant at pixel level | Button presence CONFIRMED; exact variant **SAFE UNKNOWN** — styling follows Visual SSOT not Production defaults when conflict (CF-008, CF-010) |

---

## 15. Layout Risk Assessment

| RISK-ID | RISK | WHY IT MATTERS | HOW TO PREVENT |
|---------|------|----------------|----------------|
| **LR-001** | Phones rendered as **small utility/meta text** | Breaks contact hierarchy — phones are **SECONDARY** and strongest in TOP ROW; demotion hides primary business contact path | Apply §6.2 Phone Group weight; enforce ZONE D right cluster; cite FD-16; visual review against SOURCE-001 top bar |
| **LR-002** | CTA becomes **generic red filled pill** (Production Standards 30px radius) instead of **design-intent button** | Prior failure mode — engineering tokens **overrode** Visual SSOT (CF-010); CTA reads as Bootstrap/SaaS widget not site chrome | CTA stays ZONE G isolated; styling from Visual SSOT (PDF est. ~6px radius, accent #B3261D) pending operator CF-008/CF-010 decision — **not** auto-apply SOURCE-041 |
| **LR-003** | **Primary nav moves to TOP ROW** or utility links move to MAIN ROW nav | Creates double-nav or missing utility links — contradicts dual-row IA split | FD-02 · FD-03 · FD-05; §9.4 nav vs non-nav table; §8.4 forbidden list |
| **LR-004** | Logo becomes **placeholder box** or detached text without brand object treatment | Breaks PRIMARY brand anchor — header loses institutional identity | Logo Group = mark + text **one unit** ZONE E; SU-04 is asset gap not permission to skip brand composition; LR ties to operator asset intake |
| **LR-005** | **Hours / region styled equal to phones** | Flattens visual hierarchy — meta competes with contact | Hours = SUPPORTING, Region = UTILITY, Phones = SECONDARY §6.2; explicit non-competition §6.4 |
| **LR-006** | Agent rebuilds **typical SaaS header** (centered logo · nav+CTA right blob · single row) | Root FP-0002 failure ([FP-0002-layout-spec-lesson-v1.md](../../../../projects/mars-website-factory/FP-0002-layout-spec-lesson-v1.md)) — radically unlike SOURCE-001 | Enforce §7 Alignment Model · §8–9 Row Composition · FD-01 · FD-17; dual-row ASCII §16 |
| **LR-007** | Agent uses **Production Standards v3** as **Visual SSOT substitute** for composition or styling | Tokens ≠ layout decomposition; CF-008…CF-011 conflicts — wrong padding/radius/color | This spec + Visual SSOT (SOURCE-001) govern **composition**; Production Standards §8.7 **container only**; styling conflicts require operator decision before implementation |
| **LR-008** | Agent writes **HTML/CSS without operator-approved Layout Spec** | Layout Spec Law violation — structural fantasy before gate | **HTML/CSS PERMITTED — NO** until operator **APPROVED** on this document; cite gate in commit/PR |
| **LR-009** | **Single-row collapse** — all groups in one flex row | Eliminates BLK-001/002 boundary; phones/nav/CTA compete in one band | FD-01 · Row Model §4 · §8–9 composition models |
| **LR-010** | **CTA rendered as 6th nav link** (text link in nav list) | Loses conversion isolation — CTA weight drops from PRIMARY action to nav item | GROUP 7 separation · §9.2 ZONE G · FD-07 |
| **LR-011** | **Equal-height TOP + MAIN rows** | Inverts cross-row dominance — TOP ROW reads as co-primary | §6.1 · §11 cross-row rule · MAIN ROW must dominate |
| **LR-012** | Region labels **split to opposite ends** of TOP ROW | Breaks locale cluster pairing — reads as two unrelated labels | §7.5 linked sets · GROUP 1 logic |

---

## 16. Layout Diagram

### 16.1 Desktop composition (≥ 1024px) — ASCII

*(Updated with weight tiers and alignment zones.)*

```text
┌────────────────────────────────── HEADER (BLK-001 + BLK-002) ──────────────────────────────────┐
│  full-bleed background band (viewport width)                                                    │
│  ┌──────────────────────────── inner container max 1170 · pad-x 40 ────────────────────────────┐│
│  │                                                                                              ││
│  │  ROW 1 — TOP ROW (BLK-001) · SECONDARY band                                                  ││
│  │  ┌──────────────┐  ┌─────────────────────────┐  ┌──────────────────┐  ┌───────────────────┐ ││
│  │  │ ZONE A       │  │ ZONE B                  │  │ ZONE C           │  │ ZONE D            │ ││
│  │  │ LEFT         │  │ CENTER-LEFT             │  │ CENTER-RIGHT     │  │ RIGHT             │ ││
│  │  │ UTILITY      │  │ SUPPORTING              │  │ SECONDARY        │  │ SECONDARY ★       │ ││
│  │  │ Region Group │  │ Hours Group             │  │ Utility Links    │  │ Phone Group       │ ││
│  │  │              │  │                         │  │ Group            │  │ (strongest R1)    │ ││
│  │  │ Москва,      │  │ пн-пт 08:00-18:00       │  │ Генотипирование  │  │ +7 925 183-64-64  │ ││
│  │  │ Московская   │  │ сб-вс 08:00-22:00       │  │ Специалисты      │  │ +7 995 023-92-26  │ ││
│  │  │ область      │  │                         │  │                  │  │                   │ ││
│  │  └──────────────┘  └─────────────────────────┘  └──────────────────┘  └───────────────────┘ ││
│  │                                                                                              ││
│  │  ROW 2 — MAIN ROW (BLK-002) · PRIMARY band · dominates stack                                 ││
│  │  ┌────────────────────────────┐  ┌────────────────────────────────────┐  ┌───────────────┐ ││
│  │  │ ZONE E · LEFT · PRIMARY    │  │ ZONE F · CENTER · PRIMARY          │  │ ZONE G · RIGHT│ ││
│  │  │ Logo Group                 │  │ Primary Nav Group                  │  │ PRIMARY       │ ││
│  │  │ (brand object)             │  │                                    │  │ CTA Group     │ ││
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

### 16.2 Row summary strip

```text
ROW 1 (TOP ROW) — 4 zones — SECONDARY band
LEFT[Region UTILITY] · C-L[Hours SUPPORTING] · C-R[Util links SECONDARY] · RIGHT[Phones SECONDARY ★]

ROW 2 (MAIN ROW) — 3 zones — PRIMARY band
LEFT[Logo PRIMARY] · CENTER[Nav PRIMARY] · RIGHT[CTA PRIMARY action]
```

### 16.3 Visual weight strip

```text
PRIMARY:     [ MAIN ROW: Logo · Nav · CTA ]
SECONDARY:   [ TOP ROW: Phones ★ · Utility links ]
UTILITY:     [ TOP ROW: Region ]
SUPPORTING:  [ TOP ROW: Hours ]
```

---

## 17. Operator Decisions Required

| ID | Topic | Why not closed in spec |
|----|-------|------------------------|
| **ODR-01** | Layout Spec v2 **APPROVED vs REVISE** | Operator gate — this document |
| **ODR-02** | Hours **once vs per-region** (SU-06) | Text layer suggests once — operator confirm |
| **ODR-03** | «Лечение и профилактика» placement (SU-03) | Affects Logo Group stack |
| **ODR-04** | CTA / accent **Visual SSOT vs Production Standards** (CF-008, CF-010) | Affects LR-002 prevention at styling phase — **not** composition zones |
| **ODR-05** | Logo asset delivery workflow (SU-04) | Asset gap — composition placement still locked |
| **ODR-06** | «Заказать звонок» behavior (SU-12 · D-015) | Does not block composition approval |

---

## 18. Implementation Readiness

| Gate | Verdict | Notes |
|------|---------|-------|
| Layout Spec filed | **YES** | This document v2 |
| Prior v1 preserved | **YES** | FP-0002-HEADER-LAYOUT-SPEC-v1.md untouched |
| Visual Weight Model | **YES** | §6 |
| Alignment Model | **YES** | §7 |
| Row 1 Composition Model | **YES** | §8 |
| Row 2 Composition Model | **YES** | §9 |
| Layout Risk Assessment | **YES** | §15 (LR-001…LR-012) |
| Operator APPROVED | **NO** | **STOP** — awaiting APPROVED \| REVISE |
| Composition sufficient for assembly | **YES WITH UNKNOWN** | Row/zone/group + weight/alignment locked; SU-01…SU-18 · ODR-02…06 open |
| HTML/CSS permitted | **NO** | Forbidden until operator **APPROVED** per Layout Spec Law §3 |
| Operator Visual Review | **N/A** | Runs **after** implementation — separate gate |
| Logo asset ready | **NO** | SU-04 — non-blocking for spec gate |
| PDF on disk re-verify | **NO** | SU-15 — operator should compare against SOURCE-001 PDF |

**Post-approval implementation must cite:**

```text
LAYOUT SPEC REF — FP-0002-HEADER-LAYOUT-SPEC-v2.md — APPROVED <date>
LAYOUT SPEC GATE — PASS (APPROVED)
```

---

## Document control

| Field | Value |
|-------|-------|
| Version | **v2** |
| Status | **DRAFT** |
| Prior version | [FP-0002-HEADER-LAYOUT-SPEC-v1.md](FP-0002-HEADER-LAYOUT-SPEC-v1.md) — preserved |
| Supersedes v1 when | Operator marks v2 **APPROVED** |
| Related | FP-0002-HEADER-MINI-AUDIT-v1.md (content audit — **not** substitute) |
| Commit / push | Not performed |

---

**Operator gate request:**

Layout Spec **v2** готов для **Header (BLK-001 + BLK-002, desktop ≥1024px)** с моделями визуального веса, выравнивания, композиции строк и оценкой рисков.  
Проверьте декомпозицию против Visual SSOT (SOURCE-001 + matching templates).  
Требуется решение: **APPROVED** или **REVISE**.  
Верстка запрещена до **APPROVED**.
