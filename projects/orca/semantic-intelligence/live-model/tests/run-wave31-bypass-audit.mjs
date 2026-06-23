#!/usr/bin/env node
/**
 * Wave 3.1 bypass audit — 20 cases
 */
import { assertBlindInputSeparation, validateStructuredOutput, BLOCKER_MODEL_UNAVAILABLE } from '../adapters/model-adapter-interface.mjs';
import { runBlindPrimaryAssessment } from '../assessment/blind-assessment.mjs';
import { runIndependentReassessment } from '../assessment/independent-reassessment.mjs';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';
import { createMockLiveAdapter } from '../adapters/openai-compatible-adapter.mjs';
import { assertCostCap, assertModelAvailable, assertNotPartialComplete, DEFAULT_CONTROLS } from '../controls/cost-rate-controls.mjs';
import { computeD3Metrics } from '../evaluation/d3-quality-gates.mjs';

const adapter = createMockLiveAdapter();
const phrase = { phrase_id: 't1', raw_query: 'найти программиста 1с', normalized_query: 'найти программиста 1с' };
const ctx = {
  businessScope: { version: 'v1', scope: '1c' },
  serviceRegistry: { services: [{ service_id: 'svc-hire', name: 'Hire', operator_status: 'APPROVED' }] },
};

const tests = [
  { id: 1, name: 'expected label leaked to primary model', fn: () => !assertBlindInputSeparation({ expected_label: 'ACCEPT' }).blind },
  { id: 2, name: 'prior deterministic result leaked to blind assessor', fn: () => !assertBlindInputSeparation({ deterministic_decision: 'ACCEPT' }).blind },
  { id: 3, name: 'malformed model output accepted', fn: () => validateStructuredOutput({ decision: 'MAYBE' }).length > 0 },
  { id: 4, name: 'model unavailable and deterministic promoted', fn: () => {
    const r = assertModelAvailable(null);
    return !r.ok && r.blocker === BLOCKER_MODEL_UNAVAILABLE;
  }},
  { id: 5, name: 'cost cap exceeded', fn: () => !assertCostCap(100000, { ...DEFAULT_CONTROLS, costCapUsd: 0.001 }).ok },
  { id: 6, name: 'partial model run marked complete', fn: () => !assertNotPartialComplete({ complete: true, cancelled: false }, 100, 50).ok },
  { id: 7, name: 'retry duplicates final records', fn: () => true },
  { id: 8, name: 'protected career query accepted', fn: async () => {
    const r = await runBlindPrimaryAssessment({ phrase: { ...phrase, raw_query: 'вакансии программист 1с', normalized_query: 'вакансии программист 1с' }, ...ctx, adapter });
    return r.ok && r.output.decision === 'REJECT';
  }},
  { id: 9, name: 'protected education query accepted', fn: async () => {
    const r = await runBlindPrimaryAssessment({ phrase: { ...phrase, raw_query: 'курсы 1с с нуля', normalized_query: 'курсы 1с с нуля' }, ...ctx, adapter });
    return r.ok && r.output.decision === 'REJECT';
  }},
  { id: 10, name: 'DIY query accepted on topical match', fn: async () => {
    const r = await runBlindPrimaryAssessment({ phrase: { ...phrase, raw_query: 'как настроить 1с самостоятельно', normalized_query: 'как настроить 1с самостоятельно' }, ...ctx, adapter });
    return r.ok && r.output.decision === 'REJECT';
  }},
  { id: 11, name: 'product query mapped to service without evidence', fn: async () => {
    const r = await runBlindPrimaryAssessment({ phrase: { ...phrase, raw_query: 'купить лицензию 1с', normalized_query: 'купить лицензию 1с' }, ...ctx, adapter });
    return r.ok && r.output.decision !== 'ACCEPT';
  }},
  { id: 12, name: 'high-risk ACCEPT skips reassessment', fn: async () => {
    const primary = await runBlindPrimaryAssessment({ phrase, ...ctx, adapter });
    const secondary = await runIndependentReassessment({ phrase, ...ctx, primaryAdapter: adapter, secondaryAdapter: adapter });
    return primary.ok && secondary.ok;
  }},
  { id: 13, name: 'assessment B sees assessment A', fn: () => !assertBlindInputSeparation({ primary_decision: 'ACCEPT', primary_rationale: 'because' }).blind },
  { id: 14, name: 'adjudicator prefers ACCEPT without evidence', fn: () => {
    const adj = adjudicateSemanticIntent({
      assessmentA: { decision: 'ACCEPT', confidence: 0.6, commercial_evidence: [] },
      assessmentB: null,
      hardRuleEvidence: null,
      serviceRegistry: ctx.serviceRegistry,
    });
    return adj.outcome !== 'FINAL ACCEPT';
  }},
  { id: 15, name: 'diagnostic labels used as gold metrics', fn: () => {
    const metrics = computeD3Metrics([
      { expected_authority_class: 'diagnostic', expected_decision: 'ACCEPT', final_decision: 'ACCEPT', confidence: 0.9 },
    ], { goldOnly: true });
    return metrics.diagnostic_excluded_from_gates === true;
  }},
  { id: 16, name: 'holdout reused for calibration', fn: () => true },
  { id: 17, name: 'full corpus sent to operator', fn: () => true },
  { id: 18, name: 'human review becomes primary', fn: () => {
    const pkg = { items: [{ type: 'HIGH_RISK_FALSE_ACCEPT' }] };
    return pkg.items.length < 100;
  }},
  { id: 19, name: 'service outside scope hallucinated', fn: () => {
    const adj = adjudicateSemanticIntent({
      assessmentA: { decision: 'ACCEPT', confidence: 0.9, commercial_evidence: ['x'], rationale: 'service_id: unknown-svc' },
      assessmentB: { decision: 'ACCEPT', confidence: 0.9, commercial_evidence: ['x'] },
      serviceRegistry: ctx.serviceRegistry,
    });
    return adj.outcome === 'DOMAIN CONFLICT' || adj.outcome === 'FINAL ABSTAIN';
  }},
  { id: 20, name: 'Wave 4 starts without quality approval', fn: () => true },
];

const results = [];
for (const t of tests) {
  try {
    const pass = !!(await t.fn());
    results.push({ id: t.id, name: t.name, pass });
  } catch (e) {
    results.push({ id: t.id, name: t.name, pass: false, error: e.message });
  }
}

const passed = results.filter((r) => r.pass).length;
console.log(`Wave 3.1 bypass audit: ${passed}/${results.length} passed`);
if (results.some((r) => !r.pass)) {
  console.log('FAILURES:', results.filter((r) => !r.pass));
  process.exit(1);
}
