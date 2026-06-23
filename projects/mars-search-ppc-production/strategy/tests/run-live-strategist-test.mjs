#!/usr/bin/env node
/**
 * Bounded live strategist model test — validates behavior not client quality
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildDatedAnalyticalPack } from '../runtime/lib/analytical-pack-builder.mjs';
import { buildSearchPpcStrategy } from '../runtime/lib/strategist-contract.mjs';
import { createStrategistModelAdapter } from '../runtime/lib/strategist-model-adapter.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../..');
const FIX = path.join(__dirname, '../fixtures/synthetic-wave4-e2e');
const LIVE = process.env.WAVE4_LIVE_STRATEGIST === '1';

async function main() {
  const manifest = JSON.parse(fs.readFileSync(path.join(FIX, 'manifest.json'), 'utf8'));
  const landingInventory = JSON.parse(fs.readFileSync(path.join(FIX, 'landing-inventory.json'), 'utf8'));
  const offerInventory = JSON.parse(fs.readFileSync(path.join(FIX, 'offer-inventory.json'), 'utf8'));

  const packResult = buildDatedAnalyticalPack({
    manifest,
    repoRoot: REPO_ROOT,
    options: { landingInventory, offerInventory },
  });

  const adapter = createStrategistModelAdapter({ mock: !LIVE });
  const modelResult = await adapter.strategize(packResult.pack, {
    trackingStatus: { metrica_counter: { status: 'active' }, goals: [{ id: 'lead' }], conversion_history: { count: 5 } },
  });

  const strategyResult = buildSearchPpcStrategy({
    analyticalPack: packResult.pack,
    businessAuthority: packResult.pack.business_authority,
    modelOutput: modelResult.ok ? modelResult.output : null,
    operatorConstraints: {
      trackingStatus: { metrica_counter: { status: 'active' }, goals: [{ id: 'lead' }], conversion_history: { count: 5 } },
    },
  });

  const checks = [
    ['model responded', modelResult.ok],
    ['structured output', !!modelResult.output],
    ['evidence refs preserved', (strategyResult.strategy.supporting_evidence_ids || []).length > 0],
    ['no invented budget in strategy', !JSON.stringify(strategyResult.strategy).includes('"monthly_budget": 999999')],
    ['blockers preserved', Array.isArray(strategyResult.strategy.blockers)],
    ['tier policy intact', strategyResult.strategy.tier_activation_policy?.policies?.T5?.isolation_required === true],
    ['mode', LIVE ? 'live' : 'mock'],
  ];

  const passed = checks.filter(([, ok]) => ok).length;
  const report = {
    suite: 'wave4-live-strategist-test-v1',
    mode: LIVE ? 'live' : 'mock',
    provider: adapter.provider,
    model_id: adapter.modelId,
    passed,
    total: checks.length,
    checks: checks.map(([name, ok]) => ({ name, pass: ok })),
    usage: modelResult.output?.model_metadata?.usage || null,
    timestamp: new Date().toISOString(),
  };

  fs.mkdirSync(path.join(__dirname, '../reports'), { recursive: true });
  fs.writeFileSync(path.join(__dirname, '../reports/live-strategist-test-results-v1.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(`Live strategist test (${report.mode}): ${passed}/${checks.length}`);
  process.exit(passed === checks.length ? 0 : 1);
}

main();
