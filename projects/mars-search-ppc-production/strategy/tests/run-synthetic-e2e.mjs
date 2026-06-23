#!/usr/bin/env node
/**
 * Wave 4 synthetic E2E — pack → strategist → validator
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildDatedAnalyticalPack } from '../runtime/lib/analytical-pack-builder.mjs';
import { buildSearchPpcStrategy } from '../runtime/lib/strategist-contract.mjs';
import { validateSearchPpcStrategy } from '../runtime/lib/strategy-validator.mjs';
import { createStrategistModelAdapter } from '../runtime/lib/strategist-model-adapter.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../..');
const FIX = path.join(__dirname, '../fixtures/synthetic-wave4-e2e');

function load(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

async function main() {
  const manifest = load(path.join(FIX, 'manifest.json'));
  const landingInventory = load(path.join(FIX, 'landing-inventory.json'));
  const offerInventory = load(path.join(FIX, 'offer-inventory.json'));
  const trackingStatus = {
    metrica_counter: { status: 'active', id: '12345' },
    goals: [{ id: 'lead_form', name: 'Lead form' }],
    conversion_history: { count: 12 },
  };

  const packResult = buildDatedAnalyticalPack({
    manifest,
    repoRoot: REPO_ROOT,
    analysisPeriod: { start: '2026-06-01', end: '2026-06-20' },
    options: { landingInventory, offerInventory },
  });

  const checks = [];
  checks.push(['pack built', packResult.ok]);
  checks.push(['readiness COMPLETE', packResult.readiness.readiness === 'COMPLETE']);
  checks.push(['evidence inventory populated', packResult.pack.evidence_inventory.length >= 9]);
  checks.push(['tier distribution', !!packResult.pack.tier_distribution?.T1]);

  const adapter = createStrategistModelAdapter({ mock: true });
  const modelResult = await adapter.strategize(packResult.pack, { trackingStatus });

  const strategyResult = buildSearchPpcStrategy({
    analyticalPack: packResult.pack,
    businessAuthority: packResult.pack.business_authority,
    operatorConstraints: { trackingStatus, launchMode: 'staged' },
    modelOutput: modelResult.ok ? modelResult.output : null,
  });

  checks.push(['strategy built', strategyResult.ok]);
  checks.push(['has architecture', strategyResult.strategy.campaign_segmentation.campaigns.length > 0]);
  checks.push(['T5 isolated', strategyResult.strategy.tier_activation_policy.policies.T5.isolation_required === true]);
  checks.push(['evidence linkage', strategyResult.strategy.supporting_evidence_ids.length > 0]);
  checks.push(['no false production on complete pack', !strategyResult.strategy.production_authority === true || strategyResult.strategy.strategy_status !== 'PRODUCTION READY']);

  const validation = validateSearchPpcStrategy(strategyResult.strategy, packResult.pack);
  checks.push(['validator PASS', validation.ok]);

  const passed = checks.filter(([, ok]) => ok).length;
  const report = {
    suite: 'wave4-synthetic-e2e-v1',
    timestamp: new Date().toISOString(),
    passed,
    total: checks.length,
    checks: checks.map(([name, ok]) => ({ name, pass: ok })),
    pack_readiness: packResult.readiness.readiness,
    strategy_status: strategyResult.strategy.strategy_status,
    validation: validation.verdict,
  };

  const outDir = path.join(__dirname, '../reports');
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, 'synthetic-e2e-results-v1.json'), JSON.stringify(report, null, 2) + '\n');

  console.log(`Synthetic E2E: ${passed}/${checks.length}`);
  for (const [name, ok] of checks) console.log(`  [${ok ? 'PASS' : 'FAIL'}] ${name}`);
  process.exit(passed === checks.length ? 0 : 1);
}

main();
