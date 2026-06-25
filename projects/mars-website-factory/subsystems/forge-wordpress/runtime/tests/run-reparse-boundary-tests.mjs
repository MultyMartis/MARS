#!/usr/bin/env node
/**
 * FW-07C-1 — Reparse boundary validator tests.
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateReparseBoundary } from '../src/reparse-boundary-validator.mjs';
import { resolveSiteAuthority } from '../src/runtime-authority.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURE_ROOT = path.resolve(__dirname, 'fixtures/synthetic-site');
const FWS_ROOT = 'E:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001';

let passed = 0;
let failed = 0;
const failures = [];

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

function test(name, fn) {
  try {
    fn();
    passed++;
  } catch (err) {
    failed++;
    failures.push(`${name}: ${err.message}`);
  }
}

test('fixture site root resolves within itself', () => {
  const r = validateReparseBoundary(FIXTURE_ROOT, FIXTURE_ROOT);
  assert(r.checked === true, 'checked');
  assert(r.allowed === true, `allowed — ${r.reason_codes.join(',')}`);
  assert(r.escape_detected === false, 'no escape');
});

test('fixture child path stays within root', () => {
  const child = path.join(FIXTURE_ROOT, 'wp-content', 'themes');
  const r = validateReparseBoundary(child, FIXTURE_ROOT);
  assert(r.allowed === true, `allowed — ${r.reason_codes.join(',')}`);
});

test('path outside fixture root is denied', () => {
  const outside = path.resolve(FIXTURE_ROOT, '..', 'outside-escape-test');
  const r = validateReparseBoundary(outside, FIXTURE_ROOT);
  assert(r.allowed === false, 'denied');
});

test('runtime parent E:\\MARS-Localhost is not valid site root', () => {
  const auth = resolveSiteAuthority('fws-0001', 'E:\\MARS-Localhost');
  assert(auth.valid === false, 'parent denied');
});

test('fws-0001 authority resolves when path exists', () => {
  const auth = resolveSiteAuthority('fws-0001');
  if (auth.exists) {
    assert(auth.valid === true, `valid — ${auth.reason_codes.join(',')}`);
  }
});

test('fws-0001 site root reparse self-check when exists', () => {
  const auth = resolveSiteAuthority('fws-0001');
  if (!auth.exists) return;
  const r = validateReparseBoundary(FWS_ROOT, FWS_ROOT);
  assert(r.checked === true, 'checked');
  assert(r.escape_detected === false, 'no escape at site root');
  assert(r.allowed === true, `allowed — ${r.reason_codes.join(',')}`);
});

test('unknown site is denied', () => {
  const auth = resolveSiteAuthority('unknown-site');
  assert(auth.valid === false, 'unknown denied');
});

console.log(`\nReparse boundary tests: ${passed} passed, ${failed} failed`);
if (failures.length) {
  for (const f of failures) console.error(`  FAIL: ${f}`);
}
process.exit(failed > 0 ? 1 : 0);
