/**
 * Row-level phrase-slot reconciliation — frozen deployable authority vs actual XLSX keyword rows.
 *
 * Counting contract:
 * - A deployable phrase slot = one keyword row expected in Commander import XLSX (Тексты sheet, row >= 16, phrase col populated).
 * - Authority source of truth for deployable slots: FINAL-GROUP-PLAN phrase_list entries (one slot per campaign/mode/group/phrase).
 * - Artifact source: non-blank phrase cells in each package XLSX.
 * - Slot key: campaign_id | mode | group_id | normalized_phrase
 */

import fs from 'node:fs';
import path from 'node:path';
import ExcelJS from 'exceljs';
import { DATA_START_ROW, FORENSIC_COL } from './workbook-forensic-verifier.mjs';
import { sanitizationCellValue as cellText } from './template-sanitizer.mjs';
import { normalizePhrase, phraseSlotKey, parseCampaignMode } from './phrase-normalizer.mjs';

/**
 * Build expected deployable slots from frozen group plan.
 * @param {object} groupPlan — { groups: [...] }
 * @param {object} [options]
 */
export function buildExpectedSlotsFromGroupPlan(groupPlan, options = {}) {
  const slots = [];
  let slotSeq = 0;
  for (const g of groupPlan.groups ?? []) {
    const phrases = String(g.phrase_list ?? '')
      .split(';')
      .map((p) => p.trim())
      .filter(Boolean);
    const campaignId = g.campaign;
    const mode = g.mode ?? parseCampaignMode(campaignId);
    for (const phrase of phrases) {
      slotSeq += 1;
      slots.push({
        slot_id: `EXP-${String(slotSeq).padStart(6, '0')}`,
        campaign_id: campaignId,
        campaign_name: options.campaignNames?.[campaignId] ?? campaignId,
        service: g.commercial_intent ?? campaignId?.split('-')?.slice(0, 2)?.join('-'),
        mode,
        group_id: g.group_id,
        group_name: g.group_name,
        phrase,
        normalized_phrase: normalizePhrase(phrase),
        source_decision: 'DEPLOYABLE_GROUP_PLAN',
        source_geo: mode,
        expected_xlsx: options.filenameForCampaign?.(campaignId) ?? '',
        authority_source_file: options.authority_source_file ?? 'group_plan',
        authority_source_row_or_key: `${campaignId}::${g.group_id}::${normalizePhrase(phrase)}`,
        slot_key: phraseSlotKey(campaignId, mode, g.group_id, phrase),
      });
    }
  }
  return slots;
}

/**
 * Extract actual keyword rows from one XLSX artifact.
 */
export async function extractArtifactSlotsFromXlsx(xlsxPath, options = {}) {
  const filename = options.filename ?? path.basename(xlsxPath);
  const campaignId = options.campaign_id ?? inferCampaignIdFromFilename(filename);
  const mode = options.mode ?? parseCampaignMode(campaignId);
  const groupIdByName = options.group_id_by_name ?? new Map();
  const slots = [];

  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(xlsxPath);
  const texts = workbook.getWorksheet('Тексты');
  if (!texts) {
    return { slots, error: 'MISSING_SHEET_TEXTS' };
  }

  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const phrase = cellText(texts, r, FORENSIC_COL.phrase);
    if (!phrase) continue;
    const groupName = cellText(texts, r, FORENSIC_COL.group_name);
    const groupId = groupIdByName.get(`${campaignId}::${groupName}`) ?? options.default_group_id ?? '';
    const bid = cellText(texts, r, FORENSIC_COL.bid);
    const landingUrl = cellText(texts, r, FORENSIC_COL.landing_url);
    slots.push({
      filename,
      campaign_id: campaignId,
      campaign_name: options.campaign_name ?? campaignId,
      mode,
      xlsx_row: r,
      group_id: groupId,
      group_name: groupName,
      phrase,
      normalized_phrase: normalizePhrase(phrase),
      bid,
      landing_url: landingUrl,
      slot_key: phraseSlotKey(campaignId, mode, groupId, phrase),
    });
  }
  return { slots };
}

function inferCampaignIdFromFilename(filename) {
  const m = String(filename).match(/(CA-\d+-(?:LOCAL|REMOTE))/i);
  return m ? m[1].toUpperCase() : '';
}

/**
 * Reconcile expected authority slots against artifact slots (package-wide).
 */
export function reconcilePhraseSlotSets(expectedSlots, artifactSlots) {
  const expectedByKey = new Map();
  const artifactByKey = new Map();
  const authorityDuplicates = [];
  const duplicateInArtifact = [];
  const normalizationCollisions = [];
  const artifactBlankRows = [];

  const expectedNormIndex = new Map();
  for (const s of expectedSlots) {
    if (expectedByKey.has(s.slot_key)) {
      authorityDuplicates.push({ ...s, duplicate_of: expectedByKey.get(s.slot_key).slot_id });
    } else {
      expectedByKey.set(s.slot_key, s);
    }
    const normOnly = `${s.campaign_id}|${s.mode}|${s.normalized_phrase}`;
    if (!expectedNormIndex.has(normOnly)) expectedNormIndex.set(normOnly, []);
    expectedNormIndex.get(normOnly).push(s);
  }

  const artifactNormSeen = new Map();
  for (const s of artifactSlots) {
    if (!s.phrase?.trim()) {
      artifactBlankRows.push(s);
      continue;
    }
    if (artifactByKey.has(s.slot_key)) {
      duplicateInArtifact.push({ ...s, duplicate_of: artifactByKey.get(s.slot_key).xlsx_row });
    } else {
      artifactByKey.set(s.slot_key, s);
    }
    const normOnly = `${s.campaign_id}|${s.mode}|${s.normalized_phrase}`;
    if (!artifactNormSeen.has(normOnly)) artifactNormSeen.set(normOnly, []);
    artifactNormSeen.get(normOnly).push(s);
  }

  for (const [normOnly, arts] of artifactNormSeen) {
    const exps = expectedNormIndex.get(normOnly) ?? [];
    if (arts.length > 1 || (exps.length === 1 && arts.length === 1 && arts[0].group_id !== exps[0].group_id)) {
      if (arts.length > 1 || (exps[0] && arts[0].group_id !== exps[0].group_id)) {
        normalizationCollisions.push({
          norm_key: normOnly,
          expected: exps,
          artifact: arts,
        });
      }
    }
  }

  const expected_and_present = [];
  const expected_but_missing = [];
  for (const [key, exp] of expectedByKey) {
    const art = artifactByKey.get(key);
    if (art) expected_and_present.push({ expected: exp, artifact: art });
    else expected_but_missing.push(exp);
  }

  const unexpected_in_artifact = [];
  for (const [key, art] of artifactByKey) {
    if (!expectedByKey.has(key)) unexpected_in_artifact.push(art);
  }

  const authority_phrase_slots = expectedByKey.size;
  const artifact_phrase_slots = artifactByKey.size;
  const phrase_slot_delta = artifact_phrase_slots - authority_phrase_slots;

  const missing_slots = expected_but_missing.length;
  const unexpected_slots = unexpected_in_artifact.length;
  const duplicate_slots = duplicateInArtifact.length;
  const phrase_slot_reconciliation_pass =
    phrase_slot_delta === 0 &&
    missing_slots === 0 &&
    unexpected_slots === 0 &&
    duplicate_slots === 0 &&
    authorityDuplicates.length === 0;

  return {
    authority_phrase_slots,
    artifact_phrase_slots,
    phrase_slot_delta,
    missing_slots,
    unexpected_slots,
    duplicate_slots,
    authority_duplicate_count: authorityDuplicates.length,
    phrase_slot_reconciliation_pass,
    expected_and_present,
    expected_but_missing,
    unexpected_in_artifact,
    duplicate_in_artifact: duplicateInArtifact,
    authority_duplicates: authorityDuplicates,
    artifact_blank_rows: artifactBlankRows,
    normalization_collisions: normalizationCollisions,
  };
}

function aggregateCampaignReconciliation(expectedSlots, artifactSlots, reconcileResult) {
  const campaigns = [...new Set([...expectedSlots.map((s) => s.campaign_id), ...artifactSlots.map((s) => s.campaign_id)])].sort();
  return campaigns.map((campaignId) => {
    const exp = expectedSlots.filter((s) => s.campaign_id === campaignId).length;
    const art = artifactSlots.filter((s) => s.campaign_id === campaignId).length;
    const missing = reconcileResult.expected_but_missing.filter((s) => s.campaign_id === campaignId);
    const unexpected = reconcileResult.unexpected_in_artifact.filter((s) => s.campaign_id === campaignId);
    const duplicates = reconcileResult.duplicate_in_artifact.filter((s) => s.campaign_id === campaignId);
    return {
      campaign_id: campaignId,
      authority_phrase_slots: exp,
      artifact_phrase_slots: art,
      phrase_slot_delta: art - exp,
      missing_slots: missing.length,
      unexpected_slots: unexpected.length,
      duplicate_slots: duplicates.length,
      pass: art === exp && missing.length === 0 && unexpected.length === 0 && duplicates.length === 0,
    };
  });
}

function aggregateGroupReconciliation(expectedSlots, artifactSlots, reconcileResult) {
  const keys = new Set([
    ...expectedSlots.map((s) => `${s.campaign_id}::${s.group_id}`),
    ...artifactSlots.map((s) => `${s.campaign_id}::${s.group_id}`),
  ]);
  return [...keys].sort().map((gk) => {
    const [campaignId, groupId] = gk.split('::');
    const exp = expectedSlots.filter((s) => s.campaign_id === campaignId && s.group_id === groupId).length;
    const art = artifactSlots.filter((s) => s.campaign_id === campaignId && s.group_id === groupId).length;
    const groupName =
      expectedSlots.find((s) => s.campaign_id === campaignId && s.group_id === groupId)?.group_name ??
      artifactSlots.find((s) => s.campaign_id === campaignId && s.group_id === groupId)?.group_name ??
      '';
    return {
      campaign_id: campaignId,
      group_id: groupId,
      group_name: groupName,
      authority_phrase_slots: exp,
      artifact_phrase_slots: art,
      phrase_slot_delta: art - exp,
      pass: art === exp,
    };
  });
}

/**
 * Full package phrase-slot reconciliation.
 */
export async function reconcilePackagePhraseSlots(input) {
  const {
    group_plan: groupPlan,
    architecture,
    package_root: packageRoot,
    xlsx_files: xlsxFiles,
    authority_source_file,
  } = input;

  const groupIdByName = new Map();
  const campaignNames = {};
  for (const g of architecture?.groups ?? []) {
    groupIdByName.set(`${g.campaign_id}::${g.group_name}`, g.group_id);
    campaignNames[g.campaign_id] = g.commander_name ?? g.campaign_id;
  }

  const filenameForCampaign = (campaignId) => {
    const f = (xlsxFiles ?? []).find((name) => name.toUpperCase().includes(campaignId.replace('-', '-')));
    return f ?? '';
  };

  const expectedSlots = buildExpectedSlotsFromGroupPlan(groupPlan, {
    group_id_by_name: groupIdByName,
    campaignNames,
    filenameForCampaign,
    authority_source_file,
  });

  const artifactSlots = [];
  for (const rel of xlsxFiles ?? []) {
    const fullPath = path.isAbsolute(rel) ? rel : path.join(packageRoot, rel);
    const campaignId = inferCampaignIdFromFilename(path.basename(rel));
    const { slots, error } = await extractArtifactSlotsFromXlsx(fullPath, {
      filename: path.basename(rel),
      campaign_id: campaignId,
      group_id_by_name: groupIdByName,
      campaign_name: campaignNames[campaignId],
    });
    if (error) {
      return { status: 'RECONCILIATION_FAIL', error, expected_slots: expectedSlots, artifact_slots: [] };
    }
    artifactSlots.push(...slots);
  }

  const result = reconcilePhraseSlotSets(expectedSlots, artifactSlots);
  return {
    status: result.phrase_slot_reconciliation_pass ? 'RECONCILED' : 'RECONCILIATION_FAIL',
    ...result,
    campaign_reconciliation: aggregateCampaignReconciliation(expectedSlots, artifactSlots, result),
    group_reconciliation: aggregateGroupReconciliation(expectedSlots, artifactSlots, result),
    missing_slots_list: result.expected_but_missing,
    unexpected_slots_list: result.unexpected_in_artifact,
    duplicate_slots_list: result.duplicate_in_artifact,
    expected_slots: expectedSlots,
    artifact_slots: artifactSlots,
    reconciled_at: new Date().toISOString(),
  };
}

/**
 * Write CSV reconciliation outputs.
 */
export function writePhraseSlotCsvOutputs(outputDir, reconcilePackage) {
  fs.mkdirSync(outputDir, { recursive: true });
  const esc = (v) => {
    const s = String(v ?? '');
    return s.includes(',') || s.includes('"') || s.includes('\n') ? `"${s.replace(/"/g, '""')}"` : s;
  };
  const writeCsv = (filename, headers, rows) => {
    const lines = [headers.join(',')];
    for (const row of rows) {
      lines.push(headers.map((h) => esc(row[h])).join(','));
    }
    fs.writeFileSync(path.join(outputDir, filename), lines.join('\n') + '\n', 'utf8');
  };

  const fullHeaders = [
    'slot_id', 'campaign_id', 'campaign_name', 'service', 'mode', 'group_id', 'group_name',
    'phrase', 'normalized_phrase', 'source_decision', 'source_geo', 'expected_xlsx',
    'authority_source_file', 'authority_source_row_or_key', 'status',
    'filename', 'xlsx_row', 'bid', 'landing_url',
  ];

  const fullRows = [];
  for (const pair of reconcilePackage.expected_and_present ?? []) {
    fullRows.push({
      ...pair.expected,
      status: 'expected_and_present',
      filename: pair.artifact.filename,
      xlsx_row: pair.artifact.xlsx_row,
      bid: pair.artifact.bid,
      landing_url: pair.artifact.landing_url,
    });
  }
  for (const m of reconcilePackage.expected_but_missing ?? []) {
    fullRows.push({ ...m, status: 'expected_but_missing', filename: '', xlsx_row: '', bid: '', landing_url: '' });
  }
  for (const u of reconcilePackage.unexpected_in_artifact ?? []) {
    fullRows.push({
      slot_id: '',
      campaign_id: u.campaign_id,
      campaign_name: u.campaign_name,
      service: '',
      mode: u.mode,
      group_id: u.group_id,
      group_name: u.group_name,
      phrase: u.phrase,
      normalized_phrase: u.normalized_phrase,
      source_decision: '',
      source_geo: '',
      expected_xlsx: '',
      authority_source_file: '',
      authority_source_row_or_key: '',
      status: 'unexpected_in_artifact',
      filename: u.filename,
      xlsx_row: u.xlsx_row,
      bid: u.bid,
      landing_url: u.landing_url,
    });
  }

  writeCsv('CORVONERO-V2.6.1-PHRASE-SLOT-RECONCILIATION.csv', fullHeaders, fullRows);
  writeCsv(
    'CORVONERO-V2.6.1-MISSING-SLOTS.csv',
    ['slot_id', 'campaign_id', 'mode', 'group_id', 'group_name', 'phrase', 'normalized_phrase', 'authority_source_row_or_key'],
    reconcilePackage.expected_but_missing ?? [],
  );
  writeCsv(
    'CORVONERO-V2.6.1-UNEXPECTED-SLOTS.csv',
    ['filename', 'campaign_id', 'mode', 'xlsx_row', 'group_id', 'group_name', 'phrase', 'normalized_phrase'],
    reconcilePackage.unexpected_in_artifact ?? [],
  );
  writeCsv(
    'CORVONERO-V2.6.1-DUPLICATE-SLOTS.csv',
    ['filename', 'campaign_id', 'mode', 'xlsx_row', 'group_id', 'group_name', 'phrase', 'normalized_phrase', 'duplicate_of'],
    reconcilePackage.duplicate_in_artifact ?? [],
  );
}

/**
 * Resolve authority file paths from operator receipt artifact list.
 */
export function resolveAuthorityPathsFromReceipt(receipt) {
  const paths = receipt?.authority_artifact_paths ?? [];
  const find = (pattern) => paths.find((p) => pattern.test(path.basename(p.replace(/\\/g, '/'))));
  const authority_manifest_path = find(/AUTHORITY-MANIFEST/i);
  let architecture_path = find(/CAMPAIGN-ARCHITECTURE/i);
  if (!architecture_path && authority_manifest_path && fs.existsSync(authority_manifest_path)) {
    try {
      const manifest = JSON.parse(fs.readFileSync(authority_manifest_path, 'utf8'));
      const archEntry = (manifest.files ?? []).find((f) => f.role === 'campaign_architecture');
      if (archEntry?.path) architecture_path = archEntry.path;
    } catch {
      /* ignore */
    }
  }
  return {
    group_plan_path: find(/FINAL-GROUP-PLAN/i),
    phrase_authority_path: find(/FINAL-PHRASE-AUTHORITY/i),
    architecture_path,
    phrase_allocation_path: find(/PHRASE-ALLOCATION/i),
    authority_manifest_path,
  };
}
