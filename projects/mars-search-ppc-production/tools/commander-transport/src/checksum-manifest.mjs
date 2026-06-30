import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

/**
 * Build checksum manifest for package files.
 * @param {string} packageRoot
 * @param {string[]} relativePaths
 */
export function buildChecksumManifest(packageRoot, relativePaths) {
  const entries = {};
  for (const rel of relativePaths) {
    const full = path.join(packageRoot, rel);
    if (!fs.existsSync(full)) {
      entries[rel] = { status: 'MISSING', sha256: null };
      continue;
    }
    const buf = fs.readFileSync(full);
    entries[rel] = {
      status: 'PRESENT',
      sha256: createHash('sha256').update(buf).digest('hex'),
      size_bytes: buf.length,
    };
  }
  return {
    generated_at: new Date().toISOString(),
    package_root: packageRoot,
    entries,
    manifest_sha256: null,
  };
}

/**
 * Verify checksum manifest by re-reading files.
 */
export function verifyChecksumManifest(packageRoot, manifest) {
  const violations = [];
  for (const [rel, entry] of Object.entries(manifest.entries ?? {})) {
    const full = path.join(packageRoot, rel);
    if (entry.status === 'MISSING') {
      if (fs.existsSync(full)) {
        violations.push({ file: rel, code: 'UNEXPECTED_FILE', message: 'File appeared after manifest' });
      }
      continue;
    }
    if (!fs.existsSync(full)) {
      violations.push({ file: rel, code: 'FILE_MISSING', message: 'Checksum target missing' });
      continue;
    }
    const buf = fs.readFileSync(full);
    const actual = createHash('sha256').update(buf).digest('hex');
    if (actual !== entry.sha256) {
      violations.push({
        file: rel,
        code: 'CHECKSUM_MISMATCH',
        message: `Expected ${entry.sha256}, got ${actual}`,
        expected: entry.sha256,
        actual,
      });
    }
  }
  return {
    status: violations.length === 0 ? 'SCRIPT_PASS' : 'SCRIPT_FAIL',
    violations,
  };
}
