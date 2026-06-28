# FP-0002 V8 O-Centre Founder Quote Decision v1

**Gap:** OC-G10 / OC-B09 / BLK-022
**Date:** 2026-06-29

## Present in composition

**Yes** — founder quote band is part of canonical O-Centre desktop/mobile composition.

| Surface | Node / frame | Notes |
|---|---|---|
| Desktop | `1:2301`–`1:2309` inside `1:2279` «3- Услуги» | Visible layout + photo + attribution |
| Mobile | `1:5569` institutional band | Same attribution pattern |

## Existing canonical component

| Item | Value |
|---|---|
| Partial | `src/partials/sections/founder-quote.html` (CF-004) |
| Operator authority | Manual polish checkpoint `472be1ab` |
| Block inventory | BLK-022 on PG-005 (`FP-0002-BLOCK-INVENTORY-v1.md` lines 84, 295) |

## Visible confirmed content (Figma)

| Field | Node | Text | Status |
|---|---|---|---|
| Quote body | `1:2301` | Lorem ipsum… | **PLACEHOLDER — not content** |
| Name | `1:2308` | Сергей Юрьевич Шпиговский | CONFIRMED |
| Role | `1:2309` | Основатель центра. Аддиктолог, интервенционист | CONFIRMED |

## Placeholder content

Figma quote body (`1:2301`, mobile mirror `1:5593`) is Lorem ipsum. **Must not** be implemented as page copy.

## Candidate reuse source

| Source | Authority | Content |
|---|---|---|
| `founder-quote.html` | CF-004 operator-approved V8 partial | Four paragraphs + closing quoted goal (see identity check) |
| `_fig_full_build_extract.json` (Home frame in Spig_v1.2) | Supporting Spig_v1.2 text export | Same quote body as V8 partial (punctuation variants only) |

## Identity result

Attribution/role: **exact match** between Figma and V8 partial.
Quote body: Figma Lorem ≠ V8 partial; V8 partial **matches** Spig_v1.2 Home export (normalized). See `data/FP-0002-V8-OCENTRE-CONTENT-IDENTITY-CHECK.json`.

## Classification

**`DIRECT_REUSE_SAME_CONTENT`**

Rationale:

1. BLK-022 is explicitly assigned to PG-005 in canonical block inventory.
2. CF-004 `founder-quote.html` is operator-approved site-wide expert opinion content with matching attribution.
3. O-Centre Figma confirms block presence and attribution; Lorem body is unresolved designer placeholder, not a competing content source.
4. Visual similarity alone would be insufficient; here inventory + shared block ID + operator-approved partial supply cross-page intent.

## Operator decision required

**No** — reuse is evidence-backed via BLK-022 on PG-005 and CF-004 canonical partial.

## Status

**RESOLVED_BY_CONFIRMED_REUSE**
