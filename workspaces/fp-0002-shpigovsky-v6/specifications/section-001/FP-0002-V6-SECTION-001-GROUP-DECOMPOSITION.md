# FP-0002 V6 SECTION-001 GROUP DECOMPOSITION

**Scope:** SECTION-001 — Header + Hero composite  
**Visual SSOT:** `HOME-PAGE-FULL-MOCKUP.jpg` SHA-256 `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290`  
**Region:** X 0–1398, Y 0–904  
**Law:** [group-decomposition-law-v1.md](../../../../projects/mars-website-factory/group-decomposition-law-v1.md)  
**Status:** DRAFT — READY FOR OPERATOR REVIEW

---

## Composite rule

SECTION-001 is **one** major section. Header and Hero are **internal groups**, not independent major sections.

`Y=174` is **OBSERVED_JPG_ESTIMATE** only — **CSS_USE_FORBIDDEN** — **NOT_AN_IMPLEMENTATION_BOUNDARY**.

---

## SECTION-001-GROUP-01 — Header

### ROW register

| ROW-ID | Label | Visual SSOT anchor (Y approx.) |
|--------|-------|--------------------------------|
| ROW-01 | TOP BAR — logo, meta, contacts, CTA | Y ~18–100 |
| ROW-02 | MAIN NAV ROW — menu + search | Y ~132–174 |

### GROUP register — ROW-01

| GROUP-ID | Name | Contents | Position | Bounds (JPG px, evidence) |
|----------|------|----------|----------|----------------------------|
| GROUP-01 | Logo | Brand mark «дом Шпиговский», lifebuoy icon, tagline «центр профилактики зависимостей» | left | x 130–312, y 18–100 |
| GROUP-02 | Address | «Москва,» / «Московская область» | center-left | x ~320–480, y ~38–80 |
| GROUP-03 | Schedule | «пн-пт: 08:00–18:00,» / «сб-вс: 08:00–22:00» | center | x ~490–680, y ~38–80 |
| GROUP-04 | Phones | Two tel numbers stacked | center-right | x 851–1200, y 38–80 |
| GROUP-05 | Messengers | Telegram + WhatsApp circular icons | right | x ~1200–1260, y ~40–85 |
| GROUP-06 | CTA outline | Pill button «ЗАКАЗАТЬ ЗВОНОК» — border, no red fill | far right | x ~1260–1330, y ~45–80 |

### GROUP register — ROW-02

| GROUP-ID | Name | Contents | Position | Bounds (JPG px) |
|----------|------|----------|----------|-----------------|
| GROUP-07 | Navigation | Eight list items: seven text links (Лечение и профилактика … Контакты) + search button (`fas fa-search`) as final item | left → far right | y 132–174, x ~130–1360 |
| GROUP-08 | Search | Magnifying-glass icon control — **eighth** `<li>` inside GROUP-07 nav list (not a sibling block) | far right | y ~135–165, x ~1320–1360 |

### Header relationships

| Relationship | Detail |
|--------------|--------|
| ROW-01 ↔ ROW-02 | Separated by thin horizontal rule (~y 120–125); shared light page-wash background |
| Logo ↔ Nav | Logo left edge aligns with nav left edge (~x 130) |
| CTA ↔ Search | Search right-aligned under CTA column |
| Header ↔ Hero | Header sits above hero photo; photo visible below nav with rounded top corners; **no** operator-approved Y split coordinate |
| Background | Light wash `#e6eff6` family in top band y 0–119 (probe); not full-bleed separator from page |

### Header SAFE UNKNOWN

- Sticky behavior
- Nav hover / active states
- Search click behavior
- Exact header block height as single CSS value
- `Y=174` as Header/Hero boundary

---

## SECTION-001-GROUP-02 — Hero

### ROW register

| ROW-ID | Label | Visual SSOT anchor |
|--------|-------|-------------------|
| ROW-H1 | FULL-BLEED PHOTO | Y ~107–904 |
| ROW-H2 | OVERLAY CONTENT STACK | Y ~650–837 |

### GROUP register

| GROUP-ID | Name | Contents | Position | Bounds (JPG px) |
|----------|------|----------|----------|-----------------|
| GROUP-09 | Hero photo | Building in forest — full content width, rounded top corners | full-bleed within section | x ~19–1379, y photo dominant from ~174 |
| GROUP-10 | Frosted overlay panel | Semi-transparent rounded rectangle | center | x ~400–1000, y ~660–780 (visual) |
| GROUP-11 | Hero tagline | «Центр профилактики и лечения зависимостей» | center in panel | white sans-serif |
| GROUP-12 | Hero display title | «Шпиговский дом» | center in panel | large white serif/display |
| GROUP-13 | Hero CTA | Red pill «ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ» | center below panel | x 557–854, y 792, h **45** |

### Hero relationships

| Relationship | Detail |
|--------------|--------|
| Photo ↔ Overlay | Photo is background layer; frosted panel + CTA are foreground |
| Overlay ↔ CTA | Vertical gap between panel bottom and CTA top — block-level spacing proposal |
| Hero ↔ SECTION-002 | Hard boundary at Y=904 — light page wash begins |

### Hero SAFE UNKNOWN

- Exact overlay panel radius px
- Photo crop focal point at responsive widths
- Mobile stacking order

---

## Forbidden aggregation patterns

The following are **forbidden** without discrete GROUP-IDs:

- CONTACT BLOCK (merges address, schedule, phones, messengers)
- NAV AREA (omits search)
- HERO CONTENT CLUSTER (merges tagline, title, CTA)

---

## Operator gate

```text
GROUP DECOMPOSITION — SECTION-001 — DRAFT
GROUP DECOMPOSITION GATE — PENDING OPERATOR REVIEW
ROW COUNT — Header 2 + Hero 2
GROUP COUNT — 13
VISUAL SSOT REF — HOME-PAGE-FULL-MOCKUP.jpg (SHA-256 verified)
```

Evidence: `specifications/section-001/evidence/`
