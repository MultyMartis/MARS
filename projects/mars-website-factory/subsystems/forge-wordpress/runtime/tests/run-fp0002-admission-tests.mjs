#!/usr/bin/env node
/**
 * V9-05C — FP-0002 project admission unit tests (repo-local, no live WPilot required for negatives).
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { resolveSiteAuthority, RUNTIME_PARENT } from '../src/runtime-authority.mjs';
import { lookupBinding, getBindingRegistry } from '../src/runtime-binding-registry.mjs';
import { loadProjectAdmission } from '../src/project-admission-registry.mjs';
import {
  executeProjectRuntimeInspection,
  isForbiddenWriteEndpoint,
  PROJECT_SITE_ID,
} from '../src/project-runtime-inspection-chain.mjs';
import { validateProjectAdmission } from '../src/project-admission-validator.mjs';

const SHPIGOVSKY_ROOT = 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky';
const FWS_ROOT = 'X:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001';
const PROJECTS_PARENT = 'X:\\MARS-Localhost\\sites\\wordpress\\projects';
const E_ROOT = 'E:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky';

let passed = 0;
let failed = 0;
const failures = [];

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

function test(name, fn) {
  try {
    const result = fn();
    if (result && typeof result.then === 'function') {
      return result
        .then(() => {
          passed++;
        })
        .catch((err) => {
          failed++;
          failures.push(`${name}: ${err.message}`);
        });
    }
    passed++;
  } catch (err) {
    failed++;
    failures.push(`${name}: ${err.message}`);
  }
}

function baseRequest(overrides = {}) {
  return {
    operation_id: 'wp.inspect.site_info',
    site_id: PROJECT_SITE_ID,
    environment: 'LOCAL_PROJECT',
    allowed_root: SHPIGOVSKY_ROOT,
    logical_target: SHPIGOVSKY_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    ...overrides,
  };
}

const tests = [];

tests.push(['exact Shpigovsky X root is registered', () => {
  const auth = resolveSiteAuthority(PROJECT_SITE_ID, SHPIGOVSKY_ROOT);
  assert(auth.site?.admission_mode === 'READ_ONLY', 'read-only mode');
  assert(auth.site?.write_authorized === false, 'writes not authorized');
  if (auth.exists) {
    assert(auth.valid === true, `authority valid — ${auth.reason_codes.join(',')}`);
  }
}]);

tests.push(['sibling project roots are rejected', () => {
  const sibling = 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\other-project';
  const auth = resolveSiteAuthority(PROJECT_SITE_ID, sibling);
  assert(!auth.valid, 'sibling denied');
}]);

tests.push(['parent project directory is rejected', () => {
  const auth = resolveSiteAuthority(PROJECT_SITE_ID, PROJECTS_PARENT);
  assert(!auth.valid, 'parent denied');
  assert(auth.reason_codes.includes('RT_AUTHORITY_PATH_MISMATCH'), 'path mismatch');
}]);

tests.push(['FWS-0001 remains admitted under its own profile', () => {
  const auth = resolveSiteAuthority('fws-0001', FWS_ROOT);
  if (!auth.exists) return;
  assert(auth.valid, 'fws-0001 still valid');
  assert(auth.site.environment === 'LOCAL_SYNTHETIC', 'synthetic env');
}]);

tests.push(['E legacy root is rejected', () => {
  const auth = resolveSiteAuthority(PROJECT_SITE_ID, E_ROOT);
  assert(!auth.valid, 'E root denied');
}]);

tests.push(['D legacy root is rejected', () => {
  const auth = resolveSiteAuthority(PROJECT_SITE_ID, 'D:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky');
  assert(!auth.valid, 'D root denied');
}]);

tests.push(['C legacy root is rejected', () => {
  const auth = resolveSiteAuthority(PROJECT_SITE_ID, 'C:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky');
  assert(!auth.valid, 'C root denied');
}]);

tests.push(['runtime parent is rejected for project site', () => {
  const auth = resolveSiteAuthority(PROJECT_SITE_ID, RUNTIME_PARENT);
  assert(!auth.valid, 'runtime parent denied');
}]);

tests.push(['shpigovsky write operation is rejected', () => {
  const r = validateProjectAdmission({
    operation_id: 'wp.apply.theme',
    site_id: PROJECT_SITE_ID,
    environment: 'LOCAL_PROJECT',
    raw_path: SHPIGOVSKY_ROOT,
    allowed_root: SHPIGOVSKY_ROOT,
    kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    reparse_status: 'VERIFIED',
    runtime_binding_status: 'PROVEN',
  });
  assert(!r.admitted, 'write op denied');
}]);

tests.push(['dry-run mutation endpoint is forbidden', () => {
  assert(isForbiddenWriteEndpoint('pages/3/replace-text/dry-run'), 'dry-run forbidden');
  assert(isForbiddenWriteEndpoint('pages/3/backups'), 'backups forbidden');
  assert(isForbiddenWriteEndpoint('pages/3/scoped-replace'), 'scoped-replace forbidden');
  assert(isForbiddenWriteEndpoint('pages/3/rollback'), 'rollback forbidden');
}]);

tests.push(['token values are not in binding registry', () => {
  const reg = getBindingRegistry(PROJECT_SITE_ID);
  const serialized = JSON.stringify(reg);
  assert(!/wpilot_[a-zA-Z0-9]{20,}/.test(serialized), 'no token in bindings');
  assert(reg.token_reference?.includes('local\\tokens'), 'token is reference path only');
}]);

tests.push(['WPilot build mismatch detection helper', async () => {
  const { verifyWpilotBuild } = await import('../adapters/wpilot-readonly-adapter.mjs');
  const fake = verifyWpilotBuild('X:\\nonexistent');
  assert(fake.verified === false, 'missing plugin fails build check');
}]);

tests.push(['fws-0001 binding registry unchanged', () => {
  const reg = getBindingRegistry('fws-0001');
  assert(reg.site_id === 'fws-0001', 'fws registry id');
  const proven = reg.bindings.filter((b) => b.binding_decision === 'BOUND_READ_ONLY_PROVEN');
  assert(proven.length === 4, 'four proven fws ops unchanged');
}]);

tests.push(['fp-0002 has 11 admitted read-only bindings', () => {
  const reg = getBindingRegistry(PROJECT_SITE_ID);
  const proven = reg.bindings.filter((b) => b.binding_decision === 'BOUND_READ_ONLY_PROVEN');
  assert(proven.length === 11, `expected 11, got ${proven.length}`);
}]);

tests.push(['LOCAL_PROJECT denied for fws-0001 operations', () => {
  const b = lookupBinding('wp.inspect.runtime', 'fws-0001');
  assert(b.found, 'fws binding exists');
}]);

tests.push(['admission profile is READ_ONLY', () => {
  const profile = loadProjectAdmission(PROJECT_SITE_ID);
  assert(profile.admission_mode === 'READ_ONLY', 'read only');
  assert(profile.write_authorized === false, 'no writes');
  assert(profile.control_bridge_build === 'v0.3.0-rc5', 'rc5 build');
}]);

tests.push(['unregistered operation denied for project', async () => {
  const r = await executeProjectRuntimeInspection(baseRequest({ operation_id: 'wp.mutate.pages' }));
  assert(!r.success, 'unregistered denied');
}]);

tests.push(['LOCAL_SYNTHETIC environment denied for project chain', async () => {
  const r = await executeProjectRuntimeInspection(baseRequest({ environment: 'LOCAL_SYNTHETIC' }));
  assert(!r.success, 'wrong env denied');
}]);

async function runAll() {
  for (const [name, fn] of tests) {
    await test(name, fn);
  }

  console.log(`\nFP-0002 admission tests: ${passed} passed, ${failed} failed`);
  if (failures.length) {
    for (const f of failures) console.error(`  FAIL: ${f}`);
  }
  process.exit(failed > 0 ? 1 : 0);
}

runAll();
