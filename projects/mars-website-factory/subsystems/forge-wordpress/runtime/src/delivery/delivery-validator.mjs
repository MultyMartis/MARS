/**
 * FW-07C-2C — Post-delivery validation.
 * Operations: forge.delivery.validate
 */
import fs from 'node:fs';
import { captureDirectoryManifest, sha256Buffer } from './filesystem-manifest.mjs';
import { compareManifests } from './delivery-equivalence.mjs';

export function validatePostDelivery(input) {
  const {
    initial_manifest,
    current_root,
    expected_new_files = [],
    exclude_from_compare = [],
  } = input ?? {};

  const current = captureDirectoryManifest(current_root, {
    exclude: exclude_from_compare,
  });

  const compare = compareManifests(initial_manifest, current);

  const new_files_verified = [];
  for (const nf of expected_new_files) {
    const exists = fs.existsSync(nf.path);
    let hashOk = false;
    if (exists && nf.expected_hash) {
      const content = fs.readFileSync(nf.path);
      const hash = sha256Buffer(content);
      hashOk = hash === nf.expected_hash.replace(/^sha256:/, '');
    }
    new_files_verified.push({ path: nf.path, exists, hash_verified: hashOk });
  }

  const unexpected = compare.unexpected_files.filter(
    (f) => !expected_new_files.some((nf) => nf.path.replace(/\\/g, '/').endsWith(f))
  );

  return {
    new_files: expected_new_files.length,
    new_files_verified,
    existing_files_modified: compare.hash_mismatches.length,
    existing_files_deleted: compare.missing_files.length,
    unexpected_files: unexpected,
    hash_mismatches: compare.hash_mismatches,
    passed:
      compare.hash_mismatches.length === 0 &&
      compare.missing_files.length === 0 &&
      unexpected.length === 0 &&
      new_files_verified.every((f) => f.exists && f.hash_verified),
  };
}

export default validatePostDelivery;
