/**
 * FW-07C-2C — Delivery planner (dry-run, additive-only).
 * Operations: forge.delivery.plan
 */
import fs from 'node:fs';
import path from 'node:path';
import { sha256File } from './filesystem-manifest.mjs';
import { validateDeliveryTarget } from './delivery-path-policy.mjs';
import { DELIVERY_REASON_CODES as RC } from './delivery-reason-codes.mjs';

export const DELIVERY_MODE = Object.freeze({
  ADDITIVE_ONLY: 'ADDITIVE_ONLY',
});

export const ACTION = Object.freeze({
  ADD: 'ADD',
  MODIFY: 'MODIFY',
  DELETE: 'DELETE',
  MOVE: 'MOVE',
  UNKNOWN: 'UNKNOWN',
});

/**
 * Plan delivery operations from source entries to target paths.
 * @param {object} input
 * @param {Array<{source_path: string, destination_path: string, expected_sha256?: string}>} input.entries
 * @param {string} input.mode - ADDITIVE_ONLY
 * @param {object} [input.target_manifest] - known files in target root for unknown-file detection
 */
export function planDelivery(input) {
  const {
    entries = [],
    mode = DELIVERY_MODE.ADDITIVE_ONLY,
    target_manifest = null,
    simulate_mirror = false,
  } = input ?? {};

  const operations = [];
  const reason_codes = [];
  let adds = 0;
  let modifies = 0;
  let deletes = 0;
  let moves = 0;
  let unknown = 0;

  if (mode !== DELIVERY_MODE.ADDITIVE_ONLY) {
    reason_codes.push(RC.DL_MODE_VIOLATION);
  }

  for (const entry of entries) {
    const { source_path, destination_path, expected_sha256 } = entry;
    const pathCheck = validateDeliveryTarget(destination_path);
    if (!pathCheck.allowed) {
      operations.push({
        source_path,
        destination_path,
        action: ACTION.UNKNOWN,
        allowed: false,
        reason_codes: pathCheck.reason_codes,
      });
      unknown += 1;
      continue;
    }

    const destExists = fs.existsSync(destination_path);
    let sourceHash = null;
    if (fs.existsSync(source_path)) {
      sourceHash = sha256File(source_path);
      if (expected_sha256 && sourceHash !== expected_sha256.replace(/^sha256:/, '')) {
        const opCodes = [RC.DL_SOURCE_HASH_MISMATCH];
        reason_codes.push(...opCodes);
        operations.push({
          source_path,
          destination_path,
          action: ACTION.UNKNOWN,
          allowed: false,
          reason_codes: opCodes,
          source_hash: sourceHash,
        });
        unknown += 1;
        continue;
      }
    }

    if (destExists) {
      if (mode === DELIVERY_MODE.ADDITIVE_ONLY) {
        reason_codes.push(RC.DL_DESTINATION_EXISTS);
        operations.push({
          source_path,
          destination_path,
          action: ACTION.MODIFY,
          overwrite: false,
          delete: false,
          allowed: false,
          reason_codes: [RC.DL_DESTINATION_EXISTS, RC.DL_OVERWRITE_DENIED],
          destination_exists: true,
          source_hash: sourceHash,
        });
        modifies += 1;
        continue;
      }
    }

    operations.push({
      source_path,
      destination_path,
      action: ACTION.ADD,
      overwrite: false,
      delete: false,
      allowed: true,
      reason_codes: [],
      destination_exists: destExists,
      source_hash: sourceHash,
      expected_post_write_hash: sourceHash,
      root_validation: pathCheck,
      path_validation: pathCheck,
      reparse_validation: pathCheck.reparse,
    });
    adds += 1;
  }

  if (simulate_mirror && target_manifest?.files) {
    const plannedDests = new Set(entries.map((e) => e.destination_path.replace(/\\/g, '/').toLowerCase()));
    for (const f of target_manifest.files) {
      const abs = path.join(target_manifest.root, f.relative_path).replace(/\\/g, '/').toLowerCase();
      if (!plannedDests.has(abs) && !f.relative_path.includes('.forge-proof')) {
        reason_codes.push(RC.DL_UNKNOWN_FILE_CONFLICT);
        operations.push({
          source_path: null,
          destination_path: abs,
          action: ACTION.DELETE,
          allowed: false,
          reason_codes: [RC.DL_UNKNOWN_FILE_CONFLICT, RC.DL_DELETE_DENIED],
        });
        deletes += 1;
      }
    }
  }

  const destination_conflicts = operations.filter((o) =>
    o.reason_codes?.includes(RC.DL_DESTINATION_EXISTS)
  ).length;

  const blocked = reason_codes.length > 0 || modifies > 0 || deletes > 0 || unknown > 0;
  const verdict = blocked
    ? 'BLOCKED'
    : adds > 0 && modifies === 0 && deletes === 0
      ? 'SAFE_TO_APPLY_ADDITIVE_ONLY'
      : 'BLOCKED';

  return {
    mode,
    operations,
    summary: { adds, modifies, deletes, moves, unknown, destination_conflicts },
    reason_codes: [...new Set(reason_codes)],
    verdict,
    safe_to_apply: verdict === 'SAFE_TO_APPLY_ADDITIVE_ONLY',
  };
}

export default planDelivery;
