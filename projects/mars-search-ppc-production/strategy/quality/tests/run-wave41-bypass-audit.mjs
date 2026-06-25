#!/usr/bin/env node
/** Wave 4.1 bypass audit — 20 cases */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const QUALITY = path.join(__dirname, '..');

const checks = [
  ['expected architecture not in strategist prompt', () => {
    const src = fs.readFileSync(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/strategy/strategist/prompts/strategist-prompt-v1.mjs'), 'utf8');
    return !src.includes('expected_campaign') && !src.includes('answer_key');
  }],
  ['rubric not in strategist prompt', () => {
    const src = fs.readFileSync(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/strategy/strategist/prompts/strategist-prompt-v1.mjs'), 'utf8');
    return !src.includes('quality_rubric') && !src.includes('scoring_rubric');
  }],
  ['invented budget blocked by invariant', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('no_invented_budget');
  }],
  ['invented landing blocked', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('no_invented_landings');
  }],
  ['constraints marked evaluator_only', () => {
    const dir = path.join(QUALITY, 'evaluation/constraints');
    if (!fs.existsSync(dir)) return false;
    const files = fs.readdirSync(dir).filter((f) => f.endsWith('.json'));
    return files.length >= 30 && files.every((f) => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')).evaluator_only === true);
  }],
  ['missing Paid SERP not hidden invariant', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('missing_paid_serp_not_hidden');
  }],
  ['rejected phrase activation invariant', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('rejected_phrases_not_activated');
  }],
  ['T5 isolation invariant', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('t5_isolated');
  }],
  ['auto bidding without tracking invariant', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('tracking_blocks_auto_bidding');
  }],
  ['exact bid forbidden in prompt', () => {
    const src = fs.readFileSync(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/strategy/strategist/prompts/strategist-prompt-v1.mjs'), 'utf8');
    return src.includes('exact bid');
  }],
  ['blocker preservation in reviewer', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-reviewer.mjs'), 'utf8');
    return src.includes('missingBlockers');
  }],
  ['provisional not production invariant', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('provisional_not_production');
  }],
  ['reviewer separate from strategist adapter', () => {
    return fs.existsSync(path.join(QUALITY, 'runtime/lib/strategy-reviewer.mjs')) &&
      !fs.readFileSync(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/strategy/runtime/lib/strategist-model-adapter.mjs'), 'utf8').includes('strategy-reviewer');
  }],
  ['holdout cases defined in registry', () => {
    const reg = JSON.parse(fs.readFileSync(path.join(QUALITY, 'evaluation/case-registry-v1.json'), 'utf8'));
    return reg.holdout_case_ids.length >= 6;
  }],
  ['calibration does not use holdout by default', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'tests/run-wave41-quality-validation.mjs'), 'utf8');
    return src.includes('holdout_case_ids') && src.includes('HOLDOUT_ONLY');
  }],
  ['no case-specific answers in strategist prompt', () => {
    const src = fs.readFileSync(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/strategy/strategist/prompts/strategist-prompt-v1.mjs'), 'utf8');
    return !src.includes('EV-01') && !src.includes('ADV-01');
  }],
  ['Corvonero not in quality runner', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'tests/run-wave41-quality-validation.mjs'), 'utf8');
    return !/corvonero/i.test(src);
  }],
  ['Wave 5 not started', () => {
    return !fs.existsSync(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/campaign-production'));
  }],
  ['output reconciliation invariant', () => {
    const src = fs.readFileSync(path.join(QUALITY, 'runtime/lib/strategy-invariants.mjs'), 'utf8');
    return src.includes('output_reconciliation');
  }],
  ['quality model contract exists', () => {
    return fs.existsSync(path.join(QUALITY, 'contracts/strategist-quality-model-v1.md'));
  }],
];

let passed = 0;
const results = [];
for (const [name, fn] of checks) {
  const ok = fn();
  results.push({ name, pass: ok });
  console.log(`  [${ok ? 'PASS' : 'FAIL'}] ${name}`);
  if (ok) passed++;
}
const report = { suite: 'wave41-bypass-audit-v1', passed, total: checks.length, results, timestamp: new Date().toISOString() };
fs.mkdirSync(path.join(QUALITY, 'reports'), { recursive: true });
fs.writeFileSync(path.join(QUALITY, 'reports/bypass-audit-results-v1.json'), JSON.stringify(report, null, 2) + '\n');
console.log(`Wave 4.1 bypass audit: ${passed}/${checks.length}`);
process.exit(passed === checks.length ? 0 : 1);
