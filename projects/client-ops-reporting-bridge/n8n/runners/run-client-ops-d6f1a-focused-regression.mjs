/**
 * Phase 1B-D6F1A focused Node regression: selectCandidates + import condition + gallery payloads.
 */
import assert from 'node:assert/strict';
import { selectCandidates } from './lib/client-ops-d6d-artifact.mjs';
import {
  classifyImportReport,
  offersFilesPresent,
  REPORT_CLASS,
} from './lib/client-ops-d6d-import-condition.mjs';
import { DELIVERY_ELIGIBILITY } from './lib/client-ops-d6d-constants.mjs';

function cand(partial) {
  return {
    ok: true,
    run_id: partial.run_id,
    observed_at: partial.observed_at,
    delivery_eligibility: partial.delivery_eligibility || DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    event_id: partial.event_id || partial.run_id,
    artifact_fingerprint: 'x',
    source_status: partial.source_status || 'ATTENTION',
  };
}

// T2 / daily: stale evaluated oldest must not block fresh newer
{
  const cursor = {
    evaluated_runs: {
      '2026-08-01_12-30-02': {
        delivery_decision: 'NO_SEND',
        result_class: 'STALE_REVIEW_REQUIRED',
      },
    },
  };
  const list = [
    cand({
      run_id: '2026-08-01_12-30-02',
      observed_at: '2026-08-01T05:30:34Z',
      delivery_eligibility: DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED,
    }),
    cand({
      run_id: '2026-08-06_13-04-53',
      observed_at: '2026-08-06T06:05:25Z',
      delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    }),
  ];
  const selected = selectCandidates(list, { maxCandidatesPerRun: 1, cursor });
  assert.equal(selected.length, 1);
  assert.equal(selected[0].run_id, '2026-08-06_13-04-53');
}

// Prefer fresh over older stale pending
{
  const selected = selectCandidates(
    [
      cand({
        run_id: 'old',
        observed_at: '2026-08-02T05:30:00Z',
        delivery_eligibility: DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED,
      }),
      cand({
        run_id: 'fresh',
        observed_at: '2026-08-06T06:05:25Z',
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      }),
    ],
    { maxCandidatesPerRun: 1, cursor: { evaluated_runs: {} } },
  );
  assert.equal(selected[0].run_id, 'fresh');
}

// T3 missing offers
{
  const r = classifyImportReport({
    fresh_import_confirmed: true,
    catalog_input_files: ['import0_1.xml'],
    offers_input_files: [],
    catalog_phase_ok: true,
    offers_phase_ok: true,
    offers_processed_count: 0,
  });
  assert.equal(r.report_class, REPORT_CLASS.CATALOG_SUCCESS_OFFERS_INPUT_MISSING);
  assert.equal(r.severity, 'ATTENTION');
  assert.equal(offersFilesPresent(['offer.xml']), false);
  assert.equal(offersFilesPresent(['offers0_1.xml']), true);
}

// T4 no fresh import
{
  const r = classifyImportReport({ fresh_import_confirmed: false });
  assert.equal(r.report_class, REPORT_CLASS.NO_FRESH_IMPORT);
  assert.equal(r.severity, 'ATTENTION');
}

// T5 catalog alone not full success
{
  const r = classifyImportReport({
    fresh_import_confirmed: true,
    catalog_input_files: ['import0_1.xml'],
    offers_input_files: [],
    catalog_phase_ok: true,
    offers_phase_ok: true,
    offers_processed_count: 0,
  });
  assert.notEqual(r.report_class, REPORT_CLASS.FULL_SUCCESS);
}

console.log(
  JSON.stringify({
    token: 'D6F1A_NODE_FOCUSED_REGRESSION_PASS',
    cases: ['select_skips_stale', 'prefer_fresh', 'missing_offers', 'no_fresh', 'catalog_alone'],
  }),
);
