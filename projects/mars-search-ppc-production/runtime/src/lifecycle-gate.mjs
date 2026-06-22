/**
 * MARS Search PPC — Canonical Lifecycle Gate API (Wave 1.1)
 * Single reusable authorization surface for all subsystem entry points.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { loadJson, validateLifecycle } from './validate-lifecycle.mjs';
import { DEFAULT_CONTRACT_REL, EXIT_CODES, STAGE_ORDER } from './constants.mjs';
import { normalizeManifest, getStageStatus } from './manifest-normalize.mjs';
import { validateOutputClass } from './output-class-registry.mjs';
import { createExecutionReceipt, writeExecutionReceipt } from './execution-receipt.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const RUNTIME_VERSION = 'wave1.1-v1';

const STAGE_ACTION_MAP = {
  'SPPC-02': ['source_registration', 'register_source'],
  'SPPC-03': ['corpus_intake', 'full_corpus_intake'],
  'SPPC-04': ['normalization', 'canonical_registry'],
  'SPPC-05': ['admission', 'commercial_admission', 'production_admission'],
  'SPPC-06': ['demand_tiers', 'tier_segmentation'],
  'SPPC-07': ['ownership', 'service_ownership'],
  'SPPC-08': ['clustering', 'semantic_clustering'],
  'SPPC-09': ['negatives', 'negative_intelligence'],
  'SPPC-10': ['paid_serp', 'paid_serp_collection'],
  'SPPC-11': ['competitor_audit', 'competitor_advertising_audit'],
  'SPPC-12': ['analytical_pack', 'dated_analytical_pack'],
  'SPPC-13': ['strategy', 'ppc_strategy'],
  'SPPC-14': ['campaign_architecture'],
  'SPPC-15': ['keyword_distribution'],
  'SPPC-16': ['ad_production'],
  'SPPC-17': ['landing_alignment'],
  'SPPC-18': ['bidding_budget'],
  'SPPC-19': ['campaign_qa'],
  'SPPC-20': ['commander_export', 'export'],
  'SPPC-21': ['launch'],
  'SPPC-22': ['post_launch_learning'],
  'SPPC-23': ['governance_review'],
};

const READ_ONLY_ACTIONS = new Set([
  'source_inspection',
  'manifest_status',
  'lifecycle_status',
  'read_only_inspection',
  'diagnostic_read',
]);

function resolveRepoRoot(options) {
  return options.repoRoot || path.resolve(__dirname, '../../../../');
}

function resolveContractPath(options, repoRoot) {
  return options.contractPath || path.resolve(repoRoot, DEFAULT_CONTRACT_REL);
}

function sha256File(filePath) {
  if (!filePath || !fs.existsSync(filePath)) return null;
  const buf = fs.readFileSync(filePath);
  return crypto.createHash('sha256').update(buf).digest('hex');
}

function sourceCommit(repoRoot) {
  try {
    return execSync('git rev-parse --short HEAD', { cwd: repoRoot, encoding: 'utf8' }).trim();
  } catch {
    return 'SAFE UNKNOWN';
  }
}

function actionMatchesStage(requestedAction, stageId) {
  const aliases = STAGE_ACTION_MAP[stageId] || [];
  const norm = String(requestedAction || '').toLowerCase().replace(/[\s-]+/g, '_');
  if (norm === stageId.toLowerCase()) return true;
  return aliases.some((a) => norm === a || norm.includes(a));
}

function resolveStageForAction(requestedStage, requestedAction) {
  if (requestedStage && STAGE_ORDER.includes(requestedStage)) return requestedStage;
  const norm = String(requestedAction || '').toLowerCase().replace(/[\s-]+/g, '_');
  for (const [stageId, aliases] of Object.entries(STAGE_ACTION_MAP)) {
    if (norm === stageId.toLowerCase() || aliases.some((a) => norm === a || norm.includes(a))) {
      return stageId;
    }
  }
  return requestedStage || null;
}

function checkForbiddenOutputs(expectedOutputs, manifest, contract, repoRoot, requestedStage) {
  const violations = [];
  for (const out of expectedOutputs || []) {
    const cls = out.output_class || out.class;
    if (cls) {
      const v = validateOutputClass(out.artifact_type || out.type, cls, { requestedStage });
      if (!v.allowed) violations.push(v);
    }
    if (out.forbidden === true) {
      violations.push({ artifact: out.artifact_type || out.type, reason: 'explicitly forbidden output' });
    }
  }
  return violations;
}

/**
 * @param {object} params
 * @param {string} params.manifestPath
 * @param {string} [params.requestedStage]
 * @param {string} params.requestedAction
 * @param {string} [params.actor]
 * @param {string} [params.tool]
 * @param {object[]} [params.expectedOutputs]
 * @param {string} [params.command]
 * @param {boolean} [params.writeReceipt]
 * @param {string} [params.receiptDir]
 */
export function authorizeAction(params) {
  const repoRoot = resolveRepoRoot(params);
  const contractPath = resolveContractPath(params, repoRoot);
  const requestedStage = resolveStageForAction(params.requestedStage, params.requestedAction);
  const isReadOnly = READ_ONLY_ACTIONS.has(String(params.requestedAction || '').toLowerCase().replace(/[\s-]+/g, '_'));

  if (!params.manifestPath) {
    const receipt = createExecutionReceipt({
      project_id: 'UNKNOWN',
      manifest_path: null,
      manifest_checksum: null,
      lifecycle_version: null,
      requested_stage: requestedStage,
      requested_action: params.requestedAction,
      actor: params.actor,
      tool: params.tool,
      authorization_result: 'BLOCKED',
      blockers: [{ code: 'MISSING_MANIFEST', message: 'BLOCKED — LIFECYCLE REQUIREMENT NOT MET' }],
      expected_outputs: params.expectedOutputs,
      runtime_version: RUNTIME_VERSION,
      source_commit: sourceCommit(repoRoot),
      command: params.command,
    });
    if (params.writeReceipt !== false && params.receiptDir) {
      writeExecutionReceipt(receipt, params.receiptDir);
    }
    return {
      allowed: false,
      status: 'BLOCKED',
      project_id: null,
      current_stage: null,
      requested_stage: requestedStage,
      requested_action: params.requestedAction,
      blockers: receipt.blockers,
      missing_inputs: ['manifest'],
      invalid_evidence: [],
      allowed_next_actions: [],
      forbidden_actions: [],
      evidence_record: receipt,
      exit_code: EXIT_CODES.BLOCKED,
    };
  }

  const manifestPath = path.resolve(params.manifestPath);
  if (!fs.existsSync(manifestPath)) {
    const receipt = createExecutionReceipt({
      project_id: 'UNKNOWN',
      manifest_path: manifestPath,
      manifest_checksum: null,
      lifecycle_version: null,
      requested_stage: requestedStage,
      requested_action: params.requestedAction,
      actor: params.actor,
      tool: params.tool,
      authorization_result: 'BLOCKED',
      blockers: [{ code: 'MISSING_MANIFEST', message: 'Manifest file not found' }],
      expected_outputs: params.expectedOutputs,
      runtime_version: RUNTIME_VERSION,
      source_commit: sourceCommit(repoRoot),
      command: params.command,
    });
    if (params.writeReceipt !== false && params.receiptDir) {
      writeExecutionReceipt(receipt, params.receiptDir);
    }
    return {
      allowed: false,
      status: 'BLOCKED',
      project_id: null,
      current_stage: null,
      requested_stage: requestedStage,
      requested_action: params.requestedAction,
      blockers: receipt.blockers,
      missing_inputs: ['manifest file'],
      invalid_evidence: [],
      allowed_next_actions: [],
      forbidden_actions: [],
      evidence_record: receipt,
      exit_code: EXIT_CODES.BLOCKED,
    };
  }

  const manifestRaw = loadJson(manifestPath);
  manifestRaw._manifestPath = manifestPath;
  manifestRaw._repoRoot = repoRoot;
  const manifest = normalizeManifest(manifestRaw);
  const contract = loadJson(contractPath);
  const manifestChecksum = sha256File(manifestPath);

  if (isReadOnly && manifest.lifecycle_status === 'FROZEN') {
    const receipt = createExecutionReceipt({
      project_id: manifest.project_id,
      manifest_path: manifestPath,
      manifest_checksum: manifestChecksum,
      lifecycle_version: manifest.lifecycle_version,
      requested_stage: requestedStage,
      requested_action: params.requestedAction,
      actor: params.actor,
      tool: params.tool,
      authorization_result: 'AUTHORIZED',
      blockers: [],
      expected_outputs: params.expectedOutputs,
      runtime_version: RUNTIME_VERSION,
      source_commit: sourceCommit(repoRoot),
      command: params.command,
      note: 'Read-only inspection on frozen project',
    });
    if (params.writeReceipt !== false && params.receiptDir) {
      writeExecutionReceipt(receipt, params.receiptDir);
    }
    return {
      allowed: true,
      status: 'AUTHORIZED',
      project_id: manifest.project_id,
      current_stage: manifest.current_lifecycle_stage,
      requested_stage: requestedStage,
      requested_action: params.requestedAction,
      blockers: [],
      missing_inputs: [],
      invalid_evidence: [],
      allowed_next_actions: ['read_only_inspection'],
      forbidden_actions: STAGE_ACTION_MAP['SPPC-05']?.concat(STAGE_ACTION_MAP['SPPC-08'] || []) || [],
      evidence_record: receipt,
      exit_code: EXIT_CODES.OK,
    };
  }

  const stageIdx = STAGE_ORDER.indexOf(requestedStage);
  const currentIdx = STAGE_ORDER.indexOf(manifest.current_lifecycle_stage);
  const actionStageMismatch = requestedStage && !actionMatchesStage(params.requestedAction, requestedStage);

  const validation = validateLifecycle(manifestRaw, contract, {
    repoRoot,
    requested_stage: requestedStage || manifest.current_lifecycle_stage,
    require_artifacts: false,
  });

  const blockers = [...(validation.blockers || [])];
  const forbiddenActions = [...(validation.forbidden_until_resolved || [])];

  if (actionStageMismatch) {
    blockers.push({
      code: 'ACTION_STAGE_MISMATCH',
      message: `Action ${params.requestedAction} does not match stage ${requestedStage}`,
    });
  }

  if (requestedStage && stageIdx > currentIdx && !isReadOnly) {
    const currentStatus = getStageStatus(manifest, manifest.current_lifecycle_stage);
    const currentComplete = ['COMPLETED', 'COMPLETED WITH APPROVED DEGRADATION', 'APPROVED'].includes(currentStatus);
    if (stageIdx > currentIdx && (!currentComplete || stageIdx > currentIdx + 1)) {
      blockers.push({
        code: 'FORBIDDEN_DOWNSTREAM',
        message: `BLOCKED — requested stage ${requestedStage} is not authorized at current ${manifest.current_lifecycle_stage}`,
      });
      forbiddenActions.push(params.requestedAction);
    }
  }

  const outputViolations = checkForbiddenOutputs(
    params.expectedOutputs,
    manifest,
    contract,
    repoRoot,
    requestedStage,
  );
  for (const v of outputViolations) {
    blockers.push({ code: 'OUTPUT_CLASS_VIOLATION', message: v.reason || v.message, artifact: v.artifact });
  }

  if (manifest.lifecycle_status === 'FROZEN' && !isReadOnly) {
    blockers.push({ code: 'PROJECT_FROZEN', message: 'BLOCKED — PROJECT FROZEN' });
  }

  const allowed = blockers.length === 0;
  let authResult = 'BLOCKED';
  if (allowed) {
    const stageStatus = getStageStatus(manifest, requestedStage || manifest.current_lifecycle_stage);
    authResult = stageStatus === 'COMPLETED WITH APPROVED DEGRADATION'
      ? 'AUTHORIZED WITH APPROVED DEGRADATION'
      : 'AUTHORIZED';
  }

  const receipt = createExecutionReceipt({
    project_id: manifest.project_id,
    manifest_path: manifestPath,
    manifest_checksum: manifestChecksum,
    lifecycle_version: manifest.lifecycle_version,
    requested_stage: requestedStage,
    requested_action: params.requestedAction,
    actor: params.actor,
    tool: params.tool,
    authorization_result: authResult,
    blockers,
    expected_outputs: params.expectedOutputs,
    runtime_version: RUNTIME_VERSION,
    source_commit: sourceCommit(repoRoot),
    command: params.command,
  });

  if (params.writeReceipt !== false && params.receiptDir) {
    writeExecutionReceipt(receipt, params.receiptDir);
  }

  return {
    allowed,
    status: allowed ? authResult : 'BLOCKED',
    project_id: manifest.project_id,
    current_stage: manifest.current_lifecycle_stage,
    requested_stage: requestedStage,
    requested_action: params.requestedAction,
    blockers,
    missing_inputs: validation.missing_required_inputs || [],
    invalid_evidence: validation.invalid_evidence || [],
    allowed_next_actions: validation.allowed_next_action || [],
    forbidden_actions: forbiddenActions,
    evidence_record: receipt,
    exit_code: allowed ? EXIT_CODES.OK : EXIT_CODES.BLOCKED,
  };
}

export { RUNTIME_VERSION, STAGE_ACTION_MAP, READ_ONLY_ACTIONS };
