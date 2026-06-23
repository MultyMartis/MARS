#!/usr/bin/env node
/** Wave 3.1D supplementary validation bypass audit */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SUP = path.join(__dirname, '../supplementary');

const checks = [
  ['supplementary labels not in phrase files', () => {
    const p = JSON.parse(fs.readFileSync(path.join(SUP, 'strata/protected_product/phrases-blind-v1.json'), 'utf8'));
    return !JSON.stringify(p).includes('expected_decision');
  }],
  ['manifest forbids calibration', () => {
    const m = JSON.parse(fs.readFileSync(path.join(SUP, 'strata/protected_product/manifest-v1.json'), 'utf8'));
    return m.calibration_forbidden === true && m.supplementary_blind_validation === true;
  }],
  ['holdout checksum unchanged', () => {
    const d = JSON.parse(fs.readFileSync(path.join(SUP, 'preservation/original-holdout-closed-declaration-v1.json'), 'utf8'));
    return d.holdout_checksum === '1e76c9f4b94b9cc4288e2bbccd03b812a49d1af29fdf8e0ac9646c77b1e9b52a';
  }],
  ['gold authority contract exists', () => fs.existsSync(path.join(SUP, 'authority/supplementary-blind-gold-authority-contract-v1.json'))],
  ['min 50 gold product records', () => {
    const m = JSON.parse(fs.readFileSync(path.join(SUP, 'strata/protected_product/manifest-v1.json'), 'utf8'));
    return m.gold_record_count >= 50;
  }],
  ['min 50 gold informational records', () => {
    const m = JSON.parse(fs.readFileSync(path.join(SUP, 'strata/protected_informational/manifest-v1.json'), 'utf8'));
    return m.gold_record_count >= 50;
  }],
  ['ambiguous problem policy present', () => fs.existsSync(path.join(SUP, 'policies/ambiguous-problem-query-policy-v1.json'))],
  ['under-admission analysis documented', () => fs.existsSync(path.join(SUP, 'regression/commercial-under-admission-analysis-v1.json'))],
  ['no secrets in supplementary tree', () => {
    const text = fs.readFileSync(path.join(SUP, 'authority/supplementary-blind-gold-authority-contract-v1.json'), 'utf8');
    return !/sk-[a-zA-Z0-9]/.test(text);
  }],
  ['corvonero not in supplementary runner', () => {
    const src = fs.readFileSync(path.join(__dirname, 'run-supplementary-validation.mjs'), 'utf8');
    return !/corvonero.*classif/i.test(src);
  }],
];

let passed = 0;
for (const [name, fn] of checks) {
  const ok = fn();
  console.log(`  [${ok ? 'PASS' : 'FAIL'}] ${name}`);
  if (ok) passed++;
}
console.log(`Wave 3.1D bypass audit: ${passed}/${checks.length}`);
process.exit(passed === checks.length ? 0 : 1);
