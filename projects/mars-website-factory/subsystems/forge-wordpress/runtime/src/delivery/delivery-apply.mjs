/**
 * FW-07C-2C — Bounded additive delivery apply.
 * Operations: forge.delivery.apply_additive
 */
import fs from 'node:fs';
import path from 'node:path';
import { sha256File } from './filesystem-manifest.mjs';
import { validateDeliveryTarget, validateVolumeLabel } from './delivery-path-policy.mjs';
import { planDelivery, DELIVERY_MODE } from './delivery-planner.mjs';
import { DELIVERY_REASON_CODES as RC } from './delivery-reason-codes.mjs';

export function applyAdditiveDelivery(input) {
  const {
    entries,
    mode = DELIVERY_MODE.ADDITIVE_ONLY,
    volume_label,
    dry_run = false,
  } = input ?? {};

  const volumeCheck = validateVolumeLabel(volume_label);
  if (!volumeCheck.allowed) {
    return {
      applied: false,
      dry_run,
      reason_codes: volumeCheck.reason_codes,
      results: [],
    };
  }

  const plan = planDelivery({ entries, mode });
  if (!plan.safe_to_apply) {
    return {
      applied: false,
      dry_run,
      plan,
      reason_codes: plan.reason_codes,
      results: [],
    };
  }

  if (dry_run) {
    return { applied: false, dry_run: true, plan, results: plan.operations };
  }

  const results = [];

  for (const op of plan.operations) {
    if (!op.allowed || op.action !== 'ADD') continue;

    const destCheck = validateDeliveryTarget(op.destination_path);
    if (!destCheck.allowed) {
      results.push({ ...op, applied: false, reason_codes: destCheck.reason_codes });
      continue;
    }

    if (fs.existsSync(op.destination_path)) {
      results.push({
        ...op,
        applied: false,
        reason_codes: [RC.DL_DESTINATION_EXISTS],
      });
      continue;
    }

    const destDir = path.dirname(op.destination_path);
    fs.mkdirSync(destDir, { recursive: true });

    const tmpPath = op.destination_path + '.forge-tmp';
    fs.copyFileSync(op.source_path, tmpPath);
    const tmpHash = sha256File(tmpPath);

    if (tmpHash !== op.source_hash) {
      fs.unlinkSync(tmpPath);
      results.push({
        ...op,
        applied: false,
        reason_codes: [RC.DL_SOURCE_HASH_MISMATCH],
        tmp_hash: tmpHash,
      });
      continue;
    }

    fs.renameSync(tmpPath, op.destination_path);
    const finalHash = sha256File(op.destination_path);

    results.push({
      ...op,
      applied: true,
      tmp_hash: tmpHash,
      final_hash: finalHash,
      hash_verified: finalHash === op.source_hash,
    });
  }

  const allOk = results.every((r) => r.applied && r.hash_verified);

  return {
    applied: allOk,
    dry_run: false,
    plan,
    results,
    reason_codes: allOk ? [] : [RC.DL_SOURCE_HASH_MISMATCH],
  };
}

export default applyAdditiveDelivery;
