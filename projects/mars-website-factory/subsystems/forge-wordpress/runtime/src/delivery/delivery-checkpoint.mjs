/**
 * FW-07C-2C — Pre-delivery checkpoint capture.
 * Operations: forge.delivery.checkpoint
 */
import fs from 'node:fs';
import path from 'node:path';
import { captureDirectoryManifest } from './filesystem-manifest.mjs';

export function createCheckpoint(input) {
  const {
    checkpoint_root,
    surfaces = [],
    rollback_instructions,
    safe_runtime_state,
  } = input ?? {};

  fs.mkdirSync(path.join(checkpoint_root, 'manifests'), { recursive: true });
  fs.mkdirSync(path.join(checkpoint_root, 'rollback'), { recursive: true });
  fs.mkdirSync(path.join(checkpoint_root, 'receipts'), { recursive: true });

  const snapshots = {};

  for (const surface of surfaces) {
    const { key, source_dir, snapshot_subdir } = surface;
    const manifest = captureDirectoryManifest(source_dir);
    const snapDir = path.join(checkpoint_root, snapshot_subdir);
    fs.mkdirSync(snapDir, { recursive: true });

    for (const file of manifest.files) {
      const src = path.join(source_dir, file.relative_path);
      const dest = path.join(snapDir, file.relative_path);
      fs.mkdirSync(path.dirname(dest), { recursive: true });
      fs.copyFileSync(src, dest);
    }

    const manifestPath = path.join(checkpoint_root, 'manifests', `${key}-manifest.json`);
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');

    snapshots[key] = manifest;
  }

  const checkpointMeta = {
    created_at: new Date().toISOString(),
    checkpoint_root,
    surfaces: surfaces.map((s) => s.key),
    snapshots: Object.fromEntries(
      Object.entries(snapshots).map(([k, m]) => [
        k,
        {
          aggregate_sha256: m.aggregate_sha256,
          file_count: m.file_count,
          directory_count: m.directory_count,
          total_bytes: m.total_bytes,
        },
      ])
    ),
    safe_runtime_state,
    proof_absence: true,
    rollback_instructions,
  };

  fs.writeFileSync(
    path.join(checkpoint_root, 'rollback', 'rollback-instructions.json'),
    JSON.stringify(rollback_instructions, null, 2),
    'utf8'
  );

  fs.writeFileSync(
    path.join(checkpoint_root, 'receipts', 'checkpoint-receipt.json'),
    JSON.stringify(checkpointMeta, null, 2),
    'utf8'
  );

  return checkpointMeta;
}

export default createCheckpoint;
