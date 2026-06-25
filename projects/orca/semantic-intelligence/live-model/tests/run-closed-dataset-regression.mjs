#!/usr/bin/env node
/**
 * Closed-dataset regression after Wave 3.1E product repair (not blind PASS).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLocalSecrets, getSafeConfigSummary } from '../runtime/local-secret-loader.mjs';
import { createOpenAICompatibleAdapter } from '../adapters/openai-compatible-adapter.mjs';
import { runBlindPrimaryAssessment } from '../assessment/blind-assessment.mjs';
import { runIndependentReassessment, assessmentsAgree } from '../assessment/independent-reassessment.mjs';
import { adjudicateSemanticIntent, ADJUDICATOR_VERSION } from '../adjudication/semantic-adjudicator.mjs';
import { applyHardRules } from '../../production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../production/assessors/assessor-contract.mjs';
import { PROMPT_VERSION } from '../contracts/prompt-contract.mjs';
import { DEFAULT_CONTROLS } from '../controls/cost-rate-controls.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SUP = path.join(__dirname, '../supplementary');
const FIX = path.join(__dirname, '../fixtures');
const RUN_ID = `closed-regression-${Date.now()}`;
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

function mergeStratum(stratum) {
  const phrases = loadJson(path.join(SUP, 'strata', stratum, 'phrases-blind-v1.json'));
  const labels = loadJson(path.join(SUP, 'strata', stratum, 'gold-labels-sealed-v1.json'));
  const labelMap = new Map(labels.records.map((r) => [r.record_id, r]));
  return phrases.records.map((p) => ({ ...p, ...labelMap.get(p.record_id) }));
}

async function evaluateRecord(record, context, adapter) {
  const phrase = { phrase_id: record.phrase_id, raw_query: record.raw_query, normalized_query: record.normalized_query, region: record.region };
  const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
  if (!primary.ok) return { record_id: record.record_id, error: primary.blocker };
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
    final_decision: adj.final_decision,
    primary_decision: primary.output.decision,
    secondary_decision: secondary.output?.decision,
    hard_rule_blocked: hardRules.blocked,
  };
}

async function main() {
  loadLocalSecrets();
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
  const minimalPairs = loadJson(path.join(SUP, 'regression/product-service-regression-v1.json')).minimal_pairs;
  const all = [...productRecords, ...infoRecords, ...minimalPairs.map((m) => ({
    record_id: m.record_id,
    phrase_id: m.record_id,
    raw_query: m.raw_query,
    normalized_query: m.raw_query.toLowerCase(),
    protected_class: 'regression',
    family: m.class,
    contrast_positive: m.expected_decision === 'ACCEPT',
    expected_decision: m.expected_decision,
  }))];

  const results = [];
  for (const rec of all) {
    results.push(await evaluateRecord(rec, context, adapter));
  }

  const boxed = results.filter((r) => ['SUP-PROD-BOX-02', 'SUP-PROD-BOX-04'].includes(r.record_id));
  const productNeg = results.filter((r) => r.stratum === 'protected_product' && r.expected_decision === 'REJECT');
  const productFalseAccept = productNeg.filter((r) => r.final_decision === 'ACCEPT');
  const contrastPos = results.filter((r) => r.contrast_positive && r.expected_decision === 'ACCEPT');
  const contrastFalseReject = contrastPos.filter((r) => r.final_decision === 'REJECT');
  const infoNeg = results.filter((r) => r.stratum === 'protected_informational' && r.expected_decision === 'REJECT');
  const infoFalseAccept = infoNeg.filter((r) => r.final_decision === 'ACCEPT');

  const summary = {
    mode: 'CLOSED_DATASET_REGRESSION',
    not_blind_pass: true,
    boxed_delivery_fixed: boxed.every((r) => r.final_decision === 'REJECT'),
    boxed_cases: boxed,
    product_false_accept_count: productFalseAccept.length,
    product_fpr: productNeg.length ? productFalseAccept.length / productNeg.length : null,
    contrast_false_reject_count: contrastFalseReject.length,
    informational_false_accept_count: infoFalseAccept.length,
    minimal_pairs: results.filter((r) => String(r.record_id).startsWith('PSR-')),
    holdout_reference: {
      note: 'Original holdout not re-run — commercial precision 1.0 preserved from completion-pass-1782181300220',
      commercial_precision: 1.0,
    },
  };

  writeJson('closed-regression-manifest-v1.json', {
    run_id: RUN_ID,
    regression_mode: true,
    prompt_version: PROMPT_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    secret_summary: getSafeConfigSummary(),
  });
  writeJson('closed-regression-results-v1.json', results);
  writeJson('closed-regression-summary-v1.json', summary);
  writeJson('cost-gate-v1.json', { ...cost, cap: DEFAULT_CONTROLS.costCapUsd });

  console.log(JSON.stringify({ run_id: RUN_ID, summary, cost_usd: cost.calculated_cost_usd }, null, 2));
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
