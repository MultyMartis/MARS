import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import {
  SYNTHETIC_TEST_OUTPUT_DIR,
  TRIUMPH_EXPORTER_CLI,
  TRIUMPH_HEADER_MAP,
} from './constants.mjs';
import { assertApprovedOutputPath, createGuardContext } from './filesystem-guard.mjs';
import { assertTemplateValid } from './template-validator.mjs';

const require = createRequire(import.meta.url);

const SEARCH_AD_TYPE = 'Текстово-графическое';
const DATA_START_ROW = 16;

function resolveTriumphModule(name) {
  return require(path.join(TRIUMPH_EXPORTER_CLI, name));
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

  const { loadHeaderMap } = resolveTriumphModule('workbook-writer.js');
  const { patchSheet1DataRows } = resolveTriumphModule('sheet1-xml-builder.js');
  const { patchSheet1InWorkbook, readZipEntryUtf8, verifyPreservedEntries } =
    resolveTriumphModule('xlsx-zip-patch.js');
  const { runIntegrityCheck } = resolveTriumphModule('xlsx-integrity-check.js');

  const headerMapData = loadHeaderMap(headerMapPath);
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

  const fillRows = buildFillRows(payload);
  const metadataPatches = payload.metadata_patches || {};

  const sheet1Original = readZipEntryUtf8(templatePath, 'xl/worksheets/sheet1.xml');
  const { sheetXml: patchedSheet1 } = patchSheet1DataRows(sheet1Original, fillRows, columns, {
    dataStartRow: DATA_START_ROW,
    headerMapFields,
    newCampaignMode: true,
    enableCleanup: true,
    rowRemovalMode: true,
    entityIdColumns,
    metadataPatches,
    enableMetadata: true,
  });

  fs.mkdirSync(path.dirname(resolvedOutput), { recursive: true });
  patchSheet1InWorkbook(templatePath, resolvedOutput, patchedSheet1);
  const preserve = verifyPreservedEntries(templatePath, resolvedOutput);

  if (preserve.sharedStringsIntroduced) {
    throw new Error('sharedStrings.xml introduced — forbidden');
  }

  const integrity = await runIntegrityCheck(resolvedOutput, {
    sheetName: 'Тексты',
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

export function adapterAvailable() {
  try {
    resolveTriumphModule('mapping.js');
    return fs.existsSync(TRIUMPH_HEADER_MAP);
  } catch {
    return false;
  }
}
