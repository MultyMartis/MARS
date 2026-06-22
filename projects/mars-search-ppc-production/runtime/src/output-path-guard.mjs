/**
 * MARS Search PPC — Output Path Guard (Wave 1.2)
 * Prevents ungated legacy tools from writing into canonical production locations.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../');

const CANONICAL_PRODUCTION_PREFIXES = [
  'projects/orca/projects/',
  'projects/mars-search-ppc-production/state/',
  'incoming/mig/production/',
];

const QUARANTINE_ROOT = path.join(
  REPO_ROOT,
  'projects/mars-search-ppc-production/runtime/quarantine/legacy-output',
);

export function isCanonicalProductionPath(targetPath, repoRoot = REPO_ROOT) {
  const abs = path.resolve(repoRoot, targetPath);
  const rel = path.relative(repoRoot, abs).replace(/\\/g, '/');
  return CANONICAL_PRODUCTION_PREFIXES.some((prefix) => rel.startsWith(prefix));
}

export function resolveGuardedOutputPath(requestedPath, { diagnostic = false, repoRoot = REPO_ROOT } = {}) {
  const abs = path.isAbsolute(requestedPath)
    ? requestedPath
    : path.resolve(repoRoot, requestedPath);

  if (!diagnostic && !isCanonicalProductionPath(abs, repoRoot)) {
    return { path: abs, redirected: false, output_class: 'export' };
  }

  if (!diagnostic && isCanonicalProductionPath(abs, repoRoot)) {
    return {
      allowed: false,
      path: abs,
      redirected: false,
      blocker_code: 'CANONICAL_PATH_WRITE_FORBIDDEN',
      message: 'Ungated legacy output cannot write to canonical production path',
    };
  }

  const base = path.basename(abs);
  const quarantinePath = path.join(QUARANTINE_ROOT, `${Date.now()}-${base}`);
  fs.mkdirSync(path.dirname(quarantinePath), { recursive: true });
  return {
    path: quarantinePath,
    redirected: true,
    original_path: abs,
    output_class: 'diagnostic',
    quarantine_root: QUARANTINE_ROOT,
  };
}

export function assertNoCanonicalMutation(beforeSnapshot, afterSnapshot) {
  const violations = [];
  for (const p of afterSnapshot) {
    if (!beforeSnapshot.includes(p) && isCanonicalProductionPath(p)) {
      violations.push(p);
    }
  }
  return { ok: violations.length === 0, violations };
}

export function snapshotCanonicalFiles(repoRoot = REPO_ROOT) {
  const found = [];
  for (const prefix of CANONICAL_PRODUCTION_PREFIXES) {
    const dir = path.join(repoRoot, prefix);
    if (!fs.existsSync(dir)) continue;
    walk(dir, (f) => found.push(path.relative(repoRoot, f).replace(/\\/g, '/')));
  }
  return found;
}

function walk(dir, onFile) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, onFile);
    else onFile(full);
  }
}
