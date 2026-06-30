import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import {
  COMMANDER_SHEET_TEXTS,
  SYNTHETIC_TEST_OUTPUT_DIR,
  TRIUMPH_EXPORTER_CLI,
  TRIUMPH_HEADER_MAP,
} from './constants.mjs';
import { assertApprovedOutputPath, createGuardContext } from './filesystem-guard.mjs';
import { assertTemplateValid } from './template-validator.mjs';

const require = createRequire(import.meta.url);

const SEARCH_AD_TYPE = 'Текстово-графическое';
export const DATA_START_ROW = 16;

const METADATA_KEY_MAP = {
  'Тип кампании:': 'campaigns.campaign_type',
  'Минус-фразы на кампанию:': 'campaigns.campaign_negatives',
  'Оптимизировать текст объявлений под запрос:': 'campaigns.optimize_text',
  'Объект продвижения:': 'campaigns.promotion_url',
  '№ заказа:': 'campaigns.currency',
  'Организация из Яндекс Бизнеса:': 'campaigns.organization',
};

function resolveTriumphModule(name) {
  return require(path.join(TRIUMPH_EXPORTER_CLI, name));
}

export function translateMetadataPatches(russianPatches) {
  const out = {};
  for (const [ruKey, value] of Object.entries(russianPatches ?? {})) {
    const logical = METADATA_KEY_MAP[ruKey];
    if (logical && value !== '') out[logical] = value;
  }
  return out;
}

export function extractRowXml(sheetXml, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheetXml.match(re);
  return m ? m[0] : null;
}

export function cloneRowXml(rowXml, fromRow, toRow) {
  let s = rowXml.replace(new RegExp(`r="${fromRow}"`, 'g'), `r="${toRow}"`);
  s = s.replace(new RegExp(`([A-Z]{1,3})${fromRow}(?![0-9])`, 'g'), `$1${toRow}`);
  return s;
}

export function extendSheetForExport(sheetXml, fillRowCount, dataStartRow = DATA_START_ROW) {
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

export function clearOrganizationColumnOnDataRows(sheetXml, dataStartRow, rowCount) {
  const { extractRowXml: extractRow, patchCellInRow, cellRef } =
    resolveTriumphModule('sheet1-xml-builder.js');
  const orgCol = 50;
  let next = sheetXml;
  for (let i = 0; i < rowCount; i++) {
    const rowNum = dataStartRow + i;
    const rowXml = extractRow(next, rowNum);
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

export function clearOrganizationMetadataCell(sheetXml) {
  const { extractRowXml: extractRow, patchCellInRow, cellRef } =
    resolveTriumphModule('sheet1-xml-builder.js');
  const rowNum = 12;
  const col = 5;
  const rowXml = extractRow(sheetXml, rowNum);
  if (!rowXml) return sheetXml;
  const ref = cellRef(rowNum, col);
  const { rowXml: patchedRow } = patchCellInRow(rowXml, ref, '');
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  return sheetXml.replace(re, patchedRow);
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

function resolveColumnMap(headerMapFields) {
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
  return { columns, entityIdColumns };
}

/**
 * Transport-only patcher adapter — no authority or strategy logic.
 * @param {object} options
 */
export async function patchCommanderWorkbook(options) {
  const {
    payload,
    templatePath,
    outputPath,
    headerMapPath = TRIUMPH_HEADER_MAP,
    guardOptions = {},
    allowSyntheticTestDir = false,
    dataStartRow = DATA_START_ROW,
  } = options;

  if (!payload?.rows?.length) {
    throw new Error('Payload must contain validated rows');
  }

  const context = createGuardContext(guardOptions);
  await assertTemplateValid(templatePath, guardOptions);

  let resolvedOutput;
  if (allowSyntheticTestDir) {
    const normalized = path.resolve(outputPath);
    if (!normalized.startsWith(path.resolve(SYNTHETIC_TEST_OUTPUT_DIR))) {
      throw new Error(`Synthetic output must be under ${SYNTHETIC_TEST_OUTPUT_DIR}`);
    }
    resolvedOutput = assertApprovedOutputPath(normalized, context, guardOptions);
  } else {
    resolvedOutput = assertApprovedOutputPath(outputPath, context, guardOptions);
  }

  const sheet1Module = resolveTriumphModule('sheet1-xml-builder.js');
  const { loadHeaderMap } = resolveTriumphModule('workbook-writer.js');
  const { patchSheet1DataRows, resolveWritableCleanupColumns } = sheet1Module;
  const { patchSheet1InWorkbook, readZipEntryUtf8, verifyPreservedEntries } =
    resolveTriumphModule('xlsx-zip-patch.js');
  const { runIntegrityCheck } = resolveTriumphModule('xlsx-integrity-check.js');

  const headerMapData = loadHeaderMap(headerMapPath);
  const headerMapFields = headerMapData.fields || headerMapData;
  const { columns, entityIdColumns } = resolveColumnMap(headerMapFields);
  const writableColumns = resolveWritableCleanupColumns(headerMapFields);

  const fillRows = buildFillRows(payload);
  const metadataPatches = translateMetadataPatches(payload.metadata_patches || {});

  const sheet1Original = readZipEntryUtf8(templatePath, 'xl/worksheets/sheet1.xml');
  const extendedSheet = extendSheetForExport(sheet1Original, fillRows.length, dataStartRow);
  let { sheetXml: patchedSheet1 } = patchSheet1DataRows(extendedSheet, fillRows, columns, {
    dataStartRow,
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
    dataStartRow,
    fillRows.length
  );

  fs.mkdirSync(path.dirname(resolvedOutput), { recursive: true });
  patchSheet1InWorkbook(templatePath, resolvedOutput, patchedSheet1);
  const preserve = verifyPreservedEntries(templatePath, resolvedOutput);

  if (preserve.sharedStringsIntroduced) {
    throw new Error('sharedStrings.xml introduced — forbidden');
  }

  const integrity = await runIntegrityCheck(resolvedOutput, {
    sheetName: COMMANDER_SHEET_TEXTS,
    dataStartRow,
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

export function adapterAvailable() {
  try {
    resolveTriumphModule('mapping.js');
    return fs.existsSync(TRIUMPH_HEADER_MAP);
  } catch {
    return false;
  }
}
