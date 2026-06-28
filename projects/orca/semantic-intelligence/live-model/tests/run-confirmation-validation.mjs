#!/usr/bin/env node
/**
 * Generic blind confirmation live runner (Wave 3.1E).
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
const CONF = path.join(__dirname, '../confirmation');
const FIX = path.join(__dirname, '../fixtures');

const stratumArg = process.argv.find((a) => a.startsWith('--stratum='))?.split('=')[1];
const runLabel = process.argv.find((a) => a.startsWith('--run-label='))?.split('=')[1]
  || (stratumArg?.includes('geo') ? 'geo' : 'product');
const STRATUM_VERSION = stratumArg === 'geo_commercial_confirmation_v2' ? 'v2' : 'v1';
if (!stratumArg) {
  console.error('Usage: node run-confirmation-validation.mjs --stratum=protected_product_confirmation|geo_commercial_confirmation|geo_commercial_confirmation_v2');
  process.exit(1);
}

const RUN_ID = `confirmation-${runLabel}-pass-${Date.now()}`;
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

function stratumFiles(stratum) {
  const ver = stratum === 'geo_commercial_confirmation_v2' ? 'v2' : 'v1';
  return {
    phrases: path.join(CONF, 'strata', stratum, `phrases-blind-${ver}.json`),
    labels: path.join(CONF, 'strata', stratum, `gold-labels-sealed-${ver}.json`),
  };
}

function mergeStratum(stratum) {
  const files = stratumFiles(stratum);
  const phrases = loadJson(files.phrases);
  const labels = loadJson(files.labels);
  const labelMap = new Map(labels.records.map((r) => [r.record_id, r]));
  return phrases.records.map((p) => {
    const l = labelMap.get(p.record_id);
    if (!l) throw new Error(`Missing label for ${p.record_id}`);
    return {
      ...p,
      expected_decision: l.expected_decision,
      expected_authority_class: l.expected_authority_class,
      expected_protected_intent_class: l.expected_protected_intent_class,
      expected_scope_fit: l.expected_scope_fit,
      gold_authority_basis: l.gold_authority_basis,
      geo_class: p.geo_class || l.geo_class,
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
  const hardRules = applyHardRules(phrase, det, context);
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
    businessScope: context.businessScope,
    phrase,
  });
  cost.records_processed++;
  return {
    record_id: record.record_id,
    raw_query: record.raw_query,
    stratum: record.stratum,
    family: record.family,
    geo_class: record.geo_class,
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
    hard_rule_blocked: hardRules.blocked || false,
    scope_fit: adj.scope_fit,
    ownership: adj.ownership,
    service_gap: adj.service_gap,
    expected_scope_fit: record.expected_scope_fit,
  };
}

function productMetrics(results) {
  const gold = results.filter((r) => r.expected_authority_class === 'gold' && !r.error);
  const protectedNeg = gold.filter((r) => r.expected_decision === 'REJECT');
  const falseAccepts = protectedNeg.filter((r) => r.final_decision === 'ACCEPT');
  const contrast = gold.filter((r) => r.contrast_positive);
  const falseRejects = contrast.filter((r) => r.expected_decision === 'ACCEPT' && r.final_decision === 'REJECT');
  const productOnlyAccept = gold.filter((r) => r.expected_decision === 'REJECT' && r.final_decision === 'ACCEPT');
  const productOnlyAbstain = gold.filter((r) => r.expected_decision === 'REJECT' && r.final_decision === 'ABSTAIN');
  const fpr = protectedNeg.length ? falseAccepts.length / protectedNeg.length : null;
  return {
    total_gold: gold.length,
    false_accept_on_protected_negatives: falseAccepts.length,
    false_positive_rate: fpr,
    false_reject_contrast_positives: falseRejects.length,
    product_only_accept_count: productOnlyAccept.length,
    product_only_abstain_count: productOnlyAbstain.length,
    gate_pass: fpr !== null && fpr <= 0.01,
    false_accepts: falseAccepts.map((r) => ({ record_id: r.record_id, query: r.raw_query })),
  };
}

function geoMetrics(results) {
  const gold = results.filter((r) => r.expected_authority_class === 'gold' && !r.error);
  const commercial = gold.filter((r) => r.geo_class === 'commercial_geo' || r.contrast_positive);
  const adversarial = gold.filter((r) => r.geo_class === 'noncommercial_geo' || r.expected_decision === 'REJECT');
  const commercialAccepts = commercial.filter((r) => r.expected_decision === 'ACCEPT' && r.final_decision === 'ACCEPT');
  const commercialFalseRejects = commercial.filter((r) => r.expected_decision === 'ACCEPT' && r.final_decision === 'REJECT');
  const adversarialFalseAccepts = adversarial.filter((r) => r.expected_decision !== 'ACCEPT' && r.final_decision === 'ACCEPT');
  const highConfGeoAccept = commercial.filter((r) => r.final_decision === 'ACCEPT' && (r.confidence || 0) >= 0.7);
  const highConfCorrect = highConfGeoAccept.filter((r) => r.expected_decision === 'ACCEPT');
  const advFpr = adversarial.length ? adversarialFalseAccepts.length / adversarial.length : null;
  const commercialRecall = commercial.filter((r) => r.expected_decision === 'ACCEPT').length
    ? commercialAccepts.length / commercial.filter((r) => r.expected_decision === 'ACCEPT').length
    : null;
  return {
    total_gold: gold.length,
    commercial_recall: commercialRecall,
    commercial_false_reject_count: commercialFalseRejects.length,
    adversarial_false_accept_count: adversarialFalseAccepts.length,
    adversarial_false_accept_rate: advFpr,
    high_confidence_geo_precision: highConfGeoAccept.length ? highConfCorrect.length / highConfGeoAccept.length : null,
    recall_gate_threshold: 0.90,
    gate_pass: (commercialRecall === null || commercialRecall >= 0.90)
      && (advFpr === null || advFpr <= 0.01)
      && (highConfGeoAccept.length === 0 || (highConfCorrect.length / highConfGeoAccept.length) >= 0.95),
    commercial_false_rejects: commercialFalseRejects.map((r) => ({ record_id: r.record_id, query: r.raw_query })),
    adversarial_false_accepts: adversarialFalseAccepts.map((r) => ({ record_id: r.record_id, query: r.raw_query })),
    in_scope_commercial_recall: computeInScopeRecall(gold),
    out_of_scope_commercial_intent_recall: computeOutOfScopeRecall(gold),
    scope_fit_accuracy: computeScopeFitAccuracy(gold),
    provider_noun_recall: computeFamilyRecall(gold, 'provider'),
    service_task_recall: computeFamilyRecall(gold, 'task'),
    product_service_recall: computeFamilyRecall(gold, 'product_service'),
    abstain_rate: gold.filter((r) => r.final_decision === 'ABSTAIN').length / (gold.length || 1),
    review_ratio: results.filter((r) => r.human_review_required).length / (results.length || 1),
    adjudicator_overturn_rate: results.filter((r) => r.adjudicator_overturn).length / (results.length || 1),
  };
}

function computeInScopeRecall(gold) {
  const inScope = gold.filter((r) => r.expected_scope_fit === 'IN_SCOPE' && r.expected_decision === 'ACCEPT');
  if (!inScope.length) return null;
  return inScope.filter((r) => r.final_decision === 'ACCEPT').length / inScope.length;
}

function computeOutOfScopeRecall(gold) {
  const oos = gold.filter((r) => (r.expected_scope_fit === 'OUT_OF_SCOPE' || r.family?.includes('out_of_scope')) && r.expected_decision === 'ACCEPT');
  if (!oos.length) return null;
  return oos.filter((r) => r.final_decision === 'ACCEPT').length / oos.length;
}

function computeScopeFitAccuracy(gold) {
  const labeled = gold.filter((r) => r.expected_scope_fit && r.expected_scope_fit !== 'VARIES' && r.expected_scope_fit !== 'N/A');
  if (!labeled.length) return null;
  return labeled.filter((r) => r.scope_fit === r.expected_scope_fit).length / labeled.length;
}

function computeFamilyRecall(gold, kind) {
  const patterns = {
    provider: /provider|PRV|PRV/i,
    task: /task|TSK|implementation/i,
    product_service: /product_service|PSV|PSV/i,
  };
  const subset = gold.filter((r) => patterns[kind].test(r.family || r.record_id || '') && r.expected_decision === 'ACCEPT');
  if (!subset.length) return null;
  return subset.filter((r) => r.final_decision === 'ACCEPT').length / subset.length;
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

  const records = mergeStratum(stratumArg);
  const results = [];
  for (const rec of records) {
    results.push(await evaluateRecord(rec, context, adapter, controls));
  }

  const metrics = stratumArg?.includes('geo_commercial')
    ? geoMetrics(results)
    : productMetrics(results);

  writeJson('confirmation-run-manifest-v1.json', {
    run_id: RUN_ID,
    stratum: stratumArg,
    confirmation_blind_validation: true,
    assessor_label_access: false,
    prompt_version: PROMPT_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    provider: process.env.ORCA_SEMANTIC_PROVIDER,
    model: process.env.ORCA_SEMANTIC_MODEL,
    secret_summary: getSafeConfigSummary(),
    record_count: results.length,
  });
  writeJson('confirmation-results-v1.json', results);
  writeJson('confirmation-metrics-v1.json', metrics);
  writeJson('cost-gate-v1.json', { ...cost, cap: controls.costCapUsd });

  console.log(JSON.stringify({ run_id: RUN_ID, stratum: stratumArg, metrics, cost_usd: cost.calculated_cost_usd, out: OUT }, null, 2));
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
