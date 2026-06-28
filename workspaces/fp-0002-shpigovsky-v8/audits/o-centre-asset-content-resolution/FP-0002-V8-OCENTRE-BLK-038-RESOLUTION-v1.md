# FP-0002 V8 O-Centre BLK-038 Resolution v1

**Inventory reference:** BLK-038 (infrastructure imagery / comfort band)  
**Charter blocks:** OC-B08 + OC-B10  
**Figma authority:** Spig_v1.2

## Finding

BLK-038 does **not** appear as a separate desktop section in Spig_v1.2. Infrastructure photography and decorative «/02», «/03», «/04» stage markers live inside frame `1:2440` «преимущества» alongside BLK-037 narrative copy.

On **mobile**, a dedicated frame «Комфорт, приватность» (`1:5697`, 390×4958) likely corresponds to charter OC-B10 / reuse of `comfort.html` pattern with O-Centre-specific photos.

## Resolution table

| Field | Value | Source | Confidence |
|---|---|---|---|
| Design title (desktop) | преимущества (shared) | `1:2440` | CONFIRMED |
| Design title (mobile) | Комфорт, приватность | `1:5697` | CONFIRMED |
| Heading | (none separate; uses OC-B08 H2) | — | CONFIRMED |
| Copy | Shared bullets from BLK-037 resolution | `1:2449`–`1:2477` | CONFIRMED |
| Images | 22 nodes excluding section bg; hashes in extract | `desktopSectionImages.преимущества` | CONFIRMED |
| Desktop layout | Photo grid interleaved with narrative | `1:2440` | CONFIRMED |
| Mobile layout | Dedicated comfort frame | `1:5697` | PROBABLE |
| Relationship with BLK-037 | **Single Figma section** on desktop | Anatomy | CONFIRMED |
| One vs two partials | Figma supports **one** unique desktop partial; mobile may reuse CF-006 with new assets | Charter vs Figma | PROBABLE — implementation decision deferred |
| Founder quote position | **Outside** this section (in `3- Услуги`) | Order | CONFIRMED |

## Status

**COPY RESOLVED (shared with BLK-037)** · **ASSETS PENDING export** · **MOBILE COMFORT FRAME PROBABLE**

Not `BLOCKED_MISSING_CANONICAL_SOURCE` for imagery refs; export tooling is the remaining gate.
