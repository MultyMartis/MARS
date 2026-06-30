# REPORT — Corvonero V2.6 phrase-slot reconciliation

**Date:** 2026-06-30

## 926 vs 924 evidence

| Source | Phrase slots |
|--------|-------------:|
| V2.6 `FINAL-GROUP-PLAN` (deployable authority) | 926 |
| V2.6 `PHRASE-ALLOCATION` (generation input) | 924 |
| V2.6 / V2.6.1 XLSX keyword rows | 924 |

## Exact missing slots (V2.6.1)

| Campaign | Mode | Group | Phrase |
|----------|------|-------|--------|
| CA-02-LOCAL | LOCAL | ca-02-support-tech | программа 1с не работает |
| CA-02-REMOTE | REMOTE | ca-02-support-tech | программа 1с не работает |

Evidence: `CORVONERO-V2.6.1-MISSING-SLOTS.csv`, `CORVONERO-V2.6.1-PHRASE-SLOT-RECONCILIATION.csv`

## Root-cause classification

**GENERATION_DEFECT** (both slots)

- V2.6 `build_final_groups_v26` merged `ca-02-troubleshooting-not-working` → `ca-02-support-tech` via `V26_SINGLE_PHRASE_MERGE`, placing **программа 1с не работает** in group plan (926 slots).
- `build_phrase_allocation` resolved `infer_group_id_v26` → `ca-02-troubleshooting-not-working` and skipped records when `(campaign, group_id)` not in group index (924 allocation rows).
- XLSX generation faithfully emitted 924 rows.

Semantic authority KEEP decision for PHR-0447 unchanged. Not AUTHORITY_ACCOUNTING_DEFECT (926 group-plan total is correct). Not operator semantic contradiction.

## Selected fix path

**Path A — generation defect**

- Fixed `build_phrase_allocation` to apply `resolve_deployable_group_id()` / `V26_SINGLE_PHRASE_MERGE`.
- Created **V2.6.2** package `CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30` with 2 restored keyword rows only.
- V2.6.1 package preserved; gate v1 **INVALIDATED**, not deleted.

## Operator receipt

No amendment required: derived `phrase_slot_count: 926` matches corrected deployable authority. Semantic decisions unchanged (487 KEEP / 271 REJECT / 2 MOVE).

## Package version used

**V2.6.2** (`X:/AI MARS STORAGE/exports/corvonero/CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30`)

## Final gate command

```powershell
cd projects/mars-search-ppc-production/tools/commander-transport
$env:MARS_SKIP_VOLUME_CHECK='1'
node src/release-gate-cli.mjs --project corvonero `
  --package "X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30" `
  --authority "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json" `
  --receipt "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json" `
  --json
```

## Final gate output (summary)

- **status:** `RELEASE_GATE_PASS`
- **phrase_slot_reconciliation:** authority 926, artifact 926, delta 0
- **missing / unexpected / duplicate:** 0 / 0 / 0
- **XLSX validated:** 10/10

Full JSON: `CORVONERO-CAMPAIGN-V2.6.2-RELEASE-GATE-RESULT-v1.json`

## Release-state transition

| State | Before correction | After corrected PASS |
|-------|-------------------|---------------------|
| ARTIFACT_VALIDATED | false | true |
| OPERATOR_IMPORT_READY | false | true |
| Deployable package | V2.6.1 (invalidated gate) | V2.6.2 |
| COMMANDER_IMPORTED | false | false |

## Changed files

See systemic report. Key Corvonero artifacts:

- `CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json`
- `CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-CORRECTION-v1.json`
- `CORVONERO-CAMPAIGN-V2.6.1-PHRASE-SLOT-RECONCILIATION-v1.json` + CSVs
- `CORVONERO-CAMPAIGN-V2.6.2-GENERATION-v1.json`
- `CORVONERO-CAMPAIGN-V2.6.2-FORENSIC-VALIDATION-v1.json`
- `CORVONERO-CAMPAIGN-V2.6.2-RELEASE-GATE-RESULT-v1.json`

**Git:** not staged, not committed.
