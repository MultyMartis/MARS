#!/usr/bin/env node
/**
 * Blind evaluation runner — Wave 3.1 D3 quality evaluation.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { runBlindPrimaryAssessment, buildBlindInputEvidence } from '../assessment/blind-assessment.mjs';
import { runIndependentReassessment, assessmentsAgree } from '../assessment/independent-reassessment.mjs';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';
import { createOpenAICompatibleAdapter, createMockLiveAdapter } from '../adapters/openai-compatible-adapter.mjs';
import { inspectProviderInventory } from '../adapters/provider-inventory.mjs';
import { applyHardRules } from '../../production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../production/assessors/assessor-contract.mjs';
import { computeD3Metrics } from '../evaluation/d3-quality-gates.mjs';
import { extractErrorFamilies, runBoundedCalibration } from '../evaluation/error-analysis.mjs';
import { assertCostCap, getRuntimeControls } from '../controls/cost-rate-controls.mjs';
import { loadLocalSecrets } from '../runtime/local-secret-loader.mjs';
import { PROMPT_VERSION } from '../contracts/prompt-contract.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const REPORTS = path.join(__dirname, '../reports');

function loadJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }

function resolveAdapter(useLive) {
  const inventory = inspectProviderInventory();
  if (useLive && inventory.any_live_provider_configured) {
    return { adapter: createOpenAICompatibleAdapter(), mode: 'LIVE', inventory };
  }
  if (process.env.ORCA_EVAL_USE_MOCK === '1' || !inventory.any_live_provider_configured) {
    return { adapter: createMockLiveAdapter(), mode: 'MOCK_PIPELINE', inventory };
  }
  return { adapter: null, mode: 'BLOCKED', inventory };
}

async function evaluateRecord(record, context, adapter, secondaryAdapter) {
  const phrase = {
    phrase_id: record.phrase_id,
    raw_query: record.raw_query,
    normalized_query: record.normalized_query,
    region: record.region,
  };

  const blindEvidence = buildBlindInputEvidence({ forbiddenContext: {} });

  const primary = await runBlindPrimaryAssessment({
    phrase,
    ...context,
    adapter,
    forbiddenContext: {},
  });

  if (!primary.ok) return { record_id: record.record_id, error: primary.blocker, ...record };

  const deterministicCtx = createAssessorContext(phrase, context);
  const det = assessDeterministic(deterministicCtx);
  const hardRules = applyHardRules(phrase, det);

  const secondary = await runIndependentReassessment({
    phrase,
    ...context,
    primaryAdapter: adapter,
    secondaryAdapter: secondaryAdapter || adapter,
    hardRuleEvidence: hardRules,
    primaryDecision: undefined,
    primaryRationale: undefined,
    expectedLabel: undefined,
  });

  const assessmentB = secondary.ok ? secondary.output : null;
  const adjudication = adjudicateSemanticIntent({
    assessmentA: primary.output,
    assessmentB: assessmentB,
    hardRuleEvidence: hardRules,
    invariantResults: [],
    businessScope: context.businessScope,
    serviceRegistry: context.serviceRegistry,
  });

  return {
    record_id: record.record_id,
    raw_query: record.raw_query,
    stratum: record.stratum,
    expected_decision: record.expected_decision,
    expected_authority_class: record.expected_authority_class,
    final_decision: adjudication.final_decision,
    primary_decision: primary.output.decision,
    secondary_decision: assessmentB?.decision,
    primary_intent: primary.output.primary_intent,
    confidence: adjudication.confidence,
    human_review_required: adjudication.human_review_required,
    assessor_agreement: assessmentB ? assessmentsAgree(primary.output, assessmentB) : false,
    adjudicator_overturn: primary.output.decision !== adjudication.final_decision,
    deterministic_decision: det.decision,
    p0i_equivalent: det.decision,
    blind_evidence: blindEvidence,
    independence_level: secondary.independence_level,
    rationale: primary.output.rationale,
  };
}

async function runEvaluation(corpusPath, outSubdir, label) {
  const corpus = loadJson(corpusPath);
  const businessScope = loadJson(path.join(FIX, 'business-scope-eval-v1.json'));
  const serviceRegistry = loadJson(path.join(FIX, 'service-registry-eval-v1.json'));
  const context = { businessScope, serviceRegistry, taxonomy: {}, commercialPolicy: { version: 'v1' } };

  const { adapter, mode, inventory } = resolveAdapter(process.env.ORCA_EVAL_LIVE === '1');
  const costCheck = assertCostCap(corpus.records.length, CONTROLS);
  if (!costCheck.ok && mode === 'LIVE') {
    return { label, blocked: costCheck.blocker, mode };
  }

  if (mode === 'BLOCKED') {
    return { label, blocked: 'BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE', mode, inventory };
  }

  const results = [];
  for (const record of corpus.records) {
    results.push(await evaluateRecord(record, context, adapter, adapter));
  }

  const metrics = computeD3Metrics(results);
  const errors = extractErrorFamilies(results);
  const calibration = runBoundedCalibration(results, 3);

  const p0iComparison = {
    unchanged: results.filter((r) => r.deterministic_decision === r.final_decision).length,
    det_accept_model_reject: results.filter((r) => r.deterministic_decision === 'ACCEPT' && r.final_decision === 'REJECT').length,
    det_accept_model_abstain: results.filter((r) => r.deterministic_decision === 'ACCEPT' && r.final_decision === 'ABSTAIN').length,
    det_reject_model_accept: results.filter((r) => r.deterministic_decision === 'REJECT' && r.final_decision === 'ACCEPT').length,
  };

  const outDir = path.join(REPORTS, outSubdir);
  fs.mkdirSync(outDir, { recursive: true });

  const manifest = {
    run_id: outSubdir,
    label,
    mode,
    prompt_version: PROMPT_VERSION,
    model_provider: inventory.recommended_primary || mode,
    record_count: results.length,
    cost_estimate: costCheck.estimate,
    started_at: new Date().toISOString(),
    blocked: null,
  };

  fs.writeFileSync(path.join(outDir, 'run-manifest-v1.json'), JSON.stringify(manifest, null, 2));
  fs.writeFileSync(path.join(outDir, 'evaluation-results-v1.json'), JSON.stringify(results, null, 2));
  fs.writeFileSync(path.join(outDir, 'd3-metrics-v1.json'), JSON.stringify(metrics, null, 2));
  fs.writeFileSync(path.join(outDir, 'error-families-v1.json'), JSON.stringify(errors, null, 2));
  fs.writeFileSync(path.join(outDir, 'calibration-iterations-v1.json'), JSON.stringify(calibration, null, 2));
  fs.writeFileSync(path.join(outDir, 'p0i-comparison-v1.json'), JSON.stringify(p0iComparison, null, 2));

  return { label, mode, metrics, results, errors, calibration, p0iComparison, outDir };
}

async function main() {
  loadLocalSecrets();
  const CONTROLS = getRuntimeControls();
  fs.mkdirSync(FIX, { recursive: true });
  if (!fs.existsSync(path.join(FIX, 'evaluation-corpus-v1.json'))) {
    await import('../evaluation/build-evaluation-corpus.mjs');
  }

  console.log('Running calibration corpus evaluation...');
  const cal = await runEvaluation(path.join(FIX, 'evaluation-corpus-v1.json'), `blind-eval-${Date.now()}`, 'calibration');

  console.log('Running holdout evaluation (single pass, no tuning)...');
  const hold = await runEvaluation(path.join(FIX, 'evaluation-holdout-v1.json'), `holdout-eval-${Date.now()}`, 'holdout');

  const humanReview = buildHumanReviewPackage(cal.results || [], cal.errors || {});
  fs.writeFileSync(path.join(cal.outDir || REPORTS, 'human-review-package-v1.json'), JSON.stringify(humanReview, null, 2));

  console.log(JSON.stringify({
    calibration_mode: cal.mode,
    calibration_blocked: cal.blocked || null,
    calibration_gates_pass: cal.metrics?.gates?.commercial_precision_gold_high_confidence?.pass,
    holdout_mode: hold.mode,
    holdout_gates_pass: hold.metrics?.gates?.commercial_precision_gold_high_confidence?.pass,
    human_review_items: humanReview.items.length,
  }, null, 2));
}

function buildHumanReviewPackage(results, errorFamilies) {
  const items = [];
  const highRiskAccept = results.filter((r) => r.expected_decision === 'REJECT' && r.final_decision === 'ACCEPT').slice(0, 5);
  const highValueReject = results.filter((r) => r.expected_decision === 'ACCEPT' && r.final_decision === 'REJECT').slice(0, 5);
  const policyConflicts = results.filter((r) => r.human_review_required && r.stratum?.includes('mixed')).slice(0, 3);

  for (const r of highRiskAccept) items.push({ type: 'HIGH_RISK_FALSE_ACCEPT', record_id: r.record_id, query: r.raw_query, operator_field: '' });
  for (const r of highValueReject) items.push({ type: 'HIGH_VALUE_FALSE_REJECT', record_id: r.record_id, query: r.raw_query, operator_field: '' });
  for (const r of policyConflicts) items.push({ type: 'POLICY_CONFLICT', record_id: r.record_id, query: r.raw_query, operator_field: '' });

  for (const [family, data] of Object.entries(errorFamilies)) {
    if (data.count > 0 && data.examples[0]) {
      items.push({ type: 'ERROR_FAMILY_EXAMPLE', family, example: data.examples[0], operator_field: '' });
    }
  }

  const auditSample = results.filter((_, i) => i % 50 === 0).slice(0, 3);
  for (const r of auditSample) items.push({ type: 'BOUNDED_RANDOM_AUDIT', record_id: r.record_id, query: r.raw_query, operator_field: '' });

  return {
    package_id: 'wave31-human-review-v1',
    target_size: items.length,
    justification: 'Conflict-focused samples only — not full corpus labeling',
    items,
  };
}

main().catch((e) => { console.error(e); process.exit(1); });
