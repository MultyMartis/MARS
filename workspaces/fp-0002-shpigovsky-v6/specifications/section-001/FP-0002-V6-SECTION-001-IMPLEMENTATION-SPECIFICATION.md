# FP-0002 V6 SECTION-001 IMPLEMENTATION SPECIFICATION

**Contract:** [block-implementation-specification-contract-v1.md](../../../../projects/mars-website-factory/block-implementation-specification-contract-v1.md)  
**Foundation:** [FP-0002-V6-STYLE-FOUNDATION.json](../../foundation/FP-0002-V6-STYLE-FOUNDATION.json) — `site_wide_style_foundation_approved: true`  
**Status:** READY FOR OPERATOR REVIEW

---

## Identity

| Field | Value |
|-------|-------|
| `block_spec_id` | FP-0002-V6-SPEC-SECTION-001 |
| `section_id` | SECTION-001 |
| `composite` | true |
| `internal_groups` | SECTION-001-GROUP-01 (Header), SECTION-001-GROUP-02 (Hero) |
| `component_ids` | CMP-002 (header), CMP-003 (hero) |
| `page_slug` | home |
| `section_order` | 1 |

---

## Source authority

| Field | Value |
|-------|-------|
| Visual SSOT | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Region | X 0–1398, Y 0–904 |
| Grounding | CONFIRMED_SECTION_BOUNDARY at Y=904 HIGH |
| Forbidden sources | FIG, PDF, v1–v5, legacy FP-0002 workspaces |
| Evidence crops | `specifications/section-001/evidence/` |

---

## Section geometry

| Measure | Value | Classification |
|---------|-------|----------------|
| Y start | 0 | OPERATOR_DECISION |
| Y end | 904 | CONFIRMED_SECTION_BOUNDARY |
| Height | 904px | EX-002 block exception |
| Page width | 1398px | OBSERVED_JPG_VALUE |
| Y=174 estimate | OBSERVED_JPG_ESTIMATE | **CSS_USE_FORBIDDEN** |

---

## Composite structure

SECTION-001 is implemented as **one** composite section partial. Header and Hero are **internal groups** — not separate major sections.

```text
SECTION-001 (904px)
├── SECTION-001-GROUP-01  Header
│   ├── ROW-01  logo | address | schedule | phones | messengers | CTA-outline
│   ├── separator rule
│   └── ROW-02  navigation | search
└── SECTION-001-GROUP-02  Hero
    ├── LAYER photo (full-bleed)
    └── LAYER overlay panel + red CTA
```

---

## Header group

### Observed geometry

| Measure | Observed (JPG px) | Confidence |
|---------|-------------------|------------|
| Light wash band | y 0–119 | MEDIUM (probe) |
| Logo bounds | x 130–312, y 18–100, h 82 | MEDIUM |
| Phones block | x 851–1200, y 38–80, h 42 | MEDIUM |
| Nav text band | y 132–174 | MEDIUM |
| Photo dominates center column | from y ~107 center; full photo from ~174 | MEDIUM |
| Separator rule | ~y 120–125 | LOW — visual only |
| Header ↔ Hero overlap | Photo visible below nav; header on light wash | HIGH |

**Forbidden:** Using `174px` as CSS `height`, `padding`, `margin`, or split coordinate.

### Content groups (discrete)

| GROUP | Elements |
|-------|----------|
| Logo | Brand mark, lifebuoy icon, tagline |
| Address | City + region lines |
| Schedule | Weekday + weekend hours |
| Phones | Two stacked numbers |
| Messengers | Telegram, WhatsApp icons |
| CTA outline | «ЗАКАЗАТЬ ЗВОНОК» — border pill, not red fill |
| Navigation | Seven text links |
| Search | Magnifying glass icon |

### Header background

- Light page-wash background in top band — **no** separate full-width dark layer
- Thin horizontal separator between rows — observed; exact color SAFE UNKNOWN
- Header does **not** use sticky positioning (not visible in JPG)

---

## Hero group

### Observed geometry

| Measure | Observed (JPG px) | Confidence |
|---------|-------------------|------------|
| Photo layer | Full width ~x 19–1379; rounded top below nav | HIGH |
| Frosted overlay panel | Center ~x 400–1000, y ~660–780 | MEDIUM |
| Hero CTA button | x 557, y 792, w 297, **h 45** | HIGH (probe) |
| Section lower edge | Y=904 — transition to light page SECTION-002 | HIGH |
| Bottom vignette/dark band | y 619–903 algorithmic — photo shadow, not a separate UI panel | LOW |

### Structure order (top → bottom within hero foreground)

1. Hero tagline (sans, white, in frosted panel)
2. Hero display title (serif/display, white, in panel)
3. Red CTA button (below panel, centered)

### Hero CTA label

Observed: **«ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ»**

---

## Container bindings

| Element | Binding | Proposed implementation |
|---------|---------|-------------------------|
| Header rows content | `container-main` max-width **1220px** centered | APPROVED_OPERATOR_RULE |
| Header side inset | Observed JPG x_start **130** on 1398px page | OBSERVED — map via block padding proposal, not 1138px max-width |
| Hero photo | Full-bleed within section | `container-bleed-media` |
| Hero overlay + CTA | Centered within `container-main` | block-level |
| `container-padding-inline-desktop` | **50px** | **DEFERRED** — proposal after inset measurement at HTML gate |

---

## Grid and alignment

| Area | Pattern |
|------|---------|
| Header ROW-01 | Horizontal row; groups left→right per decomposition |
| Header ROW-02 | Nav links distributed; search trailing right |
| Hero | Single centered column stack |

---

## Typography bindings

| Role | Element | Observed approx. | Normalized proposal | Weight | Case | Color role | Confidence |
|------|---------|------------------|----------------------|--------|------|------------|------------|
| `nav-primary` | Header nav links | ~14–16px | **15px** block proposal | regular | sentence | `primary-text` | LOW |
| `meta-secondary` | Address, schedule | ~12–14px | **14px** block proposal | regular | sentence | `secondary-text` | LOW |
| `contact-emphasis` | Phone numbers | ~16–18px | **18px** block proposal | semibold | — | `primary-text` | MEDIUM |
| `cta-outline-label` | «ЗАКАЗАТЬ ЗВОНОК» | ~12px | **12px** block proposal | medium | ALL CAPS | `primary-text` | LOW |
| `hero-tagline` | Tagline in panel | ~16–18px | **16px** block proposal | regular | sentence | `inverse` | MEDIUM |
| `hero-display` | «Шпиговский дом» | ~36–48px | **40px** block proposal | regular | title case | `inverse` | MEDIUM |
| `hero-cta-label` | CTA label | ~12–14px | **13px** block proposal | medium | ALL CAPS | `inverse` | MEDIUM |

**Font-family:** SAFE UNKNOWN for all roles — do not invent.

---

## Spacing bindings

| Region | Observed | Foundation / proposal | Property class |
|--------|----------|----------------------|----------------|
| Logo ↔ address gap | ~20–30px | `text-stack-gap` **20px** margin or block **30px** | margin |
| Address line stack | ~5–10px | **10px** block proposal | margin |
| Phones vertical stack | ~5–10px | **10px** block proposal | margin |
| Messenger icons gap | ~10px | OL-01 **10px** gap | gap |
| ROW-01 ↔ separator | ~15–25px | **20px** block proposal | margin |
| Separator ↔ ROW-02 | ~10–15px | **15px** `accordion-row-spacing` margin | margin |
| Nav link spacing | ~25–35px | `grid-gap-standard` **30px** | gap |
| Overlay tagline ↔ title | ~10–20px | `text-stack-gap` **20px** | margin |
| Overlay panel ↔ hero CTA | ~15–25px | **20px** block proposal | margin |
| Hero CTA internal padding | derived from h45 | block exception | padding |

**Rule:** `accordion-row-spacing` is **margin only** — never CSS `gap`.

---

## Color bindings

| Role | Sampled candidate (RGB) | JPEG variance | Confidence | Site-wide role |
|------|-------------------------|---------------|------------|----------------|
| `page-background` | 230, 239, 246 (#e6eff6 family) | MEDIUM | MEDIUM | page-background |
| `primary-text` | dark blue-grey ~60–80 RGB in header | HIGH | MEDIUM | primary-text |
| `secondary-text` | muted grey in meta lines | HIGH | LOW | secondary-text |
| `inverse` | white 255,255,255 on overlay | LOW | HIGH | inverse |
| `accent` | hero CTA red — sample unreliable in JPEG | HIGH | LOW | accent |
| `border-subtle` | header CTA border / separator | HIGH | LOW | border |
| `surface-frosted` | overlay panel semi-white | HIGH | MEDIUM | surface |

**HEX production values:** SAFE UNKNOWN — use color roles only until operator approves samples.

---

## Button bindings

| Family | Location | Observed outer height | Text | Fill | Border | Radius | Proposal |
|--------|----------|----------------------|------|------|--------|--------|----------|
| FAM-BTN-HEADER-OUTLINE | Header GROUP-06 | ~30–35px | «ЗАКАЗАТЬ ЗВОНОК» | transparent | dark 1px | pill (~50% height) | block-level — **not** `button-height-standard` 30px global |
| FAM-BTN-HERO-PRIMARY | Hero GROUP-13 | **45px** | «ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ» | red fill | none visible | pill | **EX-S001-001** height 45px |

**Critical:** `button-height-standard: 30px` is **DEFERRED** globally. Hero CTA observed **45px** — do **not** normalize down to 30px.

---

## Radius and border bindings

| Element | Observed | Proposal | Status |
|---------|----------|----------|--------|
| Header CTA | pill outline | border-radius 50% height block proposal | BLOCK_LEVEL |
| Hero CTA | pill filled | border-radius 50% height block proposal | BLOCK_LEVEL |
| Hero frosted panel | large rounded corners | SAFE UNKNOWN px — block exception required | HOLD |
| Hero photo top corners | visible radius below nav | SAFE UNKNOWN px | HOLD |

---

## Asset requirements

| Asset | Role | Extraction |
|-------|------|------------|
| Logo SVG/raster | GROUP-01 | Required before HTML — not extracted in this task |
| Hero photo | GROUP-09 | Required — full-bleed background |
| Telegram icon | GROUP-05 | Existing `src/img/social/telegram.svg` — verify against JPG |
| WhatsApp icon | GROUP-05 | Existing `src/img/social/whatsapp.svg` — verify against JPG |
| Search icon | GROUP-08 | Required — SVG |

---

## Layering and overlap

1. Hero photo (bottom)
2. Header light wash (top band)
3. Hero frosted panel + text
4. Hero red CTA
5. Header interactive elements (top)

Header nav row sits above photo; photo rounded corners begin below nav.

---

## Desktop behavior

- Single desktop layout per JPG 1398px
- SECTION-001 total height **904px** desktop (EX-002)
- Centered `container-main` 1220px for header content and hero overlay stack

---

## Responsive SAFE UNKNOWN

| Item | Status |
|------|--------|
| Mobile header menu | SAFE UNKNOWN |
| Mobile hero crop | SAFE UNKNOWN |
| Breakpoint | Operator rule **1024px** — rebuild requires separate responsive spec |
| Tablet intermediate | SAFE UNKNOWN |

Desktop HTML is **not blocked** by missing mobile source, but mobile layout must not be invented without spec.

---

## Interaction SAFE UNKNOWN

| Behavior | Status |
|----------|--------|
| Sticky header | SAFE UNKNOWN |
| Nav hover / active | SAFE UNKNOWN |
| Search click | SAFE UNKNOWN |
| CTA click targets | SAFE UNKNOWN — href/onclick not in JPG |
| Dropdown | Not visible — do not invent |

---

## Exact geometry exceptions

| ID | Token | Value | Reason |
|----|-------|-------|--------|
| EX-002 | `hero-band-height-desktop` | 904px | SECTION-001 outer boundary |
| EX-S001-001 | `hero-cta-height` | 45px | Observed hero button outer height |
| EX-S001-002 | `hero-cta-width` | ~297px | Observed at desktop JPG scale — scale proportionally with caution |

---

## Forbidden deviations

Implementers **must not**:

1. Invent Header height as a single magic number from `Y=174`
2. Use `174px` as CSS boundary between Header and Hero
3. Choose random gaps outside OL-01 / approved foundation / block exceptions
4. Create a new container width other than `container-main: 1220px`
5. Invent font-family
6. Invent HEX colors
7. Create sticky Header without operator approval
8. Create dropdown menus not in JPG
9. Reorder groups or rows
10. Split Header and Hero into independent major sections
11. Start mobile layout without separate responsive specification
12. Patch visual mismatch with local magic numbers
13. Apply `button-height-standard: 30px` to hero CTA
14. Use `accordion-row-spacing` as CSS `gap`
15. Set `max-width: 1138px` from JPG observed band

---

## HTML structure gate

```text
html_structure_authorized: false
```

Requires: operator approval of this specification.

---

## SCSS gate

```text
scss_authorized: false
```

Requires: `html_structure_authorized: true` + foundation approved (satisfied) + HTML review PASS.

---

## Visual QA acceptance criteria

1. Screenshot compare region Y 0–904 against JPG crop `evidence/01-section-001-full.jpg`
2. All GROUP-IDs present in decomposition — no aggregate contact blob
3. Header CTA is outline pill — not red primary
4. Hero CTA height ~45px — not 30px
5. `container-main` 1220px — not 1138px
6. Foundation token checklist in [FP-0002-V6-SECTION-001-SOURCE-TO-TOKEN-MAP.md](FP-0002-V6-SECTION-001-SOURCE-TO-TOKEN-MAP.md)
7. Operator visual review per factory operator-visual-approval-law

---

## Operator approval status

```text
section_001_specification_status: READY_FOR_OPERATOR_REVIEW
implementation_authorized: false
header_implementation_authorized: false
hero_implementation_authorized: false
foundation_approved_by: operator
site_wide_style_foundation_approved: true
```
