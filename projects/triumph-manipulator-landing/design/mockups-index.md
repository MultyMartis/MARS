# Mockups index — Triumph Manipulator Landing (V1 archive)

**Role:** lightweight index for **V1** PNG slices (historical strip-era landing reference). **Not** V2 canonical visuals — for V2 use `design/v2/` per [`design/README.md`](./README.md).  
**Location on disk:** `projects/triumph-manipulator-landing/design/v1/`

## Files

| File | Dimensions (px) | Notes |
|------|-------------------|--------|
| `01.png` | 1672 × 941 | Top segment of the continuous landing scroll (filename order). |
| `02.png` | 1672 × 941 | Continuation. |
| `03.png` | 1672 × 941 | Continuation. |
| `04.png` | 1536 × 1024 | Final segment; **different width/height** than 01–03 — expect layout or export variance; verify in implementation. |

## Natural order

1. `01.png`  
2. `02.png`  
3. `03.png`  
4. `04.png`

Treat **01 → 04** as **one vertical landing** composed of four raster exports, not four separate pages.

## Source of truth

- **Visual layout (V1 only):** these PNGs in `design/v1/`.
- **Design system PDF (if present):** per project guidance, a “DESIGN SYSTEM EXPORT” PDF may only enumerate export *categories*, not confirmed token values. Do not treat unstated numbers as approved unless backed by project docs or measured from approved sources.

## Frontend workspace wiring

Placeholder HTML/SCSS strips in the Gulp workspace mirror this order; see `frontend-section-map.md`.
