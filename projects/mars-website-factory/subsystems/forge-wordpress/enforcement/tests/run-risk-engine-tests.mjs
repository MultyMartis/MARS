#!/usr/bin/env node
/**
 * FW-07C-0 — Risk engine test runner.
 */
import { evaluateRiskClass, VALID_RISK_CLASSES } from '../src/risk-engine.mjs';

let passed = 0;
let failed = 0;
const failures = [];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

for (const rc of VALID_RISK_CLASSES) {
  const result = evaluateRiskClass(rc, 'FW-07C-0', {});
  try {
    if (rc === 'R0') {
      assert(result.allowed === true, 'R0 should be allowed in FW-07C-0');
    } else {
      assert(result.allowed === false, `${rc} should be denied in FW-07C-0`);
      assert(result.reason_codes.includes('FW_RISK_CLASS_DENIED'), `${rc} missing deny code`);
    }
    passed++;
  } catch (err) {
    failed++;
    failures.push(`${rc}: ${err.message}`);
  }
}

try {
  const unknown = evaluateRiskClass('R9', 'FW-07C-0', {});
  assert(unknown.allowed === false, 'unknown risk class denied');
  assert(unknown.reason_codes.includes('FW_UNKNOWN_RISK_CLASS'), 'unknown risk code');
  passed++;
} catch (err) {
  failed++;
  failures.push(`unknown-risk: ${err.message}`);
}

console.log(`Risk engine tests: ${passed} passed, ${failed} failed`);
if (failures.length) {
  for (const f of failures) console.error(`  FAIL: ${f}`);
  process.exit(1);
}
process.exit(0);
