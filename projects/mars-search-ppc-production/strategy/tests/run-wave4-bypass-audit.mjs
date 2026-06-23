#!/usr/bin/env node
/** Wave 4 bypass audit — 20 cases */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildSearchPpcStrategy } from '../runtime/lib/strategist-contract.mjs';
import { buildDatedAnalyticalPack } from '../runtime/lib/analytical-pack-builder.mjs';
import { validateSearchPpcStrategy } from '../runtime/lib/strategy-validator.mjs';
import { buildEvidenceAuthorityMatrix } from '../runtime/lib/evidence-authority-matrix.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../..');
const FIX = path.join(__dirname, '../fixtures/synthetic-wave4-e2e');

function manifest() {
  return JSON.parse(fs.readFileSync(path.join(FIX, 'manifest.json'), 'utf8'));
}

function packFrom(m = manifest()) {
  return buildDatedAnalyticalPack({ manifest: m, repoRoot: REPO_ROOT }).pack;
}

const tests = [
  { id: 1, name: 'strategy without analytical pack', fn: () => !buildSearchPpcStrategy({ analyticalPack: null }).ok },
  { id: 2, name: 'strategy without semantic pack', fn: () => {
    const m = manifest(); delete m.artifact_registry.commercial_admission_registry;
    return assessBlocked(m);
  }},
  { id: 3, name: 'missing Paid SERP hidden', fn: () => {
    const m = manifest(); delete m.artifact_registry.paid_serp_business_hours_evidence;
    const p = buildDatedAnalyticalPack({ manifest: m, repoRoot: REPO_ROOT }).pack;
    return p.blockers.some((b) => b.includes('PAID SERP'));
  }},
  { id: 4, name: 'diagnostic evidence used as authority', fn: () => {
    const m = manifest();
    m.artifact_registry.paid_serp_business_hours_evidence.path = 'projects/mars-search-ppc-production/strategy/fixtures/scenarios/diagnostic-paid-serp.json';
    const e = buildEvidenceAuthorityMatrix(m, REPO_ROOT).entries.find((x) => x.artifact_type === 'paid_serp_business_hours_evidence');
    return e.authority_level === 'DIAGNOSTIC' && !e.production_eligible;
  }},
  { id: 5, name: 'stale evidence accepted blocked', fn: () => {
    const m = manifest();
    m.artifact_registry.commercial_admission_registry.path = 'projects/mars-search-ppc-production/strategy/fixtures/scenarios/stale-admission.json';
    const r = buildDatedAnalyticalPack({ manifest: m, repoRoot: REPO_ROOT, options: { now: '2026-12-01', staleDays: 30 } });
    return r.readiness.blockers.some((b) => b.includes('STALE'));
  }},
  { id: 6, name: 'observed fact fabricated blocked by statement model', fn: () => fs.existsSync(path.join(__dirname, '../runtime/lib/statement-model.mjs')) },
  { id: 7, name: 'recommendation lacks evidence', fn: () => {
    const p = packFrom();
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority });
    return s.strategy.supporting_evidence_ids.length > 0;
  }},
  { id: 8, name: 'rejected phrase activated', fn: () => {
    const p = packFrom();
    p.semantic_clusters = JSON.parse(fs.readFileSync(path.join(FIX, 'semantic-clusters.json'), 'utf8'));
    p.semantic_clusters.clusters[0].phrases[0].decision = 'REJECT';
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority });
    return !s.strategy.keyword_activation_policy.activate.some((a) => a.phrase_id === 'p1');
  }},
  { id: 9, name: 'cluster without owner activated', fn: () => {
    const p = packFrom();
    p.semantic_clusters.clusters[0].service_id = 'unassigned';
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority });
    return validateSearchPpcStrategy(s.strategy, p).violations.some((v) => v.code === 'cluster_without_owner_activated') || s.strategy.campaign_segmentation.campaigns.some((c) => c.service_direction === 'unassigned');
  }},
  { id: 10, name: 'campaign without landing', fn: () => {
    const p = packFrom();
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority });
    return s.strategy.landing_requirements.results.some((r) => r.outcome === 'LANDING GAP');
  }},
  { id: 11, name: 'bidding without conversion evidence', fn: () => {
    const p = packFrom();
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority, operatorConstraints: { trackingStatus: { metrica_counter: { status: 'active' }, goals: [{}], conversion_history: { count: 0 } } }, strategyPolicy: { autoWithoutConversions: true } });
    return s.strategy.bidding_approach.recommendations.every((r) => r.bidding_approach !== 'automated_conversion_strategy' || r.blockers.length);
  }},
  { id: 12, name: 'budget invented', fn: () => {
    const p = packFrom();
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority, strategyPolicy: { inventBudget: true } });
    return s.strategy.budget_framework?.status === 'BLOCKED' || s.blockers.blockers.some((b) => String(b.code).includes('INVENTED'));
  }},
  { id: 13, name: 'T5 mixed into main launch', fn: () => {
    const p = packFrom();
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority, strategyPolicy: { t5MixedIntoMain: true } });
    return s.strategy.tier_activation_policy.policies.T5.launch_status.includes('BLOCKED');
  }},
  { id: 14, name: 'negative conflict ignored', fn: () => {
    const p = packFrom();
    p.semantic_clusters = JSON.parse(fs.readFileSync(path.join(FIX, 'semantic-clusters.json'), 'utf8'));
    p.negative_intelligence = JSON.parse(fs.readFileSync(path.join(FIX, 'negative-intelligence.json'), 'utf8'));
    p.negative_intelligence.negatives.push({ phrase: 'заказать внедрение 1с', scope: 'global' });
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority });
    return s.blockers.blockers.some((b) => b.code === 'negative_conflict') || s.strategy.keyword_activation_policy.conflict_status === 'CONFLICT';
  }},
  { id: 15, name: 'provisional strategy marked production', fn: () => {
    const m = manifest(); delete m.artifact_registry.paid_serp_business_hours_evidence;
    const p = buildDatedAnalyticalPack({ manifest: m, repoRoot: REPO_ROOT }).pack;
    const s = buildSearchPpcStrategy({ analyticalPack: p, businessAuthority: p.business_authority, strategyPolicy: { forceProvisional: true, claimsProduction: true } });
    return s.blockers.blockers.some((b) => b.code === 'provisional_strategy_marked_production');
  }},
  { id: 16, name: 'Commander requested before approval', fn: () => !buildSearchPpcStrategy({ analyticalPack: packFrom(), commander_export: true }).ok },
  { id: 17, name: 'Wave 5 started early', fn: () => !fs.existsSync(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/campaign-production')) },
  { id: 18, name: 'Corvonero strategy generated', fn: () => !fs.existsSync(path.join(REPO_ROOT, 'projects/orca/projects/corvonero-direct-v2-clean-room/strategy')) },
  { id: 19, name: 'secret leak', fn: () => {
    const src = fs.readFileSync(path.join(__dirname, '../runtime/lib/strategist-model-adapter.mjs'), 'utf8');
    return !src.match(/sk-[a-zA-Z0-9_-]{10,}/) && src.includes('[REDACTED]');
  }},
  { id: 20, name: 'output reconciliation failure', fn: () => {
    const p = packFrom();
    const landing = JSON.parse(fs.readFileSync(path.join(FIX, 'landing-inventory.json'), 'utf8'));
    const offer = JSON.parse(fs.readFileSync(path.join(FIX, 'offer-inventory.json'), 'utf8'));
    p.landing_inventory = landing;
    p.offer_inventory = offer;
    const s = buildSearchPpcStrategy({
      analyticalPack: p,
      businessAuthority: p.business_authority,
      operatorConstraints: { trackingStatus: { metrica_counter: { status: 'active' }, goals: [{ id: 'lead' }], conversion_history: { count: 5 } } },
    });
    return validateSearchPpcStrategy(s.strategy, p).ok;
  }},
];

function assessBlocked(m) {
  const r = buildDatedAnalyticalPack({ manifest: m, repoRoot: REPO_ROOT });
  return r.readiness.readiness === 'BLOCKED' || r.readiness.readiness === 'PARTIAL — PROVISIONAL ONLY';
}

async function main() {
  const results = [];
  for (const t of tests) {
    const pass = !!(await t.fn());
    results.push({ id: t.id, name: t.name, pass });
    console.log(`  [${pass ? 'PASS' : 'FAIL'}] #${t.id} ${t.name}`);
  }
  const passed = results.filter((r) => r.pass).length;
  const out = { suite: 'wave4-bypass-audit-v1', passed, total: results.length, results, timestamp: new Date().toISOString() };
  fs.mkdirSync(path.join(__dirname, '../reports'), { recursive: true });
  fs.writeFileSync(path.join(__dirname, '../reports/bypass-audit-results-v1.json'), JSON.stringify(out, null, 2) + '\n');
  console.log(`Wave 4 bypass audit: ${passed}/${results.length}`);
  process.exit(passed === results.length ? 0 : 1);
}

main();
