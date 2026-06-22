# FP-0002 V6 JPG SAFE UNKNOWN

## Global

- font-family for all text levels
- exact HEX for red accent and dark blue backgrounds (JPEG COLOR VARIANCE)
- hover/focus/active states
- accordion expanded content
- carousel/slider mechanics for reviews
- form field validation and submit endpoint
- video playback behavior
- mobile/tablet layout at 1024px and below
- whether sticky header is intended
- z-index stacking order
- semantic HTML mapping
- SVG vs raster for icons
- relationship between JPG content width 1138px and future CSS container 1220px

## Per-block boundary ambiguity

- BLOCK-001: boundary or internal column layout — MEDIUM confidence
- BLOCK-035: boundary or internal column layout — LOW confidence (y_end corrected to 16343)

## Grounding review (2026-06-22)

- Header/Hero exact Y split within SECTION-001 — SAFE UNKNOWN
- Whether CMP-004 and CMP-008 are identical component — SAFE UNKNOWN
- 1138px median content width vs full-width sections — SAFE UNKNOWN
- Header bar exact height (~174px estimated) — SAFE UNKNOWN
- BLOCK-027 prior contact-form role — **corrected** to BLOCK-033 in grounded map
