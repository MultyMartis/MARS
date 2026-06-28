# FP-0002 V8 O-Centre Staff-Photo Reuse Audit v1

**Date:** 2026-06-29

---

## Home staff-photo reference

| Attribute | `home-staff-photo.html` |
|---|---|
| Partial | `src/partials/sections/home-staff-photo.html` |
| Class root | `.home-staff-photo` |
| Structure | `section > container > bleed > single img` |
| Image | `shpigovsky-staff-group.webp` (1139×443) |
| Heading | None (aria-label only) |
| Role | Full-width team group photo between Home blocks |
| SCSS | Dedicated band; bleed past container |

---

## O-Centre candidate bands

| Design section | Staff-photo analog? | Evidence |
|---|---|---|
| BLK-038 Infrastructure / «преимущества» | Possible group or exterior photo | Large desktop frame; may include team or building — **UNRESOLVED** without PDF raster |
| BLK-037 «Наш Дом» | Narrative + photos | Not proven as single bleed staff band |
| Mobile «Подход» | Text-heavy | No staff bleed in parse |
| Home sequence staff photo | **Not in PG-005 inventory** | O-Centre does not list home-staff-photo block |

---

## Comparison matrix

| Criterion | Home staff-photo | O-Centre candidate | Match |
|---|---|---:|
| Visual role | Decorative team band | Infrastructure / narrative photos | Partial |
| Skeleton | Single bleed image | Multi-image or text+image composite | No |
| Image ratio | ~2.57:1 wide group | Unknown | UNRESOLVED |
| Container/bleed | Yes | Unknown | UNRESOLVED |
| Heading/caption | aria-label only | H2 sections elsewhere | No |
| Semantic image | Team group alt text | May be building/interior | Different |

---

## Structural identity

**No** — O-Centre design does not document the same single bleed staff band in inventory or Figma section names.

---

## Visual identity

Home staff-photo is a **thin full-bleed group shot** between marketing blocks. O-Centre emphasizes **institutional narrative** (BLK-036–038) and **comfort mosaic** — different visual grammar.

---

## Classification

**`HOME_SPECIFIC`**

`home-staff-photo` is Home sequence placement. O-Centre should **not** reuse this partial unless operator proves identical band in PG-005 PDF.

**Secondary note:** `clinic-landscape` (CF-010) is also a bleed landscape band but different asset/alt role — `SIMILAR_BUT_DIFFERENT` if exterior photo needed; not on PG-005 inventory row.

---

## Implementation recommendation

1. **Do not** place `home-staff-photo.html` on O-Centre by default.
2. If infrastructure band needs wide photo: evaluate **`clinic-landscape.html`** with new About-specific asset — not staff-photo.
3. Team presence on O-Centre is covered by **specialists slider (BLK-026)**, not staff bleed band.
4. **Do not rename** `home-staff-photo` in this task.

---

## Result

**PASS** — false reuse rejected; staff-photo remains Home-specific.
