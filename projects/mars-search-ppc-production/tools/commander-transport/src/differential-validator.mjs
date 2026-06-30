/**
 * Differential validator — compares frozen authority / previous package / new package.
 */

import { createHash } from 'node:crypto';
import fs from 'node:fs';
import ExcelJS from 'exceljs';
import { sanitizationCellValue as cellText } from './template-sanitizer.mjs';
import { DATA_START_ROW, FORENSIC_COL } from './workbook-forensic-verifier.mjs';

export const CHANGE_TYPES = Object.freeze({
  EXPECTED_GENERATION_CHANGE: 'EXPECTED_GENERATION_CHANGE',
  EXPECTED_VERSION_CHANGE: 'EXPECTED_VERSION_CHANGE',
  EXPECTED_METADATA_CLEAR: 'EXPECTED_METADATA_CLEAR',
  SEMANTIC_CHANGE: 'SEMANTIC_CHANGE',
  STRUCTURAL_CHANGE: 'STRUCTURAL_CHANGE',
  UNEXPECTED_CHANGE: 'UNEXPECTED_CHANGE',
});

const HOTFIX_ALLOWED = new Set([
  'file_version',
  'timestamps',
  'checksums',
  'manifest_references',
  'e9_clear_operation',
  'EXPECTED_METADATA_CLEAR',
]);

/**
 * Extract deterministic snapshot from XLSX for comparison.
 */
export async function snapshotXlsx(xlsxPath) {
  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(xlsxPath);
  const texts = workbook.getWorksheet('Тексты');
  if (!texts) throw new Error(`Missing Тексты sheet in ${xlsxPath}`);

  const phrases = [];
  const ads = [];
  const bids = [];
  const urls = [];
  const regions = new Set();

  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const h1 = cellText(texts, r, FORENSIC_COL.headline_1);
    const phrase = cellText(texts, r, FORENSIC_COL.phrase);
    const group = cellText(texts, r, FORENSIC_COL.group_name);
    const bid = cellText(texts, r, FORENSIC_COL.bid);
    const url = cellText(texts, r, FORENSIC_COL.landing_url);
    const region = cellText(texts, r, FORENSIC_COL.region);

    if (phrase) phrases.push({ group, phrase, bid });
    if (h1) ads.push({ group, h1, url });
    if (bid) bids.push(bid);
    if (url) urls.push(url);
    if (region) regions.add(region);
  }

  const e9 = cellText(texts, 9, 5);
  const org = cellText(texts, 12, 5);

  return {
    phrases: phrases.sort((a, b) => a.phrase.localeCompare(b.phrase)),
    ads: ads.sort((a, b) => a.group.localeCompare(b.group)),
    bids,
    urls,
    regions: [...regions].sort(),
    metadata: { e9, organization: org },
    hash: hashSnapshot({ phrases, ads, bids, urls, regions: [...regions], metadata: { e9, org } }),
  };
}

function hashSnapshot(obj) {
  return createHash('sha256').update(JSON.stringify(obj)).digest('hex');
}

/**
 * Compare two XLSX snapshots.
 * @param {object} previous
 * @param {object} current
 * @param {object} [options]
 */
export function compareSnapshots(previous, current, options = {}) {
  const changes = [];
  const mode = options.mode ?? 'full'; // 'hotfix' for V2.6 → V2.6.1

  if (JSON.stringify(previous.phrases) !== JSON.stringify(current.phrases)) {
    changes.push({
      type: CHANGE_TYPES.SEMANTIC_CHANGE,
      field: 'phrases',
      previous_count: previous.phrases.length,
      current_count: current.phrases.length,
    });
  }

  if (JSON.stringify(previous.ads) !== JSON.stringify(current.ads)) {
    changes.push({
      type: CHANGE_TYPES.STRUCTURAL_CHANGE,
      field: 'ads',
      previous_count: previous.ads.length,
      current_count: current.ads.length,
    });
  }

  if (JSON.stringify(previous.bids) !== JSON.stringify(current.bids)) {
    changes.push({
      type: CHANGE_TYPES.UNEXPECTED_CHANGE,
      field: 'bids',
    });
  }

  if (JSON.stringify(previous.urls) !== JSON.stringify(current.urls)) {
    changes.push({
      type: CHANGE_TYPES.UNEXPECTED_CHANGE,
      field: 'urls',
    });
  }

  if (JSON.stringify(previous.regions) !== JSON.stringify(current.regions)) {
    changes.push({
      type: CHANGE_TYPES.UNEXPECTED_CHANGE,
      field: 'regions',
      previous: previous.regions,
      current: current.regions,
    });
  }

  if (previous.metadata.e9 !== current.metadata.e9) {
    const cleared = previous.metadata.e9 && !current.metadata.e9;
    changes.push({
      type: cleared ? CHANGE_TYPES.EXPECTED_METADATA_CLEAR : CHANGE_TYPES.UNEXPECTED_CHANGE,
      field: 'e9',
      previous: previous.metadata.e9,
      current: current.metadata.e9,
    });
  }

  if (previous.metadata.organization !== current.metadata.organization) {
    changes.push({
      type: CHANGE_TYPES.EXPECTED_METADATA_CLEAR,
      field: 'organization',
      previous: previous.metadata.organization,
      current: current.metadata.organization,
    });
  }

  if (mode === 'hotfix') {
    const forbidden = changes.filter(
      (c) =>
        !HOTFIX_ALLOWED.has(c.field) &&
        c.type !== CHANGE_TYPES.EXPECTED_METADATA_CLEAR &&
        c.type !== CHANGE_TYPES.EXPECTED_VERSION_CHANGE
    );
    return {
      status: forbidden.length === 0 ? 'SCRIPT_PASS' : 'SCRIPT_FAIL',
      mode: 'hotfix',
      changes,
      forbidden_changes: forbidden,
    };
  }

  return {
    status: changes.length === 0 ? 'SCRIPT_PASS' : 'SCRIPT_FAIL',
    mode,
    changes,
  };
}

/**
 * Compare two XLSX files on disk.
 */
export async function differentialValidate(previousPath, currentPath, options = {}) {
  const previous = await snapshotXlsx(previousPath);
  const current = await snapshotXlsx(currentPath);
  return {
    ...compareSnapshots(previous, current, options),
    previous_path: previousPath,
    current_path: currentPath,
    previous_hash: previous.hash,
    current_hash: current.hash,
  };
}

/**
 * Compare package manifests (checksums, version refs).
 */
export function differentialValidateManifests(previousManifest, currentManifest, options = {}) {
  const changes = [];
  const allowedOnly = options.allowedFields ?? [
    'release_version',
    'generation_timestamp',
    'checksums',
    'transport_version',
    'validator_version',
  ];

  for (const key of Object.keys({ ...previousManifest, ...currentManifest })) {
    if (JSON.stringify(previousManifest[key]) === JSON.stringify(currentManifest[key])) continue;
    const type = allowedOnly.includes(key)
      ? CHANGE_TYPES.EXPECTED_VERSION_CHANGE
      : CHANGE_TYPES.UNEXPECTED_CHANGE;
    changes.push({ type, field: key, previous: previousManifest[key], current: currentManifest[key] });
  }

  const forbidden = changes.filter((c) => c.type === CHANGE_TYPES.UNEXPECTED_CHANGE);
  return {
    status: forbidden.length === 0 ? 'SCRIPT_PASS' : 'SCRIPT_FAIL',
    changes,
    forbidden_changes: forbidden,
  };
}
