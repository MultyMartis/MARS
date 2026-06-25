#!/usr/bin/env node
/**
 * FW-07C-0 — Admission validator test runner.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateAdmission } from '../src/admission-validator.mjs';
import { evaluateKillSwitch, DEFAULT_KILL_SWITCH_STATE } from '../src/kill-switch.mjs';
import { buildAuditEvent, sanitizeAuditInput, containsRedactedFields } from '../src/audit-event.mjs';
import {
  getOperationRegistry,
  assertAllContractsLoaded,
} from '../src/operation-registry.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const NEG_ADMISSION = path.join(__dirname, '../fixtures/negative/admission-denials.json');
const POS_DIR = path.join(__dirname, '../fixtures/positive');
const SECRET_FX = path.join(__dirname, '../fixtures/negative/secret-audit-input.json');

let passed = 0;
let failed = 0;
const failures = [];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function runNegativeAdmissionFixtures() {
  const fixtures = JSON.parse(fs.readFileSync(NEG_ADMISSION, 'utf8'));
  for (const fx of fixtures) {
    const result = validateAdmission(fx.request);
    try {
      assert(result.admitted === false, `${fx.fixture_id}: expected denied`);
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

function runPositiveAdmissionFixtures() {
  const files = fs.readdirSync(POS_DIR).filter((f) => f.endsWith('.json'));
  for (const file of files) {
    const fx = JSON.parse(fs.readFileSync(path.join(POS_DIR, file), 'utf8'));
    const result = validateAdmission(fx.request);
    try {
      assert(result.admitted === fx.expected.admitted, `${fx.fixture_id}: admission mismatch`);
      assert(result.decision === fx.expected.decision, `${fx.fixture_id}: decision mismatch`);
      passed++;
    } catch (err) {
      failed++;
      failures.push(`${fx.fixture_id}: ${err.message} — codes: ${result.reason_codes.join(',')}`);
    }
  }
}

function runKillSwitchDefault() {
  const result = evaluateKillSwitch(DEFAULT_KILL_SWITCH_STATE, 'R0');
  try {
    assert(result.allowed === false, 'default kill switch denies');
    passed++;
  } catch (err) {
    failed++;
    failures.push(`kill-switch-default: ${err.message}`);
  }
}

function runAuditSecretMasking() {
  const fx = JSON.parse(fs.readFileSync(SECRET_FX, 'utf8'));
  const sanitized = sanitizeAuditInput(fx.input);
  const event = buildAuditEvent(fx.input);
  const serialized = JSON.stringify(event);
  const sanitizedSerialized = JSON.stringify(sanitized);
  try {
    assert(
      sanitizedSerialized.includes('[REDACTED]'),
      'sanitize should contain redacted marker'
    );
    for (const forbidden of fx.expected.must_not_contain) {
      assert(!serialized.includes(forbidden), `secret leaked in audit event: ${forbidden}`);
    }
    passed++;
  } catch (err) {
    failed++;
    failures.push(`audit-secret: ${err.message}`);
  }
}

function runOperationRegistry() {
  const registry = getOperationRegistry();
  try {
    assert(registry.operation_count === 42, `expected 42 operations, got ${registry.operation_count}`);
    assert(registry.duplicates.length === 0, 'duplicate operation IDs');
    assert(registry.errors.length === 0, `registry errors: ${registry.errors.join('; ')}`);
    const contracts = assertAllContractsLoaded();
    assert(contracts.all_loaded, `contracts mismatch missing=${contracts.missing_in_contracts.length} extra=${contracts.extra_in_contracts.length}`);
    const proven = registry.operations.filter((o) => o.runtime_binding_status === 'PROVEN');
    assert(proven.length === 0, 'no operation should have proven runtime binding');
    passed += 4;
  } catch (err) {
    failed++;
    failures.push(`operation-registry: ${err.message}`);
  }
}

function runNonR0Denied() {
  const registry = getOperationRegistry();
  const nonR0 = registry.operations.filter((o) => o.risk_class !== 'R0');
  for (const op of nonR0.slice(0, 5)) {
    const result = validateAdmission({
      operation_id: op.operation_id,
      site_id: 'fws-0001',
      environment: 'LOCAL_SYNTHETIC',
      raw_path: 'E:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001',
      allowed_root: 'E:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001',
      kill_switch_state: 'SITE_ENABLED_READ_ONLY',
      reparse_status: 'TEST_ONLY_SYNTHETIC_BINDING',
      runtime_binding_status: 'TEST_ONLY_SYNTHETIC_BINDING',
    });
    try {
      assert(result.admitted === false, `${op.operation_id} non-R0 denied`);
      passed++;
    } catch (err) {
      failed++;
      failures.push(`non-r0 ${op.operation_id}: ${err.message}`);
    }
  }
}

runNegativeAdmissionFixtures();
runPositiveAdmissionFixtures();
runKillSwitchDefault();
runAuditSecretMasking();
runOperationRegistry();
runNonR0Denied();

console.log(`Admission tests: ${passed} passed, ${failed} failed`);
if (failures.length) {
  for (const f of failures) console.error(`  FAIL: ${f}`);
  process.exit(1);
}
process.exit(0);
