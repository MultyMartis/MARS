/**
 * Campaign release state model — mandatory non-interchangeable states.
 */

export const RELEASE_STATES = Object.freeze({
  DRAFT: 'DRAFT',
  PHRASE_AUDIT_COMPLETE: 'PHRASE_AUDIT_COMPLETE',
  OPERATOR_SEMANTIC_APPROVED: 'OPERATOR_SEMANTIC_APPROVED',
  AUTHORITY_FROZEN: 'AUTHORITY_FROZEN',
  GENERATION_COMPLETE: 'GENERATION_COMPLETE',
  ARTIFACT_VALIDATED: 'ARTIFACT_VALIDATED',
  OPERATOR_IMPORT_READY: 'OPERATOR_IMPORT_READY',
  COMMANDER_IMPORTED: 'COMMANDER_IMPORTED',
  IMPORT_RECONCILED: 'IMPORT_RECONCILED',
  DIRECT_POST_IMPORT_READY: 'DIRECT_POST_IMPORT_READY',
  LAUNCH_APPROVED: 'LAUNCH_APPROVED',
});

export const SCRIPT_STATUS = Object.freeze({
  PASS: 'SCRIPT_PASS',
  FAIL: 'SCRIPT_FAIL',
});

export const GATE_STATUS = Object.freeze({
  PASS: 'RELEASE_GATE_PASS',
  FAIL: 'RELEASE_GATE_FAIL',
  NOT_RUN: 'NOT_RUN',
});

/**
 * Create initial release state document.
 */
export function createReleaseState(input) {
  return {
    schema_version: 'campaign-release-state-v1',
    project_id: input.project_id,
    pilot_id: input.pilot_id,
    release_version: input.release_version,
    updated_at: new Date().toISOString(),
    states: {
      DRAFT: input.states?.DRAFT ?? true,
      PHRASE_AUDIT_COMPLETE: input.states?.PHRASE_AUDIT_COMPLETE ?? false,
      OPERATOR_SEMANTIC_APPROVED: input.states?.OPERATOR_SEMANTIC_APPROVED ?? false,
      AUTHORITY_FROZEN: input.states?.AUTHORITY_FROZEN ?? false,
      GENERATION_COMPLETE: input.states?.GENERATION_COMPLETE ?? false,
      ARTIFACT_VALIDATED: input.states?.ARTIFACT_VALIDATED ?? false,
      OPERATOR_IMPORT_READY: input.states?.OPERATOR_IMPORT_READY ?? false,
      COMMANDER_IMPORTED: input.states?.COMMANDER_IMPORTED ?? false,
      IMPORT_RECONCILED: input.states?.IMPORT_RECONCILED ?? false,
      DIRECT_POST_IMPORT_READY: input.states?.DIRECT_POST_IMPORT_READY ?? false,
      LAUNCH_APPROVED: input.states?.LAUNCH_APPROVED ?? false,
    },
    script_status: {
      last_script_result: null,
      last_script_at: null,
    },
    semantic_status: {
      automation_status: input.semantic_status?.automation_status ?? null,
      operator_approval_receipt_path: input.semantic_status?.operator_approval_receipt_path ?? null,
    },
    release_gate_status: GATE_STATUS.NOT_RUN,
    notes: input.notes ?? [],
  };
}

/**
 * Derive human-readable current phase from state flags.
 */
export function deriveCurrentPhase(stateDoc) {
  const s = stateDoc.states;
  if (s.LAUNCH_APPROVED) return RELEASE_STATES.LAUNCH_APPROVED;
  if (s.IMPORT_RECONCILED) return RELEASE_STATES.IMPORT_RECONCILED;
  if (s.COMMANDER_IMPORTED) return RELEASE_STATES.COMMANDER_IMPORTED;
  if (s.OPERATOR_IMPORT_READY) return RELEASE_STATES.OPERATOR_IMPORT_READY;
  if (s.ARTIFACT_VALIDATED) return RELEASE_STATES.ARTIFACT_VALIDATED;
  if (s.GENERATION_COMPLETE) return RELEASE_STATES.GENERATION_COMPLETE;
  if (s.AUTHORITY_FROZEN) return RELEASE_STATES.AUTHORITY_FROZEN;
  if (s.OPERATOR_SEMANTIC_APPROVED) return RELEASE_STATES.OPERATOR_SEMANTIC_APPROVED;
  if (s.PHRASE_AUDIT_COMPLETE) return RELEASE_STATES.PHRASE_AUDIT_COMPLETE;
  return RELEASE_STATES.DRAFT;
}

/**
 * Check prerequisites for release gate.
 */
export function checkReleaseStatePrerequisites(stateDoc) {
  const violations = [];
  const s = stateDoc.states;

  if (!s.AUTHORITY_FROZEN) {
    violations.push({ code: 'AUTHORITY_NOT_FROZEN', message: 'Authority must be frozen before release gate' });
  }

  if (!s.GENERATION_COMPLETE) {
    violations.push({ code: 'GENERATION_INCOMPLETE', message: 'Generation must be complete' });
  }

  return { ready: violations.length === 0, violations };
}

/**
 * Update state after successful release gate (technical only — not semantic/launch approval).
 */
export function applyReleaseGateResult(stateDoc, gateResult) {
  const next = { ...stateDoc, updated_at: new Date().toISOString() };
  next.release_gate_status = gateResult.status;
  next.script_status = {
    last_script_result: gateResult.script_status,
    last_script_at: new Date().toISOString(),
  };
  if (gateResult.status === GATE_STATUS.PASS) {
    next.states = { ...next.states, ARTIFACT_VALIDATED: true };
  }
  return next;
}
