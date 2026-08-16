# PROD-P07-FU01-CONT2 — Hub / alcohol before→after

Captures: `cont2-before-uslugi.html`, `cont2-before-alcohol.html`, `cont2-after-*.html`, `cont2-acceptance.json`.

## `/uslugi/`

| Metric | Before | After |
|--------|--------|-------|
| Visible Lorem short descriptions (card scope) | **9** | **0** |
| Visible `DEMO —` | **0** | **0** |
| REAL four-card copy | 4 | **4 preserved** |
| Card order | 13 slugs | **unchanged** |
| Titles / URLs | present | **remain** |
| Category gallery images | 5 | **5** |
| Empty `.…__service-text` `<p>` | 13 text nodes (9 Lorem) | **4** (REAL only; empty omitted) |
| HTTP | 200 | 200 |
| PHP warnings/notices | none | **none** |

The four REAL cards remain: alcohol / narcotic / behavioral / preventive analysis.

## Alcohol leaf

| Surface | Before | After |
|---------|--------|-------|
| Signs items | 9 REAL | **9 REAL** |
| Signs editorial | LOREM | **OMITTED** (no invented clinical copy) |
| Program heading + 4 cards | present | **preserved** |
| Program lead/intros | LOREM | **OMITTED** (existing `$use_emergency` did not fire because heading is non-empty) |
| FAQ | 10 REAL ACF | **10 REAL ACF preserved** |
| Guest Visit CTA | present | **present** (`Запишитесь на гостевой визит`) |
| Fancybox | present | **present** (`data-fancybox="comfort"`) |
| Page Lorem ipsum | present (editorial/program) | **0** |
| HTTP | 200 | 200 |

Fabricated clinical content: **NO**.
