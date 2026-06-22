# Corvonero Pilot Source Inventory v1

**Pilot:** `p0-i-real-slice-v1`  
**Primary authority:** preserved clean Corvonero MIG/canonical corpus

## Source paths

| Layer | Path | Role |
|-------|------|------|
| Raw MIG Wordstat | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/wordstat/wordstat-pass-a-normalized.json` | Original normalized Wordstat Pass A |
| Source ledger | `projects/orca/projects/corvonero-direct-v2-clean-room/mig-source/mig-wordstat-source-ledger-v1.json` | Provenance, frequency, file/row refs |
| Normalized corpus | `projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-normalized-corpus-v1.json` | Deterministic normalization (2399 rows) |
| Canonical registry | `projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json` | Deduplicated phrases (2368 unique) |
| Authority manifest | `projects/orca/projects/corvonero-direct-v2-clean-room/authority/corvonero-direct-v2-source-authority-manifest-v1.json` | Source authority chain |

## Candidate record fields

| Field | Source |
|-------|--------|
| phrase | `phrase` / `original_phrase` |
| query ID | `phrase_id` / `ledger_row_id` |
| provenance | ledger `provenance`, `source_file`, `source_row` |
| frequency | `combined_frequency`, `original_frequency` |

## Forbidden legacy-label fields (NOT used as truth)

- `corvonero-commercial-eligibility-v1.json` → `decision`
- `corvonero-intent-screening-v1.json` → `provisional_class`
- `corvonero-phrase-to-service-map-v1.json` → service mappings
- Old `corvonero-yandex-direct/production` semantic exports

## Safe extraction

Selection reads **canonical phrase registry** + **MIG ledger** only. No semantic-core decision files consumed.
