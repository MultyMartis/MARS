#!/usr/bin/env node
/**
 * FW-07C-1 — Run all repo-local runtime tests.
 */
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const tests = [
  'run-reparse-boundary-tests.mjs',
  'run-runtime-binding-tests.mjs',
  'run-fp0002-admission-tests.mjs',
  'run-fw07c2c-delivery-tests.mjs',
];

let allPassed = true;
const results = [];

for (const test of tests) {
  const testPath = path.join(__dirname, test);
  const proc = spawnSync(process.execPath, [testPath], { encoding: 'utf8' });
  const ok = proc.status === 0;
  if (!ok) allPassed = false;
  results.push({ test, ok, stdout: proc.stdout?.trim(), stderr: proc.stderr?.trim() });
  console.log(`\n=== ${test} ===`);
  if (proc.stdout) console.log(proc.stdout);
  if (proc.stderr) console.error(proc.stderr);
}

console.log('\n=== FW-07C-1 Summary ===');
for (const r of results) {
  console.log(`${r.ok ? 'PASS' : 'FAIL'} ${r.test}`);
}

process.exit(allPassed ? 0 : 1);
