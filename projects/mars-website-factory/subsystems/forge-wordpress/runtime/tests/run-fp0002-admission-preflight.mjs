#!/usr/bin/env node
/**
 * V9-05C — Live read-only admission preflight for FP-0002 Shpigovsky.
 * Writes receipts under runtime/reports only — never inside WordPress runtime.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { resolveSiteAuthority } from '../src/runtime-authority.mjs';
import { validateReparseBoundary } from '../src/reparse-boundary-validator.mjs';
import { captureBaseline } from '../src/baseline-capture.mjs';
import { detectMutation } from '../src/mutation-detector.mjs';
import { getBindingRegistry } from '../src/runtime-binding-registry.mjs';
import { loadProjectAdmission } from '../src/project-admission-registry.mjs';
import { executeProjectRuntimeInspection, PROJECT_SITE_ID } from '../src/project-runtime-inspection-chain.mjs';
import { verifyWpilotBuild } from '../adapters/wpilot-readonly-adapter.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SHPIGOVSKY_ROOT = 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky';
const RECEIPT_ROOT = path.resolve(__dirname, '../reports/fp0002-v9-05c-admission');

const WPILOT_PROBE_ENDPOINTS = [
  { endpoint: 'ping', auth: false },
  { endpoint: 'site-info', auth: true },
  { endpoint: 'themes', auth: true },
  { endpoint: 'plugins', auth: true },
  { endpoint: 'pages', auth: true },
  { endpoint: 'indexing-state', auth: true },
  { endpoint: 'pages/3', auth: true, label: 'page' },
  { endpoint: 'pages/3/structure', auth: true, label: 'page-structure' },
];

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function writeJson(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

async function probeWpilotEndpoint(base, endpoint, token) {
  const url = `${base.replace(/\/$/, '')}/wp-json/wpilot/v1/${endpoint}`;
  const headers = { Accept: 'application/json' };
  if (token) headers['X-WPilot-Token'] = token;
  const response = await fetch(url, { method: 'GET', headers });
  let body;
  try {
    body = await response.json();
  } catch {
    body = null;
  }
  return {
    endpoint,
    http_status: response.status,
    ok: response.ok && body?.ok !== false,
    write_enabled: body?.data?.bridge?.write_enabled ?? body?.meta?.write_enabled ?? null,
    error_code: body?.error?.code ?? null,
  };
}

async function main() {
  const admission = loadProjectAdmission(PROJECT_SITE_ID);
  const registry = getBindingRegistry(PROJECT_SITE_ID);
  const provenOps = registry.bindings
    .filter((b) => b.binding_decision === 'BOUND_READ_ONLY_PROVEN')
    .map((b) => b.operation_id);

  const summary = {
    phase: 'V9-05C',
    site_id: PROJECT_SITE_ID,
    project_id: 'FP-0002',
    started_at: new Date().toISOString(),
    admission_profile: {
      mode: admission.admission_mode,
      write_authorized: admission.write_authorized,
      allowed_root: admission.allowed_root,
      domain: admission.domain,
    },
    authority: null,
    reparse: null,
    wpilot_pre_admission: null,
    wpilot_build: null,
    operations: [],
    mutation_checks: [],
    verdict: 'PENDING',
  };

  ensureDir(RECEIPT_ROOT);
  ensureDir(path.join(RECEIPT_ROOT, 'receipts'));

  const authority = resolveSiteAuthority(PROJECT_SITE_ID, SHPIGOVSKY_ROOT);
  summary.authority = {
    valid: authority.valid,
    reason_codes: authority.reason_codes,
    resolved_root: authority.resolved_root,
    exists: authority.exists,
  };

  if (!authority.valid || !authority.exists) {
    summary.verdict = 'BLOCKED_BY_RUNTIME_AUTHORITY';
    writeJson(path.join(RECEIPT_ROOT, 'fp0002-admission-preflight-summary.json'), summary);
    console.error('BLOCKED: runtime authority failed');
    process.exit(1);
  }

  const reparse = validateReparseBoundary(SHPIGOVSKY_ROOT, SHPIGOVSKY_ROOT);
  summary.reparse = reparse;
  if (!reparse.allowed || reparse.escape_detected) {
    summary.verdict = 'BLOCKED_BY_REPARSE_BOUNDARY';
    writeJson(path.join(RECEIPT_ROOT, 'fp0002-admission-preflight-summary.json'), summary);
    console.error('BLOCKED: reparse boundary failed');
    process.exit(1);
  }

  summary.wpilot_build = verifyWpilotBuild(SHPIGOVSKY_ROOT);
  if (!summary.wpilot_build.verified) {
    summary.verdict = 'BLOCKED_BY_WPILOT_BUILD_MISMATCH';
    writeJson(path.join(RECEIPT_ROOT, 'fp0002-admission-preflight-summary.json'), summary);
    console.error('BLOCKED: WPilot build fingerprint mismatch');
    process.exit(1);
  }

  let token = null;
  const tokenRef = admission.token_reference;
  if (fs.existsSync(tokenRef)) {
    token = fs.readFileSync(tokenRef, 'utf8').trim();
  }

  const wpilotProbes = [];
  for (const probe of WPILOT_PROBE_ENDPOINTS) {
    const result = await probeWpilotEndpoint(admission.domain, probe.endpoint, probe.auth ? token : null);
    wpilotProbes.push({ ...result, label: probe.label || probe.endpoint });
  }
  const wpilotPassed = wpilotProbes.filter((p) => p.ok).length;
  const writeEnabledUnexpected = wpilotProbes.some((p) => p.write_enabled === true);

  summary.wpilot_pre_admission = {
    endpoints_passed: wpilotPassed,
    endpoints_total: WPILOT_PROBE_ENDPOINTS.length,
    write_enabled_unexpected: writeEnabledUnexpected,
    probes: wpilotProbes.map((p) => ({
      endpoint: p.label || p.endpoint,
      ok: p.ok,
      http_status: p.http_status,
      write_enabled: p.write_enabled,
    })),
  };

  if (wpilotPassed !== 8 || writeEnabledUnexpected) {
    summary.verdict = writeEnabledUnexpected
      ? 'BLOCKED_BY_WPILOT_WRITE_GATE'
      : 'BLOCKED_BY_WPILOT_PRE_ADMISSION';
    writeJson(path.join(RECEIPT_ROOT, 'fp0002-admission-preflight-summary.json'), summary);
    console.error('BLOCKED: WPilot pre-admission failed');
    process.exit(1);
  }

  const globalBaselineBefore = captureBaseline(SHPIGOVSKY_ROOT);
  writeJson(path.join(RECEIPT_ROOT, 'fp0002-mutation-baseline-before.json'), globalBaselineBefore);

  for (const operation_id of provenOps) {
    const opBaselineBefore = captureBaseline(SHPIGOVSKY_ROOT);

    const result = await executeProjectRuntimeInspection({
      operation_id,
      site_id: PROJECT_SITE_ID,
      environment: 'LOCAL_PROJECT',
      allowed_root: SHPIGOVSKY_ROOT,
      logical_target: SHPIGOVSKY_ROOT,
      kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    });

    const opBaselineAfter = captureBaseline(SHPIGOVSKY_ROOT);
    const mutation = detectMutation(opBaselineBefore, opBaselineAfter);

    const receipt = {
      operation_id,
      request: {
        site_id: PROJECT_SITE_ID,
        environment: 'LOCAL_PROJECT',
        allowed_root: SHPIGOVSKY_ROOT,
        kill_switch_state: 'SITE_ENABLED_READ_ONLY',
      },
      admission_decision: result.decision,
      success: result.success,
      runtime_binding_id: result.runtime_binding_id,
      inspection_result: result.inspection_result,
      mutation,
      no_write_verdict: mutation.unchanged && result.success,
    };

    const receiptPath = path.join(RECEIPT_ROOT, 'receipts', `${operation_id.replace(/\./g, '-')}.json`);
    writeJson(receiptPath, receipt);

    summary.operations.push({
      operation_id,
      success: result.success,
      mutation_unchanged: mutation.unchanged,
      no_write_verdict: receipt.no_write_verdict,
    });
    summary.mutation_checks.push(mutation);

    if (!result.success || !mutation.unchanged) {
      summary.verdict = mutation.unchanged ? 'VALIDATION_FAILED' : 'READ_ONLY_VIOLATION';
      writeJson(path.join(RECEIPT_ROOT, 'fp0002-admission-preflight-summary.json'), summary);
      console.error(`FAILED: ${operation_id}`);
      process.exit(1);
    }
  }

  const globalBaselineAfter = captureBaseline(SHPIGOVSKY_ROOT);
  writeJson(path.join(RECEIPT_ROOT, 'fp0002-mutation-baseline-after.json'), globalBaselineAfter);
  const globalMutation = detectMutation(globalBaselineBefore, globalBaselineAfter);
  summary.global_mutation = globalMutation;

  if (!globalMutation.unchanged) {
    summary.verdict = 'READ_ONLY_VIOLATION';
    writeJson(path.join(RECEIPT_ROOT, 'fp0002-admission-preflight-summary.json'), summary);
    console.error('FAILED: global mutation detected');
    process.exit(1);
  }

  summary.verdict = 'PASS';
  summary.completed_at = new Date().toISOString();
  summary.admitted_operations = provenOps.length;
  writeJson(path.join(RECEIPT_ROOT, 'fp0002-admission-preflight-summary.json'), summary);
  console.log(`FP-0002 V9-05C preflight PASS — ${provenOps.length} operations, 0 mutations`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
