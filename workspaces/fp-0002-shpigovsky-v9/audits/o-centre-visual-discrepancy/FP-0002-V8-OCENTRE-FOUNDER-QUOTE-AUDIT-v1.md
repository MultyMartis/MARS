# FP-0002 V8 O-Centre Founder Quote Audit v1

**Date:** 2026-06-29
**Implementation commit:** dbc057cb

## Canonical location

| Surface | Node | Context |
|---|---|---|
| Desktop | `1:2301`–`1:2309` inside `1:2279` «3- Услуги» | After institutional body copy, before who-we-treat frame |
| Mobile | Embedded in `1:5569` institutional band | Same semantic order |

**Canonical Y band (desktop):** within institutional frame cumulative Y 905–2036 (frame height 1131).

## Current location

| Metric | Value |
|---|---|
| DOM order | 8 — after `#o-centre-mid-cta`, before `#our-home` |
| Rendered Y | 4795px (1437 viewport capture) |
| Partial | `founder-quote.html` + `founder-quote--variant-b` |

## Base component status

**`BASE_COMPONENT_CORRECT`** — CF-004 partial, operator polish authority `472be1ab`; attribution and portrait match Figma nodes `1:2308`/`1:2309`.

## Page composition status

| Check | Status |
|---|---|
| Placement | **`PLACEMENT_WRONG`** |
| Context decoration | **`CONTEXT_DECORATION_MISSING`** — no institutional band wrapper |
| Spacing rhythm | **`CONTEXT_SPACING_WRONG`** — isolated between CTAs |

## Surrounding regions (canonical vs current)

| Canonical predecessor | Canonical successor | Current predecessor | Current successor |
|---|---|---|---|
| Institutional body | Who-we-treat (`1:2310`) | Mid program CTA | Infrastructure narrative |

## Correction strategy

1. **Keep** `src/partials/sections/founder-quote.html` unchanged.
2. **Move** include to immediately follow institutional narrative (inside page composition context).
3. **Optional** page-scoped wrapper class for institutional+founder visual grouping (not shared base rewrite).
4. **Do not** expand CF-004 globally.

**Classification:** `MOVE_BEFORE` + `REUSE_EXISTING_COMPONENT_AT_NEW_POSITION`
