#!/usr/bin/env node
/** Wave 3.1E final quality repair bypass audit */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const SUP = path.join(ROOT, 'supplementary');
const CONF = path.join(ROOT, 'confirmation');

const checks = [
  ['confirmation labels not in phrase files', () => {
    const p = JSON.parse(fs.readFileSync(path.join(CONF, 'strata/protected_product_confirmation/phrases-blind-v1.json'), 'utf8'));
    return !JSON.stringify(p).includes('expected_decision');
  }],
  ['confirmation manifest forbids post-run calibration', () => {
    const m = JSON.parse(fs.readFileSync(path.join(CONF, 'strata/geo_commercial_confirmation/manifest-v1.json'), 'utf8'));
    return m.calibration_forbidden === true && m.post_run_calibration_forbidden === true;
  }],
  ['product service policy exists', () => fs.existsSync(path.join(SUP, 'policies/product-service-disambiguation-policy-v1.json'))],
  ['prompt v1.2 product rules', () => {
    const src = fs.readFileSync(path.join(ROOT, 'contracts/prompt-contract.mjs'), 'utf8');
    return src.includes('v1.2') && src.includes('product_only_likelihood');
  }],
  ['adjudicator product service resolver', () => {
    const src = fs.readFileSync(path.join(ROOT, 'adjudication/semantic-adjudicator.mjs'), 'utf8');
    return src.includes('resolveProductServiceDisagreement');
  }],
  ['holdout checksum unchanged', () => {
    const d = JSON.parse(fs.readFileSync(path.join(SUP, 'preservation/original-holdout-closed-declaration-v1.json'), 'utf8'));
    return d.holdout_checksum === '1e76c9f4b94b9cc4288e2bbccd03b812a49d1af29fdf8e0ac9646c77b1e9b52a';
  }],
  ['confirmation record count product 80-120', () => {
    const m = JSON.parse(fs.readFileSync(path.join(CONF, 'strata/protected_product_confirmation/manifest-v1.json'), 'utf8'));
    return m.record_count >= 80 && m.record_count <= 120;
  }],
  ['confirmation record count geo 80-120', () => {
    const m = JSON.parse(fs.readFileSync(path.join(CONF, 'strata/geo_commercial_confirmation/manifest-v1.json'), 'utf8'));
    return m.record_count >= 80 && m.record_count <= 120;
  }],
  ['no phrase-specific record exceptions in adjudicator', () => {
    const src = fs.readFileSync(path.join(ROOT, 'adjudication/semantic-adjudicator.mjs'), 'utf8');
    return !src.includes('SUP-PROD-BOX') && !src.includes('CFM-PROD');
  }],
  ['corvonero not in confirmation runner', () => {
    const src = fs.readFileSync(path.join(__dirname, 'run-confirmation-validation.mjs'), 'utf8');
    return !/corvonero.*classif/i.test(src);
  }],
];

let passed = 0;
for (const [name, fn] of checks) {
  const ok = fn();
  console.log(`  [${ok ? 'PASS' : 'FAIL'}] ${name}`);
  if (ok) passed++;
}
console.log(`Wave 3.1E bypass audit: ${passed}/${checks.length}`);
process.exit(passed === checks.length ? 0 : 1);
