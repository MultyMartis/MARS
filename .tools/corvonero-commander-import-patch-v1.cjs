#!/usr/bin/env node
"use strict";
/**
 * Corvonero Commander import-candidate generator — sheet1 ZIP patch only.
 * Forks triumph-manipulator-commander-template-v1.xlsx; does NOT modify template source.
 *
 * C2c hold: Path rewrite does not authorize Commander import, Direct launch,
 * account mutation, advertising start, or Storage export execution.
 */

const fs = require("fs");
const path = require("path");

const REPO_ROOT = "X:\\AI MARS";
const STORAGE_ROOT = "X:\\AI MARS STORAGE";

const TRIUMPH_CLI = path.resolve(
  __dirname,
  "../projects/orca/ppc/triumph-manipulator/tools/exporter-cli"
);

const { patchSheet1DataRows } = require(path.join(TRIUMPH_CLI, "sheet1-xml-builder"));
const { patchSheet1InWorkbook, readZipEntryUtf8, verifyPreservedEntries } = require(
  path.join(TRIUMPH_CLI, "xlsx-zip-patch")
);
const { loadHeaderMap } = require(path.join(TRIUMPH_CLI, "workbook-writer"));
const { runIntegrityCheck } = require(path.join(TRIUMPH_CLI, "xlsx-integrity-check"));
const { TRANSPORT_ROW_AD, TRANSPORT_ROW_KEYWORD } = require(path.join(TRIUMPH_CLI, "mapping"));

const DATA_START_ROW = 16;
const SEARCH_AD_TYPE = "Текстово-графическое";

function extractRowXml(sheetXml, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheetXml.match(re);
  return m ? m[0] : null;
}

function cloneRowXml(rowXml, fromRow, toRow) {
  let s = rowXml.replace(new RegExp(`r="${fromRow}"`, "g"), `r="${toRow}"`);
  s = s.replace(new RegExp(`([A-Z]{1,3})${fromRow}(?![0-9])`, "g"), `$1${toRow}`);
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

  const sheetDataClose = sheetXml.lastIndexOf("</sheetData>");
  if (sheetDataClose < 0) throw new Error("sheetData close tag missing");

  let next = `${sheetXml.slice(0, sheetDataClose)}${insertRows.join("")}${sheetXml.slice(sheetDataClose)}`;

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
    "groups.group_name",
    "groups.group_number",
    "keywords.phrase",
    "ads.headline_1",
    "ads.headline_2",
    "ads.description",
    "ads.landing_url",
    "ads.display_url",
    "ads.ad_status",
    "keywords.status",
    "extensions.fastlink_titles",
    "extensions.fastlink_descriptions",
    "extensions.fastlink_urls",
    "extensions.callouts",
    "keywords.bid",
    "groups.group_negatives",
    "ads.ad_type",
    "geo.region",
    "ads.group_additional_ad",
  ];
  const columns = {};
  for (const key of keys) {
    const spec = headerMapFields[key];
    if (spec?.column) columns[key] = spec.column;
  }
  return columns;
}

function resolveEntityIdColumns(headerMapFields) {
  const keys = ["groups.group_id", "keywords.phrase_id", "ads.ad_id"];
  const columns = {};
  for (const key of keys) {
    const spec = headerMapFields[key];
    if (spec?.column) columns[key] = spec.column;
  }
  return columns;
}

function resolveWritableColumns(headerMapFields) {
  const keys = [
    "groups.group_name",
    "groups.group_number",
    "keywords.phrase",
    "ads.headline_1",
    "ads.headline_2",
    "ads.description",
    "ads.landing_url",
    "ads.display_url",
    "ads.ad_status",
    "keywords.status",
    "extensions.fastlink_titles",
    "extensions.fastlink_descriptions",
    "extensions.fastlink_urls",
    "extensions.callouts",
    "groups.group_negatives",
    "geo.region",
    "ads.image",
    "ads.creative",
    "ads.creative_moderation_status",
  ];
  const columns = {};
  for (const key of keys) {
    const spec = headerMapFields[key];
    if (spec?.column) columns[key] = spec.column;
  }
  return columns;
}

function buildFillRows(payload) {
  return payload.rows.map((row) => {
    const isAd = row.row_type === "AD";
    const isKw = row.row_type === "KEYWORD";
    return {
      transport_row_type: isAd ? TRANSPORT_ROW_AD : TRANSPORT_ROW_KEYWORD,
      group_name: row.group_name ?? "",
      group_number: String(row.group_number ?? ""),
      group_additional_ad: row.group_additional_ad ?? "",
      phrase: isKw ? row.phrase ?? "" : "",
      keyword_status: isKw ? row.phrase_status ?? "" : "",
      headline_1: isAd ? row.headline_1 ?? "" : "",
      headline_2: isAd ? row.headline_2 ?? "" : "",
      description: isAd ? row.text ?? "" : "",
      landing_url: isAd ? row.landing_url ?? "" : "",
      display_url: isAd ? row.display_path ?? "" : "",
      ad_status: isAd ? row.ad_status ?? "" : "",
      ad_type_transport: isAd ? SEARCH_AD_TYPE : "",
      geo_region: row.region ?? payload.geo_region,
      fastlink_titles: "",
      fastlink_descriptions: "",
      fastlink_urls: "",
      callouts: isAd ? row.callouts ?? "" : "",
      group_negatives: isAd ? row.group_negatives ?? "" : "",
      phrase_bid: isKw ? String(row.bid ?? "") : "",
    };
  });
}

async function main() {
  if (process.env.CORVONERO_OPERATOR_GATE !== "APPROVED") {
    console.error(
      "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This script is not safe for casual execution."
    );
    process.exit(1);
  }

  const payloadPath = process.argv[2];
  const templatePath = process.argv[3];
  const outputPath = process.argv[4];
  const headerMapPath = process.argv[5];

  if (!payloadPath || !templatePath || !outputPath || !headerMapPath) {
    console.error(
      "Usage: node corvonero-commander-import-patch-v1.cjs <payload.json> <template.xlsx> <output.xlsx> <header-map.json>"
    );
    process.exit(1);
  }

  const payload = JSON.parse(fs.readFileSync(payloadPath, "utf8"));
  const headerMapData = loadHeaderMap(headerMapPath);
  const headerMapFields = headerMapData.fields || headerMapData;
  const columns = resolveColumns(headerMapFields);
  const entityIdColumns = resolveEntityIdColumns(headerMapFields);
  const writableColumns = resolveWritableColumns(headerMapFields);
  const fillRows = buildFillRows(payload);
  const metadataPatches = payload.metadata_patches || {};

  const sheet1Original = readZipEntryUtf8(templatePath, "xl/worksheets/sheet1.xml");
  const extendedSheet = extendSheetForExport(sheet1Original, fillRows.length, DATA_START_ROW);
  const { sheetXml: patchedSheet1 } = patchSheet1DataRows(extendedSheet, fillRows, columns, {
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

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  patchSheet1InWorkbook(templatePath, outputPath, patchedSheet1);
  const preserve = verifyPreservedEntries(templatePath, outputPath);

  if (preserve.sharedStringsIntroduced) {
    throw new Error("sharedStrings.xml introduced — forbidden");
  }

  const integrity = await runIntegrityCheck(outputPath, {
    sheetName: "Тексты",
    dataStartRow: DATA_START_ROW,
    rowsWritten: fillRows.length,
    mappedColumns: Object.values(columns),
    columnsByKey: columns,
    probeLogicalKeys: ["groups.group_name", "keywords.phrase", "ads.headline_1"],
    probeLogicalKeysMode: "any-row",
  });

  const result = {
    ok: integrity.ok,
    output_path: outputPath,
    rows_written: fillRows.length,
    integrity,
    preserve_summary: {
      sheet1Changed: preserve.sheet1Changed,
      sharedStringsIntroduced: preserve.sharedStringsIntroduced,
    },
  };

  console.log(JSON.stringify(result, null, 2));
  if (!integrity.ok) process.exit(2);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
