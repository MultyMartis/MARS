# FP-0002 V8 O-Centre Approach Discrepancy v1

## Canonical anatomy (Figma `1:2341`)
- H2 «Наш подход к лечению» + play link
- Red-line highlight paragraph
- Intro paragraph
- Staff group photo band
- Four titled cards (Lorem bodies omitted by policy)
- Large clinic/territory landscape bleed (CF-010 reuse candidate)

## Current anatomy
- Inline `program-approach-band` with correct headings and staff photo
- Four card titles without bodies (authorized)
- **Missing** clinic-landscape include after cards
- **Wrong position** — no first CTA before this block

## Component boundaries
| Element | Keep in category component | Separate approach region |
|---|---|---|
| Who-we-treat copy | Yes | No |
| Group photo + 4 cards | No | Yes — belongs to `1:2310` who-we-treat frame |
| Approach heading/cards | No | Yes |
| Clinic landscape | No | Yes — `clinic-landscape.html` reuse |

**Decision:** `DIRECT_REUSE_CLINIC_LANDSCAPE` for territory band asset `shpigovsky-clinic-landscape.webp`.
