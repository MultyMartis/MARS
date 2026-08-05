# TEST DATA SEPARATION v1 — Phase 3F.2

## Detection mechanism (existing, unchanged)

`isProbableTest()` in `implementation/runtime-libs/pending-leads-lib.mjs` flags a row as test/synthetic when any of the following hold: `is_probable_test`/`probable_test` truthy flag, `__synthetic`/`synthetic_fixture`/`fixture_id` markers, `marker === 'SYNTHETIC_TEST'`, a `SYNTHETIC_TEST` or `PHASE_3*` phase marker in the name, `synthetic`/`synth_`/`синтетик`-style tokens in `lead_id`/`source`, or `test`/`синт`/`тест` tokens in the name, or `phase 3`/`sheets probe`/`стабилизац` tokens in name+summary+marker. This logic is not changed by Phase 3F.2; it is reused as-is.

## Current mixed-CLEAN state (previously reported, re-confirmed as still current)

| Bucket | Count |
|---|---|
| Business pending (test-excluded, default view) | **12** |
| Test pending (included only via the Admin-only `/pending_leads_test` variant) | **41** |

The volume of test/synthetic rows in CLEAN is large relative to real business volume and remains **mixed into the same tabs** as real leads — separation today is a **filter at read time** (`isProbableTest()`), not a physical split into separate tabs.

## Relationship to Клиент A

Клиент A's row was correctly classified `is_probable_test=false` — the detection logic is working correctly for this real lead; the concern documented here is about the **volume of pre-existing test rows**, not about any misclassification risk to the one real lead in scope for this phase.

## Status

| Item | Status |
|---|---|
| Detection logic correctness (read-time filter) | **CONFIRMED working** — reused from Phase 3E.2.2/3F.1, no regression |
| Physical separation of test rows out of `lead_clean_v2` | **NOT DONE** — filter-only today |
| Cleanup/removal of accumulated test rows | **PENDING OPERATOR** — see [TEST-CLEANUP-ACCEPTANCE-v1.md](TEST-CLEANUP-ACCEPTANCE-v1.md); no rows were deleted or moved as part of Phase 3F.2 |

*Related: [CURRENT-REAL-LEAD-SAFETY-v1.md](CURRENT-REAL-LEAD-SAFETY-v1.md), [TEST-CLEANUP-ACCEPTANCE-v1.md](TEST-CLEANUP-ACCEPTANCE-v1.md).*
