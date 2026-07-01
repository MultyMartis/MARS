/**
 * Commander package purity — single deployable version, manifest whitelist, version alignment.
 */

import fs from 'node:fs';
import path from 'node:path';

/**
 * @param {object} input
 */
export function validatePackagePurity(input) {
  const violations = [];
  const packageRoot = input.package_root;
  const expectedVersion = input.package_version;
  const manifest = input.manifest ?? loadManifest(packageRoot, input.manifest_path);

  if (!manifest) {
    violations.push({ code: 'MISSING_MANIFEST', severity: 'HARD_FAIL', message: 'Package manifest required' });
    return { status: 'FAIL', violations };
  }

  const whitelist = new Set(
    (manifest.files ?? manifest.xlsx_files ?? []).map((f) => (typeof f === 'string' ? f : f.path)),
  );

  const xlsxOnDisk = listXlsx(packageRoot);
  const historicalPattern = input.historical_version_pattern ?? /v2\.6\.1|v2\.5|v2\.4|v2\.3|v2\.2|v2\.1/i;

  for (const x of xlsxOnDisk) {
    if (historicalPattern.test(x) && expectedVersion && !x.includes(expectedVersion.replace(/\./g, '.'))) {
      violations.push({
        code: 'MIXED_HISTORICAL_XLSX',
        severity: 'HARD_FAIL',
        message: `Historical XLSX in package: ${x}`,
      });
    }
    if (whitelist.size > 0 && ![...whitelist].some((w) => x.endsWith(w) || w.endsWith(x))) {
      violations.push({
        code: 'UNMANIFESTED_XLSX',
        severity: 'WARNING',
        message: `XLSX not in manifest whitelist: ${x}`,
      });
    }
  }

  for (const ref of whitelist) {
    if (ref.toLowerCase().endsWith('.xlsx') && !fs.existsSync(path.join(packageRoot, ref))) {
      violations.push({
        code: 'MANIFEST_REFERENCE_MISSING',
        severity: 'HARD_FAIL',
        message: `Manifest references missing file: ${ref}`,
      });
    }
  }

  if (expectedVersion) {
    const importOrder = findFile(packageRoot, /IMPORT-ORDER/i);
    const checklist = findFile(packageRoot, /CHECKLIST/i);
    if (importOrder && !fs.readFileSync(importOrder, 'utf8').includes(expectedVersion.replace('V', 'v').toLowerCase())) {
      violations.push({
        code: 'IMPORT_ORDER_VERSION_MISMATCH',
        severity: 'HARD_FAIL',
        message: `Import order version != ${expectedVersion}`,
      });
    }
    if (checklist && !fs.readFileSync(checklist, 'utf8').includes(expectedVersion.replace('V', 'v').toLowerCase())) {
      violations.push({
        code: 'CHECKLIST_VERSION_MISMATCH',
        severity: 'HARD_FAIL',
        message: `Checklist version != ${expectedVersion}`,
      });
    }
    const manifestVersion = manifest.package_version ?? manifest.deployable_version;
    if (manifestVersion && manifestVersion !== expectedVersion) {
      violations.push({
        code: 'MANIFEST_VERSION_MISMATCH',
        severity: 'HARD_FAIL',
        message: `Manifest version ${manifestVersion} != ${expectedVersion}`,
      });
    }
  }

  const hardFails = violations.filter((v) => v.severity === 'HARD_FAIL');
  return { status: hardFails.length === 0 ? 'PASS' : 'FAIL', violations };
}

function loadManifest(packageRoot, explicit) {
  const candidates = explicit ? [explicit] : [];
  if (fs.existsSync(packageRoot)) {
    for (const ent of fs.readdirSync(packageRoot)) {
      if (/OUTPUT-MANIFEST/i.test(ent) && ent.endsWith('.json')) candidates.push(path.join(packageRoot, ent));
    }
  }
  for (const p of candidates) {
    try {
      return JSON.parse(fs.readFileSync(p, 'utf8'));
    } catch { /* next */ }
  }
  return null;
}

function listXlsx(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((f) => f.toLowerCase().endsWith('.xlsx'));
}

function findFile(dir, pattern) {
  if (!fs.existsSync(dir)) return null;
  const hit = fs.readdirSync(dir).find((f) => pattern.test(f));
  return hit ? path.join(dir, hit) : null;
}
