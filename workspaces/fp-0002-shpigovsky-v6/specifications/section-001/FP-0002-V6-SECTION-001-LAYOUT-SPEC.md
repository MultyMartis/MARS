# FP-0002 V6 SECTION-001 LAYOUT SPEC

**Scope:** SECTION-001 — Header + Hero composite  
**Group decomposition ref:** [FP-0002-V6-SECTION-001-GROUP-DECOMPOSITION.md](FP-0002-V6-SECTION-001-GROUP-DECOMPOSITION.md)  
**Law:** [layout-spec-law-v1.md](../../../../projects/mars-website-factory/layout-spec-law-v1.md)  
**Status:** DRAFT — READY FOR OPERATOR REVIEW

---

## Block identity

| Field | Value |
|-------|-------|
| `section_id` | SECTION-001 |
| `composite` | true |
| `internal_groups` | SECTION-001-GROUP-01 (Header), SECTION-001-GROUP-02 (Hero) |
| `page_slug` | home |
| `neighbor_below` | SECTION-002 (Y=904) |

---

## Zone model

```text
SECTION-001 [Y 0–904, full page width 1398px]
├── ZONE-A  Header stack (GROUP-01) — container-bound content
│   ├── ROW-01  top bar (GROUP-01…06)
│   ├── RULE    horizontal separator
│   └── ROW-02  navigation (GROUP-07…08)
└── ZONE-B  Hero stack (GROUP-02) — full-bleed photo + centered overlay
    ├── LAYER-1  hero photo (GROUP-09) — full-bleed
    └── LAYER-2  overlay panel + CTA (GROUP-10…13) — container-centered
```

---

## Container model

| Zone | Container binding | Evidence |
|------|-------------------|----------|
| Header ROW-01/02 content | `container-main` 1220px centered | Logo left x≈130 aligns with JPG content band; operator rule 1220px |
| Header background wash | Full viewport width light wash in top band | y 0–119 light samples |
| Hero photo | `container-bleed-media` / full-bleed within section | x 19–1379 photo span |
| Hero overlay + CTA | `container-main` centered column | Frosted panel centered ~x 400–1000 |

**Deferred:** `container-padding-inline-desktop: 50px` — not auto-applied. Observed JPG inset x_start≈130 on 1398px page (width 1138px band) is **OBSERVED_JPG_VALUE** — not CSS max-width.

---

## Row composition — Header

### ROW-01

| Order | GROUP-ID | Alignment | Isolation |
|-------|----------|-----------|-----------|
| 1 | GROUP-01 Logo | left | must not merge with address |
| 2 | GROUP-02 Address | after logo, inline cluster | separate from schedule |
| 3 | GROUP-03 Schedule | after address | separate from phones |
| 4 | GROUP-04 Phones | center-right block | separate from messengers |
| 5 | GROUP-05 Messengers | right of phones | icon pair |
| 6 | GROUP-06 CTA outline | far right | distinct control |

**Vertical alignment:** ROW-01 groups share a common vertical center band y ~38–85.

### ROW-02

| Order | GROUP-ID | Alignment |
|-------|----------|-----------|
| 1 | GROUP-07 Navigation | horizontal link row, left anchored with logo |
| 2 | GROUP-08 Search | far right, aligned under CTA column |

**Separator:** Thin horizontal rule between ROW-01 and ROW-02 — container-bound width (not full viewport bleed).

---

## Row composition — Hero

| Layer | GROUP-ID | Layout |
|-------|----------|--------|
| Background | GROUP-09 | Photo fills section below header; rounded top corners visible below nav |
| Foreground | GROUP-10–12 | Frosted panel centered; tagline above display title |
| Foreground | GROUP-13 | CTA centered below panel |

**Vertical rhythm:** Overlay stack occupies lower-middle of hero band (~y 650–837); photo visible above and around panel.

---

## Grid and alignment

| Pattern | Application |
|---------|-------------|
| Header ROW-01 | Single horizontal flex/grid row with discrete groups — no aggregate contact blob |
| Header ROW-02 | Single row: nav links + trailing search |
| Hero | Single column center stack on photo background |

---

## Overlap and layering

| Layer | Z-order | Notes |
|-------|-------|-------|
| Hero photo | 1 | Behind header bottom edge — trees visible under nav |
| Header wash | 2 | Opaque/semi-opaque light wash top band |
| Hero overlay + CTA | 3 | Above photo |
| Header text/controls | 4 | Topmost in header band |

---

## Responsive boundary

Desktop structure specified from JPG 1398px width only.

Below **1024px**: layout **SAFE UNKNOWN** — separate responsive specification gate required.

---

## Layout Spec gate

```text
LAYOUT SPEC — SECTION-001 — DRAFT
GROUP DECOMPOSITION REF — FP-0002-V6-SECTION-001-GROUP-DECOMPOSITION.md — PENDING
OPERATOR DECISION — PENDING
HTML/CSS — FORBIDDEN until Implementation Specification approved
```
