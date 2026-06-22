import fs from 'node:fs';
import path from 'node:path';
import {
  STAGE_ORDER,
  FORBIDDEN_BEFORE,
  STAGE_TO_FORBIDDEN_ACTIONS,
  ARTIFACT_OWNERS,
  BLOCKER_CODES,
  COMPLETE_STATUSES,
  LIFECYCLE_VERSION,
} from './constants.mjs';
import { normalizeManifest, getStageStatus, getArtifact, completedStages } from './manifest-normalize.mjs';
import { validateStageStart, canStartStage, validateTransition } from './transition-engine.mjs';
import { resolveArtifactPath, verifyRequiredArtifacts } from './artifact-resolver.mjs';
import { validateFullCorpus } from './corpus-enforcement.mjs';
import { validateHumanReviewBoundary } from './human-review-boundary.mjs';
import { validateDegradedMode, checkPaidSerpDegradation } from './degraded-evidence.mjs';
import { buildBlockerReport } from './blocker-report.mjs';

export function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function stageDef(contract, stageId) {
  return contract.stages.find((s) => s.stage_id === stageId);
}

function artifactExists(manifest, artifactType, repoRoot) {
  const r = resolveArtifactPath(manifest, artifactType, repoRoot);
  return r.exists;
}

export function validateLifecycle(manifestRaw, contract, options = {}) {
  if (!manifestRaw) {
    return {
      status: 'BLOCKED',
      blocker_code: 'MISSING_MANIFEST',
      blockers: [{ code: 'MISSING_MANIFEST', message: BLOCKER_CODES.MISSING_MANIFEST }],
      exit_code: 2,
    };
  }

  const manifest = normalizeManifest(manifestRaw);
  const repoRoot = manifest._repoRoot || options.repoRoot || process.cwd();
  const currentStage = options.requested_stage || manifest.current_lifecycle_stage || 'SPPC-01';
  const currentIdx = STAGE_ORDER.indexOf(currentStage);

  const blockers = [];
  const missing = [];
  const invalid = [];
  const forbidden = [];
  const owners = new Set();

  if (manifest.lifecycle_version && manifest.lifecycle_version !== LIFECYCLE_VERSION && manifest.lifecycle_version !== contract.version) {
    blockers.push({
      code: 'INVALID_LIFECYCLE_VERSION',
      message: `Lifecycle version ${manifest.lifecycle_version} does not match contract ${contract.version}`,
    });
  }

  if (manifest.lifecycle_status === 'FROZEN') {
    blockers.push({
      code: 'PROJECT_FROZEN',
      message: BLOCKER_CODES.PROJECT_FROZEN,
      owner: 'Operator',
    });
    owners.add('Operator');
  }

  const def = stageDef(contract, currentStage);
  if (def) {
    const startCheck = validateStageStart(manifest, contract, currentStage);
    for (const err of startCheck.errors) {
      if (err.code === 'PROJECT_FROZEN' && manifest.lifecycle_status === 'FROZEN') continue;
      blockers.push({ code: err.code, message: err.message, owner: stageDef(contract, err.stage_id)?.owning_system });
      if (err.stage_id) {
        missing.push({ type: 'prerequisite_stage', id: err.stage_id });
      }
    }

    const stageStatus = getStageStatus(manifest, currentStage);
    const needsArtifacts = ['READY FOR REVIEW', 'APPROVED', 'COMPLETED', 'COMPLETED WITH APPROVED DEGRADATION'].includes(stageStatus)
      || options.require_artifacts === true;

    if (needsArtifacts) {
      const artCheck = verifyRequiredArtifacts(manifest, contract, currentStage, repoRoot);
      for (const m of artCheck.missing) {
        missing.push(m);
        owners.add(m.owner);
      }
      for (const inv of artCheck.invalid) {
        invalid.push(inv);
        owners.add(inv.owner);
      }
    }

    if (def.operator_approval_required) {
      const approval = manifest.approval_registry?.[currentStage] || manifest.operator_approvals?.[currentStage];
      const needsApproval = ['READY FOR REVIEW', 'APPROVED', 'COMPLETED', 'COMPLETED WITH APPROVED DEGRADATION'].includes(stageStatus);
      if (needsApproval && !approval?.approved) {
        missing.push({ type: 'operator_approval', id: currentStage, owner: 'Operator' });
        owners.add('Operator');
      }
    }
  }

  const corpusCheck = validateFullCorpus(manifest, currentStage);
  blockers.push(...corpusCheck.blockers);
  if (corpusCheck.blockers.length) owners.add('MIG');

  const hrCheck = validateHumanReviewBoundary(manifest);
  blockers.push(...hrCheck.blockers);

  const degCheck = validateDegradedMode(manifest, currentStage);
  blockers.push(...degCheck.blockers);

  const paidCheck = checkPaidSerpDegradation(manifest, currentIdx, STAGE_ORDER);
  blockers.push(...paidCheck.blockers);
  if (paidCheck.blockers.length) owners.add('MIG');

  for (const [gateStage, arts] of Object.entries(FORBIDDEN_BEFORE)) {
    const gateIdx = STAGE_ORDER.indexOf(gateStage);
    if (currentIdx < gateIdx || !isStageComplete(getStageStatus(manifest, gateStage))) {
      for (const art of arts) {
        if (artifactExists(manifest, art, repoRoot)) {
          forbidden.push({
            artifact: art,
            reason: `exists before ${gateStage} complete`,
            action: STAGE_TO_FORBIDDEN_ACTIONS[gateStage] || [],
          });
        }
      }
    }
  }

  if (!isStageComplete(getStageStatus(manifest, 'SPPC-12')) && artifactExists(manifest, 'ppc_strategy_decision_record', repoRoot)) {
    forbidden.push({ artifact: 'ppc_strategy_decision_record', reason: 'strategy before dated analytical pack', action: ['AI PPC Strategist'] });
  }

  if (!isStageComplete(getStageStatus(manifest, 'SPPC-07')) && artifactExists(manifest, 'semantic_cluster_registry', repoRoot)) {
    forbidden.push({ artifact: 'semantic_cluster_registry', reason: 'clustering before ownership', action: ['Semantic Clustering'] });
  }

  if (!isStageComplete(getStageStatus(manifest, 'SPPC-07')) && artifactExists(manifest, 'negative_intelligence_pack', repoRoot)) {
    forbidden.push({ artifact: 'negative_intelligence_pack', reason: 'negatives before ownership', action: ['Negative Keyword Intelligence'] });
  }

  if (!isStageComplete(getStageStatus(manifest, 'SPPC-19')) && artifactExists(manifest, 'commander_export_artifact', repoRoot)) {
    forbidden.push({ artifact: 'commander_export_artifact', reason: 'Commander before QA', action: ['Commander Export'] });
  }

  if (options.check_bidding === 'automatic' && !manifest.analytics_readiness?.conversion_tracking) {
    blockers.push({ code: 'BIDDING_ANALYTICS_MISSING', message: 'Automatic bidding without analytics readiness', owner: 'Campaign Production' });
  }

  if (manifest.final_launch_authority?.granted && !isStageComplete(getStageStatus(manifest, 'SPPC-21'))) {
    forbidden.push({ artifact: 'launch_evidence_pack', reason: 'launch inferred from export', action: ['Launch'] });
  }

  const commander = getArtifact(manifest, 'commander_export_artifact');
  if (commander?.semantic_mutation_detected === true) {
    blockers.push({ code: 'EXPORT_SEMANTIC_MUTATION', message: 'Commander export attempted semantic mutation', owner: 'Commander Export' });
    forbidden.push({ artifact: 'commander_export_artifact', reason: 'export semantic mutation', action: ['Commander Export'] });
  }

  if (manifest.post_launch_policy?.silent_semantic_core_mutation === true) {
    blockers.push({ code: 'POSTLAUNCH_MUTATION', message: 'Post-launch silent Semantic Core mutation forbidden — governed proposal required', owner: 'Post-Launch Learning' });
  }

  if (manifest.requested_work?.forbidden_at_current === true) {
    blockers.push({
      code: 'FORBIDDEN_DOWNSTREAM',
      message: `Requested work ${manifest.requested_work.type} belongs to downstream stage ${manifest.requested_work.downstream_stage}`,
      owner: 'Web-GPT / Operator',
    });
  }

  if (missing.length) {
    blockers.push({ code: 'MISSING_REQUIREMENTS', message: BLOCKER_CODES.MISSING_REQUIREMENTS, items: missing });
  }

  if (forbidden.length) {
    blockers.push({ code: 'FORBIDDEN_DOWNSTREAM', message: BLOCKER_CODES.FORBIDDEN_DOWNSTREAM, items: forbidden });
  }

  const blocked = blockers.length > 0 || forbidden.length > 0;
  const allowedNext = def?.allowed_next_stages || [];
  let allowedWork = [];

  if (!blocked && def) {
    allowedWork = [`Complete ${currentStage}`, ...allowedNext.map((s) => `Advance to ${s}`)];
  } else if (manifest.lifecycle_status === 'FROZEN') {
    allowedWork = ['Resolve freeze blockers per operator charter', 'Review Wave 1+ gap closure requirements'];
  } else {
    allowedWork = [`Resolve blockers for ${currentStage}`];
  }

  const result = {
    status: blocked ? 'BLOCKED' : 'READY',
    project_id: manifest.project_id,
    current_stage: currentStage,
    completed_approved_stages: completedStages(manifest),
    missing_required_inputs: [...missing.map((m) => m.id || m.stage_id || m.type).filter(Boolean), ...invalid.map((i) => i.id)],
    invalid_evidence: invalid,
    required_owners: [...owners],
    allowed_next_action: allowedWork,
    forbidden_until_resolved: [...new Set(forbidden.flatMap((f) => f.action || []).filter(Boolean))],
    forbidden_artifacts: forbidden,
    next_allowed_stages: blocked ? [] : allowedNext,
    blockers,
    degraded_mode_available: !!(manifest.degraded_mode_registry?.['SPPC-10']?.approved || manifest.degraded_evidence_approvals?.['SPPC-10']?.approved) ? 'YES' : 'NO',
    operator_approval_required: missing.some((m) => m.type === 'operator_approval'),
    exit_code: blocked ? 2 : 0,
  };

  result.blocker_report = buildBlockerReport(result, manifest, options);
  return result;
}

function isStageComplete(status) {
  return COMPLETE_STATUSES.has(status);
}

export function validateCanStart(manifestRaw, contract, stageId, options = {}) {
  const manifest = normalizeManifest(manifestRaw);
  return canStartStage(manifest, contract, stageId);
}

export function validateTransitionDryRun(manifestRaw, contract, stageId, toStatus, options = {}) {
  const manifest = normalizeManifest(manifestRaw);
  const fromStatus = getStageStatus(manifest, stageId);
  const startCheck = validateStageStart(manifest, contract, stageId);
  const trCheck = validateTransition(manifest, stageId, fromStatus, toStatus);
  const artCheck = verifyRequiredArtifacts(manifest, contract, stageId, manifest._repoRoot || options.repoRoot);

  const blocked = !startCheck.allowed || !trCheck.allowed
    || (toStatus === 'COMPLETED' && !artCheck.valid);

  return {
    stage_id: stageId,
    from_status: fromStatus,
    to_status: toStatus,
    allowed: !blocked,
    start_errors: startCheck.errors,
    transition_errors: trCheck.errors,
    artifact_errors: artCheck.missing.concat(artCheck.invalid),
    dry_run: true,
  };
}

export { formatBlockerReportMd } from './blocker-report.mjs';
