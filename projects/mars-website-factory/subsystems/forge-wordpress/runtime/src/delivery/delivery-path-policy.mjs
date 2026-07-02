/**
 * FW-07C-2C — FP-0002 filesystem delivery path policy (allowlist + denylist).
 */
import fs from 'node:fs';
import path from 'node:path';
import { validatePath } from '../../../enforcement/src/path-validator.mjs';
import { validateReparseBoundary } from '../reparse-boundary-validator.mjs';
import { DELIVERY_REASON_CODES as RC } from './delivery-reason-codes.mjs';

export const FP0002_SITE_ROOT = 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky';
export const FP0002_SITE_ID = 'fp-0002-shpigovsky';
export const FP0002_DOMAIN = 'http://shpigovsky.test/';
export const REQUIRED_VOLUME_LABEL = 'AI WS';

export const DELIVERY_SURFACES = Object.freeze({
  theme: {
    package_id: 'shpigovsky-theme-foundation',
    source_subpath: 'theme/shpigovsky',
    target_root: `${FP0002_SITE_ROOT}\\wp-content\\themes\\shpigovsky`,
    proof_subdir: '.forge-proof',
  },
  plugin: {
    package_id: 'shpigovsky-core-foundation',
    source_subpath: 'plugins/shpigovsky-core',
    target_root: `${FP0002_SITE_ROOT}\\wp-content\\plugins\\shpigovsky-core`,
    proof_subdir: '.forge-proof',
  },
  acf_json: {
    package_id: 'fp-0002-acf-json-foundation',
    source_subpath: 'acf-json',
    target_root: `${FP0002_SITE_ROOT}\\wp-content\\acf-json`,
    proof_subdir: null,
  },
});

/** Paths that must always be rejected for delivery writes. */
export const DENIED_DELIVERY_TARGETS = Object.freeze([
  `${FP0002_SITE_ROOT}\\wp-admin`,
  `${FP0002_SITE_ROOT}\\wp-includes`,
  `${FP0002_SITE_ROOT}\\wp-content\\plugins\\metacode-wpilot`,
  `${FP0002_SITE_ROOT}\\wp-content\\mu-plugins`,
  `${FP0002_SITE_ROOT}\\wp-content\\uploads`,
  `${FP0002_SITE_ROOT}\\wp-config.php`,
  `${FP0002_SITE_ROOT}\\..\\`,
  'X:\\MARS-Localhost\\sites\\wordpress\\projects\\',
  'X:\\MARS-Localhost\\',
  'C:\\',
  'D:\\',
  'E:\\',
  'X:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v9\\src',
  'X:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v9\\dist',
  'X:\\AI MARS\\local\\tokens',
]);

const ALLOWED_TARGET_ROOTS = Object.values(DELIVERY_SURFACES).map((s) => s.target_root);

export function resolveSurfaceForTarget(targetPath) {
  const normalized = targetPath.replace(/\//g, '\\');
  for (const [key, surface] of Object.entries(DELIVERY_SURFACES)) {
    const root = surface.target_root;
    if (normalized === root || normalized.startsWith(root + '\\')) {
      return { surface: key, ...surface };
    }
  }
  return null;
}

function isUnderAllowedSurface(normalized) {
  return ALLOWED_TARGET_ROOTS.some((r) => normalized === r || normalized.startsWith(r + '\\'));
}

function matchesDeniedTarget(normalized, denied) {
  const d = denied.replace(/\//g, '\\');
  if (normalized === d) return true;
  if (d.endsWith('\\') && normalized.startsWith(d)) return true;
  if (!d.endsWith('\\') && normalized.startsWith(d + '\\')) return true;
  return false;
}

function nearestExistingAncestor(filePath) {
  let current = filePath;
  while (current && !fs.existsSync(current)) {
    const parent = path.dirname(current);
    if (parent === current) break;
    current = parent;
  }
  return current;
}

export function validateDeliveryTarget(targetPath, { siteRoot = FP0002_SITE_ROOT } = {}) {
  const reason_codes = [];
  const normalized = String(targetPath).replace(/\//g, '\\');

  if (/v9\\src|v9\\dist|local\\tokens/i.test(normalized)) {
    reason_codes.push(RC.DL_V9_SOURCE_DENIED);
  }

  const surface = resolveSurfaceForTarget(normalized);

  if (surface) {
    const reparseTarget = fs.existsSync(normalized)
      ? normalized
      : nearestExistingAncestor(path.dirname(normalized));
    const reparse = validateReparseBoundary(reparseTarget, surface.target_root);
    if (!reparse.allowed) {
      reason_codes.push(RC.DL_REPARSE_ESCAPE);
    }
    return {
      allowed: reason_codes.length === 0,
      reason_codes: [...new Set(reason_codes)],
      target_path: normalized,
      surface: surface.surface,
      reparse,
    };
  }

  for (const denied of DENIED_DELIVERY_TARGETS) {
    if (matchesDeniedTarget(normalized, denied)) {
      reason_codes.push(RC.DL_PATH_DENIED);
      break;
    }
  }

  if (!reason_codes.includes(RC.DL_PATH_DENIED)) {
    const pathResult = validatePath({ raw_path: normalized, allowed_root: siteRoot });
    if (!pathResult.allowed) {
      reason_codes.push(RC.DL_PATH_DENIED);
    } else if (!isUnderAllowedSurface(normalized)) {
      reason_codes.push(RC.DL_PATH_DENIED);
    }
  }

  return {
    allowed: reason_codes.length === 0,
    reason_codes: [...new Set(reason_codes)],
    target_path: normalized,
    surface: null,
    reparse: null,
  };
}

export function validateVolumeLabel(label) {
  return {
    allowed: label === REQUIRED_VOLUME_LABEL,
    label,
    required: REQUIRED_VOLUME_LABEL,
    reason_codes: label === REQUIRED_VOLUME_LABEL ? [] : [RC.DL_VOLUME_MISMATCH],
  };
}

export default {
  FP0002_SITE_ROOT,
  FP0002_SITE_ID,
  DELIVERY_SURFACES,
  DENIED_DELIVERY_TARGETS,
  validateDeliveryTarget,
  validateVolumeLabel,
};
