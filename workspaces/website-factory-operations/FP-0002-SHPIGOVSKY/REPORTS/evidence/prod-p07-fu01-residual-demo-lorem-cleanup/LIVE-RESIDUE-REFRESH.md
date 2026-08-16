# PROD-P07-FU01 — Live residue refresh (read-only)

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Captures:** `live-recheck-*.html`, `live-recheck-html-summary.json`

Live FE does **not** contradict the blocked-wave hub/signs/program findings. FAQ live state **does** contradict the prior “FAQ still Lorem” note: current alcohol FAQ answers are real Russian editorial, not Lorem/technical filler.

## `/uslugi/`

| Check | Result |
|-------|--------|
| Visible `DEMO —` | **0** |
| Visible Lorem in `.services-category-section-v2__service-text` | **9 / 13** child cards |
| Real short descriptions preserved | **4 / 13** |

| Slug | Class | Owner (live) |
|------|-------|----------------|
| `lechenie-alkogolnoy-zavisimosti` | REAL | ACF and/or V9 real map |
| `lechenie-narkoticheskoy-zavisimosti` | REAL | ACF and/or V9 real map |
| `lechenie-povedencheskoy-zavisimosti` | REAL | ACF and/or V9 real map |
| `profilakticheskiy-analiz` | REAL | **ACF wins** (V9 map still had DEMO string; not rendered) |
| `depressiya` | LOREM | V9 `$demo_lorem` and/or ACF Lorem (same slot) |
| `ptsr` | LOREM | V9 `$demo_lorem` and/or ACF Lorem |
| `emotsionalnoe-vygoranie` | LOREM | renamed slug; V9 key was `emocionalnoe-vygoranie` — ACF Lorem is the likely live owner |
| `trevozhnye-rasstroystva` | LOREM | V9 `$demo_lorem` and/or ACF Lorem |
| `rasstroystva-sna` | LOREM | V9 `$demo_lorem` and/or ACF Lorem |
| `travma` | LOREM | V9 `$demo_lorem` and/or ACF Lorem |
| `anoreksiya` | LOREM | V9 `$demo_lorem` and/or ACF Lorem |
| `buliniya` | LOREM | renamed slug; V9 key was `nervnaya-bulimiya` — ACF Lorem is the likely live owner |
| `kompulsivnoe-pereedanie` | LOREM | V9 `$demo_lorem` and/or ACF Lorem |

Historical DB `DEMO —` rows from the P07 probe were **not** visible on this hub. They remain classified as historical/non-rendered unless a later DB SELECT proves a live owner. **No mass-delete.**

## Alcohol leaf

Route: `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`

| Surface | Live class | Owner |
|---------|------------|--------|
| Signs items (9) | REAL | `service_general_signs_*` and/or V9 items (real RU) |
| Signs editorial | LOREM | V9 `editorial` and/or ACF `service_general_signs_editorial` |
| Program heading | REAL | default / ACF heading |
| Program lead + intros | LOREM | `shpigovsky_get_v9_alcohol_leaf_program_demo_copy()` and/or ACF program fields |
| FAQ 10 Q/A | REAL | ACF `service_general_faq_items` (V9 Lorem FAQ is **not** the live owner) |
| Guest Visit CTA | present | unchanged |
| Fancybox hint | present | unchanged |

## Smoke

All HTTP 200: `/uslugi/zavisimosti/`, `/o-centre/programma-lecheniya/`, `/o-centre/`, `/`, `/kontakty/`. No approved-class Lorem on those routes (home still has out-of-scope `demo-pagination-article-*` slugs).
