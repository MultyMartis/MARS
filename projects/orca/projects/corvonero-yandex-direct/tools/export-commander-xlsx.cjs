#!/usr/bin/env node
'use strict';

/**
 * Corvonero Direct Commander XLSX export — uses Triumph sheet1 patch transport.
 * Run after: node tools/run-full-production.mjs
 */
const fs = require('fs');
const path = require('path');

const TRIUMPH_CLI = path.resolve(
  __dirname,
  '../../../ppc/triumph-manipulator/tools/exporter-cli'
);
const { patchSheet1DataRows } = require(path.join(TRIUMPH_CLI, 'sheet1-xml-builder'));
const { patchSheet1InWorkbook, readZipEntryUtf8, verifyPreservedEntries } = require(path.join(
  TRIUMPH_CLI,
  'xlsx-zip-patch'
));
const { loadHeaderMap } = require(path.join(TRIUMPH_CLI, 'workbook-writer'));
const { runIntegrityCheck } = require(path.join(TRIUMPH_CLI, 'xlsx-integrity-check'));
const {
  TRANSPORT_ROW_AD,
  TRANSPORT_ROW_KEYWORD,
  GROUP_ADDITIONAL_AD_MARKER,
  normalizeTransportText,
  collapseWhitespace,
} = require(path.join(TRIUMPH_CLI, 'mapping'));

const DATA_START_ROW = 16;
const TEMPLATE = path.resolve(
  TRIUMPH_CLI,
  '../../assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx'
);
const HEADER_MAP = path.join(TRIUMPH_CLI, 'commander-header-map-v0.json');
const ROOT = path.resolve(__dirname, '..');
const DATASET_PATH = path.join(ROOT, 'production/direct-commander-production-dataset-v1.json');
const OUTPUT = path.join(ROOT, 'exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v1.xlsx');

const SEARCH_AD_TYPE = 'Текстово-графическое';
const GEO_REGION = 'Новосибирск и Новосибирская область';
const JOIN = '||';

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

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

/** Extend template sheet1 with cloned data rows when fill count exceeds template tail. */
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

function resolveColumns(headerMapFields) {
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
    if (spec && spec.column) columns[key] = spec.column;
  }
  return columns;
}

function buildMetadataPatches(dataset) {
  const globalNeg = (dataset.global_negatives || [])
    .map((w) => (w.startsWith('-') ? w : `-${w}`))
    .join(' ');
  return {
    'campaigns.campaign_type': 'Единая перфоманс-кампания',
    'campaigns.placement': 'search',
    'campaigns.currency': 'RUB',
    'campaigns.optimize_text': '0',
    'campaigns.promotion_url': 'https://lk.corvonero.ru/',
    'campaigns.campaign_negatives': globalNeg,
  };
}

function buildFillRows(dataset) {
  const rows = [];

  for (const group of dataset.groups) {
    const groupName = normalizeTransportText(`${group.campaign_id} — ${group.group_name}`);
    const groupNumber = String(group.group_number);
    const groupNeg = group.group_negatives_commander || '';

    for (let ai = 0; ai < group.ads.length; ai++) {
      const ad = group.ads[ai];
      const fl = ad.sitelinks || [];
      rows.push({
        transport_row_type: TRANSPORT_ROW_AD,
        group_name: groupName,
        group_number: groupNumber,
        group_additional_ad: ai > 0 ? GROUP_ADDITIONAL_AD_MARKER : '',
        phrase: '',
        keyword_status: '',
        headline_1: normalizeTransportText(ad.headline_1),
        headline_2: normalizeTransportText(ad.headline_2),
        description: normalizeTransportText(ad.text),
        landing_url: collapseWhitespace(ad.landing_url),
        display_url: normalizeTransportText(ad.display_path || ''),
        ad_status: '',
        ad_type_transport: SEARCH_AD_TYPE,
        geo_region: GEO_REGION,
        fastlink_titles: fl.map((f) => normalizeTransportText(f.title)).join(JOIN),
        fastlink_descriptions: fl.map((f) => normalizeTransportText(f.desc || f.description_1 || '')).join(JOIN),
        fastlink_urls: fl.map((f) => collapseWhitespace(f.url)).join(JOIN),
        callouts: (ad.callouts || []).map((c) => normalizeTransportText(c.text)).join(JOIN),
        group_negatives: ai === 0 ? groupNeg : '',
        phrase_bid: '',
      });
    }

    for (const kw of group.keywords) {
      rows.push({
        transport_row_type: TRANSPORT_ROW_KEYWORD,
        group_name: groupName,
        group_number: groupNumber,
        group_additional_ad: '',
        phrase: normalizeTransportText(kw.ad_phrase),
        keyword_status: '',
        headline_1: '',
        headline_2: '',
        description: '',
        landing_url: '',
        display_url: '',
        ad_status: '',
        ad_type_transport: '',
        geo_region: GEO_REGION,
        fastlink_titles: '',
        fastlink_descriptions: '',
        fastlink_urls: '',
        callouts: '',
        group_negatives: '',
        phrase_bid: kw.final_bid,
      });
    }
  }

  return rows;
}

async function main() {
  if (!fs.existsSync(DATASET_PATH)) {
    console.error('Run run-full-production.mjs first');
    process.exit(1);
  }
  if (!fs.existsSync(TEMPLATE)) {
    console.error('Template not found:', TEMPLATE);
    process.exit(1);
  }

  const dataset = loadJson(DATASET_PATH);
  const headerMapFields = loadHeaderMap(HEADER_MAP);
  const columns = resolveColumns(headerMapFields);
  const fillRows = buildFillRows(dataset);
  const metadataPatches = buildMetadataPatches(dataset);

  fs.mkdirSync(path.dirname(OUTPUT), { recursive: true });

  const sheet1Original = readZipEntryUtf8(TEMPLATE, 'xl/worksheets/sheet1.xml');
  const sheet1Extended = extendSheetForExport(sheet1Original, fillRows.length, DATA_START_ROW);
  const { sheetXml: patchedSheet1, lastExportRow } = patchSheet1DataRows(sheet1Extended, fillRows, columns, {
    dataStartRow: DATA_START_ROW,
    headerMapFields: { fields: headerMapFields },
    newCampaignMode: true,
    enableCleanup: true,
    rowRemovalMode: true,
    metadataPatches,
    enableMetadata: true,
  });

  patchSheet1InWorkbook(TEMPLATE, OUTPUT, patchedSheet1);
  const preserve = verifyPreservedEntries(TEMPLATE, OUTPUT);

  const integrity = await runIntegrityCheck(OUTPUT, {
    sheetName: 'Тексты',
    dataStartRow: DATA_START_ROW,
    rowsWritten: fillRows.length,
    mappedColumns: new Set(Object.values(columns)),
    columnsByKey: columns,
    probeLogicalKeys: ['groups.group_name', 'keywords.phrase', 'ads.headline_1'],
    probeLogicalKeysMode: 'any-row',
  });

  const result = {
    ok: integrity.ok && preserve.sheet1Changed && !preserve.sharedStringsIntroduced,
    output: OUTPUT,
    fill_rows: fillRows.length,
    groups: dataset.groups.length,
    keywords: dataset.keywords.length,
    ads: dataset.ads.length,
    last_export_row: lastExportRow,
    integrity,
    preserve_summary: {
      sheet1Changed: preserve.sheet1Changed,
      sharedStringsIntroduced: preserve.sharedStringsIntroduced,
    },
  };

  fs.writeFileSync(
    path.join(ROOT, 'production/validation/export-run-result-v1.json'),
    JSON.stringify(result, null, 2)
  );

  console.log(JSON.stringify(result, null, 2));
  if (!result.ok) process.exit(1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
