# REPORT — Multi-campaign phrase-slot release gate fix

**Date:** 2026-06-30  
**Scope:** Shared `commander-transport` release gate + Corvonero V2.6.2 restore

## False PASS mechanism

`release-gate.mjs` validated per-file XLSX contract checks (E9 blank, organization, URLs, contamination) but **did not** compare frozen `FINAL-GROUP-PLAN` phrase slots to summed deployable keyword rows across all campaigns. The V2.6.1 gate JSON recorded `926` authority vs `924` artifact as a **note only** and still set `OPERATOR_IMPORT_READY: true`.

## Missing gate assertion

Package-level and per-campaign **row-level phrase-slot reconciliation**:

`authority_phrase_slots == artifact_phrase_slots` with `missing_slots == 0`, `unexpected_slots == 0`, `duplicate_slots == 0`.

## Code owner

| Component | Path |
|-----------|------|
| Release gate | `tools/commander-transport/src/release-gate.mjs` |
| Phrase-slot reconciler | `tools/commander-transport/src/phrase-slot-reconciler.mjs` |
| Phrase normalizer | `tools/commander-transport/src/phrase-normalizer.mjs` |
| Generation defect (Corvonero) | `pilots/corvonero/tools/execute-campaign-v2.6-final-consolidation-v1.py` (`build_phrase_allocation`) |

## New reconciliation contract

- **Deployable phrase slot** = one Commander keyword row (`Тексты` sheet, row ≥ 16, phrase column populated).
- **Authority source:** `FINAL-GROUP-PLAN` `phrase_list` entries expanded per campaign/mode/group.
- **Artifact source:** actual XLSX keyword rows in package manifest `xlsx_files`.
- **Slot key:** `campaign_id | mode | group_id | normalized_phrase`
- Gate fails on missing, unexpected, duplicate, per-campaign mismatch, or aggregate mismatch.

## New tests

File: `tools/commander-transport/tests/phrase-slot-reconciler.test.mjs`

| Scenario | Covered |
|----------|---------|
| 926 vs 924 aggregate mismatch | yes |
| One missing phrase | yes |
| Two missing across campaigns | yes |
| Extra artifact phrase | yes |
| Duplicate with equal total | yes |
| Wrong group | yes |
| Wrong mode | yes |
| Per-campaign mismatch, equal package total | yes |
| Exact multi-campaign match | yes |
| Gate fail on mismatch | yes |
| Gate pass on match | yes |

**Test totals:** 98 tests, 19 suites, 0 failed (was 86).

## Other potentially affected packages

Any multi-campaign Commander package validated only by per-file structural checks without group-plan row reconciliation (Triumph and future pilots using the same gate).

## Previous release-gate results

**Review required** for any prior `RELEASE_GATE_PASS` on multi-campaign packages where phrase-slot totals were noted but not enforced.

## Changed files (this task)

- `tools/commander-transport/src/phrase-slot-reconciler.mjs` (new)
- `tools/commander-transport/src/phrase-normalizer.mjs` (new)
- `tools/commander-transport/src/release-gate.mjs`
- `tools/commander-transport/src/release-gate-cli.mjs`
- `tools/commander-transport/tests/phrase-slot-reconciler.test.mjs` (new)
- `tools/commander-transport/tests/release-gate.test.mjs`
- `pilots/corvonero/tools/execute-campaign-v2.6-final-consolidation-v1.py`
- `pilots/corvonero/tools/execute-campaign-v2.6.2-phrase-slot-restore-v1.mjs` (new)
- Corvonero pilot artifacts and release state (see Corvonero report)

**Git:** not staged, not committed (per task).
