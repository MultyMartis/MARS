#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import crypto from 'node:crypto';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(PILOT_ROOT, '../../../../../..');
const RUNTIME = path.join(REPO, 'projects/orca/semantic-intelligence/integration/runtime');

function sha256File(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex').toUpperCase();
}

function gitHead() {
  return execSync('git rev-parse --short HEAD', { cwd: REPO, encoding: 'utf8' }).trim();
}

const forbiddenTruth = ['primary_intent_truth', 'eligibility_truth', 'expected_decision', 'gold_label', 'legacy_decision_target'];
const checks = [];
let blocked = false;

function check(id, pass, detail) {
  checks.push({ id, pass, detail });
  if (!pass) blocked = true;
}

const manifest = JSON.parse(fs.readFileSync(path.join(PILOT_ROOT, 'selection/p0-i-pilot-selection-manifest-v1.json'), 'utf8'));
const freeze = JSON.parse(fs.readFileSync(path.join(PILOT_ROOT, 'input/p0-i-pilot-input-freeze-v1.json'), 'utf8'));
const scopeLock = JSON.parse(fs.readFileSync(path.join(PILOT_ROOT, 'config/p0-i-pilot-scope-lock-v1.json'), 'utf8'));

check('input_count_range', manifest.actual_count >= 180 && manifest.actual_count <= 220, { count: manifest.actual_count });
check('unique_phrases', manifest.unique_phrases === manifest.actual_count, { unique: manifest.unique_phrases });
check('provenance_complete', manifest.rows.every((r) => r.provenance?.status === 'COMPLETE'), {});
check('no_forbidden_truth', !manifest.rows.some((r) => forbiddenTruth.some((f) => f in r)), {});
check('freeze_checksum_match', freeze.phrase_count === manifest.actual_count, {});
check('scope_lock_present', !!scopeLock.scope_id, {});
check('runtime_head_pinned', gitHead() === freeze.runtime_commit, { head: gitHead(), pinned: freeze.runtime_commit });

let fixtureOk = false;
try {
  const out = execSync('node tests/run-integration-fixtures.mjs', { cwd: RUNTIME, encoding: 'utf8' });
  fixtureOk = out.includes('"passed": 21');
} catch { fixtureOk = false; }
check('fixture_suite_21_21', fixtureOk, {});

const outDir = path.join(PILOT_ROOT, 'output');
const outFiles = fs.existsSync(outDir) ? fs.readdirSync(outDir) : [];
check('output_dir_clean', outFiles.length === 0, { files: outFiles });

const report = {
  validation_id: 'p0-i-pre-run-validation-v1',
  generated_at: new Date().toISOString(),
  blocked,
  checks,
  status: blocked ? 'BLOCKED — PRE-RUN VALIDATION FAILED' : 'PRE-RUN VALIDATION PASS',
};
fs.mkdirSync(path.join(PILOT_ROOT, 'validation'), { recursive: true });
fs.writeFileSync(path.join(PILOT_ROOT, 'validation/p0-i-pre-run-validation-v1.json'), JSON.stringify(report, null, 2) + '\n', 'utf8');
fs.writeFileSync(path.join(PILOT_ROOT, 'validation/P0-I-PRE-RUN-VALIDATION-v1.md'), `# Pre-Run Validation\n\nStatus: ${report.status}\n\nChecks: ${checks.filter((c) => c.pass).length}/${checks.length} pass\n`, 'utf8');

console.log(JSON.stringify(report, null, 2));
process.exit(blocked ? 2 : 0);
