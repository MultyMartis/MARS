# CORVONERO CAMPAIGN V2.6.1 — GENERATION HOTFIX v1

Generated: 2026-06-30T15:53:26.000Z

## Root cause
- Owner: `projects/mars-search-ppc-production/tools/commander-transport/src/commander-patcher-adapter.mjs`
- Template junk at E9: `-вакансии -работа -резюме -купить -ремонт -запчасти -эвакуатор -бесплатно -своими руками`
- `translateMetadataPatches` and `patchCampaignMetadataBlock` skip empty values
- No `clearCampaignNegativesMetadataCell` equivalent to organization clear
- V2.6 forensic validated metadata intent, not actual `Тексты!E9`

## Fix
- `clearCampaignNegativesMetadataCell` + `shouldClearEmbeddedCampaignNegatives`

## Scope
- Semantic authority unchanged from V2.6
- TXT negatives unchanged (copied from V2.6)
- XLSX regenerated with blank E9
