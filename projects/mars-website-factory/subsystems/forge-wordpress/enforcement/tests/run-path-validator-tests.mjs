#!/usr/bin/env node
/**
 * FW-07C-0 — Path validator test runner.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validatePath, loadProtectedRoots } from '../src/path-validator.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURES = path.join(__dirname, '../fixtures/negative/path-denials.json');

let passed = 0;
let failed = 0;
const failures = [];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function runPathDenialFixtures() {
  const fixtures = JSON.parse(fs.readFileSync(FIXTURES, 'utf8'));
  for (const fx of fixtures) {
    const result = validatePath(fx.path_input);
    try {
      assert(result.allowed === false, `${fx.fixture_id}: expected denied`);
      assert(
        result.reason_codes.includes(fx.expected_code),
        `${fx.fixture_id}: expected ${fx.expected_code}, got ${result.reason_codes.join(',')}`
      );
      passed++;
    } catch (err) {
      failed++;
      failures.push(`${fx.fixture_id}: ${err.message}`);
    }
  }
}

function runProtectedRootsAllDenied() {
  const roots = loadProtectedRoots();
  for (const root of roots) {
    const displayRoot = root.replace(/\//g, '\\');
    const result = validatePath({ raw_path: displayRoot });
    try {
      assert(result.allowed === false, `protected root ${displayRoot} should be denied`);
      assert(
        result.reason_codes.includes('FW_PATH_PROTECTED_ROOT') ||
          result.reason_codes.includes('FW_PATH_DRIVE_ROOT'),
        `missing protected/drive code for ${displayRoot}: ${result.reason_codes.join(',')}`
      );
      passed++;
    } catch (err) {
      failed++;
      failures.push(`protected-root ${displayRoot}: ${err.message}`);
    }
  }
}

function runSyntheticDescendantAllowed() {
  const result = validatePath({
    raw_path: 'E:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001\\wp-content\\themes\\x',
    allowed_root: 'E:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001',
  });
  try {
    assert(result.allowed === true, 'synthetic descendant should be allowed');
    assert(result.requires_reparse_check === true, 'reparse check required');
    passed++;
  } catch (err) {
    failed++;
    failures.push(`synthetic-descendant: ${err.message}`);
  }
}

runPathDenialFixtures();
runProtectedRootsAllDenied();
runSyntheticDescendantAllowed();

console.log(`Path validator tests: ${passed} passed, ${failed} failed`);
if (failures.length) {
  for (const f of failures) console.error(`  FAIL: ${f}`);
  process.exit(1);
}
process.exit(0);
