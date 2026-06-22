import { VALID_TRANSITIONS, COMPLETE_STATUSES, STAGE_ORDER } from './constants.mjs';
import { getStageStatus } from './manifest-normalize.mjs';

export function isTransitionAllowed(fromStatus, toStatus) {
  const allowed = VALID_TRANSITIONS[fromStatus];
  if (!allowed) return false;
  return allowed.includes(toStatus);
}

export function validateStageStart(manifest, contract, targetStageId) {
  const errors = [];
  const def = contract.stages.find((s) => s.stage_id === targetStageId);
  if (!def) {
    errors.push({ code: 'UNKNOWN_STAGE', message: `Unknown stage ${targetStageId}` });
    return { allowed: false, errors };
  }

  if (manifest.lifecycle_status === 'FROZEN') {
    errors.push({ code: 'PROJECT_FROZEN', message: 'Project lifecycle status is FROZEN' });
    return { allowed: false, errors };
  }

  for (const pre of def.prerequisites || []) {
    const st = getStageStatus(manifest, pre.stage_id);
    const required = pre.required_status || ['COMPLETED', 'COMPLETED WITH APPROVED DEGRADATION'];
    if (!required.includes(st)) {
      errors.push({
        code: 'PREREQUISITE_NOT_MET',
        message: `${targetStageId} cannot start before ${pre.stage_id} is ${required.join(' or ')} (current: ${st})`,
        stage_id: pre.stage_id,
        current_status: st,
      });
    }
  }

  const targetIdx = STAGE_ORDER.indexOf(targetStageId);
  for (let i = 0; i < targetIdx; i++) {
    const priorId = STAGE_ORDER[i];
    const priorDef = contract.stages.find((s) => s.stage_id === priorId);
    if (!priorDef) continue;
    const st = getStageStatus(manifest, priorId);
    if (!COMPLETE_STATUSES.has(st) && st !== 'NOT STARTED' && priorId !== targetStageId) {
      if (st === 'IN PROGRESS' || st === 'BLOCKED' || st === 'READY FOR REVIEW') {
        errors.push({
          code: 'PRIOR_STAGE_INCOMPLETE',
          message: `${targetStageId} blocked: ${priorId} is ${st}, not complete`,
          stage_id: priorId,
        });
      }
    }
  }

  return { allowed: errors.length === 0, errors };
}

export function validateTransition(manifest, stageId, fromStatus, toStatus) {
  const errors = [];
  if (!isTransitionAllowed(fromStatus, toStatus)) {
    errors.push({
      code: 'FORBIDDEN_TRANSITION',
      message: `Transition ${fromStatus} → ${toStatus} is forbidden for ${stageId}`,
    });
  }

  if (toStatus === 'COMPLETED WITH APPROVED DEGRADATION') {
    const deg = manifest.degraded_mode_registry?.[stageId] || manifest.degraded_evidence_approvals?.[stageId];
    if (!deg?.approved) {
      errors.push({
        code: 'DEGRADED_NOT_APPROVED',
        message: 'COMPLETED WITH APPROVED DEGRADATION requires operator degradation approval',
      });
    }
  }

  if (toStatus === 'IN PROGRESS' && (fromStatus === 'COMPLETED' || fromStatus === 'APPROVED')) {
    errors.push({
      code: 'REOPEN_TRACE_REQUIRED',
      message: 'Reopen to IN PROGRESS requires trace in manifest reopen_log',
      severity: 'warning',
    });
  }

  return { allowed: errors.filter((e) => e.severity !== 'warning').length === 0, errors };
}

export function canStartStage(manifest, contract, stageId) {
  const current = getStageStatus(manifest, stageId);
  if (current === 'FROZEN') {
    return { allowed: false, reason: 'Stage is FROZEN' };
  }
  const startCheck = validateStageStart(manifest, contract, stageId);
  if (!startCheck.allowed) {
    return { allowed: false, reason: startCheck.errors.map((e) => e.message).join('; ') };
  }
  if (current === 'NOT STARTED' || current === 'BLOCKED') {
    const tr = validateTransition(manifest, stageId, current, 'IN PROGRESS');
    if (!tr.allowed) {
      return { allowed: false, reason: tr.errors.map((e) => e.message).join('; ') };
    }
  }
  return { allowed: true, reason: null };
}
