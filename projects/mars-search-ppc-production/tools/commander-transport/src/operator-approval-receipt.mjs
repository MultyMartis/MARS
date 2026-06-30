/**
 * Operator semantic approval receipt — generated for review, never self-approved.
 */

import fs from 'node:fs';
import { createHash } from 'node:crypto';

export const RECEIPT_STATUSES = Object.freeze({
  READY_FOR_OPERATOR_APPROVAL: 'READY_FOR_OPERATOR_APPROVAL',
  OPERATOR_SEMANTIC_APPROVED: 'OPERATOR_SEMANTIC_APPROVED',
  REJECTED: 'REJECTED',
  REVOKED: 'REVOKED',
});

/**
 * Generate receipt for operator review — does NOT set OPERATOR_SEMANTIC_APPROVED.
 * @param {object} input
 */
export function generateApprovalReceiptForReview(input) {
  const receipt = {
    schema_version: 'campaign-operator-approval-receipt-v1',
    project_id: input.project_id,
    pilot_id: input.pilot_id ?? input.project_id,
    campaign_program: input.campaign_program,
    release_version: input.release_version,
    status: RECEIPT_STATUSES.READY_FOR_OPERATOR_APPROVAL,
    authority_artifact_paths: input.authority_artifact_paths ?? [],
    authority_hashes: input.authority_hashes ?? {},
    phrase_count: input.phrase_count ?? 0,
    keep_count: input.keep_count ?? 0,
    reject_count: input.reject_count ?? 0,
    move_count: input.move_count ?? 0,
    hold_count: input.hold_count ?? 0,
    campaign_count: input.campaign_count ?? 0,
    group_count: input.group_count ?? 0,
    ad_count: input.ad_count ?? 0,
    geo_policy: input.geo_policy ?? '',
    negative_policy: input.negative_policy ?? '',
    approval_timestamp: null,
    operator_identity_label: null,
    approval_scope: input.approval_scope ?? 'semantic_authority',
    known_accepted_risks: input.known_accepted_risks ?? [],
    generated_for_review_only: true,
    generated_at: new Date().toISOString(),
  };

  return receipt;
}

/**
 * Validate receipt for release gate — must have OPERATOR_SEMANTIC_APPROVED from operator.
 */
export function validateApprovalReceipt(receipt) {
  const violations = [];

  if (!receipt) {
    violations.push({ code: 'MISSING_RECEIPT', message: 'Operator approval receipt required' });
    return { valid: false, violations };
  }

  if (receipt.generated_for_review_only === true && receipt.status !== RECEIPT_STATUSES.OPERATOR_SEMANTIC_APPROVED) {
    violations.push({
      code: 'NOT_OPERATOR_APPROVED',
      message: 'Receipt is review-only — operator must explicitly approve',
    });
  }

  if (receipt.status !== RECEIPT_STATUSES.OPERATOR_SEMANTIC_APPROVED) {
    violations.push({
      code: 'STATUS_NOT_APPROVED',
      message: `Receipt status must be OPERATOR_SEMANTIC_APPROVED, got ${receipt.status}`,
    });
  }

  if (!receipt.approval_timestamp) {
    violations.push({
      code: 'MISSING_APPROVAL_TIMESTAMP',
      message: 'Operator approval timestamp required',
    });
  }

  if (!receipt.operator_identity_label) {
    violations.push({
      code: 'MISSING_OPERATOR_IDENTITY',
      message: 'Operator identity label required',
    });
  }

  if ((receipt.hold_count ?? 0) > 0) {
    violations.push({
      code: 'UNRESOLVED_HOLD',
      message: `Cannot approve with ${receipt.hold_count} unresolved HOLD phrases`,
    });
  }

  return {
    valid: violations.length === 0,
    violations,
  };
}

export function loadApprovalReceipt(receiptPath) {
  const raw = fs.readFileSync(receiptPath, 'utf8');
  return JSON.parse(raw);
}

export function hashReceipt(receipt) {
  const copy = { ...receipt };
  delete copy.generated_at;
  return createHash('sha256').update(JSON.stringify(copy)).digest('hex');
}
