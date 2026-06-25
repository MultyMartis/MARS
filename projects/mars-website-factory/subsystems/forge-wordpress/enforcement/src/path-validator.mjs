/**
 * FW-07C-0 — Forge path validator (pure function, no filesystem mutation).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { REASON_CODES as RC } from './reason-codes.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROTECTED_ROOTS_PATH = path.resolve(__dirname, '../policies/forge-protected-roots-v1.json');

let cachedProtectedRoots = null;

export function loadProtectedRoots() {
  if (!cachedProtectedRoots) {
    const policy = JSON.parse(fs.readFileSync(PROTECTED_ROOTS_PATH, 'utf8'));
    cachedProtectedRoots = policy.protected_roots.map(normalizePathForCompare);
  }
  return cachedProtectedRoots;
}

export function resetProtectedRootsCache() {
  cachedProtectedRoots = null;
}

/** Normalize path for Windows comparison (case-insensitive, forward slashes). */
export function normalizePathForCompare(raw) {
  if (raw == null) return '';
  let p = String(raw).trim();
  p = p.replace(/\//g, '\\');
  while (p.endsWith('\\') && p.length > 3) {
    p = p.slice(0, -1);
  }
  if (/^[a-zA-Z]:\\?$/.test(p)) {
    return p.replace(/\\$/, '') + '\\';
  }
  return p.toUpperCase();
}

/** Produce display normalized path preserving backslashes. */
export function normalizePathDisplay(raw) {
  if (raw == null) return '';
  let p = String(raw).trim().replace(/\//g, '\\');
  while (p.endsWith('\\') && p.length > 3) {
    p = p.slice(0, -1);
  }
  return p;
}

function isDriveRoot(p) {
  const n = normalizePathForCompare(p);
  return /^[A-Z]:\\$/.test(n);
}

function isUncPath(p) {
  const s = String(p).trim();
  return s.startsWith('\\\\') || s.startsWith('//');
}

function hasWildcard(p) {
  return /[*?]/.test(p);
}

function isRelativePath(p) {
  const s = String(p).trim();
  if (!s) return false;
  if (s.startsWith('..')) return true;
  if (s.includes('\\..\\') || s.includes('/../') || s.endsWith('\\..') || s.endsWith('/..')) return true;
  if (!/^[a-zA-Z]:/.test(s) && !s.startsWith('\\\\') && !s.startsWith('//')) return true;
  return false;
}

function hasTraversal(p) {
  const segments = String(p).replace(/\\/g, '/').split('/');
  return segments.some((seg) => seg === '..');
}

function hasTrailingDotOrSpace(p) {
  const s = String(p);
  if (/\.$/.test(s.trim()) && !/^[a-zA-Z]:\\?$/.test(s.trim())) return 'dot';
  if (/\s$/.test(s)) return 'space';
  const parts = s.split('\\');
  const last = parts[parts.length - 1];
  if (last && (last.endsWith('.') || last.endsWith(' '))) {
    return last.endsWith('.') ? 'dot' : 'space';
  }
  return null;
}

function findProtectedRootViolation(normalizedPath, allowedRoot, protectedRoots) {
  const np = normalizePathForCompare(normalizedPath);
  const ar = allowedRoot ? normalizePathForCompare(allowedRoot) : '';

  for (const root of protectedRoots) {
    const nr = normalizePathForCompare(root);
    const rootBare = nr.replace(/\\$/, '');

    if (np === nr || np === rootBare) {
      return root;
    }

    const isUnderProtected =
      np.startsWith(nr) ||
      np.startsWith(rootBare + '\\');

    if (!isUnderProtected) continue;

    if (ar) {
      const allowedUnderProtected = ar.startsWith(rootBare + '\\') || ar === rootBare;
      const targetUnderAllowed = np.startsWith(ar + '\\') || np === ar;
      if (allowedUnderProtected && targetUnderAllowed && ar !== rootBare && ar !== nr) {
        continue;
      }
    }

    return root;
  }
  return null;
}

function isDescendantOf(targetNorm, rootNorm) {
  const t = normalizePathForCompare(targetNorm);
  const r = normalizePathForCompare(rootNorm);
  if (t === r) return true;
  const prefix = r.endsWith('\\') ? r : r + '\\';
  return t.startsWith(prefix);
}

function sharesRuntimeSandboxFamily(targetNorm, allowedRootNorm) {
  const familyPrefix = 'E:\\MARS-LOCALHOST\\SITES\\WORDPRESS\\';
  const t = normalizePathForCompare(targetNorm);
  const a = normalizePathForCompare(allowedRootNorm);
  return t.startsWith(familyPrefix) && a.startsWith(familyPrefix);
}

function isExactRootMatch(targetNorm, rootNorm) {
  return normalizePathForCompare(targetNorm) === normalizePathForCompare(rootNorm);
}

/**
 * Validate a filesystem path against allowed root and protected roots.
 * @param {object} input
 * @returns {object} validation result
 */
export function validatePath(input) {
  const {
    raw_path,
    allowed_root,
    operation_id = '',
    site_id = '',
    environment = 'LOCAL_SYNTHETIC',
    source_path,
    destination_path,
    disallow_root_mutation = false,
  } = input ?? {};

  const reason_codes = [];
  const protectedRoots = loadProtectedRoots();

  if (raw_path == null || raw_path === undefined) {
    reason_codes.push(RC.FW_PATH_EMPTY);
  }

  const rawStr = raw_path == null ? '' : String(raw_path);
  const normalized_path = normalizePathDisplay(rawStr);
  const allowedRootDisplay = allowed_root ? normalizePathDisplay(allowed_root) : '';

  if (raw_path !== undefined && raw_path !== null && rawStr.trim() === '') {
    reason_codes.push(RC.FW_PATH_EMPTY);
  }

  if (rawStr && /^\s+$/.test(rawStr)) {
    reason_codes.push(RC.FW_PATH_EMPTY);
  }

  if (rawStr && hasWildcard(rawStr)) {
    reason_codes.push(RC.FW_PATH_WILDCARD);
  }

  if (rawStr && isRelativePath(rawStr)) {
    reason_codes.push(RC.FW_PATH_RELATIVE);
  }

  if (rawStr && hasTraversal(rawStr)) {
    reason_codes.push(RC.FW_PATH_TRAVERSAL);
  }

  if (rawStr && isDriveRoot(rawStr)) {
    reason_codes.push(RC.FW_PATH_DRIVE_ROOT);
  }

  if (rawStr && isUncPath(rawStr)) {
    reason_codes.push(RC.FW_PATH_UNC_DENIED);
  }

  const trailing = rawStr ? hasTrailingDotOrSpace(rawStr) : null;
  if (trailing === 'dot') reason_codes.push(RC.FW_PATH_TRAILING_DOT);
  if (trailing === 'space') reason_codes.push(RC.FW_PATH_TRAILING_SPACE);

  const basicInvalid = reason_codes.some((c) =>
    [RC.FW_PATH_EMPTY, RC.FW_PATH_WILDCARD, RC.FW_PATH_RELATIVE, RC.FW_PATH_TRAVERSAL,
      RC.FW_PATH_DRIVE_ROOT, RC.FW_PATH_UNC_DENIED, RC.FW_PATH_TRAILING_DOT, RC.FW_PATH_TRAILING_SPACE].includes(c)
  );

  let protected_root_match = null;
  let is_descendant = false;

  if (rawStr && !basicInvalid) {
    const np = normalizePathForCompare(normalized_path);
    for (const root of protectedRoots) {
      const nr = normalizePathForCompare(root);
      const rootBare = nr.replace(/\\$/, '');
      if (np === nr || np === rootBare) {
        protected_root_match = root;
        reason_codes.push(RC.FW_PATH_PROTECTED_ROOT);
        break;
      }
    }
  }

  if (rawStr && allowed_root && !basicInvalid && !reason_codes.includes(RC.FW_PATH_PROTECTED_ROOT)) {
    is_descendant = isDescendantOf(normalized_path, allowed_root);
    if (!is_descendant) {
      if (sharesRuntimeSandboxFamily(normalized_path, allowed_root)) {
        reason_codes.push(RC.FW_PATH_OUTSIDE_ALLOWED_ROOT);
      } else {
        const crossZoneProtected = findProtectedRootViolation(normalized_path, allowed_root, protectedRoots);
        if (crossZoneProtected) {
          protected_root_match = crossZoneProtected;
          reason_codes.push(RC.FW_PATH_PROTECTED_ROOT);
        } else {
          reason_codes.push(RC.FW_PATH_OUTSIDE_ALLOWED_ROOT);
        }
      }
    }
  } else if (rawStr && allowed_root && !basicInvalid) {
    is_descendant = isDescendantOf(normalized_path, allowed_root);
  }

  if (rawStr && !basicInvalid && !reason_codes.includes(RC.FW_PATH_OUTSIDE_ALLOWED_ROOT) && !reason_codes.includes(RC.FW_PATH_PROTECTED_ROOT)) {
    protected_root_match = findProtectedRootViolation(normalized_path, allowed_root, protectedRoots);
    if (protected_root_match) {
      reason_codes.push(RC.FW_PATH_PROTECTED_ROOT);
    }
  }

  if (
    disallow_root_mutation &&
    rawStr &&
    allowed_root &&
    isExactRootMatch(normalized_path, allowed_root)
  ) {
    reason_codes.push(RC.FW_PATH_ROOT_MUTATION_DENIED);
  }

  if (source_path && destination_path) {
    const src = normalizePathForCompare(source_path);
    const dst = normalizePathForCompare(destination_path);
    if (src === dst) {
      reason_codes.push(RC.FW_PATH_SOURCE_DESTINATION_EQUAL);
    } else if (dst.length < src.length && src.startsWith(dst + '\\')) {
      reason_codes.push(RC.FW_PATH_PARENT_CHILD_REVERSAL);
    }
  }

  const requires_reparse_check = true;

  return {
    allowed: reason_codes.length === 0,
    reason_codes: [...new Set(reason_codes)],
    raw_path: rawStr,
    normalized_path,
    allowed_root: allowedRootDisplay,
    is_descendant,
    protected_root_match,
    requires_reparse_check,
    operation_id,
    site_id,
    environment,
  };
}

export default validatePath;
