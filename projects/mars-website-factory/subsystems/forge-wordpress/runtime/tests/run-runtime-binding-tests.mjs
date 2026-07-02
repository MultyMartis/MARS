#!/usr/bin/env node
/**
 * FW-07C-1 — Runtime binding and admission chain tests.
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { executeRuntimeInspection } from '../src/runtime-inspection-chain.mjs';
import { createAdmissionToken, validateAdmissionToken } from '../src/admission-token.mjs';
import {
  inspectRuntimeStructure,
  inspectThemeMetadata,
} from '../adapters/local-synthetic-readonly-adapter.mjs';
import { lookupBinding } from '../src/runtime-binding-registry.mjs';
import { detectMutation } from '../src/mutation-detector.mjs';
import { captureBaseline } from '../src/baseline-capture.mjs';
import { RUNTIME_REASON_CODES as RC } from '../src/runtime-reason-codes.mjs';
import { registerTestSiteAuthority, resolveSiteAuthority } from '../src/runtime-authority.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURE_ROOT = path.resolve(__dirname, 'fixtures/synthetic-site');
const FWS_ROOT = 'X:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001';
const SHPIGOVSKY_ROOT = 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky';
const FIXTURE_SITE_ID = 'fw07c1-test-fixture';

registerTestSiteAuthority(FIXTURE_SITE_ID, FIXTURE_ROOT);

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

function baseRequest(overrides = {}) {
  return {
    operation_id: 'wp.inspect.runtime',
    site_id: FIXTURE_SITE_ID,
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FIXTURE_ROOT,
    logical_target: FIXTURE_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    ...overrides,
  };
}

// --- Negative tests ---

test('adapter called without admission is denied', () => {
  let denied = false;
  try {
    inspectRuntimeStructure(FIXTURE_ROOT, null, { operation_id: 'wp.inspect.runtime', site_id: 'fws-0001' });
  } catch (err) {
    denied = err.code === RC.RT_DIRECT_ADAPTER_DENIED;
  }
  assert(denied, 'direct adapter denied');
});

test('expired token is denied', () => {
  const token = createAdmissionToken({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FIXTURE_ROOT,
    logical_target: FIXTURE_ROOT,
    physical_target: FIXTURE_ROOT,
    risk_class: 'R0',
    runtime_binding_id: 'test',
    reparse_verified: true,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    decision: 'ADMIT',
  }, -1000);
  const v = validateAdmissionToken(token, { operation_id: 'wp.inspect.runtime', site_id: 'fws-0001', logical_target: FIXTURE_ROOT });
  assert(!v.valid, 'expired denied');
  assert(v.reason_codes.includes(RC.RT_ADMISSION_TOKEN_EXPIRED), 'expired code');
});

test('token for another site is denied', () => {
  const token = createAdmissionToken({
    operation_id: 'wp.inspect.runtime',
    site_id: 'shpigovsky',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FIXTURE_ROOT,
    logical_target: FIXTURE_ROOT,
    physical_target: FIXTURE_ROOT,
    risk_class: 'R0',
    runtime_binding_id: 'test',
    reparse_verified: true,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    decision: 'ADMIT',
  });
  const v = validateAdmissionToken(token, { operation_id: 'wp.inspect.runtime', site_id: 'fws-0001', logical_target: FIXTURE_ROOT });
  assert(!v.valid, 'wrong site denied');
});

test('token for another operation is denied', () => {
  const token = createAdmissionToken({
    operation_id: 'wp.inspect.theme',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FIXTURE_ROOT,
    logical_target: FIXTURE_ROOT,
    physical_target: FIXTURE_ROOT,
    risk_class: 'R0',
    runtime_binding_id: 'test',
    reparse_verified: true,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    decision: 'ADMIT',
  });
  const v = validateAdmissionToken(token, { operation_id: 'wp.inspect.runtime', site_id: 'fws-0001', logical_target: FIXTURE_ROOT });
  assert(!v.valid, 'wrong operation denied');
});

test('token for another path is denied', () => {
  const token = createAdmissionToken({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FIXTURE_ROOT,
    logical_target: FIXTURE_ROOT,
    physical_target: FIXTURE_ROOT,
    risk_class: 'R0',
    runtime_binding_id: 'test',
    reparse_verified: true,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    decision: 'ADMIT',
  });
  const v = validateAdmissionToken(token, {
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    logical_target: path.join(FIXTURE_ROOT, 'other'),
  });
  assert(!v.valid, 'wrong path denied');
});

test('mutating risk class token is denied', () => {
  const token = createAdmissionToken({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FIXTURE_ROOT,
    logical_target: FIXTURE_ROOT,
    physical_target: FIXTURE_ROOT,
    risk_class: 'R2',
    runtime_binding_id: 'test',
    reparse_verified: true,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    decision: 'ADMIT',
  });
  const v = validateAdmissionToken(token, { operation_id: 'wp.inspect.runtime', site_id: 'fws-0001', logical_target: FIXTURE_ROOT });
  assert(!v.valid, 'R2 denied');
});

test('LOCAL_PROJECT_RUNTIME environment is denied', () => {
  const r = executeRuntimeInspection({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'LOCAL_PROJECT_RUNTIME',
    allowed_root: FWS_ROOT,
    logical_target: FWS_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
  });
  assert(!r.success, 'LOCAL_PROJECT_RUNTIME denied');
});

test('REMOTE_DEV is denied', () => {
  const r = executeRuntimeInspection({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'REMOTE_DEV',
    allowed_root: FWS_ROOT,
    logical_target: FWS_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
  });
  assert(!r.success, 'REMOTE_DEV denied');
});

test('REMOTE_TEST is denied', () => {
  const r = executeRuntimeInspection({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'REMOTE_TEST',
    allowed_root: FWS_ROOT,
    logical_target: FWS_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
  });
  assert(!r.success, 'REMOTE_TEST denied');
});

test('REMOTE_PRODUCTION is denied', () => {
  const r = executeRuntimeInspection({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'REMOTE_PRODUCTION',
    allowed_root: FWS_ROOT,
    logical_target: FWS_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
  });
  assert(!r.success, 'REMOTE_PRODUCTION denied');
});

test('runtime parent instead of site root is denied', () => {
  const r = executeRuntimeInspection({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: 'X:\\MARS-Localhost',
    logical_target: 'X:\\MARS-Localhost',
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
  });
  assert(!r.success, 'parent denied');
});

test('path outside fws-0001 is denied', () => {
  const r = executeRuntimeInspection({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FWS_ROOT,
    logical_target: 'X:\\MARS-Localhost\\sites\\wordpress\\synthetic\\other-site',
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
  });
  assert(!r.success, 'outside path denied');
});

test('legacy E root is rejected by authority', () => {
  const auth = resolveSiteAuthority('fws-0001', 'E:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001');
  assert(!auth.valid, 'E root rejected');
  assert(auth.reason_codes.includes('RT_AUTHORITY_PATH_MISMATCH'), 'path mismatch');
});

test('legacy D root is rejected by authority', () => {
  const auth = resolveSiteAuthority('fws-0001', 'D:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001');
  assert(!auth.valid, 'D root rejected');
  assert(auth.reason_codes.includes('RT_AUTHORITY_PATH_MISMATCH'), 'path mismatch');
});

test('shpigovsky root is not admitted for fws-0001', () => {
  const r = executeRuntimeInspection({
    operation_id: 'wp.inspect.runtime',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: SHPIGOVSKY_ROOT,
    logical_target: SHPIGOVSKY_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
  });
  assert(!r.success, 'shpigovsky denied');
});

test('canonical X root is admitted when path exists', () => {
  const auth = resolveSiteAuthority('fws-0001', FWS_ROOT);
  if (!auth.exists) return;
  assert(auth.valid === true, `X root admitted — ${auth.reason_codes.join(',')}`);
});

test('four-operation allowlist unchanged', () => {
  const proven = [
    'wp.inspect.runtime',
    'wp.inspect.theme',
    'wp.inspect.plugin_state',
    'wp.inspect.routes',
  ];
  for (const op of proven) {
    const b = lookupBinding(op);
    assert(b.allowed === true, `${op} still proven`);
    assert(b.binding.binding_decision === 'BOUND_READ_ONLY_PROVEN', `${op} decision unchanged`);
  }
  const deferred = lookupBinding('wp.validate.database');
  assert(!deferred.allowed, 'deferred ops still blocked');
});

test('kill switch disabled denies', () => {
  const r = executeRuntimeInspection(baseRequest({ kill_switch_state: 'GLOBAL_DISABLED' }));
  assert(!r.success, 'kill switch disabled');
});

test('emergency stop denies', () => {
  const r = executeRuntimeInspection(baseRequest({ kill_switch_state: 'EMERGENCY_STOP' }));
  assert(!r.success, 'emergency stop');
});

test('operation not in binding registry is denied', () => {
  const r = executeRuntimeInspection(baseRequest({ operation_id: 'wp.apply.theme' }));
  assert(!r.success, 'unbound operation denied');
});

test('database operation is deferred not proven', () => {
  const b = lookupBinding('wp.validate.database');
  assert(!b.allowed, 'database deferred');
  assert(b.binding.binding_decision === 'DEFER_DATABASE', 'defer database');
});

test('shell/external-tool operation is deferred', () => {
  const b = lookupBinding('wp.validate.wpcs');
  assert(!b.allowed, 'wpcs deferred');
});

test('baseline mutation detection triggers violation', () => {
  const before = { file_count: 10, directory_count: 5, aggregate_size: 1000, latest_modified_timestamp: '2026-01-01', top_level_entry_names: ['a'], allowlisted_hashes: [] };
  const after = { file_count: 11, directory_count: 5, aggregate_size: 1000, latest_modified_timestamp: '2026-01-01', top_level_entry_names: ['a'], allowlisted_hashes: [], audit_files_created: [] };
  const m = detectMutation(before, after);
  assert(!m.unchanged, 'mutation detected');
  assert(m.verdict === 'FW07C1_READ_ONLY_VIOLATION', 'violation verdict');
});

// --- Positive tests (fixture) ---

test('valid fixture site root with R0 operation', () => {
  const r = executeRuntimeInspection(baseRequest());
  assert(r.success === true, `success — ${JSON.stringify(r.reason_codes)}`);
  assert(r.inspection_result?.status === 'SUCCEEDED', 'inspection succeeded');
});

test('valid path below site root', () => {
  const child = path.join(FIXTURE_ROOT, 'wp-content');
  const r = executeRuntimeInspection(baseRequest({
    logical_target: child,
    allowed_root: FIXTURE_ROOT,
  }));
  assert(r.success === true, `child path success — ${JSON.stringify(r.reason_codes)}`);
});

test('valid short-lived token with fixture adapter', () => {
  const token = createAdmissionToken({
    operation_id: 'wp.inspect.theme',
    site_id: 'fws-0001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: FIXTURE_ROOT,
    logical_target: FIXTURE_ROOT,
    physical_target: FIXTURE_ROOT,
    risk_class: 'R0',
    runtime_binding_id: 'fws-0001-wp-inspect-theme-v1',
    reparse_verified: true,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    decision: 'ADMIT',
  });
  const result = inspectThemeMetadata(FIXTURE_ROOT, token, {
    operation_id: 'wp.inspect.theme',
    site_id: 'fws-0001',
    logical_target: FIXTURE_ROOT,
  });
  assert(result.theme_count >= 1, 'themes found');
});

test('redacted result has no raw secrets', () => {
  const r = executeRuntimeInspection(baseRequest());
  const serialized = JSON.stringify(r);
  assert(!/DB_PASSWORD/i.test(serialized) || /secret_keys_detected/.test(serialized), 'no raw DB_PASSWORD value');
});

test('unchanged before/after baseline on fixture', () => {
  const r = executeRuntimeInspection(baseRequest());
  assert(r.mutation_verdict === 'NO_MUTATION', 'no mutation');
  assert(r.no_write_verdict === true, 'no write');
});

console.log(`\nRuntime binding tests: ${passed} passed, ${failed} failed`);
if (failures.length) {
  for (const f of failures) console.error(`  FAIL: ${f}`);
}
process.exit(failed > 0 ? 1 : 0);
