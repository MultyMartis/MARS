import { BLOCKER_CODES } from './constants.mjs';

const REQUIRED_DEGRADED_FIELDS = [
  'affected_stage',
  'missing_evidence',
  'reason',
  'attempted_collection',
  'failure_evidence',
  'alternative_evidence',
  'impact',
  'operator_approval',
  'approval_timestamp',
  'expiry_or_recheck_condition',
  'downstream_limitations',
];

export function validateDegradedRecord(record, stageId) {
  const issues = [];
  if (!record) {
    return { valid: false, issues: ['record missing'] };
  }

  for (const field of REQUIRED_DEGRADED_FIELDS) {
    const alt = field === 'expiry_or_recheck_condition' ? record.expiry_recheck_condition : null;
    if (record[field] == null && alt == null) {
      issues.push(`missing field: ${field}`);
    }
  }

  if (record.approved !== true && record.operator_approval?.approved !== true) {
    issues.push('operator approval not granted');
  }

  return { valid: issues.length === 0, issues };
}

export function validateDegradedMode(manifest, stageId) {
  const blockers = [];
  const registry = manifest.degraded_mode_registry || manifest.degraded_evidence_approvals || {};
  const record = registry[stageId];

  const stageStatus = manifest.stage_registry?.[stageId]?.status
    || manifest.stage_statuses?.[stageId]?.status;

  if (stageStatus === 'COMPLETED WITH APPROVED DEGRADATION') {
    const check = validateDegradedRecord(record, stageId);
    if (!check.valid) {
      blockers.push({
        code: 'DEGRADED_NOT_APPROVED',
        message: BLOCKER_CODES.DEGRADED_NOT_APPROVED,
        issues: check.issues,
        owner: 'Operator',
      });
    }
  }

  return { valid: blockers.length === 0, blockers };
}

export function checkPaidSerpDegradation(manifest, currentIdx, stageOrder) {
  const blockers = [];
  const sppc13Idx = stageOrder.indexOf('SPPC-13');
  if (currentIdx < sppc13Idx) return { valid: true, blockers: [] };

  const paidSerp = manifest.artifact_registry?.paid_serp_business_hours_evidence
    || manifest.artifacts?.paid_serp_business_hours_evidence;

  const hasPaidSerp = paidSerp?.path && paidSerp.status === 'REGISTERED';
  if (hasPaidSerp) return { valid: true, blockers: [] };

  const deg = manifest.degraded_mode_registry?.['SPPC-10']
    || manifest.degraded_evidence_approvals?.['SPPC-10'];

  if (!deg?.approved) {
    blockers.push({
      code: 'PAID_SERP_MISSING',
      message: BLOCKER_CODES.PAID_SERP_MISSING,
      owner: 'MIG',
    });
    return { valid: false, blockers };
  }

  const check = validateDegradedRecord(deg, 'SPPC-10');
  if (!check.valid) {
    blockers.push({
      code: 'DEGRADED_NOT_APPROVED',
      message: BLOCKER_CODES.DEGRADED_NOT_APPROVED,
      issues: check.issues,
      owner: 'Operator',
    });
  }

  return { valid: blockers.length === 0, blockers };
}
