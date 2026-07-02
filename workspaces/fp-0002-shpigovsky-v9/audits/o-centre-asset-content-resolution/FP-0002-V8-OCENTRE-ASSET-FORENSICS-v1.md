# FP-0002 V8 O-Centre Asset Forensics v1

**Method:** Figma image hash from Spig_v1.2 extract vs repository file SHA-256; filename similarity not used as proof.

| Asset ID | Block | Figma ref | Existing candidate | Match | Export needed | Confidence |
|---|---|---|---|---:|---:|---|
| OC-A001 | OC-B01 hero | `1:2226` c96ae505… | `services-hero.webp` | 0 | 1 | CONFIRMED |
| OC-A101 | OC-B08 | `1:2451` 5d64fd20… | none verified | 0 | 1 | CONFIRMED ref |
| OC-A102 | OC-B08 | `1:2452` b46f4858… | none verified | 0 | 1 | CONFIRMED ref |
| OC-A103 | OC-B08 | `1:2453` e7930992… | none verified | 0 | 1 | CONFIRMED ref |
| OC-A104+ | OC-B08 | 19 additional nodes | none verified | 0 | 1 | CONFIRMED ref |
| OC-A200 | OC-B03 | `1:2248` bg d3ac7d00… | none | 0 | 1 | PROBABLE |
| OC-A300 | OC-B11 | `1:2524` specialist | CF-005 assets | unverified | 0 | PROBABLE reuse |

## Hero detail

- Exported JPG from fig zip matches hash `c96ae5052d14489981804509c79bb86e1bb6eae1`.
- WebP production file created at `src/img/content/o-centre/o-centre-hero.webp`.
- **No perceptual hash tooling** in repo; byte hash used.

## Infrastructure photos

- 22 distinct image hashes under `desktopSectionImages.преимущества` (excluding section background).
- No byte-level match found against existing `src/img/content/` inventory during this task.
- Bulk export deferred to targeted export task.

## Result

Hero **forensically resolved**. Infrastructure photos **catalogued, export pending**.

Full manifest: `data/FP-0002-V8-OCENTRE-APPROVED-ASSET-MANIFEST.json`
