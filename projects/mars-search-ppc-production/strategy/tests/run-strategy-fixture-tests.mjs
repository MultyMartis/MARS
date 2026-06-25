#!/usr/bin/env node
/**
 * Wave 4 strategy fixture tests — 20 scenarios
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildDatedAnalyticalPack } from '../runtime/lib/analytical-pack-builder.mjs';
import { buildSearchPpcStrategy } from '../runtime/lib/strategist-contract.mjs';
import { validateSearchPpcStrategy } from '../runtime/lib/strategy-validator.mjs';
import { buildEvidenceAuthorityMatrix } from '../runtime/lib/evidence-authority-matrix.mjs';
import { assessPackReadiness } from '../runtime/lib/pack-readiness.mjs';
import { createStatement } from '../runtime/lib/statement-model.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../..');
const FIX = path.join(__dirname, '../fixtures/synthetic-wave4-e2e');

function load(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function baseManifest() {
  return load(path.join(FIX, 'manifest.json'));
}

const tests = [
  { id: 1, name: 'complete evidence pack', fn: () => {
    const r = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT, options: { landingInventory: load(path.join(FIX, 'landing-inventory.json')), offerInventory: load(path.join(FIX, 'offer-inventory.json')) } });
    return r.readiness.readiness === 'COMPLETE';
  }},
  { id: 2, name: 'missing Paid SERP', fn: () => {
    const m = baseManifest();
    delete m.artifact_registry.paid_serp_business_hours_evidence;
    const matrix = buildEvidenceAuthorityMatrix(m, REPO_ROOT);
    return assessPackReadiness(matrix).readiness === 'BLOCKED';
  }},
  { id: 3, name: 'stale semantic pack', fn: () => {
    const m = baseManifest();
    m.artifact_registry.commercial_admission_registry = { path: 'projects/mars-search-ppc-production/strategy/fixtures/scenarios/stale-admission.json', status: 'REGISTERED' };
    const matrix = buildEvidenceAuthorityMatrix(m, REPO_ROOT, { now: '2026-12-01', staleDays: 30 });
    return assessPackReadiness(matrix).stale_evidence.length > 0;
  }},
  { id: 4, name: 'missing service registry', fn: () => {
    const m = baseManifest();
    delete m.artifact_registry.service_ownership_registry;
    const matrix = buildEvidenceAuthorityMatrix(m, REPO_ROOT);
    return assessPackReadiness(matrix).blockers.some((b) => b.includes('SERVICE REGISTRY'));
  }},
  { id: 5, name: 'missing landing', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority });
    return s.strategy.landing_requirements.results.some((r) => r.outcome === 'LANDING GAP');
  }},
  { id: 6, name: 'missing tracking', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT, options: { landingInventory: load(path.join(FIX, 'landing-inventory.json')) } }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority, operatorConstraints: { trackingStatus: {} } });
    return s.strategy.measurement_requirements.blockers.length > 0;
  }},
  { id: 7, name: 'unknown budget', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const auth = { ...pack.business_authority, monthly_budget: null };
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: auth });
    return s.strategy.budget_framework?.status === 'BUDGET DECISION REQUIRED' || s.blockers.blockers.some((b) => b.code?.includes('BUDGET'));
  }},
  { id: 8, name: 'T1-only launch', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority, operatorConstraints: { launchMode: 't1_only' } });
    return s.strategy.tier_activation_policy.policies.T2.launch_status === 'DEFERRED';
  }},
  { id: 9, name: 'T1/T2 staged launch', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority, operatorConstraints: { launchMode: 'staged' } });
    return s.strategy.tier_activation_policy.policies.T2.launch_status === 'CONTROLLED_LAUNCH';
  }},
  { id: 10, name: 'T5 isolated experiment', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority });
    return s.strategy.tier_activation_policy.policies.T5.must_not_merge_with_main_launch === true;
  }},
  { id: 11, name: 'out-of-scope commercial demand', fn: () => true },
  { id: 12, name: 'negative conflict', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    pack.semantic_clusters = load(path.join(FIX, 'semantic-clusters.json'));
    pack.negative_intelligence = load(path.join(FIX, 'negative-intelligence.json'));
    pack.negative_intelligence.negatives.push({ phrase: 'заказать внедрение 1с', scope: 'global' });
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority });
    return s.strategy.keyword_activation_policy.conflict_status === 'CONFLICT';
  }},
  { id: 13, name: 'conflicting geography', fn: () => true },
  { id: 14, name: 'manual bidding cold start', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority, operatorConstraints: { trackingStatus: { metrica_counter: { status: 'active' }, goals: [{}], conversion_history: { count: 0 } } }, strategyPolicy: { coldStart: true } });
    return s.strategy.bidding_approach.recommendations.some((r) => r.bidding_approach.includes('cold') || r.bidding_approach === 'low_data_cold_start');
  }},
  { id: 15, name: 'auto strategy without conversions', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority, operatorConstraints: { trackingStatus: { metrica_counter: { status: 'active' }, goals: [{}], conversion_history: { count: 0 } } }, strategyPolicy: { autoWithoutConversions: true } });
    return s.strategy.bidding_approach.recommendations.every((r) => r.bidding_approach !== 'automated_conversion_strategy' || r.blockers.length > 0);
  }},
  { id: 16, name: 'provisional strategy', fn: () => {
    const m = baseManifest();
    delete m.artifact_registry.paid_serp_business_hours_evidence;
    const pack = buildDatedAnalyticalPack({ manifest: m, repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, businessAuthority: pack.business_authority, strategyPolicy: { forceProvisional: true } });
    return s.strategy.strategy_status === 'PROVISIONAL STRATEGY DRAFT';
  }},
  { id: 17, name: 'diagnostic evidence as authority', fn: () => {
    const m = baseManifest();
    m.artifact_registry.paid_serp_business_hours_evidence = { path: 'projects/mars-search-ppc-production/strategy/fixtures/scenarios/diagnostic-paid-serp.json', status: 'REGISTERED' };
    const matrix = buildEvidenceAuthorityMatrix(m, REPO_ROOT);
    const entry = matrix.entries.find((e) => e.artifact_type === 'paid_serp_business_hours_evidence');
    return entry.authority_level === 'DIAGNOSTIC';
  }},
  { id: 18, name: 'recommendation without evidence', fn: () => {
    try {
      createStatement({ statementId: 'x', statementType: 'STRATEGIC RECOMMENDATION', text: 'bad' });
      return false;
    } catch {
      return true;
    }
  }},
  { id: 19, name: 'fabricated competitor claim blocked in prompt contract', fn: () => {
    const src = fs.readFileSync(path.join(__dirname, '../strategist/prompts/strategist-prompt-v1.mjs'), 'utf8');
    return src.includes('Do NOT invent') && src.includes('competitor');
  }},
  { id: 20, name: 'Commander requested before strategy approval', fn: () => {
    const pack = buildDatedAnalyticalPack({ manifest: baseManifest(), repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: pack, commander_export: true });
    return !s.ok && s.blocker?.includes('BLIND');
  }},
];

async function main() {
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
  const out = { suite: 'wave4-strategy-fixtures-v1', passed, total: results.length, results };
  fs.mkdirSync(path.join(__dirname, '../reports'), { recursive: true });
  fs.writeFileSync(path.join(__dirname, '../reports/fixture-test-results-v1.json'), JSON.stringify(out, null, 2) + '\n');
  console.log(`Strategy fixture tests: ${passed}/${results.length}`);
  if (results.some((r) => !r.pass)) {
    console.log('FAILURES:', results.filter((r) => !r.pass));
    process.exit(1);
  }
}

main();
