#!/usr/bin/env node
/**
 * Wave 4.1 quality validation orchestrator — blind strategy generation + review
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildEvaluationCase, loadCaseRegistry, loadEvaluationConstraints } from '../runtime/lib/evaluation-case-builder.mjs';
import { buildSearchPpcStrategy } from '../../runtime/lib/strategist-contract.mjs';
import { createStrategistModelAdapter } from '../../runtime/lib/strategist-model-adapter.mjs';
import { runStrategyInvariants, checksumInput, checksumOutput } from '../runtime/lib/strategy-invariants.mjs';
import { reviewStrategy } from '../runtime/lib/strategy-reviewer.mjs';
import { aggregateQualityMetrics, buildOperatorReviewPackage } from '../runtime/lib/quality-metrics.mjs';
import { STRATEGIST_PROMPT_VERSION } from '../../strategist/prompts/strategist-prompt-v1.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const LIVE = process.env.WAVE41_LIVE === '1';
const HOLDOUT_ONLY = process.env.WAVE41_HOLDOUT === '1';
const CALIBRATION = process.env.WAVE41_CALIBRATION || '0';
const REPORTS = path.join(__dirname, '../reports');

async function runCase(caseDef, adapter) {
  const built = buildEvaluationCase(caseDef, REPO_ROOT);
  const constraints = loadEvaluationConstraints(caseDef.id, REPO_ROOT);
  const inputChecksum = checksumInput(built.pack, built.operatorConstraints, built.strategyPolicy);

  const modelResult = await adapter.strategize(built.pack, built.operatorConstraints);
  const strategyResult = buildSearchPpcStrategy({
    analyticalPack: built.pack,
    businessAuthority: built.businessAuthority,
    operatorConstraints: built.operatorConstraints,
    strategyPolicy: built.strategyPolicy,
    modelOutput: modelResult.ok ? modelResult.output : null,
  });

  const strategy = strategyResult.strategy;
  const invariants = runStrategyInvariants(strategy, built.pack, {
    operatorConstraints: built.operatorConstraints,
    landingInventory: built.pack.landing_inventory,
  });
  const reviewer = reviewStrategy({ pack: built.pack, strategy, context: { operatorConstraints: built.operatorConstraints } });

  const usage = modelResult.output?.model_metadata?.usage;
  const costUsd = usage ? ((usage.prompt_tokens || 0) * 0.00000015 + (usage.completion_tokens || 0) * 0.0000006) : 0;

  return {
    case_id: caseDef.id,
    scenario: caseDef.scenario,
    holdout: caseDef.holdout || false,
    adversarial: caseDef.adversarial || false,
    model: adapter.modelId,
    prompt_version: STRATEGIST_PROMPT_VERSION,
    input_checksum: inputChecksum,
    output_checksum: checksumOutput(strategy),
    schema_valid: !!strategy?.strategy_id,
    tokens: usage || null,
    cost_usd: costUsd,
    duration_ms: modelResult.output?.model_metadata?.latency_ms || 0,
    provider_failure: !modelResult.ok && LIVE,
    strategy,
    invariants,
    reviewer,
    constraints_evaluated: !!constraints,
    model_ok: modelResult.ok,
  };
}

function compareStability(run1, run2) {
  const keys = ['strategic_objective', 'campaign_count', 'bidding_family', 'blocker_count'];
  const diffs = [];
  if (run1.strategy?.strategic_objective !== run2.strategy?.strategic_objective) diffs.push('objective');
  const c1 = run1.strategy?.campaign_segmentation?.campaigns?.length || 0;
  const c2 = run2.strategy?.campaign_segmentation?.campaigns?.length || 0;
  if (Math.abs(c1 - c2) > 2) diffs.push('campaign_count');
  if (run1.strategy?.bidding_approach?.primary_strategy !== run2.strategy?.bidding_approach?.primary_strategy) diffs.push('bidding_family');
  const b1 = run1.strategy?.blockers?.length || 0;
  const b2 = run2.strategy?.blockers?.length || 0;
  if (b1 !== b2) diffs.push('blockers');
  if (diffs.length >= 3) return 'material_contradiction';
  if (diffs.length > 0) return 'acceptable_variation';
  return 'stable';
}

async function main() {
  const registry = loadCaseRegistry(REPO_ROOT);
  let cases = registry.cases;
  if (HOLDOUT_ONLY) {
    cases = cases.filter((c) => registry.holdout_case_ids.includes(c.id));
  } else if (CALIBRATION === '0') {
    cases = cases.filter((c) => !registry.holdout_case_ids.includes(c.id));
  }

  const adapter = createStrategistModelAdapter({ mock: !LIVE });
  const results = [];

  for (const caseDef of cases) {
    const result = await runCase(caseDef, adapter);
    results.push(result);
    process.stdout.write(`  [${result.reviewer.verdict}] ${caseDef.id} ${caseDef.scenario}\n`);
  }

  const stabilityResults = [];
  for (const caseId of registry.stability_case_ids) {
    const caseDef = registry.cases.find((c) => c.id === caseId);
    if (!caseDef || (HOLDOUT_ONLY && !registry.holdout_case_ids.includes(caseId))) continue;
    const r1 = await runCase(caseDef, adapter);
    const r2 = await runCase(caseDef, adapter);
    const stability = compareStability(r1, r2);
    stabilityResults.push({ case_id: caseId, stability, run1_objective: r1.strategy?.strategic_objective, run2_objective: r2.strategy?.strategic_objective });
    const idx = results.findIndex((r) => r.case_id === caseId);
    if (idx >= 0) results[idx].stability = stability;
  }

  const constraintsMap = {};
  for (const c of registry.cases) {
    constraintsMap[c.id] = loadEvaluationConstraints(c.id, REPO_ROOT);
  }

  const metrics = aggregateQualityMetrics(results);
  const operatorPackage = buildOperatorReviewPackage(results, constraintsMap);

  const report = {
    suite: 'wave41-quality-validation-v1',
    mode: LIVE ? 'live' : 'mock',
    calibration_iteration: CALIBRATION,
    holdout_only: HOLDOUT_ONLY,
    provider: adapter.provider,
    model_id: adapter.modelId,
    timestamp: new Date().toISOString(),
    case_count: results.length,
    results_summary: results.map((r) => ({
      case_id: r.case_id,
      scenario: r.scenario,
      verdict: r.reviewer.verdict,
      invariant_pass_rate: r.invariants.pass_rate,
      critical_failures: r.invariants.critical_failures,
      stability: r.stability || null,
      cost_usd: r.cost_usd,
    })),
    stability_results: stabilityResults,
    metrics,
    operator_review_package: operatorPackage,
    error_families: buildErrorFamilies(results),
  };

  fs.mkdirSync(REPORTS, { recursive: true });
  const suffix = HOLDOUT_ONLY ? 'holdout' : CALIBRATION !== '0' ? `cal${CALIBRATION}` : 'main';
  fs.writeFileSync(path.join(REPORTS, `quality-validation-results-${suffix}-v1.json`), JSON.stringify(report, null, 2) + '\n');
  console.log(`\nWave 4.1 quality validation (${report.mode}/${suffix}): ${results.length} cases`);
  console.log(`Maturity: ${metrics.maturity_verdict}`);
  console.log(`Critical gates: ${JSON.stringify(metrics.critical_gates)}`);
  process.exit(metrics.all_critical_gates_pass ? 0 : 1);
}

function buildErrorFamilies(results) {
  const families = {
    fabricated_evidence: [], objective_mismatch: [], tier_mixing: [], landing_mismatch: [],
    bidding_overreach: [], budget_invention: [], blocker_omission: [], evidence_citation_failure: [],
  };
  for (const r of results) {
    if (r.reviewer?.invented_claims?.length) families.fabricated_evidence.push({ case_id: r.case_id, claims: r.reviewer.invented_claims });
    if (r.reviewer?.missing_blockers?.length) families.blocker_omission.push({ case_id: r.case_id, blockers: r.reviewer.missing_blockers });
    if (r.reviewer?.bidding_fit === 'FAIL') families.bidding_overreach.push({ case_id: r.case_id });
    if (r.reviewer?.budget_honesty === 'FAIL') families.budget_invention.push({ case_id: r.case_id });
    if (!r.invariants?.results?.find((i) => i.id === 'evidence_refs_exist')?.pass) families.evidence_citation_failure.push({ case_id: r.case_id });
    if (!r.invariants?.results?.find((i) => i.id === 't5_isolated')?.pass) families.tier_mixing.push({ case_id: r.case_id });
    if (r.reviewer?.landing_fit === 'FAIL') families.landing_mismatch.push({ case_id: r.case_id });
  }
  return Object.fromEntries(Object.entries(families).map(([k, v]) => [k, { count: v.length, severity: v.length ? 'critical' : 'none', examples: v.slice(0, 3) }]));
}

main().catch((e) => { console.error(e); process.exit(1); });
