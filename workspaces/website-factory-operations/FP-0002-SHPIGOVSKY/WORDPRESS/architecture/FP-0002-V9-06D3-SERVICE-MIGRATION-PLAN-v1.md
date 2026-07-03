# FP-0002 V9-06D.3 Service Migration Plan v1

**Phase:** V9-06D.3 — PLANNING ONLY
**Services:** 15

## Wave guidance

### WAVE_1_VISUAL_MINIMUM

Parents + alcohol special: layout variant + hero lead (+ alcohol intro/signs minimal).

### WAVE_2_SERVICE_CONTENT

All remaining services: structured sections, FAQ, relationships as available from V9.

### Placeholder strategy

Placeholder services keep `service_layout_variant=placeholder` and minimal notice text only.

## Service matrix summary

| Registry | ID | Path | Layout | Wave | Risk |
|---|---:|---|---|---|---|
| SVC-ZAVISIMOSTI | 73 | /uslugi/zavisimosti/ | subdivision | WAVE_1_VISUAL_MINIMUM | MEDIUM |
| SVC-ALKOGOL | 74 | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | alcohol_special | WAVE_1_VISUAL_MINIMUM | MEDIUM |
| SVC-PROFILAKTIKA | 75 | /uslugi/zavisimosti/profilakticheskiy-analiz/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-SPECIALISTAM-ZAV | 76 | /uslugi/zavisimosti/specialistam/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-PSYCH | 77 | /uslugi/psihicheskoe-zdorovie/ | subdivision | WAVE_1_VISUAL_MINIMUM | LOW |
| SVC-DEPRESSIYA | 78 | /uslugi/psihicheskoe-zdorovie/depressiya/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-PTRS | 79 | /uslugi/psihicheskoe-zdorovie/ptrs/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-VYGORANIE | 80 | /uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-TREVOGA | 81 | /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-SON | 82 | /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-TRAVMA | 83 | /uslugi/psihicheskoe-zdorovie/travma/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-RPP | 84 | /uslugi/rasstroystva-pischevogo-povedeniya/ | subdivision | WAVE_1_VISUAL_MINIMUM | LOW |
| SVC-ANOREKSIYA | 85 | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-BULIMIYA | 86 | /uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |
| SVC-KOMPULSIV | 87 | /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | placeholder | WAVE_2_SERVICE_CONTENT | LOW |

## ACF groups (all services)

- `group_fp02_service_layout_hero`
- `group_fp02_service_structured_sections`
- `group_fp02_service_faq`
- `group_fp02_service_relationships`

## Current state

All 15 Services are skeleton-complete with registry meta; ACF content fields empty.

## Result

15_MAPPED — planning only.
