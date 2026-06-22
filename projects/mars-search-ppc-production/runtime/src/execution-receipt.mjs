/**
 * MARS Search PPC — Execution Receipt (Wave 1.1)
 * Immutable record for every authorized or blocked subsystem execution.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const RECEIPT_STATUSES = new Set([
  'AUTHORIZED',
  'BLOCKED',
  'AUTHORIZED WITH APPROVED DEGRADATION',
  'EXECUTED',
  'EXECUTION FAILED',
  'OUTPUT VIOLATION',
]);

export function generateReceiptId() {
  const ts = new Date().toISOString().replace(/[:.]/g, '-');
  const rand = crypto.randomBytes(4).toString('hex');
  return `sppc-receipt-${ts}-${rand}`;
}

/**
 * @param {object} fields
 */
export function createExecutionReceipt(fields) {
  const status = fields.authorization_result || fields.status || 'BLOCKED';
  if (!RECEIPT_STATUSES.has(status)) {
    throw new Error(`Invalid receipt status: ${status}`);
  }

  return {
    receipt_id: fields.receipt_id || generateReceiptId(),
    receipt_schema_version: '1.0.0',
    timestamp: fields.timestamp || new Date().toISOString(),
    project_id: fields.project_id,
    manifest_path: fields.manifest_path,
    manifest_checksum: fields.manifest_checksum,
    lifecycle_version: fields.lifecycle_version,
    requested_stage: fields.requested_stage,
    requested_action: fields.requested_action,
    actor: fields.actor || 'SAFE UNKNOWN',
    tool: fields.tool || 'SAFE UNKNOWN',
    authorization_result: status,
    blockers: fields.blockers || [],
    expected_outputs: fields.expected_outputs || [],
    actual_outputs: fields.actual_outputs || null,
    runtime_version: fields.runtime_version,
    source_commit: fields.source_commit,
    command: fields.command || null,
    note: fields.note || null,
    immutable: true,
  };
}

export function writeExecutionReceipt(receipt, receiptDir) {
  fs.mkdirSync(receiptDir, { recursive: true });
  const filename = `${receipt.receipt_id}.json`;
  const outPath = path.join(receiptDir, filename);
  fs.writeFileSync(outPath, JSON.stringify(receipt, null, 2) + '\n', { flag: 'wx' });
  return outPath;
}

export function finalizeExecutionReceipt(receipt, actualOutputs, finalStatus) {
  if (!RECEIPT_STATUSES.has(finalStatus)) {
    throw new Error(`Invalid final status: ${finalStatus}`);
  }
  return {
    ...receipt,
    authorization_result: finalStatus,
    actual_outputs: actualOutputs,
    finalized_at: new Date().toISOString(),
  };
}

export { RECEIPT_STATUSES };
