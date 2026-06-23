#!/usr/bin/env node
/**
 * Wave 3.1D supplementary blind protected-strata live validation.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLocalSecrets, getSafeConfigSummary } from '../runtime/local-secret-loader.mjs';
import { createOpenAICompatibleAdapter } from '../adapters/openai-compatible-adapter.mjs';
import { runBlindPrimaryAssessment } from '../assessment/blind-assessment.mjs';
import { runIndependentReassessment, assessmentsAgree } from '../assessment/independent-reassessment.mjs';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';
import { applyHardRules } from '../../production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../production/assessors/assessor-contract.mjs';
import { computeD3Metrics } from '../evaluation/d3-quality-gates.mjs';
import { DEFAULT_CONTROLS } from '../controls/cost-rate-controls.mjs';
import { PROMPT_VERSION } from '../contracts/prompt-contract.mjs';

const ADJUDICATOR_VERSION = 'v1.1';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SUP = path.join(__dirname, '../supplementary');
const FIX = path.join(__dirname, '../fixtures');
const RUN_ID = `supplementary-pass-${Date.now()}`;
const OUT = path.join(__dirname, '../reports', RUN_ID);

const cost = { records_processed: 0, input_tokens: 0, output_tokens: 0, calculated_cost_usd: 0 };
const PRICING = { input_per_m: 0.15, output_per_m: 0.60 };

function loadJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }
function writeJson(name, data) {
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, name), JSON.stringify(data, null, 2));
}
function trackUsage(meta) {
  if (!meta?.usage) return;
  cost.input_tokens += meta.usage.prompt_tokens || 0;
  cost.output_tokens += meta.usage.completion_tokens || 0;
  cost.calculated_cost_usd = (cost.input_tokens / 1e6) * PRICING.input_per_m + (cost.output_tokens / 1e6) * PRICING.output_per_m;
}
function assertCap(controls) {
  if (cost.calculated_cost_usd > controls.costCapUsd) throw new Error('COST_CAP_EXCEEDED');
}

function mergeStratum(stratum) {
  const phrases = loadJson(path.join(SUP, 'strata', stratum, 'phrases-blind-v1.json'));
  const labels = loadJson(path.join(SUP, 'strata', stratum, 'gold-labels-sealed-v1.json'));
  const labelMap = new Map(labels.records.map((r) => [r.record_id, r]));
  return phrases.records.map((p) => {
    const l = labelMap.get(p.record_id);
    if (!l) throw new Error(`Missing label for ${p.record_id}`);
    return {
      ...p,
      expected_decision: l.expected_decision,
      expected_authority_class: l.expected_authority_class,
      expected_protected_intent_class: l.expected_protected_intent_class,
      gold_authority_basis: l.gold_authority_basis,
    };
  });
}

async function evaluateRecord(record, context, adapter, controls) {
  const phrase = {
    phrase_id: record.phrase_id,
    raw_query: record.raw_query,
    normalized_query: record.normalized_query,
    region: record.region,
  };
  assertCap(controls);
  const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
  if (!primary.ok) return { record_id: record.record_id, error: primary.blocker, stratum: record.stratum };
  trackUsage(primary.output?.model_metadata);
  const det = assessDeterministic(createAssessorContext(phrase, context));
  const hardRules = applyHardRules(phrase, det);
  const secondary = await runIndependentReassessment({
    phrase, ...context, primaryAdapter: adapter, secondaryAdapter: adapter,
    hardRuleEvidence: hardRules, primaryDecision: undefined, primaryRationale: undefined, expectedLabel: undefined,
  });
  if (secondary.ok) trackUsage(secondary.output?.model_metadata);
  const adj = adjudicateSemanticIntent({
    assessmentA: primary.output,
    assessmentB: secondary.ok ? secondary.output : null,
    hardRuleEvidence: hardRules,
    serviceRegistry: context.serviceRegistry,
  });
  cost.records_processed++;
  return {
    record_id: record.record_id,
    raw_query: record.raw_query,
    stratum: record.protected_class,
    family: record.family,
    contrast_positive: record.contrast_positive,
    expected_decision: record.expected_decision,
    expected_authority_class: record.expected_authority_class,
    final_decision: adj.final_decision,
    primary_decision: primary.output.decision,
    secondary_decision: secondary.output?.decision,
    confidence: adj.confidence,
    assessor_agreement: secondary.ok ? assessmentsAgree(primary.output, secondary.output) : false,
    adjudicator_overturn: primary.output.decision !== adj.final_decision,
    human_review_required: adj.human_review_required,
  };
}

function stratumMetrics(results, stratum) {
  const subset = results.filter((r) => r.stratum === stratum && r.expected_authority_class === 'gold');
  const protectedOnly = subset.filter((r) => r.expected_decision === 'REJECT');
  const falseAccepts = protectedOnly.filter((r) => r.final_decision === 'ACCEPT');
  const contrast = subset.filter((r) => r.contrast_positive);
  const falseRejects = contrast.filter((r) => r.expected_decision === 'ACCEPT' && r.final_decision === 'REJECT');
  return {
    total_gold: subset.length,
    accept: subset.filter((r) => r.final_decision === 'ACCEPT').length,
    reject: subset.filter((r) => r.final_decision === 'REJECT').length,
    abstain: subset.filter((r) => r.final_decision === 'ABSTAIN').length,
    false_accept_on_protected_negatives: falseAccepts.length,
    false_positive_rate: protectedOnly.length ? falseAccepts.length / protectedOnly.length : null,
    false_reject_contrast_positives: falseRejects.length,
    assessor_agreement: subset.length ? subset.filter((r) => r.assessor_agreement).length / subset.length : null,
    adjudicator_overturns: subset.filter((r) => r.adjudicator_overturn).length,
    gate_pass: protectedOnly.length ? (falseAccepts.length / protectedOnly.length) <= 0.01 : null,
  };
}

async function main() {
  loadLocalSecrets();
  const controls = DEFAULT_CONTROLS;
  const adapter = createOpenAICompatibleAdapter();
  if (!adapter) throw new Error('ADAPTER_UNAVAILABLE');
  const context = {
    businessScope: loadJson(path.join(FIX, 'business-scope-eval-v1.json')),
    serviceRegistry: loadJson(path.join(FIX, 'service-registry-eval-v1.json')),
    taxonomy: {},
    commercialPolicy: { version: 'v1' },
  };

  const productRecords = mergeStratum('protected_product');
  const infoRecords = mergeStratum('protected_informational');
  const all = [...productRecords, ...infoRecords];

  const results = [];
  for (const rec of all) {
    results.push(await evaluateRecord(rec, context, adapter, controls));
  }

  const productMetrics = stratumMetrics(results, 'protected_product');
  const infoMetrics = stratumMetrics(results, 'protected_informational');
  const d3 = computeD3Metrics(results);

  const closure = {
    product_stratum: productMetrics,
    informational_stratum: infoMetrics,
    combined_verdict: productMetrics.gate_pass && infoMetrics.gate_pass
      ? 'SUPPLEMENTARY_PROTECTED_STRATA_PASS'
      : 'WAVE 3.1 — QUALITY REPAIR REQUIRED',
    insufficient_gold: productMetrics.total_gold < 50 || infoMetrics.total_gold < 50
      ? 'INSUFFICIENT SUPPLEMENTARY GOLD SUPPORT'
      : null,
  };

  writeJson('supplementary-run-manifest-v1.json', {
    run_id: RUN_ID,
    supplementary_blind_validation: true,
    assessor_label_access: false,
    prompt_version: PROMPT_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    provider: process.env.ORCA_SEMANTIC_PROVIDER,
    model: process.env.ORCA_SEMANTIC_MODEL,
    secret_summary: getSafeConfigSummary(),
    record_count: results.length,
  });
  writeJson('supplementary-results-v1.json', results);
  writeJson('supplementary-product-metrics-v1.json', productMetrics);
  writeJson('supplementary-informational-metrics-v1.json', infoMetrics);
  writeJson('supplementary-d3-metrics-v1.json', d3);
  writeJson('supplementary-closure-v1.json', closure);
  writeJson('cost-gate-v1.json', { ...cost, cap: controls.costCapUsd });

  console.log(JSON.stringify({ run_id: RUN_ID, closure: closure.combined_verdict, cost_usd: cost.calculated_cost_usd, out: OUT }, null, 2));
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
