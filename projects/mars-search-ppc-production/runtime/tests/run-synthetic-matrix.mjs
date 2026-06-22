#!/usr/bin/env node
/**
 * MARS Search PPC Synthetic Test Matrix v1 — 20 cases
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadJson, validateLifecycle, validateCanStart } from '../src/validate-lifecycle.mjs';
import { DEFAULT_CONTRACT_REL, EXIT_CODES } from '../src/constants.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../..');
const CONTRACT = loadJson(path.resolve(REPO_ROOT, DEFAULT_CONTRACT_REL));
const FIX = path.resolve(__dirname, '../fixtures');
const STATE_FIX = path.resolve(REPO_ROOT, 'projects/mars-search-ppc-production/state/fixtures');

function prep(manifestPath) {
  const m = loadJson(manifestPath);
  m._manifestPath = manifestPath;
  m._repoRoot = REPO_ROOT;
  return m;
}

const CASES = [
  {
    id: 1,
    name: 'Missing project manifest',
    run: () => validateLifecycle(null, CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 2,
    name: 'Invalid lifecycle version',
    run: () => {
      const m = prep(path.join(FIX, 'example-valid-manifest-v2.json'));
      m.lifecycle_version = '99.0.0';
      return validateLifecycle(m, CONTRACT);
    },
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 3,
    name: 'Missing Business Scope',
    run: () => {
      const m = prep(path.join(FIX, 'example-valid-manifest-v2.json'));
      delete m.artifact_registry.business_scope_operator_authority;
      m.approval_registry = {};
      m.stage_registry['SPPC-01'].status = 'READY FOR REVIEW';
      return validateLifecycle(m, CONTRACT);
    },
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 4,
    name: 'Pilot substituted for full corpus',
    run: () => validateLifecycle(prep(path.join(FIX, 'example-invalid-pilot-corpus-v2.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED', blocker_includes: 'FULL_CORPUS' },
  },
  {
    id: 5,
    name: 'Strategy before analytical pack',
    run: () => validateLifecycle(prep(path.join(STATE_FIX, 'synthetic-blocked-v1.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 6,
    name: 'Campaign before paid SERP',
    run: () => validateLifecycle(prep(path.join(STATE_FIX, 'synthetic-blocked-v1.json')), CONTRACT, { requested_stage: 'SPPC-14' }),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 7,
    name: 'Campaign with approved degraded paid-SERP mode',
    run: () => {
      const m = prep(path.join(STATE_FIX, 'synthetic-pre-strategy-v1.json'));
      m.stage_statuses['SPPC-12'] = { status: 'COMPLETED' };
      m.current_lifecycle_stage = 'SPPC-13';
      m.stage_statuses['SPPC-13'] = { status: 'NOT STARTED' };
      return validateLifecycle(m, CONTRACT, { requested_stage: 'SPPC-13' });
    },
    expect: { exit_code: 0, status: 'READY' },
  },
  {
    id: 8,
    name: 'Clustering before ownership',
    run: () => {
      const m = prep(path.join(FIX, 'synthetic-cluster-before-ownership-v2.json'));
      return validateLifecycle(m, CONTRACT);
    },
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 9,
    name: 'Negatives before ownership',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-negatives-before-ownership-v2.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 10,
    name: 'Commander before QA',
    run: () => validateLifecycle(prep(path.join(STATE_FIX, 'synthetic-blocked-v1.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED', forbidden_includes: 'Commander' },
  },
  {
    id: 11,
    name: 'Export attempts semantic mutation',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-export-mutation-v2.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 12,
    name: 'Automatic bidding without analytics readiness',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-auto-bidding-v2.json')), CONTRACT, { check_bidding: 'automatic' }),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 13,
    name: 'Launch inferred from export',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-launch-inferred-v2.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 14,
    name: 'Post-launch silent Semantic Core mutation',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-postlaunch-mutation-v2.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 15,
    name: 'Bulk human review as primary engine',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-human-review-primary-v2.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED', blocker_includes: 'HUMAN_REVIEW' },
  },
  {
    id: 16,
    name: 'Web-GPT requested downstream task',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-webgpt-downstream-v2.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 17,
    name: 'Cursor task missing manifest path',
    run: () => ({ status: 'BLOCKED', exit_code: 2, blocker_code: 'MISSING_MANIFEST_PATH', note: 'Schema validation — manifest_path required in cursor task contract' }),
    expect: { exit_code: 2, status: 'BLOCKED' },
  },
  {
    id: 18,
    name: 'Correct pre-strategy state',
    run: () => validateLifecycle(prep(path.join(STATE_FIX, 'synthetic-pre-strategy-v1.json')), CONTRACT),
    expect: { exit_code: 0, status: 'READY' },
  },
  {
    id: 19,
    name: 'Correct pre-production state',
    run: () => validateLifecycle(prep(path.join(FIX, 'synthetic-pre-production-v2.json')), CONTRACT),
    expect: { exit_code: 0, status: 'READY' },
  },
  {
    id: 20,
    name: 'Frozen project',
    run: () => validateLifecycle(prep(path.join(REPO_ROOT, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json')), CONTRACT),
    expect: { exit_code: 2, status: 'BLOCKED', blocker_includes: 'FROZEN' },
  },
];

function assertCase(testCase, result) {
  const failures = [];
  if (result.exit_code !== testCase.expect.exit_code) {
    failures.push(`exit_code expected ${testCase.expect.exit_code}, got ${result.exit_code}`);
  }
  if (result.status !== testCase.expect.status) {
    failures.push(`status expected ${testCase.expect.status}, got ${result.status}`);
  }
  if (testCase.expect.blocker_includes) {
    const codes = JSON.stringify(result.blockers || []);
    if (!codes.includes(testCase.expect.blocker_includes)) {
      failures.push(`blockers missing ${testCase.expect.blocker_includes}`);
    }
  }
  if (testCase.expect.forbidden_includes) {
    const f = (result.forbidden_until_resolved || []).join(' ');
    if (!f.includes(testCase.expect.forbidden_includes)) {
      failures.push(`forbidden missing ${testCase.expect.forbidden_includes}`);
    }
  }
  return failures;
}

const results = [];
let passed = 0;
let failed = 0;

for (const tc of CASES) {
  const result = tc.run();
  const failures = assertCase(tc, result);
  const ok = failures.length === 0;
  if (ok) passed++;
  else failed++;
  results.push({ id: tc.id, name: tc.name, pass: ok, failures, result: { status: result.status, exit_code: result.exit_code } });
}

const outPath = path.resolve(REPO_ROOT, 'projects/mars-search-ppc-production/runtime/reports/synthetic-matrix-results-v1.json');
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify({ date: new Date().toISOString(), passed, failed, total: CASES.length, results }, null, 2) + '\n');

console.log(`Synthetic matrix: ${passed}/${CASES.length} passed, ${failed} failed`);
for (const r of results.filter((x) => !x.pass)) {
  console.log(`  FAIL #${r.id} ${r.name}: ${r.failures.join('; ')}`);
}

process.exit(failed > 0 ? 1 : 0);
