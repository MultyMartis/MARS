"use strict";

const ExcelJS = require("exceljs");
const fs = require("fs");
const path = require("path");

const DEFAULT_HEADER_MAP_PATH = path.join(__dirname, "commander-header-map-v0.json");

/** Rows 1–15 on Тексты are template metadata/headers — never write below this in template-fill. */
const TEMPLATE_METADATA_ROW_LIMIT = 15;

/**
 * Optional logical-key → template header translation.
 * Loads commander-header-map-v0.json when present; does not change sheet layout in v0.
 */
function loadHeaderMap(mapPath) {
  const resolved = mapPath || DEFAULT_HEADER_MAP_PATH;
  if (!fs.existsSync(resolved)) return null;
  try {
    const data = JSON.parse(fs.readFileSync(resolved, "utf8"));
    return data.fields || data;
  } catch {
    return null;
  }
}

function translateHeaders(logicalHeaders, headerMap, entityPrefix) {
  if (!headerMap) return logicalHeaders;
  return logicalHeaders.map((h) => {
    const key = entityPrefix ? `${entityPrefix}.${h}` : h;
    const spec = headerMap[key];
    if (
      spec &&
      spec.header &&
      spec.status !== "unsupported" &&
      spec.status !== "unknown"
    ) {
      return spec.header;
    }
    return h;
  });
}

/**
 * Safe scalar for XLSX cell write. Returns null to skip (undefined/null/invalid).
 * Never returns objects, NaN, or broken ref strings.
 */
function sanitizeCellValue(value) {
  if (value === undefined || value === null) return null;

  if (typeof value === "number") {
    if (Number.isNaN(value) || !Number.isFinite(value)) return null;
    return value;
  }

  if (typeof value === "boolean") {
    return value ? "1" : "0";
  }

  if (typeof value === "object") {
    return null;
  }

  const str = String(value).trim();
  if (!str.length) return null;
  if (str === "NaN" || str === "[object Object]") return null;
  if (/^#REF!$/i.test(str)) return null;

  return str;
}

function isVerifiedDataColumn(col, allowedColumns) {
  if (col == null || !Number.isInteger(col) || col < 1) return false;
  return allowedColumns.has(col);
}

function assertDataRow(rowNum, dataStartRow) {
  if (rowNum < dataStartRow) {
    const err = new Error(
      `Refusing to write row ${rowNum}: metadata/header rows must remain untouched (data starts at ${dataStartRow})`
    );
    err.code = "METADATA_ROW_TOUCH";
    throw err;
  }
}

/**
 * Fail loudly if target is a non-master cell inside a merge range.
 */
function assertCellNotMergedSlave(worksheet, rowNum, col) {
  const cell = worksheet.getCell(rowNum, col);
  if (!cell.isMerged) return;

  const master = cell.master;
  if (master && master.address && cell.address !== master.address) {
    const err = new Error(
      `Refusing to write merged slave cell ${cell.address} (master ${master.address}) row ${rowNum} col ${col}`
    );
    err.code = "MERGED_CELL_WRITE";
    throw err;
  }
}

/**
 * Write one scalar into an exact cell; preserves existing type when cell already has a value type.
 */
function safeSetCell(worksheet, rowNum, col, value, options = {}) {
  const { dataStartRow = 16, allowedColumns } = options;

  assertDataRow(rowNum, dataStartRow);

  if (!isVerifiedDataColumn(col, allowedColumns)) {
    const err = new Error(`Column ${col} is not in verified mapped column set`);
    err.code = "UNVERIFIED_COLUMN_WRITE";
    throw err;
  }

  assertCellNotMergedSlave(worksheet, rowNum, col);

  const sanitized = sanitizeCellValue(value);
  if (sanitized === null) return false;

  const cell = worksheet.getCell(rowNum, col);
  const existing = cell.value;

  if (existing != null && typeof existing === "object" && !Array.isArray(existing)) {
    if (existing.formula || existing.sharedFormula) {
      const err = new Error(
        `Refusing to overwrite formula cell ${cell.address} row ${rowNum} col ${col}`
      );
      err.code = "FORMULA_CELL_TOUCH";
      throw err;
    }
  }

  if (typeof sanitized === "number") {
    cell.value = sanitized;
  } else {
    cell.value = sanitized;
  }

  return true;
}

const SHEET_DEFS = [
  {
    name: "campaigns",
    headers: [
      "campaign_id",
      "campaign_name",
      "campaign_type",
      "primary_region",
      "strategy_label",
      "bid_intent",
    ],
    rowKey: "campaigns",
  },
  {
    name: "groups",
    headers: [
      "campaign_id",
      "campaign_name",
      "group_id",
      "group_name",
      "final_url",
    ],
    rowKey: "groups",
  },
  {
    name: "keywords",
    headers: [
      "campaign_id",
      "campaign_name",
      "group_id",
      "group_name",
      "phrase",
      "match_type",
      "status",
      "is_primary",
    ],
    rowKey: "keywords",
  },
  {
    name: "ads",
    headers: [
      "campaign_id",
      "campaign_name",
      "group_id",
      "group_name",
      "ad_id",
      "headline_1",
      "headline_2",
      "description",
      "display_url_domain",
      "display_url_path_1",
      "display_url_path_2",
      "landing_url",
      "ad_status",
    ],
    rowKey: "ads",
  },
  {
    name: "extensions",
    headers: [
      "extension_type",
      "campaign_id",
      "campaign_name",
      "group_id",
      "group_name",
      "ad_id",
      "title",
      "url",
      "description_1",
      "text",
    ],
    rowKey: "extensions",
  },
];

const SHEET_ENTITY_PREFIX = {
  campaigns: "campaigns",
  groups: "groups",
  keywords: "keywords",
  ads: "ads",
  extensions: "extensions",
};

function writeSheet(workbook, def, rows, headerMap) {
  const sheet = workbook.addWorksheet(def.name);
  const prefix = SHEET_ENTITY_PREFIX[def.name];
  const outHeaders = translateHeaders(def.headers, headerMap, prefix);
  sheet.addRow(outHeaders);
  const headerRow = sheet.getRow(1);
  headerRow.font = { bold: true };

  for (const row of rows) {
    const values = def.headers.map((h) => {
      const v = row[h];
      const sanitized = sanitizeCellValue(v);
      return sanitized === null ? "" : sanitized;
    });
    sheet.addRow(values);
  }

  sheet.views = [{ state: "frozen", ySplit: 1 }];
}

async function writeWorkbook(mapped, outputPath, options = {}) {
  const workbook = new ExcelJS.Workbook();
  workbook.creator = "ORCA Exporter Prototype v0";
  workbook.created = new Date();

  const headerMap =
    options.headerMap === false
      ? null
      : loadHeaderMap(options.headerMapPath);

  const readme = workbook.addWorksheet("_meta");
  readme.addRow(["key", "value"]);
  readme.addRow(["exporter_version", mapped.meta.exporter_version]);
  readme.addRow(["document_id", mapped.meta.document_id]);
  readme.addRow(["schema_version", mapped.meta.schema_version]);
  readme.addRow(["generated_at", mapped.meta.generated_at]);
  readme.addRow([
    "disclaimer",
    "Transport draft — NOT full Commander fidelity. Human review required.",
  ]);
  readme.addRow([
    "header_map_loaded",
    headerMap ? "yes (commander-header-map-v0)" : "no",
  ]);

  for (const def of SHEET_DEFS) {
    writeSheet(workbook, def, mapped[def.rowKey] || [], headerMap);
  }

  const dir = path.dirname(outputPath);
  fs.mkdirSync(dir, { recursive: true });
  await workbook.xlsx.writeFile(outputPath);

  return {
    outputPath,
    counts: mapped.counts,
  };
}

module.exports = {
  writeWorkbook,
  loadHeaderMap,
  translateHeaders,
  sanitizeCellValue,
  safeSetCell,
  assertDataRow,
  assertCellNotMergedSlave,
  isVerifiedDataColumn,
  TEMPLATE_METADATA_ROW_LIMIT,
  SHEET_DEFS,
};
