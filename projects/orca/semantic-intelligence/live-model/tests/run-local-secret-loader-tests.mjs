#!/usr/bin/env node
/**
 * Tests for local-secret-loader — no secret values in output.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import {
  parseEnvLine,
  validateRequiredValue,
  loadLocalSecrets,
  getSafeConfigSummary,
} from '../runtime/local-secret-loader.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');

let passed = 0;
let failed = 0;

function assert(cond, msg) {
  if (cond) { passed++; return; }
  failed++;
  console.error('FAIL:', msg);
}

function assertNoSecretsInOutput(obj) {
  const str = JSON.stringify(obj);
  assert(!/sk-or-v1|sk-[a-zA-Z0-9]{10,}/.test(str), 'output must not contain key patterns');
  assert(!str.includes('test-secret-value-12345'), 'output must not contain test secret');
}

// parseEnvLine
assert(parseEnvLine('') === null, 'empty line');
assert(parseEnvLine('# comment') === null, 'comment');
assert(parseEnvLine('KEY=value').key === 'KEY', 'simple parse');
assert(parseEnvLine('KEY="quoted"').value === 'quoted', 'quoted');
assert(parseEnvLine('malformed').malformed === true, 'malformed');

// validateRequiredValue
assert(validateRequiredValue('ORCA_EVAL_MAX_COST', '10').valid, 'valid numeric');
assert(!validateRequiredValue('ORCA_EVAL_MAX_COST', 'abc').valid, 'invalid numeric');
assert(!validateRequiredValue('OPENROUTER_API_KEY', '').valid, 'empty key');

// valid file
const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'orca-secret-test-'));
const validFile = path.join(tmpDir, 'valid.env');
fs.writeFileSync(validFile, `# comment
OPENROUTER_API_KEY=test-secret-value-12345
ORCA_SEMANTIC_PROVIDER=openrouter
ORCA_SEMANTIC_MODEL=openai/gpt-5-mini
ORCA_EVAL_LIVE=1
ORCA_EVAL_MAX_COST=10
ORCA_EVAL_MAX_RECORDS=665
ORCA_EVAL_BATCH_SIZE=10
ORCA_EVAL_CONCURRENCY=2
`);

const saved = {};
for (const k of ['OPENROUTER_API_KEY', 'ORCA_SEMANTIC_PROVIDER', 'ORCA_SEMANTIC_MODEL', 'ORCA_EVAL_LIVE', 'ORCA_EVAL_MAX_COST', 'ORCA_EVAL_MAX_RECORDS', 'ORCA_EVAL_BATCH_SIZE', 'ORCA_EVAL_CONCURRENCY']) {
  saved[k] = process.env[k];
  delete process.env[k];
}

const loaded = loadLocalSecrets({ secretFile: validFile });
assert(loaded.load_status === 'LOADED', `valid file: ${loaded.load_status}`);
assert(loaded.required_status.OPENROUTER_API_KEY === 'SET', 'key status SET');
assertNoSecretsInOutput(loaded);
assert(process.env.OPENROUTER_API_KEY === 'test-secret-value-12345', 'env loaded');

// missing file
const missing = loadLocalSecrets({ secretFile: path.join(tmpDir, 'missing.env') });
assert(missing.load_status === 'FILE_MISSING', 'missing file');

// malformed required row
const badFile = path.join(tmpDir, 'bad.env');
fs.writeFileSync(badFile, 'ORCA_EVAL_MAX_COST=not-a-number\nOPENROUTER_API_KEY=x\nORCA_SEMANTIC_PROVIDER=openrouter\nORCA_SEMANTIC_MODEL=m\nORCA_EVAL_LIVE=1\nORCA_EVAL_MAX_RECORDS=1\nORCA_EVAL_BATCH_SIZE=1\nORCA_EVAL_CONCURRENCY=1\n');
delete process.env.ORCA_EVAL_MAX_COST;
const malformed = loadLocalSecrets({ secretFile: badFile });
assert(malformed.load_status === 'MALFORMED_REQUIRED', 'malformed required');

// existing env priority
process.env.ORCA_SEMANTIC_PROVIDER = 'openai';
const priorityFile = path.join(tmpDir, 'priority.env');
fs.writeFileSync(priorityFile, fs.readFileSync(validFile, 'utf8'));
const priority = loadLocalSecrets({ secretFile: priorityFile, overwrite: false });
assert(process.env.ORCA_SEMANTIC_PROVIDER === 'openai', 'existing env not overwritten');
assert(priority.keys_skipped_existing >= 1, 'skipped existing');

// safe config summary
const summary = getSafeConfigSummary();
assert(summary.OPENROUTER_API_KEY === 'SET', 'summary shows SET not value');
assertNoSecretsInOutput(summary);

// git ignore check
try {
  const ignoreOut = execSync('git check-ignore -v .secrets/orca-live-model.env', { cwd: REPO_ROOT, encoding: 'utf8' });
  assert(ignoreOut.includes('.secrets'), 'secret file gitignored');
} catch {
  assert(false, 'git check-ignore failed');
}

const tracked = execSync('git ls-files .secrets', { cwd: REPO_ROOT, encoding: 'utf8' }).trim();
assert(tracked === '', 'no tracked secrets');

// restore env
for (const [k, v] of Object.entries(saved)) {
  if (v === undefined) delete process.env[k];
  else process.env[k] = v;
}
fs.rmSync(tmpDir, { recursive: true, force: true });

console.log(JSON.stringify({ passed, failed, verdict: failed === 0 ? 'PASS' : 'FAIL' }));
process.exit(failed > 0 ? 1 : 0);
