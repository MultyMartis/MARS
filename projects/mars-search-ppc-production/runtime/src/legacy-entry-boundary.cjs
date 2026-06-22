/**
 * CommonJS bridge for legacy entry-point boundary (Wave 1.2).
 */
'use strict';

const BLOCKER_CODE = 'LEGACY_ENTRY_POINT_REQUIRES_LIFECYCLE_GATE';
const BLOCKER_MESSAGE = 'BLOCKED — LEGACY SEARCH PPC ENTRY POINT REQUIRES LIFECYCLE GATE';
const LIFECYCLE_AUTH_ENV = 'MARS_SEARCH_PPC_LIFECYCLE_AUTHORIZED';
const DIAGNOSTIC_ENV = 'MARS_SEARCH_PPC_DIAGNOSTIC';

const GATED_REPLACEMENTS = {
  'mig-run-session': {
    command: 'node projects/mig/tools/run-ppc-gated-session.mjs',
    manifest: '--manifest <project-ppc-state-manifest>',
    stage: '--stage <SPPC stage>',
    action: '--action <source_registration|corpus_intake|normalization|paid_serp|competitor_audit>',
  },
  'triumph-export': {
    command: 'node projects/orca/ppc/triumph-manipulator/tools/run-ppc-gated-export.mjs',
    manifest: '--manifest <project-ppc-state-manifest>',
    stage: '--stage SPPC-20',
    action: '--action commander_export',
  },
};

function isLifecycleAuthorized() {
  return process.env[LIFECYCLE_AUTH_ENV] === '1';
}

function isDiagnosticContext(argv) {
  argv = argv || process.argv;
  if (process.env[DIAGNOSTIC_ENV] === '1') return true;
  return argv.includes('--diagnostic') || argv.includes('--internal-verify');
}

function isSearchPpcMigBody(body) {
  if (!body || typeof body !== 'object') return false;
  if (body.mars_search_ppc === true || body.search_ppc === true) return true;
  if (body.project_ppc_manifest || body.ppc_manifest_path || body.ppc_state_manifest) return true;
  if (body.workflow === 'search-ppc' || body.workflow === 'mars-search-ppc') return true;
  if (body.intake?.project_type === 'search_ppc' || body.intake?.mars_program === 'search-ppc') {
    return true;
  }
  return false;
}

function formatMigrationGuidance(replacementKey) {
  const r = GATED_REPLACEMENTS[replacementKey];
  if (!r) {
    return 'Use:\nnode projects/mars-search-ppc-production/runtime/cli/search-ppc-gate.mjs';
  }
  return `Use:\n${r.command}\n\nRequired:\n${r.manifest}\n${r.stage}\n${r.action}`;
}

function enforceLegacyBoundary(params) {
  const diagnosticAllowed = params.diagnosticAllowed !== false;
  const isDiagnostic = params.isDiagnostic != null ? params.isDiagnostic : isDiagnosticContext();

  if (isLifecycleAuthorized()) {
    return { allowed: true, mode: 'lifecycle_authorized' };
  }
  if (diagnosticAllowed && isDiagnostic) {
    return { allowed: true, mode: 'diagnostic', output_class: 'diagnostic' };
  }
  if (params.searchPpcMode === false) {
    return { allowed: true, mode: 'non_search_ppc' };
  }

  return {
    allowed: false,
    mode: 'blocked',
    status: 'BLOCKED',
    blocker_code: BLOCKER_CODE,
    blocker_message: BLOCKER_MESSAGE,
    migration: formatMigrationGuidance(params.replacementKey),
    exit_code: 2,
  };
}

function emitLegacyBlock(result) {
  const payload = {
    status: 'BLOCKED',
    blocker_code: result.blocker_code,
    message: result.blocker_message,
    migration: result.migration,
  };
  console.error(JSON.stringify(payload, null, 2));
  console.error(`\n${result.blocker_message}\n\n${result.migration}\n`);
}

module.exports = {
  LEGACY_BLOCKER_CODE: BLOCKER_CODE,
  LEGACY_BLOCKER_MESSAGE: BLOCKER_MESSAGE,
  LIFECYCLE_AUTH_ENV,
  DIAGNOSTIC_ENV,
  isLifecycleAuthorized,
  isDiagnosticContext,
  isSearchPpcMigBody,
  enforceLegacyBoundary,
  emitLegacyBlock,
  formatMigrationGuidance,
};
