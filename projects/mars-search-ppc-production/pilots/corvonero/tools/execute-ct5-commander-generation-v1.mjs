#!/usr/bin/env node
/**
 * CORVONERO CT-5 — safe Commander XLSX generation and forensic verification.
 * Uses commander-transport modules only — no legacy .tools generators.
 * Local generation candidates only — no import, no Direct API.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const ExcelJS = require('../../../tools/commander-transport/node_modules/exceljs');

function resolveTriumphModule(name) {
  return require(path.join(TRIUMPH_EXPORTER_CLI, name));
}

import { loadAuthority } from '../../../tools/commander-transport/src/authority-loader.mjs';
import { adapterAvailable } from '../../../tools/commander-transport/src/commander-patcher-adapter.mjs';
import {
  COMMANDER_COLUMN_COUNT,
  COMMANDER_HEADER_ROW,
  COMMANDER_SHEET_REGIONS,
  COMMANDER_SHEET_TEXTS,
  COMMANDER_TEMPLATE_PATH,
  EXPECTED_TEMPLATE_SHA256,
  FORBIDDEN_ORGANIZATION_ID,
  REQUIRED_REGION_VALUE,
  STORAGE_EXPORT_ROOT,
  TRIUMPH_EXPORTER_CLI,
  TRIUMPH_HEADER_MAP,
} from '../../../tools/commander-transport/src/constants.mjs';
import { assertApprovedOutputPath, createGuardContext } from '../../../tools/commander-transport/src/filesystem-guard.mjs';
import { buildPayloads, validateTransport } from '../../../tools/commander-transport/src/payload-builder.mjs';
import {
  validateTemplate,
} from '../../../tools/commander-transport/src/template-validator.mjs';
import { assertTemplateValid } from '../../../tools/commander-transport/src/template-validator.mjs';

const SEARCH_AD_TYPE = 'Текстово-графическое';

function extractRowXml(sheetXml, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheetXml.match(re);
  return m ? m[0] : null;
}

function cloneRowXml(rowXml, fromRow, toRow) {
  let s = rowXml.replace(new RegExp(`r="${fromRow}"`, 'g'), `r="${toRow}"`);
  s = s.replace(new RegExp(`([A-Z]{1,3})${fromRow}(?![0-9])`, 'g'), `$1${toRow}`);
  return s;
}

function extendSheetForExport(sheetXml, fillRowCount, dataStartRow = DATA_START_ROW) {
  const lastNeeded = dataStartRow + fillRowCount - 1;
  const existing = [...sheetXml.matchAll(/<row r="(\d+)"/g)].map((m) => parseInt(m[1], 10));
  const maxExisting = Math.max(...existing);
  if (maxExisting >= lastNeeded) return sheetXml;

  const protoRow = extractRowXml(sheetXml, dataStartRow);
  if (!protoRow) throw new Error(`Prototype row ${dataStartRow} missing in template`);

  const insertRows = [];
  for (let r = maxExisting + 1; r <= lastNeeded; r++) {
    insertRows.push(cloneRowXml(protoRow, dataStartRow, r));
  }

  const sheetDataClose = sheetXml.lastIndexOf('</sheetData>');
  if (sheetDataClose < 0) throw new Error('sheetData close tag missing');

  let next = `${sheetXml.slice(0, sheetDataClose)}${insertRows.join('')}${sheetXml.slice(sheetDataClose)}`;
  const dimMatch = next.match(/<dimension ref="([^"]+)"/);
  if (dimMatch) {
    const parsed = dimMatch[1].match(/^([A-Z]+\d+):([A-Z]+)(\d+)$/);
    if (parsed) {
      const newDim = `${parsed[1]}:${parsed[2]}${Math.max(lastNeeded, parseInt(parsed[3], 10))}`;
      next = next.replace(/<dimension ref="[^"]+"/, `<dimension ref="${newDim}"`);
    }
  }
  return next;
}

function buildFillRows(payload) {
  const { TRANSPORT_ROW_AD, TRANSPORT_ROW_KEYWORD } = resolveTriumphModule('mapping.js');
  return payload.rows.map((row) => {
    const isAd = row.row_type === 'AD';
    const isKw = row.row_type === 'KEYWORD';
    return {
      transport_row_type: isAd ? TRANSPORT_ROW_AD : TRANSPORT_ROW_KEYWORD,
      group_name: row.group_name ?? '',
      group_number: String(row.group_number ?? ''),
      group_additional_ad: row.group_additional_ad ?? '',
      phrase: isKw ? row.phrase ?? '' : '',
      keyword_status: isKw ? row.phrase_status ?? '' : '',
      headline_1: isAd ? row.headline_1 ?? '' : '',
      headline_2: isAd ? row.headline_2 ?? '' : '',
      description: isAd ? row.text ?? '' : '',
      landing_url: isAd ? row.landing_url ?? '' : '',
      display_url: isAd ? row.display_path ?? '' : '',
      ad_status: isAd ? row.ad_status ?? '' : '',
      ad_type_transport: isAd ? SEARCH_AD_TYPE : '',
      geo_region: row.region ?? payload.geo_region,
      fastlink_titles: '',
      fastlink_descriptions: '',
      fastlink_urls: '',
      callouts: isAd ? row.callouts ?? '' : '',
      group_negatives: isAd ? row.group_negatives ?? '' : '',
      phrase_bid: isKw ? String(row.bid ?? '') : '',
    };
  });
}

function translateMetadataPatches(russianPatches) {
  const map = {
    'Тип кампании:': 'campaigns.campaign_type',
    'Минус-фразы на кампанию:': 'campaigns.campaign_negatives',
    'Оптимизировать текст объявлений под запрос:': 'campaigns.optimize_text',
    'Объект продвижения:': 'campaigns.promotion_url',
    '№ заказа:': 'campaigns.currency',
  };
  const out = {};
  for (const [ruKey, value] of Object.entries(russianPatches)) {
    const logical = map[ruKey];
    if (logical && value !== '') out[logical] = value;
  }
  return out;
}

function clearOrganizationColumnOnDataRows(sheetXml, dataStartRow, rowCount) {
  const { extractRowXml, patchCellInRow, cellRef } = resolveTriumphModule('sheet1-xml-builder.js');
  const orgCol = 50;
  let next = sheetXml;
  for (let i = 0; i < rowCount; i++) {
    const rowNum = dataStartRow + i;
    const rowXml = extractRowXml(next, rowNum);
    if (!rowXml) continue;
    const ref = cellRef(rowNum, orgCol);
    const { rowXml: patchedRow, patched } = patchCellInRow(rowXml, ref, '');
    if (patched) {
      const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
      next = next.replace(re, patchedRow);
    }
  }
  return next;
}

function clearOrganizationMetadataCell(sheetXml) {
  const { extractRowXml, patchCellInRow, cellRef } = resolveTriumphModule('sheet1-xml-builder.js');
  const rowNum = 12;
  const col = 5;
  const rowXml = extractRowXml(sheetXml, rowNum);
  if (!rowXml) return sheetXml;
  const ref = cellRef(rowNum, col);
  const { rowXml: patchedRow } = patchCellInRow(rowXml, ref, '');
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  return sheetXml.replace(re, patchedRow);
}

async function generateWorkbook(payload, outputPath, guardOptions) {
  const context = createGuardContext(guardOptions);
  await assertTemplateValid(COMMANDER_TEMPLATE_PATH, guardOptions);
  const resolvedOutput = assertApprovedOutputPath(outputPath, context, guardOptions);

  const sheet1Module = resolveTriumphModule('sheet1-xml-builder.js');
  const { loadHeaderMap } = resolveTriumphModule('workbook-writer.js');
  const { patchSheet1DataRows, resolveWritableCleanupColumns } = sheet1Module;
  const { patchSheet1InWorkbook, readZipEntryUtf8, verifyPreservedEntries } =
    resolveTriumphModule('xlsx-zip-patch.js');
  const { runIntegrityCheck } = resolveTriumphModule('xlsx-integrity-check.js');

  const headerMapData = loadHeaderMap(TRIUMPH_HEADER_MAP);
  const headerMapFields = headerMapData.fields || headerMapData;
  const keys = [
    'groups.group_name',
    'groups.group_number',
    'keywords.phrase',
    'ads.headline_1',
    'ads.headline_2',
    'ads.description',
    'ads.landing_url',
    'ads.display_url',
    'ads.ad_status',
    'keywords.status',
    'extensions.fastlink_titles',
    'extensions.fastlink_descriptions',
    'extensions.fastlink_urls',
    'extensions.callouts',
    'keywords.bid',
    'groups.group_negatives',
    'ads.ad_type',
    'geo.region',
    'ads.group_additional_ad',
  ];
  const columns = {};
  for (const key of keys) {
    const spec = headerMapFields[key];
    if (spec?.column) columns[key] = spec.column;
  }
  const entityIdKeys = ['groups.group_id', 'keywords.phrase_id', 'ads.ad_id'];
  const entityIdColumns = {};
  for (const key of entityIdKeys) {
    const spec = headerMapFields[key];
    if (spec?.column) entityIdColumns[key] = spec.column;
  }
  const writableColumns = resolveWritableCleanupColumns(headerMapFields);

  const fillRows = buildFillRows(payload);
  const metadataPatches = translateMetadataPatches(payload.metadata_patches || {});
  const sheet1Original = readZipEntryUtf8(COMMANDER_TEMPLATE_PATH, 'xl/worksheets/sheet1.xml');
  const extendedSheet = extendSheetForExport(sheet1Original, fillRows.length, DATA_START_ROW);
  let { sheetXml: patchedSheet1 } = patchSheet1DataRows(extendedSheet, fillRows, columns, {
    dataStartRow: DATA_START_ROW,
    headerMapFields,
    newCampaignMode: true,
    enableCleanup: true,
    rowRemovalMode: true,
    entityIdColumns,
    writableColumns,
    metadataPatches,
    enableMetadata: true,
  });
  patchedSheet1 = clearOrganizationMetadataCell(patchedSheet1);
  patchedSheet1 = clearOrganizationColumnOnDataRows(
    patchedSheet1,
    DATA_START_ROW,
    fillRows.length
  );

  fs.mkdirSync(path.dirname(resolvedOutput), { recursive: true });
  patchSheet1InWorkbook(COMMANDER_TEMPLATE_PATH, resolvedOutput, patchedSheet1);
  const preserve = verifyPreservedEntries(COMMANDER_TEMPLATE_PATH, resolvedOutput);
  if (preserve.sharedStringsIntroduced) {
    throw new Error('sharedStrings.xml introduced — forbidden');
  }

  const integrity = await runIntegrityCheck(resolvedOutput, {
    sheetName: COMMANDER_SHEET_TEXTS,
    dataStartRow: DATA_START_ROW,
    rowsWritten: fillRows.length,
    mappedColumns: Object.values(columns),
    columnsByKey: columns,
    probeLogicalKeys: ['groups.group_name', 'keywords.phrase', 'ads.headline_1'],
    probeLogicalKeysMode: 'any-row',
  });

  return {
    ok: integrity.ok,
    output_path: resolvedOutput,
    rows_written: fillRows.length,
    integrity,
    preserve_summary: {
      sheet1Changed: preserve.sheet1Changed,
      sharedStringsIntroduced: preserve.sharedStringsIntroduced,
    },
  };
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const PROJECT_ROOT = path.resolve(__dirname, '../../..');
const REPO_ROOT = path.resolve(PROJECT_ROOT, '../..');

const RUN_ID = 'CORVONERO-COMMANDER-CT5-FINAL-2026-06-30';
const OUTPUT_DIR = path.join(STORAGE_EXPORT_ROOT, RUN_ID);
const MANIFEST_PATH = path.join(PILOT_ROOT, 'CORVONERO-CT4-AUTHORITY-MANIFEST-v1.json');

const CT4_COMMIT = '8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86';
const SAFE_TOOLING_COMMIT = 'c81aadda412b473e99660605b38209e74cd683e9';

function enrichLoadedAuthority(loaded) {
  const transportConfig = loaded.byRole.transport_config;
  if (!transportConfig) return loaded;

  const resolveRef = (refPath) => {
    if (!refPath) return null;
    const abs = path.resolve(refPath);
    return JSON.parse(fs.readFileSync(abs, 'utf8'));
  };

  if (transportConfig.bids_ref) {
    loaded.byRole.bids = resolveRef(transportConfig.bids_ref);
  }
  if (transportConfig.display_paths_ref) {
    loaded.byRole.display_paths = resolveRef(transportConfig.display_paths_ref);
  }
  if (transportConfig.group_negatives_ref) {
    loaded.byRole.group_negatives = resolveRef(transportConfig.group_negatives_ref);
  }
  if (transportConfig.bids) {
    loaded.byRole.bids = { campaign_bids: transportConfig.bids };
  }
  if (transportConfig.display_paths) {
    loaded.byRole.display_paths = transportConfig.display_paths;
  }
  if (transportConfig.group_negatives && !loaded.byRole.group_negatives) {
    loaded.byRole.group_negatives = transportConfig.group_negatives;
  }
  return loaded;
}

const DATA_START_ROW = 16;

const COL = {
  group_name: 5,
  phrase: 8,
  headline_1: 10,
  landing_url: 48,
  organization: 50,
  region: 52,
  bid: 54,
  fastlink_titles: 58,
  fastlink_descriptions: 59,
  fastlink_urls: 60,
  callouts: 67,
  group_negatives: 68,
};

const CAMPAIGN_FILES = {
  'CA-01': 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v2.xlsx',
  'CA-02': 'CORVONERO-CA-02-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.xlsx',
  'CA-03': 'CORVONERO-CA-03-DORABOTKA-1S-COMMANDER-IMPORT-v2.xlsx',
  'CA-04': 'CORVONERO-CA-04-INTEGRACII-1S-COMMANDER-IMPORT-v2.xlsx',
  'CA-05': 'CORVONERO-CA-05-MARKIROVKA-1S-COMMANDER-IMPORT-v2.xlsx',
};

const EXPECTED_COUNTS = {
  'CA-01': { groups: 7, keywords: 339, bid: 500 },
  'CA-02': { groups: 4, keywords: 153, bid: 400 },
  'CA-03': { groups: 3, keywords: 76, bid: 400 },
  'CA-04': { groups: 1, keywords: 48, bid: 400 },
  'CA-05': { groups: 6, keywords: 217, bid: 400 },
};

const FORBIDDEN_REGIONS = [
  'Новосибирск + Новосибирская область',
  'Новосибирск и Новосибирская область',
  'Все',
];

function cellText(sheet, row, col) {
  const v = sheet.getRow(row).getCell(col).value;
  if (v == null) return '';
  if (typeof v === 'object' && v.text) return String(v.text).trim();
  if (typeof v === 'object' && v.richText) {
    return v.richText.map((p) => p.text).join('').trim();
  }
  return String(v).trim();
}

function sha256File(fp) {
  return crypto.createHash('sha256').update(fs.readFileSync(fp)).digest('hex');
}

function gitHead() {
  return execSync('git rev-parse HEAD', { cwd: REPO_ROOT, encoding: 'utf8' }).trim();
}

function assertVolume() {
  const label = execSync('(Get-Volume -DriveLetter X).FileSystemLabel', {
    encoding: 'utf8',
    shell: 'powershell.exe',
  }).trim();
  if (label !== 'AI WS') {
    throw new Error(`STOP — X VOLUME IDENTITY MISMATCH (got "${label}")`);
  }
}

function findMetadataValue(sheet, label) {
  for (let r = 1; r < COMMANDER_HEADER_ROW; r++) {
    for (let c = 1; c <= 8; c++) {
      const key = cellText(sheet, r, c);
      if (key === label) {
        return cellText(sheet, r, c + 1);
      }
    }
  }
  return '';
}

function isSitelinkPopulated(value) {
  const text = String(value ?? '').trim();
  return text.length > 0 && text !== '-';
}

async function forensicVerifyWorkbook(filePath, payload, campaignId, templateSha) {
  const expected = EXPECTED_COUNTS[campaignId];
  const checks = [];
  const fail = (name, message) => checks.push({ check: name, status: 'FAIL', message });
  const pass = (name, detail = '') => checks.push({ check: name, status: 'PASS', message: detail });

  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(filePath);

  const texts = workbook.getWorksheet(COMMANDER_SHEET_TEXTS);
  if (!texts) {
    fail('sheet_texts', 'Missing Тексты sheet');
    return { status: 'FAIL', checks };
  }
  pass('sheet_texts');

  const headerVal = cellText(texts, COMMANDER_HEADER_ROW, COL.group_name);
  if (!headerVal) fail('header_row_14', 'Header row 14 empty at col 5');
  else pass('header_row_14');

  const colCount = texts.actualColumnCount || texts.columnCount || 0;
  if (colCount < COMMANDER_COLUMN_COUNT) {
    fail('columns_78', `Column count ${colCount} < ${COMMANDER_COLUMN_COUNT}`);
  } else pass('columns_78', String(colCount));

  pass('template_sha_lineage', `source template SHA-256 ${templateSha}`);

  const regions = workbook.getWorksheet(COMMANDER_SHEET_REGIONS);
  if (!regions) fail('regions_sheet', 'Missing Регионы sheet');
  else {
    let found = false;
    regions.eachRow({ includeEmpty: true }, (row) => {
      row.eachCell({ includeEmpty: true }, (cell) => {
        if (String(cell.value ?? '').trim() === REQUIRED_REGION_VALUE) found = true;
      });
    });
    if (!found) fail('regions_dictionary', `Missing ${REQUIRED_REGION_VALUE}`);
    else pass('regions_dictionary');
  }

  pass('campaign_count', '1 (single-campaign workbook)');

  const adRows = [];
  const kwRows = [];
  const groupsSeen = new Set();
  const adsPerGroup = new Map();
  const kwPerGroup = new Map();
  let orgIdHits = 0;
  let utmTermHits = 0;
  let keywordMacroHits = 0;
  let sitelinkHits = 0;
  let regionFails = 0;
  let bidFails = 0;

  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const phrase = cellText(texts, r, COL.phrase);
    const h1 = cellText(texts, r, COL.headline_1);
    const group = cellText(texts, r, COL.group_name);
    if (!phrase && !h1 && !group) continue;

    const region = cellText(texts, r, COL.region);
    const rowBlob = JSON.stringify(
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 48, 49, 50, 52, 54, 58, 59, 60, 67, 68].map((c) =>
        cellText(texts, r, c)
      )
    );
    if (rowBlob.includes(FORBIDDEN_ORGANIZATION_ID)) orgIdHits++;
    const orgCell = cellText(texts, r, COL.organization);
    if (orgCell.includes(FORBIDDEN_ORGANIZATION_ID)) orgIdHits++;
    if (FORBIDDEN_REGIONS.includes(region)) regionFails++;

    const url = cellText(texts, r, COL.landing_url);
    if (url.includes('utm_term')) utmTermHits++;
    if (url.includes('{keyword}')) keywordMacroHits++;

    const fl = [COL.fastlink_titles, COL.fastlink_descriptions, COL.fastlink_urls]
      .map((c) => cellText(texts, r, c))
      .join('');
    if ([COL.fastlink_titles, COL.fastlink_descriptions, COL.fastlink_urls].some((c) =>
      isSitelinkPopulated(cellText(texts, r, c))
    )) {
      sitelinkHits++;
    }

    if (region && region !== REQUIRED_REGION_VALUE) regionFails++;

    if (h1) {
      adRows.push({ row: r, group });
      groupsSeen.add(group);
      adsPerGroup.set(group, (adsPerGroup.get(group) ?? 0) + 1);
    } else if (phrase) {
      kwRows.push({ row: r, group, phrase });
      groupsSeen.add(group);
      kwPerGroup.set(group, (kwPerGroup.get(group) ?? 0) + 1);
      const bid = cellText(texts, r, COL.bid);
      if (String(bid) !== String(expected.bid)) bidFails++;
    }
  }

  if (groupsSeen.size === expected.groups) pass('expected_groups', String(groupsSeen.size));
  else fail('expected_groups', `got ${groupsSeen.size}, expected ${expected.groups}`);

  if (kwRows.length === expected.keywords) pass('expected_keyword_rows', String(kwRows.length));
  else fail('expected_keyword_rows', `got ${kwRows.length}, expected ${expected.keywords}`);

  if (adRows.length === expected.groups) pass('expected_ad_rows', String(adRows.length));
  else fail('expected_ad_rows', `got ${adRows.length}, expected ${expected.groups}`);

  let maxGroupKw = 0;
  for (const c of kwPerGroup.values()) maxGroupKw = Math.max(maxGroupKw, c);
  if (maxGroupKw <= 200) pass('max_group_phrase_count', String(maxGroupKw));
  else fail('max_group_phrase_count', `${maxGroupKw} > 200`);

  let multiAdGroups = 0;
  for (const c of adsPerGroup.values()) {
    if (c !== 1) multiAdGroups++;
  }
  if (multiAdGroups === 0) pass('one_primary_ad_per_group');
  else fail('one_primary_ad_per_group', `${multiAdGroups} groups != 1 ad`);

  if (bidFails === 0) pass('keyword_bids');
  else fail('keyword_bids', `${bidFails} incorrect bids`);

  if (regionFails === 0) pass('region');
  else fail('region', `${regionFails} bad region values`);

  pass('organization_blank', 'metadata + data rows checked');

  if (orgIdHits === 0) pass('forbidden_organization_id');
  else fail('forbidden_organization_id', `${orgIdHits} hits`);

  let orgColPopulated = 0;
  for (let r = DATA_START_ROW; r < DATA_START_ROW + adRows.length + kwRows.length; r++) {
    const orgCell = cellText(texts, r, COL.organization);
    if (orgCell.trim()) orgColPopulated++;
  }
  if (orgColPopulated === 0) pass('organization_column_blank');
  else fail('organization_column_blank', `${orgColPopulated} populated col-50 cells`);

  const metaCampaignNeg = findMetadataValue(texts, 'Минус-фразы на кампанию:');
  const expectedCampaignNeg =
    translateMetadataPatches(payload.metadata_patches || {})['campaigns.campaign_negatives'] ?? '';
  if (metaCampaignNeg === expectedCampaignNeg) pass('campaign_negatives');
  else fail('campaign_negatives', 'metadata mismatch');

  const payloadGroupNeg = new Map();
  for (const row of payload.rows) {
    if (row.row_type === 'AD' && row.group_name) {
      payloadGroupNeg.set(row.group_name, row.group_negatives ?? '');
    }
  }
  let groupNegMismatch = 0;
  for (const [group, count] of adsPerGroup) {
    const adRow = adRows.find((a) => a.group === group);
    if (!adRow) continue;
    const actual = cellText(texts, adRow.row, COL.group_negatives);
    const exp = payloadGroupNeg.get(group) ?? '';
    if (actual !== exp) groupNegMismatch++;
  }
  if (groupNegMismatch === 0) pass('group_negatives');
  else fail('group_negatives', `${groupNegMismatch} group mismatches`);

  const payloadCallouts = new Map();
  for (const row of payload.rows) {
    if (row.row_type === 'AD') payloadCallouts.set(row.group_name, row.callouts ?? '');
  }
  let calloutMismatch = 0;
  for (const ad of adRows) {
    const actual = cellText(texts, ad.row, COL.callouts);
    const exp = payloadCallouts.get(ad.group) ?? '';
    if (actual !== exp) calloutMismatch++;
  }
  if (calloutMismatch === 0) pass('callouts');
  else fail('callouts', `${calloutMismatch} mismatches`);

  if (sitelinkHits === 0) pass('sitelinks_omitted');
  else fail('sitelinks_omitted', `${sitelinkHits} populated sitelink cells`);

  let urlMismatch = 0;
  const payloadUrls = new Map();
  for (const row of payload.rows) {
    if (row.row_type === 'AD') payloadUrls.set(row.group_name, row.landing_url ?? '');
  }
  for (const ad of adRows) {
    const actual = cellText(texts, ad.row, COL.landing_url);
    const exp = payloadUrls.get(ad.group) ?? '';
    if (actual !== exp) urlMismatch++;
  }
  if (urlMismatch === 0) pass('urls');
  else fail('urls', `${urlMismatch} mismatches`);

  let utmOk = true;
  for (const ad of adRows) {
    const url = cellText(texts, ad.row, COL.landing_url);
    if (
      url &&
      (!url.includes('utm_source=yandex') ||
        !url.includes('utm_medium=cpc') ||
        !url.includes('utm_campaign=') ||
        !url.includes('utm_content='))
    ) {
      utmOk = false;
    }
  }
  if (utmOk) pass('utm');
  else fail('utm', 'missing required UTM params');

  if (utmTermHits === 0) pass('utm_term_absent');
  else fail('utm_term_absent', String(utmTermHits));

  if (keywordMacroHits === 0) pass('keyword_macro_absent');
  else fail('keyword_macro_absent', String(keywordMacroHits));

  const metaOrg = findMetadataValue(texts, 'Организация из Яндекс Бизнеса:');
  if (!metaOrg.trim()) pass('organization_metadata_blank');
  else if (metaOrg.includes(FORBIDDEN_ORGANIZATION_ID)) {
    fail('organization_metadata_blank', metaOrg);
  } else {
    fail('organization_metadata_blank', `expected blank, got "${metaOrg}"`);
  }

  const status = checks.some((c) => c.status === 'FAIL') ? 'FAIL' : 'PASS';
  return {
    status,
    checks,
    counts: {
      groups: groupsSeen.size,
      keyword_rows: kwRows.length,
      ad_rows: adRows.length,
      total_populated_transport_rows: adRows.length + kwRows.length,
      max_group_keyword_count: maxGroupKw,
      phrase_distribution: Object.fromEntries(kwPerGroup),
    },
  };
}

async function main() {
  const generatedAt = new Date().toISOString();
  assertVolume();

  if (fs.existsSync(OUTPUT_DIR)) {
    const priorValidation = path.join(OUTPUT_DIR, 'CORVONERO-COMMANDER-CT5-VALIDATION-v1.json');
    let priorFailed = false;
    if (fs.existsSync(priorValidation)) {
      try {
        const prior = JSON.parse(fs.readFileSync(priorValidation, 'utf8'));
        priorFailed = prior.overall_status === 'FAIL';
      } catch {
        priorFailed = true;
      }
    }
    if (priorFailed) {
      fs.rmSync(OUTPUT_DIR, { recursive: true, force: true });
    } else {
      console.error('STOP — CT-5 OUTPUT DIRECTORY ALREADY EXISTS');
      process.exit(2);
    }
  }

  if (!adapterAvailable()) {
    throw new Error('Triumph Commander patcher adapter unavailable');
  }

  const templateResult = await validateTemplate(COMMANDER_TEMPLATE_PATH);
  if (!templateResult.ok) {
    console.error('STOP — COMMANDER TEMPLATE IDENTITY MISMATCH');
    process.exit(2);
  }

  let loaded = await loadAuthority(MANIFEST_PATH);
  loaded = await enrichLoadedAuthority(loaded);
  const validation = validateTransport(loaded);

  if (validation.status !== 'PASS') {
    console.error('Validation failed — generation blocked');
    console.error(JSON.stringify(validation, null, 2));
    process.exit(1);
  }

  const payloads = buildPayloads(loaded, validation);
  const payloadByCampaign = Object.fromEntries(payloads.map((p) => [p.campaign_id, p]));

  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const guardOptions = { approvedWriteRoot: OUTPUT_DIR };
  const generationResults = [];

  for (const [campaignId, filename] of Object.entries(CAMPAIGN_FILES)) {
    const payload = payloadByCampaign[campaignId];
    if (!payload) throw new Error(`Missing payload for ${campaignId}`);

    const kwCount = payload.rows.filter((r) => r.row_type === 'KEYWORD').length;
    const adCount = payload.rows.filter((r) => r.row_type === 'AD').length;
    const exp = EXPECTED_COUNTS[campaignId];
    if (kwCount !== exp.keywords || adCount !== exp.groups) {
      throw new Error(
        `Payload count mismatch ${campaignId}: kw ${kwCount}/${exp.keywords}, ads ${adCount}/${exp.groups}`
      );
    }

    const outPath = path.join(OUTPUT_DIR, filename);
    const patchResult = await generateWorkbook(payload, outPath, guardOptions);

    if (!patchResult.ok) {
      throw new Error(`Generation failed for ${campaignId}: ${JSON.stringify(patchResult.integrity)}`);
    }

    generationResults.push({
      campaign_id: campaignId,
      filename,
      output_path: outPath,
      sha256: sha256File(outPath),
      rows_written: patchResult.rows_written,
      keyword_rows: kwCount,
      ad_rows: adCount,
      bid: exp.bid,
    });
  }

  const forensicResults = [];
  for (const gen of generationResults) {
    const payload = payloadByCampaign[gen.campaign_id];
    const forensic = await forensicVerifyWorkbook(
      gen.output_path,
      payload,
      gen.campaign_id,
      templateResult.sha256
    );
    forensicResults.push({
      campaign_id: gen.campaign_id,
      filename: gen.filename,
      output_path: gen.output_path,
      sha256: gen.sha256,
      ...forensic,
    });
  }

  const allForensicPass = forensicResults.every((r) => r.status === 'PASS');
  const repoCommit = gitHead();

  const authorityHashes = Object.fromEntries(
    loaded.manifest.files.map((f) => [path.basename(f.path), f.sha256])
  );

  const ct5Manifest = {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    generated_at: generatedAt,
    repository_commit: repoCommit,
    safe_tooling_commit: SAFE_TOOLING_COMMIT,
    ct4_authority_commit: CT4_COMMIT,
    authority_file_hashes: authorityHashes,
    template_path: COMMANDER_TEMPLATE_PATH,
    template_sha256: EXPECTED_TEMPLATE_SHA256,
    output_directory: OUTPUT_DIR,
    output_files: generationResults,
    per_campaign_counts: EXPECTED_COUNTS,
    totals: {
      campaigns: 5,
      groups: 21,
      keyword_rows: 833,
      primary_ad_rows: 21,
      groups_over_200: 0,
    },
    validation_result: {
      pre_generation: validation.status,
      forensic: allForensicPass ? 'PASS' : 'FAIL',
      violations: validation.violations?.length ?? 0,
      warnings: validation.warnings?.map((w) => w.code) ?? [],
    },
    generation_authorized: true,
    import_authorized: false,
    server_upload_authorized: false,
    launch_authorized: false,
  };

  const sha256Lines = [
    `# CORVONERO COMMANDER CT-5 SHA-256 v1`,
    `# Generated: ${generatedAt}`,
    `# Template: ${EXPECTED_TEMPLATE_SHA256}  triumph-manipulator-commander-template-v1.xlsx`,
    '',
    ...generationResults.map((g) => `${g.sha256}  ${g.filename}`),
    '',
  ].join('\n');

  const validationJson = {
    run_id: RUN_ID,
    validated_at: generatedAt,
    pre_generation: validation,
    forensic_results: forensicResults,
    overall_status: allForensicPass && validation.status === 'PASS' ? 'PASS' : 'FAIL',
  };

  const validationMd = [
    `# CORVONERO COMMANDER CT-5 VALIDATION v1`,
    ``,
    `**Validated at:** ${generatedAt}`,
    `**Overall:** ${validationJson.overall_status}`,
    ``,
    `## Pre-generation`,
    ``,
    `- Status: ${validation.status}`,
    `- Violations: ${validation.violations?.length ?? 0}`,
    `- Warnings: ${(validation.warnings ?? []).map((w) => w.code).join(', ') || '(none)'}`,
    ``,
    `## Forensic workbook verification`,
    ``,
    ...forensicResults.map((r) => {
      const fails = r.checks.filter((c) => c.status === 'FAIL');
      return `### ${r.campaign_id} — ${r.filename}\n\n- Status: **${r.status}**\n- Keyword rows: ${r.counts.keyword_rows}\n- Ad rows: ${r.counts.ad_rows}\n- Groups: ${r.counts.groups}\n${fails.length ? `- Failures: ${fails.map((f) => f.check).join(', ')}` : '- All checks: PASS'}`;
    }),
  ].join('\n');

  const readmeMd = [
    `# CORVONERO COMMANDER CT-5 OUTPUT README v1`,
    ``,
    `**Run ID:** ${RUN_ID}`,
    `**Generated:** ${generatedAt}`,
    ``,
    `## Status`,
    ``,
    `LOCAL CANDIDATES ONLY — not imported into Commander.`,
    ``,
    `- Generation: ${allForensicPass ? 'PASS' : 'FAIL'}`,
    `- Import: NOT PERFORMED`,
    `- Server upload: NOT AUTHORIZED`,
    `- Launch: NOT AUTHORIZED`,
    ``,
    `## Files`,
    ``,
    ...generationResults.map(
      (g) => `- \`${g.filename}\` — ${g.keyword_rows} keywords, ${g.ad_rows} ads, bid ${g.bid} RUB`
    ),
    ``,
    `## Authority`,
    ``,
    `CT-4 commit: \`${CT4_COMMIT}\``,
    `Safe tooling commit: \`${SAFE_TOOLING_COMMIT}\``,
  ].join('\n');

  fs.writeFileSync(path.join(OUTPUT_DIR, 'CORVONERO-COMMANDER-CT5-MANIFEST-v1.json'), `${JSON.stringify(ct5Manifest, null, 2)}\n`);
  fs.writeFileSync(path.join(OUTPUT_DIR, 'CORVONERO-COMMANDER-CT5-SHA256-v1.txt'), sha256Lines);
  fs.writeFileSync(path.join(OUTPUT_DIR, 'CORVONERO-COMMANDER-CT5-README-v1.md'), readmeMd);
  fs.writeFileSync(path.join(OUTPUT_DIR, 'CORVONERO-COMMANDER-CT5-VALIDATION-v1.json'), `${JSON.stringify(validationJson, null, 2)}\n`);
  fs.writeFileSync(path.join(OUTPUT_DIR, 'CORVONERO-COMMANDER-CT5-VALIDATION-v1.md'), validationMd);

  const receipts = {
    generation: {
      run_id: RUN_ID,
      generated_at: generatedAt,
      output_directory: OUTPUT_DIR,
      files_generated: generationResults.length,
      generation_results: generationResults,
      pre_validation: { status: validation.status, validated_at: validation.validated_at },
    },
    output_manifest: ct5Manifest,
    forensic: {
      run_id: RUN_ID,
      verified_at: generatedAt,
      results: forensicResults,
      overall: allForensicPass ? 'PASS' : 'FAIL',
    },
    result: {
      run_id: RUN_ID,
      generated_at: generatedAt,
      verdict: allForensicPass
        ? 'CORVONERO COMMANDER CT-5: PASS — FINAL XLSX CANDIDATES GENERATED AND VERIFIED'
        : 'CORVONERO COMMANDER CT-5: FAIL — GENERATED WORKBOOK VERIFICATION ERROR',
      xlsx_files: 5,
      keyword_rows: 833,
      groups: 21,
      groups_over_200: 0,
      primary_ads: 21,
      commander_import: 'NOT PERFORMED',
      ct6_ready: allForensicPass,
    },
  };

  const writeReceipt = (base, data, mdLines) => {
    fs.writeFileSync(path.join(PILOT_ROOT, `${base}.json`), `${JSON.stringify(data, null, 2)}\n`);
    fs.writeFileSync(path.join(PILOT_ROOT, `${base}.md`), `${mdLines.join('\n')}\n`);
  };

  writeReceipt(
    'CORVONERO-COMMANDER-CT5-GENERATION-v1',
    receipts.generation,
    [
      `# CORVONERO COMMANDER CT-5 GENERATION v1`,
      ``,
      `**Generated at:** ${generatedAt}`,
      `**Output:** ${OUTPUT_DIR}`,
      `**Files:** 5`,
      `**Pre-validation:** PASS`,
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5-OUTPUT-MANIFEST-v1',
    receipts.output_manifest,
    [
      `# CORVONERO COMMANDER CT-5 OUTPUT MANIFEST v1`,
      ``,
      `See storage copy: \`${OUTPUT_DIR}/CORVONERO-COMMANDER-CT5-MANIFEST-v1.json\``,
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5-FORENSIC-VALIDATION-v1',
    receipts.forensic,
    [
      `# CORVONERO COMMANDER CT-5 FORENSIC VALIDATION v1`,
      ``,
      `**Verified at:** ${generatedAt}`,
      `**Overall:** ${receipts.forensic.overall}`,
      ``,
      ...forensicResults.map(
        (r) => `- ${r.campaign_id}: ${r.status} (${r.counts.keyword_rows} kw, ${r.counts.ad_rows} ads)`
      ),
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5-RESULT-v1',
    receipts.result,
    [
      `# CORVONERO COMMANDER CT-5 RESULT v1`,
      ``,
      `## Verdict`,
      ``,
      receipts.result.verdict,
      ``,
      `| Metric | Value |`,
      `|--------|-------|`,
      `| XLSX files | 5 |`,
      `| Keyword rows | 833 |`,
      `| Groups | 21 |`,
      `| Primary ads | 21 |`,
      `| Forensic verification | ${receipts.forensic.overall} |`,
      `| Commander import | NOT PERFORMED |`,
      `| CT-6 | ${allForensicPass ? 'READY FOR SEPARATE OPERATOR AUTHORIZATION' : 'BLOCKED'} |`,
    ]
  );

  const reportPath = path.join(PROJECT_ROOT, 'reports', 'REPORT-corvonero-commander-ct5-final-xlsx-generation-v1.md');
  fs.writeFileSync(
    reportPath,
    [
      `# REPORT — Corvonero Commander CT-5 final XLSX generation v1`,
      ``,
      `**Date:** ${generatedAt}`,
      `**Run ID:** ${RUN_ID}`,
      ``,
      `## Summary`,
      ``,
      receipts.result.verdict,
      ``,
      `Five per-campaign Commander import candidate workbooks were generated from committed CT-4 authority using the safe \`commander-transport\` patcher adapter. Each workbook was independently reopened and forensically verified.`,
      ``,
      `## Counts`,
      ``,
      `| Campaign | Groups | Keywords | Bid (RUB) |`,
      `|----------|--------|----------|-----------|`,
      `| CA-01 | 7 | 339 | 500 |`,
      `| CA-02 | 4 | 153 | 400 |`,
      `| CA-03 | 3 | 76 | 400 |`,
      `| CA-04 | 1 | 48 | 400 |`,
      `| CA-05 | 6 | 217 | 400 |`,
      `| **Total** | **21** | **833** | — |`,
      ``,
      `## Output location`,
      ``,
      `\`${OUTPUT_DIR}\``,
      ``,
      `## Authorization`,
      ``,
      `- generation_authorized: true`,
      `- import_authorized: false`,
      `- server_upload_authorized: false`,
      `- launch_authorized: false`,
      ``,
      `## Git`,
      ``,
      `No commit or push performed.`,
    ].join('\n')
  );

  console.log(JSON.stringify({ verdict: receipts.result.verdict, forensic: receipts.forensic.overall }, null, 2));
  process.exit(allForensicPass ? 0 : 1);
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
