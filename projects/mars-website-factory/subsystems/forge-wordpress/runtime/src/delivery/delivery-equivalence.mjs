/**
 * FW-07C-2C — Final-state equivalence check.
 * Operations: forge.delivery.final_equivalence
 */
import fs from 'node:fs';
import { captureDirectoryManifest } from './filesystem-manifest.mjs';

export function compareManifests(initial, final) {
  const initialMap = new Map(initial.files.map((f) => [f.relative_path, f.sha256]));
  const finalMap = new Map(final.files.map((f) => [f.relative_path, f.sha256]));

  const hash_mismatches = [];
  const unexpected_files = [];
  const missing_files = [];

  for (const [rel, hash] of initialMap) {
    if (!finalMap.has(rel)) {
      missing_files.push(rel);
    } else if (finalMap.get(rel) !== hash) {
      hash_mismatches.push({ relative_path: rel, initial: hash, final: finalMap.get(rel) });
    }
  }

  for (const rel of finalMap.keys()) {
    if (!initialMap.has(rel)) {
      unexpected_files.push(rel);
    }
  }

  const equal =
    hash_mismatches.length === 0 &&
    unexpected_files.length === 0 &&
    missing_files.length === 0 &&
    initial.aggregate_sha256 === final.aggregate_sha256;

  return {
    equal,
    initial_aggregate: initial.aggregate_sha256,
    final_aggregate: final.aggregate_sha256,
    file_count_initial: initial.file_count,
    file_count_final: final.file_count,
    hash_mismatches,
    unexpected_files,
    missing_files,
    verdict: equal ? 'FINAL_FILESYSTEM_STATE_EQUALS_INITIAL_STATE' : 'FINAL_FILESYSTEM_STATE_DIFFERS',
  };
}

export function checkProofFilesAbsent(proofPaths) {
  const present = [];
  for (const p of proofPaths) {
    if (fs.existsSync(p)) present.push(p);
  }
  return { absent: present.length === 0, present };
}

export function checkEquivalence(initialManifest, finalManifest, proofPaths = []) {
  const manifestCompare = compareManifests(initialManifest, finalManifest);
  const proofCheck = checkProofFilesAbsent(proofPaths);

  return {
    ...manifestCompare,
    proof_files_absent: proofCheck.absent,
    proof_files_present: proofCheck.present,
    verdict:
      manifestCompare.equal && proofCheck.absent
        ? 'FINAL_FILESYSTEM_STATE_EQUALS_INITIAL_STATE'
        : 'FINAL_FILESYSTEM_STATE_DIFFERS',
  };
}

export default { compareManifests, checkEquivalence, checkProofFilesAbsent };
