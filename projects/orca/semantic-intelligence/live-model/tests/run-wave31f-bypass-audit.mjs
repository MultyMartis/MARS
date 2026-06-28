#!/usr/bin/env node
/** Wave 3.1F geo-commercial recall repair bypass audit */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const SUP = path.join(ROOT, 'supplementary');
const CONF = path.join(ROOT, 'confirmation');

const checks = [
  ['commercial intent separated from scope fit in contract', () => {
    const c = JSON.parse(fs.readFileSync(path.join(ROOT, 'contracts/commercial-scope-fit-contract-v1.json'), 'utf8'));
    return c.separation_required === true;
  }],
  ['geo evidence policy v2 exists', () => fs.existsSync(path.join(SUP, 'policies/geo-evidence-policy-v2.json'))],
  ['service intent evidence layer exists', () => fs.existsSync(path.join(ROOT, 'evidence/service-intent-evidence.mjs'))],
  ['prompt v1.4 scope-fit rules', () => {
    const src = fs.readFileSync(path.join(ROOT, 'contracts/prompt-contract.mjs'), 'utf8');
    return src.includes('v1.4') && src.includes('scope_fit');
  }],
  ['adjudicator v1.5 mandatory invariants', () => {
    const src = fs.readFileSync(path.join(ROOT, 'adjudication/semantic-adjudicator.mjs'), 'utf8');
    return src.includes('v1.5') && src.includes('applyMandatorySemanticInvariants');
  }],
  ['no phrase-specific exceptions', () => {
    const src = fs.readFileSync(path.join(ROOT, 'adjudication/semantic-adjudicator.mjs'), 'utf8');
    return !src.includes('CFM-GEO-ORD') && !src.includes('CFM2-GEO');
  }],
  ['geo v2 set exists 120-180 records', () => {
    const m = JSON.parse(fs.readFileSync(path.join(CONF, 'strata/geo_commercial_confirmation_v2/manifest-v2.json'), 'utf8'));
    return m.record_count >= 120 && m.record_count <= 180;
  }],
  ['geo v2 commercial_intent_label_separate_from_scope_fit', () => {
    const m = JSON.parse(fs.readFileSync(path.join(CONF, 'strata/geo_commercial_confirmation_v2/manifest-v2.json'), 'utf8'));
    return m.commercial_intent_label_separate_from_scope_fit === true;
  }],
  ['geo v2 post-run calibration forbidden', () => {
    const m = JSON.parse(fs.readFileSync(path.join(CONF, 'strata/geo_commercial_confirmation_v2/manifest-v2.json'), 'utf8'));
    return m.post_run_calibration_forbidden === true;
  }],
  ['product repair v1.2 preserved', () => {
    const src = fs.readFileSync(path.join(ROOT, 'adjudication/semantic-adjudicator.mjs'), 'utf8');
    return src.includes('resolveProductServiceDisagreement');
  }],
  ['holdout checksum unchanged', () => {
    const d = JSON.parse(fs.readFileSync(path.join(SUP, 'preservation/original-holdout-closed-declaration-v1.json'), 'utf8'));
    return d.holdout_checksum === '1e76c9f4b94b9cc4288e2bbccd03b812a49d1af29fdf8e0ac9646c77b1e9b52a';
  }],
  ['platform compatibility layer exists', () => fs.existsSync(path.join(ROOT, 'evidence/platform-compatibility.mjs'))],
  ['product version update repair present', () => {
    const src = fs.readFileSync(path.join(ROOT, '../production/assessors/hard-rules.mjs'), 'utf8');
    return src.includes('product_version_update_hard_rule');
  }],
  ['generic platform family abstain repair present', () => {
    const src = fs.readFileSync(path.join(ROOT, '../production/assessors/hard-rules.mjs'), 'utf8');
    return src.includes('generic_platform_family_abstain_rule');
  }],
  ['ambiguous diy abstain repair present', () => {
    const src = fs.readFileSync(path.join(ROOT, '../production/assessors/hard-rules.mjs'), 'utf8');
    return src.includes('ambiguous_diy_problem_abstain_rule');
  }],
  ['corvonero not classified', () => {
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
console.log(`Wave 3.1F bypass audit: ${passed}/${checks.length}`);
process.exit(passed === checks.length ? 0 : 1);
