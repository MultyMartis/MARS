# Corvonero Direct V2 — Source Authority Manifest v1

**Status:** ACTIVE  
**Project:** `corvonero-direct-v2-clean-room`

## Clean-room rule

Запрещено использовать как источник семантических решений любые результаты старого pipeline Corvonero v1–v7.1.

Старые материалы — только доказательство дефектов, regression anti-patterns и техническая история.

## AUTHORITATIVE

| ID | Source | Paths |
|----|--------|-------|
| AUTH-01 | Operator business inputs | `intake/`; `workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md` |
| AUTH-02 | Original MIG session | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` |
| AUTH-03 | Universal ORCA contract | `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` |
| AUTH-04 | Triumph-derived laws | `projects/orca/knowledge/triumph-derived-orca-laws-v1.md` |

## EVIDENCE ONLY

- SERP captures
- Wordstat frequency (national semantic discovery)
- MIG research notes
- Source metadata

## HISTORICAL ANTI-PATTERN ONLY

- `projects/orca/projects/corvonero-yandex-direct/` — all v1–v7.1 production artefacts

## FORBIDDEN FOR SEMANTIC DECISIONS

- `production/direct-commander-production-dataset-v*.json`
- `production/final-keyword-registry-v*.json`
- `production/final-negative-registry-v*.json`
- `production/final-controlled-test-registry-v*.json`
- `production/semantic-*-v*.json`
- `production/repair/`
- `production/recovery/`
- Previous Commander and Review XLSX exports
- Previous exclusion, group, ad registries
- Validation outputs containing semantic decisions

## Provenance rule

Every semantic record must trace to an allowed source.
