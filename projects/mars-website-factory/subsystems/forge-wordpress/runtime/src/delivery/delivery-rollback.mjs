/**
 * FW-07C-2C — Exact owned-file rollback.
 * Operations: forge.delivery.rollback
 */
import fs from 'node:fs';
import path from 'node:path';
import { sha256File } from './filesystem-manifest.mjs';
import { DELIVERY_REASON_CODES as RC } from './delivery-reason-codes.mjs';

/**
 * Rollback exact proof files owned by a proof UUID.
 */
export function rollbackProofFiles(input) {
  const {
    proof_files = [],
    expected_uuid,
    remove_empty_proof_dirs = true,
  } = input ?? {};

  const results = [];

  for (const pf of proof_files) {
    const {
      path: filePath,
      expected_hash,
      expected_uuid: fileUuid,
    } = pf;

    if (expected_uuid && fileUuid && fileUuid !== expected_uuid) {
      results.push({
        path: filePath,
        deleted: false,
        reason_codes: [RC.DL_ROLLBACK_UUID_MISMATCH],
      });
      continue;
    }

    if (!fs.existsSync(filePath)) {
      results.push({ path: filePath, deleted: false, already_absent: true });
      continue;
    }

    const actualHash = sha256File(filePath);
    const normExpected = expected_hash?.replace(/^sha256:/, '');

    if (normExpected && actualHash !== normExpected) {
      results.push({
        path: filePath,
        deleted: false,
        expected_hash: normExpected,
        actual_hash: actualHash,
        reason_codes: [RC.DL_ROLLBACK_HASH_MISMATCH],
      });
      continue;
    }

    fs.unlinkSync(filePath);
    results.push({
      path: filePath,
      deleted: true,
      expected_hash: normExpected,
      actual_hash: actualHash,
    });
  }

  const empty_dirs_removed = [];
  if (remove_empty_proof_dirs) {
    const dirs = new Set(
      proof_files
        .map((pf) => path.dirname(pf.path))
        .filter((d) => d.includes('.forge-proof'))
    );
    for (const dir of dirs) {
      try {
        const remaining = fs.readdirSync(dir);
        if (remaining.length === 0) {
          fs.rmdirSync(dir);
          empty_dirs_removed.push(dir);
        }
      } catch {
        /* dir may not exist */
      }
    }
  }

  const allDeleted = results.every((r) => r.deleted || r.already_absent);

  return {
    success: allDeleted,
    results,
    empty_dirs_removed,
    existing_files_touched: 0,
  };
}

export default rollbackProofFiles;
