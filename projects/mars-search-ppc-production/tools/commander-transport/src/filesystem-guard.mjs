import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import {
  APPROVED_WRITE_ROOT,
  DEPRECATED_DRIVES,
  OUTPUT_POLICY_FAIL_IF_EXISTS,
  PROJECT_ROOT,
  REPO_ROOT,
  REQUIRED_DRIVE,
  REQUIRED_VOLUME_LABEL,
} from './constants.mjs';

/**
 * @typedef {object} GuardOptions
 * @property {string} [approvedWriteRoot]
 * @property {boolean} [skipVolumeCheck]
 * @property {string} [overwriteExact]
 */

/**
 * @typedef {object} GuardContext
 * @property {string} approvedWriteRoot
 * @property {string} outputPolicy
 */

let cachedVolumeLabel = null;

export function getVolumeLabel(driveLetter = 'X') {
  if (cachedVolumeLabel !== null) return cachedVolumeLabel;
  try {
    const out = execSync(
      `(Get-Volume -DriveLetter ${driveLetter}).FileSystemLabel`,
      { encoding: 'utf8', shell: 'powershell.exe' }
    ).trim();
    cachedVolumeLabel = out;
    return out;
  } catch {
    return null;
  }
}

export function resetVolumeLabelCache() {
  cachedVolumeLabel = null;
}

export function isUncPath(inputPath) {
  const normalized = String(inputPath).replace(/\//g, '\\');
  return normalized.startsWith('\\\\');
}

export function normalizeInputPath(inputPath) {
  if (!inputPath || typeof inputPath !== 'string') {
    throw new Error('Path must be a non-empty string');
  }
  if (isUncPath(inputPath)) {
    throw new Error('UNC paths are rejected');
  }
  const drive = path.parse(path.resolve(inputPath)).root;
  const driveLetter = drive.slice(0, 2).toUpperCase();
  if (DEPRECATED_DRIVES.includes(driveLetter)) {
    throw new Error(`Deprecated drive rejected: ${driveLetter}`);
  }
  if (driveLetter !== REQUIRED_DRIVE) {
    throw new Error(`Drive letter must be ${REQUIRED_DRIVE}, got ${driveLetter || '(none)'}`);
  }
  return path.normalize(path.resolve(inputPath));
}

export function assertVolumeIdentity(options = {}) {
  if (options.skipVolumeCheck) return;
  const label = getVolumeLabel('X');
  if (label !== REQUIRED_VOLUME_LABEL) {
    throw new Error(
      `STOP — X VOLUME IDENTITY MISMATCH (expected "${REQUIRED_VOLUME_LABEL}", got "${label ?? 'UNKNOWN'}")`
    );
  }
}

export function createGuardContext(options = {}) {
  assertVolumeIdentity(options);
  return {
    approvedWriteRoot: normalizeInputPath(options.approvedWriteRoot ?? APPROVED_WRITE_ROOT),
    outputPolicy: OUTPUT_POLICY_FAIL_IF_EXISTS,
  };
}

export function isInsideRoot(candidate, root) {
  const normalizedRoot = path.normalize(root);
  const normalizedCandidate = path.normalize(candidate);
  const rel = path.relative(normalizedRoot, normalizedCandidate);
  if (rel === '') return true;
  return !rel.startsWith('..') && !path.isAbsolute(rel);
}

export function assertReadablePath(inputPath, options = {}) {
  const resolved = normalizeInputPath(inputPath);
  assertVolumeIdentity(options);
  if (!fs.existsSync(resolved)) {
    throw new Error(`Path does not exist: ${resolved}`);
  }
  return resolved;
}

export function assertApprovedOutputPath(outputPath, context, options = {}) {
  const resolved = normalizeInputPath(outputPath);
  assertVolumeIdentity(options);

  if (resolved.includes('*') || resolved.includes('?')) {
    throw new Error('Wildcard output paths are rejected');
  }

  const repoNorm = path.normalize(REPO_ROOT);
  const projectNorm = path.normalize(PROJECT_ROOT);

  if (resolved === repoNorm || resolved === projectNorm) {
    throw new Error('Repository or project root cannot be used as output directory');
  }

  const storageRoot = path.join('X:', 'AI MARS STORAGE');
  if (resolved === path.normalize(storageRoot)) {
    throw new Error('Storage root cannot be used as output directory');
  }

  if (!isInsideRoot(resolved, context.approvedWriteRoot)) {
    throw new Error(`Output outside approved write root: ${resolved}`);
  }

  if (context.outputPolicy === OUTPUT_POLICY_FAIL_IF_EXISTS) {
    if (options.overwriteExact) {
      const exact = normalizeInputPath(options.overwriteExact);
      if (exact !== resolved) {
        throw new Error('--overwrite-exact must match resolved output file exactly');
      }
    } else if (fs.existsSync(resolved)) {
      throw new Error(`FAIL_IF_OUTPUT_EXISTS: ${resolved}`);
    }
  }

  return resolved;
}

export function assertNoTraversal(fromPath, mustStayUnder) {
  const resolved = normalizeInputPath(fromPath);
  const root = normalizeInputPath(mustStayUnder);
  if (!isInsideRoot(resolved, root)) {
    throw new Error(`Parent traversal escapes approved root: ${resolved}`);
  }
  return resolved;
}

export function resolveRealPathSafe(inputPath, options = {}) {
  const resolved = normalizeInputPath(inputPath);
  assertVolumeIdentity(options);
  try {
    return fs.realpathSync.native(resolved);
  } catch {
    return resolved;
  }
}
