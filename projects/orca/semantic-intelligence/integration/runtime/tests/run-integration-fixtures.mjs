#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadContracts } from '../src/contract-loader.mjs';
import { buildConsumptionReport } from '../src/consumption-report.mjs';
import { runAdmissionIntegration } from '../src/admission-orchestrator.mjs';
import { ensureDir, readJson, RUNTIME_ROOT, writeJson } from '../src/lib.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURE_ROOT = path.join(RUNTIME_ROOT, 'fixtures/integration');
const LOCK_GOOD = path.join(RUNTIME_ROOT, 'config/orca-semantic-contract-runtime-lock-v1.json');
const REPORT_PATH = path.join(RUNTIME_ROOT, 'reports/integration-fixture-run-v1.json');

function listJson(dir) {
  return fs.readdirSync(dir).filter((f) => f.endsWith('.json')).map((f) => path.join(dir, f));
}

function assertExpect(result, expect, fixture) {
  const errors = [];
  if (expect.ok !== undefined && result.ok !== expect.ok) errors.push(`ok expected ${expect.ok} got ${result.ok}`);
  if (expect.blocked !== undefined && result.blocked !== expect.blocked) errors.push(`blocked expected ${expect.blocked} got ${result.blocked}`);
  if (expect.admission_decision && result.admission_decision !== expect.admission_decision) {
    errors.push(`decision expected ${expect.admission_decision} got ${result.admission_decision}`);
  }
  if (expect.review_routed !== undefined && Boolean(result.routing?.routed) !== expect.review_routed) {
    errors.push(`review_routed expected ${expect.review_routed} got ${result.routing?.routed}`);
  }
  if (expect.invariant) {
    const codes = (result.validation?.findings || []).map((f) => f.invariant_id);
    if (!codes.includes(expect.invariant)) errors.push(`missing invariant ${expect.invariant}`);
  }
  if (expect.legacy_comparison_present && !result.diagnostic_comparison) errors.push('missing diagnostic_comparison');
  if (expect.legacy_not_authoritative && result.diagnostic_comparison?.authority !== 'DIAGNOSTIC ONLY — NOT SEMANTIC AUTHORITY') {
    errors.push('legacy comparison missing diagnostic authority marker');
  }
  if (expect.legacy_rejected && result.ok) errors.push('legacy label should block');
  return errors;
}

function run() {
  const results = [];
  let passed = 0;
  let failed = 0;

  // Contract failure cases
  const contractCases = [
    { id: 'int-neg-001-missing-contract', lock: path.join(RUNTIME_ROOT, 'fixtures/contracts/lock-missing-contract-v1.json'), expectBlocked: true, message: 'NOT LOADED' },
    { id: 'int-neg-002-checksum-mismatch', lock: path.join(RUNTIME_ROOT, 'fixtures/contracts/lock-checksum-mismatch-v1.json'), expectBlocked: true, message: 'CHECKSUM' },
    { id: 'int-neg-003-version-mismatch', lock: path.join(RUNTIME_ROOT, 'fixtures/contracts/lock-version-mismatch-v1.json'), expectBlocked: true, message: 'VERSION' },
    { id: 'int-pos-009-consumption-report', lock: LOCK_GOOD, expectBlocked: false, consumption: true },
  ];

  for (const c of contractCases) {
    const load = loadContracts({ lockPath: c.lock });
    const report = buildConsumptionReport(load, { command: 'integration-fixture-suite' });
    let ok = c.expectBlocked ? load.blocked : load.ok;
    if (c.consumption) ok = load.ok && report.contracts.every((e) => e.load_status === 'LOADED AND CONSUMED' || e.load_status === 'OPTIONAL — NOT LOADED');
    if (c.message && load.blocked) {
      const msg = load.message || '';
      const evidenceStr = JSON.stringify(load.evidence || []);
      if (!msg.includes(c.message) && !evidenceStr.includes(c.message)) ok = false;
    }
    results.push({ case_id: c.id, type: 'contract', ok, load_blocked: load.blocked, message: load.message });
    ok ? passed++ : failed++;
  }

  for (const file of listJson(path.join(FIXTURE_ROOT, 'positive'))) {
    const fixture = readJson(file);
    const result = runAdmissionIntegration(fixture, { lockPath: LOCK_GOOD });
    const errors = assertExpect(result, fixture.expect || {}, fixture);
    const ok = errors.length === 0;
    results.push({ case_id: fixture.fixture_id, type: 'positive', ok, errors, file });
    ok ? passed++ : failed++;
  }

  for (const file of listJson(path.join(FIXTURE_ROOT, 'negative'))) {
    const fixture = readJson(file);
    const result = runAdmissionIntegration(fixture, { lockPath: LOCK_GOOD });
    const errors = assertExpect(result, fixture.expect || { ok: false, blocked: true }, fixture);
    const ok = errors.length === 0;
    results.push({ case_id: fixture.fixture_id, type: 'negative', ok, errors, file });
    ok ? passed++ : failed++;
  }

  const summary = {
    run_id: 'integration-fixture-run-v1',
    generated_at: new Date().toISOString(),
    total: results.length,
    passed,
    failed,
    exit_code: failed ? 1 : 0,
    results,
    note: 'INTEGRATION TEST FIXTURES — NOT GOLD LABELS',
  };

  ensureDir(path.dirname(REPORT_PATH));
  writeJson(REPORT_PATH, summary);
  console.log(JSON.stringify({ total: summary.total, passed, failed, report: REPORT_PATH }, null, 2));
  process.exit(summary.exit_code);
}

run();
