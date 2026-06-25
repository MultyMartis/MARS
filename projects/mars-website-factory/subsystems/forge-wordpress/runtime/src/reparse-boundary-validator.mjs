/**
 * FW-07C-1 — Physical/reparse boundary validator (read-only, no mutation).
 */
import fs from 'node:fs';
import path from 'node:path';
import { normalizePathForCompare, normalizePathDisplay } from '../../enforcement/src/path-validator.mjs';
import { RUNTIME_REASON_CODES as RC } from './runtime-reason-codes.mjs';

const REPARSE_TAG_SYMLINK = 0xa000000c;
const REPARSE_TAG_MOUNT_POINT = 0xa0000003;

function isDescendantOfPhysical(physicalNorm, rootNorm) {
  const p = normalizePathForCompare(physicalNorm);
  const r = normalizePathForCompare(rootNorm);
  if (p === r) return true;
  const prefix = r.endsWith('\\') ? r : r + '\\';
  return p.startsWith(prefix);
}

function getVolumeRoot(targetPath) {
  const match = /^([A-Za-z]:)/.exec(targetPath);
  return match ? match[1].toUpperCase() + '\\' : '';
}

/**
 * Inspect a single path segment for reparse/symlink attributes (lstat, no follow).
 */
function inspectSegment(segmentPath) {
  const entry = {
    segment_path: normalizePathDisplay(segmentPath),
    exists: false,
    is_reparse_point: false,
    is_symlink: false,
    reparse_tag: null,
    link_target: null,
  };

  try {
    const stat = fs.lstatSync(segmentPath);
    entry.exists = true;
    entry.is_symlink = stat.isSymbolicLink();

    if (typeof stat.isJunction === 'function') {
      entry.is_junction = stat.isJunction();
    }

    if (entry.is_symlink) {
      entry.is_reparse_point = true;
      try {
        entry.link_target = fs.readlinkSync(segmentPath);
      } catch {
        entry.link_target = null;
      }
    }
  } catch {
    entry.exists = false;
  }

  return entry;
}

/**
 * Walk path segments from drive root collecting reparse points.
 */
function collectReparsePoints(logicalPath) {
  const reparse_points = [];
  const normalized = path.win32.normalize(logicalPath);
  const parsed = path.win32.parse(normalized);
  let current = parsed.root;

  const relative = normalized.slice(parsed.root.length);
  const segments = relative.split('\\').filter(Boolean);

  const rootEntry = inspectSegment(current);
  if (rootEntry.is_reparse_point || rootEntry.is_symlink) {
    reparse_points.push({ ...rootEntry, segment: '' });
  }

  for (const seg of segments) {
    current = path.win32.join(current, seg);
    const entry = inspectSegment(current);
    if (entry.is_reparse_point || entry.is_symlink || entry.is_junction) {
      reparse_points.push({ ...entry, segment: seg });
    }
  }

  return reparse_points;
}

/**
 * Validate logical path stays within allowed root after physical resolution.
 * @param {string} logicalPath
 * @param {string} allowedRoot
 */
export function validateReparseBoundary(logicalPath, allowedRoot) {
  const reason_codes = [];
  const logical_display = normalizePathDisplay(logicalPath);
  const allowed_display = normalizePathDisplay(allowedRoot);

  let physical_path = '';
  let allowed_physical = '';
  let escape_detected = false;

  try {
    allowed_physical = fs.realpathSync.native(allowedRoot);
    physical_path = fs.realpathSync.native(logicalPath);
  } catch {
    reason_codes.push(RC.RT_REPARSE_UNKNOWN);
    return {
      checked: true,
      allowed: false,
      logical_path: logical_display,
      physical_path: '',
      allowed_root: allowed_display,
      allowed_physical_root: '',
      reparse_points: [],
      escape_detected: true,
      reason_codes,
    };
  }

  const reparse_points = collectReparsePoints(logicalPath);

  const physicalNorm = normalizePathForCompare(physical_path);
  const allowedPhysicalNorm = normalizePathForCompare(allowed_physical);

  if (!isDescendantOfPhysical(physical_path, allowed_physical)) {
    escape_detected = true;
    reason_codes.push(RC.RT_REPARSE_ESCAPE_DETECTED);
  }

  const logicalNorm = normalizePathForCompare(logical_display);
  const allowedLogicalNorm = normalizePathForCompare(allowed_display);

  if (!isDescendantOfPhysical(logical_display, allowedRoot)) {
    escape_detected = true;
    if (!reason_codes.includes(RC.RT_REPARSE_ESCAPE_DETECTED)) {
      reason_codes.push(RC.RT_REPARSE_ESCAPE_DETECTED);
    }
  }

  const volume = getVolumeRoot(physical_path);
  const allowedVolume = getVolumeRoot(allowed_physical);
  if (volume && allowedVolume && volume !== allowedVolume) {
    escape_detected = true;
    reason_codes.push(RC.RT_REPARSE_ESCAPE_DETECTED);
  }

  const allowed = reason_codes.length === 0 && !escape_detected;

  return {
    checked: true,
    allowed,
    logical_path: logical_display,
    physical_path: normalizePathDisplay(physical_path),
    allowed_root: allowed_display,
    allowed_physical_root: normalizePathDisplay(allowed_physical),
    reparse_points,
    escape_detected,
    reason_codes: [...new Set(reason_codes)],
    volume,
    logical_under_allowed: isDescendantOfPhysical(logical_display, allowedRoot),
    physical_under_allowed: isDescendantOfPhysical(physical_path, allowed_physical),
  };
}

export { REPARSE_TAG_SYMLINK, REPARSE_TAG_MOUNT_POINT };
export default validateReparseBoundary;
