/**
 * MARS Search PPC — Legacy Entry-Point Boundary (Wave 1.2)
 * Fail-closed guard for executable legacy CLIs without lifecycle authorization.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createExecutionReceipt, writeExecutionReceipt } from './execution-receipt.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const LEGACY_BLOCKER_CODE = 'LEGACY_ENTRY_POINT_REQUIRES_LIFECYCLE_GATE';
export const LEGACY_BLOCKER_MESSAGE =
  'BLOCKED — LEGACY SEARCH PPC ENTRY POINT REQUIRES LIFECYCLE GATE';

export const LIFECYCLE_AUTH_ENV = 'MARS_SEARCH_PPC_LIFECYCLE_AUTHORIZED';
export const DIAGNOSTIC_ENV = 'MARS_SEARCH_PPC_DIAGNOSTIC';

export const GATED_REPLACEMENTS = {
  'mig-run-session': {
    command: 'node projects/mig/tools/run-ppc-gated-session.mjs',
    manifest: '--manifest <project-ppc-state-manifest>',
    stage: '--stage <SPPC stage>',
    action: '--action <source_registration|corpus_intake|normalization|paid_serp|competitor_audit>',
  },
  'orca-admission': {
    command: 'node projects/orca/semantic-intelligence/integration/runtime/cli/orca-ppc-gate.mjs',
    manifest: '--manifest <project-ppc-state-manifest>',
    stage: '--stage SPPC-05',
    action: '--action <admission|demand_tiers|ownership|clustering|negatives>',
  },
  'triumph-export': {
    command: 'node projects/orca/ppc/triumph-manipulator/tools/run-ppc-gated-export.mjs',
    manifest: '--manifest <project-ppc-state-manifest>',
    stage: '--stage SPPC-20',
    action: '--action commander_export',
  },
};

export function isLifecycleAuthorized() {
  return process.env[LIFECYCLE_AUTH_ENV] === '1';
}

export function isDiagnosticContext(argv = process.argv) {
  if (process.env[DIAGNOSTIC_ENV] === '1') return true;
  return argv.includes('--diagnostic') || argv.includes('--internal-verify');
}

export function isSearchPpcMigBody(body) {
  if (!body || typeof body !== 'object') return false;
  if (body.mars_search_ppc === true || body.search_ppc === true) return true;
  if (body.project_ppc_manifest || body.ppc_manifest_path || body.ppc_state_manifest) return true;
  if (body.workflow === 'search-ppc' || body.workflow === 'mars-search-ppc') return true;
  if (body.intake?.project_type === 'search_ppc' || body.intake?.mars_program === 'search-ppc') {
    return true;
  }
  return false;
}

export function formatMigrationGuidance(replacementKey) {
  const r = GATED_REPLACEMENTS[replacementKey];
  if (!r) {
    return `Use:\nnode projects/mars-search-ppc-production/runtime/cli/search-ppc-gate.mjs\n\nRequired:\n--manifest <project-ppc-state-manifest>\n--stage <SPPC stage>\n--action <registered action>`;
  }
  return (
    `Use:\n${r.command}\n\nRequired:\n${r.manifest}\n${r.stage}\n${r.action}`
  );
}

/**
 * @param {object} params
 * @param {string} params.entryPointId
 * @param {string} params.replacementKey
 * @param {string} [params.tool]
 * @param {string} [params.requestedAction]
 * @param {string} [params.requestedStage]
 * @param {boolean} [params.searchPpcMode]
 * @param {boolean} [params.diagnosticAllowed]
 * @param {boolean} [params.isDiagnostic]
 * @param {string} [params.receiptDir]
 * @param {string} [params.command]
 */
export function enforceLegacyBoundary(params) {
  const diagnosticAllowed = params.diagnosticAllowed !== false;
  const isDiagnostic = params.isDiagnostic ?? isDiagnosticContext();

  if (isLifecycleAuthorized()) {
    return { allowed: true, mode: 'lifecycle_authorized' };
  }

  if (diagnosticAllowed && isDiagnostic) {
    return { allowed: true, mode: 'diagnostic', output_class: 'diagnostic' };
  }

  if (params.searchPpcMode === false) {
    return { allowed: true, mode: 'non_search_ppc' };
  }

  const blockers = [
    {
      code: LEGACY_BLOCKER_CODE,
      message: LEGACY_BLOCKER_MESSAGE,
    },
  ];

  const receipt = createExecutionReceipt({
    project_id: 'UNKNOWN',
    manifest_path: null,
    manifest_checksum: null,
    lifecycle_version: null,
    requested_stage: params.requestedStage || null,
    requested_action: params.requestedAction || params.entryPointId,
    actor: 'legacy-cli',
    tool: params.tool || params.entryPointId,
    authorization_result: 'BLOCKED',
    blockers,
    expected_outputs: [],
    runtime_version: 'wave1.2-v1',
    source_commit: null,
    command: params.command || params.entryPointId,
    note: 'Legacy entry point invoked without lifecycle gate',
  });

  let receiptPath = null;
  const receiptDir =
    params.receiptDir ||
    path.resolve(__dirname, '../receipts/legacy-blocked');
  try {
    receiptPath = writeExecutionReceipt(receipt, receiptDir);
  } catch {
    receiptPath = null;
  }

  return {
    allowed: false,
    mode: 'blocked',
    status: 'BLOCKED',
    blocker_code: LEGACY_BLOCKER_CODE,
    blocker_message: LEGACY_BLOCKER_MESSAGE,
    migration: formatMigrationGuidance(params.replacementKey),
    evidence_record: receipt,
    receipt_path: receiptPath,
    exit_code: 2,
  };
}

export function emitLegacyBlock(result) {
  const payload = {
    status: 'BLOCKED',
    blocker_code: result.blocker_code,
    message: result.blocker_message,
    migration: result.migration,
    receipt_path: result.receipt_path,
  };
  console.error(JSON.stringify(payload, null, 2));
  console.error(`\n${result.blocker_message}\n\n${result.migration}\n`);
}
