#!/usr/bin/env node
/**
 * FW-07C-1 — Actual runtime read-only preflight for fws-0001.
 * Writes receipts to external control path only — never inside runtime.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { resolveSiteAuthority } from '../src/runtime-authority.mjs';
import { validateReparseBoundary } from '../src/reparse-boundary-validator.mjs';
import { captureBaseline } from '../src/baseline-capture.mjs';
import { executeRuntimeInspection } from '../src/runtime-inspection-chain.mjs';
import { detectMutation } from '../src/mutation-detector.mjs';
import { getBindingRegistry } from '../src/runtime-binding-registry.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FWS_ROOT = 'E:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001';
const RECEIPT_ROOT = 'C:\\MARS Phenix\\_reconstruction-control\\fw07c1-runtime-preflight';

const PROVEN_OPERATIONS = [
  'wp.inspect.runtime',
  'wp.inspect.theme',
  'wp.inspect.plugin_state',
  'wp.inspect.routes',
];

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function writeJson(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

function main() {
  const summary = {
    phase: 'FW-07C-1',
    site_id: 'fws-0001',
    started_at: new Date().toISOString(),
    authority: null,
    reparse: null,
    operations: [],
    mutation_checks: [],
    verdict: 'PENDING',
  };

  ensureDir(RECEIPT_ROOT);
  ensureDir(path.join(RECEIPT_ROOT, 'receipts'));

  const authority = resolveSiteAuthority('fws-0001');
  summary.authority = authority;
  if (!authority.valid || !authority.exists) {
    summary.verdict = 'FW07C1_BLOCKED_BY_RUNTIME_AUTHORITY';
    writeJson(path.join(RECEIPT_ROOT, 'fw07c1-runtime-preflight-summary.json'), summary);
    console.error('BLOCKED: runtime authority failed');
    process.exit(1);
  }

  const reparse = validateReparseBoundary(FWS_ROOT, FWS_ROOT);
  summary.reparse = reparse;
  if (!reparse.allowed || reparse.escape_detected) {
    summary.verdict = 'FW07C1_BLOCKED_BY_REPARSE_BOUNDARY';
    writeJson(path.join(RECEIPT_ROOT, 'fw07c1-runtime-preflight-summary.json'), summary);
    console.error('BLOCKED: reparse boundary failed');
    process.exit(1);
  }

  const globalBaselineBefore = captureBaseline(FWS_ROOT);

  for (const operation_id of PROVEN_OPERATIONS) {
    const opBaselineBefore = captureBaseline(FWS_ROOT);

    const result = executeRuntimeInspection({
      operation_id,
      site_id: 'fws-0001',
      environment: 'LOCAL_SYNTHETIC',
      allowed_root: FWS_ROOT,
      logical_target: FWS_ROOT,
      kill_switch_state: 'SITE_ENABLED_READ_ONLY',
    });

    const opBaselineAfter = captureBaseline(FWS_ROOT);
    const mutation = detectMutation(opBaselineBefore, opBaselineAfter);

    const receipt = {
      operation_id,
      request: {
        site_id: 'fws-0001',
        environment: 'LOCAL_SYNTHETIC',
        allowed_root: FWS_ROOT,
        kill_switch_state: 'SITE_ENABLED_READ_ONLY',
      },
      admission_decision: result.decision,
      success: result.success,
      runtime_binding_id: result.runtime_binding_id,
      reparse: result.reparse,
      inspection_result: result.inspection_result,
      baseline_before: result.baseline_before,
      baseline_after: result.baseline_after,
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
      summary.verdict = mutation.unchanged ? 'FW07C1_VALIDATION_FAILED' : 'FW07C1_READ_ONLY_VIOLATION';
      writeJson(path.join(RECEIPT_ROOT, 'fw07c1-runtime-preflight-summary.json'), summary);
      console.error(`FAILED: ${operation_id}`);
      process.exit(1);
    }
  }

  const globalBaselineAfter = captureBaseline(FWS_ROOT);
  const globalMutation = detectMutation(globalBaselineBefore, globalBaselineAfter);

  summary.global_mutation = globalMutation;
  summary.completed_at = new Date().toISOString();
  summary.verdict = globalMutation.unchanged
    ? 'FW07C1_SYNTHETIC_READ_ONLY_VALIDATED'
    : 'FW07C1_READ_ONLY_VIOLATION';

  const registry = getBindingRegistry();
  writeJson(path.join(RECEIPT_ROOT, 'fw07c1-runtime-preflight-summary.json'), summary);
  writeJson(path.join(RECEIPT_ROOT, 'fw07c1-runtime-baseline.json'), {
    before: globalBaselineBefore,
    after: globalBaselineAfter,
    mutation: globalMutation,
  });

  console.log(JSON.stringify(summary, null, 2));
  process.exit(globalMutation.unchanged ? 0 : 1);
}

main();
