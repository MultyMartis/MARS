# Home hero demo fallback source trace

## Root cause

Per-slide normal render path in `template-parts/home/hero.php` injected demo copy when ACF fields were empty:

`php
$hero_title = '' !== $slide['title'] ? $slide['title'] : 'Шпиговский дом';
$hero_text  = '' !== $slide['text'] ? $slide['text'] : 'Центр профилактики и&nbsp;лечения зависимостей';
`

Confirmed live pre-fix: slide 2 title `Центр реабилитации` with empty ACF text still rendered the demo tagline.

## Exact fix (V9-06E56-FU01)

- Render `.hero__tagline` only when text non-empty
- Render `.hero__title` only when title non-empty
- Emergency empty-slides shell keeps image only (no demo title/text)
- No ACF/DB changes; no Home reseed

## Validation

| Case | Result |
|------|--------|
| Slide 1 populated title+text | PASS — both present |
| Slide 2 title only, empty text | PASS — title only, no tagline element |
| Optional per-slide button | N/A — no per-slide button field (global CTA only) |
| Image+title only | PASS — slide 2 |

Demo string no longer injected for empty fields. Slide 1 still shows operator-saved `Центр профилактики…` from ACF (not fallback).
