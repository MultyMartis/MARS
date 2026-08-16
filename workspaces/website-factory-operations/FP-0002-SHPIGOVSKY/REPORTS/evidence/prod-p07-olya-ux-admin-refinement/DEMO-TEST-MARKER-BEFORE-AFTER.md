# PROD-P07 — Demo/Test Marker Before/After Map

**Wave:** FP-0002 PROD-P07  
**Date:** 2026-08-14  

| Object | Field | Before | After | Classification |
|--------|-------|--------|-------|----------------|
| service `#73` | `section_program_footer_label` | `подробнее о программе ТЕСТ` | `подробнее о программе` | technical marker removed |
| service `#73` | `section_approach_cards` | count empty; orphan rows 1–3 with Lorem | count `3`; rows 0–2 production-safe RU texts | Admin/FE parity repair |
| service `#77` | `section_approach_cards` | serialized blob + Lorem | normal ACF repeater count `4` + safe texts | demo filler replaced |
| service `#84` | `section_approach_cards` | DEMO texts | normal ACF repeater count `4` + safe texts | demo filler replaced |
| service `#84` | `service_short_description` | `тест020 …` | prefix stripped | technical marker removed |
| page `#13` | `generic_page_reusable_blocks` | unset | `rehab_requirements` + `about_home` | selector enabled |
| service `#73` | `section_program_lead` / intro / nature Lorem fields | Lorem ipsum | production-safe / cleared empty-safe | technical demo cleanup |

## Reviewed but preserved / deferred

| Item | Reason |
|------|--------|
| Substring `тест` inside real Russian words | not a marker |
| Revisions (`#1336` etc. `ТЕСТ …`) | revision/history only — not mutated |
| Hub child `service_short_description` values still starting with `DEMO —` on some leaves | broader demo inventory; not part of exact Olya markers for this wave — **deferred** |
| Alcohol FAQ / signs Lorem on leaf `#74` | outside exact approach/CTA/program chrome scope — **deferred** residual |
| `cta_band_default_*` options still = «Остались вопросы?» | intentional generic CTA defaults; Guest Visit contexts no longer inherit them |

## Frontend acceptance (post-deploy)

| Route | Marker result |
|-------|---------------|
| `/uslugi/zavisimosti/` | `программе ТЕСТ` gone; approach cards visible with non-Lorem texts |
| `/o-centre/programma-lecheniya/` | reusable blocks render; no test markers |
| Home / Contacts | Guest Visit CTA intact |
